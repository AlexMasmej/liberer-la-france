from pathlib import Path
import sqlite3,json,hashlib,sys,copy
O=Path(__file__).resolve().parent;B=O.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as ref
H=lambda s:hashlib.sha256(s if isinstance(s,bytes)else(s or'').encode()).hexdigest()
L=lambda n:json.loads((O/n).read_text())
def S(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ss=L('source.json')+L('companion-source.json');aa=L('answer.json')+L('companion-answer.json');validate_answer(copy.deepcopy(aa),copy.deepcopy(ss));d=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');checks=[]
refs=L('references.json')+[L('election-reference.json')]
for s in ss+refs:
 k=(s['code_id'],s['source_id']);a=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone();pr=d.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();old=s.get('previous_draft');expected=(old['source_sha256'],old['proposed_xml'])if old else None
 assert tuple(a)==(s['source_sha256'],s['source_xml'])and source_notes(d,*k)==s['source_notes_xml'],s['number'];assert(tuple(pr)if pr else None)==expected,s['number']
 if s.get('source_document_xml'):
  raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert raw==s['source_document_xml'],s['number']
 checks.append({'code_id':k[0],'source_id':k[1],'number':s['number'],'source_sha256':s['source_sha256'],'source_xml_sha256':H(s['source_xml']),'notes_sha256':H(s['source_notes_xml']),'prior_proposal_sha256':H(old['proposed_xml'])if old else None,'source_notes_prior_equal':True})
for n in ['policy-coordinations.json','site-summaries.json']:assert H((O/n).read_bytes())==H((B/n).read_bytes()),n
snapshot=ref.capture(d,ss,aa)
for s in refs:snapshot['targets'][ref.key(s)]=ref.view(d,ref.key(s))
ref.check_guards(d,snapshot);S('reference-targets.json',snapshot);S('fresh-guards.json',{'checks':checks,'policy_sha256':snapshot['policy_sha256'],'readonly_snapshot':True,'absence_of_proposal_checks':48,'prior_revision_checks':1,'canonical_mutation':False})
known={ref.key(s)for s in ss+refs};extra=sorted(set(snapshot['targets'])-known);S('automatic-extra-references.json',[snapshot['targets'][k]for k in extra]);print('EXTRA',[(snapshot['targets'][k]['number'],k)for k in extra]);print('REQUIRED',[(next(s['number']for s in ss if ref.key(s)==k),len(v))for k,v in snapshot['requirements'].items()if v]);d.rollback();d.close()
