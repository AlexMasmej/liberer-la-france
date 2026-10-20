from pathlib import Path
import json,hashlib,shutil,copy,sys,sqlite3
B=Path('legal-rewrite').resolve();sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from ingest import source_notes
import reference_coherence as ref
P=B/'runtime/poursuite-20261020/microsocial/edition002';O=P.parent/'edition003'
assert not O.exists(), 'Edition003 exists; do not overwrite'
O.mkdir()
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
save=lambda n,x:(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
m=load(P/'manifest.json')
for n,sha in m['files'].items():assert h(P/n)==sha,n
for p in P.iterdir():
 if p.is_file():shutil.copyfile(p,O/p.name)
a=load(P/'answer.json');before=copy.deepcopy(a)
for r in a:
 if r['number']=='D613-6':
  old='La circulaire CNAV 2025-23 du 10 novembre 2025, pages 8 et 15, distingue droits sur forfait cotisé et neutralisation Acre/DOM ;'
  new='La circulaire CNAV 2026-12 du 7 avril 2026, pages 9–10 et 17, distingue droits sur forfait cotisé et neutralisation Acre/DOM ; elle remplace la circulaire CNAV 2025-23 du 10 novembre 2025, conservée seulement comme source historique ;'
  assert old in r['review_notes'];r['review_notes']=r['review_notes'].replace(old,new)
 if r['number']=='D756-5':
  old='selon CNAV 2025-23 et le moteur public Urssaf.'
  new='selon les tableaux de la circulaire CNAV 2026-12 du 7 avril 2026, pages 7–8, et le moteur public Urssaf. La circulaire CNAV 2025-23 est explicitement remplacée et ne sert que de source historique. La prose du point2.3 dit « hors professions libérales » alors que le tableau BNC non réglementé inclut le taux DOM1 de4,3% : cette tension documentaire est signalée, sans transformer cette instruction en corrigendum officiel DILA.'
  assert old in r['review_notes'];r['review_notes']=r['review_notes'].replace(old,new)
save('answer.json',a)
aud=load(P/'audit.json');aud['documentary_update']={'edition':'003','replaces_documentary_citation_only':True,'current_reference':'CNAV2026-12 du7avril2026','current_pdf_url':'https://legislation.lassuranceretraite.fr/Documents/Circulaires/Pdf/circulaire_cnav_2026_12_07042026.pdf','current_pdf_sha256':'cc621e66e6c280aafe86ae449c2bc64878891f632e6111b060692a488a34c2ea','pages':'7–8fractionsDOM ;9–10droits sur forfait ;17neutralisationAcre/DOM ;22annexe graphique inspectée','historical_reference':'CNAV2025-23 du10novembre2025, annulée et remplacée ; aucune affirmation d’actualité','body_changes':False,'source_changes':False,'source_tension':'Prose du point2.3hors professions libérales versus tableau BNCnonréglementéDOM1 ; coordination favorable proposée deD756-5 explicite, pascorrigendumDILA.'};save('audit.json',aud)
e=load(P/'primary-web-evidence.json')
for r in e['sources']:
 if '2025_23' in r['url']:
  r['role']='Historique CNAV2025-23 du10novembre2025, annulé et remplacé par CNAV2026-12 du7avril2026 ; ne pas citer comme instruction actuelle.'
  r['read_scope']='Filigrane d’annulation constaté au rendu ; anciennes sections conservées pour provenance historique.'
e['sources'].append({'url':aud['documentary_update']['current_pdf_url'],'role':'Instruction primaire administrative actuelle CNAV2026-12 : neutralisation Acre/DOM base et complémentaire p17 ; fractions et tableauxDOM p7–8 ; droits contributifs sur forfait p9–10. Champ Assurance retraiteL631-1, pas transpositionCipav niMayotte.','read_scope':'Texte complet22pages lu ; pages7/8/17 et annexe graphique22 inspectées visuellement.','local_pdf':'../microsocial-independent-review/edition002/tmp/pdfs/cnav-2026-12.pdf','pdf_sha256':aud['documentary_update']['current_pdf_sha256'],'legal_status':'Publication administrative officielle, ni texte législatif/réglementaire ni fac-similéJO authentifié.'})
save('primary-web-evidence.json',e)
proof=[]
for old,new in zip(before,a):
 fields=[k for k in sorted(set(old)|set(new)) if old.get(k)!=new.get(k)]
 assert fields in ([],['review_notes']),fields
 assert old['proposed_xml']==new['proposed_xml']
 proof.append({'number':old['number'],'source_id':old['source_id'],'changed_fields':fields,'body_identical':True,'before_body_sha256':hashlib.sha256((old['proposed_xml'] or '').encode()).hexdigest(),'after_body_sha256':hashlib.sha256((new['proposed_xml'] or '').encode()).hexdigest()})
assert (O/'source.json').read_bytes()==(P/'source.json').read_bytes()
db=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
checks=[]
for f in ['capture.json','additional-dependencies.json','territory-scope-dependencies.json','tax-scope-dependencies.json']:
 for r in load(O/f):
  code,sid=r['code_id'],r['source_id'];current=db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(code,sid)).fetchone();doc=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,sid)).fetchone();prev=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(code,sid)).fetchone();raw=doc[0];raw=raw.decode() if isinstance(raw,bytes) else raw
  tests={'source_identity':current['source_sha256']==r['source_sha256'],'source_body':current['content_xml']==r['source_xml'],'source_notes':source_notes(db,code,sid)==r['source_notes_xml'],'source_document':raw==r['source_document_xml']}
  prior=r['previous_draft'];pv=dict(prev) if prev else None;tests['previous_draft']=(prior is None and pv is None)or(prior is not None and pv is not None and all(pv.get(k)==v for k,v in prior.items() if k!='proposed_sha256'))
  checks.append({'number':r['number'],'source_id':sid,'guards':tests,'all_match':all(tests.values())})
referror=None
try:ref.check_guards(db,load(O/'reference-targets.json'))
except Exception as ex:referror=str(ex)
validate_answer(copy.deepcopy(a),copy.deepcopy(load(O/'source.json')))
save('guard-validation.json',{'checks':checks,'all_match':all(c['all_match'] for c in checks),'read_transaction':'SQLite mode=ro BEGIN','reference_guard_error':referror,'canonical_mutation':False})
db.rollback();db.close()
proofobj={'baseline_edition':'002','baseline_source_sha256':h(P/'source.json'),'source_sha256':h(O/'source.json'),'source_file_byte_identical':True,'baseline_answer_sha256':h(P/'answer.json'),'answer_sha256':h(O/'answer.json'),'article_comparison':proof,'all_proposed_xml_byte_identical':True,'allowed_answer_fields_changed':['review_notes'],'changed_files':[p.name for p in O.iterdir() if p.is_file() and (P/p.name).exists() and p.read_bytes()!=(P/p.name).read_bytes()],'validation':'validate_answer passed in memory; no body changes','reference_guard_error':referror,'canonical_mutation':False}
save('documentary-comparison.json',proofobj)
save('manifest.json',{'frozen':True,'edition':'003','baseline':'002','files':{p.name:h(p) for p in O.iterdir() if p.is_file() and p.name!='manifest.json'},'canonical_mutation':False})
print(json.dumps({'source':h(O/'source.json'),'answer':h(O/'answer.json'),'manifest':h(O/'manifest.json'),'all_guards':all(c['all_match'] for c in checks),'reference_error':referror,'comparison':h(O/'documentary-comparison.json')}))
