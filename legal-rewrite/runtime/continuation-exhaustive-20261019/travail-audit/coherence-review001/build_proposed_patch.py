"""Produce separate corrective files/diffs from immutable reviewed copies."""
from pathlib import Path
import difflib,hashlib,json

P=Path(__file__).resolve().parent
source=(P/'reference_coherence.py.baseline.txt').read_text()
source=source.replace('import hashlib,json,re,sqlite3','import hashlib,html,json,re,sqlite3')
source=source.replace('VERSION=1','VERSION=2')
start=source.index('def token_refs(body):')
end=source.index('\ndef requirements(',start)
source=source[:start]+'''def token_refs(body):
    result=set(references(body or ''))
    plain=html.unescape(re.sub('<[^>]+>',' ',body or ''))
    article=r'[LRDA]\\.?\\s*\\d+(?:\\s*-\\s*\\d+[A-Za-z]*)+'
    for match in re.finditer(r'(?P<first>'+article+r')\\s+à\\s+(?P<last>'+article+r'|\\d+)\\b',plain,re.I):
        first=normalize(match.group('first'));last=normalize(match.group('last'))
        family,begin=first.rsplit('-',1)
        if last.isdigit():last=family+'-'+last
        other_family,finish=last.rsplit('-',1)
        if family!=other_family or not begin.isdigit() or not finish.isdigit():continue
        if 0<=int(finish)-int(begin)<=100:
            result.update(family+'-'+str(n) for n in range(int(begin),int(finish)+1))
    return result
''' +source[end:]
source=source.replace("bodies=[article['source_xml'],(article.get('previous_draft') or {}).get('proposed_xml') or '',body or '']",
                      "bodies=[article['source_xml'],article.get('source_notes_xml') or '',(article.get('previous_draft') or {}).get('proposed_xml') or '',body or '']")
source=source.replace("'view_kind':'proposal' if old and old[1] else 'official_source_only','view_sha256':digest(body)}",
                      "'view_kind':'proposal' if old and old[1] else 'official_source_only','view_sha256':digest(body),\n            'source_xml_sha256':digest(src[1]),'source_notes_sha256':digest(source_notes(db,code,source_id))}")
source=source.replace("'view_sha256':digest(proposal if proposal else src[2])}",
                      "'view_sha256':digest(proposal if proposal else src[2]),\n            'source_xml_sha256':digest(src[2]),'source_notes_sha256':digest(source_notes(db,code,source_id))}")
source=source.replace("'requirements':needs,'targets':{k:view(db,k) for k in sorted(wanted)},",
                      "'requirements':needs,'targets':{k:view(db,k) for k in sorted(wanted)},\n            'referrers':{key(a):referrer_source(db,key(a)) for a in articles if needs[key(a)]},")
source=source.replace("('code_id','source_id','source_sha256','view_kind','view_sha256')", "('code_id','source_id','source_sha256','view_kind','view_sha256','source_xml_sha256','source_notes_sha256')")
source=source.replace('def check_guards(db,snapshot):', '''def referrer_source(db,identifier):
    current=state(db,identifier)
    return {k:current[k] for k in ('code_id','source_id','source_sha256','source_xml_sha256','source_notes_sha256')}

def assessment_digest(checks):
    return digest(json.dumps(checks,ensure_ascii=False,sort_keys=True,separators=(',',':')))

def assessments_current(checks,targets):
    if not isinstance(checks,list):return False
    found=set()
    for item in checks:
        if not isinstance(item,dict):return False
        identifier=item.get('target_key')
        if identifier in found or identifier not in targets:return False
        if item.get('view_sha256')!=targets[identifier]['view_sha256']:return False
        if not isinstance(item.get('assessment'),str) or len(item['assessment'].strip())<80:return False
        found.add(identifier)
    return found==set(targets)

def check_guards(db,snapshot):
    if snapshot.get('version')!=VERSION:raise ValueError('Reference snapshot version changed; recapture')
    for identifier,expected in snapshot.get('referrers',{}).items():
        if referrer_source(db,identifier)!=expected:raise ValueError('Referrer source changed during drafting: '+identifier)''')
before="""        row['reference_coherence']={'version':VERSION,'referrer_sha256':digest(row['proposed_xml']),
            'targets':{k:guard(snapshot['targets'][k]) for k in sorted(needed)},'semantic_review_by_jurist':False}"""
after="""        assessments=[{field:found[k][field] for field in ('target_key','view_sha256','assessment')} for k in sorted(needed)]
        row['reference_coherence']={'version':VERSION,'referrer_sha256':digest(row['proposed_xml']),
            'referrer_source':snapshot['referrers'][key(row)],
            'targets':{k:guard(snapshot['targets'][k]) for k in sorted(needed)},
            'assessments':assessments,'assessments_sha256':assessment_digest(assessments),
            'semantic_review_by_jurist':False}"""
assert source.count(before)==1
source=source.replace(before,after)
before="""    if not isinstance(guards,dict) or set(guards)!=needed:return False
    return all(state(db,k)==guards[k] for k in needed)"""
after="""    if not isinstance(guards,dict) or set(guards)!=needed:return False
    if certificate.get('semantic_review_by_jurist') is not False:return False
    if certificate.get('referrer_source')!=referrer_source(db,key(article)):return False
    checks=certificate.get('assessments')
    if not assessments_current(checks,guards):return False
    if certificate.get('assessments_sha256')!=assessment_digest(checks):return False
    return all(state(db,k)==guards[k] for k in needed)"""
assert source.count(before)==1
source=source.replace(before,after)

prior=(P/'review_prior.py.baseline.txt').read_text()
prior=prior.replace('from register_batches import writer_lock,register','from register_batches import writer_lock,register,_register as register_locked')
before="""                (folder/f'{index:05d}.json').write_text(json.dumps(legacy,ensure_ascii=False,indent=2)+'\\n')
        finally:db.close()
    db=open_db(HERE/'corpus.sqlite')
    try:register(db,HERE/'batches',True)
    finally:db.close()
    with writer_lock():"""
after="""                (folder/f'{index:05d}.json').write_text(json.dumps(legacy,ensure_ascii=False,indent=2)+'\\n')
            # Keep the same non-reentrant writer lock from target checks through
            # canonical registration. The public register() wrapper would lock
            # again; use its already-locked implementation here.
            register_locked(db,HERE/'batches',True)
        finally:db.close()
    with writer_lock():"""
assert prior.count(before)==1
prior=prior.replace(before,after)

report={}
for name,proposed in [('reference_coherence.py',source),('review_prior.py',prior)]:
    original=(P/(name+'.baseline.txt')).read_text()
    compile(proposed,name,'exec')
    (P/(name+'.proposed.txt')).write_text(proposed)
    (P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),proposed.splitlines(True),fromfile='a/legal-rewrite/'+name,tofile='b/legal-rewrite/'+name)))
    report[name]={'reviewed_sha256':hashlib.sha256(original.encode()).hexdigest(),'proposed_sha256':hashlib.sha256(proposed.encode()).hexdigest()}
(P/'proposed-file-hashes.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
