"""Prepare the recovered D351-9 formula while keeping the canonical discrepancy held."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,html,json,re,shutil,sys
from pypdf import PdfReader,PdfWriter
from PIL import Image

Q=Path(__file__).resolve().parent;P=Q.parent;PROJECT=P.parents[2]
ROOT=Q/'registry-proposal'
dump=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=next(s for s in json.loads((Q/'source-snapshot.json').read_text())['records'] if s['source_id']=='LEGIARTI000030400105')
assert source['source_notes_xml']==''
original=P/'documents/JORF_20040101_1.pdf'
extract=ROOT/'documents/css-d351-original-20040101-pages46-47.pdf'
reader=PdfReader(original);writer=PdfWriter()
for n in (46,47):writer.add_page(reader.pages[n-1])
writer.add_metadata({'/Title':'Faithful pages 46-47 from official JORF 1 January 2004; distinct local extract'})
with extract.open('wb') as f:writer.write(f)
historical='E = [∑_{k=0}^{k=57} (1/(1+i)^k × L(A+k)/L(A)) − 11/24 − 1/12] × (1/(1+i)^(A−B) × L(A)/L(B))'
current=historical.replace('k=57','k=55')
latex=r'E=\left[\sum_{k=0}^{k=55}\left(\frac{1}{(1+i)^k}\times\frac{L(A+k)}{L(A)}\right)-\frac{11}{24}-\frac{1}{12}\right]\times\left(\frac{1}{(1+i)^{A-B}}\times\frac{L(A)}{L(B)}\right)'
im=Image.open(Q/'pages/d351-E-original-detail.png')
im.crop((0,12,im.width,im.height)).save(ROOT/'historical-media/css-d351-E-2004-original-detail.png')
docs=[dict(path='documents/'+extract.name,sha256=sha(extract),bytes=extract.stat().st_size,pages=2,original_pdf_pages=[46,47],printed_pages=[46,47],parent_document_path='documents/JORF_20040101_1.pdf',parent_document_sha256=sha(original),parent_document_bytes=original.stat().st_size,local_extract=True,original_whole_document=False,cryptographic_signature_preserved=False,extraction_method='pypdf full-page content/resources copied; no cropping or recomposition',url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000433712',title='Décret 2003-1376, JO 1 janvier 2004, pages 46-47, article D351-9',read_scope='Both entire pages visually read; whole 176-page JO not claimed visually reviewed'),dict(path='documents/css-decree-2010-1737.pdf',sha256=sha(ROOT/'documents/css-decree-2010-1737.pdf'),pages=3,url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387',title='Décret 2010-1737, art. 1 point 3, page 2',read_scope='All 3 pages visually read in earlier pass; relevant page 2 read again')]
rect=Q/'primary-texts/rectificatif-2003-1376-20040131.txt'
assert 'Page 51' in rect.read_text() and 'SOCS0325036Z' in rect.read_text()
discrepancy=dict(kind='canonical_definition_conflicts_with_express_2010_amendment',canonical_literal='L (A) est l’effectif à l’âge de soixante ans',canonical_body_exact_match='L (A) est l\'effectif à l\'âge de soixante ans',primary_locator='Décret 2010-1737, art. 1 point 3, 2°, official PDF page 2',primary_instruction='Aux a, b et c du 4° et à l’avant-dernier alinéa, les mots « de soixante ans » sont remplacés par « de soixante-deux ans ».',finding='The penultimate paragraph is L(A). The canonical XML still defines it at sixty, while A is sixty-two. The recovered graphic itself uses L(A), without numerical age. No silent change is made.',resolution='Held: full canonical version concordance cannot be certified. Parent to independently review the explicit discrepancy; no canonical correction authorized here.')
assert discrepancy['canonical_body_exact_match'] in source['source_xml']
R={k:source[k] for k in ('code_id','source_id','number','source_sha256')}
R.update(expected_markers=1,documentary_recovery_complete=False,graphic_recovery_complete=True,official_jo_crosscheck_complete=True,canonical_version_concordance_complete=False,authenticated_jo_crosscheck_complete=False,cryptographic_signature_validation_complete=False,ready_for_activation=False,count_as_completed=False,activation_performed=False,status='held_canonical_version_definition_discrepancy',source_and_notes_read_in_full=True,source_notes_empty=True,source_body_sha256=hashlib.sha256(source['source_xml'].encode()).hexdigest(),source_document_xml_sha256=hashlib.sha256(source['source_document_xml'].encode()).hexdigest(),source_notes_xml_sha256=hashlib.sha256(source['source_notes_xml'].encode()).hexdigest(),documents=docs,media=[],transcriptions=[dict(marker=1,text=current,latex=latex,source_document=docs[0]['path'],pdf_page=2,original_pdf_page=47,amendment_document=docs[1]['path'],amendment_pdf_page=2,amendment_locator='article 1, point 3, 3°',verified_against_explicit_primary_chain=True,primary_graphic_verified_visually=True,express_amendments_only=True,current_facsimile_available=False,method='Exact historical monthly graphic read at whole-page and native 300 dpi detail; only express 2010 change k=57→55 applied. Separate −11/24 and −1/12 preserved.')],historical_transcription=historical,historical_media=[dict(path='historical-media/css-d351-E-2004-original-detail.png',sha256=sha(ROOT/'historical-media/css-d351-E-2004-original-detail.png'),historical_only=True,registered_as_current_media=False,verified_visually=True,source_document=docs[0]['path'],pdf_page=2,extraction='Faithful crop of native 300 dpi page rendering, no reconstruction')],unresolved_content=discrepancy,concordance=[dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000249142',locator='whole rectificatif, JO 31 January 2004 text 2',finding='Seven textual/reference corrections; none changes E graphic.',evidence='primary-texts/'+rect.name,evidence_sha256=sha(rect)),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000790599',locator='article 1 III and article 7',finding='2006 changes projected ceiling increments and B date definition, plus transitional 2006 B rule; no E operator change.',evidence='web-9.json; web-11.json'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019986224',locator='article 2 III',finding='2008 changes acceptance-date wording to request-date wording; no E operator change.',evidence='../web/open-10-2008-initial.json'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387',locator='article 1 point 3, 1° to 4°, PDF page 2',finding='2010 changes formula 57→55, changes A to 62, and expressly changes sixty to sixty-two at the penultimate paragraph. This last instruction conflicts with canonical L(A) wording.',evidence='../pages/modif2010-2.png; web-11.json'),dict(url='https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030398366',locator='article 2',finding='2015 changes mortality table reference and D 167→172; no E operator change and no resolution of L(A) wording discrepancy.',evidence='web-8.json; web-9.json; web-11.json')],provenance_notes='The official monthly graphic has been recovered, but the candidate remains held because full canonical version concordance fails on a surrounding definition. No source text or notes are changed and no active registry or DB is opened. Historical image is not registered as current because its upper bound is historical.')
dump(ROOT/'records'/f"{source['source_id']}.json",R)
old=re.search(r'<p>\(Formule non reproduite\)\s*</p>',source['source_xml']).group()
new='<p>'+html.escape(current)+'</p>'
body=source['source_xml'].replace(old,new,1)
assert body.replace(new,old,1)==source['source_xml']
(Q/'d351-9-HELD-source-completion-candidate.html').write_text(body+'\n')
sys.path.insert(0,str(PROJECT))
import source_assets
c=source_assets.load_companions(ROOT)[(source['code_id'],source['source_id'])]
validation=dict(record_schema_loads=True,document_hashes_validated=True,graphic_transcription_present=source_assets.recovered_content_present(body,c),recovery_complete=source_assets.recovery_complete(source['source_xml'],c),full_canonical_concordance=False,non_marker_source_content_unchanged=True,source_notes_unchanged=True,activation_performed=False)
assert validation['graphic_transcription_present'] and not validation['recovery_complete']
dump(Q/'d351-validation.json',validation)
dump(Q/'d351-report.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source_id=source['source_id'],status=R['status'],ready_for_activation=False,graphic_recovery_complete=True,normative_source_complete=False,discrepancy=discrepancy,validation=validation,canonical_source_modified=False,active_registry_modified=False,DB_opened=False,document_path_base='registry-proposal/',documents=docs,concordance=R['concordance']))
dump(Q/'manifest.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'files':[dict(path=str(f.relative_to(Q)),bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(Q.rglob('*')) if f.is_file() and f.name!='manifest.json']})
print(json.dumps(validation,ensure_ascii=False))
