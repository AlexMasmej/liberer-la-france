from pathlib import Path
import json,sqlite3,copy,hashlib,sys,re,xml.etree.ElementTree as E
O=Path(__file__).resolve().parent;B=O.parents[3];P=O.parents[1]/'fiscal/edition001';sys.path.insert(0,str(B));from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
L=lambda n:json.loads((P/n).read_text())
def S(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ss=L('source.json')+L('companion-source.json');aa=L('answer.json')+L('companion-answer.json');rr=L('references.json');m=L('manifest.json')
for n,h in m.get('files_sha256',m.get('files',{})).items():assert H((P/n).read_bytes())==h,n
validate_answer(copy.deepcopy(aa),copy.deepcopy(ss));d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');checks=[]
for s in ss+rr:
 k=s['code_id'],s['source_id'];r=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone();assert tuple(r)==(s['source_sha256'],s['source_xml']),s['number'];assert source_notes(d,*k)==s['source_notes_xml'],s['number'];raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert raw==s['source_document_xml'],s['number'];pr=d.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();old=s.get('previous_draft');assert(tuple(pr)if pr else None)==((old['source_sha256'],old['proposed_xml'])if old else None),s['number']
 checks.append({'code_id':k[0],'source_id':k[1],'number':s['number'],'source_sha256':s['source_sha256'],'body_sha256':H(s['source_xml']),'notes_sha256':H(s['source_notes_xml']),'document_sha256':H(raw),'prior_proposed_sha256':H(old['proposed_xml'])if old else None,'source_notes_document_prior_equal':True})
snap=L('reference-targets.json');rc.check_guards(d,snap)
for n in ['policy-coordinations.json','site-summaries.json']:assert H((P/n).read_bytes())==H((B/n).read_bytes()),n
s=next(x for x in ss if x['number']=='1665 bis');a=next(x for x in aa if x['number']=='1665 bis');prefix=s['source_xml'][:s['source_xml'].rfind('<p>')];assert a['proposed_xml'].startswith(prefix)
tables=[]
for x in rr:
 if x['number']!='204 H':continue
 old=E.fromstring('<root>'+x['source_xml']+'</root>');new=E.fromstring('<root>'+x['previous_draft']['proposed_xml']+'</root>');ts=lambda root:[[[(''.join(cell.itertext()),dict(cell.attrib))for cell in row]for row in t.findall('.//tr')]for t in root.findall('.//table')]
 left=ts(old);right=ts(new);assert[[[c[0]for c in row]for row in t]for t in left]==[[[c[0]for c in row]for row in t]for t in right];tables={'table_count':len(left),'row_counts':[len(t)for t in left],'all_cell_texts_identical':True}
S('guards.json',{'readonly_snapshot':True,'checks':checks,'unique_identities':len({x['code_id']+'|'+x['source_id']for x in ss+rr}),'source_entries':len(ss),'reference_entries_including_duplicate900B':len(rr),'reference_check_guards':True,'policy_sha256':snap['policy_sha256'],'source_table_204H_cells':tables,'advance_prefix_byte_identical':True,'source_and_answer_files':{n:H((P/n).read_bytes())for n in ['source.json','answer.json','companion-source.json','companion-answer.json','manifest.json']},'canonical_mutation':False})
d.rollback();d.close();print('PASS',len(ss),len(rr),len(checks),tables)
