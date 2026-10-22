from pathlib import Path
import json, hashlib, datetime, re, html, importlib.util, subprocess
from pypdf import PdfReader
P=Path(__file__).resolve().parent
ROOT=P.parents[2]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,data): (P/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
src=next(x for x in json.loads((P/'source-snapshot.json').read_text())if x['source_id']=='LEGIARTI000032792438')
pdf=P/'documents/joe_20160629_0150_0048.pdf'
assert sha(pdf)=='f5ba18bc1ae08e4b6a7a77272f3534135a3829f036cea81d42c5af9d8af2c991'
doc={'path':'documents/'+pdf.name,'sha256':sha(pdf),'url':'https://www.legifrance.gouv.fr/download/file/Sg8D8XoPE4qUiyh8_0ztpeDH88V2_zW0rTU0Ov0dQlU=/JOE_TEXTE','landing_url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032791452','label':'Légifrance/DILA, JORF 0150 du 29 juin 2016, texte 48 sur 130, décret 2016-855 du 27 juin 2016, NOR LHAL1422063D, article 2 ; extrait officiel complet de trois pages.','retrieved_date_utc':'2026-10-22','recovery_method':'Téléchargement navigateur normal par le parent à partir du lien explicite JOE_TEXTE de la page publique officielle ; transfert local du fichier PDF entier. Aucun CAPTCHA résolu ni cookie exporté selon le journal du parent.','bytes':pdf.stat().st_size,'page_count':3,'pages_visually_read_in_full':[1,2,3],'formula_pages':[2],'digital_signature_present':False,'cryptographic_signature_validation_complete':False}
con=json.loads((P/'r254-concordance.json').read_text())
assert all(x['pdf_text_match_after_typographic_normalization']for x in con['paragraph_checks'])
media=json.loads((P/'r254-images.json').read_text())
linear=["V_N = [VL_N * (1 - (1 + t_N)^(-n))] / t_N", "t_N = (Valeur du loyer annuel moyen au m²)_N / (Valeur de la vente moyenne au m²)_N"]
for item,text in zip(media,linear):
    item['verified_visually']=True
    item['documentary_status']='Image originale du fac-similé officiel Légifrance JOE_TEXTE, intégralement contrôlée sur la page 2 entière.'
    item['alt']=text
record=json.loads((P/'registry-proposal/records/LEGIARTI000032792438.json').read_text())
record.update(documentary_recovery_complete=True,official_jo_crosscheck_complete=True,authenticated_jo_crosscheck_complete=False,cryptographic_signature_validation_complete=False,status='verified_official_primary_documentary_recovery_ready_for_activation',ready_for_activation=True,count_as_completed=False,missing_elements=[],media=media,documents=[doc],transcriptions=[{'marker':i,'page':2,'text':s,'verified_visually':True,'role':'Linearisation fidèle pour lecture/recherche ; l’image officielle reste la reproduction graphique.'}for i,s in enumerate(linear,1)],proposed_xml=None,verification_date_utc=now,canonical_version_concordance_complete=True,canonical_version_concordance_notes='Les 12 paragraphes textuels de LEGIARTI000032792438, hors les deux renvois graphiques, correspondent au texte officiel intégral de la page 2 après normalisation exclusivement typographique. Les 14 paragraphes et les deux images ont été lus visuellement. Source unique en vigueur depuis le 30 juin 2016, lien créateur vers le décret 2016-855 art. 2, NOR LHAL1422063D et JO du 29 juin 2016, texte 48 concordants. La note canonique est vide et reste vide.',signature_notes='Le fichier JOE_TEXTE est un extrait officiel téléchargé sur Légifrance ; son catalogue ne contient pas d’AcroForm et aucune annotation de page ni signature PDF incorporée n’est présente. Il ne s’agit pas d’une validation cryptographique du numéro authentifié signé ; authenticated_jo_crosscheck_complete reste donc false par prudence sémantique. Cela ne retire rien à la récupération documentaire du texte officiel et de ses deux images.',provenance_notes='Vérifié sur la publication officielle complète de trois pages, et non sur Cheuvreux. Les deux images ont été exportées sans recadrage ni modification de leurs pixels ; égalité des pixels exportés avec les flux images PDF décodés vérifiée. Exposant -n, dénominateur t_N, index N des deux valeurs, unité m² et signe de multiplication * conservés. Aucun coefficient 100, changement de taux, hypothèse de t_N nul ou autre inférence ajouté. Aucun registre actif ni candidat de réécriture modifié. Le présent état est prêt pour activation documentaire distincte par le coordinateur ; il ne compte pas comme article réécrit.')
write('registry-proposal/records/LEGIARTI000032792438.json',record)
records=[json.loads(p.read_text())for p in sorted((P/'registry-proposal/records').glob('*.json'))]
write('companion-record-proposals.json',records)
i=0
def replace_marker(match):
    global i
    if 'Vous pouvez consulter' not in match.group():return match.group()
    item=media[i];i+=1
    return '<p><img src="'+item['path']+'" alt="'+html.escape(item['alt'],quote=True)+'"></p>'
recovered=re.sub(r'<p\b[^>]*>.*?</p>',replace_marker,src['source_xml'],flags=re.S)
assert i==2
(P/'r254-source-with-recovered-graphics.html').write_text(recovered)
spec=importlib.util.spec_from_file_location('source_assets_ro',ROOT/'source_assets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
loaded=m.load_companions(P/'registry-proposal')
checks=[]
for source in json.loads((P/'source-snapshot.json').read_text()):
    rec=loaded[(source['code_id'],source['source_id'])]
    checks.append({'source_id':source['source_id'],'source_assets_schema_load_passed':True,'recovery_complete':m.recovery_complete(source['source_xml'],rec)})
assert sum(x['recovery_complete']for x in checks)==1
assert m.recovered_content_present(recovered,record)
write('companion-validation.json',checks)
result=subprocess.run(['pdfsig','-nocert',str(pdf)],capture_output=True,text=True)
reader=PdfReader(pdf)
signature={'pdf_path':'documents/'+pdf.name,'pdf_sha256':sha(pdf),'inspected_at_utc':now,'catalog_has_acroform':'/AcroForm' in reader.trailer['/Root'],'catalog_has_permissions':'/Perms' in reader.trailer['/Root'],'page_annotation_counts':[len(page.get('/Annots') or [])for page in reader.pages],'digital_signature_present':False,'cryptographic_signature_validation_complete':False,'pdfsig_returncode':result.returncode,'pdfsig_stdout':result.stdout,'pdfsig_stderr':result.stderr,'interpretation':'Extrait JOE_TEXTE sans signature PDF incorporée ; origine officielle attestée par le téléchargement public et identité/contenu contrôlés. Aucune validation cryptographique du JO signé revendiquée.'}
write('r254-signature-information.json',signature)
write('r254-verified-provenance.json',{'inspected_at_utc':now,'document':doc,'source_id':src['source_id'],'source_sha256':src['source_sha256'],'documentary_recovery_complete':True,'official_jo_crosscheck_complete':True,'media':media,'textual_paragraphs_matched':12,'textual_paragraphs_expected':12,'notes_empty':True,'concordance_file':'r254-concordance.json','signature_information_file':'r254-signature-information.json','activation_performed':False,'rewrite_created':False})
report=json.loads((P/'report.json').read_text())
report.update(report_date_utc=now,status='one_primary_recovery_verified_four_remaining',provisional=False,primary_normative_recoveries_completed=1,source_graphic_elements_recovered=2,source_graphic_elements_remaining=6,documents_retrieved=2,documents_retrieved_relevant_to_missing_graphics=1,source_assets_schema_validation='5 notices chargées ; R254-5 recovery_complete=true, les 4 autres restent false.',verified_recoveries=[{'source_id':src['source_id'],'number':'R254-5','formula_count':2,'document':doc,'record':'registry-proposal/records/LEGIARTI000032792438.json','ready_for_activation':True,'activated':False,'counts_as_article_rewritten':False}],pending_parent_attempts=['Le parent poursuit les autres PDF officiels dans le navigateur ; aucun autre fichier reçu à ce stade.'])
for x in report['specific_remaining_requirements']:
    if x['source_id']==src['source_id']:
        x.update(status='recovered_verified',missing=None,avenues='PDF officiel JOE_TEXTE reçu ; 3 pages lues, 2 images extraites et concordées ; notice documentaire prête hors registre actif.')
write('report.json',report)
print(json.dumps({'verified_companion':str(P/'registry-proposal/records/LEGIARTI000032792438.json'),'recovery_complete':True,'recovered_graphics_present_in_review_copy':True,'matched_canonical_textual_paragraphs':12,'digital_signature_present':False,'activation_performed':False}))
