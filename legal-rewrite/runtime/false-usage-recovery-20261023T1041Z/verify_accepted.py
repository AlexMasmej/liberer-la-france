"""Verify the new coordinator's accepted work, without registering anything."""
from pathlib import Path
from collections import Counter
from contextlib import nullcontext
import datetime
import hashlib
import json
import sqlite3
import sys

PROOF=Path(__file__).resolve().parent
ROOT=PROOF.parents[1]
OUTPUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else PROOF/'accepted-verification.json'
assert OUTPUT.parent==PROOF and not OUTPUT.exists()
sys.path.insert(0,str(ROOT))
from ingest import source_notes,source_evidence
from worker_execution import verify_execution
import reference_coherence as refs

def sha(value):
    return hashlib.sha256(value if isinstance(value,bytes) else (value or '').encode()).hexdigest()

stable={}
def read(path):
    data=Path(path).read_bytes();stable[Path(path)]=sha(data);return json.loads(data)

base=ROOT/'runtime/exhaustive'
metrics_data=(base/'job-metrics.jsonl').read_bytes()
metrics=[json.loads(x) for x in metrics_data.splitlines()]
accepted=[x for x in metrics if x['coordinator_pid']==39614 and x['outcome']=='accepted']
reviewed=[x for x in metrics if x['coordinator_pid']==39614 and x['outcome']=='reviewed']
assert accepted
ledger=[json.loads(x) for x in (ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/current-article-ledger.jsonl').read_text().splitlines()]
canonical={(x['code_id'],x['source_id']):x for x in ledger}
original=read(PROOF/'locked-disposition.json')
old_sources={(x['code_id'],x['source_id']) for x in original['rows'] if x['kind']=='new' and x['first_pass_absent']}
old_queue=read(ROOT/'runtime/supervision/restarts/20261023T105555458418Z/mixed-queue.json')
unattempted={('LEGITEXT000006072050',i) for x in old_queue
             if not x['review'] and x['index'] in [475,476,477,478] for i in x['source_ids']}
verified=[];verified_reviews=[]
# Observe with a pinned ro transaction and unchanged input-file hashes. The
# canonical writer can finish its valid review; any changed input aborts this
# evidence collection instead of producing a mixed-state verification.
with nullcontext():
    db=sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True)
    db.execute('BEGIN')
    registry=read(ROOT/'registered-batches.json')
    for metric in accepted:
        folder=base/'jobs'/metric['job']; sources=read(folder/'source.json')
        answer=read(folder/'answer.json'); intent=read(folder/'registration-intent.json')
        complete=read(folder/'registration-complete.json');batch=read(Path(complete['batch_path']))
        observed=read(folder/f"execution-observed-{metric['attempts']}.json")
        execution=verify_execution(folder,stderr_path=observed['source_log'])
        assert execution['verified'] and execution['model']=='gpt-6-astra' and execution['reasoning_effort']=='medium'
        assert execution['session_id']==metric['execution_session_id']
        assert complete['accepted_articles']==metric['articles']==len(batch)==len(answer)==len(sources)
        assert intent['rows']==batch and intent['batch_path']==complete['batch_path']
        assert sha((folder/'source.json').read_bytes())==intent['source_sha256']
        assert sha((folder/'reference-targets.json').read_bytes())==intent['reference_sha256']
        source_map={(x['code_id'],x['source_id']):x for x in sources}
        answer_map={(x['code_id'],x['source_id']):x for x in answer}
        assert len(source_map)==len(answer_map)==len(batch)
        statuses=Counter();certificates=Counter();rows=[]
        for row in batch:
            key=row['code_id'],row['source_id'];source=source_map[key];raw=answer_map[key]
            assert key in old_sources|unattempted and key in canonical
            expected=(row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes'])
            actual=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
            assert actual==expected
            assert (raw['source_sha256'],raw.get('status','rewrite_draft'),raw['proposed_xml'],raw['reason'],raw['review_notes'])==expected
            actual_source=db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
            assert actual_source==(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
            assert source_notes(db,*key)==source['source_notes_xml']
            assert canonical[key]['source_sha256']==source['source_sha256']
            evidence=db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',key).fetchone()
            assert evidence==(source_evidence(source['source_xml'],source['source_notes_xml']),source['valid_from'],source['valid_until'])
            assert registry['|'.join(key)]==dict(source_sha256=row['source_sha256'],proposed_sha256=sha(row['proposed_xml']))
            statuses[row.get('status','rewrite_draft')]+=1
            needed=refs.requirements(source,row['proposed_xml'],db=db)
            cert_state=('not_required_by_catalogue' if not needed else
                        'current' if refs.certificate_current(db,source,row['proposed_xml'],row.get('reference_coherence')) else
                        'pending_convergence')
            certificates[cert_state]+=1
            rows.append(dict(code_id=key[0],source_id=key[1],source_sha256=row['source_sha256'],proposed_sha256=sha(row['proposed_xml']),reason_sha256=sha(row['reason']),notes_sha256=sha(row['review_notes']),all_five_fields_source_notes_versions_batch_registry_intent_match=True))
        verified.append(dict(job=metric['job'],articles=len(rows),execution=execution,metric=metric,statuses=dict(statuses),reference_certificates=dict(certificates),rows=rows))
    wanted=set()
    for metric in reviewed:
        wanted.update((x['code_id'],x['source_id']) for x in read(base/'jobs'/metric['job']/'source.json'))
    owners={};owner_rows={}
    if wanted:
        for path in sorted((ROOT/'batches').glob('*/*.json')):
            if not path.stem.isdigit() and not path.stem.startswith('batch'):continue
            data=json.loads(path.read_bytes())
            for row in data:
                key=row['code_id'],row['source_id']
                if key not in wanted:continue
                assert key not in owners
                owners[key]=path;owner_rows[key]=row;stable[path]=sha(path.read_bytes())
    archives={}
    if wanted:
        for path in (ROOT/'revisions/radical-review').glob('*.json'):
            data=json.loads(path.read_bytes())
            for entry in data:
                key=entry['code_id'],entry['source_id']
                if key in wanted:
                    archives.setdefault(key,[]).append((path,entry))
    for metric in reviewed:
        folder=base/'jobs'/metric['job'];sources=read(folder/'source.json');answer=read(folder/'answer.json')
        observed=read(folder/f"execution-observed-{metric['attempts']}.json")
        execution=verify_execution(folder,stderr_path=observed['source_log'])
        assert execution['verified'] and execution['model']=='gpt-6-astra' and execution['reasoning_effort']=='medium'
        assert execution['session_id']==metric['execution_session_id']
        assert len(sources)==len(answer)==metric['articles']
        answers={(x['code_id'],x['source_id']):x for x in answer};checked=[]
        for source in sources:
            key=source['code_id'],source['source_id'];row=owner_rows[key];raw=answers[key]
            expected=(row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes'])
            assert db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()==expected
            assert (raw['source_sha256'],raw.get('status','rewrite_draft'),raw['proposed_xml'],raw['reason'],raw['review_notes'])==expected
            assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()==(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
            assert source_notes(db,*key)==source['source_notes_xml']
            assert db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',key).fetchone()==(source_evidence(source['source_xml'],source['source_notes_xml']),source['valid_from'],source['valid_until'])
            assert registry['|'.join(key)]==dict(source_sha256=row['source_sha256'],proposed_sha256=sha(row['proposed_xml']))
            matches=[(path,entry) for path,entry in archives[key] if entry['replacement']==row]
            assert len(matches)==1
            path,entry=matches[0];prior=source['previous_draft']
            assert path.stem==sha(json.dumps(read(path),ensure_ascii=False,sort_keys=True))
            assert tuple(entry[k] for k in ['source_sha256','status','proposed_xml','reason','review_notes'])==tuple(prior[k] for k in ['source_sha256','status','proposed_xml','reason','review_notes'])
            assert sha(entry['proposed_xml'])==prior['proposed_sha256']==row['prior_proposal_sha256']
            checked.append(dict(code_id=key[0],source_id=key[1],archive=str(path.relative_to(ROOT)),
                source_proposal_notes_versions_and_archived_beforeimage_match=True,
                current_proposal_sha256=sha(row['proposed_xml']),prior_proposal_sha256=prior['proposed_sha256']))
        verified_reviews.append(dict(job=metric['job'],articles=len(checked),execution=execution,metric=metric,rows=checked))
    states={(c,i):(s,status,bool(body)) for c,i,s,status,body in db.execute('SELECT code_id,source_id,source_sha256,status,proposed_xml FROM drafts')}
    present={k for k,x in canonical.items() if k in states and states[k][0]==x['source_sha256'] and (states[k][2] or states[k][1]=='retained_unchanged')}
    missing=set(canonical)-present
    review=read(ROOT/'runtime/radical-review-20261019.json')
    old_review_pending={(x['code_id'],x['source_id']) for x in review['prior_articles'] if x['review_status']=='pending'}
    for result in verified_reviews:
        for row in result['rows']:
            assert any(x['code_id']==row['code_id'] and x['source_id']==row['source_id'] and x['review_status']=='completed' for x in review['prior_articles'])
    unresolved_reviews={(x['code_id'],x['source_id']) for x in original['rows'] if x['kind']=='review' and x['prior_review_pending']}
    disposition=dict(first_pass_covered=len(present),first_pass_pending=len(missing),
        old_nonaccepted_new_still_absent=len(missing&old_sources),old_unattempted_new_still_absent=len(missing&unattempted),
        documentary_holds_pending=len(missing-(old_sources|unattempted)),
        nonaccepted_old_reviews_still_pending=len(old_review_pending&unresolved_reviews),
        old_review_pending=len(old_review_pending),old_review_completed=review['completed_second_pass'])
    db.rollback();db.close()
    for path,expected in stable.items():assert sha(path.read_bytes())==expected
report=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),coordinator_pid=39614,
    verified_accepted_jobs=len(verified),verified_accepted_new_articles=sum(x['articles'] for x in verified),
    verified_reviewed_jobs=len(verified_reviews),verified_reviewed_articles=sum(x['articles'] for x in verified_reviews),
    verification_scope='Whole source, NOTA, versions, five proposal fields, native execution and current DB/batch/registry/intention; not final legal review',
    no_replay_no_registration_no_canonical_mutation=True,verified_jobs=verified,verified_reviews=verified_reviews,current_disposition=disposition,
    input_hashes={str(p.relative_to(ROOT)):v for p,v in stable.items()})
with OUTPUT.open('x') as output:json.dump(report,output,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in report.items() if k not in ['verified_jobs','verified_reviews','input_hashes']},ensure_ascii=False))
