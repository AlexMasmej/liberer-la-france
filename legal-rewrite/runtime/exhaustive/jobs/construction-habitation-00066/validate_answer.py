import collections
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())


def plain(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()


assert len(answer) == len(sources) == 24
assert len({a['source_id'] for a in answer}) == 24
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
for a, s in zip(answer, sources):
    n = a['number']
    for k in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert a[k] == s[k], (n, k)
    assert len(a['reason']) >= 40 and len(a['review_notes']) >= 40
    si = a['substantive_impact']
    assert si['version'] == 1 and si['classification'] in classes
    for k in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(si[k]) >= 40, (n, k)
    pairs = [(e['measure_id'], e['kind']) for e in si['effects']]
    assert len(pairs) == len(set(pairs)), (n, 'Duplicate measure and effect in one article')
    measures = [e['measure_id'] for e in si['effects']]
    assert len(measures) == len(set(measures)), (n, 'Repeated measure in one article')
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == si['classification'] == 'retained_necessary'
        assert si['effects'] == []
    else:
        assert a['status'] == 'rewrite_draft'
        root = ET.fromstring('<root>' + a['proposed_xml'] + '</root>')
        for el in root.iter():
            if el.tag != 'root':
                assert el.tag in allowed, (n, el.tag)
            for k, v in el.attrib.items():
                assert k in ['rowspan', 'colspan'] and v.isdecimal(), (n, k)
        assert len(plain(a['proposed_xml'])) > 30
    for e in si['effects']:
        assert e['kind'] in kinds and e['unit'] in units
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        for k, haystack in [('source_quote', plain(s['source_xml'])), ('proposed_quote', plain(a['proposed_xml']))]:
            assert len(e[k]) >= 12 and e[k] in haystack, (n, k, e[k])
        for k in ['description', 'before', 'after', 'affected_population', 'conditions_and_transition', 'replacement_or_new_burdens']:
            assert isinstance(e[k], str) and len(e[k]) > 12, (n, k)
    required = refs['requirements'][a['code_id'] + '|' + a['source_id']]
    assert [c['target_key'] for c in a['reference_checks']] == required, (n, 'reference set')
    for c in a['reference_checks']:
        assert c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment']) >= 80
    if s.get('benefit_check_required'):
        assert len(a['benefit_review']) >= 100
    if a.get('change_type') == 'full_repeal':
        assert a['repeal_policy_id'] == 'editorial_direction_2026_10_19'
        assert len(a['repeal_scope']) >= 30
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
    elif a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert a['removed_provisions'] and all(len(v) >= 30 for v in a['removed_provisions'])

print('Structure JSON/XML, identifiants, citations, références et effets uniques : OK')
print('Articles :', len(answer))
print('Statuts :', dict(collections.Counter(a['status'] for a in answer)))
print('Impacts :', dict(collections.Counter(a['substantive_impact']['classification'] for a in answer)))
print('Vérifications de cibles :', sum(len(a['reference_checks']) for a in answer))
print('Contrôle technique de cohérence ; ne constitue pas une validation juridique.')
