"""Ordinary global validation of nine staged candidates, with no registration.

Only changed batch copies and links to pinned untouched files are staged.
No writer, admission, manual reservation, canonical DB or completed flag changes.
"""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,re,sqlite3,sys,time
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime'
def sha(b):return hashlib.sha256(b).hexdigest()
def encoded(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def put(n,o):
    with (OUT/n).open('xb') as f:f.write(encoded(o))
def read(p):return json.loads(p.read_bytes())
def verify(folder,h):
    b=(folder/'artifact-manifest.json').read_bytes();assert sha(b)==h
    for n,i in json.loads(b)['files'].items():
        b=(folder/n).read_bytes();assert len(b)==i['bytes'] and sha(b)==i['sha256'],n
preps=[('coherence-coordination-guarded-preparation-20261023T221149Z','4de88c844136845c298fcc498ad8dc5ffdb8da3ecb33fa33d261b2408adc90a2'),
       ('cross-border-ordinary-preparation-20261024T0005Z','7e27cd7b59183a23ea3dae9311a3542880ab243a34ec9698377f9d5e3c4ab1c9'),
       ('urbanisme-procedure-coherence-followup-20261024T0112Z','79fa7bc78a43d13fa1cb1c07cea7c77d480a716c4478e43ae215402bbcc8687c')]
for folder,h in preps:verify(R/folder,h)
pins=read(R/'coherence-rollout-20261023T2042Z/resumption-observation-pins-v4.json')
pins['run_exhaustive.py']='d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
sys.path.insert(0,str(ROOT))
import run_exhaustive as runner,reference_coherence as refs,review_prior
from ingest import source_notes
from register_batches import validate_batches
sources=[];answers=[];original_owners={}
for folder,h in preps:
    p=R/folder;sources+=read(p/'source.json');answers+=read(p/'candidate-answer.json')
    owners=read(p/'whole-owner-beforeimage.json') if folder.startswith('urbanisme') else read(p/'whole-owner-beforeimages.json')
    if folder.startswith('urbanisme'):owners=[owners]
    elif folder.startswith('cross-border'):
        assert isinstance(owners,dict) and len(owners)==5
        owners=[dict(whole_owner_row=x['whole_row']) for x in owners.values()]
    for x in owners:
        row=x['whole_owner_row'];k=(row['code_id'],row['source_id']);assert k not in original_owners;original_owners[k]=row
key=lambda a:(a['code_id'],a['source_id'])
by_key={key(a):copy.deepcopy(a) for a in answers};source_map={key(a):a for a in sources}
assert len(by_key)==len(answers)==len(sources)==9 and set(by_key)==set(source_map)==set(original_owners)
registry_b=(ROOT/'registered-batches.json').read_bytes();registry=json.loads(registry_b)
work_b=(R/'radical-review-20261019.json').read_bytes();work={key(a):a for a in json.loads(work_b)['prior_articles']}
paths=sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
hashes={};changed={};owners={}
for p in paths:
    b=p.read_bytes();hashes[p]=sha(b);rows=json.loads(b)
    replacements=[]
    for index,row in enumerate(rows):
        k=key(row)
        if k not in by_key:continue
        assert k not in owners,k
        assert row==original_owners[k],('Whole owner changed',k)
        assert registry['|'.join(k)]=={'source_sha256':row['source_sha256'],'proposed_sha256':runner.digest(row['proposed_xml'])}
        owners[k]=dict(path=str(p),index=index,whole_row=copy.deepcopy(row),row_sha256=review_prior.batch_row_sha256(row))
        replacements.append(dict(index=index,key=list(k)))
        rows[index]=by_key[k]
    if replacements:changed[p]=dict(rows=rows,replacements=replacements)
assert set(owners)==set(by_key)
db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=15)
db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
try:
    for k,a in source_map.items():
        assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',k).fetchone()==(a['source_sha256'],a['source_xml'],a['valid_from'],a['valid_until']),k
        assert source_notes(db,*k)==a['source_notes_xml'],k
        actual=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
        assert actual==review_prior.draft_values(a['previous_draft'])==review_prior.draft_values(owners[k]['whole_row']),k
        assert a['previous_draft']['batch_row_sha256']==owners[k]['row_sha256'],k
    snapshot=refs.capture(db,sources,list(by_key.values()))
    # Existing analyses are retained only under exactly current target views.
    runner.validate_answer(list(by_key.values()),sources)
    refs.accept_checks(list(by_key.values()),sources,snapshot);refs.check_guards(db,snapshot)
    writes={refs.key(a) for a in sources};reads=set().union(*(set(v) for v in snapshot['requirements'].values()))-writes
    put('shared-footprint-preflight.json',dict(writes=sorted(writes),reads=sorted(reads),reservations_acquired=False,
        runtime_manual_guard='review_tail rejects new manual reservations; no bypass or admission closure attempted',
        safe_point_still_required=True))
    staged=OUT/'staged-batches';staged.mkdir()
    for p in paths:
        dest=staged/p.relative_to(ROOT/'batches');dest.parent.mkdir(parents=True,exist_ok=True)
        if p in changed:
            dest.write_bytes(encoded(changed[p]['rows']))
            (OUT/('whole-before-'+str(len([x for x in (OUT).glob('whole-before-*')]))+'.json')).write_bytes(p.read_bytes())
        else:dest.symlink_to(p)
    started=time.time()
    # validate_batches is the read-only function. _register(commit=False) is
    # deliberately not called because it writes batch-validation.json.
    records,diagnostics,files=validate_batches(db,staged)
    refs.check_guards(db,snapshot)
    for k,a in source_map.items():
        assert records[k][0]==by_key[k]
    result=dict(at_utc=datetime.now(timezone.utc).isoformat(),ordinary_global_validation_passed=True,
        validation_seconds=time.time()-started,authored_articles=len(records),batch_files=len(files),
        changed_batch_copies=len(changed),candidate_count=9,ordinary_answer_benefit_impact_reference_checks_passed=True,
        independent_semantic_review_or_jurist_validation=False,registered=False)
