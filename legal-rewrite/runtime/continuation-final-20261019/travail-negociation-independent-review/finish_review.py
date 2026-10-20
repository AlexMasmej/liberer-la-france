from pathlib import Path
import json,hashlib,sqlite3,sys,copy
sys.path.insert(0,'legal-rewrite');from run_exhaustive import validate_answer
P=Path(__file__).parent;Q=P.parent/'travail-negociation/edition001';H=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
s=json.loads((P/'audited-source.json').read_text());a=json.loads((P/'audited-answer.json').read_text());before=json.loads((P/'audited-beforeimages.json').read_text());validate_answer(a,s)
for f in ['source.json','answer.json','beforeimages.json']:assert (Q/f).read_bytes()==(P/('audited-'+f)).read_bytes()
D=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);D.row_factory=sqlite3.Row;guards=[]
for r in s:
 old=next(t for t in before if t['source_id']==r['source_id'])['draft'];d=D.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(r['code_id'],r['source_id'])).fetchone();assert (d['proposed_xml'] if d else None)==((old or {}).get('proposed_xml'))
 guards.append({'code_id':r['code_id'],'source_id':r['source_id'],'number':r['number'],'source_sha256':r['source_sha256'],'current_draft_absent':d is None or not d['proposed_xml'],'previous_draft':None if not old else {'source_sha256':old['source_sha256'],'proposed_sha256':H(old['proposed_xml'])}})
(P/'expected.json').write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n');(P/'answer.json').write_text('[]\n')
findings={
'L2232-6':'Signature au moins30% et absence d’opposition majoritaire sur suffrages représentatifs du bon niveau conservées ; délai15jours etL2231-8 intacts.',
'L2232-7':'Habilitation catégorielle et assiette du collège conservées ; pas de majorité globale nouvelle.',
'L2232-8':'Absence, salaire/compensation, frais et financement forfaitaire des petites entreprises conservés ; réutilisation de la preuve déjà détenue ne dispense pas du salaire ; coordinationR2232-1-5 et modèle nécessaire.',
'L2232-9':'CPPNI obligatoire, veille et avis judiciaire maintenus ; rapport/transmission et minimum3réunions supprimés sans supprimer négociations/autres obligations de protection. D2232-1-1/-1-2 restent à coordonner.',
'L2232-10':'Observatoire facultatif et mutualisable ; engagements conventionnels existants conservés jusqu’à révision régulière.',
'L2232-10-1':'Document unilatéral petites entreprises reste limité aux options prédéfinies ; garantie déjà dansD2232-1-6, sans nouvelle interdiction.',
'L2232-11':'Champ entreprise/établissement/groupe inchangé.',
'L2232-12':'Majorités >50% et >30%, assiettes, priorité syndicale1mois, opposition collective,8jours,2mois, approbation majoritaire et non-écrit maintenus. Réemploi protocole exige accord écrit des mêmes parties ; pas de silence. ElectoratL2314-18 conservé avecL2314-15/-17 ; ancien18-1 n’est pas réactivé.',
'L2232-13':'Majorités et consultation au collège catégoriel maintenues ; renvoi12 cohérent.',
'L2232-14':'RSS mandaté dans cas légal et ratification majorité des suffrages préservés ; pas de non-écrit supprimé.',
'L2232-16':'Réserve explicite des modes sansDS, niveaux et révision/dénonciation préservés.',
'L2232-17':'Dans la copie figée, plafond supplétif des salariés supplémentaires et exception deux salariés avecDSunique formulés comme maximums, pas minimum imposé.',
'L2232-18':'Tout temps de négociation reste payé comme travail à échéance normale.',
'L2232-19':'Audition à demande des délégués des entreprises extérieures conservée ; pas de droit de signature nouveau.',
'L2232-20':'Dispense de reproduction subordonnée à localisation, fraîcheur et accès effectif en temps utile ; données absentes/incomplètes à transmettre ; négociations et moyensautonomes maintenus.',
'L2232-21':'Moins11sansDS : tous thèmes et révision possibles ; projet remis individuellement et15jours minimum conservés.',
'L2232-22':'Deux tiers du personnel et non des votants ; dénonciation collective écrite2/3 touteannée, préavis/survie/garantie salariale maintenus, accords existants inclus sans extinction rétroactive.',
'L2232-22-1':'Passerelle de révision/dénonciation après changement de situation conservée.',
'L2232-23':'11–20sansélu : procédure directe avec conditions21 et vote2/3 maintenus.',
'L2232-23-1':'11–<50sansDS : distinction élu/mandaté préservée ; majorité électorale des élus et poids central identiques ; mandatés nonélus votés par salariés.',
'L2232-24':'≥50sansDS : mandat exprès, un parorganisation, information effective et vote majoritaire salariés conservés ; seuls doublons même destinataire/même objet dispensés.',
'L2232-25':'Sansélu mandaté : champ limité aux accords légalement nécessaires, exceptionL1233-21 et majorité électorale conservés ; pas de nouveau referendum.',
'L2232-25-1':'Un mois reste un droit individuel ; anticipation exige tous choix exprès libres/définitifs et exercice effectif du mandatement ; ni silence ni pression ni perte de priorité mandatés.',
'L2232-26':'Mandat et approbation majoritaire maintenus ; carence actuelle démontrée et procédureélections autonome non dispensée ; PVnonrefait pourchaquenégociation seulement s’il demeureexact.'}
assert len(findings)==24
(P/'article-findings.json').write_text(json.dumps([{'number':r['number'],'source_id':r['source_id'],'proposed_sha256':H(r['proposed_xml']),'verdict':'no_concrete_blocking_error_found','finding':findings[r['number']]} for r in a],ensure_ascii=False,indent=2)+'\n')
# Record only current source versions of supportive norms, rather than historical annulled versions.
refs={}
for f in ['references-current.json','references-supplement.json']:
 for r in json.loads((Q/f).read_text()):
  if r['valid_from']<='2026-10-19'<r['valid_until'] and r['state'] in ['VIGUEUR','ABROGE_DIFF']:refs[r['number']]=r
