"""Collect frozen reviewed packs; guard all before-images and dependencies."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, sqlite3, sys

P = Path(__file__).resolve().parent
B = P.parents[1]
sys.path.insert(0, str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc

def read(path):
    return json.loads(path.read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

pairs = [
    ('tsa/edition002', 'source.json', 'answer.json'),
    ('social/edition002', 'source.json', 'answer.json'),
    ('dpae/edition001', 'source.json', 'answer.json'),
    ('urbanisme/edition001', 'source.json', 'answer.json'),
    ('urbanisme/edition001', 'companion-source.json', 'companion-answer.json'),
    ('urbanisme/edition001/papier', 'source.json', 'answer.json'),
    ('crpa-classification/edition001', 'source.json', 'answer.json'),
]
sources, answers, lineage = [], [], []
for folder, sn, an in pairs:
    here = P / folder
    ss, aa = read(here / sn), read(here / an)
    validate_answer(copy.deepcopy(aa), copy.deepcopy(ss))
    sources += ss
    answers += aa
    lineage.append(dict(package=folder, source_file=sn, answer_file=an,
                        source_sha256=sha(here/sn), answer_sha256=sha(here/an)))
keys = {rc.key(s) for s in sources}
assert len(sources) == len(answers) == len(keys) == 96
db = sqlite3.connect('file:' + str(B/'corpus.sqlite') + '?mode=ro', uri=True)
db.execute('BEGIN')
snapshot = dict(version=3, scope='Reviewed whole-article phase B; bounded dependencies',
                policy_sha256=rc.policy_state(), requirements={}, targets={}, referrers={},
                semantic_review_by_jurist=False)
def merge_view(k, v):
    if k in keys:
        return  # Own source and before-image are checked as one bundle below.
    if k in snapshot['targets']:
        assert rc.guard(snapshot['targets'][k]) == rc.guard(v), ('Divergent capture', k)
    snapshot['targets'][k] = v

for folder in ['tsa/edition002', 'dpae/edition001', 'urbanisme/edition001']:
    captured = read(P/folder/'reference-targets.json')
    rc.check_guards(db, captured)
    for k, v in captured['targets'].items():
        merge_view(k, v)
    snapshot['referrers'].update(captured.get('referrers', {}))
    snapshot['requirements'].update(captured.get('requirements', {}))

social = read(P/'social/edition002/context.json')
for s in social:
    k = rc.key(s)
    key = s['code_id'], s['source_id']
    assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key).fetchone() == (s['source_sha256'], s['source_xml']), k
    assert source_notes(db, *key) == s['source_notes_xml'], k
    current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    old = s.get('previous_draft')
    assert current == ((old['source_sha256'], old['proposed_xml']) if old else None), k
    merge_view(k, rc.view(db, k))

checks = []
for s, a in zip(sources, answers):
    k = rc.key(s)
    assert rc.key(a) == k
    key = s['code_id'], s['source_id']
    assert db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', key).fetchone() == (s['number'], s['source_sha256'], s['source_xml']), k
    assert source_notes(db, *key) == s['source_notes_xml'], k
    if s.get('source_document_xml') is not None:
        raw = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", key).fetchone()[0]
        raw = raw.decode() if isinstance(raw, bytes) else raw
        assert raw == s['source_document_xml'], k
    current = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    old = s.get('previous_draft')
    assert current == ((old['source_sha256'], old['proposed_xml']) if old else None), ('Changed proposal', k)
    checks.append(dict(code_id=key[0], source_id=key[1], number=s['number'],
                       source_and_notes_exact=True, before_image_exact=True))
rc.check_guards(db, snapshot)
db.close()
out = P/'integration/edition001'
out.mkdir(parents=True, exist_ok=True)
assert not (out/'registration.json').exists()
save(out/'source.json', sources)
save(out/'answer.json', answers)
save(out/'reference-targets.json', snapshot)
save(out/'preflight.json', dict(checked_at=datetime.now(timezone.utc).isoformat(),
    sources=len(sources), external_guarded_targets=len(snapshot['targets']),
    whole_source_notes_before_images=checks, packages=lineage,
    canonical_mutation=False, all_five_codes_completed=False))
save(P/'urbanisme/edition001/root-independent-review.json', dict(
    reviewed_at=datetime.now(timezone.utc).isoformat(),
    reviewer='Parent independent of author',
    sources_and_notes_read_entire=30, proposals_read_entire=24,
    retained_necessary=6,
    critical_contexts_read_entire=['L433-1','L433-2','L433-3','L433-4','L433-5','L433-6','L433-7','R474-1'],
    findings=[], scope='Only these 30 articles and identified dependencies; no jurist audit',
    retained_favorable_division_exemptions=True,
    actual_new_measures=8, whole_procedures_abolished=0,
    paper_copy_public_cost='Unknown; transferred burden classified mixed',
    existing_CRPA_rights_not_counted_as_new=True,
    proposal_hashes={an:sha(P/folder/an) for folder,sn,an in pairs if folder.startswith('urbanisme')},
    semantic_review_by_jurist=False))
print(json.dumps(dict(articles=len(sources), dependencies=len(snapshot['targets']),
    new=sum(not s.get('previous_draft') for s in sources),
    revisions=sum(bool(s.get('previous_draft')) for s in sources),
    schema_and_guards=True, awaiting_independent_social_delta=True)))
