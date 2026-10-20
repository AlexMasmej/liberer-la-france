import json,pathlib,sqlite3,re
from html.parser import HTMLParser
class P(HTMLParser):
 def __init__(self):super().__init__();self.ps=[];self.cur=[];self.on=False
 def handle_starttag(self,t,a):
  if t=='p':self.cur=[];self.on=True
 def handle_endtag(self,t):
  if t=='p':self.ps.append(''.join(self.cur));self.on=False
 def handle_data(self,d):
  if self.on:self.cur.append(d)
D=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);D.row_factory=sqlite3.Row
p=pathlib.Path(__file__).parent;out=[]
for f in pathlib.Path('sites/liberer-la-retraite/dist/corpus').glob('*.json'):
 a=json.loads(f.read_text())
 if not isinstance(a,list):continue
 for r in a:
  if not isinstance(r,dict) or 'source_id' not in r:continue
  if (f.name=='impots.json' and r['number'] in ['206','209','219','111 bis','221 bis','260']) or (f.name=='construction-habitation.json' and r['number']=='L411-2'):
   c=D.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(r['code_id'],r['source_id'])).fetchone();x=r.copy();x['current_draft']=dict(c) if c else None;out.append(x)
   t=c['proposed_xml'] if c and c['proposed_xml'] else r['source_xml'];y=P();y.feed(t);ps=y.ps
   print('\nARTICLE',r['number'])
   if r['number']=='L411-2':
    for i,v in enumerate(ps,1):print(i,v)
   elif r['number'] in ['111 bis','221 bis','260']:print('\n'.join(ps))
   else:
    run=False
    for txt in ps:
     if re.match(r'^(12\.|XI\.|XII\.|XIII\.|V\.|VI\.)',txt):run=True
     if run:print(txt)
(p/'is-and-benefit-context.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
