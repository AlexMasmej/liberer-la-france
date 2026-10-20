import json,re,html,collections,hashlib
from pathlib import Path
from xml.etree import ElementTree as ET
s=json.loads(Path('source.json').read_text()); a=json.loads(Path('answer.json').read_text()); r=json.loads(Path('reference-targets.json').read_text())
assert len(a)==len(s)==24
assert len({(x['code_id'],x['source_id']) for x in a})==24
kinds=set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
classes=set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
units=set('percent euro legal_duty regime calendar_days working_days financing other'.split())
tags=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
plain=lambda x:html.unescape(re.sub('<[^>]*>','',x or ''))
for b,c in zip(s,a):
 n=b['number']
 for k in ['code_id','source_id','source_sha256','number']:assert b[k]==c[k],(n,k)
 assert isinstance(c['reason'],str) and len(c['reason'])>80
 assert isinstance(c['review_notes'],str) and len(c['review_notes'])>80
 assert len(c['benefit_review'])>=100
 imp=c['substantive_impact'];assert imp['version']==1 and imp['classification'] in classes
 if imp['classification']=='payment_timing_relief':
  assert imp['effects'] and all(e['kind'] in ['payment_deferred','coordination'] for e in imp['effects']),(n,'calendrier seul')
 for k in ['assessment','scope_limitations','new_burdens_review']:assert len(imp[k])>=40,(n,k)
 if c['status']=='retained_unchanged':
  assert c['proposed_xml'] is None and c['classification']=='retained_necessary' and imp['classification']=='retained_necessary' and imp['effects']==[]
 else:
  assert c['status']=='rewrite_draft' and isinstance(c['proposed_xml'],str) and c['proposed_xml']!=b['source_xml']
  tree=ET.fromstring('<root>'+c['proposed_xml']+'</root>')
  for el in tree.iter():
   if el.tag=='root':continue
   assert el.tag in tags,(n,el.tag)
   for k,v in el.attrib.items():assert k in ['rowspan','colspan'] and re.fullmatch(r'[0-9]+',v),(n,k,v)
  assert 'texte inchangé' not in c['proposed_xml'].lower()
 if c.get('change_type')=='full_repeal':
  assert c['repeal_policy_id']=='editorial_direction_2026_10_19' and len(c['repeal_scope'])>=30
  assert plain(c['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé'))
 if c.get('change_type')=='normative_reduction':
  assert c['reform_policy_id']=='editorial_direction_2026_10_19' and c['removed_provisions']
  assert all(len(x)>=30 for x in c['removed_provisions'])
 required=r['requirements'][b['code_id']+'|'+b['source_id']]
 assert [x['target_key'] for x in c['reference_checks']]==required,n
 for check in c['reference_checks']:
  assert check['view_sha256']==r['targets'][check['target_key']]['view_sha256']
  assert len(check['assessment'])>=80
 pairs=[(e['measure_id'],e['kind']) for e in imp['effects']]
 assert len(pairs)==len(set(pairs)),(n,'Duplicate measure and effect in one article')
 if imp['classification']=='coordination_only':
  assert all(e['kind']=='coordination' for e in imp['effects']),(n,'coordination comptée comme réduction')
 for e in imp['effects']:
  assert set(e)==set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split())
  assert e['kind'] in kinds and e['unit'] in units
  assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
  assert len(e['source_quote'])>=12 and e['source_quote'] in plain(b['source_xml']),(n,'source_quote')
  assert len(e['proposed_quote'])>=12 and e['proposed_quote'] in plain(c['proposed_xml']),(n,'proposed_quote')
  assert '...' not in e['source_quote'] and '…' not in e['source_quote']
  assert '...' not in e['proposed_quote'] and '…' not in e['proposed_quote']
# Contrôle des alinéas intégralement maintenus dans les nouvelles règles partielles.
by_s={x['number']:x for x in s};by_a={x['number']:x for x in a}
for n,indices in {'L432-1':[0],'L432-3':[0],'L432-9':[1,2],'L433-1':[0,1,2,4,5,6,7],'L434-1':[0,1],'L434-8':[1,2,3,4]}.items():
 src=re.findall(r'<p>(.*?)</p>',by_s[n]['source_xml'],re.S)
 prop=re.findall(r'<p>(.*?)</p>',by_a[n]['proposed_xml'],re.S)
 for i in indices:assert src[i]==prop[i],(n,'alinéa',i+1)
assert 'aux 1° et 3°' in by_s['L432-1']['source_xml']
assert 'sans préjudice des autorisations, procédures collectives et protections spéciales dont dépend la rupture' in by_a['L433-1']['proposed_xml']
print(json.dumps({'articles':len(a),'statuts':dict(collections.Counter(x['status'] for x in a)),'impacts':dict(collections.Counter(x['substantive_impact']['classification'] for x in a)),'references':sum(len(x['reference_checks']) for x in a),'effets':sum(len(x['substantive_impact']['effects']) for x in a),'sha256_answer':hashlib.sha256(Path('answer.json').read_bytes()).hexdigest()},ensure_ascii=False))
