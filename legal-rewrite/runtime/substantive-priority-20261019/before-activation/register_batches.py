"""Validate authored full-article batches, then register in one transaction.

Integrity checks do not constitute legal review. Completion is never inferred
from source coverage or from the mere existence of a batch file.
"""
from pathlib import Path
import argparse,hashlib,html,json,re,sqlite3,sys,fcntl
from contextlib import contextmanager
from html.parser import HTMLParser
from ingest import HERE,open_db,source_notes,source_evidence
from source_assets import verified_image,graphic_markers,load_companions,recovery_complete,recovered_content_present

FIELDS={'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes'}
ALLOWED={'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote','img'}

class Markup(HTMLParser):
    def __init__(self,strict=True):super().__init__(convert_charrefs=True);self.words=[];self.tables=0;self.rows=0;self.cells=0;self.stack=[];self.strict=strict
    def handle_starttag(self,tag,attrs):
        if self.strict and tag not in ALLOWED:raise ValueError('Unexpected HTML tag: '+tag)
        if self.strict and tag=='img':
            values=dict(attrs)
            if set(values)!={'src','alt'} or not values['alt'] or len(attrs)!=2:raise ValueError('Formula image needs only a local src and descriptive alt')
            verified_image(values['src'])
            return
        for name,value in attrs:
            if self.strict and (name not in {'rowspan','colspan'} or not value or not value.isdigit()):raise ValueError('Unexpected HTML attribute: '+name)
        if tag=='table':self.tables+=1
        if tag=='tr':self.rows+=1
        if tag in {'td','th'}:self.cells+=1
        if self.strict and tag!='br':self.stack.append(tag)
    def handle_endtag(self,tag):
        if not self.strict or tag in {'br','img'}:return
        if not self.stack or self.stack.pop()!=tag:raise ValueError('Unbalanced HTML: '+tag)
    def handle_data(self,data):self.words.append(data)
    def result(self):
        if self.stack:raise ValueError('Unclosed HTML tags')
        return ' '.join(' '.join(self.words).split())

def text(value,strict=True):
    parser=Markup(strict);parser.feed(value);return parser.result(),parser.tables

def references(value):
    value=html.unescape(re.sub('<[^>]*>',' ',value))
    return sorted(set(re.sub(r'\s+|\.', '',s).upper() for s in re.findall(r'\b(?:LO|[LRDA])\.?\s*\d{1,5}(?:\s*-\s*\d+[A-Za-z]*)+',value,re.I)))

def full_repeal(row):
    """A deliberate repeal may remove the norm and its tables, never its source."""
    if row.get('change_type')!='full_repeal':return False
    policy_id='editorial_direction_2026_10_19'
    policy=HERE/'policy-coordinations.json'
    if row.get('repeal_policy_id')!=policy_id or not policy.exists() or not json.loads(policy.read_text()).get(policy_id):
        raise ValueError('Full repeal requires the explicit author policy')
    body,_=text(row.get('proposed_xml') or '')
    if not re.match(r'(?:Le présent article est abrogé|Abrogé)\b',body,re.I):
        raise ValueError('Full repeal needs an operative repeal provision')
    if len(row.get('repeal_scope','').strip())<30:
        raise ValueError('Full repeal needs an article-specific explanation of the removed duties')
    return True

def authorized_reduction(row):
    if full_repeal(row):return True
    if row.get('change_type')!='normative_reduction':return False
    policy_id='editorial_direction_2026_10_19'
    policy=HERE/'policy-coordinations.json'
    if row.get('reform_policy_id')!=policy_id or not policy.exists() or not json.loads(policy.read_text()).get(policy_id):
        raise ValueError('Normative reduction requires the explicit author policy')
    removed=row.get('removed_provisions')
    if not isinstance(removed,list) or not removed or any(not isinstance(item,str) or len(item.strip())<30 for item in removed):
        raise ValueError('Normative reduction must identify the removed provisions')
    return True

