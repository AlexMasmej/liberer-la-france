"""Frozen contract-law dependencies; audit evidence is not a jurist's approval.

Only local canonical material is read. This module neither changes sources nor
registers proposals. Every certificate is tied to full source/proposal hashes.
"""
from pathlib import Path
from functools import lru_cache
import hashlib,html,json,re,sqlite3
import xml.etree.ElementTree as ET
from register_batches import references
from ingest import source_notes

HERE=Path(__file__).resolve().parent
WORK='LEGITEXT000006072050'
BASE={'L1221-2','L1234-1','L1234-9'}
VERSION=3

def digest(value):return hashlib.sha256((value or '').encode()).hexdigest()
def key(a):return a['code_id']+'|'+a.get('source_id',a.get('id',''))
def normalize(value):return re.sub(r'[\s.]','',value).upper()

def policy_state():
    return {name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() if (HERE/name).exists() else 'missing'
            for name in ('policy-coordinations.json','site-summaries.json')}

@lru_cache(maxsize=1)
def focus():
    folder=HERE/'runtime/contrat-unique-20261019/priority'
    rows=json.loads((folder/'excluded-packs.json').read_text())+json.loads((folder/'priority-targets.proposed.json').read_text())['targets']
    extra=HERE/'reference-focus-extra.json'
    if extra.exists():rows+=json.loads(extra.read_text())
    return {key(a):a for a in rows}

_LOOKUPS={}
def lookup(catalog):
    prior=_LOOKUPS.get(id(catalog))
    if prior and prior[0] is catalog:return prior[1]
    numbered={};qualified={}
    for k,a in catalog.items():
        n=normalize(a['number']);numbered.setdefault(n,[]).append((k,a));qualified.setdefault((a['code_id'],n),[]).append(k)
    value=(numbered,qualified)
    if len(_LOOKUPS)>8:_LOOKUPS.clear()
    _LOOKUPS[id(catalog)]=(catalog,value)
    return value

def token_refs(body):
    result=set(references(body or ''))
    plain=html.unescape(re.sub('<[^>]+>',' ',body or ''))
    article=r'[LRDA]\.?\s*\d+(?:\s*-\s*\d+[A-Za-z]*)+'
    for match in re.finditer(r'(?P<first>'+article+r')\s+à\s+(?P<last>'+article+r'|\d+)\b',plain,re.I):
        first=normalize(match.group('first'));last=normalize(match.group('last'))
        family,begin=first.rsplit('-',1)
        if last.isdigit():last=family+'-'+last
        other_family,finish=last.rsplit('-',1)
        if family!=other_family or not begin.isdigit() or not finish.isdigit():continue
        if 0<=int(finish)-int(begin)<=100:
            result.update(family+'-'+str(n) for n in range(int(begin),int(finish)+1))
    return result

def requirements(article,body=None,catalog=None,db=None):
    catalog=focus() if catalog is None else catalog
    bodies=[article['source_xml'],article.get('source_notes_xml') or '',(article.get('previous_draft') or {}).get('proposed_xml') or '',body or '']
    refs=set().union(*(token_refs(b) for b in bodies));own=article['code_id'];wanted=set()
    numbered,qualified=lookup(catalog)
    for ref in refs:
        for target_key,a in numbered.get(ref,[]):
            if a['code_id']==own or a['code_id']==WORK:wanted.add(target_key)
    employment=re.search(r'\bsalari|\bemploy|\bapprenti|\blicenci|\bCDD\b|\bCDI\b',' '.join(bodies),re.I)
    contract=re.search(r'contrat.{0,45}(?:durée|unique|travail)|préavis|indemnit.{0,50}(?:rupture|licenci|ancienneté)',' '.join(bodies),re.I)
    if key(article) in catalog or (employment and contract) or wanted:
        wanted.update(k for number in BASE for k in qualified.get((WORK,number),[]))
    if db is not None and re.fullmatch(r'LEGITEXT\d{12}',own):
        row=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(own,article['source_id'])).fetchone()
        if row:
            root=ET.fromstring(row[0])
            for link in root.findall('./LIENS/LIEN'):
                if link.get('sens')!='source' or link.get('typelien')!='CITATION':continue
                identifier=link.get('cidtexte','')+'|'+link.get('id','')
                if identifier in catalog:wanted.add(identifier)
                elif link.get('cidtexte'):
                    candidates=qualified.get((link.get('cidtexte'),normalize(link.get('num',''))),[])
                    if len(candidates)==1:wanted.add(candidates[0])
    wanted.discard(key(article))
    return wanted

def state(db,identifier):
    code,source_id=identifier.split('|',1)
    src=db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',(code,source_id)).fetchone()
    if not src:raise ValueError('Missing canonical reference target '+identifier)
    old=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',(code,source_id)).fetchone()
    if old and old[0]!=src[0]:raise ValueError('Reference target source mismatch '+identifier)
    body=old[1] if old and old[1] else src[1]
    return {'code_id':code,'source_id':source_id,'source_sha256':src[0],
            'view_kind':'proposal' if old and old[1] else 'official_source_only','view_sha256':digest(body),
            'source_xml_sha256':digest(src[1]),'source_notes_sha256':digest(source_notes(db,code,source_id))}

def view(db,identifier):
    code,source_id=identifier.split('|',1)
    src=db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',(code,source_id)).fetchone()
    if not src:raise ValueError('Missing canonical reference target '+identifier)
    old=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',(code,source_id)).fetchone()
    if old and old[0]!=src[1]:raise ValueError('Reference target draft has a different canonical source '+identifier)
    proposal=old[1] if old else None
    return {'code_id':code,'source_id':source_id,'number':src[0],'source_sha256':src[1],
            'source_xml':src[2],'source_notes_xml':source_notes(db,code,source_id),
            'proposed_xml':proposal,'view_kind':'proposal' if proposal else 'official_source_only',
            'view_sha256':digest(proposal if proposal else src[2]),
            'source_xml_sha256':digest(src[2]),'source_notes_sha256':digest(source_notes(db,code,source_id))}

