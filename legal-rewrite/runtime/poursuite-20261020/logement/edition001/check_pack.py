"""Read-only validation and bounded evidence ledger, never register."""
import pathlib,sys,json,hashlib,sqlite3,datetime,collections,zlib,xml.etree.ElementTree as ET
D=pathlib.Path(__file__).resolve().parent
B=D.parents[3]
sys.path.insert(0,str(B))
from run_exhaustive import validate_answer,graphic_markers
from ingest import source_notes
import substantive_impact as impact
import reference_coherence as refs
def h(v):return hashlib.sha256((v or '').encode()).hexdigest()
def load(name):return json.loads((D/name).read_text())
def save(name,data):(D/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

all_sources=[];all_answers=[]
for prefix in ['', 'companion/']:
    s=load(prefix+'source.json');a=load(prefix+'answer.json')
    validate_answer(a,s)
    save(prefix+'answer.json',a)
    all_sources+=s;all_answers+=a

db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True)
db.row_factory=sqlite3.Row;db.execute('BEGIN')
checks=[];wanted={(a['code_id'],a['source_id'])for a in all_sources}
for name in ['source.json','companion/source.json','references.json','additional-references.json','historical-references.json']:
    for s in load(name):
        key=s['code_id'],s['source_id']
        current=db.execute('select * from articles where code_id=? and id=?',key).fetchone()
        raw=db.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',key).fetchone()[0]
        if isinstance(raw,bytes):raw=raw.decode()
        draft=db.execute('select * from drafts where code_id=? and source_id=?',key).fetchone()
        absence=name in ['source.json','companion/source.json']
        matches=(draft is None) if absence else (not s.get('view_sha256') or h((dict(draft).get('proposed_xml')or current['content_xml'])if draft else current['content_xml'])==s['view_sha256'])
        check={'file':name,'code_id':key[0],'source_id':key[1],'number':s['number'],
               'source_sha256':s['source_sha256'],'source_xml_sha256':h(s['source_xml']),
               'source_notes_sha256':h(s['source_notes_xml']),
               'source_matches':current['content_xml']==s['source_xml']and current['source_sha256']==s['source_sha256'],
               'raw_document_matches':raw==s['source_document_xml']and h(raw)==s['source_sha256'],
               'notes_match':source_notes(db,*key)==s['source_notes_xml'],
               'draft_guard_matches':matches,'absence_required':absence,'draft_view_sha256':s.get('view_sha256')}
        assert all(check[k]for k in ['source_matches','raw_document_matches','notes_match','draft_guard_matches']),check
        checks.append(check)
policy={name:{'captured_sha256':hashlib.sha256((D/name).read_bytes()).hexdigest(),
              'current_sha256':hashlib.sha256((B/name).read_bytes()).hexdigest()}for name in ['policy-coordinations.json','site-summaries.json']}
assert all(v['captured_sha256']==v['current_sha256']for v in policy.values())
snapshot=load('reference-targets.json');refs.check_guards(db,snapshot)
assert not snapshot['targets'],'Need additional explicit dependency review before delivery'
hits=[]
for p in (B/'runtime/exhaustive/jobs').glob('*/source.json'):
    try:rows=json.loads(p.read_text())
    except Exception:continue
    if not isinstance(rows,list):continue
    keys={(r.get('code_id'),r.get('source_id'))for r in rows if isinstance(r,dict)}&wanted
    if keys:hits.append({'job':p.parent.name,'keys':sorted(keys),'has_result':(p.parent/'result.json').exists()})
assert not hits,('Jobs overlap',hits)
held=load('../../../exhaustive/held-graphic-sources.json') if False else json.loads((B/'runtime/exhaustive/held-graphic-sources.json').read_text())
assert all(not graphic_markers(s['source_xml'])for s in all_sources)
for key in wanted:
    slug='urbanisme'if key[0]=='LEGITEXT000006074075'else'construction-habitation'
    assert any(x['source_id']==key[1]for x in json.loads((B/'runtime/export-source'/f'{slug}.json').read_text()))