def validate_batches(db,root):
    records={};diagnostics=[];batch_files=[]
    companions=load_companions()
    registry_path=HERE/'registered-batches.json'
    registry=json.loads(registry_path.read_text()) if registry_path.exists() else {}
    for path in sorted(root.glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
        rows=json.loads(path.read_text())
        if not isinstance(rows,list):raise ValueError(f'{path}: expected an article array')
        batch_files.append({'file':str(path.relative_to(HERE)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'articles':len(rows)})
        for row in rows:
            if FIELDS-set(row):raise ValueError(f'{path}: missing fields {FIELDS-set(row)}')
            retained=row.get('status')=='retained_unchanged'
            for field in FIELDS:
                if field=='proposed_xml' and retained and row[field] is None:continue
                if not isinstance(row[field],str) or not row[field].strip():raise ValueError(f'{path}: empty field {field}')
            key=(row['code_id'],row['source_id'])
            if key in records:raise ValueError('Duplicate authored article across batches: '+str(key))
            source=db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
            if not source:raise ValueError('Unknown source '+str(key))
            number,sha,body,start,end=source
            if sha!=row['source_sha256'] or number!=row['number']:raise ValueError('Source version or number mismatch: '+str(key))
            original,source_tables=text(body,False)
            proposed,tables=text(row['proposed_xml'] or '')
            repealed=full_repeal(row)
            reduced=authorized_reduction(row)
            if retained:
                if original not in {'Réservé.','Réservé','(Réservé)'} or row['proposed_xml'] is not None:raise ValueError('Only explicit non-normative reserved slots may be retained')
            elif not proposed:raise ValueError('Empty draft '+str(key))
            elif proposed==original:raise ValueError('Unchanged source cannot count as rewritten: '+str(key))
            if re.search(r'\[\s*(?:\.\.\.|…|à compléter|texte inchangé)\s*\]|<placeholder>|TODO',proposed,re.I):raise ValueError('Placeholder in article '+str(key))
            if not reduced and source_tables and tables<source_tables:raise ValueError('Source table missing from draft: '+str(key))
            source_parser=Markup(False);source_parser.feed(body)
            draft_parser=Markup();draft_parser.feed(row['proposed_xml'] or '');draft_parser.result()
            if not reduced and (draft_parser.rows<source_parser.rows or draft_parser.cells<source_parser.cells):raise ValueError('Source table rows or cells missing from draft: '+str(key))
            if graphic_markers(body) and not repealed:
                companion=companions.get(key)
                if not recovery_complete(body,companion):raise ValueError('Normative graphic source is unresolved: '+str(key))
                if not recovered_content_present(row['proposed_xml'] or '',companion):raise ValueError('Recovered formula content is missing from draft: '+str(key))
            ratio=len(proposed)/max(1,len(original))
            if reduced:diagnostics.append({'source_id':key[1],'number':number,'check':'explicit_normative_reduction','scope':row.get('repeal_scope') or row['removed_provisions']})
            if not retained and (ratio<.45 or ratio>2.5):diagnostics.append({'source_id':key[1],'number':number,'check':'length_change','ratio':round(ratio,2)})
            original_refs=references(body);draft_refs=references(row['proposed_xml'])
            if original_refs!=draft_refs:diagnostics.append({'source_id':key[1],'number':number,'check':'references_changed','removed':sorted(set(original_refs)-set(draft_refs)),'added':sorted(set(draft_refs)-set(original_refs))})
            existing=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
            if existing and existing!=(sha,row['proposed_xml']):
                previous=registry.get('|'.join(key))
                if not previous or existing[0]!=sha or hashlib.sha256((existing[1] or '').encode()).hexdigest()!=previous['proposed_sha256']:
                    raise ValueError('Refusing to overwrite an existing different draft: '+str(key))
            records[key]=(row,body,start,end)
    return records,diagnostics,batch_files

@contextmanager
def writer_lock():
    with (HERE/'draft-writer.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        try:yield
        finally:fcntl.flock(lock,fcntl.LOCK_UN)


def register(db,root,commit=False):
    with writer_lock():return _register(db,root,commit)


def _register(db,root,commit=False):
    records,diagnostics,files=validate_batches(db,root)
    report={'validation':'integrity only; not legal review','authored_articles':len(records),'batches':files,'checks_requiring_editorial_review':diagnostics,'registered':False}
    if commit:
        for item in files:
            if hashlib.sha256((HERE/item['file']).read_bytes()).hexdigest()!=item['sha256']:
                raise ValueError('Batch changed during validation; retry: '+item['file'])
        try:
            db.execute('BEGIN IMMEDIATE')
            for key,(row,body,start,end) in records.items():
                db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?) ON CONFLICT(code_id,source_id) DO UPDATE SET status=excluded.status,proposed_xml=excluded.proposed_xml,reason=excluded.reason,review_notes=excluded.review_notes',(*key,row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes']))
                notes=source_notes(db,*key)
                db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?) ON CONFLICT(code_id,source_id) DO NOTHING',(*key,source_evidence(body,notes),start,end))
            db.commit()
        except Exception:
            db.rollback();raise
        report['registered']=True
        registry={ '|'.join(key):{'source_sha256':row['source_sha256'],'proposed_sha256':hashlib.sha256((row['proposed_xml'] or '').encode()).hexdigest()} for key,(row,body,start,end) in records.items() }
        registry_file=HERE/'registered-batches.json'
        temporary=registry_file.with_suffix('.json.tmp');temporary.write_text(json.dumps(registry,ensure_ascii=False,indent=2));temporary.replace(registry_file)
    (HERE/'batch-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='batches'},ensure_ascii=False,indent=2))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--commit',action='store_true');args=parser.parse_args()
    register(open_db(HERE/'corpus.sqlite'),HERE/'batches',args.commit)
