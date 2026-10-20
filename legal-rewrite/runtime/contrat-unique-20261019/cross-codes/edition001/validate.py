from pathlib import Path
import json,sqlite3,hashlib,sys,re
P=Path(__file__).resolve().parent
B=P.parents[3];sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from ingest import source_notes
s=json.loads((P/'source.json').read_text());a=json.loads((P/'answer.json').read_text());validate_answer(a,s)
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True)
checks=[]
for x,y in zip(s,a):
 k=x['code_id'],x['source_id'];assert c.execute('select content_xml,source_sha256 from articles where code_id=? and id=?',k).fetchone()==(x['source_xml'],x['source_sha256']);assert source_notes(c,*k)==x['source_notes_xml'];d=c.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',k).fetchone();prev=x['previous_draft'];assert d==((prev['source_sha256'],prev['proposed_xml'])if prev else None)
 if prev:assert hashlib.sha256(prev['proposed_xml'].encode()).hexdigest()==x['current_beforeimage_sha256']
 old=(prev or{}).get('proposed_xml',x['source_xml']);oldp=re.findall(r'<p[^>]*>.*?</p>',old,flags=re.S);newp=re.findall(r'<p[^>]*>.*?</p>',y['proposed_xml'],flags=re.S);diffs=[i+1 for i,(v,w)in enumerate(zip(oldp,newp))if v!=w]
 if x['number']in ['220 sexies','220 quaterdecies']:assert diffs==[2] and len(oldp)==len(newp)
 if x['number']=='R133-14':assert len(diffs)==2 and len(oldp)==len(newp)
 checks.append({'number':x['number'],'source_and_notes_match':True,'beforeimage_matches':True,'paragraphs_before':len(oldp),'paragraphs_after':len(newp),'changed_paragraph_positions':diffs,'appended_paragraphs':max(0,len(newp)-len(oldp)),'benefit_review_characters':len(y['benefit_review'])})
r={'validation':'passed','articles':len(a),'source_sha256':hashlib.sha256((P/'source.json').read_bytes()).hexdigest(),'answer_sha256':hashlib.sha256((P/'answer.json').read_bytes()).hexdigest(),'checks':checks,'db_or_publication_modified':False}
(P/'validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},ensure_ascii=False,indent=2))
