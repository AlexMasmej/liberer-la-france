"""Contrôles de structure et de fidélité textuelle, sans validation juridique."""

import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ALLOWED = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
KINDS = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
CLASSES = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
UNITS = set('percent euro legal_duty regime calendar_days working_days financing other'.split())


class XMLText(HTMLParser):
    def __init__(self, check_tags=False):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.check_tags = check_tags
        self.stack = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if not self.check_tags:
            return
        assert tag in ALLOWED, tag
        for key, value in attrs:
            assert key in {'rowspan', 'colspan'} and re.fullmatch(r'[0-9]+', value or ''), (tag, attrs)
        if tag != 'br':
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag != 'br':
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if self.check_tags and tag != 'br':
            assert self.stack and self.stack.pop() == tag, tag


def plain(xml, check_tags=False):
    parser = XMLText(check_tags)
    parser.feed(xml)
    parser.close()
    assert not parser.stack, parser.stack
    return ''.join(parser.parts)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, ('duplicate JSON key', key)
        result[key] = value
    return result


sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text(), object_pairs_hook=unique_object)
refs = json.loads(Path('reference-targets.json').read_text())
assert len(sources) == len(answers) == 23
assert len({(a['code_id'], a['source_id']) for a in answers}) == 23

for source, answer in zip(sources, answers):
    number = source['number']
    for key in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert source[key] == answer[key], (number, key)
    for key in ['reason', 'review_notes']:
        assert isinstance(answer[key], str) and len(answer[key]) >= 40, (number, key)
    impact = answer['substantive_impact']
    assert impact['version'] == 1 and impact['classification'] in CLASSES, number
    for key in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert isinstance(impact[key], str) and len(impact[key]) >= 40, (number, key)
    assert isinstance(impact['effects'], list), number
    xml = answer['proposed_xml']
    if xml is None:
        assert answer['status'] == 'retained_unchanged', number
        assert impact['classification'] in {'retained_necessary', 'reserved'}, number
        assert impact['effects'] == [], number
        assert 'change_type' not in answer, number
    else:
        assert answer['status'] == 'rewrite_draft', number
        assert xml and xml != source['source_xml'], number
        assert impact['classification'] not in {'retained_necessary', 'reserved'}, number
        proposed_text = plain(xml, check_tags=True)
    if source.get('benefit_check_required'):
        assert len(answer.get('benefit_review', '')) >= 100, number
    change = answer.get('change_type')
    if change == 'full_repeal':
        assert proposed_text.startswith(('Le présent article est abrogé', 'Abrogé')), number
        assert answer['repeal_policy_id'] == 'editorial_direction_2026_10_19', number
        assert len(answer['repeal_scope']) >= 30, number
    elif change == 'normative_reduction':
        assert answer['reform_policy_id'] == 'editorial_direction_2026_10_19', number
        assert answer['removed_provisions'] and all(len(item) >= 30 for item in answer['removed_provisions']), number
    else:
        assert change is None, number
    key = source['code_id'] + '|' + source['source_id']
    required = refs['requirements'][key]
    checks = answer.get('reference_checks', [])
    assert [check['target_key'] for check in checks] == required, number
    for check in checks:
        assert check['view_sha256'] == refs['targets'][check['target_key']]['view_sha256'], number
        assert len(check['assessment']) >= 80, number
    for effect in impact['effects']:
        assert effect['kind'] in KINDS and effect['unit'] in UNITS, number
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', effect['measure_id']), number
        assert 6 <= len(effect['measure_id']) <= 96, number
        for field in ['description', 'before', 'after', 'affected_population', 'conditions_and_transition', 'replacement_or_new_burdens']:
            assert isinstance(effect[field], str) and effect[field].strip(), (number, field)
        for quote, text in [('source_quote', plain(source['source_xml'])), ('proposed_quote', proposed_text)]:
            assert len(effect[quote]) >= 12 and effect[quote] in text, (number, quote, effect[quote])
            assert '...' not in effect[quote] and '…' not in effect[quote], (number, quote)
    if impact['classification'] == 'payment_timing_relief':
        assert impact['effects'] and all(effect['kind'] in {'payment_deferred', 'coordination'} for effect in impact['effects']), number
    if impact['classification'] == 'coordination_only':
        assert impact['effects'] and all(effect['kind'] == 'coordination' for effect in impact['effects']), number
    if impact['classification'] == 'financing_transfer':
        assert impact['effects'] and all(effect['kind'] in {'financing_transfer', 'coordination'} for effect in impact['effects']), number
    for effect in impact['effects']:
        if effect['measure_id'] == 'credit-paiement-cession-maintien':
            assert effect['kind'] in {'payment_deferred', 'coordination'}, number

print('23 articles : identifiants, champs, XML, citations exactes, transitions déclarées et cibles requises contrôlés.')
print('Classes :', dict(Counter(answer['substantive_impact']['classification'] for answer in answers)))
print('Le calendrier des crédits et les transferts de financement ne sont comptés comme aucune suppression permanente de taxe.')
