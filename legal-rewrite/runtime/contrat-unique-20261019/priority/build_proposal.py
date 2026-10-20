"""Inventory and proposal only: SQLite is opened in read-only snapshot mode."""
from pathlib import Path
import collections, copy, datetime, hashlib, html, json, re, sqlite3, types

FOLDER=Path(__file__).resolve().parent
LEGAL=FOLDER.parents[2]
PROJECT=LEGAL.parent
BASE=FOLDER.parent
helper=types.ModuleType('cu_priority_proposal')
helper.__file__=str(LEGAL/'contrat_unique_priority.py')
exec(compile((FOLDER/'contrat_unique_priority.proposed.py.txt').read_text(),helper.__file__,'exec'),helper.__dict__)
sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def write(name,value): (FOLDER/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def rows(path):
    x=json.loads(path.read_text())
    return x if isinstance(x,list) else x['records']
def key(row):return row['code_id'],row['source_id']
def plain(value):return ' '.join(html.unescape(re.sub('<[^>]*>',' ',value or '')).split())
def references(value):
    return set(re.sub(r'[.\s]','',x).upper() for x in re.findall(r'\b[LRD]\.?(?:\s*\d+)(?:\s*-\s*\d+)+\b',plain(value)))

inventory_path=BASE/'inventory-travail/inventaire.json'
inventory=json.loads(inventory_path.read_text())
manifest_path=LEGAL/'runtime/radical-review-20261019.json'
manifest_bytes=manifest_path.read_bytes();manifest=json.loads(manifest_bytes)
manifest_by={key(x):x for x in manifest['prior_articles']}
db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True)
db.execute('BEGIN')
canonical={}
for code,id,number,body,source_hash in db.execute('SELECT code_id,id,number,content_xml,source_sha256 FROM articles'):
    canonical[(code,id)]={'code_id':code,'source_id':id,'number':number,'source_xml':body,'source_sha256':source_hash}
drafts={}
for code,id,source_hash,status,body in db.execute('SELECT code_id,source_id,source_sha256,status,proposed_xml FROM drafts'):
    drafts[(code,id)]={'source_sha256':source_hash,'status':status,'proposed_xml':body,'proposed_sha256':sha(body or '')}

# Explicit coordination ownership, including proposed-but-not-yet-registered packs.
packs=[('noyau45','inventory-travail/source.json','inventory-travail/answer.json'),
       ('cdd70','primary-review/cdd-repeal/edition001/source.json','primary-review/cdd-repeal/edition001/answer.json'),
       ('root48','root-coordinations/edition001/source.json','root-coordinations/edition001/answer.json'),
       ('cross12','cross-codes/edition001/source.json','cross-codes/edition001/answer.json'),
       ('cdd47','primary-review/cdd-coordinations/edition001/source.json','primary-review/cdd-coordinations/edition001/answer.json'),
       ('complement5','primary-review/cdd-complement/edition001/source.json','primary-review/cdd-complement/edition001/answer.json'),
       ('root_regulatory','root-regulatory/edition001/source.json','root-regulatory/edition001/answer.json'),
       ('cdd_senior2','primary-review/cdd-senior-complement/edition001/source.json','primary-review/cdd-senior-complement/edition001/answer.json')]
excluded={};pack_reports=[];guard_failures=[]
for label,source_name,answer_name in packs:
    source_path=BASE/source_name;answer_path=BASE/answer_name
    if not source_path.exists():raise ValueError('Missing explicitly reserved pack: '+source_name)
    source_rows=rows(source_path);answer_rows=rows(answer_path) if answer_path.exists() else []
    answers={key(a):a for a in answer_rows};counts=collections.Counter()
    for row in source_rows:
        k=key(row);current=canonical.get(k)
        if current is None or current['source_sha256']!=row['source_sha256']:
            guard_failures.append({'kind':'reserved_pack_source_changed','pack':label,'code_id':k[0],'source_id':k[1]})
        answer=answers.get(k);draft=drafts.get(k)
        status=('registered_matching_answer' if answer and draft and draft['proposed_xml']==answer['proposed_xml']
                else 'reserved_answer_not_registered' if answer else 'reserved_source_pending_answer')
        counts[status]+=1
        item={'code_id':k[0],'source_id':k[1],'number':row['number'],'source_sha256':row['source_sha256'],'pack':label,'state':status}
        if k in excluded:raise ValueError('Overlapping explicit contract packs: '+str(k))
        excluded[k]=item
    pack_reports.append({'pack':label,'source_path':str(source_path.relative_to(LEGAL)),
                         'source_file_sha256':sha(source_path.read_bytes()),'source_count':len(source_rows),
                         'answer_file_sha256':sha(answer_path.read_bytes()) if answer_path.exists() else None,
                         'states':dict(counts)})

