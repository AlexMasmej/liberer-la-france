"""Validate only the frozen audit, then write evidence in this new folder.

No source database connection, active pipeline import, or corpus mutation.
The latest pointer is updated separately, only after this script succeeds.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parent.parent
sys.path.insert(0, str(PROJECT))
import global_reference_audit as audit

GUARDS = ('source_sha256', 'source_body_sha256', 'source_notes_sha256',
          'article_document_sha256', 'article_document_stored_sha256',
          'proposal_sha256', 'draft_source_sha256', 'draft_status')


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value or b'').hexdigest()


def file_sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(name):
    return json.loads((OUT / name).read_text())


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


errors = []


def check(condition, description):
    if not condition:
        errors.append(description)


summary, capture, fingerprints = read('summary.json'), read('capture.json'), read('fingerprints.json')
run_id, as_of = summary['audit_id'], summary['as_of']
check(as_of == '2026-10-18', 'as_of changed')
check(capture['quick_check'] == 'ok', 'snapshot quick_check not successful')
snapshot_hash = file_sha(OUT / 'corpus.snapshot.sqlite')
check(snapshot_hash == capture['snapshot_sha256'] == fingerprints['snapshot_sha256'], 'snapshot bytes differ from capture')
check(file_sha(PROJECT / 'global_reference_audit.py') == capture['auditor_sha256'] == fingerprints['auditor_sha256'], 'auditor changed after capture')
check(capture['pages_per_step'] == 256 and capture['max_read_bytes_per_step'] <= 1048576, 'unexpected backup read-lock step bound')
check(capture['source_connection'].startswith('mode=ro; query_only=ON'), 'backup source was not declared read-only')
for name, policy in capture['policies'].items():
    check(file_sha(OUT / name) == policy['sha256'], 'frozen policy hash: ' + name)
    check(policy['stable_during_capture'], 'policy unstable during capture: ' + name)
check(summary['snapshot_and_policy_fingerprints'] == fingerprints, 'summary fingerprint differs')
without_id = {k: v for k, v in fingerprints.items() if k != 'audit_id'}
check(sha(json.dumps(without_id, ensure_ascii=False, sort_keys=True)) == run_id == fingerprints['audit_id'], 'audit id not derived from fingerprints')
check(summary['automatic_change'] is False and summary['semantic_review_by_jurist'] is False, 'audit claims mutation or legal approval')

db = sqlite3.connect((OUT / 'corpus.snapshot.sqlite').as_uri() + '?mode=ro', uri=True)
db.execute('PRAGMA query_only=ON')
db.row_factory = sqlite3.Row
config = read('corpus.json')
codes = config['codes'] + config.get('annexes', [])
selected = set()
inventory_counts = {}
for code in codes:
    ids, missing_sections, missing_articles = audit.inventory(db, code['id'], as_of)
    check(not missing_sections and not missing_articles, 'incomplete canonical inventory: ' + code['id'])
    selected.update(code['id'] + '|' + identifier for identifier in ids)
    inventory_counts[code['id']] = len(ids)
check(len(codes) == 9 and len(selected) == summary['entries_scanned'] == 30317, 'nine-code inventory coverage/count')
check(not summary['missing_inventory_articles'] and not summary['inventory_date_mismatches'], 'inventory missing/date exceptions')

metadata, metadata_hash = {}, hashlib.sha256()
for row in db.execute('SELECT code_id,id,number,valid_from,valid_until,state,source_sha256,archive FROM articles ORDER BY code_id,id'):
    metadata[row['code_id'] + '|' + row['id']] = dict(row)
    metadata_hash.update(json.dumps(dict(row), sort_keys=True, ensure_ascii=False).encode() + b'\n')
check(len(metadata) == summary['all_historical_article_versions_indexed'], 'historical version count')
check(metadata_hash.hexdigest() == fingerprints['all_article_metadata_sha256'], 'all article metadata fingerprint')
for table, query, field in [
    ('documents', 'SELECT code_id,id,kind,sha256,archive FROM documents ORDER BY code_id,id,kind', 'all_document_metadata_sha256'),
    ('archives', 'SELECT * FROM archives ORDER BY name', 'archives_sha256'),
    ('drafts', 'SELECT * FROM drafts ORDER BY code_id,source_id', 'all_drafts_sha256'),
]:
    h = hashlib.sha256()
    for row in db.execute(query):
        h.update(json.dumps(list(row), ensure_ascii=False).encode() + b'\n')
    check(h.hexdigest() == fingerprints[field], table + ' logical fingerprint')

manifest, guards = {}, {}
for line in (OUT / 'article-manifest.jsonl').open():
    row = json.loads(line)
    check(row['key'] not in manifest, 'duplicate manifest key: ' + row['key'])
    manifest[row['key']] = row
    guards[row['key']] = {field: row[field] for field in GUARDS}
check(set(manifest) == selected, 'manifest keys differ from canonical inventory')

body_count, proposal_count, retained_count, unchanged_count = 0, 0, 0, 0
document_count, note_count, checked_current = 0, 0, 0
query = '''SELECT a.code_id,a.id,a.content_xml,a.source_sha256,
    doc.xml AS document_xml,doc.sha256 AS document_stored_sha256,
    d.source_sha256 AS draft_source_sha256,d.status AS draft_status,d.proposed_xml
    FROM articles a LEFT JOIN documents doc ON doc.code_id=a.code_id AND doc.id=a.id AND doc.kind='ARTICLE'
    LEFT JOIN drafts d ON d.code_id=a.code_id AND d.source_id=a.id
    WHERE a.valid_from<=? AND a.valid_until>? ORDER BY a.code_id,a.id'''
for row in db.execute(query, (as_of, as_of)):
    key = row['code_id'] + '|' + row['id']
    if key not in selected:
        continue
    notes = ''
    raw = row['document_xml']
    check(raw is not None, 'missing canonical document: ' + key)
    if raw is not None:
        root = ET.fromstring(raw)
        node = root.find('NOTA/CONTENU')
        if node is not None:
            notes = ((node.text or '') + ''.join(ET.tostring(child, encoding='unicode') for child in node)).strip()
        body = root.find('BLOC_TEXTUEL/CONTENU')
        mirror = ((body.text or '') + ''.join(ET.tostring(child, encoding='unicode') for child in body)) if body is not None else ''
        check(mirror == row['content_xml'], 'canonical body differs: ' + key)
        document_count += 1
        note_count += bool(audit.plain(notes).strip())
    current = {
        'source_sha256': row['source_sha256'], 'source_body_sha256': sha(row['content_xml']),
        'source_notes_sha256': sha(notes), 'article_document_sha256': sha(raw),
        'article_document_stored_sha256': row['document_stored_sha256'],
        'proposal_sha256': sha(row['proposed_xml']) if row['proposed_xml'] is not None else None,
        'draft_source_sha256': row['draft_source_sha256'], 'draft_status': row['draft_status'],
    }
    check(current == guards[key], 'manifest guard differs from frozen source/proposal: ' + key)
    check(current['article_document_sha256'] == current['article_document_stored_sha256'], 'stored canonical document hash: ' + key)
    check(not current['draft_source_sha256'] or current['draft_source_sha256'] == current['source_sha256'], 'stale proposal source: ' + key)
    checked_current += 1
    proposal_count += row['proposed_xml'] is not None
    retained_count += row['draft_status'] == 'retained_unchanged' and row['proposed_xml'] is None
    unchanged_count += row['proposed_xml'] == row['content_xml']
    body_count += 1
check(checked_current == len(selected), 'current manifest guard coverage')
check(summary['fields_scanned']['source_body'] == body_count and summary['fields_scanned']['source_notes'] == body_count, 'body/notes coverage count')
check(summary['fields_scanned']['proposal'] == proposal_count, 'proposal coverage count')
check(summary['fields_scanned']['canonical_article_document'] == document_count, 'canonical document coverage count')
check(summary['canonical_document_checks']['nonempty_official_application_notes'] == note_count, 'nonempty note count')

counts = Counter(manifest_entries=len(manifest), current_article_guards_checked=checked_current)


def validate_target(target, guard, where):
    check(target in metadata, 'target absent from snapshot: ' + where)
    category = 'finding' if where.startswith('finding ') else 'edge'
    if target in guards:
        check(guard == guards[target], 'current target guard mismatch: ' + where)
        counts['current_target_' + category + '_guards_checked'] += 1
    elif target in metadata:
        check(guard == {'source_sha256': metadata[target]['source_sha256'], 'historical_source_only': True}, 'historical target guard mismatch: ' + where)
        counts['historical_target_' + category + '_guards_checked'] += 1


edge_fields, edge_resolution_counts = Counter(), Counter()
edge_fields_by_code, findings_by_code = Counter(), Counter()
for line in (OUT / 'edges.jsonl').open():
    edge = json.loads(line)
    key, field = edge['source_key'], edge['field']
    check(edge['audit_id'] == run_id, 'edge audit id')
    check(edge['source_guard'] == guards.get(key), 'edge source guard: ' + key)
    resolution = edge['resolution']
    if resolution.get('target_key'):
        validate_target(resolution['target_key'], edge.get('target_guard'), 'edge ' + key)
    if resolution.get('current_number_candidate_key'):
        candidate = resolution['current_number_candidate_key']
        check(candidate in guards and edge.get('current_number_candidate_guard') == guards[candidate], 'historical-context candidate guard: ' + key)
        counts['historical_context_candidate_guards_checked'] += 1
    edge_fields[field] += 1
    edge_fields_by_code[(key.split('|', 1)[0], field)] += 1
    if field not in {'canonical_other_link', 'canonical_version_lineage'}:
        edge_resolution_counts[resolution['status']] += 1
    counts['edges'] += 1
check(dict(edge_fields) == summary['edge_counts'], 'edge field totals')
check(dict(edge_resolution_counts) == summary['resolution_counts'], 'resolution totals')

finding_hashes, finding_ids, kinds, priorities, finding_sources, p1_sources = {}, [], Counter(), Counter(), set(), set()
for line in (OUT / 'findings.jsonl').open():
    item = json.loads(line)
    fid, key = item['finding_id'], item['source_key']
    check(item['audit_id'] == run_id and item['source_guard'] == guards.get(key), 'finding audit/source guard: ' + key)
    expected = sha(run_id + '|' + key + '|' + item['kind'] + '|' + json.dumps(item['evidence'], sort_keys=True, ensure_ascii=False))
    check(fid == expected and fid not in finding_hashes, 'finding id duplicate or invalid: ' + fid)
    if item.get('target_key'):
        # Target validation is also required on findings, independently of edges.
        validate_target(item['target_key'], item.get('target_guard'), 'finding ' + fid)
        counts['finding_target_guards_checked'] += 1
    check(item['automatic_change'] is False and item['semantic_review_by_jurist'] is False, 'finding legal/mutation flags')
    finding_hashes[fid] = sha(json.dumps(item, sort_keys=True, ensure_ascii=False))
    finding_ids.append(fid)
    kinds[item['kind']] += 1
    priorities[str(item['priority'])] += 1
    finding_sources.add(key)
    if item['priority'] == 1:
        p1_sources.add(key)
    findings_by_code[(item['code_id'], str(item['priority']))] += 1
    counts['findings'] += 1
check(counts['findings'] == summary['findings_count'], 'finding count')
check(dict(kinds) == summary['findings_by_kind'] and dict(priorities) == summary['findings_by_priority'], 'finding type/priority totals')
check(len(finding_sources) == summary['distinct_articles_with_findings'], 'distinct referrers')
check(len(p1_sources) == summary['distinct_articles_with_priority_1_findings'], 'distinct P1 referrers')

queue = read('queue.json')
check(queue['audit_id'] == run_id and queue['items_count'] == counts['findings'], 'queue metadata/count')
queue_ids, ordering = [], []
for item in queue['items']:
    fid = item['finding_id']
    queue_ids.append(fid)
    check(sha(json.dumps(item, sort_keys=True, ensure_ascii=False)) == finding_hashes.get(fid), 'queue content differs from finding: ' + fid)
    ordering.append((item['priority'], item['code_id'], item['source_key'], item['kind'], fid))
check(len(queue_ids) == len(set(queue_ids)) and set(queue_ids) == set(finding_ids), 'queue ids differ from findings')
check(ordering == sorted(ordering), 'queue priority ordering')
counts['queue_items'] = len(queue_ids)
del queue

for code in codes:
    report = read('codes/' + code['slug'] + '.json')
    check(report['audit_id'] == run_id and report['inventory_entries'] == inventory_counts[code['id']] == report['scanned_entries'], 'per-code inventory: ' + code['slug'])
    check(report['edges_by_field'] == {field: count for (cid, field), count in edge_fields_by_code.items() if cid == code['id']}, 'per-code edges: ' + code['slug'])
    expected_priority = {priority: count for (cid, priority), count in findings_by_code.items() if cid == code['id']}
    check(report['findings_by_priority'] == expected_priority and report['queue_items'] == sum(expected_priority.values()), 'per-code queue: ' + code['slug'])

clusters = read('coordination-clusters.json')
check(clusters['audit_id'] == run_id and len(clusters['targets']) == summary['proposed_repeal_targets_with_detected_referrers'], 'coordination clusters count')
for cluster in clusters['targets']:
    check(cluster['target_guard'] == guards.get(cluster['target_key']), 'cluster target guard')
    check(cluster['distinct_referrers'] == len(set(cluster['source_keys'])), 'cluster source count')
    check(cluster['occurrences'] == len(cluster['finding_ids']) and all(fid in finding_hashes for fid in cluster['finding_ids']), 'cluster finding ids')
cycles = read('cycles.json')
for name in ['official_source_citations', 'proposed_view_textual_citations']:
    item = cycles[name]
    check(item['status'] == 'informational_only_not_an_incoherence', 'cycles falsely classified')
    check(item['components'] == len(item['members']) and item['vertices_in_cycles'] == sum(map(len, item['members'])), 'cycle counts')
    check(all(key in metadata for component in item['members'] for key in component), 'cycle member missing')

# Preserve reviews, and explicitly check whether their exact dependency guards
# still match this new snapshot. A structural refresh never resolves a finding.
previous = read('previous-latest.json')
prior = Path(previous['folder'])
old_manifest = {row['key']: {field: row[field] for field in GUARDS}
                for row in map(json.loads, (prior / 'article-manifest.jsonl').open())}
reviews = []
for label, folder, packet_name, deps_name, final_name, report_name in [
    ('L1242-2', prior, 'L1242-2-review-packet.json', 'L1242-2-review-dependencies.json', 'L1242-2-final-state-check.json', 'L1242-2-REVIEW.md'),
    ('CVAE', prior / 'fiscal-CVAE-semantic-review-20261022', 'review-packet.json', 'review-dependencies.json', 'final-state-check.json', 'REPORT.md'),
]:
    packet = json.loads((folder / packet_name).read_text())
    deps = json.loads((folder / deps_name).read_text())
    final = json.loads((folder / final_name).read_text())
    findings = json.loads((folder / 'findings-reviewed.json').read_text())
    keys = sorted({a['key'] for a in packet['articles'] + deps['articles']})
    article_checks = []
    for key in keys:
        expected = old_manifest.get(key)
        # Fiscal review packet explicitly freezes all its source/proposal guards.
        current_guard = final.get('articles', {}).get(key, {})
        if isinstance(current_guard, dict):
            expected = current_guard.get('current_guard', expected)
        article_checks.append({'key': key, 'matches_prior_guard': guards.get(key) == expected,
                               'prior_guard': expected, 'new_snapshot_guard': guards.get(key)})
    policy_checks = {name: {'prior_sha256': item['current_sha256'],
                            'new_snapshot_sha256': capture['policies'][name]['sha256'],
                            'matches': item['current_sha256'] == capture['policies'][name]['sha256']}
                     for name, item in final['policies'].items()}
    reviews.append({'label': label, 'review_id': findings['review_id'], 'folder': str(folder),
                    'report': str(folder / report_name),
                    'findings_reviewed': findings['findings_reviewed'],
                    'articles_checked': len(keys), 'article_guards': article_checks,
                    'all_article_guards_match_new_snapshot': all(x['matches_prior_guard'] for x in article_checks),
                    'policies': policy_checks, 'all_policy_guards_match_new_snapshot': all(x['matches'] for x in policy_checks.values()),
                    'limits': findings.get('limits_and_unknowns', findings.get('limits')),
                    'still_in_analysis': findings.get('still_in_analysis', []),
                    'effective_inconsistencies_established': findings.get('effective_inconsistencies_established', 0),
                    'resolved_findings': findings['resolved_findings'],
                    'semantic_review_by_jurist': False, 'automatic_change': False})
db.close()
write('semantic-review-inheritance.json', {'audit_id': run_id,
      'status': 'Prior limited classifications retained with their own limits; no new legal approval or automatic resolution.',
      'reviews': reviews})

tests_tail = (OUT / 'tests.log').read_text().splitlines()[-5:]
check(tests_tail[-1] == 'OK' and any('Ran 30 tests' in x for x in tests_tail), 'parser tests not successful')
result = {'audit_id': run_id, 'validated_at_utc': datetime.now(timezone.utc).isoformat(),
          'checks_passed': not errors, 'errors': errors, 'counts': dict(counts),
          'all_current_source_article_document_hashes_match': not errors,
          'source_and_target_current_guards_match_manifest': not errors,
          'queue_ids_match_findings': set(queue_ids) == set(finding_ids),
          'queue_sorted_by_priority': ordering == sorted(ordering),
          'snapshot_byte_hash_matches_capture': snapshot_hash == capture['snapshot_sha256'],
          'all_edge_target_and_candidate_guards_verified': not errors,
          'full_inventory_and_logical_fingerprints_recomputed': not errors,
          'frozen_snapshot_counts': {'proposals_in_canonical_inventory': proposal_count,
                                    'retained_unchanged_in_canonical_inventory': retained_count,
                                    'proposals_identical_to_source_body': unchanged_count},
          'refresh_counter_basis': read('pre-capture-progress.json'),
          'semantic_reviews_preserved': [{k: v for k, v in r.items() if k not in {'article_guards', 'policies', 'limits', 'still_in_analysis'}} for r in reviews],
          'tests_log_tail': tests_tail,
          'read_only_snapshot_connection': True, 'live_database_scan_performed': False,
          'automatic_change': False}
write('validation.json', result)
print(json.dumps({'stage': 'validation_complete', 'checks_passed': not errors, 'errors_count': len(errors), 'counts': dict(counts), 'frozen_snapshot_counts': result['frozen_snapshot_counts']}, ensure_ascii=False), flush=True)
if errors:
    print(json.dumps(errors[:30], ensure_ascii=False), flush=True)
    raise SystemExit(1)
