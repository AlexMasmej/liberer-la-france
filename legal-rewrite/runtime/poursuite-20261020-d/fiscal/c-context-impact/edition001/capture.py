"""Read-only comparison: actual C audits versus hypothetical D whole bodies."""
from pathlib import Path
from datetime import datetime,timezone
import sqlite3,json,hashlib,sys,re,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent;B=P.parents[4];C=B/'runtime/poursuite-20261020-c';D=B/'runtime/poursuite-20261020-d/fiscal/edition002';sys.path.insert(0,str(B))
from ingest import source_notes
from substantive_impact import digest,assessment_digest
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ledger_raw=(B/'runtime/substantive-audits.json').read_bytes();ledger=json.loads(ledger_raw);receipt=load(C/'audit-adoption.json');wanted={r['key']for r in receipt['adopted']};audits={r['code_id']+'|'+r['source_id']:r for r in ledger['audits']};assert len(wanted)==144 and wanted<=set(audits)
ss=load(D/'source.json')+load(D/'companion-source.json');aa=load(D/'answer.json')+load(D/'companion-answer.json');sources={s['code_id']+'|'+s['source_id']:s for s in ss};answers={a['code_id']+'|'+a['source_id']:a for a in aa};changed={k:a for k,a in answers.items()if a.get('proposed_xml')is not None};assert len(changed)==11
conn=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);conn.row_factory=sqlite3.Row;conn.execute('BEGIN');cache={}
def get(k):
 if k in cache:return cache[k]
 code,sid=k.split('|');a=conn.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(code,sid)).fetchone();assert a is not None,k;dr=conn.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(code,sid)).fetchone();raw=conn.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,sid)).fetchone();body=raw['xml'].decode()if isinstance(raw['xml'],bytes)else raw['xml'];assert H(body)==a['source_sha256']==raw['sha256'];notes=source_notes(conn,code,sid)
 s=dict(code_id=code,source_id=sid,number=a['number'],source_sha256=a['source_sha256'],source_xml=a['content_xml'],source_notes_xml=notes,source_document_xml=body,source_document_sha256=H(body),source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+sid,previous_draft=dict(dr)if dr else None)
 pin=dict(code_id=code,source_id=sid,number=a['number'],source_sha256=a['source_sha256'],source_body_sha256=H(a['content_xml']),source_notes_sha256=H(notes),proposed_sha256=H(dr['proposed_xml']if dr else None));cache[k]=(s,pin);return cache[k]
fields=['code_id','source_id','source_sha256','source_body_sha256','source_notes_sha256','proposed_sha256']
D_changes=[]
for k,a in changed.items():
 s,pin=get(k);frozen=sources[k];assert(s['source_sha256'],s['source_xml'],s['source_notes_xml'],s['source_document_xml'],s['previous_draft'])==(frozen['source_sha256'],frozen['source_xml'],frozen['source_notes_xml'],frozen['source_document_xml'],frozen['previous_draft']),('D before-image changed',k)
 future={**pin,'proposed_sha256':H(a['proposed_xml'])};D_changes.append(dict(key=k,number=a['number'],before_guard=pin,future_guard=future,future_guard_is_hypothetical_not_DB=True,changed_fields=[f for f in fields if pin[f]!=future[f]],future_body_sha256=H(a['proposed_xml'])))
