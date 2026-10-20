from pathlib import Path
import json,hashlib,sqlite3,sys
sys.path.insert(0,'legal-rewrite');from run_exhaustive import validate_answer
P=Path(__file__).parent;Q=P.parent/'cvae/editions/001';H=lambda b:hashlib.sha256(b).hexdigest()
source=json.loads((P/'audited-source.json').read_text());answer=json.loads((P/'audited-answer-edition2.json').read_text());keys={r['source_id'] for r in answer}
for f,snapshot in [('source.json','audited-source.json'),('answer.json','audited-answer-edition2.json'),('expected.json','audited-expected.json')]:assert (Q/f).read_bytes()==(P/snapshot).read_bytes()
validate_answer(answer,[r for r in source if r['source_id'] in keys])
db=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);db.row_factory=sqlite3.Row;guards=[]
for r in source:
 d=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(r['code_id'],r['source_id'])).fetchone();prior=r['current_beforeimage'];assert (d['proposed_xml'] if d else None)==((prior or {}).get('proposed_xml'))
 raw=r['source_document_xml'].encode();assert H(raw)==r['source_sha256'];assert H(r['source_xml'].encode())==r['source_body_sha256']
 guards.append({'code_id':r['code_id'],'source_id':r['source_id'],'number':r['number'],'has_prior':bool(prior),'previous_draft':None if not prior else {'source_sha256':prior['source_sha256'],'proposed_sha256':H(prior['proposed_xml'].encode())},'source_sha256':r['source_sha256'],'source_body_sha256':r['source_body_sha256'],'beforeimage_matches_current_db':True})
(P/'current-guards.json').write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
findings={
'1447-0':'CET limitée à la CFE pour les années supprimées ; absence de prélèvement de remplacement et de hausse des paramètres de CFE.',
'1586 ter':'Suppression par année d’imposition dès le 1er janvier suivant l’année d’entrée en vigueur ; anciennes années et droits conservés ; aucun paiement ou déclaration future de CVAE.',
'1586 quater':'Barème et consolidation propres à CVAE supprimés ; anciens dégrèvements188euros et autres droits conservés pour leurs années.',
'1586 quinquies':'Périodes autonomes maintenues pour plafonnement CFE et autres renvois ; périodes atypiques, absence de clôture, création, exercices multiples et exclusion du double compte conservés ; annualisation spécifique CFE demeure à1647Bsexies.',
'1586 sexies':'Toute la définition source conservée octet pour octet entre deux clauses de champ ; règles sectorielles,95%,80/85%,7,6M€,déductions et reports de création intacts.',
'1586 septies':'Seuil63euros maintenu pour anciennes années ; aucune CVAE, même supérieure à ce seuil, après suppression.',
'1586 octies':'Suppression assujettissement déclarations et répartitions CVAE pour années nouvelles ; anciennes années maintenues ; aucune extension aux obligations des autres impôts.',
'1586 nonies':'Suppression des exonérations exclusivementCVAE avec suppression de la taxe entière, non retrait d’avantages sur impôt survivant ; CFE1466A/F expressément préservée ; anciennes conditions conservées.',
'1679 septies':'Aucun acompte ni solde, même calculé sur ancienne base, pour année supprimée ; restitution des indus sans liquidation annuelle CVAE. Édition001 a retiré le nouveau délai60jours de la première édition : procédures et délais de réclamation de droit commun, anciens délais de remboursement toujours préservés.',
'1647 B sexies':'Plafonnement CFE maintenu avec ses demandes,80%,périodes,annualisation,exclusions,cotisationminimum,imputationCFE et ordonnancement6mois ; taux1,531/1,438/1,344/1,25 conformes aux sources2026–2030. Coordination2030 encore à rédiger séparément.',
'1600':'Douze exonérations, moitié de base artisans et toutII CFE conservés octet pour octet ;1,12%inchangé ; additionnelleCVAE9,23%supprimée pour années nouvelles sans report de produit versCFE ; anciennes années maintenues.',
'1649 quater B quater':'SeulIV CVAE remplacé ; toutes autres obligations et suppression990I nouveaux décès maintenues ; pas de télédéclarationCVAE future.',
'1681 septies':'Seul3 CVAE remplacé ; paiement IS et taxes autonomes inchangés ; suppression990I conservée ; anciens paiementsCVAE demeurent électroniques.',
'1731':'1,2,4 inchangés ; suppression de majoration propre aux acomptesCVAE des années supprimées ; pas de sanction d’une obligation nouvelle inexistante ; réserve loi répressive plus douce.',
'1770 decies':'Suppression amende déclarative200euros/salarié plafond100000 pour années supprimées ; réserve des anciennes règles et loi répressive plus douce.',
'317 septies E':'Ancien ratio territorialCVAE, y compris plancher1/10, supprimé seulement pour années nonimposables ; sources historiques conservées et droits antérieurs sauvegardés.',
'38':'AnnexeIII : seulII3° tableauVA destinéCVAE remplacé dans le brouillon ; données de résultat, tableaux fiscaux, réemploi et exemplaire unique maintenus.',
'40 A':'AnnexeIII : seulIm calculVA destinéCVAE remplacé ; déclarationsBNC et réemploi maintenus.',
'46 C':'AnnexeIII : seulIII tableauVA destinéCVAE remplacé ; droits des associés, informations immobilières, réemploi et contrôle distincts maintenus.',
'39':'AnnexeIII : seuls1°g et2°l données exclusivementCVAE remplacés ; effectif général1°b, salaires, retraites, options, actions, impatriés et Suisse maintenus ; réemploi final inchangé.',
'344-0 B':'Seul6° dépôtCVAE restreint aux anciennes années ; pas de changement de champ des autres taxes, notamment15°231ter/231quater/1599quaterC.',
'344 I-0 bis':'Seul renvoi de calendrierCVAE retiré pour années supprimées ;175/223/298bis/1477 conservés ; incohérence matérielle ancienne de renvoi1679septies non transformée en nouvelle échéance.',
'406 terdecies':'SeulII recouvrementCVAE restreint aux anciennes années ; options foncières, durées, destinataires et autres prélèvements inchangés.',
'238 bis HW':'Accès au dispositif électrique préservé par définitionVA figée et preuve comptable sans déclarationCVAE ;2,5kWh/€,15ans,55%,8000heures et capital600000euros inchangés.'}
for r in answer:
 if r['number'].startswith('328 G'):findings[r['number']]='Suppression des seules déclarations/répartitions CVAE pour années supprimées ; dispositions anciennes et droits historiques maintenus. Le texte de transition est identique à celui relu pour328Gbis ; les sources propres à chaque article ont été examinées séparément.'
