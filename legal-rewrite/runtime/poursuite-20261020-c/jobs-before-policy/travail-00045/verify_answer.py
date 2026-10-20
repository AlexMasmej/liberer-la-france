import collections
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

s=json.loads(Path('source.json').read_text())
a=json.loads(Path('answer.json').read_text())
targets=json.loads(Path('reference-targets.json').read_text())
allowed=set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
classes=set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
kinds=set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
units=set('percent euro legal_duty regime calendar_days working_days financing other'.split())
required={'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status','substantive_impact'}
plain=lambda x:html.unescape(re.sub(r'<[^>]*>','',x or ''))
refs=lambda x:set(re.findall(r'\b[LRDA]\.\s*\d[\d-]*(?:\s+[IVX]+)?',plain(x)))
labels=lambda x:re.findall(r'<p(?:\s[^>]*)?>\s*(\d+°(?:\s*bis)?|[a-z]\))',x or '')
assert len(s)==len(a)==24
assert len({(x['code_id'],x['source_id']) for x in a})==24
checks=[]
for src,row in zip(s,a):
 n=src['number'];assert required<=row.keys(),n
 assert all(row[k]==src[k] for k in ['code_id','source_id','source_sha256','number']),n
 source_key=src['code_id']+'|'+src['source_id']
 expected_targets=targets['requirements'][source_key]
 reference_checks=row['reference_checks']
 assert [c['target_key'] for c in reference_checks]==expected_targets,(n,'reference targets')
 assert len({c['target_key'] for c in reference_checks})==len(reference_checks),(n,'duplicate target')
 for check in reference_checks:
  target=targets['targets'][check['target_key']]
  assert set(check)=={'target_key','view_sha256','assessment'},n
  assert check['view_sha256']==target['view_sha256'],(n,'stale target view')
  assert len(check['assessment'])>=80,(n,'reference assessment')
  assert hashlib.sha256(target['proposed_xml'].encode()).hexdigest()==target['view_sha256'],(n,'target hash')
  assert hashlib.sha256(target['source_xml'].encode()).hexdigest()==target['source_xml_sha256'],(n,'target source hash')
  assert hashlib.sha256(target['source_notes_xml'].encode()).hexdigest()==target['source_notes_sha256'],(n,'target notes hash')
 assert len(row['reason'])>=40 and len(row['review_notes'])>=40,n
 imp=row['substantive_impact'];assert imp['version']==1 and imp['classification'] in classes,n
 for field in ['assessment','scope_limitations','new_burdens_review']:assert isinstance(imp[field],str) and len(imp[field])>=40,(n,field)
 if src.get('benefit_check_required'):assert len(row['benefit_review'])>=100,n
 assert len(row['benefit_review'])>=100,n
 if row['status']=='retained_unchanged':
  assert row['proposed_xml'] is None and imp['classification']=='retained_necessary' and imp['effects']==[],n
  assert 'change_type' not in row,n
 else:
  assert row['status']=='rewrite_draft' and isinstance(row['proposed_xml'],str),n
  root=ET.fromstring('<root>'+row['proposed_xml']+'</root>')
  for el in root.iter():
   if el.tag=='root':continue
   assert el.tag in allowed,(n,el.tag)
   for k,v in el.attrib.items():assert k in ['rowspan','colspan'] and re.fullmatch('[0-9]+',v),(n,k)
  assert labels(src['source_xml'])==labels(row['proposed_xml']),(n,'subdivisions',labels(src['source_xml']),labels(row['proposed_xml']))
  if row.get('change_type')=='normative_reduction':
   assert row['reform_policy_id']=='editorial_direction_2026_10_19'
   assert row['removed_provisions'] and all(len(x)>=30 for x in row['removed_provisions']),n
  assert not re.search(r'texte inchangé|\.\.\.|à compléter',row['proposed_xml'],re.I),n
 for e in imp['effects']:
  assert set(e)==set('kind measure_id description before after unit affected_population conditions_and_transition replacement_or_new_burdens source_quote proposed_quote'.split()),n
  assert e['kind'] in kinds and e['unit'] in units,n
  assert re.fullmatch('[a-z][a-z0-9-]{5,95}',e['measure_id']),(n,e['measure_id'])
  assert len(e['source_quote'])>=12 and e['source_quote'] in plain(src['source_xml']),(n,'source_quote')
  assert len(e['proposed_quote'])>=12 and e['proposed_quote'] in plain(row['proposed_xml']),(n,'proposed_quote')
  assert '...' not in e['source_quote'] and '...' not in e['proposed_quote'],n
 # Every original explicit reference is retained, or accounted for in the manual review.
 original_refs=refs(src['source_xml']); proposed_refs=refs(row['proposed_xml']) if row['proposed_xml'] else original_refs
 missing=original_refs-proposed_refs
 assert not missing,(n,'missing reference',missing)
 checks.append({'number':n,'status':row['status'],'classification':imp['classification'],'effect_count':len(imp['effects'])})
report={'article_count':len(a),'status_counts':dict(collections.Counter(x['status'] for x in a)), 'classification_counts':dict(collections.Counter(x['substantive_impact']['classification'] for x in a)), 'structural_checks':'passed', 'exact_quote_checks':'passed', 'reference_checks':{'status':'passed','count':sum(len(x['reference_checks']) for x in a),'requirements_exact':True,'current_view_hashes':True}, 'source_references_and_subdivision_labels':'preserved', 'review_limit':'Contrôles internes de structure et de concordance ; aucune validation juridique indépendante ni réduction nationale nette démontrée.', 'answer_sha256':hashlib.sha256(Path('answer.json').read_bytes()).hexdigest(), 'articles':checks}
Path('verification_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='articles'},ensure_ascii=False,indent=2))
