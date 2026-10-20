"""Bounded E52 RO preflight; frozen answers are copied, never recertified or registered."""
from pathlib import Path
import argparse,copy,hashlib,json,re,sqlite3,sys,datetime
O=Path(__file__).resolve().parent;E=O.parents[1];B=next(p for p in O.parents if p.name=='legal-rewrite');sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
L=lambda p:json.loads(p.read_text())
def save(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
key=lambda x:x['code_id']+'|'+x.get('source_id',x.get('id',''))
parser=argparse.ArgumentParser();parser.add_argument('--social-review',type=Path,required=True);parser.add_argument('--social-review-sha256',required=True);args=parser.parse_args()
assert not(O/'manifest.json').exists(),'Refuse to overwrite frozen integration edition'
packs=[('fiscal/edition001','04477a61f4f31d078bc8d8c207c8cdf04aefe613d46365dfa4b98eef3e45511c',24),('logement/edition001','2f45f3ed979e39a73c8c30c16002d2d6c736ee9ec4c66b9d073648b96d832ad7',24),('social-coordination/edition001','9831f7210a9a28dab7417b205b49b9a0337256657e77b67902b2b6be8b5b5150',3),('social-coordination/complement-r243-59/edition001','32efc5b74c970dc2110c42193e8a77e6abc3b7b4e964d85c74f8fae7a784e36a',1)]
proofs=[(E/'fiscal-independent-review/edition001/review.json','c73f1d58049a4ff089dd683655cdb269a15f4061b0cf664aeaad330e764cf4f8'),(E/'logement-independent-review/edition001/review.json','d0daab7d432f6fc39ca45e9869681911023185ea8b86e0add6d4a5d2b9a82c0d'),(args.social_review.resolve(),args.social_review_sha256)]
for p,h in proofs:assert H(p.read_bytes())==h,(p,'review hash')
for p,h in proofs:assert not L(p).get('blocking_findings'),(p,'blocking findings')
def manifest(p,expected):
 m=L(p/'manifest.json');assert H((p/'manifest.json').read_bytes())==expected
 for n,h in m.get('files_sha256',m.get('files',{})).items():assert H((p/n).read_bytes())==h,(p,n)
 for n,h in m.get('external_evidence',{}).items():assert H((B/n).read_bytes())==h,n
 return m
ss=[];aa=[];snaps=[];provenance=[]
for name,msha,count in packs:
 p=E/name;manifest(p,msha);s=L(p/'source.json');a=L(p/'answer.json');assert len(s)==len(a)==count
 validate_answer(copy.deepcopy(a),copy.deepcopy(s));assert[key(x)for x in s]==[key(x)for x in a]
 ss+=s;aa+=a;snaps.append(L(p/'reference-targets.json'));provenance.append({'path':str(p),'manifest_sha256':msha,'source_sha256':H((p/'source.json').read_bytes()),'answer_sha256':H((p/'answer.json').read_bytes()),'count':count})
assert len(ss)==len({key(s)for s in ss})==52
supp=E/'logement/dependency-supplement/edition001';manifest(supp,'94cffba79d4cb00227af440997c119a214a9adb08bcf7af2ba787bedf2a3cf55')
Dcontext=B/'runtime/poursuite-20261020-d/social-context-review/edition001';manifest(Dcontext,'d96cec5f43ceb7751ad7b742252cb8100d856f47a8d0ca0573c18ae7226ff2e6')
l2443=next(t for t in L(Dcontext/'job-current.json')if t['number']=='L244-3');assert l2443['source_id']=='LEGIARTI000033713008'
expected={key(s):s for s in ss};answer={key(a):a for a in aa};conn=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);conn.row_factory=sqlite3.Row;conn.execute('BEGIN');cache={};checks=[]
def current(k):
 if k not in cache:
  code,sid=k.split('|');r=conn.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',(code,sid)).fetchone();assert r is not None,k
  raw=conn.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,sid)).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert H(raw)==r['source_sha256'];pr=conn.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(code,sid)).fetchone();notes=source_notes(conn,code,sid)
  cache[k]={'number':r['number'],'source_sha256':r['source_sha256'],'source_xml':r['content_xml'],'source_notes_xml':notes,'source_document_xml':raw,'prior':dict(pr)if pr else None,'state':rc.state(conn,k),'guard':{'code_id':code,'source_id':sid,'number':r['number'],'source_sha256':r['source_sha256'],'source_body_sha256':H(r['content_xml']),'source_notes_sha256':H(notes),'proposed_sha256':H(pr['proposed_xml']if pr else None)}}
 return cache[k]
