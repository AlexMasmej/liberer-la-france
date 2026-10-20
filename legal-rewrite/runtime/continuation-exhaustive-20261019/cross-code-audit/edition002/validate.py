from pathlib import Path
import json,sqlite3,hashlib,sys,re,xml.etree.ElementTree as E
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
s=json.loads((P/'source.json').read_text());a=json.loads((P/'answer.json').read_text());validate_answer(a,s)
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.execute('BEGIN');checks=[];conflicts=[]
for x,y in zip(s,a):
    k=x['code_id'],x['source_id'];current=c.execute('select content_xml,source_sha256 from articles where code_id=? and id=?',k).fetchone();assert current==(x['source_xml'],x['source_sha256']);assert source_notes(c,*k)==x['source_notes_xml'];raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',k).fetchone()[0];assert sha(raw)==x['source_document_sha256']==x['source_sha256'];assert sha(x['source_xml'])==x['source_body_sha256'];assert sha(x['source_notes_xml'])==x['source_notes_sha256'];d=c.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',k).fetchone();prev=x['previous_draft'];guard=d==((prev['source_sha256'],prev['proposed_xml'])if prev else None)
    if not guard:conflicts.append({'number':x['number'],'source_id':x['source_id'],'current_proposed_sha256':sha(d[1])if d else None,'captured_beforeimage_sha256':x['current_beforeimage_sha256']})
    old=(prev or{}).get('proposed_xml')or x['source_xml'];op=re.findall(r'<p[^>]*>.*?</p>',old,re.S);np=re.findall(r'<p[^>]*>.*?</p>',y['proposed_xml'],re.S)
    # Preserve every source/prior table and all table cells exactly.
    oldtables=re.findall(r'<table\b.*?</table>',re.sub(r'\s(?:align|border)="[^"]*"','',old),re.S);newtables=re.findall(r'<table\b.*?</table>',y['proposed_xml'],re.S);assert oldtables==newtables
    if x['number']=='39'and x['slug']=='impots-annexe-3':
        assert all(p in y['proposed_xml']for p in op if 'CVAE' in p or 'réutilise' in p)
    if x['number']=='204 H':assert len(oldtables)==len(newtables)==3
    if x['number']in ['L767-1','L135-9']:assert 'droit public' in y['proposed_xml']
    checks.append({'number':x['number'],'slug':x['slug'],'source_id':x['source_id'],'canonical_source_notes_document_match':True,'draft_guard_matches':guard,'all_tables_preserved_exactly':True,'paragraphs_before':len(op),'paragraphs_after':len(np),'proposed_sha256':sha(y['proposed_xml'])})
c.rollback();c.close()
r={'validation_structure':'passed','legal_review_is_separate':True,'source_sha256':sha((P/'source.json').read_bytes()),'answer_sha256':sha((P/'answer.json').read_bytes()),'articles':len(a),'checks':checks,'conflicts':conflicts,'database_modified':False,'published':False}
(P/'validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},ensure_ascii=False,indent=2))