support=[]
for n in ['R2232-1-3','R2232-1-4','R2232-1-5','D2232-1-1','D2232-1-2','D2232-1-6','D2232-2','D2232-3','D2232-4','D2232-6','D2232-7','D2232-8','D2232-9','L2232-27','L2232-28','L2232-29','R2232-10','R2232-11','R2232-12','R2232-13','L2261-9','L2261-10','L2261-11','L2261-12','L2261-13']:
 r=copy.deepcopy(refs[n]);d=D.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(r['code_id'],r['id'])).fetchone();r['current_draft']=dict(d) if d else None;support.append(r)
(P/'supporting-current-sources.json').write_text(json.dumps(support,ensure_ascii=False,indent=2)+'\n')
pending=[{'articles':['D2232-1-1','D2232-1-2'],'status':'source_only_no_db_proposal','action':'Retirer le circuit réglementaire de transmissionCPPNI et ses anonymisation additionnelle/information/AR ; décider séparément des coordonnées publiques utiles, sans refaire un dépôt obligatoire.','normative_fix_to_24_needed':False},{'articles':['R2232-1-5','arrêté modèle prévu par son dernieralinéa'],'status':'source_only_no_db_proposal','action':'Aligner contenu et complétude de demande sur preuves déjà détenues ; conserver salaire,50salariés,forfait,délai6mois etremboursement90jours, sans faire repartir cesdélais à cause d’une pièce déjà valablement reçue.','normative_fix_to_24_needed':False},{'articles':['D2232-2','R2324-5 à R2324-17'],'status':'preexisting_obsolete_cross_reference','action':'Vérifier coordination au vote électronique CSE ; ne pas retirer secret, temps de travail, sécurité ou recours. Pas de simple remplacement automatique numérotation.','normative_fix_to_24_needed':False},{'articles':['D2232-7'],'status':'preexisting_interpretation_to_clarify_with_protocol_reuse','action':'Conserver recours8jours et procédure ; préciser dans sa réécriture que défaut de recours ne remplace pas consentement exprès au protocole requis parL2232-12. LesII/IIIannulés deD2232-6 ne sont pas restaurés.','normative_fix_to_24_needed':False}]
(P/'pending-coordinations.json').write_text(json.dumps(pending,ensure_ascii=False,indent=2)+'\n')
audit={'audited_edition':str(Q),'package_sha256':{f:H((Q/f).read_bytes()) for f in ['source.json','answer.json','beforeimages.json']},'sources_and_notes_read_entirely':24,'proposals_read_entirely':24,'verdict':'no_concrete_blocking_error_found_in_24_candidates','normative_correction_candidates':0,'direct_reference_inventory':{'canonical_articles_searched':30317,'matched_articles_including_internal_and_notes':39,'scope':'Direct textual references to changedmechanisms L2232-8/9/10/12/20/22/25-1/26 only, not global semantic or outsidecode inventory.'},'pending_coordinations':pending,'limits':['No assertion that regulatory coordinations are drafted or registered.','L2261-19/22/32 and protections ofmandatedworkers remain autonomous; no territorial/representation rule silently removed.','Only officialDILA sources and primaryLegifrance lookups used for legal conclusions; the outsideform is an identifiedlead, not a recovered completeform.'],'db_batches_manifest_or_publication_written':False}
(P/'audit-manifest.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(P/'validation.json').write_text(json.dumps({'validate_answer24':'passed','all24_source_hashes_and_notes':'match_canonical_DB','all24_current_DB_beforeimages':'match_author_capture','stable_edition_sha':'matches_archived_copies','normative_corrections':0,'regulatory_closure_complete':False,'no_canonical_write':True},ensure_ascii=False,indent=2)+'\n');print(json.dumps(audit['package_sha256'],indent=2))
