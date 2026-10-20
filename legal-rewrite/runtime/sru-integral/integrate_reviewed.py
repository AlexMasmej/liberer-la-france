"""Register reviewed whole-article SRU lots with canonical and prior-draft guards."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

LEGAL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LEGAL))
from ingest import open_db, source_notes
from run_exhaustive import validate_answer
from register_batches import register
import review_prior

parser = argparse.ArgumentParser()
parser.add_argument('--pack', action='append', required=True)
parser.add_argument('--batch', required=True, type=int)
parser.add_argument('--commit', action='store_true')
args = parser.parse_args()
rows, sources, seen = [], {}, set()
db = open_db(LEGAL/'corpus.sqlite')
try:
    for folder in map(Path, args.pack):
        answers = folder/('candidates.json' if (folder/'candidates.json').exists() else 'answer.json')
        proposed = json.loads(answers.read_text())
        source_path = folder/('source.json' if (folder/'source.json').exists() else 'sources.json')
        expected = json.loads(source_path.read_text())
        by_key = {(a['code_id'], a['source_id']): a for a in expected}
        # A reference bundle can also retain adjacent articles or a documented
        # source gap. Only explicitly proposed, complete articles are registered.
        validate_answer(proposed, [by_key[(r['code_id'], r['source_id'])] for r in proposed])
        for row in proposed:
            key = row['code_id'], row['source_id']
            assert key not in seen, ('Duplicate article', key)
            seen.add(key)
            source = by_key[key]
            assert db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key).fetchone() == (row['number'], row['source_sha256'], source['source_xml'])
            canonical_notes = source_notes(db, *key)
            assert canonical_notes.strip() == source['source_notes_xml'].strip()
            source['source_notes_xml'] = canonical_notes
            prior = source.get('previous_draft')
            if prior:
                digest = hashlib.sha256(prior['proposed_xml'].encode()).hexdigest()
                if prior.get('proposed_sha256'):
                    assert prior['proposed_sha256'] == digest
                prior['proposed_sha256'] = digest
            sources[key] = source
            rows.append(row)
    revisions, fresh, registered = [], [], []
    for row in rows:
        key = row['code_id'], row['source_id']
        current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        if current == (row['source_sha256'], row['proposed_xml']):
            registered.append(row)
            continue
        prior = sources[key].get('previous_draft')
        if prior:
            assert current == (prior['source_sha256'], prior['proposed_xml']), ('Prior proposal changed', key)
            revisions.append(row)
        else:
            assert current is None, ('Independent proposal exists', key)
            fresh.append(row)
finally:
    db.close()

report_folder = LEGAL/'runtime/sru-integral'/f'registration-{args.batch:03d}'
report_folder.mkdir(exist_ok=True)
plan = {'articles': len(rows), 'revisions': len(revisions), 'first_drafts': len(fresh),
        'already_registered': len(registered), 'source_and_notes_verified': True,
        'prior_proposals_verified': True, 'committed': False,
        'whole_sru_repeal_complete': False, 'numbers': [r['number'] for r in rows]}
(report_folder/'sources.json').write_text(json.dumps(list(sources.values()), ensure_ascii=False, indent=2))
(report_folder/'candidates.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
if args.commit:
    if revisions:
        review_prior.commit(revisions, [sources[(r['code_id'], r['source_id'])] for r in revisions])
    if fresh:
        path = LEGAL/'batches/sru-integral'/f'{args.batch:03d}.json'
        assert not path.exists(), 'Refusing to replace another registered batch'
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(fresh, ensure_ascii=False, indent=2))
        db = open_db(LEGAL/'corpus.sqlite')
        try:
            register(db, LEGAL/'batches', True)
        finally:
            db.close()
    db = open_db(LEGAL/'corpus.sqlite')
    try:
        for row in rows:
            assert db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?', (row['code_id'], row['source_id'])).fetchone() == (row['proposed_xml'],)
    finally:
        db.close()
    plan['committed'] = True
(report_folder/'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2))
print(json.dumps(plan, ensure_ascii=False, indent=2))
