import json, pathlib, hashlib, sqlite3, sys, datetime
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]))
from run_exhaustive import validate_answer
from ingest import source_notes

P=pathlib.Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
s=json.loads((P/'source.json').read_text())
a=json.loads((P/'answer.json').read_text())
b=json.loads((P/'beforeimages.json').read_text())
validate_answer(a,s)
c=sqlite3.connect('file:'+str(P.resolve().parents[2]/'corpus.sqlite')+'?mode=ro',uri=True)
c.row_factory=sqlite3.Row
guards=[]
for x,y,z in zip(s,a,b):
    art=c.execute('select * from articles where code_id=? and id=?',(x['code_id'],x['source_id'])).fetchone()
    d=c.execute('select * from drafts where code_id=? and source_id=?',(x['code_id'],x['source_id'])).fetchone()
    current=dict(d) if d else None
    g={k:x[k] for k in ('code_id','source_id','number','source_sha256')}
    g.update(source_unchanged=art['source_sha256']==x['source_sha256'] and art['content_xml']==x['source_xml'],notes_unchanged=source_notes(c,x['code_id'],x['source_id'])==x['source_notes_xml'],draft_unchanged=current==z['draft'],expected_draft=z['draft'],current_draft=current,proposed_sha256=sha(y['proposed_xml'].encode()))
    assert all(g[k] for k in ('source_unchanged','notes_unchanged','draft_unchanged')),x['number']
    assert len(y['benefit_review'])>=100,x['number']
    guards.append(g)
checks={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'article_count':len(a),'validate_answer':'passed','all_source_content_and_notes_unchanged':True,'all_expected_drafts_absent_and_still_absent':all(x['current_draft'] is None for x in guards),'benefit_review_minimum':min(len(x['benefit_review']) for x in a),'normative_reductions':[x['number'] for x in a if x.get('change_type')=='normative_reduction'],'full_repeals':[],'answer_sha256':sha((P/'answer.json').read_bytes()),'source_file_sha256':sha((P/'source.json').read_bytes()),'legal_validation_claimed':False,'registered_or_published':False}
for name,data in [('guards.json',guards),('checks.json',checks)]:
    t=P/(name+'.tmp');t.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');t.replace(P/name)
print(json.dumps(checks,ensure_ascii=False,indent=2))
