from pathlib import Path
import json,sqlite3,hashlib,sys,copy,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes;from run_exhaustive import validate_answer;import reference_coherence as ref
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or '').encode()).hexdigest()
s=json.loads((P/'source.json').read_text())+json.loads((P/'companion-source.json').read_text());a=json.loads((P/'answer.json').read_text())+json.loads((P/'companion-answer.json').read_text());ctx=json.loads((P/'references.json').read_text())+json.loads((P/'automatic-extra-references.json').read_text())+[json.loads((P/'election-reference.json').read_text())];snap=json.loads((P/'reference-targets.json').read_text())
input_freezes={}
for sub in ['coherence002','transition001','metadata-crpa001']:
 Q=P/sub; ss=json.loads((Q/'source.json').read_text());aa=json.loads((Q/'answer.json').read_text());replacements={ref.key(x):(x,y)for x,y in zip(ss,aa)}
 for j,x in enumerate(s):
  if ref.key(x)in replacements:s[j],a[j]=replacements[ref.key(x)]
 m=json.loads((Q/'manifest.json').read_text());input_freezes[sub]={n:sha((Q/n).read_bytes())==v for n,v in m['files_sha256'].items()}
ctx+=json.loads((P/'coherence002/cch-references.json').read_text())
(P/'reviewed-effective-source.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');(P/'reviewed-effective-answer.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
check=copy.deepcopy(a);validate_answer(check,s);schema_unchanged=check==a
# One coherent read transaction. Duplicate candidate/context records compared only once.
allrows={ref.key(x):x for x in ctx+s};db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');checks=[]
for k,x in allrows.items():
 c,i=x['code_id'],x['source_id'];r=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',(c,i)).fetchone();d=db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone();prior=dict(d)if d else None
 if prior and 'proposed_sha256'in(x.get('previous_draft')or{}):prior['proposed_sha256']=sha(prior['proposed_xml'])
 expected_prior=x.get('previous_draft');tests=dict(source_sha256=r['source_sha256']==x['source_sha256'],source_body=sha(r['content_xml'])==sha(x['source_xml']),source_notes=sha(source_notes(db,c,i))==sha(x.get('source_notes_xml')))
 if 'previous_draft'in x:tests['entire_beforeimage']=prior==expected_prior
 else:tests['proposed_body']=sha(d['proposed_xml']if d else None)==sha(x.get('proposed_xml'))
 raw=db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",(c,i)).fetchone();tests['raw_document']=sha(raw['xml'])==raw['sha256']==x['source_sha256']
 checks.append(dict(number=x['number'],code_id=c,source_id=i,checks=tests))
try:ref.check_guards(db,snap);reference_guards=True
except Exception as e:reference_guards=False;reference_error=str(e)
certs=[dict(number=x['number'],needed=bool(snap['requirements'][ref.key(x)]),current_before_commit=ref.certificate_current(db,x,y['proposed_xml'],y.get('reference_coherence')))for x,y in zip(s,a)]
db.rollback();db.close();pol={n:sha((L/n).read_bytes())==sha((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']}
original=P.parents[1]/'logement/edition001';freeze={f:sha((P/f).read_bytes())==sha((original/f).read_bytes())for f in ['source.json','answer.json','companion-source.json','companion-answer.json','manifest.json']}
# Companion changes only the old8th consultation against its actual preimage.
cs=s[-1];ca=a[-1];old="<p>8° Les demandes d'agrément ou de modification d'agrément concernant la maîtrise d'ouvrage prévue à l'article L. 365-2 ;</p>";companion_exact=cs['previous_draft']['proposed_xml'].replace(old,'<p>8° Abrogé.</p>')==ca['proposed_xml']
r=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),mode='ro BEGIN',schema_valid_articles=len(a),schema_does_not_change_frozen_answer=schema_unchanged,source_and_context_records=len(checks),individual_guards=sum(len(x['checks'])for x in checks),checks=checks,policies=pol,author_freeze_matches=freeze,reference_guards=reference_guards,reference_error=locals().get('reference_error'),reference_targets=len(snap['targets']),certificates=certs,companion_only_eighth_entry_changed=companion_exact,all_guards_match=all(all(x['checks'].values())for x in checks)and all(pol.values())and all(freeze.values())and reference_guards and schema_unchanged and companion_exact,semantic_review_by_jurist=False)
(P/'combined-validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['checks','certificates']},ensure_ascii=False));print('FAILURES',[x for x in checks if not all(x['checks'].values())]);print('STALECERT',[x for x in certs if not x['current_before_commit']])

external=[]
for x in json.loads((P/'coherence002/primary-records.json').read_text()):
 f=P/'coherence002'/x['path'];external.append(dict(id=x['id'],sha256=x['sha256'],raw_hash_matches=sha(f.read_bytes())==x['sha256']))
assert all(x['raw_hash_matches']for x in external)
assert all(all(f.values())for f in input_freezes.values()),input_freezes
# Exact body limits against initial frozen proposal.
initial=json.loads((P/'answer.json').read_text());initial_by={ref.key(x):x for x in initial};merged_by={ref.key(x):x for x in a}
transitions={}
import re
for x in json.loads((P/'transition001/answer.json').read_text()):
 before=initial_by[ref.key(x)]['proposed_xml'];after=x['proposed_xml'];bs=re.findall(r'<p>.*?</p>',before,re.S);ns=re.findall(r'<p>.*?</p>',after,re.S);transitions[x['number']]=sum(v!=w for v,w in zip(bs,ns))==1 and len(bs)==len(ns)
dsrc=json.loads((P/'coherence002/source.json').read_text())[1]['source_xml'];dnew=merged_by[ref.key(json.loads((P/'coherence002/source.json').read_text())[1])]['proposed_xml'];two_replacements=dsrc.replace('R. 481-5-6','D. 481-5-6').replace("aux 1° à 5° de l'article 3 de la loi n° 91-650 du 9 juillet 1991 portant réforme des procédures civiles d'exécution","aux 1° à 5° de l'article L. 111-3 du code des procédures civiles d'exécution")==dnew
meta=json.loads((P/'metadata-crpa001/answer.json').read_text())[0];metadata_body_unchanged=meta['proposed_xml']==initial_by[ref.key(meta)]['proposed_xml']
from collections import Counter
r.update(additional_freezes=input_freezes,external_primary_files=external,transition_each_one_paragraph=transitions,D481_5_7_only_two_exact_replacements=two_replacements,R365_6_metadata_body_unchanged=metadata_body_unchanged,merged_classifications=dict(Counter(x['substantive_impact']['classification']for x in a)))
r['all_guards_match']=r['all_guards_match']and all(transitions.values())and two_replacements and metadata_body_unchanged
(P/'combined-validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');assert r['all_guards_match'];print('COMBINED',len(s),'GUARDS',r['individual_guards'],'PRIMARY',len(external),'PASS')
