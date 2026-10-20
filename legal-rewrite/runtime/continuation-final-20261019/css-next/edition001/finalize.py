from pathlib import Path
import json,hashlib,sqlite3,sys,xml.etree.ElementTree as E
H=Path(__file__).resolve().parent;B=H.parents[3];sys.path.insert(0,str(B));from run_exhaustive import validate_answer
sha=lambda v:hashlib.sha256(v.encode()if isinstance(v,str)else v).hexdigest()
sources=json.loads((H/'source.json').read_text());answers=json.loads((H/'answer.json').read_text());validate_answer(answers,sources)
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;checks=[];conflicts=[]
for s in sources:
 assert sha(s['source_document_xml'])==s['source_sha256'];assert sha(s['source_xml'])==s['source_body_sha256'];assert sha(s['source_notes_xml'])==s['source_notes_sha256'];assert '<img'not in s['source_xml']
 a=c.execute('select source_sha256,content_xml from articles where code_id=? and id=?',(s['code_id'],s['source_id'])).fetchone();d=c.execute('select * from drafts where code_id=? and source_id=?',(s['code_id'],s['source_id'])).fetchone()
 good=a['source_sha256']==s['source_sha256']and a['content_xml']==s['source_xml']and d is None
 check={'code_id':s['code_id'],'source_id':s['source_id'],'number':s['number'],'source_match':a['source_sha256']==s['source_sha256'],'no_current_draft':d is None,'valid':good};checks.append(check)
 if not good:conflicts.append(check)
c.close()
(H/'guards.json').write_text(json.dumps({'checked_readonly':True,'as_of':'2026-10-19','conflicts':conflicts,'records':checks},ensure_ascii=False,indent=2)+'\n')
(H/'validation.json').write_text(json.dumps({'valid':not conflicts,'candidate_count':len(answers),'source_count':len(sources),'validate_answer':'passed; structural validation only','source_raw_body_notes_hashes':'passed','graphics':0,'concurrent_changes':conflicts,'registered':False,'published':False},ensure_ascii=False,indent=2)+'\n')
assert not conflicts,conflicts
files=['source.json','expected.json','answer.json','references.json','direct-links.json','dsn-law-links.json','guards.json','validation.json','audit.md']
manifest={'frozen':True,'edition':'001','as_of':'2026-10-19','candidate_count':len(answers),'files':{f:sha((H/f).read_bytes())for f in files},'registered':False,'published':False}
(H/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');print(json.dumps(manifest,ensure_ascii=False,indent=2))
