"""Read-only registration/source reconciliation for the single-file repair.

Never installs code or starts a model. This is not the review-phase transfer
controller and cannot declare all second passes or legal convergence complete.
"""
from pathlib import Path
from collections import Counter
import datetime
import hashlib
import json
import re
import sqlite3
import sys
import time

PROOF = Path(__file__).resolve().parent
ROOT = PROOF.parents[1]
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else PROOF/'preflight.json'
assert OUTPUT.parent == PROOF and not OUTPUT.exists()
sys.path.insert(0, str(ROOT))
import register_batches as registration
import reference_coherence as refs
from ingest import source_notes, source_evidence


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else (value or '').encode()).hexdigest()


stable = {}


def read(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise RuntimeError('Unknown regular evidence: '+str(path))
    data = path.read_bytes(); stable[path] = digest(data)
    return json.loads(data)


def note(message):
    print(message, flush=True)


def values(row):
    return (row['source_sha256'],row.get('status','rewrite_draft'),
            row['proposed_xml'],row['reason'],row['review_notes'])


started = time.time()
base = ROOT/'runtime/exhaustive'
run = read(base/'coordinator-run.json')
assert run['pid'] == 3122
exit_receipt = read(base/'coordinator-exit.json')
last_alive = read(ROOT/'runtime/false-usage-classification-20261023T0943Z/system-check.json')
assert type(exit_receipt['exit_code']) is int and exit_receipt['exit_code'] == 0
assert exit_receipt['pid'] == 3122 and exit_receipt['stop_requested'] is True
assert exit_receipt['exit_type'] is None
assert last_alive['observed_at_unix'] < exit_receipt['ended_at_unix'] <= time.time()
assert (base/'coordinator-exit.json').stat().st_mtime >= exit_receipt['ended_at_unix']
assert last_alive['os_process_birth']['epoch'] <= run['started_at_unix']
assert last_alive['os_process_birth']['run_start_delay_seconds'] == 6
pause = read(ROOT/'runtime/supervision/disabled')
assert pause['owner'] == 'false-usage-classification-20261023T0943Z-f7e28488-2bc7-4a9f-8113-ee14df0a6198'
assert stable[ROOT/'runtime/supervision/disabled'] == '56afa06903a7e52346f17f5d937844c9d16160f68dce473c8837aa94fc4a009c'
assert read(base/'manual-agent-slots.json') == []
assert read(base/'worker-limit.json') == dict(workers=7,role_limits=dict(new=6,review=1))
admission = read(base/'admission-status.json')
assert admission['coordinator_pid'] == 3122 and admission['action'] == 'stopped'
assert admission['reserved_or_running_by_kind'] == {'new':0,'review':0}

pin_names = ['run_exhaustive.py','register_batches.py','review_prior.py',
             'reference_coherence.py','reference_queue.py','source_assets.py',
             'substantive_impact.py','worker_execution.py','worker_capacity.py',
             'review_lanes.py','review_lane_observation.py','supervise_exhaustive.py',
             'ingest.py','corpus.json','policy-coordinations.json','site-summaries.json',
             'reference-focus-extra.json','runtime/exhaustive/model-policy.json',
             'runtime/exhaustive/parallelism-plan.json']
pins = {name:digest((ROOT/name).read_bytes()) for name in pin_names}
assert pins['run_exhaustive.py'] == '1c66699d0b54334c099460546c8bd1cfced0a831336a544caf17b7b928538f7e'
assert pins['register_batches.py'] == '75287e3267fb8d182a7262cdb747ae90070e20d6bf92b698768684e03c39051f'
for path in (ROOT/'attachments/records').glob('*.json'):
    pins[str(path.relative_to(ROOT))] = digest(path.read_bytes())
registry = read(ROOT/'registered-batches.json')
ledger_data = (ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/current-article-ledger.jsonl').read_bytes()
assert digest(ledger_data) == '0f23741391f96834a9e2d8db569bc06da450d47805989f641d44a28755ca1272'
ledger = [json.loads(line) for line in ledger_data.splitlines()]
canonical = {(x['code_id'],x['source_id']):x for x in ledger}
assert len(canonical) == 30317 and len({x['slug'] for x in ledger}) == 9
outside = read(ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/outside-current-inventory.json')
outside_guards = {(x['code_id'],x['source_id']):x['draft_guards'] for x in outside}
assert len(outside_guards) == 4 and not set(outside_guards) & set(canonical)
db = sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True)
db.execute('BEGIN')
note('Validating whole current batches with the unchanged native validator')
records, diagnostics, files = registration.validate_batches(db,ROOT/'batches')
owners = {}
for entry in files:
    path = ROOT/entry['file']; rows = read(path)
    assert digest(path.read_bytes()) == entry['sha256']
    for row in rows:
        key = row['code_id'],row['source_id']
        assert key not in owners
        owners[key] = entry['file']
assert set(owners) == set(records)
note('Checking exact database, immutable source evidence and registry mirrors')
all_drafts = {(c,i):(s,st,b,reason,notes) for c,i,s,st,b,reason,notes in db.execute(
    'SELECT code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes FROM drafts')}
for key,(row,body,start,end) in records.items():
    assert all_drafts.get(key) == values(row), ('Database/batch differs',key)
    expected = dict(source_sha256=row['source_sha256'],proposed_sha256=digest(row['proposed_xml']))
    assert registry.get('|'.join(key)) == expected, ('Registry/batch differs',key)
    evidence = db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources '
                          'WHERE code_id=? AND source_id=?',key).fetchone()
    assert evidence == (source_evidence(body,source_notes(db,*key)),start,end), ('Source evidence differs',key)
assert set(registry) == {'|'.join(k) for k in records}, 'Unclassified registry owner'
unowned = []
for key,value in all_drafts.items():
    if key in records: continue
    row = canonical.get(key)
    if row:
        guard = row['draft_guards']
        assert value[0] == guard['source_sha256'] and value[1] == guard['status']
        assert [digest(x) for x in value[2:]] == [guard['proposal_sha256'],guard['reason_sha256'],guard['notes_sha256']]
        unowned.append(dict(code_id=key[0],source_id=key[1],classification='exact_legacy_inventory_beforeimage'))
    else:
        assert key in outside_guards, ('Unknown ownerless historical draft',key)
        guard=outside_guards[key]
        assert value[0] == guard['source_sha256'] and value[1] == guard['status']
        assert [digest(x) for x in value[2:]] == [guard['proposal_sha256'],guard['reason_sha256'],guard['notes_sha256']]
        unowned.append(dict(code_id=key[0],source_id=key[1],classification='historical_outside_canonical_inventory_preserved'))
assert {k for k in all_drafts if k not in canonical} == set(outside_guards)
note('Checking all canonical source identities and versions')
for key,row in canonical.items():
    src = db.execute('SELECT source_sha256 FROM articles WHERE code_id=? AND id=?',key).fetchone()
    assert src and src[0] == row['source_sha256'], ('Canonical source changed',key)

note('Partitioning the immutable PID queue into terminal and never-admitted jobs')
plan=read(base/'queue-admission-plan.json');queue=read(base/'mixed-queue.json')
assert plan['coordinator_pid']==3122 and plan['queue_file']=='mixed-queue.json'
deferred=read(base/'admission-deferred.json');assert deferred['coordinator_pid']==3122
metrics_path=base/'job-metrics.jsonl';metrics_data=metrics_path.read_bytes()
stable[metrics_path]=digest(metrics_data);assert metrics_data.endswith(b'\n')
metrics=[json.loads(x) for x in metrics_data.splitlines()]
metrics=[x for x in metrics if x['coordinator_pid']==3122]
def qkey(x):return ('review' if x['review'] else 'new',x['slug'],x['index'])
def mkey(x):return (x['kind'],x['slug'],x['index'])
scheduled={qkey(x):x for x in queue};terminal={mkey(x):x for x in metrics}
unadmitted={mkey(x):x for x in deferred['jobs']}
assert len(scheduled)==len(queue) and len(terminal)==len(metrics) and len(unadmitted)==len(deferred['jobs'])
assert not set(terminal)&set(unadmitted) and set(scheduled)==set(terminal)|set(unadmitted)
assert Counter(k[0] for k in scheduled)==plan['scheduled_by_kind']
assert Counter(k[0] for k in terminal)==admission['admitted_by_kind']
assert Counter(k[0] for k in unadmitted)==admission['deferred_by_kind']
for k,entry in unadmitted.items():
    assert entry['source_ids']==scheduled[k]['source_ids']
    assert entry['attempted'] is False and entry['accepted'] is False and entry['reason']=='stop_requested'
for k,metric in terminal.items():
    assert run['started_at_unix']<=metric['started_at_unix']<=metric['finished_at_unix']<=exit_receipt['ended_at_unix']
    assert metric['outcome'] in {'accepted','reviewed','skipped','deferred','stopped','blocked_auth_or_usage'}
    assigned=scheduled[k]['source_ids']
    assert len(assigned)==len(set(assigned))
    if metric['outcome']=='skipped':
        for sid in assigned:
            keys=[key for key,x in canonical.items() if x['slug']==k[1] and key[1]==sid]
            assert len(keys)==1 and keys[0] in all_drafts
        continue
    saved=read(base/'jobs'/metric['job']/'source.json')
    assert [x['source_id'] for x in saved]==assigned
    for source in saved:
        key=source['code_id'],source['source_id']
        actual=db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
        assert actual==(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
        assert source_notes(db,*key)==source['source_notes_xml']

note('Inventorying current reference certificates; stale targets remain pending')
catalog = refs.focus(); certificate_counts = Counter(); pending_refs=[]
for key,(row,body,start,end) in records.items():
    article = {'code_id':key[0],'source_id':key[1],'number':row['number'],'source_xml':body}
    needed = refs.requirements(article,row['proposed_xml'],catalog,db)
    if not needed: certificate_counts['not_required_by_current_catalogue']+=1;continue
    certificate = row.get('reference_coherence')
    if not certificate:
        certificate_counts['missing_pending']+=1
        pending_refs.append(dict(code_id=key[0],source_id=key[1],reason='missing_certificate'))
        continue
    assert isinstance(certificate,dict), ('Malformed certificate',key)
    assert certificate['referrer_sha256'] == digest(row['proposed_xml']), ('Referrer body integrity',key)
    assert certificate['semantic_review_by_jurist'] is False
    targets = certificate['targets']; checks = certificate['assessments']
    assert refs.assessments_current(checks,targets), ('Assessment integrity',key)
    assert certificate['assessments_sha256'] == refs.assessment_digest(checks), ('Assessment digest',key)
    assert certificate['referrer_source'] == refs.referrer_source(db,refs.key(article)), ('Referrer source integrity',key)
    if refs.certificate_current(db,article,row['proposed_xml'],certificate,catalog):
        certificate_counts['current']+=1;continue
    reason=[]
    if certificate.get('version') != refs.VERSION:reason.append('legacy_version')
    if certificate.get('policy_sha256') != refs.policy_state():reason.append('policy_changed')
    if set(targets) != needed:reason.append('requirements_changed')
    changed=[k for k,t in targets.items() if refs.state(db,k) != t]
    if changed:reason.append('target_view_changed')
    assert reason, ('Unclassified reference inconsistency',key)
    certificate_counts['stale_pending']+=1
    pending_refs.append(dict(code_id=key[0],source_id=key[1],reason=reason,changed_targets=changed))

note('Reconciling durable first-pass registration intentions against current owners')
intents = Counter(); intent_details=[]
for path in sorted((base/'jobs').glob('*/registration-intent.json')):
    intent = read(path); current=historical=absent=0
    for row in intent['rows']:
        key=row['code_id'],row['source_id'];value=all_drafts.get(key)
        if value is None:absent+=1;continue
        assert value[0] == row['source_sha256'], ('Intent source mismatch',key)
        if value == values(row):current+=1
        else:
            assert key in records and all_drafts[key] == values(records[key][0])
            historical+=1
    completion=path.parent/'registration-complete.json'
    if current or historical:
        assert completion.exists(), ('Accepted rows without completion mirror',path)
        receipt=read(completion)
        assert receipt['batch_path'] == intent['batch_path']
        assert receipt['accepted_articles'] == len(intent['rows'])
        assert absent == 0, ('Partially missing committed intent',path)
    else:
        assert not completion.exists(), ('Completion without rows',path)
    intents['files']+=1;intents['current_rows']+=current;intents['historical_rows']+=historical;intents['uncommitted_absent_rows']+=absent
    intent_details.append(dict(path=str(path.relative_to(ROOT)),current=current,historical=historical,absent=absent))
note('Checking archived before-images and exact current review replacements')
replacements = {}
archive_entries={}
archive_files=[]
for path in sorted((ROOT/'revisions/radical-review').glob('*.json')):
    archive = read(path)
    assert path.stem == digest(json.dumps(archive,ensure_ascii=False,sort_keys=True)), ('Review archive identity',path)
    for entry in archive:
        replacement = entry['replacement'];key=entry['code_id'],entry['source_id']
        assert key == (replacement['code_id'],replacement['source_id'])
        assert entry['source_sha256'] == replacement['source_sha256']
        assert digest(entry['proposed_xml']) == replacement['prior_proposal_sha256']
        fingerprint=digest(json.dumps(replacement,ensure_ascii=False,sort_keys=True,separators=(',',':')))
        replacements.setdefault((key,fingerprint),[]).append(str(path.relative_to(ROOT)))
        archive_entries.setdefault(key,[]).append(replacement)
    archive_files.append(str(path.relative_to(ROOT)))
approval=read(ROOT/'runtime/poursuite-20261020-e/root-adoption-approval.json')
recapture=approval['recapture']
assert approval['approved'] is True and approval['scope']=='E52-and-C141-bounded-context'
for field in ['source','answer','snapshot','proof','receipt','capture','capture_approval','helper']:
    evidence=ROOT/recapture[field+'_path']
    stable[evidence]=digest(evidence.read_bytes())
    assert stable[evidence] == recapture[field+'_sha256'], ('Historical recertification pin',field)
receipt=read(ROOT/recapture['receipt_path'])
assert receipt['metadata_only'] is True and receipt['sqlite_changed'] is False and receipt['registry_changed'] is False
assert receipt['normative_bodies_changed']==receipt['impacts_changed']==receipt['workflow_fields_changed']==0
recertified_files={x['path']:x['after_sha256'] for x in receipt['owning_files']}
first_pass_captures={}
for folder in ['runtime/sru-integral/registration-003','runtime/sru-urbanisme-fiscalite']:
    sources=read(ROOT/folder/'sources.json');answers=read(ROOT/folder/'candidates.json')
    source_map={(x['code_id'],x['source_id']):x for x in sources}
    for answer in answers:
        key=answer['code_id'],answer['source_id'];source=source_map[key]
        if source.get('previous_draft') is None and answer.get('prior_proposal_sha256') is None:
            first_pass_captures[key]=(source,answer)
reviewed_rows=0;metadata_only_history=[];first_pass_null_marker=[]
for key,(row,body,start,end) in records.items():
    if 'prior_proposal_sha256' not in row:continue
    if row['prior_proposal_sha256'] is None:
        assert key in first_pass_captures, ('Unknown null prior marker',key)
        source,answer=first_pass_captures[key]
        assert values(row)==values(answer) and source['source_sha256']==row['source_sha256']
        assert source['source_xml']==body
        assert source['source_notes_xml'].strip()==source_notes(db,*key).strip()
        first_pass_null_marker.append(dict(code_id=key[0],source_id=key[1],classification='captured_first_pass_not_independent_review'))
        continue
    fingerprint=digest(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':')))
    if (key,fingerprint) not in replacements:
        assert refs.key(row) in approval['approved_refreshed_identifiers']
        owner=owners[key];assert owner in recertified_files
        assert digest((ROOT/owner).read_bytes())==recertified_files[owner]
        matches=[old for old in archive_entries.get(key,[]) if
            {k:v for k,v in old.items() if k not in {'reference_checks','reference_coherence'}} ==
            {k:v for k,v in row.items() if k not in {'reference_checks','reference_coherence'}}]
        assert len(matches)==1, ('No exact archive plus bounded metadata receipt',key)
        assert any((x['code_id'],x['source_id'])==key and x['prior_checked'] is True and
                   x['proposed_sha256']==digest(row['proposed_xml']) for x in receipt['checks'])
        metadata_only_history.append(dict(code_id=key[0],source_id=key[1],owner=owner,
            recertification_receipt=recapture['receipt_path'],owning_file_sha256=recertified_files[owner],
            changed_fields=['reference_checks','reference_coherence'],legal_text_or_impact_changed=False))
    reviewed_rows+=1
