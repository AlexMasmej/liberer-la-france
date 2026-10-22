from pathlib import Path
import json,hashlib,datetime,re,html,unicodedata,shutil,subprocess,importlib.util
from pypdf import PdfReader
from PIL import Image
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,data):(P/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
src=next(x for x in json.loads((P/'source-snapshot.json').read_text())if x['source_id']=='LEGIARTI000049362876')
pdf=P/'documents/joe_20101231_0303_0067.pdf'
assert sha(pdf)=='6e58b9cd2c41d76ce8c274f85c606394ab2d040931483bf62bad152f83511c14'
reader=PdfReader(pdf)
assert len(reader.pages)==3
shutil.copyfile(pdf,P/'registry-proposal/documents'/pdf.name)
linear=['β_t = (1 + z_t)^(-t/12)','Σ_(t=1)^T (1 + i)^(-t/12) = Σ_(t=1)^T β_t']
media=[]
for n,(name,dimensions) in enumerate([('Im1.tiff',(283,57)),('Im2.tiff',(364,120))],1):
    original=next(x for x in reader.pages[1].images if x.name==name)
    assert original.image.size==dimensions
    target=P/'registry-proposal/media'/f'49septieszzh-formule-{n}-jo2010.png'
    original.image.save(target,format='PNG')
    exported=Image.open(target)
    assert exported.size==original.image.size and exported.tobytes()==original.image.tobytes()
    media.append({'marker':n,'path':str(target.relative_to(P/'registry-proposal')),'sha256':sha(target),'width':dimensions[0],'height':dimensions[1],'page':2,'pdf_image_name':name,'pdf_path':'documents/'+pdf.name,'decoded_pixel_sha256':hashlib.sha256(original.image.tobytes()).hexdigest(),'pixel_equality_verified':True,'extraction':'Export PNG sans recadrage, changement de résolution ni redessin de l’image CCITT 1 bit incorporée au PDF. Pixels du PNG vérifiés identiques à l’image décodée du PDF.','verified_visually':True,'documentary_status':'Deux images originales du fac-similé officiel, lues sur la page 2 entière puis chacune séparément.','alt':linear[n-1]})
doc={'path':'documents/'+pdf.name,'sha256':sha(pdf),'url':'https://www.legifrance.gouv.fr/download/file/63svbPxxA_9vv0UbiiKxBb2WtDEED7w2wigHyhC4AJI=/JOE_TEXTE','landing_url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023333871','label':'Légifrance/DILA, JORF 0303 du 31 décembre 2010, texte 67 sur 167, décret 2010-1728 du 30 décembre 2010, NOR EFIE1033033D, article 1 ; extrait officiel complet de trois pages.','retrieved_date_utc':'2026-10-22','recovery_method':'Téléchargement navigateur normal par le parent depuis le lien explicite public JOE_TEXTE ; fichier PDF entier transféré localement. Aucun CAPTCHA résolu ni cookie exporté selon le journal du parent.','bytes':pdf.stat().st_size,'page_count':3,'pages_visually_read_in_full':[1,2,3],'formula_pages':[2],'digital_signature_present':False,'cryptographic_signature_validation_complete':False}
def norm(t):
    t=html.unescape(re.sub('<[^>]+>',' ',t))
    t=unicodedata.normalize('NFKC',t).lower().replace('웁','β')
    t=re.sub(r'\bn(?:o|°)\s*(?=\d)','n',t)
    t=re.sub(r'(?<=\d)o(?=\s)','',t)
    return re.sub(r'[^\w]','',t)
pdftext=(P/'documents/joe_20101231_0303_0067.txt').read_text()
npdf=norm(pdftext)
pars=re.findall(r'<p\b[^>]*>(.*?)</p>',src['source_xml'],re.S)
checks=[]
for index,body in enumerate(pars,1):
    text=html.unescape(re.sub('<[^>]+>',' ',body)).strip()
    if 'formule non reproduite' in text:continue
    adjustment=''
    comparison=text
    if 'ou la société de financement' in comparison:
        comparison=comparison.replace(' ou la société de financement','')
        adjustment='La source actuelle ajoute « ou la société de financement » ; cette phrase actuelle reste entière et n’est pas remplacée par la phrase de 2010.'
    checks.append({'canonical_paragraph':index,'canonical_text':text,'pdf_text_match_after_typographic_normalization_and_documented_version_difference':norm(comparison) in npdf,'documented_version_difference':adjustment})
assert len(checks)==8 and all(x['pdf_text_match_after_typographic_normalization_and_documented_version_difference']for x in checks)
concordance={'source_id':src['source_id'],'source_sha256':src['source_sha256'],'valid_from':src['valid_from'],'valid_until':src['valid_until'],'source_notes_xml_preserved':src['source_notes_xml'],'pages_visually_read_in_full':[1,2,3],'canonical_textual_paragraph_count':8,'canonical_graphic_markers':2,'paragraph_checks':checks,'normalization':'NFKC/case/whitespace/punctuation and no→n before number; the corrupt text-extraction glyph 웁 is matched to β only after visual reading of the PDF. Formula transcriptions come from the images, never this glyph substitution.','canonical_table_kept_exactly':True,'historical_2010_table_imported':False,'historical_table_excluded':'La table 2010 1à5/6à8/9et10, primes75/55/35, est seulement le contexte historique du fac-similé. Elle n’est jamais copiée dans la source actuelle.','current_official_page':'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049362876','current_official_page_verified':'La page officielle en vigueur depuis le 4avril2024 reproduit les mêmes définitions et les deux renvois expressément dirigés vers le JO2010texte67.','2024_modification_primary_evidence':{'url':'https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=NIM:202406063','document':'Décret2024-304du2avril2024, JORF3avril2024texte21, NOR TREL2403702D','article9':'A la dernière colonne de la première ligne du tableau du neuvième alinéa de l’article49septiesZZH, le chiffre3estremplacépar4.','article12':'Applicationauxoffresdeprêtsémisesàcompterdu1eravril2024.','scope':'Corps du fac-similé officiel accessible en texte par outil web. GET local202vide, capture webPDF impossible ; aucun PDF2024 local ou rendu2024 prétendu.','evidence_file':'zzh-current-version-web-evidence.json'},'current_parameters_preserved':{'tranches':['1','2 À 4'],'prime_p':['75 points de base','55 points de base'],'source_notes_xml':src['source_notes_xml']},'source_media_mapping':media,'formula_continuity_basis':'La source officielle actuelle désigne exactement le JO2010texte67 aux deux emplacements et conserve les phrases de définition. Les deux seules expressions sont récupérées dans cette publication. Aucune formule d’un autre régime, aucun coefficient financier recalculé ni changement des paramètres actuels.'}
write('zzh-concordance.json',concordance)
record=json.loads((P/'registry-proposal/records/LEGIARTI000049362876.json').read_text())
record.update(documentary_recovery_complete=True,official_jo_crosscheck_complete=True,authenticated_jo_crosscheck_complete=False,cryptographic_signature_validation_complete=False,status='verified_official_primary_documentary_recovery_ready_for_activation',ready_for_activation=True,count_as_completed=False,missing_elements=[],media=media,documents=[doc],transcriptions=[{'marker':n,'page':2,'text':txt,'verified_visually':True,'role':'Linearisation fidèle pour lecture/recherche ; l’image officielle reste la reproduction graphique.'}for n,txt in enumerate(linear,1)],proposed_xml=None,verification_date_utc=now,canonical_version_concordance_complete=True,canonical_version_concordance_notes='Source actuelle49septiesZZH depuis4avril2024, corps et note préservés. Ses deux renvois désignent expressément JO2010texte67; les huit paragraphes textuels correspondent au contexte2010, sous réserve de l’ajout courant «ou la société de financement», conservé. La table2010n’estpasimportée; la table courante1/2À4et75/55ainsiqueNOTA1avril2024restentexactes. Le texte officiel2024-304art9modifieseulement3en4dansl’entêtedeladernièrecolonne; art12confirme application1avril2024. Voirzzh-concordance.jsonetpreuveweb.',signature_notes='Extrait officiel JOE_TEXTE sans AcroForm, permission de signature ou annotations de page ; aucune signature PDF incorporée ni validation cryptographique revendiquée. L’origine officielle et le contenu du texte du JO sont contrôlés séparément.',provenance_notes='Trois pages officielles lues intégralement ; deux images originales exportées sans redessin et lues séparément. Bornes t=1 à T, exposant -t/12 des deux expressions, indices t des z et β, signe égal entre les deux sommes conservés. Ne pas remplacer l’expression annuelle par un taux mensuel, ni développer la somme par calcul. Les deux images seules complètent les renvois actuels ; le reste du corps et les notes restent intacts. Aucun registre actif, proposition de réécriture ou publication modifié.')
write('registry-proposal/records/LEGIARTI000049362876.json',record)
i=0
def substitute(match):
    global i
    if 'formule non reproduite'not in match.group():return match.group()
    item=media[i];i+=1
    return '<p><img src="'+item['path']+'" alt="'+html.escape(item['alt'],quote=True)+'"></p>'
recovered=re.sub(r'<p\b[^>]*>.*?</p>',substitute,src['source_xml'],flags=re.S)
assert i==2
assert re.search(r'<table\b.*?</table>',recovered,re.S).group()==re.search(r'<table\b.*?</table>',src['source_xml'],re.S).group()
(P/'zzh-source-with-recovered-graphics.html').write_text(recovered)
spec=importlib.util.spec_from_file_location('source_assets_ro',ROOT/'source_assets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
loaded=m.load_companions(P/'registry-proposal')
checks=[{'source_id':x['source_id'],'source_assets_schema_load_passed':True,'recovery_complete':m.recovery_complete(x['source_xml'],loaded[(x['code_id'],x['source_id'])])}for x in json.loads((P/'source-snapshot.json').read_text())]
assert sum(x['recovery_complete']for x in checks)==2 and m.recovered_content_present(recovered,record)
write('companion-validation.json',checks)
write('companion-record-proposals.json',[json.loads(x.read_text())for x in sorted((P/'registry-proposal/records').glob('*.json'))])
run=subprocess.run(['pdfsig','-nocert',str(pdf)],capture_output=True,text=True)
sig={'pdf_path':'documents/'+pdf.name,'pdf_sha256':sha(pdf),'catalog_has_acroform':'/AcroForm'in reader.trailer['/Root'],'catalog_has_permissions':'/Perms'in reader.trailer['/Root'],'page_annotation_counts':[len(x.get('/Annots')or[])for x in reader.pages],'digital_signature_present':False,'cryptographic_signature_validation_complete':False,'pdfsig_returncode':run.returncode,'pdfsig_stdout':run.stdout,'pdfsig_stderr':run.stderr,'interpretation':'Le PDF officiel extrait ne contient pas de signature incorporée ; aucune validation cryptographique du JO signé revendiquée.'}
write('zzh-signature-information.json',sig)
write('zzh-verified-provenance.json',{'inspected_at_utc':now,'document':doc,'source_id':src['source_id'],'source_sha256':src['source_sha256'],'documentary_recovery_complete':True,'official_jo_crosscheck_complete':True,'media':media,'canonical_current_table_and_note_preserved':True,'concordance_file':'zzh-concordance.json','signature_information_file':'zzh-signature-information.json','activation_performed':False,'rewrite_created':False})
report=json.loads((P/'report.json').read_text())
report.update(report_date_utc=now,status='two_primary_recoveries_verified_three_remaining',primary_normative_recoveries_completed=2,source_graphic_elements_recovered=4,source_graphic_elements_remaining=4,initial_missing_elements=8,missing_elements=4,documents_retrieved=3,documents_retrieved_relevant_to_missing_graphics=2,source_assets_schema_validation='5 notices chargées ; R254-5 et49septiesZZH recovery_complete=true, les3autresrestentfalse.')
report['verified_recoveries'].append({'source_id':src['source_id'],'number':'49septiesZZH','formula_count':2,'document':doc,'record':'registry-proposal/records/LEGIARTI000049362876.json','ready_for_activation':True,'activated':False,'counts_as_article_rewritten':False})
for x in report['specific_remaining_requirements']:
    if x['source_id']==src['source_id']:x.update(status='recovered_verified',missing=None,avenues='PDF officiel JOE_TEXTE reçu ;3pageslues,deuximagesoriginalesexportées ; corps/tableau75/55etNOTAactuels conservés. Voirzzh-concordance.json.')
write('report.json',report)
print(json.dumps({'verified_companion':str(P/'registry-proposal/records/LEGIARTI000049362876.json'),'recovery_complete':True,'current_table_preserved':True,'notes_preserved':True,'activation_performed':False}))
