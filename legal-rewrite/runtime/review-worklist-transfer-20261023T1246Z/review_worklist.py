"""Current whole-corpus worklist, prepared offline; no production entry point.

The controller supplies a fresh, fully reconciled observation under exclusion.
The publication is journalled by that controller, never by this pure builder.
Historical completion flags, metadata repairs and reference-only checks cannot
certify an independent substantive second pass.
"""
import copy, hashlib, json
from collections import Counter
from pathlib import Path

WORKLIST='runtime/radical-review-20261019.json'
SCHEMA='whole-canonical-second-pass-20261023-v1'

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def build(proof,previous,owner):
    if (proof.get('integrity_status')!='reconciled' or proof.get('ambiguities')!=[] or
            proof.get('all_accessible_first_passes_registered') is not True):
        raise ValueError('Fresh complete reconciliation and accessible first-pass coverage required')
    if not isinstance(owner,str) or not owner:raise ValueError('Publication owner required')
    dispositions=proof['required_second_pass_dispositions']
    keys=[(r['code_id'],r['source_id']) for r in dispositions]
    if len(set(keys))!=len(keys) or len(keys)!=proof['canonical_identities']:
        raise ValueError('Canonical identity inventory is incomplete or duplicated')
    held={(x['code_id'],x['source_id']) for x in proof['documentary_holds']}
    old={}
    for row in previous['prior_articles']:
        key=(row['code_id'],row['source_id'])
        if key in old:raise ValueError('Duplicate historical review identity')
        old[key]=row
    required=[];holds=[]
    for source in dispositions:
        key=source['code_id'],source['source_id'];row=copy.deepcopy(source)
        if source['state']=='first_pass_open':
            if key not in held:raise ValueError('Accessible or unclassified first pass remains open')
            row.update(review_status='documentary_hold_unverified',counts_as_verified=False)
            holds.append(row);continue
        if key in held:raise ValueError('Held identity contradicts first-pass disposition')
        if not isinstance(source.get('current_guard'),dict):raise ValueError('Whole current guard is absent')
        evidence=source.get('independent_review_evidence')
        completed=bool(evidence)
        if completed and evidence.get('current_guard_sha256')!=fingerprint(source['current_guard']):
            raise ValueError('Independent review is attached to a different current whole row')
        row.update(review_status='completed' if completed else 'pending',
                   previous_policy_review_status=old.get(key,{}).get('review_status'),
                   coverage_guard_sha256=fingerprint(source['current_guard']))
        required.append(row)
    if set(keys)!={(x['code_id'],x['source_id']) for x in required+holds}:
        raise ValueError('Worklist lost a canonical identity')
    # Keep the previous policy/instruction fields, and the entire previous
    # document in the controller's durable before-image, under its byte hash.
    result=copy.deepcopy(previous)
    result.update(prior_articles=required,documentary_holds=holds,
        historical_outside_current_inventory=copy.deepcopy(proof.get('historical_outside_canonical',[])),
        outside_current_inventory=[copy.deepcopy(v) for k,v in old.items() if k not in set(keys)],
        current_review_inventory_entries=len(required),prior_current_articles=len(required),
        completed_second_pass=sum(x['review_status']=='completed' for x in required),
        complete_canonical_worklist=dict(schema=SCHEMA,publication_owner=owner,
            canonical_identities=len(keys),collections=proof['collections'],
            registered_identities=len(required),documentary_holds_unverified=len(holds),
            prior_manifest_sha256=proof['review_manifest_sha256'],
            canonical_dispositions_sha256=fingerprint(dispositions),
            policy_and_code_pins=copy.deepcopy(proof['pins']),
            classifications=dict(Counter(x['review_status'] for x in required)),
            legal_convergence_claimed=False,human_legal_validation_claimed=False))
    return result

def matches(proof,manifest):
    """Recompute from current files; a saved ready flag cannot approve a list."""
    publication=manifest.get('complete_canonical_worklist')
    if not isinstance(publication,dict) or publication.get('schema')!=SCHEMA:return False
    # Rebuilding uses the present document only for its preserved policy fields
    # and historical annotations; the covered rows all come from fresh proof.
    expected=build(proof,manifest,publication['publication_owner'])
    actual={(r['code_id'],r['source_id']):r for r in manifest['prior_articles']}
    wanted={(r['code_id'],r['source_id']):r for r in expected['prior_articles']}
    if len(actual)!=len(manifest['prior_articles']) or set(actual)!=set(wanted):return False
    for key,row in wanted.items():
        present=actual[key]
        for field in ['source_sha256','proposed_sha256','reason_sha256','review_notes_sha256',
                      'owner','batch_row_sha256','current_guard','coverage_guard_sha256',
                      'independent_review_evidence','review_status']:
            if present.get(field)!=row.get(field):return False
    if manifest.get('documentary_holds')!=expected['documentary_holds']:return False
    if manifest.get('historical_outside_current_inventory')!=expected['historical_outside_current_inventory']:return False
    for field in ['canonical_identities','collections','registered_identities','documentary_holds_unverified',
                  'classifications']:
        if publication.get(field)!=expected['complete_canonical_worklist'][field]:return False
    return (publication.get('policy_and_code_pins')==proof['pins'] and
        manifest.get('completed_second_pass')==expected['completed_second_pass'] and
        manifest.get('current_review_inventory_entries')==len(wanted) and manifest.get('prior_current_articles')==len(wanted))

