import json, re, hashlib
from collections import Counter
import xml.etree.ElementTree as ET
from pathlib import Path
s=json.loads(Path('source.json').read_text())
a=json.loads(Path('answer.json').read_text())
assert len(s)==len(a)==24
keys={'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status'}
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())

def text(xml):
 return ' '.join(''.join(ET.fromstring('<div>'+xml+'</div>').itertext()).split())
def paragraphs(xml):
 root=ET.fromstring('<div>'+xml+'</div>')
 if root.findall('p'):
  return [text(ET.tostring(p,encoding='unicode')) for p in root.findall('p')]
 return [re.sub(r'\s+',' ',p).strip() for p in re.split(r'<br\s*/?>',xml) if re.sub(r'\s+',' ',p).strip()]
def digits(xml):
 return re.findall(r'\d+',text(xml))
def cells(xml):
 root=ET.fromstring('<div>'+xml+'</div>')
 return [[(c.tag,{k:v for k,v in c.attrib.items() if k in {'rowspan','colspan'}},text(ET.tostring(c,encoding='unicode'))) for c in r] for r in root.findall('.//tr')]

for src,out in zip(s,a):
 assert set(out)==keys
 for k in ['code_id','source_id','source_sha256','number']:
  assert src[k]==out[k], (src['number'],k)
 assert out['status']=='rewrite_draft'
 assert out['proposed_xml'] and out['reason'] and out['review_notes']
 assert src['source_xml']!=out['proposed_xml']
 root=ET.fromstring('<div>'+out['proposed_xml']+'</div>')
 for n in root.iter():
  assert n.tag in allowed
  for k,v in n.attrib.items():
   assert k in {'rowspan','colspan'} and re.fullmatch(r'[0-9]+',v)
 assert len(paragraphs(src['source_xml']))==len(paragraphs(out['proposed_xml'])), (src['number'],'alinéas')
 assert Counter(digits(src['source_xml']))==Counter(digits(out['proposed_xml'])), (src['number'],'chiffres',digits(src['source_xml']),digits(out['proposed_xml']))
 assert cells(src['source_xml'])==cells(out['proposed_xml']), (src['number'],'tableau')
 print(src['number'],': identifiants, XML, chiffres,',len(paragraphs(out['proposed_xml'])),'alinéas et tableau conformes')
print('Vérifications structurelles terminées : 24/24.')
print('Tableau 52 ter :',len(cells(a[21]['proposed_xml'])),'lignes intégrales.')
print('SHA256 source.json :',hashlib.sha256(Path('source.json').read_bytes()).hexdigest())
