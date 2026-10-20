from pathlib import Path
import json,sys,sqlite3,hashlib,re,datetime
O=Path(__file__).resolve().parent;B=next(p for p in O.parents if p.name=='legal-rewrite');sys.path.insert(0,str(B));import reference_coherence as rc
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
L=lambda n:json.loads((O/n).read_text())
S=lambda n,x:(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ss=L('source.json');aa=L('answer.json');refs=L('references.json');allrows=ss+refs;by={s['number']:s for s in allrows};key=lambda x:x['code_id']+'|'+x['source_id']
M={
'L634-1':['L634-3','L634-4','L635-1','L635-3','L511-1','L511-2','L353-1','L821-2','L831-1','L831-2'],
'L634-2':['L634-1','L634-3'],
'L634-3':['L634-1','L634-4','L635-3','L635-4','L511-1','L511-2','L521-1','L521-2','L831-1'],
'L634-4':['L634-1','R634-4','R634-5'],
'L634-5':['L634-4'],
'R634-1':[f'L634-{i}'for i in range(1,6)]+['R635-1'],
'R634-2':['L634-3'],
'R634-3':['L634-3','R634-2'],
'R634-4':['L634-4'],
'R634-5':['L634-4','R634-4'],
'L635-1':[f'L635-{i}'for i in range(3,11)]+['L353-1','L821-2','L831-1','L831-2','R635-5'],
'L635-3':['L635-1','L635-4','L711-2'],
'L635-4':['L635-1','L635-3','L635-8','L635-9','R635-3','L511-11','L511-19','L521-1','L521-2','L521-3-1','L521-3-2'],
'L635-5':['L635-4','R635-3'],
'L635-6':['L635-3'],
'L635-7':['L635-1','L635-3','L635-4','R635-3','R635-4'],
'L635-8':['L635-4'],
'L635-9':['L635-3','L635-4','L511-1','L511-2','L511-11','L511-19','L521-1','L521-2','L521-3-1','L521-3-2'],
'L635-10':['L635-3'],
'R635-1':[f'L635-{i}'for i in range(1,12)],
'R635-2':['L635-3','L635-4','R635-3'],
'R635-3':['L635-1','L635-4','L635-8','L635-9'],
'R635-4':['L635-7','L635-4','R635-3'],
'R635-5':['R635-4','L635-7','L635-1'],
}
why={
'L634-1':'Le régime déclaratif/zones/délégation cesse ; sa suppression ne ferme pas le permis indépendant.',
'L634-2':'Seule transmission du zonage déclaratif, pas signalement de non-décence autonome.',
'L634-3':'Dépôt15jours/diagnostics/récépissé et condition tierspayant supprimés ; droits des locataires et aides demeurent.',
'L634-4':'Fin des sanctions non définitives et maintien borné des seules amendes anciennes définitives légalement dues.',
'L634-5':'L’habilitation ne doit pas reconstituer le dispositif aboli.',
'R634-2':'Champs exclusivement destinés à la déclaration supprimée ; aucun nouveau relevé exigé.',
'R634-4':'Régularisation sanction déclarative supprimée ; pas de nouveau délai pour bénéficier de la loi plusdouce.',
'R634-5':'Recouvrement ancien définitif seulement ; rapport annuel supprimé, pas de nouveau titre indu.',
'L635-1':'Permis ciblé habitat dégradé, sixmois avant dispositif, dérogationssocial/conventionné et délégation maintenus ; seul rapport annuel retiré.',
'L635-2':'InformationCAF/MSA surzonage permis conservée ; ne dépend pas du récépissé déclaratif supprimé.',
'L635-3':'Premier permis et refus motivé/sécurité/salubrité, visites6h–21h etJLD ; une autorisation déjà valable satisfait la délivrance requise.',
'L635-4':'Dossier/diagnostics/récépissé/accordtacite1mois maintenus ; autorisation durable et noncaducité2ans dèsloi sans attente du décret.',
'L635-5':'Copie au locataire du permis existant, distincte du renouvellement administratif supprimé.',
'L635-6':'Décisions de refus transmises pourcontrôles autonomes ; pas second dossier du propriétaire.',
'L635-7':'Sanctions restent bornées à une demande encore nécessaire ou à un refus opposable ; proportionnalité/observations1an/5000–15000€ inchangés.',
'L635-8':'Bail préservé même irrégularité administrative ; accordtacite necertifie pas décence.',
'L635-9':'Police et droits occupants nonopposables au permis ; arrêté interdit délivrance etoccupationcontraires.',
'L635-10':'Décisions refus/réserves ciblées àl’observatoire ne sont pas la déclaration générale dechaque bail supprimée.',
'L635-11':'Habilitation d’application du permis maintenu ; aucun nouveau régime législatif créé par voie réglementaire.',
'R635-1':'Champ titresI/Ibis et dispenses reconduction/renouvellement/avenant conservés ; aucun terme d’emploi en cause.',
'R635-2':'Première demande identifie propriétaire/mandataire/logement ; pas nouveau dossier au seulchangement de propriétaire.',
'R635-3':'Accuséréception équivaut déjàrécépissé ; contenu décision conservé ; caducitécoordonnée dèsloi/transfertplein droit dèsdécret distincts.',
'R635-4':'Mois contradictoire/régularisation première demande conservé ; pas sanction d’un renouvellement désormais dispensé.',
'R635-5':'Bénéficiaires de créance etrecours inchangés ; rapport supprimé etrenvoi mortCGCT remplacé par droit commun.',
'L353-1':'Les conventionsbailleurs/occupants restent les conventions deL831-1, sans perdreleur avantage locatif.',
'L821-2':'Aides à la résidence principale ; la suppression du récépissé ne dispense pas des conditions autonomes.',
'L831-1':'Catégoriesconventionnées/APL entières gardées, notamment6branches et deuxcircuits du2° ; pas conversion de tous allocataires enlogements conventionnés.',
'L831-2':'Prêts/locationsaccession post2017 exclus, exceptionancien/communes/dates2020 maintenue : aucun droit àaide rouvert artificiellement.',
'L511-1':'Police autonome sécurité/salubrité demeure etsa note2021 garde sonchamp temporel.',
'L511-2':'Quatrecas réelsrisques/équipements/explosifs/insalubrité distincts duformulaire aboli.',
'L511-3':'Champfunéraire autonome horslot, aucune extension ni retrait par la déclaration de location.',
'L511-11':'Mesures de police et travaux avantoccupation demeurent ; le projetactuel permet de différer certains travaux de locaux vacants sûrs sansautorisation, avantage nonrestreint ici.',
'L511-19':'Mesures urgentes de dangerimminent etautorisationjudiciaire demolition restent ; ni permis durable ni déclaration supprimée ne les neutralisent.',
'L521-1':'Qualitéoccupants et obligationhébergement/relogement/recours restent.',
'L521-2':'Suspensionloyers/restitution/prolongationbaux/bonnefoi restent dansleurs champs propres, sans expulsionprivée.',
'L521-3-1':'Hébergement, relogement adapté et3mois indemnité occupant restent ; aucune condition récépissé ajoutée.',
'L521-3-2':'Substitutionpublique/relogement, fraisplafonnés à1an dansprojet, noncumul etrecours maintenus ; pas financement fictif de déclaration.',
'L711-2':'Seul vrai renvoi inverse CCH détecté vise refusL635-3 inchangé ; registrecopro ne rétablit ni déclaration634 ni demande répétée635.',
}
D=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);D.row_factory=sqlite3.Row;D.execute('BEGIN');catalog={key(s):s for s in allrows};snap=rc.capture(D,ss,aa);S('reference-targets.json',snap)
fulltargets={key(s):rc.view(D,key(s))for s in allrows}
external=[{'target_id':x['code_id']+'|'+x['source_id'],'number':x['number'],'file':'external-baseline-references.json','document_sha256':x['sha256'],'source_type':'DILA_baseline_2025_07_13_read_whole_current_status_crosschecked_primary_search_2026'}for x in L('external-baseline-references.json')]
external+= [{'target_id':'LEGITEXT000006069108|'+x['source_id'],'number':'loi1989 '+x['number'],'file':'external-primary-references.json','document_sha256':x['document_sha256'],'source_type':'DILA_local_466updates_to_2026_10_18_and_primary_index_crosscheck'}for x in L('external-primary-references.json')]
EXT={
'L634-3':['loi1989 3-3','loi1989 6'],
'L635-3':['loi1989 6'],
'L635-4':['loi1989 3-3','loi1989 6'],
'R634-5':['L1617-5','R2342-4'],
'R635-3':['L112-3','R112-5','L112-6'],
'R635-5':['L1617-5','R2342-4'],
}
source_by_id={key(s):s for s in ss};answers={key(s):s for s in aa};future=[];maps=[]
for s in ss:
 k=key(s);n=s['number'];deps=[]
 for tn in M[n]:
  t=by[tn];tk=key(t);before=fulltargets[tk];af=answers.get(tk)
  snippets=[]
  for label,text in [('source',s['source_xml']),('notes',s['source_notes_xml']),('proposed',answers[k]['proposed_xml']or'')]:
   pat=re.compile(re.escape(tn).replace(r'\-',r'\s*-\s*').replace(tn[0],tn[0]+r'\s*\.?\s*',1),re.I)
   for m in pat.finditer(text):snippets.append({'field':label,'quote':text[max(0,m.start()-70):m.end()+90]})
  deps.append({'target_key':tk,'number':tn,'basis':'explicit_source_note_or_proposed_reference'if snippets else'non_cited_necessary_scope_exemption_or_transition_context','why_used':why[tn],'cited_evidence':snippets,'actual_guard':rc.guard(before),'future_intrapack_body_sha256':H(af['proposed_xml'])if af and af['proposed_xml']is not None else None,'future_intrapack_is_not_actual_DB':bool(af and af['proposed_xml']is not None)})
 ext=[x for x in external if x['number']in EXT.get(n,[])]
 # Law1990 precise definitions read in official search; article3 observatory not modified and wholelawnotclaimed.
 if n in ['L635-8','L635-10']:ext.append({'target_id':'LEGITEXT000006075926|article1-1'if n=='L635-8'else'LEGITEXT000006075926|article3','file':'primary-web-contexts.json'if n=='L635-8'else'primary-web-contexts-extra.json','primary_read':'article1-1wholeindexed'if n=='L635-8'else'observatory context only; article3whole not claimed; no normative change or new dependencybody invented','unchanged_external_regime':True})
 proto=[]
 for tk in snap['requirements'].get(k,[]):
  t=snap['targets'][tk];proto.append({'target_key':tk,'number':t['number'],'reason':'Technical falsepositive: external CRPA L112-3 unqualified token collides with CCH L112-3, triggering CT base guards. Whole views read; no employment relation or construction-rule delegation is altered by this rentalreceipt text.','guard':rc.guard(t),'legal_dependency':False})
 maps.append({'referrer_key':k,'number':n,'source_body_sha256':H(s['source_xml']),'notes_sha256':H(s['source_notes_xml']),'proposed_body_sha256':H(answers[k]['proposed_xml']),'legal_dependencies':deps,'external_dependencies':ext,'protocol_only_false_positives':proto,'no_all_to_all_pinning':True})
