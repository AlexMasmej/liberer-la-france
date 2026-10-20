import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

source = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())

def plain(value):
    return html.unescape(re.sub(r'<[^>]+>', '', value or ''))

assert len(source) == len(answer) == 24
assert len({a['source_id'] for a in answer}) == 24
for s, a in zip(source, answer):
    for key in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert a[key] == s[key], (a['number'], key)
    for key in ['reason', 'review_notes']:
        assert isinstance(a[key], str) and len(a[key]) > 40, (a['number'], key)
    impact = a['substantive_impact']
    assert impact['version'] == 1 and impact['classification'] in classes
    for key in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(impact[key]) >= 40, (a['number'], key)
    if s.get('benefit_check_required'):
        assert len(a['benefit_review']) >= 100, a['number']
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == impact['classification'] == 'retained_necessary'
        assert impact['effects'] == []
    else:
        assert a['status'] == 'rewrite_draft'
        assert isinstance(a['proposed_xml'], str)
        assert a['proposed_xml'] != s['source_xml']
        root = ET.fromstring('<root>' + a['proposed_xml'] + '</root>')
        for elem in list(root.iter())[1:]:
            assert elem.tag in allowed, (a['number'], elem.tag)
            for key, value in elem.attrib.items():
                assert key in ['rowspan', 'colspan'] and value.isdecimal()
        assert 'texte inchangé' not in a['proposed_xml'].lower()
    if a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert a['removed_provisions']
        assert all(len(v) >= 30 for v in a['removed_provisions'])
    for e in impact['effects']:
        assert set(e) == set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
        assert e['kind'] in kinds and e['unit'] in units
        assert re.fullmatch('[a-z][a-z0-9-]{5,95}', e['measure_id'])
        assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(s['source_xml'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml'])
        assert all(isinstance(v, str) and v for v in e.values())
    req = refs['requirements'][s['code_id'] + '|' + s['source_id']]
    assert [c['target_key'] for c in a['reference_checks']] == req
    for check in a['reference_checks']:
        target = refs['targets'][check['target_key']]
        assert check['view_sha256'] == target['view_sha256']
        assert len(check['assessment']) >= 80
        view = target['proposed_xml'] if target['view_kind'] == 'proposal' else target['source_xml']
        assert hashlib.sha256(view.encode()).hexdigest() == check['view_sha256']

# Conserver exactement les alinéas qui ne portent pas la réforme, à leur place.
unchanged_paragraphs = {
    'L443-1': [0, 2, 3, 4],
    'L452-4': [0, 1, 2, 3, 5, 6],
    'L453-1': [0, 2],
    'L454-1': [0, 1, 2, 3, 5, 6, 8, 9, 10],
    'L454-2': [0, 3, 5],
    'L461-1': [0, 1, 2, 3, 4, 5, 6, 8],
}
for s, a in zip(source, answer):
    if a['number'] not in unchanged_paragraphs:
        continue
    old = re.findall(r'<p>(.*?)</p>', s['source_xml'], re.S)
    new = re.findall(r'<p>(.*?)</p>', a['proposed_xml'], re.S)
    for index in unchanged_paragraphs[a['number']]:
        assert old[index] == new[index], (a['number'], index)
    if a['number'] == 'L454-1':
        assert new[4].startswith(old[4]) and old[7] in new[7]
    if a['number'] == 'L461-1':
        assert new[7] == old[7].replace("à l'article L. 315-1", "au I de l'article L. 315-2")

print(f'Contrôles structurels réussis : {len(answer)} identités, XML, statuts, citations exactes, avantages et {sum(len(a["reference_checks"]) for a in answer)} cibles/empreintes.')
print('Alinéas maintenus : texte, chiffres et place identiques à la source.')
print('Ces contrôles ne constituent pas une validation juridique.')