def capture(db,articles,answers=None,catalog=None):
    by_key={key(a):a for a in answers or []};needs={}
    for article in articles:
        body=by_key.get(key(article),{}).get('proposed_xml')
        needs[key(article)]=sorted(requirements(article,body,catalog,db))
    wanted=set().union(*(set(v) for v in needs.values())) if needs else set()
    return {'version':VERSION,'scope':'contract_unique_and_related_severance',
            'policy_sha256':policy_state(),
            'requirements':needs,'targets':{k:view(db,k) for k in sorted(wanted)},
            'referrers':{key(a):referrer_source(db,key(a)) for a in articles if needs[key(a)]},
            'semantic_review_by_jurist':False}

def guard(target):
    return {k:target[k] for k in ('code_id','source_id','source_sha256','view_kind','view_sha256','source_xml_sha256','source_notes_sha256')}

def referrer_source(db,identifier):
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
    if snapshot.get('policy_sha256')!=policy_state():raise ValueError('Reference policy changed during drafting; recapture')
    for identifier,expected in snapshot.get('referrers',{}).items():
        if referrer_source(db,identifier)!=expected:raise ValueError('Referrer source changed during drafting: '+identifier)
    for identifier,target in snapshot.get('targets',{}).items():
        current=state(db,identifier)
        if guard(current)!=guard(target):raise ValueError('Reference target changed during drafting: '+identifier)

def accept_checks(rows,expected,snapshot,catalog=None):
    before={key(a):a for a in expected}
    for row in rows:
        needed=requirements(before[key(row)],row['proposed_xml'],catalog)|set(snapshot['requirements'].get(key(row),[]))
        if not needed:continue
        if not needed<=set(snapshot['targets']):raise ValueError('New reference needs its complete target text; refresh reference-targets.json')
        checks=row.get('reference_checks')
        if not isinstance(checks,list):raise ValueError('Explicit reference_checks required for contract-law dependencies')
        found={}
        for item in checks:
            if not isinstance(item,dict):raise ValueError('Malformed reference check')
            identifier=item.get('target_key')
            if identifier in found:raise ValueError('Duplicate reference check')
            if identifier not in needed:raise ValueError('Unexpected reference target in assessment')
            if item.get('view_sha256')!=snapshot['targets'][identifier]['view_sha256']:raise ValueError('Reference assessment uses an outdated target')
            if not isinstance(item.get('assessment'),str) or len(item['assessment'].strip())<80:raise ValueError('Reference assessment must explain the actual rule, transition or inapplicability')
            found[identifier]=item
        if set(found)!=needed:raise ValueError('A required reference has no explicit assessment')
        assessments=[{field:found[k][field] for field in ('target_key','view_sha256','assessment')} for k in sorted(needed)]
        row['reference_coherence']={'version':VERSION,'referrer_sha256':digest(row['proposed_xml']),
            'policy_sha256':dict(snapshot['policy_sha256']),
            'referrer_source':snapshot['referrers'][key(row)],
            'targets':{k:guard(snapshot['targets'][k]) for k in sorted(needed)},
            'assessments':assessments,'assessments_sha256':assessment_digest(assessments),
            'semantic_review_by_jurist':False}
    return rows

def certificate_current(db,article,body,certificate,catalog=None):
    needed=requirements(article,body,catalog,db)
    if not needed:return True
    if not isinstance(certificate,dict) or certificate.get('version')!=VERSION or certificate.get('referrer_sha256')!=digest(body):return False
    if certificate.get('policy_sha256')!=policy_state():return False
    guards=certificate.get('targets')
    if not isinstance(guards,dict) or set(guards)!=needed:return False
    if certificate.get('semantic_review_by_jurist') is not False:return False
    if certificate.get('referrer_source')!=referrer_source(db,key(article)):return False
    checks=certificate.get('assessments')
    if not assessments_current(checks,guards):return False
    if certificate.get('assessments_sha256')!=assessment_digest(checks):return False
    return all(state(db,k)==guards[k] for k in needed)

PROMPT='''
RENVOIS AU CONTRAT UNIQUE : lis reference-targets.json en entier, pour les cibles applicables à tes articles. Ce fichier contient les textes officiels entiers, leurs notes et les propositions actuelles ; une proposition n'est pas le droit en vigueur. Les identifiants dans requirements désignent les cibles à vérifier pour chaque article source. Vérifie le champ de chaque renvoi, les alinéas/subdivisions réellement visés, les anciens contrats, les avantages futurs et les exceptions spéciales. Un renvoi à un code extérieur ou à un régime public ne doit pas être attribué artificiellement au contrat privé : explique l'inapplicabilité lorsqu'elle existe.
Pour chaque objet answer.json concerné, ajoute reference_checks : une liste d'objets target_key, view_sha256, assessment. Couvre toutes les cibles requises. Reprends leurs empreintes EXACTES et donne pour chaque cible au moins80caractères d'analyse spécifique : règle réellement visée, cohérence/rectification du renvoi, condition d'ancienneté et de notification ou distinction d'une ancienne règle/situation spéciale. Pas de simple « vérifié ». Tout nouveau renvoi à une cible non fournie doit être signalé ; n'invente pas son contenu. La vérification automatique ne constitue aucune approbation juridique.
'''
