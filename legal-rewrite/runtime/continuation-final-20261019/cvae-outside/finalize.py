from pathlib import Path
import json,hashlib,sqlite3,shutil,xml.etree.ElementTree as E,re,sys
H=Path(__file__).resolve().parent;B=H.parents[2];sha=lambda b:hashlib.sha256(b.encode()if isinstance(b,str)else b).hexdigest()
source=json.loads((H/'source-versions.json').read_text());sources=json.loads((H/'source.json').read_text());answers=json.loads((H/'answer.json').read_text()); byid={s['source_id']:s for s in sources}
checks=[]
for r in source['articles']:
 n=E.fromstring(r['source_document_xml']);co=n.find('BLOC_TEXTUEL/CONTENU');no=n.find('NOTA/CONTENU')
 inner=lambda e:(e.text or '')+''.join(E.tostring(c,encoding='unicode')for c in e)if e is not None else''
 assert sha(r['source_document_xml'])==r['source_sha256'];assert inner(co)==r['source_xml'];assert inner(no)==r['source_notes_xml']
 checks.append({'code_id':r['code_id'],'source_id':r['source_id'],'whole_article_sha256':r['source_sha256'],'body_sha256':sha(r['source_xml']),'notes_sha256':sha(r['source_notes_xml']),'valid':True})
future=json.loads((H/'all-future-code-support.json').read_text())
for r in future:assert sha(r['source_document_xml'])==r['source_sha256']
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True)
archive_proof={n:{'sha256':s,'source_url':u,'complete':bool(co)}for n,s,u,co in c.execute('select name,sha256,source_url,complete from archives')}
guards=[]
for s in sources:
 before=c.execute('select source_sha256,status,proposed_xml from drafts where code_id=? and source_id=?',(s['code_id'],s['source_id'])).fetchone();assert before is None
 guards.append({'code_id':s['code_id'],'source_id':s['source_id'],'canonical_raw_sha256':s['source_sha256'],'existing_database_draft':None,'checked_readonly':True})
c.close()
read_full={'LEGIARTI000053547707','LEGIARTI000051215956','LEGIARTI000051173263','LEGIARTI000054334488','LEGIARTI000054334492','LEGIARTI000024166624','LEGIARTI000045917200','LEGIARTI000053564351','LEGIARTI000038611033','LEGIARTI000039653551','LEGIARTI000039469799','LEGIARTI000032517552','LEGIARTI000006240042','LEGIARTI000054587047','LEGIARTI000053100833'}
audit=[]
for r in source['articles']:
 current=r['valid_from']<='2026-10-19'<r['valid_until'];id=r['source_id']
 if id in byid:disposition='complete_proposal';scope='entire current article and notes read'
 elif id in read_full:disposition='unchanged_source_reference';scope='entire article and notes read'
 elif current and re.search(r'CVAE|valeur\s+ajoutée|1586|1679\s+septies',r['source_xml'],re.I):disposition='body_reference_requires_review';scope='automatic lexical classification only'
 elif current:disposition='metadata_link_or_non_CVAE_reference';scope='body reference search; not counted as whole legal review or rewriting'
 else:disposition='historical_or_future_source_only';scope='archived source; not counted as rewriting'
 audit.append({k:r[k]for k in['code_id','source_id','number','valid_from','valid_until','state','source_sha256','source_url']}|{'current_as_of':current,'disposition':disposition,'review_extent':scope})
assert not any(r['disposition']=='body_reference_requires_review'for r in audit)
(H/'reference-audit.json').write_text(json.dumps({'as_of':'2026-10-19','selected_versions':len(audit),'reviewed_complete_ids':sorted(read_full),'records':audit},ensure_ascii=False,indent=2)+'\n')
(H/'source-validation.json').write_text(json.dumps({'valid':True,'raw_body_notes_checks':checks,'future_raw_checks':len(future),'readonly_database_guards':guards,'archives_replayed':source['archives_replayed'],'stock_extraction':'Official stock selectively extracted by bsdtar; subsequent 466 archives replayed with article-ID replacement. XML, notes, member path and source checksum retained.','archive_manifest_sha256':source['archive_manifest_sha256']},ensure_ascii=False,indent=2)+'\n')
articles=[]
titles={'55':'Loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023 — article 55','79':'Loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024 — article 79','62':'Loi n° 2025-127 du 14 février 2025 de finances pour 2025 — article 62'}
for a in answers:
 s=byid[a['source_id']]; rawsha=s['source_sha256'];article=s|a
 # Companion publication loader deliberately hashes the body, distinct from the canonical raw-source hash.
 article.update({'title':titles[s['number']],'kind':'noncodified_article','owner':s['code_id'],'source_date':'2026-10-19','source_state':s['state'],'source_sha256':sha(s['source_xml']),'source_article_raw_sha256':rawsha,'source_document_sha256':rawsha,'source_sha256_convention':'whole source body for companion loader; raw ARTICLE XML separately fingerprinted','excluded_from_30317_counter':True,'provenance':{'provider':'DILA — LEGI','archive':s['archive'],'archive_member':s['archive_member'],'archive_sha256':archive_proof[s['archive']]['sha256'],'archive_source_url':s['archive_source_url'],'as_of':'2026-10-19','last_update_archive':'LEGI_20261018-205213.tar.gz','archives_replayed':467},'status':'proposal_not_adopted'})
 articles.append(article)
manifest={'title':'Suppression prospective de la CVAE — coordinations législatives de calendrier','as_of':'2026-10-19','outside_code_inventory':True,'excluded_from_30317_counter':True,'groups':['impots'],'candidate_only':True,'registered':False,'published':False,'scope_note':'Trois articles non codifiés consolidés complets. Leurs dispositions nouvelles neutralisent les rétablissements différés de CVAE, protègent les anciennes années et les avantages CFE ainsi que les autres réformes. Les marqueurs historiques des parties déjà codifiées restent identifiés comme tels et ne sont pas comptés comme de nouveaux articles réécrits. Aucun financement de remplacement n’est créé.','articles':articles}
# Test only the isolated candidate manifest with the actual publication validator, outside any active coordination directory.
test=H/'loader-check'/'cvae-calendar';test.mkdir(parents=True,exist_ok=True);(test/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
sys.path.insert(0,str(B));from coordination_downloads import load
assert len(load(H/'loader-check'))==1
(H/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('FINAL SOURCES',len(source['articles']),'FUTURE',len(future),'PROPOSALS',len(answers),'LOADER OK')
