import json, re, collections, xml.etree.ElementTree as ET
from pathlib import Path
s=json.loads(Path('source.json').read_text())
a=json.loads(Path('answer.json').read_text())
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
fields=set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())
assert len(s)==len(a)==24
assert len({x['source_id'] for x in a})==24

def root(xml): return ET.fromstring('<root>'+xml+'</root>')
def txt(xml): return ' '.join(root(xml).itertext())
def tokens(xml): return collections.Counter(re.findall(r'\d+(?:[,.]\d+)?',txt(xml)))
def cells(t): return [[re.sub(r'\s+',' ',''.join(c.itertext())).strip() for c in row] for row in t.findall('.//tr')]
report=[]
for x,y in zip(s,a):
 assert set(y)==fields
 for k in ['code_id','source_id','source_sha256','number']: assert x[k]==y[k],(x['number'],k)
 assert y['status']=='rewrite_draft'
 assert y['reason'] and y['review_notes']
 r=root(y['proposed_xml'])
 for n in r.iter():
  if n is r:continue
  assert n.tag in allowed,(x['number'],n.tag)
  assert all(k in ['rowspan','colspan'] and re.fullmatch('[0-9]+',v) for k,v in n.attrib.items()),(x['number'],n.attrib)
 assert txt(x['source_xml']).strip()!=txt(y['proposed_xml']).strip(),x['number']
 sr=root(x['source_xml'])
 st,pt=sr.findall('.//table'),r.findall('.//table')
 assert len(st)==len(pt),(x['number'],'tables')
 for c,d in zip(st,pt):
  sc=cells(c);pc=cells(d)
  sc=[[v.replace('1914 et antér','1914 et années antérieures') for v in row] for row in sc]
  assert sc==pc,(x['number'],'table cells')
 diffs={'removed':dict(tokens(x['source_xml'])-tokens(y['proposed_xml'])),'added':dict(tokens(y['proposed_xml'])-tokens(x['source_xml']))}
 item={'number':x['number'],'source_chars':len(x['source_xml']),'proposed_chars':len(y['proposed_xml']),'source_paragraphs':len(sr.findall('p')),'proposed_paragraphs':len(r.findall('p')),'tables':len(pt),'numeric_differences':diffs}
 report.append(item)
 print(json.dumps(item,ensure_ascii=False))
Path('verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('VALIDATION STRUCTURE ET TABLEAUX : OK')
