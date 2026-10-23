"""Lossless, versioned importer for official DILA LEGI archives.

The importer stores source XML verbatim, never invents rewrites and never
extracts paths from an untrusted archive to the filesystem. Archive imports
are atomic. A truncated archive is rejected, including gzip footer errors.
"""
import argparse, sqlite3, tarfile, gzip, hashlib, json, re
from pathlib import Path
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

HERE=Path(__file__).resolve().parent
CONFIG=json.loads((HERE/'corpus.json').read_text())
TARGETS={x['id']:x for x in CONFIG['codes']+CONFIG.get('annexes',[])}


def atomic_json(path,value,compact=False):
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,**({'separators':(',',':')} if compact else {'indent':2})))
    temporary.replace(path)

def open_db(path):
    db=sqlite3.connect(path,timeout=600)
    db.executescript('''
    PRAGMA journal_mode=WAL;
    CREATE TABLE IF NOT EXISTS archives(name TEXT PRIMARY KEY,sha256 TEXT NOT NULL,source_url TEXT NOT NULL,complete INTEGER NOT NULL,documents INTEGER NOT NULL);
    CREATE TABLE IF NOT EXISTS documents(code_id TEXT NOT NULL,id TEXT NOT NULL,kind TEXT NOT NULL,xml BLOB NOT NULL,sha256 TEXT NOT NULL,archive TEXT NOT NULL,PRIMARY KEY(code_id,id,kind));
    CREATE TABLE IF NOT EXISTS articles(code_id TEXT NOT NULL,id TEXT NOT NULL,number TEXT NOT NULL,valid_from TEXT,valid_until TEXT,state TEXT,content_xml TEXT NOT NULL,plain_text TEXT NOT NULL,source_sha256 TEXT NOT NULL,archive TEXT NOT NULL,PRIMARY KEY(code_id,id));
    CREATE TABLE IF NOT EXISTS drafts(code_id TEXT NOT NULL,source_id TEXT NOT NULL,source_sha256 TEXT NOT NULL,status TEXT NOT NULL,proposed_xml TEXT,reason TEXT,review_notes TEXT,PRIMARY KEY(code_id,source_id));
    CREATE TABLE IF NOT EXISTS draft_sources(code_id TEXT NOT NULL,source_id TEXT NOT NULL,source_xml TEXT NOT NULL,valid_from TEXT,valid_until TEXT,PRIMARY KEY(code_id,source_id));
    CREATE TABLE IF NOT EXISTS scope_completion(scope TEXT PRIMARY KEY,archives INTEGER NOT NULL);
    ''')
    return db

def text_of(root,path):return root.findtext(path,default='').strip()
def xml_contents(el):
    if el is None:return ''
    return (el.text or '')+''.join(ET.tostring(c,encoding='unicode') for c in el)

def source_notes(db,code,identifier):
    row=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,identifier)).fetchone()
    if not row:return ''
    root=ET.fromstring(row[0])
    content=root.find('NOTA/CONTENU')
    if content is None:return ''
    if not ''.join(content.itertext()).strip() and content.find('.//img') is None:return ''
    return xml_contents(content).strip()

def source_evidence(body,notes):
    return body+('\n<!-- OFFICIAL APPLICATION NOTES -->\n'+notes if notes else '')

