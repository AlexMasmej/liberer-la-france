import json
import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


class MarkupCheck(HTMLParser):
    allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
    def handle_starttag(self, tag, attrs):
        assert tag in self.allowed, tag
        assert all(k in ('rowspan', 'colspan') and v.isdigit() for k, v in attrs), attrs


src = json.loads(Path('source.json').read_text())
out = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
assert len(out) == len(src) == 24
assert len({a['source_id'] for a in out}) == 24
for s, a in zip(src, out):
    assert all(a[k] == s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
    assert a['reason'] and a['review_notes']
    imp = a['substantive_impact']
    assert imp['version'] == 1
    assert all(len(imp[k]) >= 40 for k in ('assessment', 'scope_limitations', 'new_burdens_review'))
    key = a['code_id'] + '|' + a['source_id']
    expected = refs['requirements'][key]
    assert [c['target_key'] for c in a['reference_checks']] == expected
    for c in a['reference_checks']:
        assert c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment']) >= 80
    if s.get('benefit_check_required'):
        assert len(a['benefit_review']) >= 100
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == imp['classification'] == 'retained_necessary'
        assert not imp['effects']
    else:
        assert a['status'] == 'rewrite_draft'
        assert a['proposed_xml'] and a['proposed_xml'] != s['source_xml']
        MarkupCheck().feed(a['proposed_xml'])
        for e in imp['effects']:
            assert set(e) == set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(s['source_xml']), (a['number'], 'source', e['source_quote'])
            assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed', e['proposed_quote'])
        if a.get('change_type') == 'normative_reduction':
            assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
            assert a['removed_provisions'] and all(len(p) >= 30 for p in a['removed_provisions'])
    print(a['number'], a['status'], imp['classification'], len(imp['effects']))
print('Statuts :', dict(Counter(a['status'] for a in out)))
print('Impacts :', dict(Counter(a['substantive_impact']['classification'] for a in out)))
print('Citations exactes :', sum(len(a['substantive_impact']['effects']) for a in out) * 2)
print('Contrôles de cibles requis :', sum(len(a['reference_checks']) for a in out))
