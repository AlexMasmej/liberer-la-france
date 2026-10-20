from pathlib import Path
import json,hashlib,sqlite3,shutil,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
J=L/'runtime/exhaustive/jobs/review-travail-LEGIARTI000026566046-00005'
for n in ['source.json','answer.json','reference-targets.json','policy.json','coordination.json','policy-fingerprint.json','result.json']:
 shutil.copyfile(J/n,P/(n.replace('.json','.capture.json')))
for n in ['policy-coordinations.json','site-summaries.json']:shutil.copyfile(L/n,P/n)
s=json.loads((P/'source.capture.json').read_text());a=json.loads((P/'answer.capture.json').read_text());refs=json.loads((P/'reference-targets.capture.json').read_text());keys={(x['code_id'],x['source_id'])for x in s};keys|={(x['code_id'],x['source_id'])for x in refs['targets'].values()}
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
for number in ['L1234-3','R1234-1','R1234-2','R1234-4']:
 rows=db.execute('select id from articles where code_id=? and number=? order by valid_from desc',('LEGITEXT000006072050',number)).fetchall();assert rows;keys.add(('LEGITEXT000006072050',rows[0]['id']))
records=[]
for c,i in sorted(keys):
 r=dict(db.execute('select * from articles where code_id=? and id=?',(c,i)).fetchone());d=db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone();raw=db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",(c,i)).fetchone()
 records.append(dict(code_id=c,source_id=i,number=r['number'],source_sha256=r['source_sha256'],source_xml=r['content_xml'],source_body_sha256=sha(r['content_xml']),source_notes_xml=source_notes(db,c,i),source_notes_sha256=sha(source_notes(db,c,i)),current_draft=dict(d)if d else None,raw_document_sha256=sha(raw['xml']),raw_document_official_sha256=raw['sha256']))
db.rollback();db.close();(P/'current-snapshot.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
checks=[];by={(r['code_id'],r['source_id']):r for r in records}
for x,y in zip(s,a):
 r=by[x['code_id'],x['source_id']];checks.append(dict(number=x['number'],source_id=x['source_id'],source_same=r['source_sha256']==x['source_sha256'],body_same=r['source_xml']==x['source_xml'],notes_same=r['source_notes_xml']==x['source_notes_xml'],accepted_proposal_same=r['current_draft']['proposed_xml']==y['proposed_xml'],status_same=r['current_draft']['status']==y['status']))
changes=[dict(number=t['number'],capture_view_sha=t['view_sha256'],current_proposed_sha256=sha(by[t['code_id'],t['source_id']]['current_draft']['proposed_xml'])if by[t['code_id'],t['source_id']]['current_draft']else None)for t in refs['targets'].values()if by[t['code_id'],t['source_id']]['current_draft']and by[t['code_id'],t['source_id']]['current_draft']['proposed_xml']!=t.get('proposed_xml')]
report=dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_only_transaction='mode=ro BEGIN',job=J.name,source_count=len(s),whole_current_records=len(records),policy_semantically_identical=json.loads((P/'coordination.capture.json').read_text())==json.loads((P/'policy-coordinations.json').read_text()),policy_sha256={n:sha((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},checks=checks,all_candidate_guards_match=all(all(x[k]for k in ['source_same','body_same','notes_same','accepted_proposal_same','status_same'])for x in checks),changed_targets_since_job_capture=changes,raw_source_documents_valid=all(x['raw_document_sha256']==x['raw_document_official_sha256']==x['source_sha256']for x in records),scope='Ce seul lot de12 ; les autres lots ne sont pas certifiés. Captures entières pour revue humaine ; ni certificat juridique ni changement actif.')
(P/'capture.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
