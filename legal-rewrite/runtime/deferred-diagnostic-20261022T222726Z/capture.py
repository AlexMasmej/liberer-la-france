"""Small read-only diagnosis; no coordinator, canonical, or queue mutation."""
from pathlib import Path
from datetime import datetime, timezone
import copy, collections, hashlib, json, re, sqlite3, sys

HERE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import substantive_impact as impact
import reference_coherence as references
import register_batches
import run_exhaustive
from ingest import source_notes
from worker_execution import verify_execution

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(name, value):
    target = OUT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

inputs = []
def read(relative, copied=None):
    path = HERE / relative
    data = path.read_bytes()
    item = {'path': str(path), 'bytes': len(data), 'sha256': sha(data)}
    if copied:
        target = OUT / copied
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        item['preserved_copy'] = str(target.relative_to(OUT))
    inputs.append(item)
    return data

captured = datetime.now(timezone.utc).isoformat()
metrics = [json.loads(line) for line in read('runtime/exhaustive/job-metrics.jsonl').splitlines()]
cohort = [m for m in metrics if m.get('coordinator_pid') == 3122]
older = [m for m in metrics if m.get('coordinator_pid') == 18713]
failed = json.loads(read('runtime/exhaustive/failed-jobs.json', 'inputs/failed-jobs.json'))
resolved = json.loads(read('runtime/exhaustive/failed-job-resolutions.json', 'inputs/failed-job-resolutions.json'))
failmap = {f['job']: f for f in failed}
deferred = [m for m in cohort if m.get('outcome') == 'deferred']
write('metrics.json', {'captured_at_utc': captured, 'previous_cohort': older, 'current_cohort': cohort})
for relative in ['runtime/exhaustive/coordinator-run.json', 'runtime/exhaustive/stop-request.json',
                 'runtime/exhaustive/coordinator-exit.json', 'runtime/resume-latest.json',
                 'runtime/exhaustive/worker-limit.json', 'runtime/exhaustive/admission-deferred.json',
                 'runtime/exhaustive/status.json', 'runtime/supervision/status.json']:
    read(relative, 'inputs/' + relative.replace('/', '__'))

queue = json.loads(read('runtime/exhaustive/mixed-queue.json'))
queued = collections.defaultdict(list)
for q in queue:
    for identifier in q['source_ids']:
        queued[(identifier, bool(q.get('review')))].append({'slug': q['slug'], 'index': q['index']})
prior = json.loads(read('runtime/radical-review-20261019.json'))
review_status = {(a['code_id'], a['source_id']): a for a in prior['prior_articles']}

db = sqlite3.connect('file:' + str(HERE/'corpus.sqlite') + '?mode=ro', uri=True)
db.execute('BEGIN')
diagnoses = []
for metric in deferred:
    name = metric['job']
    directory = HERE/'runtime/exhaustive/jobs'/name
    recorded = failmap[name]
    sources = json.loads(read(str(directory.relative_to(HERE)/'source.json'), 'jobs/'+name+'/source.json'))
    attempts = []
    for errorlog in sorted(directory.glob('errors-*.log')):
        raw = read(str(errorlog.relative_to(HERE)))
        lines = raw.decode(errors='replace').splitlines()
        actual_errors = [line for line in lines if line.startswith(('ERROR:', 'warning: Falling back'))
                         or (re.match(r'^2026-\d\d-\d\dT', line) and ' ERROR ' in line)]
        write('jobs/'+name+'/'+errorlog.stem+'-errors.json', actual_errors)
        transport = [line for line in actual_errors if re.search(r'workspace routing discovery|error sending request|request timed out|Reconnecting', line, re.I)]
        access = [line for line in actual_errors if re.search(r'rate.limit|usage.limit|quota|unauthori[sz]ed|authentication|sign.in|insufficient|\b40[13]\b|\b429\b', line, re.I)]
        attempts.append({'log': str(errorlog), 'log_sha256': sha(raw), 'network_error_lines': transport,
                         'access_or_quota_error_lines': access,
                         'native_execution': verify_execution(directory, stderr_path=errorlog)})
    dispositions = []
    for source in sources:
        key = source['code_id'], source['source_id']
        canonical = db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone()
        draft = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        disposition = {'code_id': key[0], 'source_id': key[1], 'number': source['number'],
                       'canonical_source_hash_matches': canonical is not None and canonical[0] == source['source_sha256'],
                       'canonical_source_xml_matches': canonical is not None and canonical[1] == source['source_xml'],
                       'canonical_source_notes_matches': source_notes(db,*key) == source.get('source_notes_xml',''),
                       'canonical_versions_match': canonical is not None and canonical[2:] == (source.get('valid_from'),source.get('valid_until')),
                       'draft_present': draft is not None,
                       'canonical_draft_status': draft[1] if draft else None,
                       'canonical_draft_source_hash_matches': draft is not None and draft[0] == source['source_sha256'],
                       'canonical_draft_body_sha256': sha((draft[2] or '').encode()) if draft else None,
                       'in_persistent_startup_queue': queued.get((source['source_id'], metric['kind']=='review'), []),
                       'review_status': review_status.get(key, {}).get('review_status'),
                       'this_failed_job_accepted': False}
        dispositions.append(disposition)
    diagnoses.append({'job': name, 'kind': metric['kind'], 'metric': metric, 'recorded_failure': recorded,
                      'explicit_resolution_entry': [r for r in resolved if r.get('job')==name],
                      'cause': 'metadata_exact_passage' if 'exact passage' in recorded['error'] else 'transport_failure',
                      'attempts': attempts, 'articles': dispositions})