future_by={x['key']:x['future_guard']for x in D_changes};rows=[];direct={};read=[]
# Explicit number references only; no claim that text search alone establishes semantic compatibility.
patterns={k:re.compile(r'(?<![\dA-Za-z])'+re.escape(a['number']).replace(r'\ ',r'\s*')+r'(?![\dA-Za-z])',re.I)for k,a in changed.items()}
for k in sorted(wanted):
 audit=audits[k];s,_=get(k);dr=s['previous_draft'];assert dr is not None;before_fail=[];future_new=[];actual_changes=[]
 cert=audit['certificate'];expected=dict(source_sha256=s['source_sha256'],source_notes_sha256=H(s['source_notes_xml']),proposed_sha256=H(dr['proposed_xml']),assessment_sha256=assessment_digest(audit['assessment']),policy_sha256=H((B/'policy-coordinations.json').read_bytes()))
 own_changed=[f for f,v in expected.items()if cert.get(f)!=v]
 if audit.get('source_body_sha256')!=H(s['source_xml']):own_changed.append('source_body_sha256')
 for g in audit['dependency_guards']:
  dk=g['code_id']+'|'+g['source_id'];ds,actual=get(dk);bad=[f for f in fields if g.get(f)!=actual[f]]
  if bad:before_fail.append(dict(target_key=dk,number=ds['number'],fields=bad,expected_guard=g,actual_guard=actual))
  if dk in future_by:
   future=future_by[dk];badfuture=[f for f in fields if g.get(f)!=future[f]]
   if badfuture:
    actual_changes.append(dict(target_key=dk,number=ds['number'],currently_exact=not bad,changed_fields_vs_stored_guard=badfuture,before_guard=g,actual_before_guard=actual,hypothetical_future_guard=future))
    if not bad:future_new.append(dk)
 body=dr['proposed_xml']or s['source_xml'];matches=[]
 for dk,pat in patterns.items():
  found=[]
  for label,text in [('source_xml',s['source_xml']),('source_notes_xml',s['source_notes_xml']),('current_proposed_xml',dr['proposed_xml']or'')]:
   for m in pat.finditer(text):found.append(dict(field=label,context=text[max(0,m.start()-150):m.end()+200]))
  if found:matches.append(dict(target_key=dk,target_number=changed[dk]['number'],contexts=found))
 # DILA links can cite an older ID; resolve by code+number as well.
 typed=[]
 for e in ET.fromstring(s['source_document_xml']).findall('./LIENS/LIEN'):
  if e.get('sens')!='source'or e.get('typelien')!='CITATION':continue
  for dk,target in changed.items():
   if e.get('cidtexte')==target['code_id']and(e.get('id')==target['source_id']or e.get('num')==target['number']):typed.append(dict(target_key=dk,target_number=target['number'],link=dict(e.attrib)))
 if typed:
  existing={x['target_key']for x in matches}
  for entry in typed:
   if entry['target_key']not in existing:matches.append(dict(target_key=entry['target_key'],target_number=entry['target_number'],contexts=[dict(field='official_typed_CITATION_link',context=entry['link'])]))
 if matches:
  direct[k]=dict(source=s,matches=matches);read.append(s)
 rows.append(dict(key=k,number=s['number'],current_own_certificate_exact=not own_changed,own_certificate_mismatches=own_changed,currently_stale_dependencies=before_fail,hypothetical_D_changed_dependency_guards=actual_changes,newly_mismatching_dependency_keys=future_new,D_would_newly_expire_current_certificate=not own_changed and not before_fail and bool(future_new),D_impacts_declared_guard=bool(actual_changes),textual_candidates_not_yet_semantic_review=matches))
conn.rollback();conn.close();policy={n:H((B/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']};assert H((B/'runtime/substantive-audits.json').read_bytes())==H(ledger_raw),'Ledger mutated during capture'
save('D-future-guard-changes.json',D_changes);save('C-audit-dependency-impact.json',rows);save('C-direct-reference-captures.json',list(direct.values()));save('C-direct-sources.json',read);save('input-state.json',dict(captured_at=datetime.now(timezone.utc).isoformat(),mode='SQLite mode=ro BEGIN',C_audits=144,D_proposals=11,ledger_sha256=H(ledger_raw),C_adoption_sha256=H((C/'audit-adoption.json').read_bytes()),D_manifest_sha256=H((D/'manifest.json').read_bytes()),policy_sha256=policy,mechanically_affected_audits=sum(r['D_impacts_declared_guard']for r in rows),newly_expired_by_D=sum(r['D_would_newly_expire_current_certificate']for r in rows),already_stale=sum(bool(r['currently_stale_dependencies']or r['own_certificate_mismatches'])for r in rows),direct_reference_candidate_articles=len(direct),no_semantic_read_of_all144_claimed=True,no_recertification_or_mutation=True))
print(json.dumps(load(P/'input-state.json'),ensure_ascii=False,indent=2));print('DIRECT',[(k,v['source']['number'],[m['target_number']for m in v['matches']])for k,v in direct.items()])
