from pathlib import Path
import sqlite3,json,hashlib,sys
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
scope={'securite-sociale':{'L136-5','L161-22','L161-22-1-5','L315-1','L433-1','L932-41','R243-26','R752-20','D133-13-4','D241-10','D433-5'},'impots-annexe-3':{'49 Q'}}
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN');rows=[]
for slug,nums in scope.items():
    for p in json.loads((B.parent/'sites/liberer-la-retraite/dist/corpus'/(slug+'.json')).read_text()):
        if p['number']not in nums:continue
        key=p['code_id'],p['source_id'];x=dict(c.execute('select * from articles where code_id=? and id=?',key).fetchone());raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw
        x['source_id']=x.pop('id');x['source_xml']=x.pop('content_xml');x['source_notes_xml']=source_notes(c,*key);x['source_document_xml']=raw;x['source_document_sha256']=sha(raw);assert x['source_sha256']==sha(raw);x['source_body_sha256']=sha(x['source_xml']);x['source_notes_sha256']=sha(x['source_notes_xml']);d=c.execute('select * from drafts where code_id=? and source_id=?',key).fetchone();x['previous_draft']=dict(d)if d else None;x['current_beforeimage_sha256']=sha(d['proposed_xml'])if d else None;x['benefit_check_required']=True;x['slug']=slug;x['source_url']='https://www.legifrance.gouv.fr/codes/article_lc/'+x['source_id'];rows.append(x)
c.rollback();c.close();assert len(rows)==12
(P/'audited-source.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'number':x['number'],'source_characters':len(x['source_xml']),'notes_characters':len(x['source_notes_xml']),'previous_draft_characters':len(x['previous_draft']['proposed_xml'])if x['previous_draft']else 0}for x in rows],indent=2))
