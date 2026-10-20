import pathlib,json,hashlib,sqlite3,sys,datetime,shutil,re
R=pathlib.Path(__file__).resolve().parent;H=pathlib.Path('legal-rewrite').resolve();sys.path.insert(0,str(H));from ingest import source_notes
sha=lambda s:hashlib.sha256((s or '').encode()).hexdigest()
write=lambda n,x:(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
J=H/'runtime/exhaustive/jobs/securite-sociale-00046'
for n in ['source.json','answer.json','reference-targets.json','coordination.json','policy.json','policy-fingerprint.json','result.json']:
 shutil.copyfile(J/n,R/('job-'+n))
for src,dst in [('runtime/substantive-audits.json','ledger-before.json'),('runtime/poursuite-20261020-c/audit-adoption.json','C-adoption.json'),('policy-coordinations.json','policy-coordinations.json'),('site-summaries.json','site-summaries.json')]:shutil.copyfile(H/src,R/dst)
S=json.loads((R/'job-source.json').read_text());A=json.loads((R/'job-answer.json').read_text());T=json.loads((R/'job-reference-targets.json').read_text());L=json.loads((R/'ledger-before.json').read_text());C=json.loads((R/'C-adoption.json').read_text());Ckeys={x['key'] for x in C['adopted']};Cledger=[x for x in L['audits'] if x['code_id']+'|'+x['source_id'] in Ckeys]
index={}
for p in (H/'runtime/export-source').glob('*.json'):
 try:
  x=json.loads(p.read_text())
  if isinstance(x,list):
   for a in x:
    if isinstance(a,dict) and 'source_id'in a:index[(a['code_id'],a['number'])]=(a['code_id'],a['source_id'])
 except:pass
c=sqlite3.connect('file:'+str(H/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN');cache={}
def get(k):
 if k in cache:return cache[k]
 a=c.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone()
 if not a:cache[k]=None;return None
 d=c.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();raw=c.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()
 x={'code_id':k[0],'source_id':k[1],'number':a['number'],'source_sha256':a['source_sha256'],'source_xml':a['content_xml'],'source_notes_xml':source_notes(c,*k),'proposed_xml':d['proposed_xml'] if d else None,'draft_exists':bool(d),'status':d['status'] if d else None,'reason':d['reason'] if d else None,'review_notes':d['review_notes'] if d else None,'raw_document_xml':raw['xml'].decode() if raw and isinstance(raw['xml'],bytes) else raw['xml'] if raw else None}
 x['guards']={z:sha(x[f]) for z,f in [('source_body_sha256','source_xml'),('source_notes_sha256','source_notes_xml'),('proposed_sha256','proposed_xml'),('raw_document_sha256','raw_document_xml')]};cache[k]=x;return x
jobcurrent=[get((x['code_id'],x['source_id'])) for x in S]
extra=[]
for k in T['targets']:extra.append(get(tuple(k.split('|'))))
for num in ['R243-18','R243-19','L243-6-1','L244-8-1','L244-11','R243-17','R133-8-7','L1234-3','L1237-1','L3243-4','L1251-49','L8222-1','D8222-5']:
 code='LEGITEXT000006072050' if num in ['L1234-3','L1237-1','L3243-4','L1251-49','L8222-1','D8222-5'] else 'LEGITEXT000006073189'
 k=index.get((code,num))
 if k:extra.append(get(k))
 else:print('missing canonical index',num)
jobchecks=[]
for old,ans,now in zip(S,A,jobcurrent):
 checks={'source_sha256':old['source_sha256']==now['source_sha256'],'source_body':old['source_xml']==now['source_xml'],'notes':old['source_notes_xml']==now['source_notes_xml'],'draft_exists':now['draft_exists'],'accepted_answer_body':ans['proposed_xml']==now['proposed_xml'],'accepted_answer_status':ans['status']==now['status']}
 jobchecks.append({'key':now['code_id']+'|'+now['source_id'],'number':now['number'],'checks':checks})
Ccurrent=[get(tuple(k.split('|'))) for k in sorted(Ckeys)]
changed={};allguardresults=[]
for au in Cledger:
 ak=au['code_id']+'|'+au['source_id'];bad=[]
 for g in au.get('dependency_guards',[]):
  now=get((g['code_id'],g['source_id']));ng={'source_sha256':now['source_sha256'],**now['guards']} if now else {}
  delta={f:{'before':g[f],'current':ng.get(f)} for f in ['source_sha256','source_body_sha256','source_notes_sha256','proposed_sha256'] if g.get(f)!=ng.get(f)}
  if delta:
   k=g['code_id']+'|'+g['source_id'];bad.append(k);changed.setdefault(k,{'number':now['number'] if now else None,'delta':delta,'affected_C_audits':[]})['affected_C_audits'].append(ak)
 allguardresults.append({'audit_key':ak,'changed_dependency_keys':bad})
pattern=re.compile(r'L\s*[. ]?\s*243\s*[-–]\s*7\s*[-–]\s*6(?![0-9])',re.I)
direct=[]
for x in Ccurrent:
 if pattern.search((x['source_xml'] or '')+'\n'+(x['proposed_xml'] or '')):direct.append({'key':x['code_id']+'|'+x['source_id'],'number':x['number'],'source_has_reference':bool(pattern.search(x['source_xml'])),'proposed_has_reference':bool(pattern.search(x['proposed_xml'] or ''))})
write('job-current.json',jobcurrent);write('critical-context.json',list({(x['code_id'],x['source_id']):x for x in extra if x}.values()));write('accepted-job-checks.json',jobchecks)
write('C-dependency-impact.json',{'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ledger_sha256':hashlib.sha256((R/'ledger-before.json').read_bytes()).hexdigest(),'phase_C_count':len(Cledger),'changed_targets':changed,'mechanical_guard_checks':allguardresults,'direct_body_references_to_L243_7_6':direct,'scope':'Guard comparison and literal-reference search over144; full semantic rereading only targeted entries, not all144'})
write('C-direct-referrers.json',[x for x in Ccurrent if any(d['key']==x['code_id']+'|'+x['source_id'] for d in direct)])
write('captured-guard-records.json',[{'code_id':x['code_id'],'source_id':x['source_id'],'number':x['number'],'source_sha256':x['source_sha256'],'draft_exists':x['draft_exists'],'status':x['status'],**x['guards']} for x in cache.values() if x])
c.rollback();c.close();print('job checks',all(all(r['checks'].values()) for r in jobchecks),'critical',len(extra),'C',len(Cledger),'targets',[(v['number'],len(v['affected_C_audits'])) for v in changed.values()],'direct',direct,'snapshot guards',len(cache))
