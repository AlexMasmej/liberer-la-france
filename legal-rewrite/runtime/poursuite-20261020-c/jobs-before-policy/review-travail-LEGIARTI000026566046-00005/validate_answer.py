import json, re, hashlib, html
from pathlib import Path
from html.parser import HTMLParser
s=json.loads(Path('source.json').read_text()); a=json.loads(Path('answer.json').read_text()); r=json.loads(Path('reference-targets.json').read_text())
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
classes=set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
kinds=set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
units=set('percent euro legal_duty regime calendar_days working_days financing other'.split())
class XML(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.parts=[]
 def handle_starttag(self,t,attrs):
  assert t in allowed,t
  assert all(k in ['rowspan','colspan'] and re.fullmatch(r'[0-9]+',v) for k,v in attrs),attrs
  if t!='br':self.stack.append(t)
 def handle_endtag(self,t):
  if t=='br':return
  assert self.stack and self.stack.pop()==t,t
 def handle_startendtag(self,t,attrs):
  self.handle_starttag(t,attrs)
  if t!='br':self.handle_endtag(t)
 def handle_data(self,d):self.parts.append(d)
def text(x):
 p=XML();p.feed(x);assert not p.stack;return ''.join(p.parts)
assert len(a)==len(s)==12
assert len({(v['code_id'],v['source_id']) for v in a})==12
for source,answer in zip(s,a):
 n=source['number'];key=source['code_id']+'|'+source['source_id']
 for k in ['code_id','source_id','source_sha256','number']:assert source[k]==answer[k],(n,k)
 for k in ['proposed_xml','reason','review_notes','status','substantive_impact','reference_checks']:assert k in answer,(n,k)
 assert isinstance(answer['reason'],str) and len(answer['reason'])>=40
 assert isinstance(answer['review_notes'],str) and len(answer['review_notes'])>=40
 ref=r['referrers'][key]
 assert hashlib.sha256(source['source_xml'].encode()).hexdigest()==ref['source_xml_sha256'],n
 assert hashlib.sha256(source['source_notes_xml'].encode()).hexdigest()==ref['source_notes_sha256'],n
 im=answer['substantive_impact'];assert im['version']==1 and im['classification'] in classes
 for k in ['assessment','scope_limitations','new_burdens_review']:assert len(im[k])>=40,(n,k)
 if answer['status']=='retained_unchanged':
  assert answer['proposed_xml'] is None and im['classification']=='retained_necessary' and im['effects']==[]
  pt=''
 else:
  assert answer['status']=='rewrite_draft'
  pt=text(answer['proposed_xml']);assert pt.strip()
 if source.get('benefit_check_required'):assert len(answer['benefit_review'])>=100,n
 if answer.get('change_type')=='full_repeal':
  assert pt.startswith(('Le présent article est abrogé','Abrogé'))
  assert answer['repeal_policy_id']=='editorial_direction_2026_10_19' and len(answer['repeal_scope'])>=30
 if answer.get('change_type')=='normative_reduction':
  assert answer['reform_policy_id']=='editorial_direction_2026_10_19'
  assert answer['removed_provisions'] and all(len(v)>=30 for v in answer['removed_provisions'])
 st=text(source['source_xml'])
 for e in im['effects']:
  assert set(e)==set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split()),n
  assert e['kind'] in kinds and e['unit'] in units
  assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
  assert len(e['source_quote'])>=12 and e['source_quote'] in st,(n,e['source_quote'])
  assert len(e['proposed_quote'])>=12 and e['proposed_quote'] in pt,(n,e['proposed_quote'])
  assert '...' not in e['source_quote'] and '…' not in e['source_quote']
  assert '...' not in e['proposed_quote'] and '…' not in e['proposed_quote']
 actual={v['target_key']:v for v in answer['reference_checks']}
 assert len(actual)==len(answer['reference_checks'])
 assert set(actual)==set(r['requirements'][key]),n
 for tk,c in actual.items():
  assert c['view_sha256']==r['targets'][tk]['view_sha256'] and len(c['assessment'])>=80,(n,tk)
 if source['number']=='D5134-41':assert '45 %' in st and '88 %' in st
 if source['number']=='D5213-63-1':assert pt.count('75 %')==2
 if source['number']=='R5213-76':
  assert '0 % à 10 %' in pt and 'Mayotte' in pt and 'revalorisés' in pt
  assert all(m in pt for m in ['I. –','II. –','III. –','IV. –','1°','2°'])
 print(n,answer['status'],im['classification'],len(answer['reference_checks']),'cibles',len(im['effects']),'effets')
print('Validation structurelle réussie : 12 objets, identifiants et sources cohérents, 51 contrôles de renvoi, XML et citations exactes. Ne vaut pas validation juridique.')
print('Contrôles de renvoi effectifs :',sum(len(v['reference_checks']) for v in a))
