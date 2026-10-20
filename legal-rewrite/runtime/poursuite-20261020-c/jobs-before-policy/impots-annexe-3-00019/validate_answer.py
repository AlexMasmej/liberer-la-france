import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from html import unescape
from pathlib import Path

root = Path(__file__).resolve().parent
sources = json.loads((root / 'source.json').read_text())
answer = json.loads((root / 'answer.json').read_text())
expected_fields = {
    'code_id', 'source_id', 'source_sha256', 'number', 'proposed_xml',
    'reason', 'review_notes', 'status',
}
allowed_tags = set(
    'p br table thead tbody tfoot tr th td b strong i em u sup sub '
    'ul ol li div span blockquote'.split()
)


def text(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml)).strip()


def paragraphs(xml):
    matched = re.findall(r'<p\b[^>]*>(.*?)</p>', xml, re.S)
    if matched:
        return [text(part) for part in matched]
    return [text(part) for part in re.split(r'<br\s*/?>', xml) if text(part)]


def marker(paragraph):
    found = re.match(r'^(\d+°|[a-z]\.|[a-z]+\)|[IVX]+\.)', paragraph)
    return found.group(1) if found else None


assert len(sources) == len(answer) == 24
assert len({item['source_id'] for item in answer}) == 24
checks = []
for index, (source, proposal) in enumerate(zip(sources, answer)):
    assert set(proposal) == expected_fields, index
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[key] == proposal[key], (index, key)
    assert proposal['status'] == 'rewrite_draft', index
    assert proposal['reason'] and proposal['review_notes'], index
    xml = proposal['proposed_xml']
    assert isinstance(xml, str) and xml.strip(), index
    parsed = ET.fromstring('<div>' + xml + '</div>')
    for element in parsed.iter():
        assert element.tag in allowed_tags, (index, element.tag)
        for key, value in element.attrib.items():
            assert key in ('rowspan', 'colspan') and re.fullmatch(r'\d+', value)
    source_paragraphs = paragraphs(source['source_xml'])
    proposed_paragraphs = paragraphs(xml)
    assert len(source_paragraphs) == len(proposed_paragraphs), index
    assert [marker(p) for p in source_paragraphs] == [marker(p) for p in proposed_paragraphs], index
    # Les chiffres du texte normatif, y compris les numéros répétés des renvois,
    # sont contrôlés séparément des notes historiques non normatives.
    assert Counter(re.findall(r'\d+', text(source['source_xml']))) == Counter(re.findall(r'\d+', text(xml))), index
    assert text(source['source_xml']) != text(xml), index
    assert len(re.findall(r'<table\b', source['source_xml'])) == len(re.findall(r'<table\b', xml)), index
    checks.append({
        'source_id': source['source_id'],
        'number': source['number'],
        'paragraph_count': len(proposed_paragraphs),
        'identifiers_exact': True,
        'numbers_preserved': True,
        'subdivision_positions_preserved': True,
        'xml_valid': True,
    })

report = {
    'article_count': len(answer),
    'rewritten_count': sum(item['status'] == 'rewrite_draft' for item in answer),
    'checks': checks,
}
(root / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print('24 articles : identifiants, chiffres, alinéas, subdivisions, tableaux, schéma JSON et XML conformes.')