def import_archive(db,path,url):
    name=Path(urlsplit(url).path).name
    prior=db.execute('SELECT sha256 FROM archives WHERE name=?',(name,)).fetchone()
    with Path(path).open('rb') as source_file:
        digest=hashlib.file_digest(source_file,'sha256').hexdigest()
    if prior:
        if prior[0]!=digest:raise RuntimeError('Previously imported archive changed: '+name)
        return 0
    count=0
    db.execute('BEGIN')
    try:
        # Read to the gzip footer as well as tar EOF to detect truncated files.
        with gzip.open(path,'rb') as gz:
            with tarfile.open(fileobj=gz,mode='r|') as archive:
                for m in archive:
                    if not m.isfile() or not m.name.endswith('.xml'):continue
                    components=m.name.split('/')
                    code=next((c for c in components if c in TARGETS),None)
                    if code is None:continue
                    if m.size>20_000_000:raise ValueError('Unexpectedly large XML document')
                    raw=archive.extractfile(m).read()
                    if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:raise ValueError('External XML entities are not accepted')
                    root=ET.fromstring(raw)
                    identifier=text_of(root,'META/META_COMMUN/ID') or root.findtext('ID')
                    if not identifier:raise ValueError('Missing source identifier')
                    kind=root.tag
                    sha=hashlib.sha256(raw).hexdigest()
                    db.execute('''INSERT INTO documents VALUES(?,?,?,?,?,?)
                        ON CONFLICT(code_id,id,kind) DO UPDATE SET xml=excluded.xml,sha256=excluded.sha256,archive=excluded.archive
                        WHERE excluded.archive>=documents.archive''',(code,identifier,kind,raw,sha,name))
                    if kind=='ARTICLE':
                        meta='META/META_SPEC/META_ARTICLE/'
                        content=root.find('BLOC_TEXTUEL/CONTENU')
                        plain=''.join(content.itertext()) if content is not None else ''
                        db.execute('''INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)
                            ON CONFLICT(code_id,id) DO UPDATE SET number=excluded.number,valid_from=excluded.valid_from,valid_until=excluded.valid_until,state=excluded.state,content_xml=excluded.content_xml,plain_text=excluded.plain_text,source_sha256=excluded.source_sha256,archive=excluded.archive
                            WHERE excluded.archive>=articles.archive''',(code,identifier,text_of(root,meta+'NUM'),text_of(root,meta+'DATE_DEBUT'),text_of(root,meta+'DATE_FIN'),text_of(root,meta+'ETAT'),xml_contents(content),plain,sha,name))
                    count+=1
            while gz.read(1024*1024):pass
        db.execute('INSERT INTO archives VALUES(?,?,?,?,?)',(name,digest,url,1,count))
        db.commit()
    except Exception:
        db.rollback();raise
    return count

def inventory(db,code,as_of):
    root=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='TEXTELR'",(code,code)).fetchone()
    result={'article_ids':[],'sections':[],'missing_sections':[],'missing_articles':[],'paths':{}}
    if not root:
        result['missing_sections'].append(code);return result
    visited=set()
    def walk(node,path):
        for link in node:
            start=link.get('debut','0001-01-01');end=link.get('fin','2999-01-01')
            if not(start<=as_of<end):continue
            identifier=link.get('id')
            if link.tag=='LIEN_ART':
                if identifier not in result['article_ids']:result['article_ids'].append(identifier)
                result['paths'][identifier]=path
                if not db.execute('SELECT 1 FROM articles WHERE code_id=? AND id=?',(code,identifier)).fetchone():result['missing_articles'].append(identifier)
            elif link.tag=='LIEN_SECTION_TA' and identifier not in visited:
                visited.add(identifier);title=''.join(link.itertext()).strip();newpath=path+[title]
                result['sections'].append({'id':identifier,'title':title,'path':newpath})
                row=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='SECTION_TA'",(code,identifier)).fetchone()
                if not row:result['missing_sections'].append(identifier);continue
                section=ET.fromstring(row[0]);struct=section.find('STRUCTURE_TA')
                if struct is not None:walk(struct,newpath)
    element=ET.fromstring(root[0]);struct=element.find('STRUCT')
    if struct is not None:walk(struct,[])
    return result