merged_sources=[]
for s in ss:
 k=key(s);v=current(k);assert all(s[f]==v[f]for f in ['number','source_sha256','source_xml','source_notes_xml']),k
 if'source_document_xml'in s:assert s['source_document_xml']==v['source_document_xml']
 old=s.get('previous_draft');assert(v['prior']is None)==(old is None),k
 if old:
  assert all(v['prior'][f]==old[f]for f in v['prior']),k
  if'proposed_sha256'in old:assert old['proposed_sha256']==H(v['prior']['proposed_xml'])
 out=copy.deepcopy(s);out['source_document_xml']=v['source_document_xml'];merged_sources.append(out);checks.append({'key':k,'number':s['number'],'source_notes_rawXML_prior_exact':True,'prior_exists':old is not None,'before_guard':v['guard']})
for snap in snaps:rc.check_guards(conn,snap)
# Author-specific map normalization only; preserve the complete original row and native certificates.
fm=L(E/'fiscal/edition001/article-dependency-map.json')['rows'];hm=L(E/'logement/edition001/article-dependency-map.json')['articles'];sm=L(E/'social-coordination/article-dependency-map.json')['articles'];normalized=[]
def dep(k,why,old=None):
 v=current(k);g=v['guard']
 if old:
  for f,h in old.items():
   if f in g:assert g[f]==h,(k,f)
   elif f in v['state']:assert v['state'][f]==h,(k,f)
 future={**g,'proposed_sha256':H(answer[k]['proposed_xml'])}if k in answer else None
 return {'target_key':k,'number':v['number'],'why_used':why,'actual_before_guard':g,'internal_E':k in expected,'future_guard_not_actual_DB':future,'future_body_changes':bool(future and future!=g)}
for x in fm:normalized.append({'referrer_key':key(x),'number':x['number'],'author_map_row':x,'legal_dependencies':[dep(key(d),d['justification'],d['current_guard'])for d in x['dependencies']],'documentary_dependencies':x.get('documentary_dependencies',[])})
for x in hm:normalized.append({'referrer_key':x['referrer_key'],'number':x['number'],'author_map_row':x,'legal_dependencies':[dep(d['target_key'],d['why_used'],d['actual_guard'])for d in x['legal_dependencies']],'documentary_dependencies':x['external_dependencies']})
social_catalog={key(t):t for snap in snaps[2:]for t in snap['targets'].values()}
for t in L(E/'social-coordination/edition001/additional-context.json'):social_catalog[key(t)]=t
social_catalog[key(l2443)]=l2443
for s in ss[48:]:social_catalog[key(s)]=s
for x in sm:
 src=next(s for s in ss[48:]if s['number']==x['number']);deps=[]
 for label,why in x['operative_targets'].items():
  for n in re.findall(r'[LR]\d+(?:-\d+)+(?:\s+[A-Z](?=\s|$))?',label):
   candidates=[(k,t)for k,t in social_catalog.items()if t['code_id']=='LEGITEXT000006073189'and rc.normalize(t['number'])==rc.normalize(n)]
   assert len(candidates)==1,(x['number'],label,n);k,t=candidates[0];v=current(k)
   assert v['source_sha256']==t['source_sha256']and v['source_xml']==t['source_xml']and v['source_notes_xml']==t['source_notes_xml']
   if'view_sha256'in t:assert v['state']['view_sha256']==t['view_sha256']
   if'proposed_xml'in t:assert H(t['proposed_xml'])==v['guard']['proposed_sha256']
   if'raw_document_xml'in t:assert t['raw_document_xml']==v['source_document_xml']
   deps.append(dep(k,label+': '+why))
 normalized.append({'referrer_key':key(src),'number':x['number'],'author_map_row':x,'legal_dependencies':deps,'documentary_dependencies':[]})
