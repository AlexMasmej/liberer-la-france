import json
from pathlib import Path
sources = json.loads(Path('source.json').read_text())
drafts = []
for name in ('part1.json', 'part2.json', 'part3.json'):
    drafts.extend(json.loads((Path('drafts') / name).read_text()))
assert len(sources) == len(drafts) == 24
answer = []
for source, draft in zip(sources, drafts):
    assert source['number'] == draft['number']
    row = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update({k: draft[k] for k in ('proposed_xml', 'reason', 'review_notes')})
    row['status'] = 'rewrite_draft'
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles, {sum(len(a["proposed_xml"]) for a in answer)} caractères proposés')
