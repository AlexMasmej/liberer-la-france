import json,re,html
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter

S=json.loads(Path('source.json').read_text());A=json.loads(Path('answer.json').read_text());R=json.loads(Path('reference-targets.json').read_text())
class Markup(HTMLParser):
    def __init__(self): super().__init__();self.errors=[];self.stack=[];self.tags=Counter()
    def handle_starttag(self,tag,attrs):
        self.tags[tag]+=1
        if tag not in {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}:self.errors.append('tag '+tag)
        for k,v in attrs:
            if k not in {'rowspan','colspan'} or not v.isdigit():self.errors.append('attr '+k)
        if tag!='br':self.stack.append(tag)
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag!='br':self.handle_endtag(tag)
    def handle_endtag(self,tag):
        if not self.stack or self.stack[-1]!=tag:self.errors.append('unbalanced '+tag)
        else:self.stack.pop()

def plain(x):
    return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]*>',' ',x or ''))).strip()
def raw_plain(x):
    return html.unescape(re.sub('<[^>]*>','',x or ''))
issues=[]
assert len(A)==len(S)==24
assert len({(a['code_id'],a['source_id']) for a in A})==24
for s,a in zip(S,A):
    n=s['number']
    for k in ['code_id','source_id','source_sha256','number']:
        if s[k]!=a[k]:issues.append((n,k))
    for k in ['proposed_xml','reason','review_notes','status','substantive_impact','reference_checks']:
        if k not in a:issues.append((n,'missing '+k))
    p=a['proposed_xml']
    if a['status']=='retained_unchanged':
        if p is not None or a.get('classification')!='retained_necessary' or a['substantive_impact']['effects']:issues.append((n,'retained'))
    else:
        if a['status']!='rewrite_draft' or not isinstance(p,str) or not p:issues.append((n,'rewrite'))
        parser=Markup();parser.feed(p);parser.close()
        if parser.errors or parser.stack:issues.append((n,'markup',parser.errors,parser.stack))
    if s.get('benefit_check_required') and len(a.get('benefit_review',''))<100:issues.append((n,'benefit'))
    si=a['substantive_impact']
    if si['version']!=1 or si['classification'] not in {'material_reduction','coordination_only','retained_necessary','financing_transfer','payment_timing_relief','mixed','reserved','editorial_only'}:issues.append((n,'impact'))
    for k in ['assessment','scope_limitations','new_burdens_review']:
        if len(si[k])<40:issues.append((n,'short '+k))
    if a.get('change_type')=='normative_reduction':
        assert a['reform_policy_id']=='editorial_direction_2026_10_19'
        assert a['removed_provisions'] and all(len(x)>=30 for x in a['removed_provisions'])
    if a.get('change_type')=='full_repeal':
        assert a['repeal_policy_id']=='editorial_direction_2026_10_19'
        assert len(a['repeal_scope'])>=30 and plain(p).startswith(('Le présent article est abrogé','Abrogé'))
    key=s['code_id']+'|'+s['source_id']
    if [c['target_key'] for c in a['reference_checks']]!=R['requirements'][key]:issues.append((n,'target set'))
    for c in a['reference_checks']:
        if c['view_sha256']!=R['targets'][c['target_key']]['view_sha256'] or len(c['assessment'])<80:issues.append((n,'target hash/analysis'))
    effect_keys=[(e['measure_id'],e['kind']) for e in si['effects']]
    if len(effect_keys)!=len(set(effect_keys)):issues.append((n,'duplicate measure and effect'))
    for e in si['effects']:
        for k in ['kind','measure_id','description','before','after','unit','affected_population','conditions_and_transition','replacement_or_new_burdens','source_quote','proposed_quote']:
            if not isinstance(e.get(k),str) or not e[k]:issues.append((n,'effect '+k))
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) or not 6<=len(e['measure_id'])<=96:issues.append((n,'measure_id'))
        for k,body in [('source_quote',s['source_xml']),('proposed_quote',p)]:
            if len(e[k])<12 or '<' in e[k] or e[k] not in raw_plain(body):issues.append((n,'quote '+k))
print('ISSUES',issues)
print('STATUSES',dict(Counter(a['status'] for a in A)))
print('IMPACTS',dict(Counter(a['substantive_impact']['classification'] for a in A)))
print('REF_CHECKS',sum(len(a['reference_checks']) for a in A))
print('EFFECTS',sum(len(a['substantive_impact']['effects']) for a in A))
print('SOURCES',sum(len(a['source_xml']) for a in S),'characters ; PROPOSED',sum(len(a['proposed_xml'] or '') for a in A),'characters')
assert not issues
