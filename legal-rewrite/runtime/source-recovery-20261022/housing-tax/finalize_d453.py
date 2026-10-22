from pathlib import Path
import json,hashlib,datetime,re,html,unicodedata,shutil,subprocess,importlib.util
from pypdf import PdfReader
from PIL import Image
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,data):(P/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
src=next(x for x in json.loads((P/'source-snapshot.json').read_text())if x['source_id']=='LEGIARTI000039048613')
pdf=P/'documents/joe_20071230_0303_0157.pdf'
assert sha(pdf)=='269015f17a3931e1adbd7cab09fa7920eebf9c45acefb5bf827a2edfed12bbe5'
reader=PdfReader(pdf);assert len(reader.pages)==2
shutil.copyfile(pdf,P/'registry-proposal/documents'/pdf.name)
image=reader.pages[0].images[0];assert image.image.size==(1535,262)
target=P/'registry-proposal/media/d453-7-formule-1-jo2007.png';image.image.save(target,format='PNG')
assert Image.open(target).tobytes()==image.image.tobytes()
linear="(maximum sur les quatre derniers trimestres de l'encours réel) x [moyenne de l'encours réel sur les quatre derniers trimestres / moyenne de l'encours réel sur quatre trimestres un an auparavant] x [encours réel au dernier trimestre / (5 x (somme des fonds propres dédiés))]"
media={'marker':1,'path':str(target.relative_to(P/'registry-proposal')),'sha256':sha(target),'width':1535,'height':262,'page':1,'pdf_image_name':image.name,'pdf_path':'documents/'+pdf.name,'decoded_pixel_sha256':hashlib.sha256(image.image.tobytes()).hexdigest(),'pixel_equality_verified':True,'extraction':'Export PNG de l’image CCITT 1 bit incorporée au PDF, sans recadrage, changement de résolution ni redessin ; pixels exportés identiques à l’image PDF décodée.','verified_visually':True,'documentary_status':'Formule du I de R453-7 publiée dans le fac-similé officiel, page 1 entière et image séparée lues visuellement.','alt':linear}
doc={'path':'documents/'+pdf.name,'sha256':sha(pdf),'url':'https://www.legifrance.gouv.fr/download/file/TFQj9gu0J44tYcNwc7AVDtieE4usNqEK-A0gjHu8w3E=/JOE_TEXTE','landing_url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017767416','label':'Légifrance/DILA, JORF 0303 du 30 décembre 2007, texte 157 sur 191, décret 2007-1941 du 26 décembre 2007, NOR MLVU0762969D, article 1 ; extrait officiel complet de deux pages.','retrieved_date_utc':'2026-10-22','recovery_method':'Téléchargement navigateur normal par le parent depuis le lien explicite public JOE_TEXTE ; fichier PDF entier transféré localement. Aucun CAPTCHA résolu ni cookie exporté selon le journal du parent.','bytes':pdf.stat().st_size,'page_count':2,'pages_visually_read_in_full':[1,2],'formula_pages':[1],'digital_signature_present':False,'cryptographic_signature_validation_complete':False}
def norm(t):
    t=html.unescape(re.sub('<[^>]+>',' ',t));t=unicodedata.normalize('NFKC',t).lower();t=re.sub(r'\bn(?:o|°)\s*(?=\d)','n',t);return re.sub(r'[^\w]','',t)
npdf=norm((P/'documents/joe_20071230_0303_0157.txt').read_text())
pars=re.findall(r'<p\b[^>]*>(.*?)</p>',src['source_xml'],re.S)
checks=[];ii=[]
for index,body in enumerate(pars,1):
    text=html.unescape(re.sub('<[^>]+>',' ',body)).strip()
    if 'consulter la formule' in text or text.startswith('n° 303'):continue
    if index>=14:
        ii.append({'canonical_paragraph':index,'canonical_text':text,'preserved_from_current_canonical_source':True,'not_replaced_by_2007_decree':True});continue
    comparison=text.replace('D. 453-2','R. 453-2')
    checks.append({'canonical_paragraph':index,'canonical_text':text,'pdf_text_match_after_typographic_normalization_and_documented_2019_reference_change':norm(comparison)in npdf,'documented_version_difference':'Renvoi actuel D453-2, anciennement R453-2 : décret 2019-873, art. 6 IV 48°.'if comparison!=text else ''})
assert len(checks)==11 and all(x['pdf_text_match_after_typographic_normalization_and_documented_2019_reference_change']for x in checks)and len(ii)==2
con={'source_id':src['source_id'],'source_sha256':src['source_sha256'],'valid_from':src['valid_from'],'valid_until':src['valid_until'],'source_notes_xml':src['source_notes_xml'],'notes_empty':not src['source_notes_xml'],'pages_visually_read_in_full':[1,2],'canonical_I_textual_paragraphs_matched':checks,'current_II_preserved':ii,'2019_primary_evidence':{'url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038947944','article5_II_4':'Les articles R453-1 à R453-8 sont identifiés par un D comme relevant d’un décret.','article6_IV_48':'A l’article D453-7, tel que modifié par l’article5, la référence R453-2 est remplacée par D453-2.','article8_I':'Entrée en vigueur le 1er septembre 2019.','evidence_file':'d453-current-version-web-evidence.json'},'formula_scope':'Le décret 2007-1941 remplace seulement le I de R453-7 ; le II actuel n’est pas extrait de ce PDF et demeure intégralement celui de la source canonique. Seul le graphique désigné expressément par la source est complété.','source_media_mapping':[media]}
write('d453-concordance.json',con)
record=json.loads((P/'registry-proposal/records/LEGIARTI000039048613.json').read_text())
record.update(documentary_recovery_complete=True,official_jo_crosscheck_complete=True,authenticated_jo_crosscheck_complete=False,cryptographic_signature_validation_complete=False,status='verified_official_primary_documentary_recovery_ready_for_activation',ready_for_activation=True,count_as_completed=False,missing_elements=[],media=[media],documents=[doc],transcriptions=[{'marker':1,'page':1,'text':linear,'verified_visually':True,'role':'Linearisation fidèle du produit pour lecture/recherche ; l’image officielle reste la reproduction graphique.'}],proposed_xml=None,verification_date_utc=now,canonical_version_concordance_complete=True,canonical_version_concordance_notes='Les onze paragraphes textuels du I correspondent au décret 2007-1941, à la seule différence documentée du renvoi R453-2 devenu D453-2 en 2019. Le décret 2019-873, art. 5 II 4°, identifie R453-7 par la lettre D ; art. 6 IV 48° coordonne ce renvoi ; art. 8 fixe le 1er septembre 2019. Le II canonique entier, non modifié par le décret 2007, est préservé ; note canonique vide. La source actuelle renvoie expressément au JO 2007 texte 157 pour son graphique.',signature_notes='Le PDF possède un AcroForm vide et des annotations Link de navigation ; aucun champ de signature n’est présent et pdfsig indique aucune signature. Aucune validation cryptographique du JO signé revendiquée ; origine officielle et contenu contrôlés séparément.',provenance_notes='Deux pages officielles lues entièrement et formule originale lue séparément. Les trois facteurs, les deux fractions et le coefficient 5 au dénominateur sont conservés exactement. Aucun signe égal ni inégalité n’est ajouté au graphique, aucune simplification ou formule professionnelle substituée. La condition textuelle « plus de dix fois » du premier alinéa reste intacte. Aucun registre actif, projet de réécriture ou publication modifié.')
write('registry-proposal/records/LEGIARTI000039048613.json',record)
i=0
def substitute(match):
    global i
    if 'Vous pouvez consulter la formule'not in match.group():return match.group()
    i+=1
    return '<p><img src="'+media['path']+'" alt="'+html.escape(linear,quote=True)+'"></p>'
recovered=re.sub(r'<p\b[^>]*>.*?</p>',substitute,src['source_xml'],flags=re.S)
assert i==1
source_ii=src['source_xml'][src['source_xml'].index('<p>II.-'):]
assert recovered[recovered.index('<p>II.-'):]==source_ii
(P/'d453-source-with-recovered-graphics.html').write_text(recovered)
spec=importlib.util.spec_from_file_location('source_assets_ro',ROOT/'source_assets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
loaded=m.load_companions(P/'registry-proposal')
checks_schema=[{'source_id':x['source_id'],'source_assets_schema_load_passed':True,'recovery_complete':m.recovery_complete(x['source_xml'],loaded[(x['code_id'],x['source_id'])])}for x in json.loads((P/'source-snapshot.json').read_text())]
assert sum(x['recovery_complete']for x in checks_schema)==3 and m.recovered_content_present(recovered,record)
write('companion-validation.json',checks_schema)
write('companion-record-proposals.json',[json.loads(x.read_text())for x in sorted((P/'registry-proposal/records').glob('*.json'))])
run=subprocess.run(['pdfsig','-nocert',str(pdf)],capture_output=True,text=True)
annots=[]
for page in reader.pages:
    a=page.get('/Annots');a=a.get_object()if a is not None else []
    annots.append({'count':len(a),'types':[str(x.get_object().get('/Subtype'))for x in a]})
sig={'pdf_path':'documents/'+pdf.name,'pdf_sha256':sha(pdf),'catalog_has_acroform':True,'acroform_fields':reader.get_fields(),'page_annotations':annots,'digital_signature_present':False,'cryptographic_signature_validation_complete':False,'pdfsig_returncode':run.returncode,'pdfsig_stdout':run.stdout,'pdfsig_stderr':run.stderr,'interpretation':'AcroForm vide et six liens de navigation, sans signature PDF incorporée ; aucune validation cryptographique du JO signé revendiquée.'}
write('d453-signature-information.json',sig)
write('d453-verified-provenance.json',{'inspected_at_utc':now,'document':doc,'source_id':src['source_id'],'source_sha256':src['source_sha256'],'documentary_recovery_complete':True,'official_jo_crosscheck_complete':True,'media':[media],'current_II_and_notes_preserved':True,'concordance_file':'d453-concordance.json','signature_information_file':'d453-signature-information.json','activation_performed':False,'rewrite_created':False})
report=json.loads((P/'report.json').read_text());report.update(report_date_utc=now,status='three_primary_recoveries_verified_two_remaining',primary_normative_recoveries_completed=3,source_graphic_elements_recovered=5,source_graphic_elements_remaining=3,initial_missing_elements=8,missing_elements=3,documents_retrieved=4,documents_retrieved_relevant_to_missing_graphics=3,source_assets_schema_validation='5 notices chargées ; R254-5, D453-7 et49septiesZZH recovery_complete=true, les2autresrestentfalse.')
report['verified_recoveries'].append({'source_id':src['source_id'],'number':'D453-7','formula_count':1,'document':doc,'record':'registry-proposal/records/LEGIARTI000039048613.json','ready_for_activation':True,'activated':False,'counts_as_article_rewritten':False})
for x in report['specific_remaining_requirements']:
    if x['source_id']==src['source_id']:x.update(status='recovered_verified',missing=None,avenues='PDF officiel JOE_TEXTE reçu ; deux pages lues, formule originale exportée, renumérotation 2019 et renvoi D453-2 vérifiés ; II canonique intact.')
write('report.json',report)
print(json.dumps({'verified_companion':str(P/'registry-proposal/records/LEGIARTI000039048613.json'),'recovery_complete':True,'current_II_preserved':True,'activation_performed':False}))
