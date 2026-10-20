import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter

s = json.loads(Path('source.json').read_text())
a = json.loads(Path('answer.json').read_text())
r = json.loads(Path('reference-targets.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())

class CheckHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed, tag
        for key, value in attrs:
            assert key in ('rowspan','colspan') and value.isdigit(), (key,value)
    handle_startendtag = handle_starttag

def text(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))

assert len(a) == len(s) == 24
assert len({x['source_id'] for x in a}) == 24
for src, ans in zip(s,a):
    for field in ('code_id','source_id','source_sha256','number'):
        assert ans[field] == src[field], (src['number'],field)
    for field in ('reason','review_notes','status','proposed_xml','substantive_impact','reference_checks'):
        assert field in ans, (src['number'],field)
    key=src['code_id']+'|'+src['source_id']
    required=r['requirements'][key]
    assert [x['target_key'] for x in ans['reference_checks']] == required, src['number']
    for check in ans['reference_checks']:
        assert check['view_sha256'] == r['targets'][check['target_key']]['view_sha256']
        assert len(check['assessment']) >= 80
        assert r['targets'][check['target_key']]['number'] in check['assessment']
    if src['benefit_check_required']:
        assert len(ans['benefit_review']) >= 100
    imp=ans['substantive_impact']
    assert imp['version'] == 1
    assert imp['classification'] in ('material_reduction','coordination_only','retained_necessary','financing_transfer','payment_timing_relief','mixed','reserved','editorial_only')
    for field in ('assessment','scope_limitations','new_burdens_review'):
        assert len(imp[field]) >= 40
    if ans['status'] == 'retained_unchanged':
        assert ans['proposed_xml'] is None
        assert ans['classification'] == imp['classification'] == 'retained_necessary'
        assert imp['effects'] == []
    else:
        assert ans['status'] == 'rewrite_draft'
        assert isinstance(ans['proposed_xml'],str) and len(ans['proposed_xml']) > 30
        CheckHTML().feed(ans['proposed_xml'])
    if ans.get('change_type') == 'normative_reduction':
        assert ans['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert ans['removed_provisions']
        assert all(len(x)>=30 for x in ans['removed_provisions'])
    for effect in imp['effects']:
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', effect['measure_id'])
        assert 6 <= len(effect['measure_id']) <= 96
        assert effect['unit'] in ('percent','euro','legal_duty','regime','calendar_days','working_days','financing','other')
        for field in ('kind','measure_id','description','before','after','unit','affected_population','conditions_and_transition','replacement_or_new_burdens','source_quote','proposed_quote'):
            assert isinstance(effect[field],str) and effect[field]
        assert len(effect['source_quote'])>=12 and effect['source_quote'] in text(src['source_xml']), (src['number'],'source_quote')
        assert len(effect['proposed_quote'])>=12 and effect['proposed_quote'] in text(ans['proposed_xml']), (src['number'],'proposed_quote')

print(json.dumps(dict(articles=len(a),reference_checks=sum(len(x['reference_checks']) for x in a),
                     status=dict(Counter(x['status'] for x in a)),
                     impact=dict(Counter(x['substantive_impact']['classification'] for x in a))), ensure_ascii=False))