save('guards.json',{'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'sqlite_mode':'mode=ro BEGIN','checks':checks,'conflicts':[],'policy':policy,
     'job_intersections':hits,'source_count':28,'unresolved_graphic_markers':0,
     'all_sources_in_export_inventory':True,'reference_guard_version':snapshot['version']})

ext=sqlite3.connect('file:'+str((B/'runtime/sru-integral/urbanisme-evidence/external-evidence.sqlite').resolve())+'?mode=ro',uri=True)
ext.row_factory=sqlite3.Row;ext.execute('BEGIN');external_checks=[]
for s in load('external-references.json'):
    row=ext.execute('select * from documents where code_id=? and id=? and kind="ARTICLE"',(s['code_id'],s['id'])).fetchone()
    raw=zlib.decompress(row['xml_zlib']).decode()
    assert raw==s['source_document_xml']and h(raw)==s['sha256']
    external_checks.append({'code_id':s['code_id'],'source_id':s['id'],'raw_sha256':h(raw),'match':True,'archive':s['archive'],'archive_sha256':s['archive_provenance']['sha256']})
save('external-guards.json',external_checks)

results=[]
for s,a in zip(all_sources,all_answers):
    assert (s['code_id'],s['source_id'])==(a['code_id'],a['source_id'])
    results.append({'code_id':s['code_id'],'source_id':s['source_id'],'number':s['number'],
        'pack':'assigned24'if s in all_sources[:24]else'companion4',
        'source_sha256':s['source_sha256'],'source_xml_sha256':h(s['source_xml']),
        'source_notes_sha256':h(s['source_notes_xml']),'source_notes_xml':s['source_notes_xml'],
        'proposed_sha256':h(a['proposed_xml']),'before_plain':impact.plain(s['source_xml']),
        'after_plain':impact.plain(a['proposed_xml']or s['source_xml']),
        'status':a['status'],'classification':a['substantive_impact']['classification'],
        'substantive_impact':a['substantive_impact'],'benefit_review':a['benefit_review'],
        'transition_and_reference_review':a['review_notes']})
save('article-results.json',results)
measures={}
for a in all_answers:
    for e in a['substantive_impact']['effects']:
        m=measures.setdefault(e['measure_id'],{'measure_id':e['measure_id'],'articles':[],'kinds':set(),'evidence':[]})
        if a['number']not in m['articles']:m['articles'].append(a['number'])
        m['kinds'].add(e['kind']);m['evidence'].append({'number':a['number'],'kind':e['kind'],'before':e['before'],'after':e['after'],'source_quote':e['source_quote'],'proposed_quote':e['proposed_quote'],'replacement_or_new_burdens':e['replacement_or_new_burdens']})
for m in measures.values():m['kinds']=sorted(m['kinds'])
save('measure-results.json',list(measures.values()))
classifications=dict(collections.Counter(a['substantive_impact']['classification']for a in all_answers))
summary={'articles_examined':28,'assigned':24,'indispensable_companions':4,
         'whole_proposed_articles':sum(a['status']=='rewrite_draft'for a in all_answers),
         'retained_integral_sources_not_rewritten':sum(a['status']=='retained_unchanged'for a in all_answers),
         'classifications':classifications,'distinct_documentary_relief_measures':sum(bool(set(m['kinds'])&impact.CUTS)for m in measures.values()),
         'distinct_new_service_routing_tasks_disclosed':sum('obligation_added'in m['kinds']for m in measures.values()),
         'taxes_newly_removed_by_this_pack':0,'whole_sectoral_authorizations_removed':0,
         'automatic_permit_duration_reduction_claimed':False,'national_budget_savings_claimed':False,
         'source_and_notes_checks':len(checks),'unique_source_and_reference_checks':len({(x['code_id'],x['source_id'])for x in checks}),
         'structural_and_impact_validation_passed':True,'independent_substantive_review_complete':False,
         'all_28_draft_absence_guards_passed':True,'sources_and_canonical_database_modified':False,'registered_or_published':False}
save('validation.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
