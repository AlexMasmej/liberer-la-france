import json, re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[]
    def handle_data(self,d):self.parts.append(d)
def plain(s):
    p=Text();p.feed(s);return ' '.join(' '.join(p.parts).split())
def nums(s):
    return Counter(re.findall(r'\d+(?:[.,-]\d+)*',plain(s)))
def refs(s):
    return Counter(re.findall(r'\bL\.\s*(\d+(?:-\d+)+)',plain(s)))
def markers(s):
    root=ET.fromstring('<root>'+s+'</root>')
    return [re.match(r'^(?:[IVX]+\.\s*-|\d+°|[a-z]\))', ''.join(p.itertext()).strip()).group(0).replace(' ','') for p in root.findall('p') if re.match(r'^(?:[IVX]+\.\s*-|\d+°|[a-z]\))', ''.join(p.itertext()).strip())]
source=json.loads(Path('source.json').read_text())
answer=json.loads(Path('answer.json').read_text())
assert len(source)==len(answer)==24
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
for s,a in zip(source,answer):
    assert set(a)==set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())
    assert all(a[k]==s[k] for k in ['code_id','source_id','source_sha256','number'])
    assert a['status']=='rewrite_draft'
    assert a['reason'] and a['review_notes']
    assert plain(a['proposed_xml']) != plain(s['source_xml'])
    root=ET.fromstring('<root>'+a['proposed_xml']+'</root>')
    for e in root.iter():
        assert e.tag=='root' or e.tag in allowed
        for k,v in e.attrib.items():assert k in ['rowspan','colspan'] and v.isdigit()
    n1,n2=nums(s['source_xml']),nums(a['proposed_xml'])
    r1,r2=refs(s['source_xml']),refs(a['proposed_xml'])
    # Extra repeated internal paragraph identifiers may be used to make references explicit.
    print(a['number'], 'p',s['source_xml'].count('<p>'),len(root.findall('p')),'chars',len(s['source_xml']),len(a['proposed_xml']))
    if n1!=n2:print('  NUMBERS:', 'removed',dict(n1-n2),'added',dict(n2-n1))
    if r1!=r2:print('  REFERENCES:',dict(r1-r2),dict(r2-r1))
    try:
        if markers(s['source_xml'])!=markers(a['proposed_xml']):print('  MARKERS:',markers(s['source_xml']),markers(a['proposed_xml']))
    except ET.ParseError as e:print('  SOURCE PARSER:',e)
    sr=ET.fromstring('<root>'+s['source_xml']+'</root>')
    for tag in ['table','tr','td','th']:
        assert len(sr.findall('.//'+tag))==len(root.findall('.//'+tag)), (a['number'],tag)
    if sr.findall('.//table'):
        assert [[plain(ET.tostring(c,encoding='unicode')) for c in row] for row in sr.findall('.//tr')]==[[plain(ET.tostring(c,encoding='unicode')) for c in row] for row in root.findall('.//tr')]
print('Validation structurelle et comparaison du tableau : OK')
