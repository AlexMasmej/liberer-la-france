import json,re,html
from html.parser import HTMLParser
from pathlib import Path

src=json.loads(Path('source.json').read_text())
ans=json.loads(Path('answer.json').read_text())
refs=json.loads(Path('reference-targets.json').read_text())
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
kinds=set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
classes=set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
units=set('percent euro legal_duty regime calendar_days working_days financing other'.split())

def plain(x): return html.unescape(re.sub(r'<[^>]*>','',x or ''))

class CheckHTML(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True);self.stack=[]
    def handle_starttag(self,t,attrs):
        assert t in allowed,t
        assert all(k in ('rowspan','colspan') and v.isdecimal() for k,v in attrs),(t,attrs)
        if t!='br': self.stack.append(t)
    def handle_startendtag(self,t,attrs):
        self.handle_starttag(t,attrs)
        if t!='br': self.handle_endtag(t)
    def handle_endtag(self,t):
        assert self.stack and self.stack[-1]==t,(t,self.stack)
        self.stack.pop()

errors=[]
assert len(src)==len(ans)==20
for i,(s,a) in enumerate(zip(src,ans)):
    try:
        for k in ('code_id','source_id','source_sha256','number'): assert a[k]==s[k],k
        assert a['status'] in ('rewrite_draft','retained_unchanged')
        if a['status']=='rewrite_draft':
            assert a['proposed_xml'] and len(a['proposed_xml'])>100
            parser=CheckHTML();parser.feed(a['proposed_xml']);assert not parser.stack
        else: assert a['proposed_xml'] is None
        si=a['substantive_impact']; assert si['version']==1 and si['classification'] in classes
        for k in ('assessment','scope_limitations','new_burdens_review'): assert len(si[k])>=40,k
        for e in si['effects']:
            assert e['kind'] in kinds and e['unit'] in units
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
            for k in ('description','before','after','affected_population','conditions_and_transition','replacement_or_new_burdens'): assert e[k],k
            for field,body in [('source_quote',plain(s['source_xml'])),('proposed_quote',plain(a['proposed_xml']))]:
                assert len(e[field])>=12,(field,e[field])
                assert e[field] in body,(field,e[field])
        if s['benefit_check_required']: assert len(a['benefit_review'])>=100
        if a.get('change_type')=='normative_reduction':
            assert a['reform_policy_id']=='editorial_direction_2026_10_19'
            assert a['removed_provisions'] and all(len(x)>=30 for x in a['removed_provisions'])
        key=s['code_id']+'|'+s['source_id']
        checks=a.get('reference_checks',[])
        assert [x['target_key'] for x in checks]==refs['requirements'][key]
        for x in checks:
            assert x['view_sha256']==refs['targets'][x['target_key']]['view_sha256']
            assert len(x['assessment'])>=80
        assert not re.search(r'\.\.\.|…|texte inchangé|TODO|TBD',a['proposed_xml'],re.I)
        print(i,a['number'],len(s['source_xml']),len(a['proposed_xml']),si['classification'],len(si['effects']),'effects')
    except Exception as e: errors.append((i,s['number'],str(e)))
print('ERRORS',json.dumps(errors,ensure_ascii=False))
if errors: raise SystemExit(1)
print('Validation structure, citations exactes et empreintes : OK')
