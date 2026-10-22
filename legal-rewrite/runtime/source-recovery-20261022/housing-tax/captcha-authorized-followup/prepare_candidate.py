"""Prepare the isolated A123-1 companion and evidence; never activate it."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, html, re, shutil, xml.etree.ElementTree as ET

BASE=Path(__file__).resolve().parent
REG=BASE/'registry-proposal'
ROOT=BASE.parents[3]
NOW=datetime.now(timezone.utc).isoformat()
sha=lambda data:hashlib.sha256(data).hexdigest()
write=lambda path,obj:path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
history=json.loads((BASE/'canonical-history.json').read_text())
current=next(x for x in history['versions']if x['id']=='LEGIARTI000006813811')
body=current['content_xml']
official='La représentation des différentes servitudes mentionnées aux I et II de l’article R. 123-18 et pouvant figurer sur les documents graphiques du plan d’occupation des sols est fixée conformément à la légende annexée au présent article.'
normalize=lambda s:' '.join(html.unescape(re.sub('<[^>]+>',' ',s)).replace('’',"'").split())
canon=normalize(body)
canon_without_omission=canon.replace(' (non reproduite, voir JONC du 17 juillet 1984)','')
assert canon_without_omission==normalize(official)
assert current['valid_from']=='1984-07-17'
raw=(BASE/current['xml_path']).read_bytes()
assert sha(raw)==current['source_sha256']==current['document_sha256']=='c58d74ee3fa7ec9e7e634feaa0f1f5005b646a9b5bc77df666685db87c9bb882'
notes=ET.fromstring(raw).find('NOTA/CONTENU')
assert notes is not None and not ''.join(notes.itertext()).strip()
assert not list(notes)

labels=[
 'Zone','Zone industrielle (ou trame plus aérée)','Secteur','Plan de masse',
 'Secteur de point de vue','Secteur de point à voir',
 'Espace boisé classé à conserver ou à créer au titre du L. 130-1',
 'Terrain cultivé à protéger (en zone urbaine)','Plantation à réaliser',
 'Emplacement réservé pour ouvrage public, installation d’intérêt général ou espace vert',
 'Emplacement réservé pour voie ou passage public à créer',
 'Emplacement réservé pour voie publique à élargir',
 'Emplacement réservé pour voie publique à élargir (faible élargissement)',
 'Emplacement réservé pour rue ou sentier piétonnier à créer',
 'Emplacement réservé pour piste cyclable à créer',
 'Numéro d’opérations (renvoie à la liste des emplacements réservés)',
 'Emprise maximale de construction','Règle architecturale particulière',
 'Alignement le long duquel le dépassement du C.O.S. est permis',
 'Alignement le long duquel le dépassement du C.O.S. peut être imposé',
 'Reculement','Ligne à haute tension',
 'Voie existante à conserver (voie publique ou chemin rural)',
 'Cheminement piétonnier existant à conserver','Piste cyclable à conserver',
 'Voie bruyante de type I. (Bruit fort)','Voie bruyante de type II. (Bruit modéré).',
 'Secteur sauvegardé (date de création)',
 'Z.A.C. dont le P.A.Z. est approuvé (Indiquer la date d’approbation du P.A.Z.)',
 'Z.A.C. seulement créée. (Indiquer la date)',
 'Périmètre sensible (zone de préemption indiquer la date)',
 'Z.A.D. (Indiquer la date de création)',
 'Périmètre de concession d’usage de certains terrains urbains (date de création à indiquer)',
 'Zone de rénovation urbaine (date de création à indiquer)',
 'Zone de résorption de l’habitat insalubre (date de création à indiquer)',
 'Zone à urbaniser par priorité (date de création à indiquer)',
 'Périmètre de développement prioritaire pour l’utilisation de la chaleur (date de création à indiquer)',
 'Périmètres d’action forestière (date de création à indiquer)',
 'Périmètres miniers (date de création à indiquer)',
 'Périmètres de zones spéciales de recherche et d’exploitation de carrières et des zones d’exploitation et d’aménagement coordonné de carrières. (date de création à indiquer)',
]
assert len(labels)==40
inventory=[]
for num,label in enumerate(labels,1):
    page=14 if num<=8 else 15 if num<=20 else 16 if num<=32 else 17
    group='1.A Les zones et les secteurs' if num<=6 else '1.B Les autres indications' if num<=27 else '2.A Périmètres exclus du champ d’application du P.O.S.' if num<=29 else '2.B Zonages reportés à titre d’information'
    inventory.append({'number':num,'label_read_visually':label,'original_pdf_page':page,
                      'original_printed_page':6172+page,'group':group,
                      'original_symbol_retained_in_image':True,'label_symbol_and_parenthetical_mentions_visually_checked':True})
write(BASE/'legend-inventory.json',{
    'source':'JO NC du17juillet1984, annexe POS p.6186-6189',
    'status':'Auxiliary reading index, not a replacement for the original graphical legend.',
    'title':'Tableau des légendes affectant les servitudes d’urbanisme mentionnées à l’article 1er du présent arrêté.',
    'major_headings':['1. PRESCRIPTIONS EDICTEES PAR LE P.O.S.','2. PRESCRIPTIONS REPORTEES SUR LE P.O.S.'],
    'rows':inventory,'all_row_numbers_continuous_1_through_40':True,
    'no_separate_annex_footnote_after_row40_before_next_act':True,
    'symbols_are_not_ocr_or_redrawn':True,
    'examples_preserved_without_new_normative_interpretation':'Circled operation numbers, letters, hatch patterns, solid/hollow shapes, line styles, the15m graphical example and all date instructions remain the original pixels.'})

concordance={
    'verified_at_utc':NOW,'source_id':current['id'],'source_sha256':current['source_sha256'],
    'code_id':current['code_id'],'number':'A123-1','valid_from':current['valid_from'],'valid_until':current['valid_until'],
    'canonical_full_body':body,'canonical_notes_xml_exact':current['notes_xml'],
    'manually_read_official_article_2_II_text':official,'official_pdf_page':14,'official_printed_page':6186,
    'comparison':'Exclusive normalization of apostrophe glyphs, spaces and HTML markup; export omission parenthesis removed for comparison only.',
    'canonical_body_matches_official_in_full_except_documentary_omission_marker':True,
    'canonical_body_changed':False,'canonical_notes_empty_and_preserved':True,
    'direct_annex_link':'Arrêté POS du11mai1984 art.1→annexe ; art.2II insère A123-1 renvoyant à cette même légende. Tableau commence sur la même p.6186 et se poursuit sans interruption jusqu’à la ligne40 p.6189.',
    'annex_title_matches_urbanisme_not_utilite_publique':True,'annex_complete_40_rows':True,
    'pages_original_pdf':[14,15,16,17],'pages_original_printed':[6186,6187,6188,6189],
    'sup_distinction':{'different_act_begins_original_pdf_page':17,'different_act_begins_printed_page':6189,
                       'different_act_reference':'R.126-1 / A.126-1','sup_annex_begins_pdf_page':18,
                       'sup_annex_begins_printed_page':6190,'sup_excluded_from_companion':True},
    'other_historical_a123_1':{'id':'LEGIARTI000006813810','valid_from':'1977-01-18','valid_until':'1978-07-07',
        'state':'ABROGE','scope':'Ancienne autorisation d’établissements dangereux, insalubres ou incommodes ; matière différente, pas une version antérieure de la présente légende.',
        'not_imported':True},
    'public_web_current_read_attempt':'Direct web reader unavailable and exact-ID search empty in this pass. Concordance is established against the preserved canonical target version and the complete official facsimile, not an inferred current-web result.',
}
write(BASE/'canonical-concordance.json',concordance)

original=BASE.parent/'documents/JORF_NC_19840717_165.pdf'
original_sha=sha(original.read_bytes())
assert original_sha=='1c7710e196cb6845326ecaa00eda9580ba69cd0a6538e1aac7784d36c1e696ed' and original.stat().st_size==21785371
provenance={
    'verified_at_utc':NOW,'whole_original_local_path':str(original),'whole_original_bytes':original.stat().st_size,
    'whole_original_sha256':original_sha,'whole_original_page_count':48,
    'edition':'JORF numéro0165, numéro complémentaire, 17juillet1984',
    'access_route_url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000292388',
    'access_route_is_sup_act_not_pos_identity':True,
    'observed_download_landing_url':'https://www.legifrance.gouv.fr/download/securePrint?token=ZF5ryfZFouqVzYx!chh3',
    'observed_actual_file_url':'https://www.legifrance.gouv.fr/download/secure/file/ZF5ryfZFouqVzYx!chh3',
    'temporary_download_token_may_expire':True,
    'authorization_record':'runtime/source-recovery-20261022/captcha-authorization-20261022.json',
    'download_manifest':'runtime/source-recovery-20261022/authorized-downloads.json',
    'method':'Parent downloaded the official complete PDF through normal browser access after explicit user authorization for the four listed CAPTCHA controls; byte-exact local copy independently hashed here.',
    'security_bypass':False,'cookies_exported':False,'captcha_authorized_by_user':True,
    'whole_original_in_public_companion_documents':False,
    'local_excerpt_is_not_the_downloaded_whole_journal':True,
    'cryptographic_signature_validation_complete':False,
}
write(BASE/'official-provenance.json',provenance)
for src in [ROOT/'runtime/source-recovery-20261022/captcha-authorization-20261022.json',ROOT/'runtime/source-recovery-20261022/authorized-downloads.json']:
    if src.is_file():shutil.copyfile(src,BASE/'preuves'/src.name)

crops=json.loads((BASE/'crop-specification.json').read_text())
excerpt=json.loads((BASE/'excerpt-integrity.json').read_text())
media=[]
for i,item in enumerate(crops,1):
    media.append({**{k:v for k,v in item.items()if k not in ['source_path']},
        'marker':1,'part':i,'of_parts':4,'pdf_path':excerpt['path'],'page':i,'excerpt_pdf_page':i,
        'source_pdf_page':item['page'],'original_jo_sha256':original_sha,
        'extraction':'Original embedded JPEG2000 scan decoded losslessly to RGB; integer-coordinate crop only. Original sRGB ICC profile preserved. No resampling, rotation, retouch, OCR or redrawing. The excerpt PDF embeds exactly these same cropped pixel bytes and profile.',
        'pixel_equality_verified':True,'verified_visually':True,
        'alt':f"Extrait local de l’annexe POS de1984, partie{i}/4, page originale{item['printed_page']}, entrées{item['row_range'][0]} à{item['row_range'][1]}, symboles et mentions d’origine."})
record={
    'code_id':current['code_id'],'source_id':current['id'],'source_sha256':current['source_sha256'],
    'number':'A123-1','expected_markers':1,'documentary_recovery_complete':True,
    'official_jo_crosscheck_complete':True,'authenticated_jo_crosscheck_complete':False,
    'cryptographic_signature_validation_complete':False,
    'status':'verified_official_primary_documentary_recovery_ready_for_activation',
    'canonical_version_concordance_complete':True,'canonical_notes_preserved':True,
    'source_read_in_full':True,'notes_read_in_full':True,'media':media,'transcriptions':[],
    'documents':[{
        'path':excerpt['path'],'sha256':excerpt['sha256'],'bytes':excerpt['bytes'],'page_count':4,
        'label':'EXTRAIT LOCAL de l’annexe POS seule, arrêté du11mai1984, JORF numéro complémentaire du17juillet1984, p.6186-6189 ; 40entrées et tous symboles. Recadrages documentés ; aucune légende SUP incluse.',
        'document_kind':'locally_created_faithful_excerpt_of_official_scan',
        'is_official_downloaded_whole_pdf':False,'original_whole_jo_sha256':original_sha,
        'original_whole_jo_bytes':21785371,'original_whole_jo_page_count':48,
        'original_pdf_pages':[14,15,16,17],'original_printed_pages':[6186,6187,6188,6189],
        'retrieved_date_utc':'2026-10-22','created_excerpt_date_utc':'2026-10-22',
        'official_access_route_url':provenance['access_route_url'],
        'official_whole_file_observed_url':provenance['observed_actual_file_url'],
        'url_note':'Temporary authorized official whole-JO download URL, not a URL for the locally created excerpt; route SUP is access only.',
        'recovery_method':provenance['method'],'pages_visually_read_in_full':[1,2,3,4],
        'digital_signature_present':False,'cryptographic_signature_validation_complete':False,
    }],
    'primary_reference_url':'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006813811',
    'official_access_route_url':provenance['access_route_url'],'official_access_route_is_not_pos_normative_identity':True,
    'missing_elements':[],
    'canonical_version_concordance_notes':'Une phrase canonique comparée en entier à l’art.2II imprimé p.6186 : concordance après normalisation typographique et retrait, pour comparaison seulement, du renvoi d’export non reproduite. Art.1 et art.2II rattachent directement les40entrées de l’annexe à A123-1/R123-18I-II. NOTA vide conservée. Ancien A123-1 de1977, de matière différente, exclu. SUP/A126-1 commence après la ligne40, exclu.',
    'provenance_notes':'Original officiel complet gardé uniquement dans runtime comme preuve locale. Le compagnon contient seulement quatre portions de l’annexe POS, avec tous symboles, titres, libellés et mentions parenthétiques. Pixels sRGB et profil ICC d’origine conservés. Extrait local explicitement identifié, aucun OCR masqué ou contenu recadré restant incorporé. Aucune adaptation CNIG, SUP ou dessin reconstitué. Aucun texte canonique, registre actif, lot ou processus modifié.',
    'signature_notes':'Fac-similé officiel ancien sans validation cryptographique incorporée revendiquée ; ne pas confondre origine officielle et validation d’une signature. Extrait local non signé.',
    'ready_for_activation':True,'count_as_completed':False,'proposed_xml':None,
    'verification_date_utc':NOW,
}
write(REG/'records/LEGIARTI000006813811.json',record)

markup='<h1>A123-1 : annexe POS de1984</h1><p>Extrait local fidèle de l’annexe seule, arrêté du11mai1984, JORF numéro complémentaire du17juillet1984, p.6186-6189. Recadrages des pages6186 et6189, sans retouche des pixels. La légende SUP voisine est exclue.</p>'+body
for item in media:
    markup+=f"<p>Extrait, partie{item['part']}/4 : page originale{item['printed_page']}, entrées{item['row_range'][0]} à{item['row_range'][1]}.</p><img style='width:100%;height:auto' src='{item['path']}' alt='{html.escape(item['alt'],quote=True)}'>"
markup+=f"<p><a href='{excerpt['path']}'>Extrait PDF local de l’annexe POS seule</a></p>"
(REG/'a123-1-source-with-recovered-legend.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><title>A123-1 - extrait de l’annexe POS</title><body style="max-width:950px;margin:auto;font-family:serif">'+markup+'</body></html>')
print(json.dumps({'source_id':record['source_id'],'complete_legend_rows':len(inventory),'companion_media_parts':len(media),'document_path':excerpt['path'],'ready_for_activation':True,'activated':False},ensure_ascii=False))