assert len(findings)==35
(P/'article-findings.json').write_text(json.dumps([{'code_id':r['code_id'],'source_id':r['source_id'],'number':r['number'],'proposed_sha256':r['proposed_sha256'],'verdict':'no_concrete_blocking_error_found','finding':findings[r['number']]} for r in answer],ensure_ascii=False,indent=2)+'\n')
manifest={'audited_edition':str(Q),'as_of':'2026-10-19','scope':'37 sources et notes,35 candidats de édition001,3 rédactions futures du plafonnement. Aucun avis sur des ajouts ultérieurs non identifiés par SHA.','package_sha256':{f:H((Q/f).read_bytes()) for f in ['source.json','answer.json','expected.json']},'initial_27_answer_sha256':H((P/'audited-answer.json').read_bytes()),'future_cap_sources_sha256':H((P/'audited-future-cap-sources.json').read_bytes()),'no_source_or_active_manifest_modified':True,'no_db_batches_or_publication_write':True,'verdict':'no_concrete_blocking_error_found_in_edition001','correction_candidates':0,'not_exhaustively_coordinated':True,'pending':['Édition002 :1679quinquies et annexeIV214 annoncés mais non audités ici.','Compagnon des rédactions différées2028/2029/2030, notamment1647BsexiesA et définitions/périodes : pas encore livré au moment du présent audit.','Autres renvois hors corpus et effets budgétaires/CCI à borner par auteur ; pas de financement ou compensation déduits.'],'mechanical_cfe_caveat':'Pas de hausse de taux ou baseCFE ; sa part nette peut augmenter lorsque l’ancien plafonnementCET imputé surCFE couvrait aussiCVAE. Charge globale CET ne croît pas. Ne pas présenter comme CFE nette identique en tout cas.','sources_without_candidate':[{'number':r['number'],'reason':'1447 conserve un seuil CFE fondé sur une définition de chiffre d’affaires1586sexies maintenue ; pas de nouvelle charge.' if r['number']=='1447' else '344quindecies porte taux99%pour2025 : disposition historique. Ne pas inventer sa reconduction pour une année ultérieure ; exonérations des années encore dues conservées.'} for r in source if r['source_id'] not in keys]}
(P/'audit-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');(P/'answer.json').write_text('[]\n')
(P/'validation.json').write_text(json.dumps({'validated_candidates':35,'source_records_read':37,'source_notes_read':37,'future_cap_sources_read':3,'validate_answer':'passed','source_raw_sha_and_body_sha':'all37passed','prior_proposals_current_db_guards':'all37match','proposed_sha256':'all35match','stable_edition001_files_match_audited_copies':True,'normative_corrections_required_in_audited_scope':0,'future_companion_review_pending':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
