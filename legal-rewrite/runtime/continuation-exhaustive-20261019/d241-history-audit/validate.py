"""Read-only pack/source/target checks; never registers or publishes anything."""
from pathlib import Path
import hashlib
import json
import re
import sqlite3
import sys

PACK = Path(__file__).resolve().parent
LEGAL = PACK.parents[2]
sys.path.insert(0, str(LEGAL))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as audit


def check():
    sources = json.loads((PACK / 'source.json').read_text())
    answers = json.loads((PACK / 'answer.json').read_text())
    targets = json.loads((PACK / 'target-source.json').read_text())
    validate_answer(answers, sources)
    assert len(sources) == len(answers) == 1
    assert answers[0]['number'] == 'D241-10'
    before = sources[0]['previous_draft']['proposed_xml']
    after = answers[0]['proposed_xml']
    old = re.findall(r'<p>.*?</p>', before, re.S)
    new = re.findall(r'<p>.*?</p>', after, re.S)
    assert len(old) == len(new) == 11
    assert [i for i, pair in enumerate(zip(old, new)) if pair[0] != pair[1]] == [3]
    assert old[1] == new[1]
    assert re.findall(r'\d+(?:[,.]\d+)?', before) == re.findall(r'\d+(?:[,.]\d+)?', after)
    with sqlite3.connect('file:' + str(LEGAL / 'corpus.sqlite') + '?mode=ro', uri=True) as db:
        db.execute('BEGIN')
        for source in sources + targets:
            key = source['code_id'], source['source_id']
            assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key).fetchone() == (source['source_sha256'], source['source_xml'])
            assert source_notes(db, *key) == source['source_notes_xml']
            current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
            prior = source['previous_draft']
            assert current == (prior['source_sha256'], prior['proposed_xml'])
            assert audit.digest(prior['proposed_xml']) == prior['proposed_sha256']
        audit.check_guards(db, json.loads((PACK / 'reference-targets.json').read_text()))
        db.rollback()
    for item in json.loads((PACK / 'historical-source-manifest.json').read_text()):
        assert hashlib.sha256((PACK / item['path']).read_bytes()).hexdigest() == item['sha256']
    return {'structure': 'passed', 'source_notes_beforeimages_and_target_guards': 'current',
            'changed_paragraphs': 1, 'formula_and_numeric_tokens': 'identical',
            'database_modified': False, 'registration': False}


if __name__ == '__main__':
    print(json.dumps(check(), ensure_ascii=False, indent=2))
