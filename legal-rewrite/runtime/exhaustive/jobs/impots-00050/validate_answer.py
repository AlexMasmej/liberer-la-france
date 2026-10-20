import json
import re
import html
import hashlib
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

s = json.loads(Path('source.json').read_text())
a = json.loads(Path('answer.json').read_text())
r = json.loads(Path('reference-targets.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())

def text(x):
    return html.unescape(re.sub('<[^>]*>', '', x or ''))

assert len(s) == len(a) == 19
assert len({(z['code_id'], z['source_id']) for z in a}) == 19
for src, ans in zip(s, a):
    n = src['number']
    for k in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert src[k] == ans[k], (n, k)
    assert len(ans['reason']) > 40 and len(ans['review_notes']) > 40
    imp = ans['substantive_impact']
    assert imp['version'] == 1 and imp['classification'] in classes
    for k in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(imp[k]) >= 40, (n, k)
    if src.get('benefit_check_required'):
        assert len(ans['benefit_review']) >= 100
    proposed = ans['proposed_xml']
    if proposed is None:
        assert ans['status'] == 'retained_unchanged'
        assert ans['classification'] == imp['classification'] == 'retained_necessary'
        assert imp['effects'] == []
    else:
        assert ans['status'] == 'rewrite_draft'
        root = ET.fromstring('<root>' + proposed + '</root>')
        for el in root.iter():
            if el.tag == 'root':
                continue
            assert el.tag in allowed, (n, el.tag)
            for k, v in el.attrib.items():
                assert k in ['rowspan', 'colspan'] and v.isdigit(), (n, k, v)
        assert proposed != src['source_xml'], n
    if ans.get('change_type') == 'normative_reduction':
        assert ans['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert all(len(z) >= 30 for z in ans['removed_provisions'])
    for ef in imp['effects']:
        assert ef['kind'] in kinds and ef['unit'] in units
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', ef['measure_id'])
        assert 6 <= len(ef['measure_id']) <= 96
        for k, body in [('source_quote', src['source_xml']), ('proposed_quote', proposed)]:
            assert len(ef[k]) >= 12, (n, k)
            assert ef[k] in text(body), (n, k, ef[k])
        for k in ['description', 'before', 'after', 'affected_population',
                  'conditions_and_transition', 'replacement_or_new_burdens']:
            assert isinstance(ef[k], str) and ef[k], (n, k)
    required = r['requirements'][src['code_id'] + '|' + src['source_id']]
    checks = ans.get('reference_checks', [])
    assert [c['target_key'] for c in checks] == required, n
    for check in checks:
        assert check['view_sha256'] == r['targets'][check['target_key']]['view_sha256']
        assert len(check['assessment']) >= 80
    print(n + ': ' + ans['status'] + ' / ' + imp['classification'] +
          ' / ' + str(len(imp['effects'])) + ' effets / ' + str(len(checks)) + ' cibles')

# Comparaison exhaustive par paragraphe des deux longs articles partiellement réduits.
for i, expected_changed in [(0, {33, 34, 36, 37, 42, 43, 44, 45, 46, 47, 61}),
                            (1, {5}), (15, {2})]:
    before = re.findall(r'<p>.*?</p>', s[i]['source_xml'], re.S)
    after = re.findall(r'<p>.*?</p>', a[i]['proposed_xml'], re.S)
    changed = {j for j, v in enumerate(before) if v != after[j]}
    assert changed == expected_changed, (s[i]['number'], changed)
    print(s[i]['number'], ':', len(before) - len(changed),
          'paragraphes sources reproduits intégralement ;', len(changed),
          'paragraphes modifiés et', len(after) - len(before), 'ajoutés')

print('Comptage :', dict(Counter(z['substantive_impact']['classification'] for z in a)))
print('Références obligatoires :', sum(len(z.get('reference_checks', [])) for z in a))
print('Empreinte answer.json :', hashlib.sha256(Path('answer.json').read_bytes()).hexdigest())
print('Contrôles structurels et citations exactes : OK ; aucune validation juridique indépendante inférée.')
