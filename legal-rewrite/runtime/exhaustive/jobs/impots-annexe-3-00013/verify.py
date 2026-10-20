import json,re
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

class Text(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.parts=[]; self.p=[]; self.cur=[]; self.depth=0; self.table=0
 def handle_starttag(self,tag,attrs):
  if tag=='table': self.table+=1
  if tag=='p' and not self.table: self.depth+=1;self.cur=[]
  if tag=='br': self.parts.append(' ')
 def handle_endtag(self,tag):
  if tag=='p' and self.depth:
   self.p.append(''.join(self.cur).strip());self.depth-=1
  if tag=='table':self.table-=1
  self.parts.append(' ')
 def handle_data(self,data):
  self.parts.append(data)
  if self.depth:self.cur.append(data)
def parse(s):
 t=Text();t.feed(s);return t

def nums(s):
 t=''.join(parse(s).parts)
 return Counter(re.sub(r'\s','',m) for m in re.findall(r'\d+(?:[ \u00a0\u202f]\d{3})*(?:,\s*\d+)?',t))

s=json.loads(Path('source.json').read_text());a=json.loads(Path('answer.json').read_text())
assert len(a)==len(s)==15
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
required=set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())
for i,(src,out) in enumerate(zip(s,a)):
 assert set(out)==required,(i,'fields')
 for k in ['code_id','source_id','source_sha256','number']:assert out[k]==src[k],(i,k)
 assert out['status']=='rewrite_draft'
 assert all(isinstance(out[k],str) and out[k] for k in required)
 root=ET.fromstring('<root>'+out['proposed_xml']+'</root>')
 for el in root.iter():
  if el.tag=='root':continue
  assert el.tag in allowed,(i,el.tag)
  for k,v in el.attrib.items(): assert k in ['rowspan','colspan'] and re.fullmatch(r'[0-9]+',v),(i,k,v)
 assert out['proposed_xml']!=src['source_xml']
 sn,on=nums(src['source_xml']),nums(out['proposed_xml'])
 print(i,src['number'],'paragraphes',len(parse(src['source_xml']).p),'->',len(parse(out['proposed_xml']).p),'tables',src['source_xml'].count('<table'),'->',out['proposed_xml'].count('<table'))
 if sn!=on: print(' NUMERALS removed:',dict(sn-on),'added:',dict(on-sn))
print('JSON, identifiants, statuts et XML : contrôles réussis.')