write('deferred-disposition.json', {'captured_at_utc': captured, 'coordinator_pid':3122,
                                 'jobs': diagnoses, 'counting_note':'A draft existing before a failed review does not mean that review was accepted. Persistent startup queue membership is not an acceptance or a live admission.'})

candidate_job = 'travail-00396-resume-d9t22r7o'
directory = HERE/'runtime/exhaustive/jobs'/candidate_job
source_data = read(str(directory.relative_to(HERE)/'source.json'), 'metadata-repair/source.json')
answer_data = read(str(directory.relative_to(HERE)/'answer.json'), 'metadata-repair/answer.original.json')
target_data = read(str(directory.relative_to(HERE)/'reference-targets.json'), 'metadata-repair/reference-targets.json')
sources, original, snapshot = json.loads(source_data), json.loads(answer_data), json.loads(target_data)
for filename in ['coordination.json','policy.json','policy-fingerprint.json','validation-failure.json','result.json','execution-observed-3.json']:
    read(str(directory.relative_to(HERE)/filename),'metadata-repair/'+filename)

candidate = copy.deepcopy(original)
matches = []
for row in candidate:
    for index, effect in enumerate(row['substantive_impact']['effects']):
        if row['source_id']=='LEGIARTI000033407486' and effect['measure_id']=='afpa-comites-facultatifs':
            before = effect['proposed_quote']
            after = before.replace('institué ;3°', 'institué ; 3°')
            if after == before:
                raise ValueError('Pinned repair does not match original exact quote')
            if impact.plain(after) not in impact.plain(row['proposed_xml']):
                raise ValueError('Corrected quote is still not an exact current passage')
            effect['proposed_quote'] = after
            matches.append({'source_id':row['source_id'],'number':row['number'],'effect_index':index,
                            'field':'substantive_impact.effects[0].proposed_quote','before':before,'after':after})
assert len(matches)==1
write('metadata-repair/answer.candidate.json', candidate)
article_keys = ['code_id','source_id','source_sha256','number','status','proposed_xml','reason','review_notes']
assert all({k:r.get(k) for k in article_keys}=={k:c.get(k) for k in article_keys} for r,c in zip(original,candidate))
changed_article = next(a for a in candidate if a['source_id']=='LEGIARTI000033407486')
source_article = next(s for s in sources if s['source_id']==changed_article['source_id'])
write('metadata-repair/whole-article-context.json', {'source':source_article,'candidate':changed_article,
      'review_scope':'Whole source, empty NOTA, complete proposal, reasons, review notes and all impact fields read. Committee audit, nomination mechanism, economic/financial control, transitional continuation and council competences remain unchanged. This file repairs evidence spacing only; no new legal conclusion is inferred.'})
validation = {'state':'offline_prepared_not_integrated','changes':matches,
              'all_24_normative_texts_and_reasons_strictly_unchanged':True,
              'new_certificates_not_carried_into_prepared_answer':True,
              'canonical_registration_performed':False,'semantic_review_by_jurist':False}
