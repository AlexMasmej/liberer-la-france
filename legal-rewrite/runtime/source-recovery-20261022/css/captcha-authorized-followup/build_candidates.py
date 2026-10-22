"""Build isolated documentary companions; do not open any DB or active registry."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, html, json, re, shutil, sys
from pypdf import PdfReader, PdfWriter

Q=Path(__file__).resolve().parent
P=Q.parent
PROJECT=P.parents[2]
ROOT=Q/'registry-proposal'
for d in ('records','documents','historical-media'):
 (ROOT/d).mkdir(parents=True,exist_ok=True)
dump=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
snap=json.loads((P/'source-snapshot.json').read_text())['records']

def doc_copy(source,name,**meta):
 target=ROOT/'documents'/name
 shutil.copy2(source,target)
 return dict(path='documents/'+name,sha256=sha(target),bytes=target.stat().st_size,**meta)

def page_extract(source,numbers,name,**meta):
 target=ROOT/'documents'/name
 reader=PdfReader(source);writer=PdfWriter()
 for n in numbers: writer.add_page(reader.pages[n-1])
 writer.add_metadata({'/Title':'Faithful page selection from official JORF; distinct local extract'})
 with target.open('wb') as f: writer.write(f)
 return dict(path='documents/'+name,sha256=sha(target),bytes=target.stat().st_size,pages=len(numbers),original_pdf_pages=numbers,parent_document_path=str(source.relative_to(P)),parent_document_sha256=sha(source),parent_document_bytes=source.stat().st_size,local_extract=True,original_whole_document=False,extraction_method='pypdf add_page, full page content/resources copied; no cropping, recomposition or replacement',cryptographic_signature_preserved=False,**meta)

def source_proof(s):
 return {k:s[k] for k in ('code_id','source_id','number','source_sha256')}|{'source_body_sha256':hashlib.sha256(s['source_xml'].encode()).hexdigest(),'source_document_xml_sha256':hashlib.sha256(s['source_document_xml'].encode()).hexdigest(),'source_notes_xml_sha256':hashlib.sha256(s['source_notes_xml'].encode()).hexdigest(),'source_and_notes_read_in_full':True,'source_notes_empty':s['source_notes_xml']==''}

s=next(s for s in snap if s['source_id']=='LEGIARTI000023395852')
assert s['source_notes_xml']==''
d1=page_extract(P/'documents/JORF_20040529_124.pdf',[97],'css-d643-original-20040529-page9593.pdf',url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000437935',title='JORF 29 mai 2004, page imprimée 9593, décret 2004-461, art. 2 : D643-7',read_scope='Whole normative D643-7 page 97 / printed 9593 visually read; rest of 152-page JO not claimed visually reviewed')
d2=doc_copy(P/'documents/joe_20040904_0206_0019.pdf','css-d643-rectificatif-20040904.pdf',pages=1,url='https://www.legifrance.gouv.fr/download/file/a_urgQLFljTH3a379PKqvLLRPUtKNSw_DzSHjt1DoHk=/JOE_TEXTE',source_page_url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000445868',title='JORF 4 septembre 2004, texte 19, décret 2004-461 rectificatif, NOR SANS0420911Z',read_scope='Whole single page visually read; both historical erroneous and corrected E compared')
d3=doc_copy(P/'documents/joe_20101231_0303_0083.pdf','css-decree-2010-1737.pdf',pages=3,url='https://www.legifrance.gouv.fr/download/file/63svbPxxA_9vv0UbiiKxBdygrRYNmELc4MrM4SFNwfQ=/JOE_TEXTE',source_page_url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387',title='Décret 2010-1737 du 30 décembre 2010, JO 31 décembre 2010, texte 83',read_scope='All three pages visually reviewed in prior pass; page 2, art. 1 point 6 reread for D643-7')
historical='E = [∑_{k=0}^{k=52 à 57} (1/(1+i)^k × L(A+k)/L(A)) − 3/8 − 1/4] × (1/(1+i)^(A−B) × L(A)/L(B))'
current=historical.replace('k=52 à 57','k=51 à 55')
latex=r'E=\left[\sum_{k=0}^{k=51\,\text{à}\,55}\left(\frac{1}{(1+i)^k}\times\frac{L(A+k)}{L(A)}\right)-\frac{3}{8}-\frac{1}{4}\right]\times\left(\frac{1}{(1+i)^{A-B}}\times\frac{L(A)}{L(B)}\right)'
media_src=Q/'pages/d643-rectifier-original-image-010.png'
if not media_src.exists(): raise FileNotFoundError(media_src)
media_target=ROOT/'historical-media/css-d643-corrected-E-2004-original-image.png'
shutil.copy2(media_src,media_target)
R=source_proof(s)|dict(expected_markers=1,documentary_recovery_complete=True,official_jo_crosscheck_complete=True,canonical_version_concordance_complete=True,authenticated_jo_crosscheck_complete=False,cryptographic_signature_validation_complete=False,ready_for_activation=True,count_as_completed=False,activation_performed=False,independent_review_required_before_activation=True,status='complete_documentary_candidate_not_activated',documents=[d1,d2,d3],media=[],transcriptions=[dict(marker=1,text=current,latex=latex,pdf_page=1,source_document=d2['path'],historical_original_document=d1['path'],amendment_document=d3['path'],amendment_pdf_page=2,amendment_locator='article 1, point 6, 1°',verified_against_explicit_primary_chain=True,primary_graphic_verified_visually=True,express_amendments_only=True,current_facsimile_available=False,method='Corrected 2004 graphic read visually, then only express 2010 upper-bound number replacements 52→51 and 57→55; no algebraic simplification')],historical_media=[dict(path='historical-media/'+media_target.name,sha256=sha(media_target),historical_only=True,registered_as_current_media=False,verified_visually=True,source_document=d2['path'],pdf_page=1,extraction='Original embedded stencil image 21 0 / pdfimages item 10, 927x126 pixels; no redrawing')],historical_corrected_2004_transcription=historical,concordance=[dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000445868',locator='whole text, single PDF page',finding='Express rectification of E: closes summand before separate minus 3/8 and minus 1/4; May 2004 erroneous grouping excluded.',evidence='primary-texts/rectificatif-2004-461-20040904.txt; pages/d643-rectificatif-1.png'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000790599',locator='articles 3 and 7',finding='2006 does not alter D643-7 formula; article 7 gives a 2006 transitional B rule. Canonical current B preserved.',evidence='web-9.json'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019986224',locator='article 4 III',finding='2008 changes only wording of request date in D643-7; no formula operators changed.',evidence='../web/open-10-2008-initial.json'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387',locator='article 1, point 6, 1° to 3°, PDF page 2',finding='52 and 57 in formula replaced by 51 and 55; k and A lists expressly updated and match canonical current body.',evidence='../pages/modif2010-2.png')],provenance_notes='Original whole 152-page JO retained locally; published companion is one faithful entire page, explicitly a distinct local extract. Corrected E is taken from the complete official September rectificatif, not borrowed from CNBF. Current E is a transcription through express 2010 amendments. Historical original image is proof only and is not registered as a current graphic. Source body and empty notes unchanged except isolated replacement of one omission. No active registry or DB opened.')
dump(ROOT/'records'/f"{s['source_id']}.json",R)
pattern=r'<p>\(formule non reproduite\)\s*</p>'
old=re.search(pattern,s['source_xml']).group()
replacement='<p>'+html.escape(current)+'</p>'
body,n=re.subn(pattern,lambda m:replacement,s['source_xml'])
assert n==1 and body.replace(replacement,old,1)==s['source_xml']
(Q/'d643-7-source-completion-candidate.html').write_text(body+'\n')
sys.path.insert(0,str(PROJECT))
import source_assets
loaded=source_assets.load_companions(ROOT)
c=loaded[(s['code_id'],s['source_id'])]
checks={'source_id':s['source_id'],'record_schema_loads':True,'document_hashes_validated':True,'recovery_complete':source_assets.recovery_complete(s['source_xml'],c),'recovered_content_present':source_assets.recovered_content_present(body,c),'non_marker_source_content_unchanged':True,'source_notes_preserved_empty':True,'activation_performed':False}
assert checks['recovery_complete'] and checks['recovered_content_present']
dump(Q/'d643-validation.json',checks)
dump(Q/'d643-report.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source=source_proof(s),status=R['status'],ready_for_activation=True,registry='registry-proposal',record='registry-proposal/records/'+s['source_id']+'.json',recovered_elements=1,remaining_uncertainty=None,canonical_source_modified=False,active_registry_modified=False,DB_opened=False,normative_proof=R['concordance'],validation=checks,document_path_base='registry-proposal/',documents=R['documents'],original_whole_JO_kept_local=True,historical_image_not_current=True))
dump(Q/'manifest.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'files':[dict(path=str(f.relative_to(Q)),bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(Q.rglob('*')) if f.is_file() and f.name!='manifest.json']})
print(json.dumps(checks,ensure_ascii=False))
