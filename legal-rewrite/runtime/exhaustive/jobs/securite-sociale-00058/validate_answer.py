import hashlib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


class TextAndTags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.tags = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, attrs))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def plain(xml):
    parser = TextAndTags()
    parser.feed(xml or '')
    return ''.join(parser.parts), parser.tags


sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
previous = json.loads(Path('previous-answer.json').read_text())
source_index = {(s['code_id'], s['source_id']): s for s in sources}
old_index = {(s['code_id'], s['source_id']): s for s in previous}
assert len(answers) == len(sources) == 24
assert len({(a['code_id'], a['source_id']) for a in answers}) == 24
assert {(a['code_id'], a['source_id']) for a in answers} == set(source_index)

allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
allowed_classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
allowed_kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
allowed_units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
effect_fields = set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())

for key, target in refs['targets'].items():
    for field, hashfield in [('source_xml', 'source_xml_sha256'), ('source_notes_xml', 'source_notes_sha256')]:
        assert hashlib.sha256(target[field].encode()).hexdigest() == target[hashfield], (key, field)
    view = target['proposed_xml'] if target['proposed_xml'] is not None else target['source_xml']
    assert hashlib.sha256(view.encode()).hexdigest() == target['view_sha256'], key

for a in answers:
    key = a['code_id'], a['source_id']
    s = source_index[key]
    for field in ['code_id', 'source_id', 'number', 'source_sha256']:
        assert a[field] == s[field], (a['number'], field)
    assert all(field in a for field in ['proposed_xml', 'reason', 'review_notes', 'status'])
    assert a['reason'] and a['review_notes']
    source_text, _ = plain(s['source_xml'])
    proposal_text, tags = plain(a['proposed_xml'])
    for tag, attrs in tags:
        assert tag in allowed_tags, (a['number'], tag)
        for attr, value in attrs:
            assert attr in ['rowspan', 'colspan'] and value.isdigit(), (a['number'], attr)
    impact = a['substantive_impact']
    assert impact['version'] == 1 and impact['classification'] in allowed_classes
    for f in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(impact[f]) >= 40, (a['number'], f)
    assert isinstance(impact['effects'], list)
    for e in impact['effects']:
        assert set(e) == effect_fields, (a['number'], set(e) ^ effect_fields)
        assert e['kind'] in allowed_kinds and e['unit'] in allowed_units
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and e['source_quote'] in source_text, (a['number'], 'source quote')
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in proposal_text, (a['number'], 'proposed quote')
        assert all(isinstance(value, str) and value for value in e.values())
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == impact['classification'] == 'retained_necessary'
        assert impact['effects'] == []
    else:
        assert a['status'] == 'rewrite_draft' and proposal_text.strip()
        assert a['proposed_xml'] != s['source_xml']
    if a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert a['removed_provisions'] and all(len(x) >= 30 for x in a['removed_provisions'])
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review', '')) >= 100
    req = refs['requirements']['|'.join(key)]
    checks = a.get('reference_checks', [])
    assert [c['target_key'] for c in checks] == req, (a['number'], 'target coverage')
    for c in checks:
        assert set(c) == {'target_key', 'view_sha256', 'assessment'}
        assert c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment']) >= 80
        old_checks = old_index[key].get('reference_checks', [])
        assert c['assessment'] not in [old['assessment'] for old in old_checks], (a['number'], 'old assessment')
    if '|'.join(key) in refs['referrers']:
        referrer = refs['referrers']['|'.join(key)]
        assert a['source_sha256'] == referrer['source_sha256']
        assert hashlib.sha256(s['source_xml'].encode()).hexdigest() == referrer['source_xml_sha256']
        assert hashlib.sha256(s['source_notes_xml'].encode()).hexdigest() == referrer['source_notes_sha256']
    assert a['proposed_xml'] == old_index[key]['proposed_xml'], (a['number'], 'unintended normative change')

print(json.dumps({
    'article_count': len(answers),
    'current_reference_checks': sum(len(a.get('reference_checks', [])) for a in answers),
    'status_counts': dict(Counter(a['status'] for a in answers)),
    'impact_counts': dict(Counter(a['substantive_impact']['classification'] for a in answers)),
    'exact_effect_quotes_checked': sum(2 * len(a['substantive_impact']['effects']) for a in answers),
    'preserved_normative_bodies': True,
    'validation_scope': 'Contrôles de structure, citations, empreintes et couverture ; aucune validation juridique indépendante.',
}, ensure_ascii=False, indent=2))