try:
    run_exhaustive.validate_answer(copy.deepcopy(original), sources)
    validation['original_validate_answer']='unexpected_pass'
except Exception as error:
    validation['original_validate_answer']={'type':type(error).__name__,'error':str(error)}
checked = run_exhaustive.validate_answer(copy.deepcopy(candidate), sources)
validation['candidate_validate_answer']='pass'
references.accept_checks(checked, sources, snapshot)
validation['candidate_accept_checks']='pass'
try:
    references.check_guards(db,snapshot)
    validation['current_reference_guards']='pass'
except Exception as error:
    validation['current_reference_guards']={'type':type(error).__name__,'error':str(error)}
batch = OUT/'metadata-repair/isolated-batches/test/00001.json'
batch.parent.mkdir(parents=True,exist_ok=True)
batch.write_text(json.dumps(candidate,ensure_ascii=False,indent=2)+'\n')
try:
    records, diagnostics, batch_files = register_batches.validate_batches(db,batch.parent.parent)
    validation['candidate_real_register_validate_batches']={'passed':True,'articles':len(records),'diagnostics':diagnostics,'batch_files':batch_files}
except Exception as error:
    validation['candidate_real_register_validate_batches']={'passed':False,'type':type(error).__name__,'error':str(error)}
validation['current_sources_all_match']=all(a['canonical_source_hash_matches'] and a['canonical_source_xml_matches'] and a['canonical_source_notes_matches'] and a['canonical_versions_match'] for d in diagnoses if d['job']==candidate_job for a in d['articles'])
validation['no_current_draft_for_any_of_24']=all(not a['draft_present'] for d in diagnoses if d['job']==candidate_job for a in d['articles'])
validation['full_policy_is_current']=run_exhaustive.policy_is_current(directory)
validation['required_next_step']='Before integration at a coordinated safe point: recheck all source/NOTA/versions, current owner and before-image absence, policy/code hashes, exact target guards and whole article/reference context; acquire the normal reservations/transaction guards. Keep failed originals; never count the prepared patch as accepted.'
write('metadata-repair/validation.json',validation)
db.rollback()
db.close()

supervisor_events=[]
for line in read('runtime/supervision/events.jsonl').splitlines():
    event=json.loads(line)
    if 1792696860 <= event.get('checked_at_unix',0) <= 1792702855:
        supervisor_events.append({k:v for k,v in event.items() if k in ['state','reason','checked_at_unix','coordinator_pids','consecutive_unexpected_exits','next_start_after_unix','counters']})
write('supervision-transition.json',supervisor_events)
for relative in ['runtime/supervision/restarts/20261022T183134956172Z/continuation.log',
                 'runtime/supervision/restarts/20261022T205415036821Z/continuation.log']:
    data=read(relative)
    lines=data.decode(errors='replace').splitlines()
    selected=[line for line in lines if line.startswith(('ACCEPTED ','RADICAL REVIEW ','DEFERRED ','STOP ','START ','MIXED QUEUE ','BLOCKED ','FINISH '))]
    write('logs/'+Path(relative).parent.name+'-events.json',selected)
read('runtime/supervision/restarts/20261022T205415036821Z/launch.json','inputs/launch-3122.json')
for relative in ['register_batches.py','run_exhaustive.py','reference_coherence.py','substantive_impact.py','policy-coordinations.json','policy.json','site-summaries.json','reference-dependencies.json']:
    if (HERE/relative).exists():read(relative)
write('inputs-manifest.json',{'captured_at_utc':captured,'inputs':inputs,'source_db_access':'SQLite URI mode=ro, one read transaction; no snapshot copy','side_effects':'Only new diagnosis folder written; no launch, signal, slot, source, queue, policy, catalogue or canonical change.'})
print(json.dumps({'folder':str(OUT),'deferred_jobs':len(diagnoses),'new_articles':sum(len(d['articles']) for d in diagnoses if d['kind']=='new'),'review_articles':sum(len(d['articles']) for d in diagnoses if d['kind']=='review'),'draft_present_new':sum(a['draft_present'] for d in diagnoses if d['kind']=='new' for a in d['articles']),'review_completed':sum(a['review_status']=='completed' for d in diagnoses if d['kind']=='review' for a in d['articles']),'metadata_validation':validation},ensure_ascii=False,indent=2))
