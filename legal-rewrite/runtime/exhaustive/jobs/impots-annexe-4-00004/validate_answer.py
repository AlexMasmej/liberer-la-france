import hashlib
import html
import json
import re
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


source = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
required = {
    'code_id', 'source_id', 'source_sha256', 'number',
    'proposed_xml', 'reason', 'review_notes', 'status',
}
allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', ' ', xml))


def numbers(xml):
    return Counter(re.findall(r'\d+(?:,\d+)?', plain(xml)))


def labels(xml):
    # Br-separated source paragraphs and p-separated drafts retain the same labels.
    text = html.unescape(re.sub(r'<(?:br\b[^>]*|/?p\b[^>]*)>', '\n', xml))
    text = re.sub(r'<[^>]*>', ' ', text)
    return re.findall(r'^\s*((?:\d+°(?:\s+bis)?|\d+\.|[a-z](?:\s+bis)?[.)]|[IVX]+\.))', text, re.M)


assert len(source) == len(answer) == 24
assert len({a['source_id'] for a in answer}) == 24
report = []
for s, a in zip(source, answer):
    assert set(a) == required, a['number']
    for k in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[k] == s[k], (a['number'], k)
    assert a['status'] == 'rewrite_draft'
    assert all(isinstance(a[k], str) and a[k].strip() for k in ('proposed_xml', 'reason', 'review_notes'))
    xml = a['proposed_xml']
    tree = ET.fromstring('<div>' + xml + '</div>')
    for node in tree.iter():
        assert node.tag in allowed_tags, (a['number'], node.tag)
        for key, value in node.attrib.items():
            assert key in {'rowspan', 'colspan'} and re.fullmatch(r'[0-9]+', value), (a['number'], key)
    assert not re.search(r'https?://|```|<!--|<\?', xml)
    assert not re.search(r'texte inchangé|voir (?:le )?texte|résumé|à compléter', xml, re.I)
    assert re.sub(r'\s+', ' ', plain(xml)).strip() != re.sub(r'\s+', ' ', plain(s['source_xml'])).strip(), a['number']
    assert labels(s['source_xml']) == labels(xml), (a['number'], labels(s['source_xml']), labels(xml))

    old, new = numbers(s['source_xml']), numbers(xml)
    removed, added = old - new, new - old
    assert not removed, (a['number'], 'removed numbers', removed)
    expected_added = {'23 A': Counter({'23': 1}), '23 B': Counter({'23': 1}), '23 G': Counter({'23': 2})}.get(a['number'], Counter())
    assert added == expected_added, (a['number'], 'added numbers', added, expected_added)
    report.append({
        'number': a['number'],
        'identifiers_exact': True,
        'xml_valid_and_allowed': True,
        'subdivision_labels_preserved': True,
        'numeric_tokens_preserved': True,
        'added_numeric_tokens': dict(added),
    })

bis_s = next(s for s in source if s['number'] == '23 L bis')
bis_a = next(a for a in answer if a['number'] == '23 L bis')
root_s = ET.fromstring('<div>' + bis_s['source_xml'] + '</div>')
root_a = ET.fromstring('<div>' + bis_a['proposed_xml'] + '</div>')
source_series = []
for p in root_s:
    pairs = re.findall(r'Années? (\d{4}(?: et antérieures)?)\s*:\s*([0-9]+(?:,[0-9]+)?)\.', ''.join(p.itertext()))
    if pairs:
        source_series.append(pairs)
proposed_series = []
for table in root_a.findall('table'):
    pairs = [tuple(td.text for td in tr.findall('td')) for tr in table.findall('./tbody/tr')]
    proposed_series.append(pairs)
assert source_series == proposed_series
assert [len(series) for series in proposed_series] == [63, 63, 63, 63]
assert proposed_series[0][58] == ('1972', '63')

# Technical lists, including their qualifiers, remain exhaustive.
by_number = {a['number']: a['proposed_xml'] for a in answer}
for value in ['LFP', 'LMP', 'LMFP', 'LMO', 'LNMO', 'NMC', 'NCA', 'NMx', 'LCO', 'Na-ion', 'Zinc', 'LTO', 'lithium-soufre', 'lithium solide et semi-solide', 'graphite artificiel', 'graphite naturel', 'manganèse', 'cobalt', 'rebuts de production']:
    assert value in by_number['23 M bis'], value
for value in ['polysilicium de qualité photovoltaïque', 'lingots de silicium de qualité photovoltaïque', 'plaquettes photovoltaïques', 'verre solaire', 'y compris pilotables', 'structures porteuses spécifiques aux traqueurs', 'onduleurs', 'silicium, le germanium et le cuivre', '(PVT)']:
    assert value in by_number['23 M ter'], value
assert by_number['23 M ter'].count("d'une capacité équivalente") == 2
assert 'sur le même site' not in by_number['23 M ter']

result = {
    'article_count': len(answer),
    'source_file_sha256': hashlib.sha256(Path('source.json').read_bytes()).hexdigest(),
    'coefficient_tables': len(proposed_series),
    'coefficient_rows': sum(map(len, proposed_series)),
    'coefficient_pairs_and_order_exact': True,
    'articles': report,
}
Path('validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print('Validation réussie : 24 articles, identifiants exacts, XML autorisé, subdivisions et chiffres conservés ; 252 couples année-coefficient identiques dans 4 tableaux.')
