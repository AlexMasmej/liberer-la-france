"""Small operational coverage ledger; no legal-reference audit or DB snapshot."""
from pathlib import Path
import collections,datetime,hashlib,json,sqlite3

ROOT=Path(__file__).resolve().parents[3]
HERE=ROOT/'legal-rewrite'
OUT=Path(__file__).resolve().parent
CORPUS=ROOT/'sites/liberer-la-retraite/dist/corpus'
def sha(value):return hashlib.sha256(value).hexdigest()
def dump(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

started=datetime.datetime.now(datetime.timezone.utc).isoformat()
policy_path=HERE/'runtime/radical-review-20261019.json'
prior_raw=policy_path.read_bytes();prior=json.loads(prior_raw)
prior_by_key={(a['code_id'],a['source_id']):a for a in prior['prior_articles']}
assert len(prior_by_key)==len(prior['prior_articles'])
config=json.loads((HERE/'corpus.json').read_bytes())
coverage=json.loads((CORPUS/'coverage.json').read_bytes())
expected={a['slug']:a['expected_articles'] for a in coverage['codes']}
sources={};source_files=[]
for spec in config['codes']+config['annexes']:
    path=CORPUS/(spec['slug']+'.json');raw=path.read_bytes();rows=json.loads(raw)
    assert len(rows)==expected[spec['slug']]
    for row in rows:
        identity=(row['code_id'],row['source_id'])
        assert identity not in sources and row['code_id']==spec['id']
        sources[identity]=(spec['slug'],row['source_sha256'],row['number'])
    source_files.append({'path':str(path),'bytes':len(raw),'sha256':sha(raw),'entries':len(rows)})
assert len(sources)==sum(expected.values())==30317
db=sqlite3.connect((HERE/'corpus.sqlite').resolve().as_uri()+'?mode=ro',uri=True,timeout=15)
try:
    db.execute('BEGIN')
    canonical={(code,identifier):(fingerprint,number) for code,identifier,fingerprint,number in db.execute('SELECT code_id,id,source_sha256,number FROM articles')}
    drafts={}
    for code,identifier,fingerprint,status,body,reason,notes in db.execute('SELECT code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes FROM drafts'):
        drafts[(code,identifier)]={'source_sha256':fingerprint,'status':status,'body_present':bool(body),
                                  'proposal_sha256':sha((body or '').encode()),'reason_sha256':sha((reason or '').encode()),'notes_sha256':sha((notes or '').encode())}
finally:db.close()
counts=collections.Counter();by_code={slug:collections.Counter() for slug in expected}
with (OUT/'current-article-ledger.jsonl').open('w') as stream:
    for identity,(slug,fingerprint,number) in sorted(sources.items()):
        assert canonical.get(identity)==(fingerprint,number)
        draft=drafts.get(identity);entry=prior_by_key.get(identity)
        completed_first=bool(draft and draft['source_sha256']==fingerprint and (draft['body_present'] or draft['status']=='retained_unchanged'))
        first='pending_first_pass' if not completed_first else ('retained_unchanged' if draft['status']=='retained_unchanged' else 'rewrite_draft')
        review=entry.get('review_status') if entry else 'outside_initial_prior_manifest'
        counts[(first,review)]+=1;by_code[slug][(first,review)]+=1
        stream.write(json.dumps({'slug':slug,'code_id':identity[0],'source_id':identity[1],'number':number,
                                'source_sha256':fingerprint,'first_pass_status':first,'prior_manifest_review_status':review,
                                'draft_guards':draft,'independent_current_second_pass_proven_by_this_inventory':False},ensure_ascii=False)+'\n')
outside=[{'code_id':identity[0],'source_id':identity[1],'draft_guards':draft,'counted_in_current_canonical_coverage':False} for identity,draft in drafts.items() if identity not in sources]
dump('outside-current-inventory.json',outside)
stable=policy_path.read_bytes()==prior_raw
summary={'captured_at_utc':started,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'source_records':len(sources),'collections':expected,'current_source_identity_hashes_match_export':True,
         'first_pass_covered':sum(n for (first,review),n in counts.items() if first!='pending_first_pass'),
         'pending_first_pass':sum(n for (first,review),n in counts.items() if first=='pending_first_pass'),
         'prior_review_status_counts':dict(collections.Counter(a['review_status'] for a in prior['prior_articles'])),
         'coverage_by_first_pass_and_initial_manifest':[{'first_pass':first,'initial_manifest':review,'articles':n} for (first,review),n in sorted(counts.items())],
         'by_code':{slug:[{'first_pass':first,'initial_manifest':review,'articles':n} for (first,review),n in sorted(values.items())] for slug,values in by_code.items()},
         'outside_current_inventory_drafts_preserved':len(outside),'prior_manifest_stable_during_read':stable,
         'database_and_manifest_not_one_transactional_resource':True,'read_only_database':True,'writer_lock_acquired':False,'snapshot_created':False,
         'initial_prior_manifest_covers_all_current_entries':set(sources)<=set(prior_by_key),
         'initial_manifest_scope':'Prior drafts requiring a new substantive pass after the 19 October directive; not all later first-pass entries.',
         'not_in_initial_manifest_does_not_establish_missing_first_pass_validation':True,
         'completed_marker_alone_does_not_prove_current_full_review_or_reference_freshness':True,
         'future_closure_must_reconcile_each_required_second_pass_against_current_source_proposal_policy_and_targets':True,
         'no_extra_review_job_created_or_counted_as_completed':True,'no_legal_error_or_jurist_validation_claim':True,
         'not_a_replacement_for_the_global_reference_audit':True,'prior_manifest_sha256':sha(prior_raw),'source_file_guards':source_files}
dump('summary.json',summary)
(OUT/'initial-prior-manifest.json').write_bytes(prior_raw)
dump('artifact-manifest.json',[{'path':str(p.relative_to(OUT)),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='artifact-manifest.json'])
print(json.dumps({k:summary[k] for k in ['source_records','first_pass_covered','pending_first_pass','prior_review_status_counts','outside_current_inventory_drafts_preserved','prior_manifest_stable_during_read']},ensure_ascii=False))