for s,a in zip(ss,aa):
 if a['proposed_xml']is None:continue
 old=rc.guard(fulltargets[key(s)]);new={**old,'view_kind':'proposal','view_sha256':H(a['proposed_xml'])}
 referrers=[{'key':m['referrer_key'],'number':m['number']}for m in maps if any(d['target_key']==key(s)for d in m['legal_dependencies'])]
 future.append({'target_key':key(s),'number':s['number'],'actual_before_guard':old,'hypothetical_after_guard':new,'actual_post_registration_guard_not_yet_captured':True,'referrers_in_this_pack':referrers})
S('article-dependency-map.json',{'method':'Explicit per-referrer legal, exemption, transition and scope map after whole-text reads; snapshot targets are actual canonical views, future sibling bodies are separately labelled hypothetical. No default all-to-all pinning. Native contract checker falsepositives separately labelled. External proof freshness limitations remain explicit.','articles':maps})
S('legal-dependency-targets-full.json',fulltargets);S('intrapack-future-guards.json',future)
ledger_path=B/'runtime/substantive-audits.json';raw=ledger_path.read_bytes();ledger=json.loads(raw);changed={x['target_key']for x in future};impacted=[]
for row in ledger['audits']:
 hits=[g for g in row.get('dependency_guards',[])if g['code_id']+'|'+g['source_id']in changed]
 if hits:impacted.append({'referrer_key':row['code_id']+'|'+row['source_id'],'evidence_file':row.get('evidence_file'),'changed_dependency_guards':hits,'actual_semantic_read_not_claimed':True})