db.rollback();db.close()

for path,expected in stable.items():assert digest(path.read_bytes()) == expected, ('Intervening evidence',str(path))
for name,expected in pins.items():assert digest((ROOT/name).read_bytes()) == expected, ('Intervening code/policy',name)
assert {x['file'] for x in files} == {str(p.relative_to(ROOT)) for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name)}
report=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.time()-started,
    coordinator_pid=3122,exit_receipt_temporally_bound_to_last_alive=True,pause_owner=pause['owner'],
    pins=pins,input_hashes={str(p.relative_to(ROOT)):v for p,v in stable.items()},
    canonical_identities=len(canonical),canonical_collections=9,validated_batch_records=len(records),
    validated_batch_files=len(files),exact_db_registry_batch_source_mirrors=True,
    preserved_unowned_legacy=unowned,reference_certificates=dict(certificate_counts),
    pending_reference_details=pending_refs,registration_intents=dict(intents),intent_details=intent_details,
    checked_review_archive_files=len(archive_files),current_review_rows_with_exact_beforeimages=reviewed_rows,
    historical_metadata_only_recertifications=metadata_only_history,captured_first_pass_null_markers=first_pass_null_marker,
    immutable_queue_partition=dict(scheduled=dict(Counter(k[0] for k in scheduled)),terminal=dict(Counter(k[0] for k in terminal)),never_admitted=dict(Counter(k[0] for k in unadmitted)),unknown_jobs=0),
    diagnostics_count=len(diagnostics),canonical_mutations=0,production_sqlite_read_only=True,
    legal_convergence_claimed=False,second_pass_transfer_ready=False)
with OUTPUT.open('x') as stream:json.dump(report,stream,ensure_ascii=False,indent=2)
note(json.dumps({k:v for k,v in report.items() if k not in ['pins','input_hashes','pending_reference_details','intent_details']},ensure_ascii=False))
