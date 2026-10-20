import json,re,html
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
S=json.loads(Path('source.json').read_text());A=json.loads(Path('answer.json').read_text());R=json.loads(Path('reference-targets.json').read_text())
def text(x):return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]*>',' ',x or ''))).strip()
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
class Check(HTMLParser):
 def handle_starttag(self,t,attrs):
  assert t in allowed,t
  for k,v in attrs:assert k in ['rowspan','colspan'] and v.isdigit(),(k,v)
problems=[]
for i,(s,a) in enumerate(zip(S,A)):
 try:
  for k in ['code_id','source_id','source_sha256','number']:assert s[k]==a[k],k
  assert set(['proposed_xml','reason','review_notes','status','substantive_impact'])<=a.keys()
  if a['status']=='retained_unchanged':
   assert a['proposed_xml'] is None
   assert a['substantive_impact']['classification']=='retained_necessary'
   assert a['substantive_impact']['effects']==[]
  else:
   assert a['status']=='rewrite_draft'
   assert isinstance(a['proposed_xml'],str) and len(a['proposed_xml'])>20
   Check().feed(a['proposed_xml'])
  if s.get('benefit_check_required'):assert len(a.get('benefit_review',''))>=100,'benefit_review'
  if a.get('change_type')=='normative_reduction':
   assert a['reform_policy_id']=='editorial_direction_2026_10_19'
   assert a.get('removed_provisions') and all(len(x)>=30 for x in a['removed_provisions'])
  imp=a['substantive_impact'];assert imp['version']==1
  for k in ['assessment','scope_limitations','new_burdens_review']:assert len(imp[k])>=40,k
  seen=set()
  for e in imp['effects']:
   key=e['measure_id'],e['kind'];assert key not in seen,('duplicate effect',key);seen.add(key)
   assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
   for k in ['source_quote','proposed_quote']:
    assert len(e[k])>=12,k
    hay=text(s['source_xml'] if k=='source_quote' else a['proposed_xml'])
    assert e[k] in hay,(k,e[k])
  req=R['requirements'][s['code_id']+'|'+s['source_id']]
  chk=a['reference_checks'];assert [x['target_key'] for x in chk]==req,'reference targets'
  for x in chk:
   assert x['view_sha256']==R['targets'][x['target_key']]['view_sha256']
   assert len(x['assessment'])>=80
 except Exception as err:problems.append((i,s['number'],str(err)))
print('Problems:',problems)
print('Articles:',len(A),'classifications:',dict(Counter(a['substantive_impact']['classification'] for a in A)))
print('Reference checks:',sum(len(a['reference_checks']) for a in A))
print('Effects:',sum(len(a['substantive_impact']['effects']) for a in A))
for i,a in enumerate(A):print(i,a['number'],a['status'],len(text(a['proposed_xml'])),[(e['measure_id'],e['kind']) for e in a['substantive_impact']['effects']])
assert not problems
