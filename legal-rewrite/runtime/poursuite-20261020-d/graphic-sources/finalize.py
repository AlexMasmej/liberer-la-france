import pathlib, json, hashlib, datetime, sqlite3
R=pathlib.Path(__file__).resolve().parent
sha=lambda v: hashlib.sha256((v or '').encode()).hexdigest()
load=lambda p: json.loads((R/p).read_text())
write=lambda p,v:(R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
S=load('source-snapshot.json'); c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
g=[]
for s in S:
 k=(s['code_id'],s['source_id']);a=c.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone();d=c.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();raw=c.execute('SELECT xml FROM documents WHERE code_id=? AND id=?',k).fetchone()
 tests={'article_present':bool(a),'source_xml_unchanged':bool(a and a['content_xml']==s['source_xml']),'source_declared_sha_unchanged':bool(a and a['source_sha256']==s['source_sha256']),'raw_article_xml_unchanged':bool(raw and (raw['xml'].decode('utf-8') if isinstance(raw['xml'],bytes) else raw['xml'])==s['raw_document_xml']),'proposed_xml_unchanged':(d['proposed_xml'] if d else None)==s['proposed_xml']}
 g.append({'code_id':k[0],'source_id':k[1],'number':s['number'],'source_sha256':s['source_sha256'],'source_body_sha256':sha(s['source_xml']),'source_notes_sha256':sha(s['source_notes_xml']),'raw_document_sha256':sha(s['raw_document_xml']),'proposed_sha256':sha(s['proposed_xml']),'draft_exists_now':bool(d),'checks':tests})
c.rollback();c.close()
write('fresh-guards.json',{'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'read-only transaction BEGIN, no registration and no active files changed','passed':all(all(a['checks'].values()) for a in g),'records':g})
missing={
'D351-9':('monthly_annuity_E',1,'Fac-similé de la formule mensuelle E de D351-9, avec indices/exposants exacts, puis confrontation aux rectificatifs et modifications de 2004, 2010 et 2015 ; ne pas convertir une formule en x/60/omega ni corriger L(A) par déduction.'),
'D643-7':('quarterly_annuity_E',1,'Fac-similé du terme trimestriel E, notamment rectificatif du décret initial de 2004 et portée des modifications 2010-1737 ; pas de transposition du terme mensuel.'),
'D653-4':('two_purchase_options_and_quarterly_E',3,'Trois formules originales de D723-7 (devenu D653-4) : décret 2004-1457, puis modifications et transfert 2019-718. Les simples renumérotations ne restituent pas une image absente.'),
"Annexe I à l'art. R434-32 (7)":('quadranopsia_quadrant_figure',1,'Cliché du barème AT français à la suite de la phrase quadranopsies ; ne pas le remplacer par le barème fonctionnel de 2026, des taux étrangers, une application CNAM ou une moyenne des hémianopsies.'),
'A123-1':('pos_1984_complete_legend',1,'Annexe graphique complète du JONC 17 juillet 1984 pour R123-18 I/II ; la légende SUP relative à R126-1 est un autre texte et les standards CNIG ultérieurs sont des adaptations.'),
'R254-5':('rights_value_and_rate',2,'Deux images JO0150 du 29 juin 2016, texte48, décret2016-855. Recherche antérieure du parent laissée intacte ; cette passe ne réessaye pas cet accès.'),
'D453-7':('total_guarantee_commitment',1,'Formule entière JO0303 du 30 décembre 2007 texte157 JORFTEXT000017767416, ancien R453-7 ; les cinq définitions de variables ne permettent pas d’inférer les opérations mathématiques.'),
'49 septies ZZH':('discount_factor_and_reference_rate',2,'Deux formules JO0303 du 31 décembre 2010 texte67, décret2010-1728 JORFTEXT000023333871. La pièce BOI4A-6-12 reproduit les renvois et non les formules. Ne pas emprunter celles de l’éco-PTZ ou de Mayotte.'),
'15':('two_historical_cerfa_models',2,'Cadres intégraux CERFA historiques30-0812 et30-0813, avec rattachement officiel à l’article15 ; les champs énumérés et les modèles IFU modernes ne valent pas preuve des cadres.'),
}
F=[]
for s in S:
 typ,n,piece=missing[s['number']]
 F.append({'code_id':s['code_id'],'source_id':s['source_id'],'number':s['number'],'missing_content_type':typ,'missing_elements':n,'recovered_elements':0,'recovery_complete':False,'source_and_notes_read_in_full':True,'status':'still_held_no_normative_transcription','missing_primary_piece':piece,'source_url':s['source_url'],'new_pass_focus':s['number'] in ['D351-9','D643-7','D653-4','A123-1','49 septies ZZH','15']})
write('recovery-findings.json',{'version':1,'scope':'9 held sources inventoried; targeted new documentary searches, no claim that every historical publication was inspected','complete_normative_recoveries':0,'normative_transcriptions':[],'records':F,'new_primary_document':{'path':'boi-4a612-20120330.pdf','publication':'BOI39,30 mars2012,4A-6-12, instruction27mars2012','primary_publisher':'DGFiP/ministère des finances','role':'primary official tax commentary, annex reproducing legislation; not JO facsimile','inspection_scope':'Cover/title/contents and annex3, especially printed/PDFpage32 visually rendered and read; not a legal review of all49pages','result':'Both missing formulas remain absent on page32; literal JO referral lines replace them. Historical premium table1..5/6..8/9..10 must not replace current2024table.','recovery_complete':False}})
write('access-attempts.json',{'attempts':[
{'url':'https://www11.minefi.gouv.fr/boi/boi2012/4fepub/textes/4a612/4a612.pdf','method':'standard HTTPS urllib, public official site','result':'downloaded; PDF49pages, visually checked page32; missing both formulas','provenance_file':'boi-4a612-provenance.json'},
{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023333871','method':'standard public HTTPS; no custom authentication or anti-protection headers','result':'HTTP403; not retried with evasive credentials/headers','evidence':'legifrance-standard-attempt.json'},
{'url':'https://www.legifrance.gouv.fr/jo_pdf.do?id=JORFTEXT000023333871','method':'web reader normal public URL exposed by source','result':'tool could not access; no document acquired'},
{'url':'https://www.legifrance.gouv.fr/download/pdf?id=JORFTEXT000023333871','method':'web reader standard endpoint (not a token or challenge bypass)','result':'tool could not access; no document acquired'},
{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000000893867','method':'normal public Chrome navigation','result':'security verification page; challenge left untouched; no downloadMedia used'},
{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000000893867','method':'web reader','result':'historical HTML text accessible; equation linearly fragmented/duplicated, not a visually verified facsimile; no attempt to reconstruct currentformula'},
{'url':'https://bofip-archives.impots.gouv.fr/bofip/24759-AIDA.html/identifiant=-20120330','method':'web reader','result':'official annex3 also contains two JO referrals, no formula images at those positions'},
{'url':'https://legislation.lassuranceretraite.fr/Pdf/circulaire_rsi_2011_017_14062011.pdf','method':'web reader','result':'official circular on 2010age changes; inspected relevant passage, not an original formula facsimile; no recoveryclaim'},
{'url':'https://www.sgfgas.fr/','method':'web reader','result':'tool internal/access error; no resource acquired'},
{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017767416','method':'web reader','result':'not accessible; no resource acquired'},
{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038731196','method':'web reader','result':'HTTP403 on open; indexed initialtext metadata accessible; no PDF acquired'},
], 'protection_bypassed':False,'captcha_solved':False,'active_registry_changed':False,'canonical_articles_written':False})
files={str(p.relative_to(R)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name not in ['manifest.json']}
write('manifest.json',{'version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'recovery_complete':False,'recovered_sources_count':0})
print('guards',all(all(a['checks'].values()) for a in g),'records',len(g),'files',len(files))
