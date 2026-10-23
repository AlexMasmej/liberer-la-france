import json, pathlib, hashlib, datetime, sqlite3, xml.etree.ElementTree as E, difflib
O=pathlib.Path(__file__).resolve().parent; P=O.parent/'global-reference-audit-20261022T182623Z'; OLD=O.parent/'global-reference-audit-20261022'
def read(p): return json.loads(p.read_text())
def sha(x):return hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
def put(n,d): (O/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();cap=read(P/'capture.json'); inh=next(r for r in read(P/'semantic-review-inheritance.json')['reviews'] if r['label']=='L1242-2'); summary=read(P/'summary.json'); aid=summary['audit_id']; rid=sha(O.name+'|'+aid)
FIELDS=['source_sha256','source_body_sha256','source_notes_sha256','article_document_sha256','article_document_stored_sha256','proposal_sha256','draft_source_sha256','draft_status']
keys={read(f)['key'] for f in O.glob('*-full.txt')}; guards={}
for line in (P/'article-manifest.jsonl').open():
 r=json.loads(line)
 if r['key'] in keys:guards[r['key']]={k:r[k] for k in FIELDS}
db=sqlite3.connect('file:'+str(P/'corpus.snapshot.sqlite')+'?mode=ro&immutable=1',uri=True);db.row_factory=sqlite3.Row;db.execute('pragma query_only=on')
checks={};coverage=[];by_num={};all_rows=[];changes=[]
oldrows={a['key']:a for fn in ['L1242-2-review-packet.json','L1242-2-review-dependencies.json'] for a in read(OLD/fn)['articles']}
for fn in ['L1242-2-review-packet.json','L1242-2-review-dependencies.json']:
 packet=read(O/fn)
 for a in packet['articles']:
  d=a['draft'];raw=a['document']['xml'];root=E.fromstring(raw);node=root.find('NOTA/CONTENU');notes=((node.text or '')+''.join(E.tostring(ch,encoding='unicode') for ch in node)).strip() if node is not None else ''
  body=root.find('BLOC_TEXTUEL/CONTENU');mirror=(body.text or '')+''.join(E.tostring(ch,encoding='unicode') for ch in body)
  g={'source_sha256':a['source_sha256'],'source_body_sha256':sha(a['content_xml']),'source_notes_sha256':sha(notes),'article_document_sha256':sha(raw),'article_document_stored_sha256':a['document']['sha256'],'proposal_sha256':sha(d['proposed_xml']),'draft_source_sha256':d['source_sha256'],'draft_status':d['status']}
  assert g==guards[a['key']] and mirror==a['content_xml'] and sha(raw)==a['document']['sha256']
  current=dict(db.execute('select * from drafts where code_id=? and source_id=?',(a['code_id'],a['id'])).fetchone());assert current==d
  a.update({k:d[k] for k in ['status','proposed_xml','reason','review_notes']});a.update(draft_source_sha256=d['source_sha256'],source_notes_xml=notes,article_document_xml=raw,snapshot_guard=g)
  checks[a['key']]={'number':a['number'],'current_guard':g,'matches_snapshot':True,'source_document_body_matches':True,'draft_metadata_rechecked':True}
  coverage.append({'key':a['key'],'number':a['number'],'read_in_full':['source body','NOTA','canonical ARTICLE document including metadata links lineage','proposal','reason','review_notes'],'full_article_metadata_retained':True,'hashes':{k:sha(v) for k,v in {'content_xml':a['content_xml'],'source_notes_xml':notes,'article_document_xml':raw,'proposed_xml':d['proposed_xml'],'reason':d['reason'],'review_notes':d['review_notes']}.items()},'snapshot_guard':g})
  prior=oldrows[a['key']];diff={k:{'prior':prior[k],'new':d[k],'prior_sha256':sha(prior[k]),'new_sha256':sha(d[k])} for k in ['proposed_xml','reason','review_notes'] if prior[k]!=d[k]}
  if diff:changes.append({'key':a['key'],'number':a['number'],'changed_fields':diff,'source_body_unchanged':prior['content_xml']==a['content_xml']})
  by_num[a['number']]=a;all_rows.append(a)
 packet.update(snapshot_path=str(P/'corpus.snapshot.sqlite'),snapshot_sha256=cap['snapshot_sha256'],global_audit_id=aid,review_id=rid)
 put(fn,packet)
db.close()
policyguards={n:{'current_sha256':sha((P/n).read_bytes()),'snapshot_sha256':info['sha256'],'matches_snapshot':sha((P/n).read_bytes())==info['sha256']} for n,info in cap['policies'].items()};assert all(r['matches_snapshot'] for r in policyguards.values())
policy=read(P/'policy-coordinations.json');corpus=read(P/'corpus.json')
put('policy-evidence.json',{'guards':policyguards,'scope':policy['scope'],'travail':policy['travail'],'editorial_direction':policy['editorial_direction_2026_10_19'],'preserved_benefits':policy['preserved_benefits_2026_10_19'],'site_embauche':read(P/'site-summaries.json')[0],'corpus_coverage_rules':corpus['coverage_rules'],'official_source':corpus['official_source'],'reference_focus_extra_entries_for_15_articles':[]})
target=by_num['L1242-2']['key'];cluster=next(r for r in read(P/'coordination-clusters.json')['targets'] if r['target_key']==target);selected=set(cluster['finding_ids']);newfind=[]
for line in (P/'findings.jsonl').open():
 f=json.loads(line)
 if f['finding_id'] in selected:newfind.append(f)
assert len(newfind)==8
put('new-target-findings.json',newfind)
packet=read(O/'L1242-2-review-packet.json');packet.update(target=cluster,findings=newfind);put('L1242-2-review-packet.json',packet)
put('old-new-comparison.json',{'changed_articles':changes,'changed_guard_articles':[r for r in inh['article_guards'] if not r['matches_prior_guard']],'unchanged_article_count':14,'all_15_freshly_read':True,'interpretation':'L1221-2 précise droit privé, saison, aide/accompagnement, transition directement opératoire, maintien ancienneté/créances, avantages futurs à mêmes conditions et réserves agents publics/protections spéciales. Aucun effet de suppression des prolongations L2412 ni importation du préavis individuel dans leurs délais.'})
put('full-read-coverage.json',coverage)
put('L1242-2-final-state-check.json',{'checked_at_utc':now,'scope':'frozen new snapshot only; not active database','source_connection':'mode=ro&immutable=1; PRAGMA query_only=ON','snapshot_path':str(P/'corpus.snapshot.sqlite'),'all_match':True,'all_article_guards_match_snapshot':True,'all_policy_guards_match_snapshot':True,'articles':checks,'policies':policyguards})
impacts={
'L1221-2':'Nouvelle interdiction du terme en droit privé; transition et avantages futurs renforcés. Les autorisations et protections spéciales sont réservées expressément; les agents publics restent distincts.',
'L1241-1':'Interdiction des nouveaux CDD/renouvellements; anciens termes/primes/recours et reports légaux conservés, conversion sans remise à zéro; aides et protections autonomes maintenues.',
'L1242-2':'Suppression prospective des six motifs; qualifications et effets antérieurs sauvegardés, pas de fin automatique de saison/projet.',
'L1244-2-2':'Abrogation prospective du mécanisme supplétif CDD, maintien du réemploi acquis et de l’information, qualification et motif dûment fondé; exécution future en emploi sans terme.',
'L1251-6':'Conditions de mission distinctes de la durée de l’emploi; définition saisonnière rendue autonome, anciens contrats préservés. Pas de validation exhaustive des secteurs ou décrets.',
'L1251-37':'Compétence de la branche étendue et réserve L1251-5 conservées. Note 2017 reste bornée aux contrats concernés; coordination globale de la carence au-delà des huit renvois hors revue.',
'L1251-37-1':'Dispense de carence pour futures lettres de mission, sécurité/égalité/licéité maintenues; six exceptions anciennes et champ de la note 2017 conservés.',
'L2411-1':'Liste intégrale des catégories, extension explicite du 7° ter aux opérations transfrontalières et autorisation patronale corrélative; n’efface aucune des sept catégories examinées. Coordinations L2411-12/L2413-1 et durées précises hors revue.'}
for n in ['L2412-2','L2412-3','L2412-4','L2412-5','L2412-8','L2412-9','L2412-13']:impacts[n]='Corps source conservé pour anciens CDD; autorisation et catégories/durées sources préservées; réemploi en contrat sans terme. Dernier alinéa étend explicitement la prolongation saisonnière ou d’usage aux futurs salariés protégés dans le même champ matériel. Cette prolongation autonome ne vaut ni terme ni dispense d’autorisation.'
put('article-impact-review.json',{'scope':'Impacts qualitatifs explicités à partir des propositions, reasons et review_notes du snapshot; aucune table d’impacts distincte dans ce snapshot SQLite. Aucun chiffrage financier inventé.','articles':[{'key':a['key'],'number':a['number'],'analysis':impacts[a['number']]} for a in all_rows]})
limits=['Revue de huit signalements vers L1242-2 et quinze articles seulement; pas de validation globale des renvois du code.','Corpus DILA disponible jusqu’au 18 octobre 2026; aucune mise à jour officielle postérieure vérifiée.','Aucune validation juridique humaine, aucune résolution d’alerte ni modification de texte, politique, certificat, base active ou pointeur.','Durées détaillées du chapitre L2411, procédures et cibles extérieures (environnement/minier, accords et décrets sectoriels) non vérifiées intégralement au-delà des quinze articles.','La phrase « exclusivement » des L2412 est comprise avec le dernier alinéa exprès pour les futurs bénéficiaires; une clarification de portée/version statique reste possible, sans suppression de garantie.','La NOTA 2017 des L1251-37/37-1 ne date pas la future réforme et ne doit pas être appliquée à tous les contrats anciens indistinctement.','Gardes portent sur ce snapshot figé uniquement; tout nouveau snapshot exige contrôle des quinze gardes et quatre politiques.']
findings=[]
for f in newfind:
 a=next(a for a in all_rows if a['key']==f['source_key']);special=a['number'].startswith('L2412');classification='protection_speciale_independante_avec_composante_transitoire' if special else 'renvoi_historique_transitoire'
 paragraphs=E.fromstring('<root>'+a['proposed_xml']+'</root>');ev=[{'paragraph_index_zero_based':i,'exact_paragraph_xml':E.tostring(p,encoding='unicode'),'paragraph_xml_sha256':sha(E.tostring(p,encoding='unicode'))} for i,p in enumerate(paragraphs)]
 findings.append({'review_id':rid,'original_finding_id':f['finding_id'],'global_audit_id':aid,'source_key':a['key'],'number':a['number'],'classification':classification,'effective_inconsistency_established':False,'review_status':'fresh_full_context_review_not_marked_resolved','resolved':False,'automatic_change':False,'semantic_review_by_jurist':False,'source_guard':guards[a['key']],'target_key':target,'target_guard':guards[target],'analysis':impacts[a['number']],'reference_components':{'legacy_contract_reference':'Définition historique du 3° appliquée aux anciens contrats sous transition L1241-1/L1242-2.','future_reference':'Champ matériel de la prolongation autonome explicite du dernier alinéa, sans nouveau CDD.' if special else None},'evidence':ev,'new_L1221_2_effect':'Réserve explicite des protections spéciales; conservation des avantages futurs et des droits acquis. Ne contredit pas ce renvoi.','queue_overlay_recommendation':'Conserver signal original avec cette revue limitée; aucune résolution automatique.'})
put('findings-reviewed.json',{'review_id':rid,'global_audit_id':aid,'reviewed_at_utc':now,'scope':'Fresh semantic review of 8 L1242-2 references / 15 articles on frozen snapshot','target_key':target,'findings_reviewed':8,'classification_counts':{'renvoi_historique_transitoire':1,'protection_speciale_independante_avec_composante_transitoire':7},'all_article_guards_match_current_state':True,'all_policy_guards_match_current_state':True,'current_state_means':'named frozen snapshot only','full_articles_read':15,'findings':findings,'limits_and_unknowns':limits,'still_in_analysis':limits[3:6],'effective_inconsistencies_established':0,'semantic_review_by_jurist':False,'resolved_findings':0,'automatic_change':False})
put('prior-evidence-manifest.json',{'purpose':'Provenance/comparison only; conclusions freshly re-established from all fifteen full texts.','files':{str(OLD/f):{'sha256':sha((OLD/f).read_bytes()),'bytes':(OLD/f).stat().st_size} for f in ['L1242-2-review-packet.json','L1242-2-review-dependencies.json','L1242-2-final-state-check.json','findings-reviewed.json','L1242-2-REVIEW.md','semantic-review-manifest.json']}})
put('provenance.json',{'snapshot_path':str(P/'corpus.snapshot.sqlite'),'snapshot_sha256_from_verified_capture':cap['snapshot_sha256'],'snapshot_byte_hash_not_recomputed_by_this_limited_review':True,'global_validation_checks_passed':read(P/'validation.json')['checks_passed'],'read_only_connection':True,'source_as_of':cap['as_of'],'inputs':{n:sha((P/n).read_bytes()) for n in ['capture.json','validation.json','semantic-review-inheritance.json','coordination-clusters.json','summary.json']},'validator_schema':str(O.parent/'semantic-review-override-support-20261022/validate_refresh.py.template'),'validator_schema_sha256':sha((O.parent/'semantic-review-override-support-20261022/validate_refresh.py.template').read_bytes()),'no_live_database_read':True})
(O/'L1242-2-REVIEW.md').write_text('''# Relecture fraîche limitée — L1242-2

Huit renvois ont été réexaminés sur le snapshot global du 22 octobre 2026 à 18:26:23 UTC après lecture intégrale des quinze articles, documents ARTICLE et NOTA, propositions, raisons et notes de revue. Aucune incohérence effective n’est établie dans ces huit renvois : un renvoi est historique/transitoire et sept maintiennent aussi une protection future autonome. Aucun signalement n’est résolu.

La seule garde changée depuis le paquet antérieur est la proposition L1221-2 (LEGIARTI000019071087), de `0f4a0061aadf2d6fc30386f95fb3d102a6306fc6d536e3c0409e13b7393c405d` à `0a424087fd3feecf301564a0cb84a961f2da0ea518034152c6494836e516842e`. Ses raisons et notes changent également; sources, NOTA et statut sont identiques. Les quatorze autres corps/propositions/raisons/notes et les quatre politiques correspondent au paquet précédent. Les différences exactes, anciens et nouveaux contenus complets figurent dans old-new-comparison.json.

L1221-2 ajoute explicitement le droit privé, la saison parmi les événements sans terme automatique, les conventions d’aide et l’accompagnement parmi les phases limitées, une transition directement opératoire (durée/terme anciens, primes, congés, créances et recours), la conversion avec ancienneté, le maintien futur des aides/exonérations/droits sociaux/logement sous leurs autres conditions, la réserve des agents publics et des procédures collectives/autorisations/protections spéciales. Ces ajouts confortent la lecture du groupe; ils ne suppriment aucune prolongation L2412. Les notes distinguent le barème ordinaire et les protections; elles ne transforment pas les quinze jours en durée des protections.

| Article | Qualification et portée |
|---|---|
| L1251-37-1 | Citation dans le bloc des contrats antérieurs; dispense autonome de carence pour les futures lettres de mission, sans supprimer sécurité, égalité ou licéité. |
| L2412-2 | Délégué syndical : transition ancienne et prolongation future autonome. |
| L2412-3 | Élus/représentants syndicaux CSE, anciens/candidats selon les délais sources : même distinction. |
| L2412-4 | Représentants de proximité, anciens/candidats : même distinction. |
| L2412-5 | CSE interentreprises, anciens/candidats : même distinction. |
| L2412-8 | Représentants d’entreprise extérieure CSSCT dans le champ installations classées/minier : même distinction. |
| L2412-9 | Commission paritaire agricole, anciens/candidats : même distinction. |
| L2412-13 | Conseillers prud’hommes : même distinction. |

Les sept L2412 conservent leur corps source, puis interdisent que le renvoi rétablisse de nouveaux CDD; ils préservent le réemploi en contrat sans terme et ouvrent expressément, au dernier alinéa, la prolongation égale à l’interruption habituelle de l’activité aux futurs salariés protégés du même champ saisonnier/d’usage. Lire seulement le bloc « exclusivement » ferait perdre cette garantie. L1242-2 et L1241-1 maintiennent les qualifications/effets anciens; L1244-2-2 conserve les droits de réemploi acquis; L1251-6 distingue affectation et emploi. L2411-1 conserve les catégories concernées et explicite son extension transfrontalière distincte; cette revue ne certifie pas toutes ses coordinations externes.

Les quinze jours calendaires valent préavis individuel des deux côtés. L’indemnité ordinaire est nulle avant un an, puis 0,20 mois par année totale, fractions en mois complets et plafond six mois, à charge de l’employeur seulement. Aucun de ces paramètres ne remplace une autorisation protectrice, une période de protection ou un préavis autonome. Aucun gain financier chiffré n’est inféré.

La NOTA de 2017 des L1251-37 et L1251-37-1 conserve sa date et son champ propres; les autres NOTA des quinze articles sont sans contenu normatif. Les liens documentaires historiques ne sont pas à eux seuls des erreurs de renvoi. Une clarification facultative de la phrase d’ouverture et de la version historique visée peut améliorer la lecture, sans réduire les protections futures.

Limites : huit renvois seulement; corpus officiel arrêté au 18 octobre 2026; aucune actualisation officielle postérieure ni validation juridique humaine. Les durées détaillées L2411, les accords/décrets sectoriels et procédures externes restent hors cette revue. Les gardes sont celles du snapshot figé, pas de la base active. Aucune proposition, politique, base active, source synchronisée, certificat, processus, slot ou pointeur n’a été modifié.
''')
put('validation.json',{'checks_passed':True,'errors':[],'articles':15,'findings':8,'all_guards_recomputed_against_frozen_manifest':True,'canonical_documents_hash_and_body_verified':True,'draft_metadata_rechecked':True,'policies':4,'compatible_review_override_schema':True,'scope':'small package checks only; not full global validator run','automatic_change':False})
put('semantic-review-manifest.json',{'review_id':rid,'global_audit_id':aid,'snapshot_sha256':cap['snapshot_sha256'],'current_guards_matched':True,'scope':'frozen snapshot only','files':{f.name:{'sha256':sha(f.read_bytes()),'bytes':f.stat().st_size} for f in sorted(O.iterdir()) if f.is_file() and f.name!='semantic-review-manifest.json'}})
print(json.dumps({'folder':str(O),'review_id':rid,'manifest_sha256':sha((O/'semantic-review-manifest.json').read_bytes()),'files':len(list(O.iterdir())),'bytes':sum(f.stat().st_size for f in O.iterdir()),'changed_articles':[x['number'] for x in changes]},ensure_ascii=False))
