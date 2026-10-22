"""Finalize isolated documentary candidates; never activate or touch the live DB."""
from pathlib import Path
import hashlib,html,json,re,sys
from datetime import datetime,timezone

P=Path(__file__).resolve().parent
PROJECT=P.parents[2]
write=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
S=json.loads((P/'source-snapshot.json').read_text())['records']
T=json.loads((P/'cnbf2004-transcription.json').read_text())
for v in T['transcriptions']:
 if v['marker']==3:
  v['text']='E = [∑_{k=0}^{k=52 à 57} (1/(1+i)^k × L(A+k)/L(A)) − 3/8 − 1/4] × (1/(1+i)^(A−B) × L(A)/L(B))'
T['current_E']['text']=T['transcriptions'][2]['text'].replace('k=52 à 57','k=51 à 55')
write(P/'cnbf2004-transcription.json',T)
rp=P/'registry-proposal/records/LEGIARTI000038774726.json'
R=json.loads(rp.read_text())
R['documents']=[
 {'path':'documents/css-decree-2004-1457.pdf','sha256':T['document_sha256'],'url':T['observed_file_url'],'source_page_url':T['original_page_url'],'title':'Décret2004-1457, JORF0303du30décembre2004, texte39','pages':3,'read_scope':'All3pages visually inspected; formulas page2'},
 {'path':'documents/css-decree-2010-1737.pdf','sha256':T['amendment_pdf']['sha256'],'url':T['amendment_pdf']['file_url'],'source_page_url':T['amendment_pdf']['source_page_url'],'title':'Décret2010-1737, JORF0303du31décembre2010, texte83','pages':3,'read_scope':'All3pages visually inspected; D723-7 amendment page3'},
]
R['transcriptions']=[{'marker':x['marker'],'text':x['text'],'latex':x['latex'],'pdf_page':2,'source_document':'documents/css-decree-2004-1457.pdf','method':'Facsimile whole page plus separate 300 dpi formula detail checked','verified_visually':True} for x in T['transcriptions'][:2]]
for media in R['media']:
 if media['marker'] in (1,2):
  media['verified_visually']=True
R['transcriptions'].append({'marker':3,'text':T['current_E']['text'],'latex':T['current_E']['latex'],'pdf_page':2,'source_document':'documents/css-decree-2004-1457.pdf','amendment_document':'documents/css-decree-2010-1737.pdf','amendment_pdf_page':3,'amendment_locator':'article 1, point 8, 1°','method':'Literal transcription of 2004 graphic with only express 52→51 and 57→55 substitutions authorized by 2010 decree; no algebraic simplification','verified_against_explicit_primary_chain':True,'primary_graphic_verified_visually':True,'express_amendments_only':True,'current_facsimile_available':False})
R.update(documentary_recovery_complete=True,authenticated_jo_crosscheck_complete=False,official_jo_crosscheck_complete=True,canonical_version_concordance_complete=True,cryptographic_signature_validation_complete=False,status='complete_documentary_candidate_not_activated',ready_for_activation=True,count_as_completed=False,unresolved_content=None)
R['provenance_notes']='Two official JORF PDFs obtained via normal IAB by root, no authentication/cookie export or protection bypass. Actual downloaded file bytes/hashes verified; advertised viewer sizes differ and are not treated as file sizes. Three2004pages and three2010pages rendered and read; formulas absent from text extraction and checked visually. 2008decree changes Bdate wording only. 2010expressly changes52/57 into51/55 in E. 2019article5III4° transfersD723-7 toD653-4; III12° changes surrounding references only. Source ARTICLE/notes unchanged; notes empty. official_jo_crosscheck_complete denotes comparison to official JORF facsimiles; authenticated_jo_crosscheck_complete=false and cryptographic_signature_validation_complete=false because no cryptographic signature verification is claimed. See cnbf2004-transcription.json and audit.md.'
R['concordance']=T['normative_concordance']
R['independent_review_required_before_activation']=True
R['activation_performed']=False
write(rp,R)
src=next(s for s in S if s['source_id']==R['source_id'])
body=src['source_xml']
replacement_iter=iter(R['transcriptions'])
def complete(m):
 v=next(replacement_iter)
 return '<p>'+html.escape(v['text'])+'</p>'
