"""Full read-only technical reconciliation for a future coordinated transfer.

This module has no production activator. The original production controller
continues to refuse before collection. No supplied JSON approves a mismatch.
Each invocation reads current SQLite and owner files again; old certificates
remain classified as pending convergence, never treated as legally current.
"""
from pathlib import Path
from collections import Counter
import datetime, hashlib, importlib, json, re, sqlite3, sys, time
import xml.etree.ElementTree as ET
import types
from review_worklist import native_reviews, fingerprint as worklist_fingerprint, matches as worklist_matches

LEDGER_SHA='0f23741391f96834a9e2d8db569bc06da450d47805989f641d44a28755ca1272'
CANONICAL_COUNT=30317

def digest(value):
    return hashlib.sha256(value if isinstance(value,bytes) else (value or '').encode()).hexdigest()

def values(row):
    return (row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes'])


def _partition(ROOT,db,read,canonical,all_drafts,ingest,assets):
    source_notes,inventory=ingest.source_notes,ingest.inventory
    xml_contents,text_of=ingest.xml_contents,ingest.text_of
    config = read(ROOT/'corpus.json')
    specs = config['codes'] + config.get('annexes', [])
    assert len(specs) == 9 and len({x['id'] for x in specs}) == len({x['slug'] for x in specs}) == 9
    corpus = ROOT.parent/'sites/liberer-la-retraite/dist/corpus'
    coverage = read(corpus/'coverage.json')
    assert coverage['sources_complete'] is True and coverage['missing_archives'] == []
    covered = {x['slug']: x for x in coverage['codes']}
    assert set(covered) == {x['slug'] for x in specs} and len(coverage['codes']) == 9
    actual_keys = set(); held=[]; accessible=[]; inventory_counts={}
    companions = assets.load_companions(ROOT/'attachments')
    for spec in specs:
        slug, code = spec['slug'], spec['id']
        rows = read(corpus/(slug+'.json')); tree = inventory(db, code, coverage['as_of'])
        assert not tree['missing_sections'] and not tree['missing_articles']
        ids = [x['source_id'] for x in rows]
        assert len(ids) == len(set(ids)) and set(ids) == set(tree['article_ids'])
        cv = covered[slug]
        assert cv['inventory_reconciled'] is True
        assert cv['expected_articles'] == cv['imported_versions'] == len(ids) > 0
        inventory_counts[slug]=len(ids)
        for source in rows:
            key=(source['code_id'], source['source_id']); assert key[0] == code
            assert key not in actual_keys and key in canonical; actual_keys.add(key)
            full = db.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", key).fetchone()
            assert full and digest(full[0]) == full[1] == source['source_sha256'] == canonical[key]['source_sha256']
            element=ET.fromstring(full[0]); meta='META/META_SPEC/META_ARTICLE/'
            expected=(xml_contents(element.find('BLOC_TEXTUEL/CONTENU')),text_of(element,meta+'DATE_DEBUT'),text_of(element,meta+'DATE_FIN'),text_of(element,meta+'NUM'))
            actual=db.execute('SELECT content_xml,valid_from,valid_until,number FROM articles WHERE code_id=? AND id=?',key).fetchone()
            assert actual == expected == (source['source_xml'],source['valid_from'],source['valid_until'],source['number'])
            assert source_notes(db,*key) == source['source_notes_xml']
            if key not in all_drafts:
                item=dict(slug=slug,code_id=key[0],source_id=key[1],source_sha256=source['source_sha256'])
                if assets.graphic_markers(source['source_xml']) and not assets.recovery_complete(source['source_xml'],companions.get(key)):
                    held.append(item)
                else: accessible.append(item)
            else:
                v=all_drafts[key]
                assert v[0] == source['source_sha256'] and (v[2] or v[1]=='retained_unchanged')
    assert actual_keys == set(canonical)
    return inventory_counts,held,accessible


def first_pass_inventory(root,pins):
    """Pre-drain coverage only, while a valid review may still stage a commit.

    Whole-source/NOTA/version guards and all nine immutable inventories are
    checked. Batch/DB mirrors can temporarily differ inside a guarded review
    write; the full reconciliation is mandatory again after natural exit.
    """
    if not __debug__:raise RuntimeError('Assertions must be active')
    ROOT=Path(root).resolve();stable={}
    def read(path):
        path=Path(path);assert path.resolve().is_relative_to(ROOT.parent) and path.is_file() and not path.is_symlink()
        data=path.read_bytes();stable[path]=digest(data);return json.loads(data)
    for name,h in pins.items():assert digest((ROOT/name).read_bytes())==h
    sys.path.insert(0,str(ROOT));sys.dont_write_bytecode=True
    try:
        for name in ['ingest','source_assets']:
            old=sys.modules.get(name)
            if old is not None and Path(old.__file__).resolve().parent!=ROOT:raise RuntimeError('Foreign source module')
        ingest=importlib.import_module('ingest');assets=importlib.import_module('source_assets')
        ledger_path=ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/current-article-ledger.jsonl'
        data=ledger_path.read_bytes();assert digest(data)==LEDGER_SHA
        stable[ledger_path]=digest(data)
        ledger=[json.loads(line) for line in data.splitlines()];canonical={(x['code_id'],x['source_id']):x for x in ledger}
        assert len(canonical)==len(ledger)==CANONICAL_COUNT
        db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True)
        try:
            db.execute('BEGIN')
            drafts={(c,i):(sha,st,body,reason,notes) for c,i,sha,st,body,reason,notes in db.execute('SELECT code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes FROM drafts')}
            counts,held,accessible=_partition(ROOT,db,read,canonical,drafts,ingest,assets)
        finally:db.close()
        for path,h in stable.items():assert digest(path.read_bytes())==h
        for name,h in pins.items():assert digest((ROOT/name).read_bytes())==h
        return dict(canonical_identities=len(canonical),collections=counts,accessible_first_pass_pending=accessible,documentary_holds=held,
                    all_accessible_first_passes_registered=not accessible,full_registration_reconciliation_still_required_after_exit=True,
                    canonical_mutations=0,input_hashes={str(k.relative_to(ROOT.parent)):v for k,v in stable.items()})
    finally:sys.path.pop(0)

