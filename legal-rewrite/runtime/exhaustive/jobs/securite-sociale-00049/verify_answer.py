import json
import re
import html
from pathlib import Path
from collections import Counter
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
s = json.loads((root/'source.json').read_text())
a = json.loads((root/'answer.json').read_text())
r = json.loads((root/'reference-targets.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
def plain(x):
    return html.unescape(re.sub('<[^>]*>', '', x or ''))

assert len(a) == len(s) == 24
assert len({x['source_id'] for x in a}) == 24
for src,out in zip(s,a):
    n = src['number']
    assert all(out[k] == src[k] for k in ['code_id','source_id','source_sha256','number']), n
    assert out['reason'] and out['review_notes'], n
    retained = out['status'] == 'retained_unchanged'
    assert out['status'] in ['retained_unchanged','rewrite_draft'], n
    assert (out['proposed_xml'] is None) == retained, n
    if retained:
        assert out['classification'] == 'retained_necessary', n
        assert out['substantive_impact']['effects'] == [], n
    else:
        t = ET.fromstring('<root>'+out['proposed_xml']+'</root>')
        for el in t.iter():
            if el.tag == 'root': continue
            assert el.tag in allowed, (n,el.tag)
            assert all(k in ['rowspan','colspan'] and str(v).isdigit() for k,v in el.attrib.items()), n
    if src['benefit_check_required']:
        assert len(out['benefit_review']) >= 100, n
    if out.get('change_type') == 'full_repeal':
        assert out['repeal_policy_id'] == 'editorial_direction_2026_10_19', n
        assert len(out['repeal_scope']) >= 30, n
        assert plain(out['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé')), n
    if out.get('change_type') == 'normative_reduction':
        assert out['reform_policy_id'] == 'editorial_direction_2026_10_19', n
        assert out['removed_provisions'] and all(len(x)>=30 for x in out['removed_provisions']), n
    im = out['substantive_impact']
    assert im['version'] == 1, n
    for k in ['assessment','scope_limitations','new_burdens_review']:
        assert len(im[k]) >= 40, (n,k)
    for e in im['effects']:
        assert set(e) == set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split()), n
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id']) and 6<=len(e['measure_id'])<=96, n
        assert len(e['source_quote'])>=12 and e['source_quote'] in plain(src['source_xml']), (n,'source_quote',e['source_quote'])
        assert len(e['proposed_quote'])>=12 and e['proposed_quote'] in plain(out['proposed_xml']), (n,'proposed_quote',e['proposed_quote'])
    key = src['code_id']+'|'+src['source_id']
    assert [x['target_key'] for x in out['reference_checks']] == r['requirements'][key], n
    for c in out['reference_checks']:
        assert c['view_sha256'] == r['targets'][c['target_key']]['view_sha256'], n
        assert len(c['assessment']) >= 80, n

print('Validation structurelle : 24 identités exactes ; JSON et XML valides ; citations exactes ; avantages signalés analysés ; cibles et empreintes exactes.')
print('Statuts :',dict(Counter(x['status'] for x in a)))
print('Impacts :',dict(Counter(x['substantive_impact']['classification'] for x in a)))
print('Contrôles de renvois :',sum(len(x['reference_checks']) for x in a))
print('Cette vérification automatique ne constitue pas une validation juridique.')