body,n=re.subn(r'<p>\(Formule non reproduite\)\s*</p>',complete,body)
assert n==3
(P/'d653-4-source-completion-candidate.html').write_text(body+'\n')
REPORT=json.loads((P/'report.json').read_text())
REPORT.update(status='documentary_pass_complete_one_CSS_source_recovered_others_held',result='one_complete_normative_documentary_recovery',complete_normative_sources=1,recovered_elements=3,remaining_missing_elements=3)
REPORT['new_normative_documents']=[dict(d,path='registry-proposal/'+d['path'],registry_relative_path=d['path']) for d in R['documents']]
REPORT['normative_transcription_document_path_base']='registry-proposal/'
REPORT['normative_transcriptions']=R['transcriptions']
for x in REPORT['records']:
 if x['source_id']==R['source_id']:
  x.update(status=R['status'],recovered_elements=3,documentary_recovery_complete=True,exact_normative_extractions=R['transcriptions'],graphic_page=2,normative_proof='cnbf2004-transcription.json',ready_for_activation=True,missing_primary_piece=None,finding='All3expressions recovered from2004facsimile; Eupper numbers changed only as expressly prescribed by2010facsimile. 2008date wording and2019transfer verified in primary text. Not activated.')
  for flag in ('official_jo_crosscheck_complete','canonical_version_concordance_complete','authenticated_jo_crosscheck_complete','cryptographic_signature_validation_complete'):
   x[flag]=R[flag]
 else:
  x['ready_for_activation']=False
REPORT['PDF_review']['new_requested_PDF_download_success']=True
REPORT['PDF_review']['reason']='Initial CLI/mirror access failed. Root later accessed official IAB normally and supplied2real JORF PDFs. Local whole-document renders, visual reading, original image details and exact express amendment comparison completed.'
REPORT['PDF_review']['new_documents_reviewed']=[{'path':'documents/joe_20041230_0303_0039.pdf','pages':3,'all_pages_rendered_and_visually_read':True,'formula_page':2,'formulas_absent_from_text_extraction':True,'detail_images':'pages/cnbf2004-E-detail.png and registry-proposal/media/css-d653-4-option-a.png / css-d653-4-option-b.png'},{'path':'documents/joe_20101231_0303_0083.pdf','pages':3,'all_pages_rendered_and_visually_read':True,'relevant_amendment_page':3,'finding':'Only upper label numbers52 and57 changed into51 and55; k/A lists agree with canonical source.'}]
REPORT['safe_process']['other_agent_created']=False
REPORT['companion_proposals']='registry-proposal/records/*.json; D653-4 is a complete isolated candidate, the other three remain incomplete; none activated by this subagent'
REPORT['browser_scope']={'Chrome_subagent_attempt':'Passive Cloudflare; no interactive action. Own tabs1399865406/1399865409 only.','IAB_subagent_availability':'BrowserID2 and iab alias unavailable; inventory showed onlyChromeID1. Root alone acquired PDFs via itsIAB.','root_legacy_scan_status':'Root reports explicit interactive CAPTCHA for1982, January2004 andMay2004facsimiles; not solved by thissubagent. User handoff handled byroot.','no_browser_cookie_export':True}
REPORT['at_utc']=datetime.now(timezone.utc).isoformat()
write(P/'report.json',REPORT)
sys.path.insert(0,str(PROJECT))
import source_assets
loaded=source_assets.load_companions(P/'registry-proposal')
V=[]
for s in S:
 c=loaded[(s['code_id'],s['source_id'])]
 v={'source_id':s['source_id'],'record_schema_loads':True,'expected_markers_agree':c['expected_markers']==len(source_assets.graphic_markers(s['source_xml'])),'recovery_complete':source_assets.recovery_complete(s['source_xml'],c),'registered_media':len(c['media']),'transcriptions':len(c['transcriptions']),'source_notes_preserved_empty':s['source_notes_xml']==''}
 if s['source_id']==R['source_id']:
  v['recovered_content_present_in_isolated_candidate']=source_assets.recovered_content_present(body,c)
  restored=body
  for original,entry in zip(re.findall(r'<p>\(Formule non reproduite\)\s*</p>',s['source_xml']),R['transcriptions']):
   restored=restored.replace('<p>'+html.escape(entry['text'])+'</p>',original,1)
  v['non_marker_content_unchanged']=restored==s['source_xml']
  assert v['non_marker_content_unchanged']
  assert v['recovery_complete'] and v['recovered_content_present_in_isolated_candidate']
 V.append(v)
write(P/'companion-validation.json',V)
write(P/'manifest.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'files':[{'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':digest(f)} for f in sorted(P.rglob('*')) if f.is_file() and f.name!='manifest.json']})
print(json.dumps({'complete_sources':sum(v['recovery_complete'] for v in V),'recovered_elements':3,'remaining':3,'activated':False,'isolated_candidate_content_verified':True},ensure_ascii=False))
