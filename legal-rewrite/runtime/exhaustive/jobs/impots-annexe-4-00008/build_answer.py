import json
from pathlib import Path
import draft_part1
import draft_part2
import draft_part3

sources = json.loads(Path('source.json').read_text())
draft_part3.add_nomenclature(next(a['source_xml'] for a in sources if a['number'] == '41 undecies'))
drafts = draft_part1.drafts | draft_part2.drafts | draft_part3.drafts
assert len(sources) == len(drafts) == 24
answer = []
for source in sources:
    text, reason, notes = drafts[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': text.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
