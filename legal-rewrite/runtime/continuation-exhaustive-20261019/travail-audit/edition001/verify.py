"""Read-only validation. Does not register, revise or publish any article."""
from pathlib import Path
import datetime, hashlib, json, sqlite3, sys, time

P=Path(__file__).resolve().parent
LEGAL=P.parents[3]
sys.path.insert(0,str(LEGAL))
from ingest import source_notes
from run_exhaustive import validate_answer, mentions_possible_relief

sha=lambda value:hashlib.sha256((value or '').encode()).hexdigest()

def compare_record(record,current_source,current_notes,current_draft):
    errors=[]
    expected=(record['source_xml'],record['source_sha256'])
    if current_source!=expected:errors.append('canonical_source_changed')
    if current_notes!=record['source_notes_xml']:errors.append('official_application_notes_changed')
    prior=record.get('previous_draft')
    expected_draft=(prior['source_sha256'],prior['status'],prior['proposed_xml'],prior['reason'],prior['review_notes']) if prior else None
    if current_draft!=expected_draft:errors.append('prior_draft_changed')
    if prior and sha(prior['proposed_xml'])!=prior['proposed_sha256']:errors.append('corrupt_before_image_guard')
    return errors

def verify():
    sources=json.loads((P/'source.json').read_text())
    dependencies=json.loads((P/'dependency-sources.snapshot.json').read_text())
    answers=json.loads((P/'answer.json').read_text())
    expected=[r|{'benefit_check_required':mentions_possible_relief(r['source_xml'])} for r in sources]
    validate_answer(answers,expected)
    capture=json.loads((P/'capture.json').read_text())
    failures=[];checks=[]
    if hashlib.sha256((LEGAL/'policy-coordinations.json').read_bytes()).hexdigest()!=capture['policy_sha256']:
        failures.append({'kind':'active_policy_changed'})
    db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True)
    db.execute('BEGIN')
    try:
        for record in sources+dependencies:
            key=record['code_id'],record['source_id']
            current_source=db.execute('SELECT content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?',key).fetchone()
            current_notes=source_notes(db,*key)
            current_draft=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
            errors=compare_record(record,current_source,current_notes,current_draft)
            check={'number':record['number'],'code_id':key[0],'source_id':key[1],
                   'role':'correction' if record in sources else 'dependency','source_guard':record['source_sha256'],
                   'prior_proposal_guard':record['previous_draft']['proposed_sha256'] if record.get('previous_draft') else None,
                   'passed':not errors,'errors':errors}
            checks.append(check)
            if errors:failures.append(check)
    finally:db.close()
    # Conservative exclusion of recently started unfinished jobs. Completed jobs
    # are still caught by the exact before-image comparison above.
    corrective_keys={(r['code_id'],r['source_id']) for r in sources}
    for folder in (LEGAL/'runtime/exhaustive/jobs').glob('*travail*'):
        path=folder/'source.json'
        if not path.exists() or (folder/'result.json').exists():continue
        mtimes=[f.stat().st_mtime for f in folder.iterdir() if f.is_file()]
        if not mtimes or time.time()-max(mtimes)>7200:continue
        for row in json.loads(path.read_text()):
            if (row['code_id'],row['source_id']) in corrective_keys:
                failures.append({'kind':'potential_active_job_collision','number':row['number'],'folder':folder.name})
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'articles':len(answers),'dependency_articles':len(dependencies),'checks':checks,'guard_failures':failures,
            'schema_and_whole_article_checks_passed':True,'ready_for_parent_review':not failures,
            'registered':False,'jurist_reviewed':False,'exhaustive_chain_validated':False}
    (P/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False,indent=2))
    return not failures

if __name__=='__main__':raise SystemExit(0 if verify() else 1)
