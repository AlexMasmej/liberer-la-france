from pathlib import Path
import json,sqlite3,hashlib,sys,copy,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes;from run_exhaustive import validate_answer;import reference_coherence as ref
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or '').encode()).hexdigest()
s=json.loads((P/'source.json').read_text())+json.loads((P/'companion-source.json').read_text());a=json.loads((P/'answer.json').read_text())+json.loads((P/'companion-answer.json').read_text());ctx=json.loads((P/'references.json').read_text())+json.loads((P/'automatic-extra-references.json').read_text())+[json.loads((P/'election-reference.json').read_text())];snap=json.loads((P/'reference-targets.json').read_text())
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
(P/'validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['checks','certificates']},ensure_ascii=False));print('FAILURES',[x for x in checks if not all(x['checks'].values())]);print('STALECERT',[x for x in certs if not x['current_before_commit']])
