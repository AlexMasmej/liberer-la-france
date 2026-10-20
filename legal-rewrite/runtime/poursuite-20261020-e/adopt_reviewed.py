"""E52 + bounded C141 adoption. Never run before explicit parent approval.

Only writes the audit ledger/history/receipt, under the shared writer lock.
Never writes SQLite, policy, sites or any frozen input. No work on import.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, copy, importlib.util, json, re, sqlite3, sys

P = Path(__file__).resolve().parent
B = P.parents[1]
sys.path.insert(0, str(B))
spec = importlib.util.spec_from_file_location('phase_c_primitives', P.parent / 'poursuite-20261020-c/adopt_reviewed.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
from ingest import source_notes, xml_contents
from register_batches import writer_lock
from substantive_impact import certificate, validate
from build_substantive_report import _checked
import reference_coherence as rc

BASE_LEDGER = '8b036b9f5ad1b63507f7c63eae890bcb0ace9e2741f155fde6ecc5ef81adf06e'
POLICY = {'policy-coordinations.json': 'a124c4c31a9ec9395f66ec470708878f2458bdee9ae8d72d6e36737f3ab7c14e',
          'site-summaries.json': '3a600ec16c3959a626e262d51b47fd7b99e7ce1c9c356ed228f9e3ad43e4f740'}
PACK_MANIFEST = '4c8108b377e075fedbff4201d76c46d6c28694e8177937bee33b5627916771f3'
SOCIAL = {'LEGITEXT000006073189|' + x for x in ('LEGIARTI000047437198', 'LEGIARTI000047437207', 'LEGIARTI000047480864')}
RECAPTURED = SOCIAL | {'LEGITEXT000006073189|LEGIARTI000053220874', 'LEGITEXT000006073189|LEGIARTI000047435216'}
L76 = 'LEGITEXT000006073189|LEGIARTI000041396065'
ALLOWED_TARGETS = {'LEGITEXT000006069577|' + x for x in ('LEGIARTI000042907661', 'LEGIARTI000006305938', 'LEGIARTI000022336384')} | {
    'LEGITEXT000006073189|' + x for x in ('LEGIARTI000041396065', 'LEGIARTI000047437198', 'LEGIARTI000047480864', 'LEGIARTI000053220874')}


def refresh_context_guards(audit, actual, allowed):
    """Pure: change only explicitly approved proposal pins, never own certificate."""
    updated = copy.deepcopy(audit)
    seen, changes = set(), []
    for old, new in zip(audit['dependency_guards'], updated['dependency_guards']):
        key = c.key(old)
        c.require(key not in seen, 'Duplicate old dependency: ' + key)
        seen.add(key)
        now = actual[key]
        if c.dependency_matches(old, now):
            continue
        c.require(key in allowed and c.dependency_matches(allowed[key], now), 'Unapproved context delta: ' + key)
        c.require(all(old.get(f) == now[f] for f in ('code_id', 'source_id', 'source_sha256', 'source_body_sha256', 'source_notes_sha256')),
                  'Context source/notes changed, not just proposal: ' + key)
        c.require('proposed_sha256' in old, 'Missing old proposal pin: ' + key)
        new['proposed_sha256'] = now['proposed_sha256']
        changes.append(dict(target_key=key, before=old['proposed_sha256'], after=new['proposed_sha256']))
    c.require({k: v for k, v in updated.items() if k != 'dependency_guards'} ==
              {k: v for k, v in audit.items() if k != 'dependency_guards'}, 'Own audit changed')
    return updated, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-approval', required=True)
    parser.add_argument('--execute-approved-adoption', action='store_true')
    args = parser.parse_args()
    c.require(args.execute_approved_adoption, 'Explicit parent execution switch required')
    with writer_lock():
        tracked = {}
        def read(path, sha=None):
            path = Path(path).resolve()
            c.require(path.is_relative_to(B.resolve()), 'Evidence outside legal-rewrite')
            raw = path.read_bytes()
            actual = c.sha_bytes(raw)
            c.require(sha is None or sha == actual, 'Changed evidence: ' + str(path))
            tracked[path] = actual
            return json.loads(raw)
        def frozen(folder, expected_sha=None):
            manifest = read(folder / 'manifest.json', expected_sha)
            for name, sha in manifest.get('files_sha256', manifest.get('files', {})).items():
                path = c.within(folder, name)
                c.require(c.file_sha(path) == sha, 'Frozen input changed: ' + str(path))
                tracked[path] = sha
            for name, sha in manifest.get('external_evidence', {}).items():
                path = c.within(B, name)
                c.require(c.file_sha(path) == sha, 'External proof changed: ' + name)
                tracked[path] = sha
            return manifest
        c.require(c.file_sha(Path(c.__file__)) == 'caa78ee474bc9c4aa573aed2f08dae3dd1de94ff0e2fd75cd44b1cb43c3ab9d4', 'C primitives changed')
        tracked[Path(c.__file__)] = c.file_sha(Path(c.__file__))
        approval_path = Path(args.root_approval).resolve()
        approval = read(approval_path)
        c.require(approval.get('approved') is True and approval.get('scope') == 'E52-and-C141-bounded-context', 'Missing parent approval')
        c.require(approval['helper_sha256'] == c.file_sha(Path(__file__)), 'Helper not approved')
        c.require(approval['policy_sha256'] == rc.policy_state() == POLICY, 'Policy changed')
        c.require(approval['base_ledger_sha256'] == BASE_LEDGER, 'Wrong approved prior ledger')
        pack = P / 'integration/edition001'
        frozen(pack, PACK_MANIFEST)
        c.require(approval['integration_manifest_sha256'] == PACK_MANIFEST, 'Wrong integration approval')
        sources, rows = read(pack / 'source.json'), read(pack / 'answer.json')
        pre = read(pack / 'preflight.json')
        maps = {x['referrer_key']: x for x in read(pack / 'article-dependency-map.json')['articles']}
        c.require(len(rows) == len(sources) == len(maps) == 52, 'Wrong E size')
        row_by, source_by = {c.key(x): x for x in rows}, {c.key(x): x for x in sources}
        c.require(len(row_by) == 52 and set(row_by) == set(source_by) == set(maps), 'E identity mismatch')
        for item in pre['pack_inputs']:
            folder = Path(item['path'])
            frozen(folder, item['manifest_sha256'])
            c.require(c.file_sha(folder / 'source.json') == item['source_sha256'] and c.file_sha(folder / 'answer.json') == item['answer_sha256'], 'Changed reviewed pack')
        proofs = []
        for item in pre['review_evidence']:
            proof = read(Path(item['path']), item['sha256'])
            c.require(str(proof.get('verdict', '')).startswith('approved') and not proof.get('blocking_findings') and not proof.get('concrete_defects'), 'Unapproved independent review')
            proofs.append(item)
        c.require(len(proofs) == 3, 'Need fiscal, housing and social independent reviews')
        registration = read(c.within(B, approval['registration_path']), approval['registration_sha256'])
        c.require(registration['registered_articles'] == 52 and registration['first_drafts'] == 49 and registration['revisions'] == 3, 'Wrong E receipt')
        c.require({c.key(x) for x in registration['checks']} == set(row_by), 'Receipt identity mismatch')
        for check in registration['checks']:
            c.require(check['source_and_notes_verified'] and check['prior_checked'] and check['proposed_sha256'] == c.digest(row_by[c.key(check)].get('proposed_xml')), 'Wrong registered E body')
        # Actual recapture/re-emission is mandatory. Its proof and metadata-only receipt are approved by the parent, never manufactured here.
        rec = approval['recapture']
        c.require(approval.get('actual_recapture_approved') is True, 'Parent has not reviewed actual recapture')
        for label in ('source', 'answer', 'snapshot', 'proof', 'receipt', 'capture', 'capture_approval'):
            rec[label] = read(c.within(B, rec[label + '_path']), rec[label + '_sha256'])
        c.require(rec['proof']['metadata_only'] is True and rec['proof']['articles'] == 5, 'Wrong staging proof')
        c.require(rec['proof']['capture_sha256'] == rec['capture_sha256'] and rec['proof']['approval_sha256'] == rec['capture_approval_sha256'], 'Staging lineage mismatch')
        producer = c.within(B, rec['helper_path'])
        c.require(c.file_sha(producer) == rec['helper_sha256'] == rec['proof']['helper_sha256'] == rec['capture']['helper_sha256'], 'Recapture producer changed')
        tracked[producer] = rec['helper_sha256']
        ca = rec['capture_approval']
        c.require(ca['approved'] is True and ca['approved_by'] == 'root' and ca['capture_sha256'] == rec['capture_sha256'], 'No real capture approval')
        c.require(ca['approved_optional_check_removals'] == rec['capture']['optional_checks_to_remove'], 'Optional-removal approval mismatch')
        cap_folder = c.within(B, rec['capture_path']).parent
        for name, sha in rec['capture']['files'].items():
            read(c.within(cap_folder, name), sha)
        before = {c.key(x): x for x in read(cap_folder/'before-answer.json')}
        for name,label in [('source.json','source'),('answer.json','answer'),('reference-targets.json','snapshot')]:
            c.require(rec['proof']['files'][name] == rec[label+'_sha256'], 'Staging output changed')
        refreshed = {c.key(x): x for x in rec['answer']}
        c.require(set(refreshed) == RECAPTURED and {c.key(x) for x in rec['source']} == RECAPTURED, 'Wrong recaptured five')
        c.require(rec['receipt']['registered_articles'] == 5 and {c.key(x) for x in rec['receipt']['checks']} == RECAPTURED, 'Wrong metadata re-emission receipt')
        c.require(rec['receipt']['first_drafts'] == 0 and rec['receipt']['revisions'] == 5, 'Recertification must be metadata-only revisions')
        # The parent approval explicitly binds the real capture proof, receipt and five identifiers.
        c.require(set(approval['approved_refreshed_identifiers']) == RECAPTURED, 'Wrong recapture approval identifiers')
        c.require(set(before) == RECAPTURED, 'Wrong captured owner set')
        optional_removed = {k: [] for k in RECAPTURED}
        for key in RECAPTURED:
            c.require({k:v for k,v in before[key].items() if k not in {'reference_checks','reference_coherence'}} == {k:v for k,v in refreshed[key].items() if k not in {'reference_checks','reference_coherence'}}, 'Re-emission changed a non-reference field')
        for key in set(refreshed) & set(row_by):
            frozen_row, actual_row = row_by[key], refreshed[key]
            mutable = {'reference_checks', 'reference_coherence'}
            c.require(all(before[key].get(k) == v for k,v in frozen_row.items() if k not in mutable), 'Canonical capture differs from frozen E')
            c.require(set(before[key]) - set(frozen_row) <= {'policy_review_id','prior_proposal_sha256'}, 'Unexpected captured provenance field')
            removed = {x['target_key'] for x in frozen_row.get('reference_checks', [])} - {x['target_key'] for x in actual_row.get('reference_checks', [])}
            c.require(removed <= {L76}, 'Unapproved optional target removed')
            if removed: optional_removed[key] = sorted(removed)
            c.require(any(edge['target_key'] == L76 for edge in maps[key]['legal_dependencies']), 'L243-7-6 legal dependency was lost')
            row_by[key] = actual_row
        c.require(approval['approved_optional_check_removals'] == ca['approved_optional_check_removals'] == optional_removed, 'Parent did not approve the exact optional removals')
        for check in rec['receipt']['checks']:
            c.require(check['source_and_notes_verified'] and check['prior_checked'] and check['proposed_sha256'] == c.digest(refreshed[c.key(check)].get('proposed_xml')), 'Wrong actual metadata receipt body')
        ledger = B / 'runtime/substantive-audits.json'
        old_raw = ledger.read_bytes()
        c.require(c.sha_bytes(old_raw) == BASE_LEDGER, 'Ledger changed; obtain a separately reviewed edition')
        old = json.loads(old_raw)
        old_by = {c.key(x): x for x in old['audits']}
        c.require(len(old_by) == len(old['audits']) == 453, 'Wrong prior453')
        c.require(set(row_by) & set(old_by) == SOCIAL, 'Unexpected E replacements')
        phase_c = read(P.parent / 'poursuite-20261020-c/audit-adoption.json')
        c141 = {x['key'] for x in phase_c['adopted']} - SOCIAL
        c.require(len(c141) == 141 and c141 <= set(old_by) and not(c141 & set(row_by)), 'Wrong C141')
        compatibility_path = P.parent / 'poursuite-20261020-d/social-context-review/edition001/compatibility-141.proposed.json'
        compatibility = read(compatibility_path, approval['C141_compatibility_sha256'])
        c.require(approval['C141_compatibility_sha256'] == '82af86ae63a699979c2da1c708e04f759319a5f80602b70c006f909fa0a5b7f1', 'Wrong bounded C141 proof')
        c.require(set(compatibility['audit_keys']) == c141, 'Compatibility selection changed')
        fiscal_bridge = read(P.parent / 'poursuite-20261020-d/fiscal-independent-review/c-context/edition001/approval.json', approval['D_fiscal_context_approval_sha256'])
        c.require(approval['D_fiscal_context_approval_sha256'] == '4184092713e68ceb4008c577a22ef561039f643e48cc1f02d096e618d52cacaf', 'Wrong D fiscal context approval')
        c.require(str(fiscal_bridge.get('status', '')).startswith('approved_bounded_independent_context_compatibility'), 'D bridge not approved')
        frozen(P.parent / 'poursuite-20261020-d/fiscal/edition002', 'fa70b5b8084dc352f29acfcc90504db69c4e297efe3cb6ef5484660540917b2f')
        frozen(P.parent / 'poursuite-20261020-d/social-context-review/edition001', 'd96cec5f43ceb7751ad7b742252cb8100d856f47a8d0ca0573c18ae7226ff2e6')
        dsource = read(P.parent / 'poursuite-20261020-d/fiscal/edition002/source.json')
        drows = read(P.parent / 'poursuite-20261020-d/fiscal/edition002/answer.json')
        c.require(c.file_sha(P.parent / 'poursuite-20261020-d/fiscal/edition002/manifest.json') == 'fa70b5b8084dc352f29acfcc90504db69c4e297efe3cb6ef5484660540917b2f', 'D frozen input changed')
        expected_allowed = {c.key(r): c.pin(s, r) for s, r in zip(dsource, drows) if c.key(r) in ALLOWED_TARGETS}
        job = read(P.parent / 'poursuite-20261020-d/social-context-review/edition001/job-current.json')
        for x in job:
            if c.key(x) in ALLOWED_TARGETS: expected_allowed[c.key(x)] = c.pin(x, x)
        expected_allowed.update({k: c.pin(source_by[k], row_by[k]) for k in set(row_by) & ALLOWED_TARGETS})
        c.require(set(expected_allowed) == ALLOWED_TARGETS, 'Missing exact allowed target')
        db = sqlite3.connect('file:' + str(B / 'corpus.sqlite') + '?mode=ro', uri=True)
        db.execute('BEGIN')
        try:
            materials = {}
            def material(key):
                if key not in materials:
                    s = c.verified_sources(db, key, source_notes, xml_contents)
                    r = c.source_only_or_draft(db, s)
                    if key in row_by or key in c141: r = c.current_row(db, s)
                    materials[key] = s, r
                return materials[key]
            def pin(key): return c.pin(*material(key))
            for key, approved in expected_allowed.items():
                c.require(c.dependency_matches(approved, pin(key)), 'Actual allowed context differs: ' + key)
            rc.check_guards(db, rec['snapshot'])
            for key, row in refreshed.items():
                s, actual = material(key)
                captured_source = next(x for x in rec['source'] if c.key(x) == key)
                c.require(all(captured_source[f] == s[f] for f in ('source_sha256','source_xml','source_notes_xml')), 'Actual recapture source/notes differ')
                c.require(row['proposed_xml'] == actual['proposed_xml'], 'Recaptured body differs')
                notes = db.execute('select reason,review_notes from drafts where code_id=?and source_id=?',key.split('|')).fetchone()
                c.require(notes == (row['reason'],row['review_notes']), 'Actual recapture notes differ')
                c.require(rc.certificate_current(db, s, row.get('proposed_xml'), row['reference_coherence']), 'Stale actual recaptured reference certificate')
                if key not in row_by:
                    c.require(row['substantive_impact'] == old_by[key]['assessment'] and row['substantive_impact_certificate'] == old_by[key]['certificate'], 'C referrer impact/certificate changed')
            # Check the five actual canonical owners after metadata inscription. Only separately approved workflow provenance may differ from staging.
            owned = {}
            for path in sorted((B/'batches').glob('*/*.json')):
                if not re.fullmatch(r'(?:batch)?\d+\.json', path.name): continue
                batch_raw = path.read_bytes()
                batch = json.loads(batch_raw)
                for row in batch:
                    if c.key(row) in RECAPTURED:
                        tracked[path] = c.sha_bytes(batch_raw)
                        c.require(c.key(row) not in owned, 'Duplicate recaptured owner')
                        owned[c.key(row)] = row
            c.require(set(owned) == RECAPTURED, 'Missing real recaptured owner')
            prov = {'policy_review_id','prior_proposal_sha256'}
            provenance = {}
            for key,row in owned.items():
                c.require({k:v for k,v in row.items() if k not in prov} == {k:v for k,v in refreshed[key].items() if k not in prov}, 'Canonical metadata does not equal real re-emission')
                provenance[key] = {k:row[k] for k in prov if k in row}
            c.require(approval['approved_post_registration_provenance'] == provenance, 'Workflow provenance not explicitly approved')
            now = datetime.now(timezone.utc).isoformat()
            updates, changes = {}, []
            for key in sorted(c141):
                audit = old_by[key]
                actual = {c.key(g): pin(c.key(g)) for g in audit['dependency_guards']}
                updated, delta = refresh_context_guards(audit, actual, expected_allowed)
                s, r = material(key)
                c.require(not c.prior_reasons(updated, s, r, actual), 'Stale own/unrelated C audit: ' + key)
                c.require(updated['certificate'] == audit['certificate'], 'C own certificate changed')
                updates[key] = updated
                if delta: changes.append(dict(key=key,changes=delta,old_audit_sha256=c.canonical_digest(audit),new_audit_sha256=c.canonical_digest(updated)))
            for key, row in row_by.items():
                s, r = material(key)
                expected = source_by[key]
                c.require(all(s[f] == expected[f] for f in ('source_sha256','source_xml','source_notes_xml')), 'Changed E source')
                actual = c.current_row(db, s)
                c.require(all(actual[f] == row[f] for f in ('source_sha256','status','proposed_xml')), 'Changed E disposition')
                notes = db.execute('select reason,review_notes from drafts where code_id=?and source_id=?',key.split('|')).fetchone()
                c.require(notes == (row['reason'],row['review_notes']), 'Changed E notes')
                validate(copy.deepcopy(row), s, required=True, enforce_workflow=False)
                if row.get('reference_coherence'):
                    c.require(rc.certificate_current(db,s,row.get('proposed_xml'),row['reference_coherence']), 'E reference certificate not current: '+key)
                deps=[]
                for edge in maps[key]['legal_dependencies']:
                    expected = edge['future_guard_not_actual_DB'] if edge['internal_E'] else edge['actual_before_guard']
                    current = pin(edge['target_key'])
                    c.require(c.dependency_matches(expected,current), 'Changed specifically mapped dependency')
                    deps.append(current)
                c.require(len({c.key(g)for g in deps})==len(deps),'Duplicate per-article dependency')
                updates[key]=dict(code_id=row['code_id'],source_id=row['source_id'],assessment=copy.deepcopy(row['substantive_impact']),certificate=certificate(row,s,POLICY['policy-coordinations.json']),source_body_sha256=c.digest(s['source_xml']),reviewed_by='Contrelecture IA indépendante E : root fiscal/logement, agent fiscalité social ; corpus141 non relu',approved_at=now,evidence_file=str((pack/'preflight.json').relative_to(B)),evidence_sha256=c.file_sha(pack/'preflight.json'),parent_review_file=str(approval_path.relative_to(B)),parent_review_sha256=c.file_sha(approval_path),dependency_guards=deps,documentary_dependencies=maps[key]['documentary_dependencies'],semantic_review_by_jurist=False)
            exported={(s['code_id'],s['source_id']):dict(s,**r)for s,r in materials.values()}
            for key,audit in updates.items():
                s,r=material(key)
                c.require(_checked(audit,dict(s,**r),POLICY['policy-coordinations.json'],approved=True,exported=exported)==audit['assessment'],'Invalid final impact certificate: '+key)
            new=copy.deepcopy(old)
            new['audits']=[updates.get(c.key(x),x)for x in old['audits']]+[updates[k]for k in row_by if k not in old_by]
            c.require(len(new['audits'])==502,'Wrong resulting502')
            preserved=set(old_by)-c141-SOCIAL
            c.require(all(next(x for x in new['audits']if c.key(x)==k)==old_by[k]for k in preserved),'Unrelated old audit modified')
            c.require(len(preserved)==309,'Wrong untouched309')
            new['approved_at']=now
            for path,sha in tracked.items(): c.require(c.file_sha(path)==sha,'Evidence changed before write')
            c.require(ledger.read_bytes()==old_raw and rc.policy_state()==POLICY,'Concurrent active change')
            c.archived_write(P/'audit-ledger-history'/(BASE_LEDGER+'.json'),old_raw)
            for key in SOCIAL:c.archived_write(P/'audit-ledger-history'/('replaced-'+key.replace('|','-')+'.json'),c.encoded(old_by[key]))
            raw=c.encoded(new)
            receipt=dict(adopted_at=now,previous_ledger_sha256=BASE_LEDGER,resulting_ledger_sha256=c.sha_bytes(raw),new_E_independent_readings=52,new_audits=49,replaced_old_C_social=3,context_only_C_updates=changes,context_scope=141,unchanged_other_audits=309,stored_audits=502,parent_approval_sha256=c.file_sha(approval_path),recapture_proof_sha256=rec['proof_sha256'],recapture_receipt_sha256=rec['receipt_sha256'],registration_sha256=approval['registration_sha256'],policy_sha256=POLICY,no_new_C141_semantic_reading=True,no_CLI46_audits_adopted=True,national_savings=None,global_net_complexity_reduction='not_established',semantic_review_by_jurist=False,exhaustive_rewriting_complete=False)
            c.atomic_bytes(ledger,raw)
            c.atomic_bytes(P/'audit-adoption.json',c.encoded(receipt))
            print(json.dumps(receipt,ensure_ascii=False,indent=2))
        finally:
            db.close()


if __name__ == '__main__':
    main()