def collect(root,pins):
    if not __debug__: raise RuntimeError('Reconciliation requires active assertions')
    ROOT=Path(root).resolve(); started=time.time(); stable={}
    def read(path):
        path=Path(path)
        # Source export is a generated sibling of legal-rewrite; synced sources
        # are never edited or loaded as executable code.
        assert path.resolve().is_relative_to(ROOT.parent) and not path.is_symlink() and path.is_file()
        data=path.read_bytes();stable[path]=digest(data);return json.loads(data)
    def capture(path):
        path=Path(path)
        assert path.resolve().is_relative_to(ROOT.parent) and not path.is_symlink() and path.is_file()
        data=path.read_bytes();stable[path]=digest(data);return data
    def note(message): pass
    def verify():
        for name, expected in pins.items():
            path=ROOT/name
            assert not Path(name).is_absolute() and '..' not in Path(name).parts
            assert path.resolve().is_relative_to(ROOT) and not path.is_symlink()
            assert digest(path.read_bytes())==expected, ('Pinned dependency changed',name)
        assert {str(p.relative_to(ROOT)) for p in (ROOT/'attachments/records').glob('*.json')} == {n for n in pins if n.startswith('attachments/records/')}
    verify()
    # Never reuse an imported module whose __file__ belongs to another root.
    sys.dont_write_bytecode=True
    sys.path.insert(0,str(ROOT))
    for name in ['ingest','source_assets','substantive_impact','register_batches','reference_coherence']:
        existing=sys.modules.get(name)
        if existing is not None and Path(existing.__file__).resolve().parent != ROOT:
            raise RuntimeError('Imported dependency belongs to another project: '+name)
    registration=importlib.import_module('register_batches')
    refs=importlib.import_module('reference_coherence');refs.focus.cache_clear()
    assets=importlib.import_module('source_assets')
    ingest=importlib.import_module('ingest')
    source_notes,source_evidence=ingest.source_notes,ingest.source_evidence
    inventory,xml_contents,text_of=ingest.inventory,ingest.xml_contents,ingest.text_of
    base=ROOT/'runtime/exhaustive'
    db=None
    try:
        registry = read(ROOT/'registered-batches.json')
        ledger_data = (ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/current-article-ledger.jsonl').read_bytes()
        assert digest(ledger_data) == LEDGER_SHA
        ledger = [json.loads(line) for line in ledger_data.splitlines()]
        canonical = {(x['code_id'],x['source_id']):x for x in ledger}
        assert len(canonical) == CANONICAL_COUNT and len({x['slug'] for x in ledger}) == 9
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

        inventory_counts,held,accessible=_partition(ROOT,db,read,canonical,all_drafts,ingest,assets)
        note('Inventorying current reference certificates; stale targets remain pending')
        catalog = refs.focus(); certificate_counts = Counter(); pending_refs=[]; reference_views={}; target_cache={}
        for key,(row,body,start,end) in records.items():
            article = {'code_id':key[0],'source_id':key[1],'number':row['number'],'source_xml':body,'source_notes_xml':source_notes(db,*key)}
            needed = refs.requirements(article,row['proposed_xml'],catalog,db)
            for target in needed:
                if target not in target_cache:target_cache[target]=refs.state(db,target)
            reference_views[key]={target:target_cache[target] for target in sorted(needed)}
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
        intents = Counter(); intent_details=[]; historical_intent_rows=[]
        for path in sorted((base/'jobs').glob('*/registration-intent.json')):
            intent = read(path); current=historical=absent=0
            assert len({(x['code_id'],x['source_id']) for x in intent['rows']})==len(intent['rows'])
            for field,filename in [('source_sha256','source.json'),('reference_sha256','reference-targets.json')]:
                evidence=path.parent/filename
                read(evidence);assert stable[evidence]==intent[field]
            intended_batch=Path(intent['batch_path'])
            assert intended_batch.resolve().is_relative_to(ROOT/'batches') and not intended_batch.is_symlink()
            for row in intent['rows']:
                key=row['code_id'],row['source_id'];value=all_drafts.get(key)
                if value is None:absent+=1;continue
                assert value[0] == row['source_sha256'], ('Intent source mismatch',key)
                if value == values(row):current+=1
                else:
                    assert key in records and all_drafts[key] == values(records[key][0])
                    historical+=1;historical_intent_rows.append(row)
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
        archive_entries={};whole_archive_entries={}
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
                whole_archive_entries.setdefault(key,[]).append(entry)
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
        beforeimages={}
        for path in archive_files:
            for archived in read(ROOT/path):
                key=(archived['code_id'],archived['source_id'])
                beforeimages.setdefault(key,[]).append(values(archived))
        for row in historical_intent_rows:
            key=(row['code_id'],row['source_id'])
            assert values(row) in beforeimages.get(key,[]), ('Historical intent lacks exact archived beforeimage',key)
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

        # The prior manifest is an old work list, not proof of coverage for all
        # later first passes. Every canonical identity gets an explicit state.
        manifest=read(ROOT/'runtime/radical-review-20261019.json')
        prior={}
        for row in manifest['prior_articles']:
            key=(row['code_id'],row['source_id']); assert key not in prior
            assert row['review_status'] in {'pending','completed'};prior[key]=row
        parser=types.ModuleType('_worklist_native_parser')
        exec(compile(capture(ROOT/'worker_execution.py'),str(ROOT/'worker_execution.py'),'exec'),parser.__dict__)
        independent,unproven_native=native_reviews(ROOT,read,capture,canonical,records,whole_archive_entries,db,ingest,parser,refs)
        passes=Counter(); second_pass=[]; worklist_blockers=[]
        bounded_recertifications={(x['code_id'],x['source_id']) for x in metadata_only_history}
        for key in sorted(canonical):
            row=records.get(key,(None,))[0]
            old=prior.get(key)
            exact_review=bool(row and row.get('prior_proposal_sha256') and
                              ((key,digest(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':')))) in replacements or key in bounded_recertifications))
            # A native archive of a whole row is technical evidence, not a
            # current-target legal certificate. Legacy completed flags alone
            # stay open until independently anchored, including ownerless rows.
            state=('first_pass_open' if key not in all_drafts else
                   'whole_row_review_beforeimage_present' if exact_review else
                   'legacy_review_flag_needs_reconciliation' if old and old['review_status']=='completed' else
                   'independent_second_pass_required')
            passes[state]+=1
            draft=all_drafts.get(key)
            fingerprint=dict(code_id=key[0],source_id=key[1],state=state,source_sha256=canonical[key]['source_sha256'],
                proposed_sha256=digest(draft[2]) if draft else None,reason_sha256=digest(draft[3]) if draft else None,
                review_notes_sha256=digest(draft[4]) if draft else None,owner=owners.get(key),
                batch_row_sha256=digest(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':'))) if row else None)
            full=db.execute("SELECT sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()
            version=db.execute('SELECT content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
            if key not in reference_views:
                article=dict(code_id=key[0],source_id=key[1],number=canonical[key]['number'],source_xml=version[0],source_notes_xml=source_notes(db,*key))
                needed=refs.requirements(article,draft[2] if draft else None,catalog,db)
                for target in needed:
                    if target not in target_cache:target_cache[target]=refs.state(db,target)
                reference_views[key]={target:target_cache[target] for target in sorted(needed)}
            fingerprint['current_guard']=dict(source_sha256=full[0],source_xml_sha256=digest(version[0]),
                source_notes_sha256=digest(source_notes(db,*key)),valid_from=version[1],valid_until=version[2],
                draft_status=draft[1] if draft else None,proposed_sha256=fingerprint['proposed_sha256'],
                reason_sha256=fingerprint['reason_sha256'],review_notes_sha256=fingerprint['review_notes_sha256'],
                owner=fingerprint['owner'],batch_row_sha256=fingerprint['batch_row_sha256'],
                policy_pins={n:h for n,h in pins.items() if n in {'policy-coordinations.json','site-summaries.json','reference-focus-extra.json'} or n.startswith('runtime/contrat-unique-20261019/priority/')},
                current_reference_target_views=reference_views[key],
                reference_certificate_sha256=worklist_fingerprint(row.get('reference_coherence')) if row else None)
            proof=independent.get(key)
            fingerprint['independent_review_evidence']=(proof|dict(current_guard_sha256=worklist_fingerprint(fingerprint['current_guard']))) if proof else None
            second_pass.append(fingerprint)
            if draft is not None:
                if old is None:worklist_blockers.append(fingerprint|dict(reason='canonical_identity_absent_from_current_review_worklist'))
                elif old['review_status']=='completed' and not exact_review:worklist_blockers.append(fingerprint|dict(reason='legacy_completed_flag_without_whole_current_beforeimage'))
                elif old['review_status']=='pending' and (old.get('source_sha256')!=draft[0] or old.get('proposed_sha256')!=digest(draft[2])):
                    worklist_blockers.append(fingerprint|dict(reason='pending_review_beforeimage_no_longer_current'))
        for path, expected in stable.items():
            assert digest(path.read_bytes())==expected, ('Evidence changed during collection',str(path))
        verify()
        assert {x['file'] for x in files} == {str(p.relative_to(ROOT)) for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name)}
        assert set(archive_files) == {str(p.relative_to(ROOT)) for p in (ROOT/'revisions/radical-review').glob('*.json')}
        assert {x['path'] for x in intent_details} == {str(p.relative_to(ROOT)) for p in (base/'jobs').glob('*/registration-intent.json')}
        result=dict(integrity_status='reconciled',ambiguities=[],checked_at_unix=time.time(),elapsed_seconds=time.time()-started,
            canonical_identities=len(canonical),collections=inventory_counts,
            accessible_first_pass_pending=accessible,documentary_holds=held,
            all_accessible_first_passes_registered=not accessible,
            validated_batch_records=len(records),validated_batch_files=len(files),
            input_hashes={str(p.relative_to(ROOT.parent)):v for p,v in stable.items()},pins=pins,
            preserved_legacy_unowned=unowned,historical_outside_canonical=[dict(code_id=k[0],source_id=k[1],draft_guards=v,counts_toward_current_canonical_coverage=False) for k,v in sorted(outside_guards.items())],reference_certificates=dict(certificate_counts),pending_reference_work=pending_refs,
            registration_intents=dict(intents),intent_details=intent_details,
            checked_review_archive_files=len(archive_files),current_review_rows_with_beforeimages=reviewed_rows,
            historical_metadata_only_recertifications=metadata_only_history,captured_first_pass_null_markers=first_pass_null_marker,
            required_second_pass_states=dict(passes),required_second_pass_dispositions=second_pass,
            required_second_pass_worklist_ready=not worklist_blockers,required_second_pass_worklist_blockers=worklist_blockers,
            canonical_mutations=0,production_sqlite_read_only=True,legal_convergence_claimed=False,second_pass_completion_claimed=False,
            independent_native_review_rows=len(independent),unproven_historical_native_reviews=unproven_native,
            review_manifest_sha256=stable[ROOT/'runtime/radical-review-20261019.json'])
        # Initial proof is sufficient to prepare a new list, never to launch it.
        # Recollection after publication verifies every current identity again.
        if manifest.get('complete_canonical_worklist'):
            result['required_second_pass_worklist_ready']=worklist_matches(result,manifest)
        return result
    finally:
        if db is not None: db.close()
        if sys.path[0]==str(ROOT): sys.path.pop(0)
