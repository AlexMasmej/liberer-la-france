import json,re,html,collections
from html.parser import HTMLParser
from pathlib import Path
s=json.loads(Path('source.json').read_text());a=json.loads(Path('answer.json').read_text());r=json.loads(Path('reference-targets.json').read_text())
class P(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.text=[];self.tags=[]
 def handle_data(self,x):self.text.append(x)
 def handle_starttag(self,t,attrs):
  assert t in {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'},t
  for k,v in attrs:assert k in {'rowspan','colspan'} and v.isdigit(),(k,v)
 def handle_endtag(self,t):pass
 def get(self):return ''.join(self.text)
def plain(x):
 p=P();p.feed(x);return p.get()
assert len(a)==len(s)==24
assert len({x['source_id'] for x in a})==24
for z,w in zip(s,a):
 for k in ['code_id','source_id','source_sha256','number']:assert w[k]==z[k],(z['number'],k)
 assert w['status'] in {'rewrite_draft','retained_unchanged'}
 for k in ['reason','review_notes']: assert len(w[k])>80
 si=w['substantive_impact']; assert si['version']==1
 assert si['classification'] in {'material_reduction','coordination_only','retained_necessary','financing_transfer','payment_timing_relief','mixed','reserved','editorial_only'}
 for k in ['assessment','scope_limitations','new_burdens_review']:assert len(si[k])>=40
 if w['status']=='retained_unchanged':
  assert w['proposed_xml'] is None
  assert si['classification']=='retained_necessary' and w['classification']=='retained_necessary' and si['effects']==[]
 else:
  assert w['proposed_xml'] and w['proposed_xml']!=z['source_xml']
  target=plain(w['proposed_xml'])
 if z['benefit_check_required']:assert len(w.get('benefit_review',''))>=100
 if w.get('change_type')=='normative_reduction':
  assert w['reform_policy_id']=='editorial_direction_2026_10_19'
  assert all(len(p)>=30 for p in w['removed_provisions'])
 requirements=r['requirements'][z['code_id']+'|'+z['source_id']]
 assert [p['target_key'] for p in w['reference_checks']]==requirements
 for p in w['reference_checks']:
  assert p['view_sha256']==r['targets'][p['target_key']]['view_sha256']
  assert len(p['assessment'])>=80
 for e in si['effects']:
  assert set(e)=={'kind','measure_id','description','before','after','unit','affected_population','conditions_and_transition','replacement_or_new_burdens','source_quote','proposed_quote'}
  assert e['kind'] in {'tax_removed','tax_reduced','obligation_removed','obligation_merged','authorization_removed','regime_merged','deadline_reduced','compliance_cost_reduced','tax_increased','obligation_added','deadline_increased','complexity_added','financing_transfer','payment_deferred','relief_extended','relief_preserved','coordination'}
  assert re.fullmatch('[a-z0-9-]{6,96}',e['measure_id'])
  assert e['unit'] in {'percent','euro','legal_duty','regime','calendar_days','working_days','financing','other'}
  assert len(e['source_quote'])>=12 and e['source_quote'] in html.unescape(re.sub('<[^>]*>','',z['source_xml'])),(w['number'],'source_quote')
  assert len(e['proposed_quote'])>=12 and e['proposed_quote'] in target,(w['number'],'proposed_quote')
print('Vérification structurelle : OK')
print('Statuts :',dict(collections.Counter(w['status'] for w in a)))
print('Impacts :',dict(collections.Counter(w['substantive_impact']['classification'] for w in a)))
print('Cibles contrôlées :',sum(len(w['reference_checks']) for w in a))
for z,w in zip(s,a):
 if w['proposed_xml']:
  print('\n',w['number'],'source/proposition',len(z['source_xml']),len(w['proposed_xml']))
  zn=collections.Counter(re.findall(r'\d+',html.unescape(re.sub('<[^>]*>','',z['source_xml']))))
  wn=collections.Counter(re.findall(r'\d+',plain(w['proposed_xml'])))
  print('Chiffres retirés :',dict(zn-wn),'ajoutés :',dict(wn-zn))