finally:db.close()
assert (ROOT/'registered-batches.json').read_bytes()==registry_b
assert (R/'radical-review-20261019.json').read_bytes()==work_b
assert paths==sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
for p,h in hashes.items():assert sha(p.read_bytes())==h,('Intervening batch write',str(p))
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
put('ordinary-global-validation.json',result)
put('global-validation-diagnostics.json',diagnostics)
put('current-pins.json',pins);put('reference-targets.json',snapshot)
put('source.json',sources);put('candidate-answer.json',list(by_key.values()))
put('whole-nine-owner-beforeimages.json',list(owners.values()))
put('current-batch-input-guards.json',[dict(path=str(p),sha256=h) for p,h in hashes.items()])
put('pending-independent-review-disposition.json',dict(candidates=[dict(code_id=k[0],source_id=k[1],current_status=work[k]['review_status'],
    parent_correction_is_not_native_completed=True,after_future_manual_correction_requires_fresh_pending_beforeimage_and_native_review=True) for k in by_key],
    worklist_bytes_unchanged=True,do_not_use_review_prior_commit_to_claim_native_review=True))
put('CONTROL.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),state='STAGED_NINE_CANDIDATES_GLOBAL_ORDINARY_PREFLIGHT_PASSED_NOT_REGISTERED',
    ordinary_global_validation=result,all_whole_source_NOTA_bounds_current_five_fields_whole_owners_registry_current_targets_77pins_match=True,
    no_fresh_semantic_reread_claimed=True,original_semantic_limits_preserved=True,
    canonical_mutations=0,models_launched=0,shared_reservations_acquired=0,admissions_changed=False,writer_lock_taken=False,
    review_prior_commit_not_called=True,no_completed_changed=True,
    production_controller_not_prepared_or_activated=True,
    remaining_gates=['first native accepted58195 proof and guarded rollout finalization','reviewed operational integration controller with isolated resume tests before any admission closure',
                    'fresh actual safe point with shared reservations and full guarded reconciliation','durable owner/file/registry/DB beforeimages and ordinary registration',
                    'keep parental corrections separate from required independent native second passes','fresh reconstruction and reference convergence after guarded registration'],
    global_legal_completion=False,jurist_validation=False))
print(json.dumps(result,ensure_ascii=False))
