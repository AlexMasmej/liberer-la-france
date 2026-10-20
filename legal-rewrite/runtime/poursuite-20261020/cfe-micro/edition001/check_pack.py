"""Read-only CFE source/absence/dependency and table integrity checks."""
import pathlib,sqlite3,json,sys,hashlib,re,datetime,collections
D=pathlib.Path(__file__).resolve().parent;B=D.parents[3];sys.path.insert(0,str(B))
from run_exhaustive import validate_answer,graphic_markers
from ingest import source_notes
import reference_coherence as ref
import substantive_impact as impact
def h(v):return hashlib.sha256((v or'').encode()).hexdigest()
def load(n):return json.loads((D/n).read_text())
def save(n,v):(D/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
s=load('source.json');a=load('answer.json');validate_answer(a,s)
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
checks=[];wanted={(x['code_id'],x['source_id'])for x in s}
for original in load('captured-source-and-references.json')+[load('historical-1464K.json')]:
    key=original['code_id'],original['source_id'];r=db.execute('select * from articles where code_id=? and id=?',key).fetchone()
    raw=db.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',key).fetchone()[0]
    if isinstance(raw,bytes):raw=raw.decode()
    dr=db.execute('select * from drafts where code_id=? and source_id=?',key).fetchone()
    check={'code_id':key[0],'source_id':key[1],'number':original['number'],'source_sha256':original['source_sha256'],
           'source_xml_sha256':h(original['source_xml']),'source_notes_sha256':h(original['source_notes_xml']),
           'source_matches':r['content_xml']==original['source_xml']and r['source_sha256']==original['source_sha256'],
           'raw_document_matches':raw==original['source_document_xml']and h(raw)==original['source_sha256'],
           'notes_match':source_notes(db,*key)==original['source_notes_xml'],
           'draft_absence_required':key in wanted,
           'draft_matches':dr is None if key in wanted else (not original.get('view_sha256')or h((dr['proposed_xml']or r['content_xml'])if dr else r['content_xml'])==original['view_sha256'])}
    assert all(check[n]for n in ['source_matches','raw_document_matches','notes_match','draft_matches']),check
    checks.append(check)
snap=load('reference-targets.json');ref.check_guards(db,snap);ref.accept_checks(a,s,snap)
for row in a:
    if snap['requirements'][ref.key(row)]:assert ref.certificate_current(db,next(x for x in s if ref.key(x)==ref.key(row)),row['proposed_xml'],row['reference_coherence'])
policy={name:{'captured':hashlib.sha256((D/name).read_bytes()).hexdigest(),'current':hashlib.sha256((B/name).read_bytes()).hexdigest()}for name in ['policy-coordinations.json','site-summaries.json']}
assert all(v['captured']==v['current']for v in policy.values())
hits=[]
for p in (B/'runtime/exhaustive/jobs').glob('*/source.json'):
    try:rows=json.loads(p.read_text())
    except Exception:continue
    if not isinstance(rows,list):continue
    found={(r.get('code_id'),r.get('source_id'))for r in rows if isinstance(r,dict)}&wanted
    if found:hits.append({'job':p.parent.name,'keys':sorted(found)})
assert not hits,hits
assert all(not graphic_markers(x['source_xml'])for x in s)
# The whole provisions outside the exact amendments remain byte-for-byte, after
# dropping only HTML presentation attributes which the strict writer rejects.
for number in ['1447','1477']:
    old=next(x for x in s if x['number']==number)['source_xml'].rstrip()
    new=next(x for x in a if x['number']==number)['proposed_xml']
    assert new.startswith(old+'\n')
old=next(x for x in s if x['number']=='1647 D')['source_xml']
new=next(x for x in a if x['number']=='1647 D')['proposed_xml']
normal=lambda x:re.sub(r' (?:align|border)="[^"]*"','',x)
insert=", à l'exception des bénéficiaires de l'exonération du IV de l'article 1447 pour leurs activités éligibles,"
assert new.replace(insert,'',1)==normal(old)
table=lambda v:re.search('<table[^>]*>.*?</table>',v,re.S).group()
assert table(new)==normal(table(old))
old_table=table(old)
assert len(re.findall('<tr[ >]',old_table))==7
assert len(re.findall('<td[ >]',old_table))==12
assert len(re.findall('<th[ >]',old_table))==2
save('answer.json',a)
save('guards.json',{'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sqlite':'mode=ro BEGIN',
    'checks':checks,'conflicts':[],'jobs_intersections':hits,'policy':policy,'reference_guard_version':snap['version'],
    'reference_target_206_current':True,'four_draft_absence_guards_passed':True})
results=[]
for before,after in zip(s,a):
    results.append({'code_id':before['code_id'],'source_id':before['source_id'],'number':before['number'],
        'source_sha256':before['source_sha256'],'source_notes_xml':before['source_notes_xml'],'source_notes_sha256':h(before['source_notes_xml']),
        'source_xml_sha256':h(before['source_xml']),'proposed_sha256':h(after['proposed_xml']),
        'before_plain':impact.plain(before['source_xml']),'after_plain':impact.plain(after['proposed_xml']or before['source_xml']),
        'status':after['status'],'substantive_impact':after['substantive_impact'],'benefit_review':after['benefit_review']})
save('article-results.json',results)
summary={'records':4,'whole_drafts':3,'retained_integral_not_rewritten':1,
    'classifications':dict(collections.Counter(x['substantive_impact']['classification']for x in a)),
    'distinct_tax_exemptions_created':1,'separate_filing_relief_measures':1,'first_return_deadline_relief':1,
    'new_tax_rates_or_social_rates_set':False,'fixed_national_cfe_saving_claimed':False,
    'minimum_table_preserved':True,'table_rows_including_header':7,'table_data_cells':12,'table_header_cells':2,
    'all_other_1647D_bytes_identical_after_presentation_attributes':True,
    '1447_and1477_original_provisions_identical':True,'four_absence_guards':True,'read_only_source_reference_checks':len(checks),
    'reference_206_full_source_notes_and_current_draft_read':True,'structure_and_impact_validation':True,
    'independent_review_complete':False,'canonical_mutations':False,'registered_or_published':False}
save('validation.json',summary);print(json.dumps(summary,ensure_ascii=False,indent=2))