assert len(normalized)==52 and{r['referrer_key']for r in normalized}==set(expected)
# External documentary additions for R635-3 are bound to the unchanged housing answer.
x=L(supp/'article-dependency-map-supplement.json');assert H((E/'logement/edition001/answer.json').read_bytes())==x['bound_answer_file_sha256']
next(r for r in normalized if r['referrer_key']==x['referrer_key'])['documentary_dependencies']+=x['additional_external_dependencies']
registration={'version':rc.VERSION,'scope':'E52_external_targets_only_registration_guard_not_reissued_certificate','policy_sha256':rc.policy_state(),'requirements':{},'targets':{},'referrers':{key(s):rc.referrer_source(conn,key(s))for s in ss},'semantic_review_by_jurist':False}
for row in normalized:
 k=row['referrer_key'];registration['requirements'][k]=[]
 for d in row['legal_dependencies']:
  if not d['internal_E']:registration['targets'][d['target_key']]=rc.view(conn,d['target_key']);registration['requirements'][k].append(d['target_key'])
for snap in snaps:
 assert snap['policy_sha256']==registration['policy_sha256']
 for k,needs in snap['requirements'].items():
  for tk in needs:
   if tk not in expected:
    registration['targets'][tk]=snap['targets'][tk];registration['requirements'][k]=sorted(set(registration['requirements'][k])|{tk})
rc.check_guards(conn,registration)
# Frozen analyses/impact certificates/native reference checks remain byte-for-byte JSON objects.
assert aa==sum([L(E/name/'answer.json')for name,_,_ in packs],[])
validate_answer(copy.deepcopy(aa),copy.deepcopy(merged_sources));save('source.json',merged_sources);save('answer.json',aa);save('reference-targets.json',registration)
save('original-reference-snapshots.json',{'packs':provenance,'snapshots':snaps,'no_initial_checks_or_certificates_discarded':True})
save('article-dependency-map.json',{'scope':'52 specifically mapped rows, author analyses preserved; no all-to-all pinning','articles':normalized})
save('internal-future-guards.json',{'status':'hypothetical_only_not_recertified','edges':[{'referrer_key':r['referrer_key'],**d}for r in normalized for d in r['legal_dependencies']if d['internal_E']],'native_protocol_internal_edges':[{'referrer_key':k,'target_key':tk,'actual_before_state':current(tk)['state'],'future_body_sha256':H(answer[tk]['proposed_xml'])}for snap in snaps for k,needs in snap['requirements'].items()for tk in needs if tk in expected],'post_commit_plan_path':str(E/'social-coordination/post-commit-reissue-plan.json'),'post_commit_plan_sha256':H((E/'social-coordination/post-commit-reissue-plan.json').read_bytes()),'no_future_certificate_emitted':True})
save('preflight.json',{'status':'passed_readonly_preflight_not_registration','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'identities':52,'fresh_sources':sum(s.get('previous_draft')is None for s in ss),'prior_revisions':sum(s.get('previous_draft')is not None for s in ss),'pack_inputs':provenance,'review_evidence':[{'path':str(p),'sha256':h}for p,h in proofs],'additional_frozen_L2443_evidence':{'manifest_path':str(Dcontext/'manifest.json'),'manifest_sha256':H((Dcontext/'manifest.json').read_bytes()),'capture_path':str(Dcontext/'job-current.json'),'capture_sha256':H((Dcontext/'job-current.json').read_bytes()),'actual_DB_body_notes_rawXML_proposal_exact':True},'own_checks':checks,'external_registration_targets':len(registration['targets']),'per_article_legal_edges':sum(len(r['legal_dependencies'])for r in normalized),'native_snapshots_checked':4,'answers_analyses_certificates_unmodified':True,'merged_social_rawXML_added_from_actual_DB':True,'no_future_target_certificates_emitted':True,'requires_parent_writer_lock_recheck':True,'canonical_mutation':False})
conn.rollback();conn.close();save('manifest.json',{'frozen':True,'files_sha256':{p.name:H(p.read_bytes())for p in sorted(O.iterdir())if p.is_file()and p.name!='manifest.json'},'identities':52,'canonical_mutation':False});print(json.dumps({n:H((O/n).read_bytes())for n in ['source.json','answer.json','reference-targets.json','article-dependency-map.json','internal-future-guards.json','preflight.json','manifest.json']},indent=2))