work='LEGITEXT000006072050'
seed_numbers={x['number'] for x in excluded.values() if x['code_id']==work and x['pack'] in {'noyau45','cdd70'}}
seed_numbers |= set('L1251-1 L1251-2 L1251-6 L1251-11 L1251-32 L1251-58-1 L1251-58-2 L1251-58-3 L1251-58-4 L1251-58-5 L1251-58-6 L1254-7 L1254-8 L1254-18 L1254-20 L6222-7 L6222-7-1 L6222-16 L6222-18 L6222-18-1 L6325-5 L6325-6 L6325-7 L6325-8 L6325-9 L6325-11 L6325-13 L6325-15 L6324-3 L6324-7 L5132-5 L5132-6 L5132-11-1 L5132-15-1 L5134-24 L5134-25 L5134-25-1 L5134-26 L5134-28 L5134-69 L5134-70 L5134-71 L5134-103 L5134-104 L5134-105 L5134-106 L5134-107 L5134-115'.split())
patterns={
 'cdd_explicit':r'\b(?:CDD|contrats? (?:de travail )?à durée déterminée)\b',
 'preavis_explicit':r'\bpréavis\b',
 'essai_explicit':r'\bpériode(?:s)? d[’\x27]essai\b',
 'contrat_mission_explicit':r'\bcontrat(?:s)? de mission\b',
 'indemnite_rupture_explicit':r'\bindemnit[ée]s? (?:(?:spécifique|spéciale|légale|compensatrice)s? )?de (?:licenciement|rupture|fin de contrat|fin de mission|départ (?:à la |en )retraite|mise à la retraite)\b',
 'apprentissage_duree_limitee':r'\bcontrat d[’\x27]apprentissage.{0,75}\bdurée limitée\b',
}
core_numbers={'L1221-1','L1221-2','L1221-5-1'}|{f'L1221-{i}' for i in range(19,27)}|{f'L1231-{i}' for i in range(1,6)}|{f'L1232-{i}' for i in range(1,7)}
def classify(source,draft):
    reasons=[]
    if source['number'] in core_numbers:
        reasons.append({'kind':'explicit_contract_and_termination_core','evidence':source['number']})
    for channel,body in [('source',source['source_xml']),('draft',draft.get('proposed_xml') if draft else '')]:
        text=plain(body)
        for label,pattern in patterns.items():
            hit=re.search(pattern,text,re.I)
            if hit:
                # A notice to take leave or call a strike is not a notice to
                # terminate employment. Avoid promoting those unrelated rules.
                if label=='preavis_explicit' and not re.search(r'licenci|rupture|romp|démission|départ.{0,35}retraite|fin.{0,30}contrat',text,re.I):
                    continue
                reasons.append({'kind':label,'channel':channel,'evidence':text[max(0,hit.start()-70):min(len(text),hit.end()+110)]})
        refs=references(body)&seed_numbers
        if refs:reasons.append({'kind':'direct_reference_to_coordinated_article','channel':channel,'references':sorted(refs)})
    return reasons

outside=[]
old_keys={key(a) for a in inventory['records']}
active_work_ids={key(a) for a in rows(LEGAL/'runtime/export-source/travail.json')}
outside_scope=rows(FOLDER/'outside-scope48.json')
if len(outside_scope)!=48 or len({key(a) for a in outside_scope})!=48:
    raise ValueError('The explicitly approved supplement must contain exactly 48 identities')
outside_keys={key(a) for a in outside_scope}
for row in outside_scope:
    current=canonical.get(key(row))
    if current is None or current['source_sha256']!=row['source_sha256']:
        guard_failures.append({'kind':'approved_supplement_source_changed','code_id':row['code_id'],'source_id':row['source_id']})
for k,source in canonical.items():
    if k in outside_keys and k in active_work_ids and k not in old_keys and k not in excluded:
        reasons=classify(source,drafts.get(k))
        if reasons:outside.append({field:source[field] for field in ['code_id','source_id','number','source_sha256']}|{'reasons':reasons,'categories':['explicit_supplement_outside_initial_inventory'],'added_to_priority':True})

