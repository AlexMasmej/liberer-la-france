import json
from pathlib import Path


def main():
    sources = json.loads(Path('source.json').read_text())
    drafts = []
    for name in (
        '01-representation.json',
        '02-non-amortissables.json',
        '03-amortissables.json',
    ):
        drafts.extend(json.loads((Path('fragments') / name).read_text()))
    assert len(sources) == len(drafts) == 24
    answer = []
    for source, draft in zip(sources, drafts):
        assert source['number'] == draft['number']
        item = {
            key: source[key]
            for key in ('code_id', 'source_id', 'source_sha256', 'number')
        }
        item.update({
            key: draft[key]
            for key in ('proposed_xml', 'reason', 'review_notes')
        })
        item['status'] = 'rewrite_draft'
        answer.append(item)
    Path('answer.json').write_text(
        json.dumps(answer, ensure_ascii=False, indent=2) + '\n'
    )
    print(f'answer.json : {len(answer)} articles')


if __name__ == '__main__':
    main()