def native_reviews(root,read,capture,canonical,records,archive_entries,db,ingest,parser,refs):
    """One pass over accepted metrics and saved jobs, with current owner checks.

    Missing or obsolete historical evidence stays pending, with an explicit
    reason. Structural source/owner/archive integrity is checked by the caller.
    No authenticated call, writable database, CLI launch or policy change.
    """
    root=Path(root);base=root/'runtime/exhaustive';data=capture(base/'job-metrics.jsonl')
    if not data.endswith(b'\n'):raise ValueError('Incomplete metrics snapshot')
    metrics=[json.loads(line) for line in data.splitlines()]
    sessions={}
    for m in metrics:
        session=m.get('execution_session_id')
        if session:sessions.setdefault(session,set()).add(m.get('job'))
    candidates=[m for m in metrics if m.get('kind')=='review' and m.get('outcome')=='reviewed']
    proofs={};pending=[]
    current_policy=read(root/'policy-coordinations.json');current_sites=read(root/'site-summaries.json')
    for metric in candidates:
        name=metric.get('job')
        if not isinstance(name,str) or Path(name).name!=name:raise ValueError('Ambiguous accepted review job owner')
        folder=base/'jobs'/name
        def skip(reason):pending.append(dict(job=name,reason=reason))
        if name.startswith('reference-review-'):skip('reference_only_not_substantive_second_pass');continue
        required=['source.json','answer.json','coordination.json','policy.json','policy-fingerprint.json',
                  'reference-targets.json','execution-observed-'+str(metric.get('attempts'))+'.json']
        if any(not (folder/n).is_file() for n in required):skip('historical_job_evidence_incomplete');continue
        sources=read(folder/'source.json');answer=read(folder/'answer.json')
        source_map={(x['code_id'],x['source_id']):x for x in sources}
        answers={(x['code_id'],x['source_id']):x for x in answer}
        if len(source_map)!=len(sources) or len(answers)!=len(answer) or set(source_map)!=set(answers) or metric['articles']!=len(sources):
            raise ValueError('Historical accepted review assignments are ambiguous')
        if any(x.get('reference_recheck_only') for x in sources):skip('reference_only_not_substantive_second_pass');continue
        coord=read(folder/'coordination.json');policy=read(folder/'policy.json');pin=read(folder/'policy-fingerprint.json')
        if (coord!=current_policy or policy!=current_sites or pin.get('radical_review') is not True or
                pin.get('coordination_sha256')!=hashlib.sha256(capture(folder/'coordination.json')).hexdigest()):
            skip('historical_policy_not_current');continue
        snapshot=read(folder/'reference-targets.json')
        try:
            refs.check_guards(db,snapshot)
            refs.accept_checks(answer,sources,snapshot,refs.focus())
        except ValueError:
            skip('historical_reference_guards_or_assessments_not_current');continue
        observed=read(folder/required[-1]);log=Path(observed['source_log'])
        if log.parent.resolve()!=folder.resolve() or not log.is_file():skip('native_log_owner_missing_or_different');continue
        capture(log)
        native=parser.verify_execution(folder,stderr_path=log);session=native.get('session_id')
        if not native.get('verified') or session!=metric.get('execution_session_id') or sessions.get(session)!={name}:
            skip('distinct_native_response_unverified');continue
        if not 0<metric.get('started_at_unix',0)<=metric.get('finished_at_unix',0):
            skip('accepted_review_temporal_order_unverified');continue
        for key,source in source_map.items():
            if key not in canonical or key not in records:continue
            row,body,start,end=records[key];raw=answers[key];prior=source.get('previous_draft')
            fields=lambda r:(r['source_sha256'],r.get('status','rewrite_draft'),r['proposed_xml'],r['reason'],r['review_notes'])
            if prior is None or fields(raw)!=fields(row):continue
            if any(raw[k]!=row.get(k) for k in raw if k not in {'reference_coherence','policy_review_id','prior_proposal_sha256'}):continue
            if (source['source_sha256'],source['source_xml'],source['source_notes_xml'],source['valid_from'],source['valid_until'])!=(row['source_sha256'],body,ingest.source_notes(db,*key),start,end):continue
            matches=[a for a in archive_entries.get(key,[]) if a['replacement']==row and fields(a)==fields(prior)]
            if len(matches)!=1:continue
            prior_sha=hashlib.sha256((prior['proposed_xml'] or '').encode()).hexdigest()
            if prior_sha!=prior.get('proposed_sha256') or prior_sha!=row.get('prior_proposal_sha256'):continue
            proof=dict(job=name,coordinator_pid=metric['coordinator_pid'],native_session_id=session,
                accepted_at_unix=metric['finished_at_unix'],native_header_sha256=native['header_sha256'],
                archived_whole_beforeimage_sha256=fingerprint(matches[0]),
                source_job_sha256=hashlib.sha256(capture(folder/'source.json')).hexdigest(),
                answer_job_sha256=hashlib.sha256(capture(folder/'answer.json')).hexdigest())
            if key in proofs and proofs[key]!=proof:raise ValueError('Multiple independent proofs claim one exact current row')
            proofs[key]=proof
    return proofs,pending
