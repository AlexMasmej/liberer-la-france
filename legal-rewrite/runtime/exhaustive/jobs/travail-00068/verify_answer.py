import json
import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    parser = PlainText()
    parser.feed(value)
    return unescape(''.join(parser.parts))


def normalized(value):
    return re.sub(r'\s+', ' ', value).strip()


class AllowedMarkup(HTMLParser):
    allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())

    def handle_starttag(self, tag, attributes):
        assert tag in self.allowed, tag
        for key, value in attributes:
            assert key in ('rowspan', 'colspan') and value.isdigit(), (key, value)


sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
assert len(sources) == len(answers) == 24
assert len({a['source_id'] for a in answers}) == 24
effect_keys = set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
for source, answer in zip(sources, answers):
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[key] == answer[key], (source['number'], key)
    for key in ('reason', 'review_notes', 'status', 'proposed_xml', 'substantive_impact'):
        assert key in answer, (source['number'], key)
    impact = answer['substantive_impact']
    assert impact['version'] == 1
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(impact[key]) >= 40, (source['number'], key)
    if answer['status'] == 'retained_unchanged':
        assert answer['proposed_xml'] is None
        assert answer['classification'] == impact['classification'] == 'retained_necessary'
        assert impact['effects'] == []
    else:
        assert answer['status'] == 'rewrite_draft'
        assert answer['proposed_xml']
        AllowedMarkup().feed(answer['proposed_xml'])
    if source['benefit_check_required']:
        assert len(answer['benefit_review']) >= 100
    if answer.get('change_type') == 'normative_reduction':
        assert answer['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert all(len(item) >= 30 for item in answer['removed_provisions'])
    for item in impact['effects']:
        assert set(item) == effect_keys
        assert item['kind'] in kinds
        assert item['unit'] in units
        assert len(item['source_quote']) >= 12
        assert len(item['proposed_quote']) >= 12
        assert normalized(item['source_quote']) in normalized(plain(source['source_xml'])), (source['number'], 'source_quote')
        assert normalized(item['proposed_quote']) in normalized(plain(answer['proposed_xml'])), (source['number'], 'proposed_quote')
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', item['measure_id'])
        assert 6 <= len(item['measure_id']) <= 96
        assert all(isinstance(item[key], str) and item[key] for key in effect_keys)

print('Articles:', len(answers))
print('Classifications:', dict(Counter(a['substantive_impact']['classification'] for a in answers)))
print('Identifiers copied exactly; required fields, markup, benefit review and text quotations checked.')
print('These checks do not constitute an independent legal review or a cryptographic validation of the imported source.')
