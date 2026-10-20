import json
import re
from collections import Counter
from html import unescape
from pathlib import Path
from xml.etree import ElementTree as ET

sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
keys = {'code_id', 'source_id', 'source_sha256', 'number', 'proposed_xml', 'reason', 'review_notes', 'status'}
allowed_tags = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
assert len(sources) == len(answer) == 24
assert len({a['source_id'] for a in answer}) == 24

def text(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()

def paragraphs(xml):
    root = ET.fromstring('<root>' + xml + '</root>')
    ps = root.findall('.//p')
    if ps:
        return [text(ET.tostring(p, encoding='unicode')) for p in ps]
    return [text(p) for p in re.split(r'<br\s*/?>', xml) if text(p)]

def label(p):
    found = re.match(r'^(I{1,3}|IV)\s*\.', p)
    if found: return found[1]
    found = re.match(r'^(\d+\s+bis)(?=\s|\.)', p)
    if found: return found[1]
    found = re.match(r'^(\d+[°.])', p)
    if found: return found[1]
    found = re.match(r'^([a-z][.)])', p)
    return found[1] if found else None

expected_numeric_differences = {
    '47': {'added': Counter({'240': 1, '241': 1}), 'removed': Counter()},
    '49 B': {'added': Counter({'3': 1}), 'removed': Counter()},
}
checks = []
for source, proposed in zip(sources, answer):
    assert set(proposed) == keys, proposed['number']
    for k in ('code_id','source_id','source_sha256','number'):
        assert source[k] == proposed[k], (source['number'],k)
    assert proposed['status'] == 'rewrite_draft'
    assert all(isinstance(proposed[k],str) and proposed[k].strip() for k in ('proposed_xml','reason','review_notes'))
    xml = proposed['proposed_xml']
    root = ET.fromstring('<root>' + xml + '</root>')
    for element in root.iter():
        if element is root: continue
        assert element.tag in allowed_tags, element.tag
        for name, value in element.attrib.items():
            assert name in ('rowspan','colspan') and re.fullmatch(r'[0-9]+',value)
    assert not re.search(r'```|\]\(|texte inchangé|à compléter|\[\.\.\.\]', xml, flags=re.I)
    assert text(source['source_xml']) != text(xml), source['number']
    before, after = paragraphs(source['source_xml']), paragraphs(xml)
    assert len(before) == len(after), (source['number'],len(before),len(after))
    assert list(map(label,before)) == list(map(label,after)), source['number']
    source_nums = Counter(re.findall(r'\d+', re.sub(r'\(1\)', '', source['source_xml'])))
    proposed_nums = Counter(re.findall(r'\d+', xml))
    numeric_diff = {'added': proposed_nums - source_nums, 'removed': source_nums - proposed_nums}
    expected = expected_numeric_differences.get(source['number'], {'added': Counter(), 'removed': Counter()})
    assert numeric_diff == expected, (source['number'], numeric_diff)
    for tag in ('table','thead','tbody','tfoot','tr','th','td'):
        assert len(re.findall(r'<' + tag + r'\b',source['source_xml'])) == len(root.findall('.//'+tag))
    checks.append({'number': source['number'], 'identifiers_exact': True, 'paragraphs': len(after), 'subdivisions_preserved': True, 'numerals_checked': True, 'permitted_markup_only': True, 'rewritten': True})
report = {
    'article_count': len(answer),
    'rewrite_draft_count': len(answer),
    'source_table_count': sum(len(re.findall(r'<table\b',s['source_xml'])) for s in sources),
    'proposed_character_count': sum(len(a['proposed_xml']) for a in answer),
    'checks': checks,
    'numeric_explanations': {
        '47': 'Articles 240 et 241 répétés pour expliciter les renseignements additionnels ; leurs autres occurrences sont réordonnées.',
        '49 B': 'Le premier alinéa est explicitement identifié comme celui du 3, sans déplacement de texte.',
        'notes': 'Appels (1) retirés pour 49 B, 49 D et 49 I bis ; leur contenu est consigné dans review_notes.'
    }
}
Path('verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'valid': True, 'articles': len(answer), 'paragraphs': sum(c['paragraphs'] for c in checks), 'tables':report['source_table_count'], 'all_identifiers_exact': True, 'all_numerals_checked': True, 'all_subdivisions_preserved': True},ensure_ascii=False))