targets=[];filtered=[];operations=[];preserved_pending=[];counts=collections.Counter()
for old in inventory['records']+outside:
    k=key(old);source=canonical.get(k)
    if source is None or source['source_sha256']!=old['source_sha256']:
        guard_failures.append({'kind':'initial_inventory_source_changed','code_id':k[0],'source_id':k[1]})
        continue
    draft=drafts.get(k);reasons=classify(source,draft)
    if k in excluded:
        counts['explicitly_coordinated_or_reserved']+=1
        continue
    # This declaration was already wholly repealed for future cases. Its old
    # source references retirement, but a reference alone must not revive it.
    if source['number']=='L1221-18' and draft and re.match(r'Le présent article est abrogé',plain(draft['proposed_xml'])):
        reasons=[]
    if not reasons:
        filtered.append({'code_id':k[0],'source_id':k[1],'number':source['number'],'previous_categories':old['categories'],
                         'reason':'No exact CDD, notice, trial, mission, severance clause, core identity or direct coordinated reference; broad chapter/word candidate removed.'})
        continue
    target={k:source[k] for k in ['code_id','source_id','number','source_sha256']}
    prior=manifest_by.get(k)
    target.update(reasons=reasons,drafted=bool(draft and draft['proposed_xml']),manifest_status=prior.get('review_status') if prior else None,
                  current_proposed_sha256=draft['proposed_sha256'] if draft else None)
    targets.append(target)
    if not draft or not draft['proposed_xml']:
        counts['first_draft_priority']+=1
        continue
    if draft['source_sha256']!=source['source_sha256']:
        guard_failures.append({'kind':'draft_linked_to_stale_source','code_id':k[0],'source_id':k[1]});continue
    if prior and prior['review_status']=='outside_current_inventory':
        guard_failures.append({'kind':'current_target_marked_outside_inventory','code_id':k[0],'source_id':k[1]});continue
    if prior and prior['review_status']=='pending' and prior.get('source_sha256')==source['source_sha256'] and prior.get('proposed_sha256')==draft['proposed_sha256']:
        preserved_pending.append(target);counts['already_pending_guard_current']+=1;continue
    action=('reopen_completed' if prior and prior['review_status']=='completed'
            else 'refresh_pending_guard' if prior else 'append_new_review_candidate')
    counts[action]+=1
    operations.append({'code_id':k[0],'source_id':k[1],'number':source['number'],'action':action,
                       'source_sha256':source['source_sha256'],'proposed_sha256':draft['proposed_sha256'],
                       'previous_manifest_entry':copy.deepcopy(prior),
                       'reason':'The contract-unique direction requires a new full-article review of the exact clauses/references listed in the priority inventory; an earlier radical pass is not evidence of this coordination.'})

priority={'schema_version':1,'review_id':'contrat_unique_2026_10_19','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'selection':'Exact identities/clauses and direct references, not the former broad chapter inventory. Coordinated and reserved packs excluded.',
          'initial_inventory_sha256':sha(inventory_path.read_bytes()),'initial_inventory_count':len(inventory['records']),
          'targets':targets,'excluded_packs':pack_reports}
write('priority-targets.proposed.json',priority)
write('excluded-packs.json',list(excluded.values()))
write('filtered-broad-candidates.json',filtered)
write('outside-initial-inventory-leads.json',outside)
write('reopen-operations.proposed.json',operations)
write('already-pending.json',preserved_pending)
guards={'created_utc':priority['created_utc'],'database_access':'read-only snapshot transaction',
        'initial_inventory_count':len(inventory['records']),'selected_priority_targets':len(targets),
        'filtered_broad_candidates':len(filtered),'excluded_pack_records':len(excluded),
        'excluded_from_initial_inventory':counts['explicitly_coordinated_or_reserved'],
        'counts':dict(counts),'manifest_file_sha256':sha(manifest_bytes),
        'manifest_canonical_sha256':helper.object_digest(manifest),'policy_sha256':sha((LEGAL/'policy-coordinations.json').read_bytes()),
        'pack_guards':pack_reports,'guard_failures':guard_failures,'outside_initial_inventory_leads':len(outside),
        'proposal_not_applied':True,'counts_as_articles_rewritten':False}
if not guard_failures:
    proposal=helper.propose_review_manifest(manifest,operations,
        {k:s['source_sha256'] for k,s in canonical.items()},
        {k:d['proposed_sha256'] for k,d in drafts.items()},guards['manifest_canonical_sha256'])
    write('review-manifest.proposed.json',proposal)
    guards['proposed_manifest_counts']=dict(collections.Counter(x['review_status'] for x in proposal['prior_articles']))
write('guard-report.json',guards)
print(json.dumps({k:guards[k] for k in ['initial_inventory_count','selected_priority_targets','filtered_broad_candidates','excluded_pack_records','counts','guard_failures','outside_initial_inventory_leads']},ensure_ascii=False,indent=2))