def export_snapshot(db,as_of,output):
    output.mkdir(parents=True,exist_ok=True)
    coverage={'as_of':as_of,'sources_complete':False,'codes':[],'warnings':[]}
    imported={r[0] for r in db.execute('SELECT name FROM archives WHERE complete=1')}
    required=json.loads((HERE/'archive-manifest.json').read_text()) if (HERE/'archive-manifest.json').exists() else []
    missing=[r['name'] for r in required if r['name'] not in imported]
    coverage['missing_archives']=missing
    annexes_complete=db.execute("SELECT archives FROM scope_completion WHERE scope='cgi-annexes'").fetchone()
    coverage['sources_complete']=bool(required) and not missing and bool(annexes_complete and annexes_complete[0]==len(required))
    for code,config in TARGETS.items():
        tree=inventory(db,code,as_of)
        source_rows=db.execute('SELECT id,number,valid_from,valid_until,state,content_xml,plain_text,source_sha256,archive FROM articles WHERE code_id=? AND valid_from<=? AND valid_until>?',(code,as_of,as_of)).fetchall()
        by_id={row[0]:row for row in source_rows}
        rows=[by_id[i] for i in tree['article_ids'] if i in by_id]
        records=[]
        for row in rows:
            identifier,number,start,end,state,body,plain,sha,archive=row
            notes=source_notes(db,code,identifier)
            draft=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',(code,identifier)).fetchone()
            status='source_imported';proposed=None;reason=None;review=None
            if draft:
                old_sha,status,proposed,reason,review=draft
                if old_sha!=sha:
                    previous=db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',(code,identifier)).fetchone()
                    if previous!=(source_evidence(body,notes),start,end):status='source_changed_review_required';proposed=None
            records.append({'code_id':code,'source_id':identifier,'number':number,'path':tree['paths'].get(identifier,[]),'valid_from':start,'valid_until':end,'source_state':state,'source_xml':body,'source_notes_xml':notes,'source_text':plain,'source_sha256':sha,'source_archive':archive,'source_url':CONFIG['official_source']['source_url_pattern'].format(article_id=identifier),'status':status,'proposed_xml':proposed,'reason':reason,'review_notes':review})
        same_slots={}
        for record in records:
            same_slots.setdefault((record['number'],tuple(record['path'])),[]).append(record['source_id'])
        for record in records:
            others=same_slots[(record['number'],tuple(record['path']))]
            record['source_conflict_ids']=others if len(others)>1 else []
        (output/(config['slug']+'.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2))
        unmatched=[i for i in tree['article_ids'] if i not in by_id]
        inventory_ok=not tree['missing_sections'] and not unmatched and bool(records)
        coverage['codes'].append({'code_id':code,'title':config['title'],'slug':config['slug'],'expected_articles':len(tree['article_ids']),'imported_versions':len(records),'inventory_reconciled':inventory_ok,'missing_sections':tree['missing_sections'],'missing_articles':unmatched,'drafted':sum(r['status']=='rewrite_draft' for r in records),'reviewed':sum(r['status']=='reviewed' for r in records),'retained_unchanged':sum(r['status']=='retained_unchanged' for r in records),'unprocessed':sum(r['status']=='source_imported' for r in records)})
        (output/(config['slug']+'-structure.json')).write_text(json.dumps(tree['sections'],ensure_ascii=False,indent=2))
        numbers={}
        for r in records:numbers.setdefault(r['number'],[]).append(r['source_id'])
        conflicts={n:ids for n,ids in numbers.items() if len(ids)>1}
        if conflicts:coverage['warnings'].append({'code':code,'overlapping_article_numbers':conflicts})
    (output/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
    return coverage

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--db',default=str(HERE/'corpus.sqlite'));p.add_argument('--archive');p.add_argument('--source-url');p.add_argument('--export');p.add_argument('--as-of');args=p.parse_args()
    db=open_db(args.db)
    if args.archive:
        if not args.source_url:raise SystemExit('--source-url is required')
        print('Imported source documents:',import_archive(db,args.archive,args.source_url))
    if args.export:
        if not args.as_of:raise SystemExit('--as-of is required')
        print(json.dumps(export_snapshot(db,args.as_of,Path(args.export)),ensure_ascii=False))
