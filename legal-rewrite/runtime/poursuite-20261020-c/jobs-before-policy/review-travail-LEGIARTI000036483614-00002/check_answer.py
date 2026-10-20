import json
import re
from html.parser import HTMLParser
from pathlib import Path

class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)
    def handle_starttag(self, tag, attrs):
        if tag in {'p', 'br', 'div', 'li', 'tr', 'td', 'th'}:
            self.parts.append(' ')
    def handle_endtag(self, tag):
        if tag in {'p', 'div', 'li', 'tr', 'td', 'th'}:
            self.parts.append(' ')

def plain(s):
    p = Text()
    p.feed(s)
    return re.sub(r'\s+', ' ', ''.join(p.parts)).strip()

class Markup(HTMLParser):
    allowed = {'p','br','table','thead','tbody','tfoot','tr','th','td','b',
               'strong','i','em','u','sup','sub','ul','ol','li','div',
               'span','blockquote'}
    def handle_starttag(self, tag, attrs):
        assert tag in self.allowed, tag
        assert all(k in {'rowspan','colspan'} and re.fullmatch(r'\d+', v)
                   for k,v in attrs), (tag, attrs)

src = json.loads(Path('source.json').read_text())
ans = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
assert len(src) == len(ans) == 12
assert len({(a['code_id'],a['source_id']) for a in ans}) == 12
kinds = {'tax_removed','tax_reduced','obligation_removed','obligation_merged',
         'authorization_removed','regime_merged','deadline_reduced',
         'compliance_cost_reduced','tax_increased','obligation_added',
         'deadline_increased','complexity_added','financing_transfer',
         'payment_deferred','relief_extended','relief_preserved','coordination'}
for s,a in zip(src,ans):
    for k in ['code_id','source_id','source_sha256','number']:
        assert s[k] == a[k], (k,a['number'])
    for k in ['reason','review_notes']:
        assert isinstance(a[k],str) and len(a[k]) >= 40
    assert a['status'] in {'rewrite_draft','retained_unchanged'}
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['substantive_impact']['classification'] == 'retained_necessary'
        assert a['substantive_impact']['effects'] == []
    else:
        assert isinstance(a['proposed_xml'],str) and a['proposed_xml']
        Markup().feed(a['proposed_xml'])
    if a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert a['removed_provisions']
        assert all(len(x)>=30 for x in a['removed_provisions'])
    if s.get('benefit_check_required'):
        assert len(a['benefit_review'])>=100
    si=a['substantive_impact']
    assert si['version']==1
    for k in ['assessment','scope_limitations','new_burdens_review']:
        assert len(si[k])>=40
    sq=plain(s['source_xml'])
    pq=plain(a['proposed_xml'] or '')
    for e in si['effects']:
        assert e['kind'] in kinds
        assert e['unit'] in {'percent','euro','legal_duty','regime',
                             'calendar_days','working_days','financing','other'}
        assert re.fullmatch(r'[a-z0-9][a-z0-9-]{4,94}[a-z0-9]',e['measure_id'])
        for q, body in [('source_quote',sq),('proposed_quote',pq)]:
            assert len(e[q])>=12
            assert e[q] in body,(a['number'],e['measure_id'],q,e[q])
    key=a['code_id']+'|'+a['source_id']
    assert set(refs['requirements'][key]).issubset({c['target_key'] for c in a['reference_checks']})
    assert len({c['target_key'] for c in a['reference_checks']}) == len(a['reference_checks'])
    for c in a['reference_checks']:
        assert c['view_sha256']==refs['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment'])>=80
    print(a['number'], a['status'], si['classification'],
          'references',len(a['reference_checks']),
          'effects',len(si['effects']), 'chars',len(a['proposed_xml'] or ''))
print('Structure, identifiants, balises, citations et cibles : contrôles locaux réussis.')
