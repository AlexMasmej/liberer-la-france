import hashlib
import json
import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml))


allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())


class CheckXML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed, tag
        for name, value in attrs:
            assert name in ('rowspan', 'colspan') and value.isdigit(), (tag, attrs)


required_effect_fields = set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
allowed_kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
allowed_classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
allowed_units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
assert len(answer) == len(sources) == 12
assert len({(a['code_id'], a['source_id']) for a in answer}) == 12
for source, row in zip(sources, answer):
    n = row['number']
    for key in ('code_id', 'source_id', 'number', 'source_sha256'):
        assert row[key] == source[key], (n, key)
    key = row['code_id'] + '|' + row['source_id']
    for field, hash_field in [('source_xml', 'source_xml_sha256'), ('source_notes_xml', 'source_notes_sha256')]:
        assert hashlib.sha256(source[field].encode()).hexdigest() == refs['referrers'][key][hash_field], (n, field)
    si = row['substantive_impact']
    assert si['version'] == 1 and si['classification'] in allowed_classes
    for field in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(si[field]) >= 40, (n, field)
    assert len(row['reason']) > 40 and len(row['review_notes']) > 40
    if row['status'] == 'retained_unchanged':
        assert row['proposed_xml'] is None
        assert si['classification'] in ('retained_necessary', 'reserved')
        assert si['effects'] == []
    else:
        assert row['status'] == 'rewrite_draft' and row['proposed_xml']
        CheckXML().feed(row['proposed_xml'])
        assert '\\n' not in row['proposed_xml']
    if source.get('benefit_check_required'):
        assert len(row['benefit_review']) >= 100
    if row.get('change_type') == 'normative_reduction':
        assert row['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert row['removed_provisions'] and all(len(v) >= 30 for v in row['removed_provisions'])
    assert [c['target_key'] for c in row['reference_checks']] == refs['requirements'][key]
    for check in row['reference_checks']:
        assert check['view_sha256'] == refs['targets'][check['target_key']]['view_sha256']
        assert len(check['assessment']) >= 80
    for e in si['effects']:
        assert set(e) == required_effect_fields
        assert e['kind'] in allowed_kinds and e['unit'] in allowed_units
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and len(e['proposed_quote']) >= 12
        assert e['source_quote'] in plain(source['source_xml']), (n, 'source_quote', e['source_quote'])
        assert e['proposed_quote'] in plain(row['proposed_xml']), (n, 'proposed_quote', e['proposed_quote'])
    print(n, row['status'], si['classification'], 'effects', len(si['effects']), 'refs', len(row['reference_checks']))

print('Checks passed. Status:', dict(Counter(a['status'] for a in answer)))
print('Impact:', dict(Counter(a['substantive_impact']['classification'] for a in answer)))
