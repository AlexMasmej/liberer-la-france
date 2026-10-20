import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
allowed_classes = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
allowed_effects = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
allowed_units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
required_effect = set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
plain = lambda x: html.unescape(re.sub('<[^>]*>', '', x or ''))
assert len(sources) == len(answers) == 12
for s, a in zip(sources, answers):
    n = s['number']
    for k in ['code_id','source_id','source_sha256','number']:
        assert a[k] == s[k], (n,k)
    assert a['status'] in ['rewrite_draft','retained_unchanged'], n
    impact = a['substantive_impact']
    assert impact['version'] == 1 and impact['classification'] in allowed_classes
    for k in ['assessment','scope_limitations','new_burdens_review']:
        assert len(impact[k]) >= 40, (n,k)
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert impact['classification'] == 'retained_necessary' and impact['effects'] == []
    else:
        root = ET.fromstring('<root>' + a['proposed_xml'] + '</root>')
        for e in root.iter():
            assert e.tag == 'root' or e.tag in allowed_tags, (n,e.tag)
            for k,v in e.attrib.items():
                assert k in ['rowspan','colspan'] and v.isdigit(), (n,k,v)
    if a.get('change_type') == 'full_repeal':
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé'))
        assert a['repeal_policy_id'] == 'editorial_direction_2026_10_19'
        assert len(a['repeal_scope']) >= 30
    if a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert a['removed_provisions'] and all(len(x) >= 30 for x in a['removed_provisions'])
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review','')) >= 100
    for e in impact['effects']:
        assert set(e) == required_effect, (n,set(e))
        assert e['kind'] in allowed_effects and e['unit'] in allowed_units
        assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(s['source_xml']), (n,'source_quote',e['source_quote'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml']), (n,'proposed_quote',e['proposed_quote'])
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6 <= len(e['measure_id']) <= 96
    key = s['code_id'] + '|' + s['source_id']
    assert [c['target_key'] for c in a['reference_checks']] == refs['requirements'][key]
    for c in a['reference_checks']:
        assert c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment']) >= 80
    print(n, a['status'], a.get('change_type','maintien'), impact['classification'], len(impact['effects']))
print('Structure, citations exactes, balises et 60 empreintes : OK. Ce contrôle technique ne valide pas le fond juridique.')
