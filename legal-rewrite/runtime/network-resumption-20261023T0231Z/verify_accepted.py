"""Verify accepted rows in a read-only transaction; never register or invoke."""
from pathlib import Path
import collections, datetime, hashlib, json, sqlite3, sys
HERE=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from ingest import source_notes
from reference_coherence import requirements, key

def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(path):
    raw=path.read_bytes()
    inputs.append({'path':str(path),'sha256':sha(raw),'bytes':len(raw)})
    return json.loads(raw)

inputs=[]
incident=read(HERE/'runtime/network-incident-20261023T0121Z/check.json')
epoch=datetime.datetime.fromisoformat(incident['captured_at_utc']).timestamp()
cohort=read(OUT/'cohort-metrics.json')
accepted=[m for m in cohort if m.get('outcome') in {'accepted','reviewed'} and m['finished_at_unix']>epoch]
prior=read(HERE/'runtime/radical-review-20261019.json')
review_status={(a['code_id'],a['source_id']):a.get('review_status') for a in prior['prior_articles']}
db=sqlite3.connect((HERE/'corpus.sqlite').resolve().as_uri()+'?mode=ro',uri=True,timeout=15)
results=[]
try:
    db.execute('BEGIN')
    for metric in accepted:
        folder=HERE/'runtime/exhaustive/jobs'/metric['job']
        sources=read(folder/'source.json')
        answer=read(folder/'answer.json')
        if metric['kind']=='new':
            complete=read(folder/'registration-complete.json')
            rows=read(Path(complete['batch_path']))
            assert complete['accepted_articles']==metric['articles']
        else:
            rows=answer
        before={(a['code_id'],a['source_id']):a for a in sources}
        assert len(rows)==len(before)==metric['articles']
        article_checks=[]
        for row in rows:
            identity=(row['code_id'],row['source_id']);source=before[identity]
            current=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',identity).fetchone()
            canonical=db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',identity).fetchone()
            values=tuple(row.get(k) for k in ['source_sha256','status','proposed_xml','reason','review_notes'])
            check={'code_id':identity[0],'source_id':identity[1],
                   'all_canonical_draft_fields_match_accepted_row':current==values,
                   'source_hash_body_versions_match':canonical==(source['source_sha256'],source['source_xml'],source.get('valid_from'),source.get('valid_until')),
                   'source_notes_match':source_notes(db,*identity)==source.get('source_notes_xml',''),
                   'prior_review_completed':review_status.get(identity)=='completed' if metric['kind']=='review' else None,
                   'new_batch_impact_certificate_present':bool(row.get('substantive_impact_certificate')) if metric['kind']=='new' else None}
            assert check['all_canonical_draft_fields_match_accepted_row'] and check['source_hash_body_versions_match'] and check['source_notes_match'],check
            if metric['kind']=='review':assert check['prior_review_completed'],check
            article_checks.append(check)
        archives=[]
        if metric['kind']=='review':
            for path in (HERE/'revisions/radical-review').glob('*.json'):
                if not metric['started_at_unix']-5<=path.stat().st_mtime<=metric['finished_at_unix']+5:continue
                content=json.loads(path.read_bytes())
                if {(a['code_id'],a['source_id']) for a in content}!=set(before):continue
                for item in content:
                    old=before[(item['code_id'],item['source_id'])]['previous_draft']
                    assert all(item.get(k)==old.get(k) for k in ['source_sha256','status','proposed_xml','reason','review_notes'])
                archives.append({'path':str(path),'sha256':sha(path.read_bytes()),'articles':len(content),'all_before_image_fields_match':True})
            assert archives,'Review before-image archive not found'
        results.append({'job':metric['job'],'kind':metric['kind'],'articles':len(rows),'metric':metric,'article_checks':article_checks,'review_before_image_archives':archives})
finally:db.close()

# Technical refusal inventory only. Never fabricate the missing legal assessment.
refusals=[]
for name in ['travail-00422','travail-00425']:
    folder=HERE/'runtime/exhaustive/jobs'/name
    sources=read(folder/'source.json');answer=read(folder/'answer.json');snapshot=read(folder/'reference-targets.json')
    before={key(a):a for a in sources};missing=[]
    for row in answer:
        needed=requirements(before[key(row)],row['proposed_xml'])|set(snapshot['requirements'].get(key(row),[]))
        present={a.get('target_key') for a in row.get('reference_checks',[]) if isinstance(a,dict)}
        if needed-present:missing.append({'code_id':row['code_id'],'source_id':row['source_id'],'number':row['number'],'missing_target_keys':sorted(needed-present)})
    refusals.append({'job':name,'recorded_validation':read(folder/'validation-failure.json'),'missing_assessments':missing,'new_assessment_written':False,'guard_relaxed':False,'requires_fresh_full_targets_and_substantive_assessment':True})

summary={'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'coordinator_pid':3122,'incident_capture_epoch_unix':epoch,
         'accepted_new_articles_since_incident_capture':sum(a['articles'] for a in results if a['kind']=='new'),
         'accepted_review_articles_since_incident_capture':sum(a['articles'] for a in results if a['kind']=='review'),
         'accepted_jobs':results,'all_accepted_rows_found_in_current_canonical_database':True,
         'sources_notes_versions_and_review_beforeimages_verified':True,'read_only_database':True,
         'no_registration_or_model_invocation':True,'no_freshness_claim_for_all_reference_targets_after_other_jobs':True,
         'global_semantic_review_or_jurist_completion':False,'reference_refusals':refusals,'input_guards':inputs}
(OUT/'accepted-verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['verified_at_utc','accepted_new_articles_since_incident_capture','accepted_review_articles_since_incident_capture','all_accepted_rows_found_in_current_canonical_database']},ensure_ascii=False))
