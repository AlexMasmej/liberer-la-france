"""Contrôles de structure et de traçabilité ; aucune validation juridique."""
import json
import re
from collections import Counter
from html import unescape
from pathlib import Path
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parent
sources = json.loads((root / 'source.json').read_text())
answer = json.loads((root / 'answer.json').read_text())
refs = json.loads((root / 'reference-targets.json').read_text())


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()


allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
classifications = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
cut_kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced'.split())
addition_kinds = set('tax_increased obligation_added deadline_increased complexity_added'.split())
units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
effect_fields = set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
assert len(sources) == len(answer) == 24
assert len({(x['code_id'], x['source_id']) for x in answer}) == 24
for source, obj in zip(sources, answer):
    n = source['number']
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert obj[key] == source[key], (n, key)
    for key in ('reason', 'review_notes'):
        assert isinstance(obj[key], str) and len(obj[key]) > 40, (n, key)
    si = obj['substantive_impact']
    assert si['version'] == 1
    assert si['classification'] in classifications
    assert obj['classification'] == si['classification']
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(si[key]) >= 40, (n, key)
    if obj['status'] == 'retained_unchanged':
        assert obj['proposed_xml'] is None
        assert si['classification'] == 'retained_necessary'
        assert si['effects'] == []
    else:
        assert obj['status'] == 'rewrite_draft'
        xml = obj['proposed_xml']
        assert isinstance(xml, str) and xml
        tree = ET.fromstring('<root>' + xml + '</root>')
        for element in tree.iter():
            if element.tag == 'root':
                continue
            assert element.tag in allowed, (n, element.tag)
            for name, value in element.attrib.items():
                assert name in {'rowspan', 'colspan'} and re.fullmatch(r'\d+', value)
        assert not re.search(r'texte inchangé|\[\.\.\.\]|à compléter', xml, re.I), n
        for ef in si['effects']:
            assert set(ef) == effect_fields, (n, set(ef))
            assert all(isinstance(x, str) and x for x in ef.values()), n
            assert ef['kind'] in kinds and ef['unit'] in units
            assert re.fullmatch(r'[a-z][a-z0-9-]{5,95}', ef['measure_id']), n
            for field, original in [('source_quote', source['source_xml']), ('proposed_quote', xml)]:
                quote = ef[field]
                assert len(quote) >= 12 and '...' not in quote and '…' not in quote, (n, field)
                assert plain(quote) in plain(original), (n, field, quote)
    ekinds = {e['kind'] for e in si['effects']}
    if si['classification'] in {'material_reduction', 'mixed'}:
        assert ekinds & cut_kinds, (n, 'absence de coupe concrète')
    if ekinds & addition_kinds:
        assert si['classification'] == 'mixed', (n, 'ajout non signalé')
    if si['classification'] == 'coordination_only':
        assert ekinds <= {'coordination'}, (n, ekinds)
    if source.get('benefit_check_required'):
        assert len(obj.get('benefit_review', '')) >= 100, n
    if obj.get('change_type') == 'normative_reduction':
        assert obj['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert obj['removed_provisions'] and all(len(v) >= 30 for v in obj['removed_provisions'])
    source_key = source['code_id'] + '|' + source['source_id']
    required = refs['requirements'][source_key]
    checks = obj['reference_checks']
    assert len(checks) == len(required)
    assert {v['target_key'] for v in checks} == set(required)
    for check in checks:
        assert check['view_sha256'] == refs['targets'][check['target_key']]['view_sha256']
        assert len(check['assessment']) >= 80

summary = {
    'article_count': len(answer),
    'statuses': dict(Counter(x['status'] for x in answer)),
    'classifications': dict(Counter(x['substantive_impact']['classification'] for x in answer)),
    'reference_checks': sum(len(x['reference_checks']) for x in answer),
    'benefit_reviews_required_and_present': sum(bool(x.get('benefit_check_required')) for x in sources),
    'scope': 'Structure, identifiants, intégrité des passages cités, balises, empreintes des vues et cohérence des classifications ; aucune validation juridique ni preuve de solde net.'
}
(root / 'answer-checks.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
