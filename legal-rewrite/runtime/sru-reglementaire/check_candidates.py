import json,sqlite3,sys,hashlib,re
from pathlib import Path
sys.path.insert(0,'legal-rewrite')
from register_batches import text,Markup,full_repeal,authorized_reduction,FIELDS,references
from ingest import source_notes
base=Path('legal-rewrite');path=base/'runtime/sru-reglementaire/articles.candidates.json'
rows=json.loads(path.read_text());sources=json.loads((base/'runtime/sru-reglementaire/sources.json').read_text())+[json.loads((base/'runtime/sru-reglementaire/r445-24.source.json').read_text())]
src={(s['code_id'],s['source_id']):s for s in sources}
c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True)
c.row_factory=sqlite3.Row
checks=[];numbers=set()
for r in rows:
 assert not FIELDS-set(r)
 key=r['code_id'],r['source_id'];a=dict(c.execute('select * from articles where code_id=? and id=?',key).fetchone())
 assert (a['source_sha256'],a['number'])==(r['source_sha256'],r['number'])
 assert a['content_xml']==src[key]['content_xml']
 assert source_notes(c,*key)==src[key]['source_notes_xml']
 assert r['number'] not in numbers;numbers.add(r['number'])
 original,ot=text(a['content_xml'],False);draft,dt=text(r['proposed_xml'])
 assert draft and draft!=original
 assert not re.search(r'\[\s*(?:\.\.\.|…|à compléter|texte inchangé)\s*\]|<placeholder>|TODO',draft,re.I)
 assert ot==dt==0
 reduced=authorized_reduction(r);repealed=full_repeal(r)
 if repealed:assert 'V de l’article L. 302-5' in draft or "V de l'article L. 302-5" in draft
 existing=c.execute('select * from drafts where code_id=? and source_id=?',key).fetchone()
 checks.append({'number':r['number'],'source_id':r['source_id'],'source_sha256':r['source_sha256'],'source_sha256_matches_canonical':True,'source_body_matches_snapshot':True,'source_notes_match_snapshot':True,'source_notes_empty':not bool(src[key]['source_notes_xml'].strip()),'proposed_sha256':hashlib.sha256(r['proposed_xml'].encode()).hexdigest(),'change_type':r.get('change_type','coordination'),'html_valid':True,'tables_source':ot,'tables_proposed':dt,'references_original':references(a['content_xml']),'references_proposed':references(r['proposed_xml']),'previous_draft_present_now':bool(existing),'previous_draft_sha256':hashlib.sha256((existing['proposed_xml'] or '').encode()).hexdigest() if existing else None,'source_chars':len(original),'proposed_chars':len(draft)})
assert len(rows)==17 and sum(full_repeal(r) for r in rows)==12
# Exact retained boundaries and conditions, independent of wording of the authored paragraphs.
by={r['number']:text(r['proposed_xml'])[0] for r in rows}
assert all(v in by['R302-15'] for v in ['III.-','III bis.-','par trois','partie entière','R. 151-1','chaque terrain familial locatif correspond à un logement équivalent'])
assert 'trois mois' in by['R302-7']
assert all(v in by['R302-19'] for v in ['par neuvième','de mars à novembre','ne constituent pas','ni exigibilité anticipée'])
assert all(v in by['R302-16-2'] for v in ['10 000 euros','5 000 euros',"d'Ile-de-France", "Provence-Alpes-Côte d'Azur",'par logement et par an'])
assert 'délai de deux ans expire à compter' in by['R302-18']
assert all(v in by['R445-24'] for v in ['moins de 50 %','au moins égale à 50 % et inférieure à 100 %','totalité du patrimoine','R. 445-36','III de l\'article R. 302-15'])
assert all(re.search(r'(?<!\d)'+str(n)+'°',by['R362-2']) for n in range(1,22))
assert '5° Abrogé.' in by['R362-2']
assert 'L. 302-9' not in by['R362-2']
assert 'R. 445-37' not in by['R445-24']
assert 'note est vide' not in next(r['review_notes'] for r in rows if r['number']=='R445-24')
assert '1er janvier 2022' in next(r['review_notes'] for r in rows if r['number']=='R445-24')
assert 'L. 302-9-1' not in by['R362-2']
report={'validation':'Contrôle matériel des seuls candidats ; aucune inscription ni validation juridique.','articles':len(rows),'full_repeals':12,'targeted_reductions':5,'coordination_only':0,'canonical_database_opened_read_only':True,'sources_immutable':True,'registered':False,'published':False,'candidate_file':str(path),'candidate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'checks':checks,'remaining_issues':[{'article':'L302-5 / L302-9','issue':'Les candidats doivent être intégrés avec les propositions législatives coordonnées IV/V de L302-5 et le bilan général de L302-9, non comme dispositions isolées.'}]}
out=base/'runtime/sru-reglementaire/checks.json';tmp=out.with_suffix('.json.tmp');tmp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');tmp.replace(out)
print(json.dumps({k:v for k,v in report.items() if k not in ['checks']},ensure_ascii=False,indent=2))
