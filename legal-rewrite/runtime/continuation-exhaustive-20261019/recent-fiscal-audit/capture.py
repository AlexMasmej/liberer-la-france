from pathlib import Path
import json,sqlite3,hashlib,sys,time
P=Path(__file__).resolve().parent;B=P.parents[2];sys.path.insert(0,str(B));from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
# Explicit manual authorship and article-level review decisions, not broad captures.
manual=set();exclusion_files=[]
for d in (B/'batches').iterdir():
    if not d.is_dir()or d.name.startswith('automatic-'):continue
    for f in d.glob('*.json'):
        try:r=json.loads(f.read_text())
        except (ValueError,UnicodeError):continue
        if not isinstance(r,list):continue
        found=False
        for x in r:
            if isinstance(x,dict)and x.get('proposed_xml')and x.get('code_id')and x.get('source_id'):manual.add((x['code_id'],x['source_id']));found=True
        if found:exclusion_files.append({'path':str(f.relative_to(B)),'sha256':sha(f.read_bytes())})
for f in (B/'runtime').rglob('review-decisions.json'):
    if 'exhaustive' in f.relative_to(B/'runtime').parts or P in f.parents:continue
    try:r=json.loads(f.read_text())
    except ValueError:continue
    if isinstance(r,list):
        for x in r:
            if isinstance(x,dict)and x.get('code_id')and x.get('source_id'):manual.add((x['code_id'],x['source_id']))
        exclusion_files.append({'path':str(f.relative_to(B)),'sha256':sha(f.read_bytes())})
files=[]
for slug in ['impots']+['impots-annexe-'+str(i)for i in range(1,5)]:
    for f in (B/'batches'/('automatic-'+slug)).glob('*.json'):files.append((f.stat().st_mtime_ns,slug,f))
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN');rows=[];excluded=[];seen=set()
for mtime,slug,f in sorted(files,reverse=True):
    content=f.read_bytes();accepted=json.loads(content)
    for index in range(len(accepted)-1,-1,-1):
        x=accepted[index];key=x['code_id'],x['source_id']
        if key in seen:continue
        seen.add(key)
        if key in manual:excluded.append({'code_id':key[0],'source_id':key[1],'number':x['number'],'reason':'Explicit prior manual batch or article-level review'});continue
        d=c.execute('select * from drafts where code_id=? and source_id=?',key).fetchone()
        if not d or not d['proposed_xml']or d['proposed_xml']!=x.get('proposed_xml'):excluded.append({'code_id':key[0],'source_id':key[1],'number':x['number'],'reason':'Not current accepted body in coherent snapshot'});continue
        a=dict(c.execute('select * from articles where code_id=? and id=?',key).fetchone());raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert sha(raw)==a['source_sha256']==d['source_sha256']
        a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(c,*key);a['source_document_xml']=raw;a['source_document_sha256']=sha(raw);a['source_body_sha256']=sha(a['source_xml']);a['source_notes_sha256']=sha(a['source_notes_xml']);a['previous_draft']=dict(d);a['current_beforeimage_sha256']=sha(d['proposed_xml']);a['source_url']='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id'];a['slug']=slug;a['benefit_check_required']=True;a['accepted_batch']={'path':str(f.relative_to(B)),'sha256':sha(content),'file_mtime_ns':mtime,'row_index_zero_based':index};rows.append(a)
        if len(rows)==32:break
    if len(rows)==32:break
assert len(rows)==32;c.rollback();c.close()
(P/'audited-source.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
policy={}
for n in ['policy-coordinations.json','site-summaries.json']:
    raw=(B/n).read_bytes();(P/n).write_bytes(raw);policy[n]=sha(raw)
manifest={'scope':'32 latest currently accepted first-rewrite fiscal records, excluding explicitly manually authored/reviewed identifiers','ordering':'Descending atomic accepted batch filemtime; descending row index breaks equal commit-time ties deterministically. mtime is acceptance-order proxy, not a database timestamp.','captured_at_unix':time.time(),'transaction':'SQLite mode=ro; BEGIN; all32records anddocuments from the same read transaction; ROLLBACK','audited_source_sha256':sha((P/'audited-source.json').read_bytes()),'policy_hashes':policy,'manual_exclusion_index_count':len(manual),'manual_exclusion_evidence':exclusion_files,'excluded_encountered':excluded,'articles':[{k:x[k]for k in ['code_id','source_id','number','slug','source_sha256','source_body_sha256','source_notes_sha256','current_beforeimage_sha256','accepted_batch']}for x in rows],'state':'captured_not_yet_legal_review_complete'}
(P/'capture-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'articles':[{'slug':x['slug'],'number':x['number'],'source_chars':len(x['source_xml']),'draft_chars':len(x['previous_draft']['proposed_xml'])}for x in rows],'excluded':excluded,'manifest_sha256':sha((P/'capture-manifest.json').read_bytes())},ensure_ascii=False,indent=2))