S('existing-audit-dependency-impact.json',{'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ledger_sha256':H(raw),'ledger_audits_scanned':len(ledger['audits']),'method':'Mechanical exact-ID intersection with14futurechangedbodies; no semanticreread ofwholeledger. This includesC/D andotheradoptedaudits. No automaticrebind.','impacted_audits':impacted,'C_D_referrers_if_any':[x for x in impacted if'poursuite-20261020-c'in(x.get('evidence_file')or'')or'poursuite-20261020-d'in(x.get('evidence_file')or'')],'canonical_mutation':False})
# Guard map stays compact: only explicit real edges, all full bodies kept once.
S('legal-dependency-guards.json',{'version':1,'policy_sha256':snap['policy_sha256'],'targets':{tk:rc.guard(v)for tk,v in fulltargets.items()if any(any(d['target_key']==tk for d in m['legal_dependencies'])for m in maps)},'requirements':{m['referrer_key']:[d['target_key']for d in m['legal_dependencies']]for m in maps},'external_files_sha256':{n:H((O/n).read_bytes())for n in ['external-baseline-references.json','external-primary-references.json','primary-web-contexts.json','primary-web-contexts-extra.json','primary-reference-check.json','recovery-primary-contexts.json']},'post_registration_recertification_required_for_changed_sibling_targets':True})
D.rollback();D.close();print('MAP',len(maps),'LEGAL_EDGES',sum(len(m['legal_dependencies'])for m in maps),'PROTOCOL_FALSE_POSITIVES',sum(len(m['protocol_only_false_positives'])for m in maps),'EXISTING_AUDIT_HITS',len(impacted))
