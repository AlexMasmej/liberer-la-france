import hashlib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
issues = []


class Text(HTMLParser):
    def __init__(self, check_markup=False):
        super().__init__(convert_charrefs=True)
        self.fragments = []
        self.check_markup = check_markup
        self.stack = []

    def handle_data(self, data):
        self.fragments.append(data)

    def handle_starttag(self, tag, attrs):
        if not self.check_markup:
            return
        allowed = {'p', 'br', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'th',
                   'td', 'b', 'strong', 'i', 'em', 'u', 'sup', 'sub', 'ul',
                   'ol', 'li', 'div', 'span', 'blockquote'}
        assert tag in allowed, tag
        assert all(k in ('rowspan', 'colspan') and v and v.isdigit()
                   for k, v in attrs), attrs
        if tag != 'br':
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.check_markup:
            assert self.stack.pop() == tag, tag


def plain(xml, check_markup=False):
    parser = Text(check_markup)
    parser.feed(xml)
    parser.close()
    assert not parser.stack
    return ''.join(parser.fragments)


assert len(sources) == len(answers) == 24
assert len({(a['code_id'], a['source_id']) for a in answers}) == 24
effect_fields = {'kind', 'measure_id', 'description', 'before', 'after', 'unit',
                 'affected_population', 'conditions_and_transition',
                 'replacement_or_new_burdens', 'source_quote', 'proposed_quote'}
kinds = {'tax_removed', 'tax_reduced', 'obligation_removed', 'obligation_merged',
         'authorization_removed', 'regime_merged', 'deadline_reduced',
         'compliance_cost_reduced', 'tax_increased', 'obligation_added',
         'deadline_increased', 'complexity_added', 'financing_transfer',
         'payment_deferred', 'relief_extended', 'relief_preserved', 'coordination'}
units = {'percent', 'euro', 'legal_duty', 'regime', 'calendar_days',
         'working_days', 'financing', 'other'}

for source, answer in zip(sources, answers):
    number = source['number']
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[key] == answer[key], (number, key)
    assert {'proposed_xml', 'reason', 'review_notes', 'status',
            'substantive_impact'} <= answer.keys(), number
    req = references['requirements'][source['code_id'] + '|' + source['source_id']]
    checks = answer['reference_checks']
    assert [c['target_key'] for c in checks] == req, number
    for check in checks:
        target = references['targets'][check['target_key']]
        assert check['view_sha256'] == target['view_sha256'], number
        assert len(check['assessment']) >= 80, number
        # Vérification du corps actuel correspondant à l'empreinte fournie.
        view = target['proposed_xml'] if target['view_kind'] == 'proposal' else target['source_xml']
        assert hashlib.sha256(view.encode()).hexdigest() == target['view_sha256']
    if source['benefit_check_required']:
        assert len(answer['benefit_review']) >= 100, number
    impact = answer['substantive_impact']
    assert impact['version'] == 1
    assert impact['classification'] in {
        'material_reduction', 'coordination_only', 'retained_necessary',
        'financing_transfer', 'payment_timing_relief', 'mixed', 'reserved',
        'editorial_only'}
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(impact[key]) >= 40, (number, key)
    if answer['status'] == 'retained_unchanged':
        assert answer['proposed_xml'] is None
        assert answer['classification'] == impact['classification'] == 'retained_necessary'
        assert impact['effects'] == []
        continue
    assert answer['status'] == 'rewrite_draft'
    proposed = plain(answer['proposed_xml'], True)
    official = plain(source['source_xml'])
    for effect in impact['effects']:
        assert effect_fields <= effect.keys(), number
        assert effect['kind'] in kinds and effect['unit'] in units, number
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', effect['measure_id'])
        assert 6 <= len(effect['measure_id']) <= 96
        assert len(effect['source_quote']) >= 12 and effect['source_quote'] in official, number
        assert len(effect['proposed_quote']) >= 12 and effect['proposed_quote'] in proposed, number
    if answer.get('change_type') == 'full_repeal':
        assert proposed.startswith(('Le présent article est abrogé', 'Abrogé'))
        assert answer['repeal_policy_id'] == 'editorial_direction_2026_10_19'
        assert len(answer['repeal_scope']) >= 30
    if answer.get('change_type') == 'normative_reduction':
        assert answer['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert answer['removed_provisions']
        assert all(len(p) >= 30 for p in answer['removed_provisions'])

# Garanties et alinéas maintenus : comparaisons textuelles exactes du corps.
by_number = {a['number']: a for a in answers}
source_by_number = {a['number']: a for a in sources}
for number, count in [('L651-1', 3), ('L651-3', 1), ('L651-5', 1), ('L651-7', 1)]:
    old = plain(source_by_number[number]['source_xml']).strip()
    new = plain(by_number[number]['proposed_xml'])
    if number == 'L651-1':
        sentences = [p.strip() for p in old.split('\n') if p.strip()][:count]
        assert all(p in new for p in sentences), number
    elif number in ('L651-3', 'L651-7'):
        first = next(p.strip() for p in old.split('\n') if p.strip())
        assert first in new, number
    else:
        retained = old.split(" L'intéressé est, en outre,")[0]
        assert retained in new, number

old65110 = re.findall(r'<p>(.*?)</p>', source_by_number['L651-10']['source_xml'], re.S)
new65110 = re.findall(r'<p>(.*?)</p>', by_number['L651-10']['proposed_xml'], re.S)
assert old65110[1:] == new65110[1:4]
assert old65110[0].replace('L. 511-6, L. 521-4 et L. 184-1',
                           'L. 511-22, L. 521-4 et L. 184-4 à L. 184-6') == new65110[0]

report = {
    'article_count': len(answers),
    'reference_check_count': sum(len(a['reference_checks']) for a in answers),
    'status_counts': dict(Counter(a['status'] for a in answers)),
    'impact_counts': dict(Counter(a['substantive_impact']['classification'] for a in answers)),
    'errors': issues,
    'limits': 'Contrôles locaux de structure, empreintes, citations et alinéas maintenus ; aucune validation juridique indépendante.'
}
Path('local-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
