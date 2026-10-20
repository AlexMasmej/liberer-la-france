import json
import re
import html
import hashlib
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


def plain(value):
    return html.unescape(re.sub(r'<[^>]+>', '', value or ''))


sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
assert len(sources) == len(answers) == 24
allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
allowed_kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
allowed_units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
required = set('code_id source_id source_sha256 number proposed_xml reason review_notes status substantive_impact'.split())
for s, a in zip(sources, answers):
    assert required <= a.keys(), s['number']
    for k in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[k] == s[k], (s['number'], k)
    assert len(a['reason']) >= 80 and len(a['review_notes']) >= 80
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review', '')) >= 100, s['number']
    si = a['substantive_impact']
    assert si['version'] == 1
    for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert isinstance(si[k], str) and len(si[k]) >= 40, (s['number'], k)
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None and a['classification'] == 'retained_necessary'
        assert si['classification'] == 'retained_necessary' and si['effects'] == []
    else:
        assert a['status'] == 'rewrite_draft'
        assert a['proposed_xml'] and a['proposed_xml'] != s['source_xml']
        tree = ET.fromstring('<root>'+a['proposed_xml']+'</root>')
        for element in tree.iter():
            assert element.tag == 'root' or element.tag in allowed_tags, (s['number'], element.tag)
            for name, value in element.attrib.items():
                assert name in ('rowspan', 'colspan') and re.fullmatch(r'\d+', value)
        if a.get('change_type') == 'full_repeal':
            assert a['repeal_policy_id'] == 'editorial_direction_2026_10_19'
            assert len(a['repeal_scope']) >= 30
            assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        if a.get('change_type') == 'normative_reduction':
            assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
            assert a['removed_provisions'] and all(len(v) >= 30 for v in a['removed_provisions'])
        for e in si['effects']:
            assert set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split()) == e.keys()
            assert e['kind'] in allowed_kinds and e['unit'] in allowed_units
            assert re.fullmatch(r'[a-z][a-z0-9-]{5,95}', e['measure_id'])
            assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(s['source_xml']), (s['number'], 'source_quote', e['source_quote'])
            assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml']), (s['number'], 'proposed_quote', e['proposed_quote'])
    key = s['code_id']+'|'+s['source_id']
    assert [c['target_key'] for c in a['reference_checks']] == refs['requirements'][key]
    for c in a['reference_checks']:
        target = refs['targets'][c['target_key']]
        assert c['view_sha256'] == target['view_sha256']
        assert len(c['assessment']) >= 80
        assert hashlib.sha256(target['source_xml'].encode()).hexdigest() == target['source_xml_sha256']
        assert hashlib.sha256(target['source_notes_xml'].encode()).hexdigest() == target['source_notes_sha256']

# Les maintiens partiels doivent garder leurs paragraphes utiles, sans renumérotation.
by_source = {a['number']: a for a in sources}
by_answer = {a['number']: a for a in answers}
for number, untouched in [('L442-1', [0, 2, 3, 4]), ('L442-3-1', [0, 1, 2, 4, 5]),
                          ('L442-4-3', [0])]:
    sp = re.findall(r'<p>(.*?)</p>', by_source[number]['source_xml'], re.S)
    ap = re.findall(r'<p>(.*?)</p>', by_answer[number]['proposed_xml'], re.S)
    for index in untouched:
        assert sp[index] == ap[index], (number, 'paragraph', index)
sp = re.findall(r'<p>(.*?)</p>', by_source['L442-3']['source_xml'], re.S)
ap = re.findall(r'<p>(.*?)</p>', by_answer['L442-3']['proposed_xml'], re.S)
for i in list(range(7)) + [8, 9]:
    assert sp[i] == ap[i], ('L442-3', 'paragraph', i)
assert len(re.findall(r'<p>', by_answer['L442-1']['proposed_xml'])) == 5
assert by_source['L442-2-1']['source_xml'].count('<table') == 2
assert by_answer['L442-2-1']['proposed_xml'] is None

print('Contrôles de structure, identité, balises, citations, renvois et paragraphes : OK')
print('Statuts :', dict(Counter(a['status'] for a in answers)))
print('Impacts :', dict(Counter(a['substantive_impact']['classification'] for a in answers)))
print('Références contrôlées :', sum(len(a['reference_checks']) for a in answers))
print('Empreinte answer.json :', hashlib.sha256(Path('answer.json').read_bytes()).hexdigest())
