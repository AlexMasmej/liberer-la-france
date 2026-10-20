import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
fields = {'code_id', 'source_id', 'source_sha256', 'number', 'proposed_xml',
          'reason', 'review_notes', 'status'}
allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())


def plain(xml):
    return re.sub(r'<[^>]*>', ' ', xml)


def paragraphs(xml):
    explicit = re.findall(r'<p\b[^>]*>(.*?)</p>', xml, re.S)
    if explicit:
        return explicit
    return [piece.strip() for piece in re.split(r'<br\s*/?>', xml)
            if plain(piece).strip()]


def references(xml):
    return Counter(re.findall(r'\bL\.\s*\d+(?:-\d+)*', plain(xml)))


def numerals(xml):
    return Counter(re.findall(r'\b\d+(?:-\d+)*\b', plain(xml)))


assert len(sources) == len(answer) == 24
assert len({item['source_id'] for item in answer}) == 24
report = []
for source, draft in zip(sources, answer):
    number = source['number']
    assert set(draft) == fields, (number, 'fields')
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert draft[key] == source[key], (number, key)
    assert draft['status'] == 'rewrite_draft', number
    for key in ('proposed_xml', 'reason', 'review_notes'):
        assert isinstance(draft[key], str) and draft[key].strip(), (number, key)
    assert draft['proposed_xml'].strip() != source['source_xml'].strip(), number
    root = ET.fromstring('<root>' + draft['proposed_xml'] + '</root>')
    for element in root.iter():
        if element.tag == 'root':
            continue
        assert element.tag in allowed_tags, (number, element.tag)
        for key, value in element.attrib.items():
            assert key in ('colspan', 'rowspan') and re.fullmatch(r'[0-9]+', value), (number, key, value)
    source_paragraphs = paragraphs(source['source_xml'])
    draft_paragraphs = paragraphs(draft['proposed_xml'])
    assert len(source_paragraphs) == len(draft_paragraphs), (number, 'paragraphs')
    for i, (old, new) in enumerate(zip(source_paragraphs, draft_paragraphs), start=1):
        assert references(old) == references(new), (number, i, 'references')
        assert numerals(old) == numerals(new), (number, i, 'numerals')
        heading = r'^\s*((?:[IVX]+\s*\.-?)|(?:\d+°(?:\s+bis)?)|(?:[a-z]\)))'
        old_heading = re.match(heading, plain(old))
        new_heading = re.match(heading, plain(new))
        normalize = lambda match: re.sub(r'[\s.\-]', '', match.group(1)) if match else None
        assert normalize(old_heading) == normalize(new_heading), (number, i, 'heading')
    assert source['source_xml'].count('<table') == draft['proposed_xml'].count('<table'), (number, 'tables')
    report.append({'number': number, 'paragraphs': len(draft_paragraphs),
                   'references_and_numerals_by_paragraph': 'ok',
                   'xml_and_identifiers': 'ok'})

Path('validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print('24 articles : structure, identifiants, alinéas, subdivisions, renvois et chiffres par alinéa conformes.')
print('Tableaux dans le lot : 0. Articles avec notes historiques :', sum(bool(x['source_notes_xml'].strip()) for x in sources))
print('Taille de answer.json :', Path('answer.json').stat().st_size, 'octets.')
