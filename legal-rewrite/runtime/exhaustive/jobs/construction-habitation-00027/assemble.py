import json
from pathlib import Path

root = Path(__file__).resolve().parent
sources = json.loads((root / 'source.json').read_text())
drafts = {}
for path in sorted((root / 'fragments').glob('*.json')):
    for draft in json.loads(path.read_text()):
        if draft['number'] in drafts:
            raise ValueError(f"Duplicate article: {draft['number']}")
        drafts[draft['number']] = draft

assert len(sources) == len(drafts) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    draft = drafts[source['number']]
    record = {key: source[key] for key in
              ('code_id', 'source_id', 'source_sha256', 'number')}
    record.update({key: draft[key] for key in
                   ('proposed_xml', 'reason', 'review_notes')})
    record['status'] = 'rewrite_draft'
    answer.append(record)
(root / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
