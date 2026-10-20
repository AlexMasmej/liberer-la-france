"""Check and register the coordinated SRU proposals, retaining before-images."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
LEGAL = HERE.parents[1]
sys.path.insert(0, str(LEGAL))
from ingest import open_db, source_notes
from run_exhaustive import validate_answer
from register_batches import register
import review_prior

parser = argparse.ArgumentParser()
parser.add_argument('--commit', action='store_true')
args = parser.parse_args()

packs = [
    (HERE / 'core-candidates.json', [HERE / 'core-source.json']),
    (LEGAL / 'runtime/sru-reglementaire/articles.candidates.json', [LEGAL / 'runtime/sru-reglementaire/sources.json', LEGAL / 'runtime/sru-reglementaire/r445-24.source.json']),
    (LEGAL / 'runtime/sru-cch-coordinations/candidates.json', [LEGAL / 'runtime/sru-cch-coordinations/source.json']),
    (LEGAL / 'runtime/sru-urbanisme-fiscalite/candidates.json', [LEGAL / 'runtime/sru-urbanisme-fiscalite/sources.json']),
]
rows = []
expected = {}
seen = set()
db = open_db(LEGAL / 'corpus.sqlite')
for candidate_path, source_paths in packs:
    candidates = json.loads(candidate_path.read_text())
    sources = []
    for path in source_paths:
        value = json.loads(path.read_text())
        sources.extend(value if isinstance(value, list) else [value])
    by_key = {(s['code_id'], s['source_id']): s for s in sources}
    selected = []
    for row in candidates:
        key = row['code_id'], row['source_id']
        assert key not in seen, ('Duplicate proposal', key)
        seen.add(key)
        source = dict(by_key[key])
        source['source_xml'] = source.get('source_xml', source.get('content_xml'))
        canonical = db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key).fetchone()
        assert canonical == (row['number'], row['source_sha256'], source['source_xml']), ('Canonical source changed', key)
        assert source_notes(db, *key) == source['source_notes_xml'], ('Application notes changed', key)
        prior = source.get('previous_draft')
        if prior:
            assert prior['proposed_sha256'] == hashlib.sha256((prior['proposed_xml'] or '').encode()).hexdigest()
        selected.append(source)
        expected[key] = source
    validate_answer(candidates, selected)
    rows.extend(candidates)

revisions = []
fresh = []
already_registered = []
for row in rows:
    key = row['code_id'], row['source_id']
    source = expected[key]
    current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    if current == (row['source_sha256'], row['proposed_xml']):
        already_registered.append(row)
        continue
    prior = source.get('previous_draft')
    if prior:
        assert current == (prior['source_sha256'], prior['proposed_xml']), ('Previous proposal changed', key)
        revisions.append(row)
    else:
        assert current is None, ('Independent proposal would be overwritten', key)
        fresh.append(row)
db.close()

plan = {
    'articles': len(rows), 'revisions': len(revisions), 'first_drafts': len(fresh),
    'already_registered': len(already_registered), 'canonical_sources_and_application_notes_match': True,
    'prior_proposals_match_guarded_before_images': True,
    'change_types': {kind: sum(a.get('change_type', 'coordination') == kind for a in rows)
                     for kind in sorted({a.get('change_type', 'coordination') for a in rows})},
    'committed': False,
}
(HERE / 'all-candidates.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
(HERE / 'all-sources.json').write_text(json.dumps(list(expected.values()), ensure_ascii=False, indent=2))
(HERE / 'integration-plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2))
if args.commit:
    if revisions:
        review_prior.commit(revisions, [expected[(r['code_id'], r['source_id'])] for r in revisions])
    if fresh:
        dest = LEGAL / 'batches/sru-coordinations/001.json'
        assert not dest.exists(), 'Do not replace an independently registered SRU batch'
        dest.parent.mkdir(parents=True, exist_ok=True)
        temp = dest.with_suffix('.json.tmp')
        temp.write_text(json.dumps(fresh, ensure_ascii=False, indent=2))
        temp.replace(dest)
        db = open_db(LEGAL / 'corpus.sqlite')
        try:
            register(db, LEGAL / 'batches', True)
        finally:
            db.close()
    db = open_db(LEGAL / 'corpus.sqlite')
    try:
        for row in rows:
            current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', (row['code_id'], row['source_id'])).fetchone()
            assert current == (row['source_sha256'], row['proposed_xml'])
    finally:
        db.close()
    plan['committed'] = True
    (HERE / 'integration-plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2))
print(json.dumps(plan, ensure_ascii=False, indent=2))
