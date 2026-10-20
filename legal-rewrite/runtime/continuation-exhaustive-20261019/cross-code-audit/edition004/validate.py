from pathlib import Path
import json,sqlite3,hashlib,sys,re
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from run_exhaustive import validate_answer;from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
s=json.loads((P/'source.json').read_text());a=json.loads((P/'answer.json').read_text());validate_answer(a,s)
audited=json.loads((P/'audited-source.json').read_text());c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.execute('BEGIN');checks=[];conflicts=[]
for x in s+audited:
    k=x['code_id'],x['source_id'];assert c.execute('select content_xml,source_sha256 from articles where code_id=? and id=?',k).fetchone()==(x['source_xml'],x['source_sha256']);assert source_notes(c,*k)==x['source_notes_xml'];raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',k).fetchone()[0];assert sha(raw)==x['source_document_sha256'];d=c.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',k).fetchone();prior=x['previous_draft'];expected=(prior['source_sha256'],prior['proposed_xml'])if prior else None
    if x.get('beforeimage_status')=='expected_after_predecessor_registration_not_yet_in_database':
        captured=x['captured_database_draft'];captured=(captured['source_sha256'],captured['proposed_xml'])if captured else None
        valid=d in [captured,expected];state='ready_after_exact_predecessor_registration'if d==expected else'predecessor_still_pending_do_not_register_this_article_yet'
    else:valid=d==expected;state='captured_database_beforeimage_matches'if valid else'concurrent_change'
    if not valid:conflicts.append({'number':x['number'],'source_id':x['source_id'],'database_proposed_sha256':sha(d[1])if d else None})
    checks.append({'number':x['number'],'source_id':x['source_id'],'source_document_and_notes_match':True,'guard_valid_for_declared_stage':valid,'state':state})
for x,y in zip(s,a):
    old=(x['previous_draft']or{}).get('proposed_xml')or x['source_xml']
    assert re.findall(r'<table\b.*?</table>',old,re.S)==re.findall(r'<table\b.*?</table>',y['proposed_xml'],re.S)
    if x['number']=='L241-13':
        op=re.findall(r'<p[^>]*>.*?</p>',old,re.S);np=re.findall(r'<p[^>]*>.*?</p>',y['proposed_xml'],re.S);diff=[i for i,(u,v)in enumerate(zip(op,np))if u!=v];assert len(op)==len(np)and len(diff)==1 and op[diff[0]].startswith('<p>2° Aux salariés auxquels');assert x['expected_predecessor']['proposed_sha256']==sha(old)
    if x['number']=='D241-10':
        op=re.findall(r'<p[^>]*>.*?</p>',old,re.S);np=re.findall(r'<p[^>]*>.*?</p>',y['proposed_xml'],re.S);diff=[i for i,(u,v)in enumerate(zip(op,np))if u!=v];assert len(op)==len(np)and len(diff)==1 and op[diff[0]].startswith('<p>III.-Pour les salariés');assert np[1]==op[1]
c.rollback();c.close()
out={'validation_structure':'passed','source_sha256':sha((P/'source.json').read_bytes()),'answer_sha256':sha((P/'answer.json').read_bytes()),'audited_source_sha256':sha((P/'audited-source.json').read_bytes()),'candidates':3,'initial_complete_article_reviews':12,'additional_complete_sources_reviewed':['L241-13','L1251-54'],'checks':checks,'conflicts':conflicts,'database_modified':False,'requires_ordered_predecessor_registration':True,'publication':False}
(P/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'},ensure_ascii=False,indent=2))
