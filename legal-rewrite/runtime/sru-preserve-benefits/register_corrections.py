"""Apply reviewed benefit restorations with exact source and draft guards."""
from pathlib import Path
import json
import sys

LEGAL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LEGAL))
from ingest import open_db, source_notes
from run_exhaustive import validate_answer
from review_prior import commit, digest

ROOT = Path(__file__).resolve().parent
rows, expected, checks = [], [], []
db = open_db(LEGAL / 'corpus.sqlite')
try:
    for name in sys.argv[1:]:
        folder = ROOT / name
        answers = json.loads((folder / 'answer.json').read_text())
        priors = json.loads((folder / 'expected.json').read_text())
        sources = {(a['code_id'], a['source_id']): a
                   for a in json.loads((folder / 'source.json').read_text())}
        guards = {(a['code_id'], a['source_id']): a for a in priors}
        complete = [sources[(a['code_id'], a['source_id'])] for a in answers]
        validate_answer(answers, complete)
        for row in answers:
            key = row['code_id'], row['source_id']
            source, guard = sources[key], guards[key]
            canonical = db.execute(
                'SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key
            ).fetchone()
            assert canonical == (row['number'], row['source_sha256'], source['source_xml']), key
            assert source_notes(db, *key).strip() == source['source_notes_xml'].strip(), key
            prior = source.get('previous_draft', {}) | guard['previous_draft']
            assert digest(prior['proposed_xml']) == prior['proposed_sha256'], key
            current = db.execute(
                'SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key
            ).fetchone()
            assert current == tuple(prior[f] for f in (
                'source_sha256', 'status', 'proposed_xml', 'reason', 'review_notes')), key
            rows.append(row)
            expected.append(source | {'previous_draft': prior})
            checks.append({'code_id': key[0], 'source_id': key[1], 'number': row['number'],
                           'source_and_notes_verified': True,
                           'previous_proposal_sha256': prior['proposed_sha256'],
                           'replacement_sha256': digest(row['proposed_xml'])})
finally:
    db.close()
assert len({(r['code_id'], r['source_id']) for r in rows}) == len(rows)
commit(rows, expected)
db = open_db(LEGAL / 'corpus.sqlite')
try:
    for row in rows:
        assert db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',
                          (row['code_id'], row['source_id'])).fetchone() == (row['proposed_xml'],)
finally:
    db.close()
report = {'registered_corrections': len(rows), 'checks': checks,
          'counts_as_first_drafts': False, 'exhaustive_rewriting_complete': False}
path = ROOT / ('registration-' + '-'.join(sys.argv[1:]) + '.json')
path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
