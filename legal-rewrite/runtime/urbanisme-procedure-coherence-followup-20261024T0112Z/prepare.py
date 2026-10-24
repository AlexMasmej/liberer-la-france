"""Fresh whole-text guards and ordinary candidate checks; no registration."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, re, sqlite3, sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime'
sys.path.insert(0,str(ROOT))
import ingest,run_exhaustive as runner,reference_coherence as refs,review_prior
from source_assets import load_companions
def sha(b):return hashlib.sha256(b).hexdigest()
def put(n,o):
    with (OUT/n).open('x') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')
stable={}
def read(p):
    b=p.read_bytes();stable[p]=b;return json.loads(b)
pins=read(R/'coherence-rollout-20261023T2042Z/resumption-observation-pins-v4.json')
pins['run_exhaustive.py']='d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
packets=read(OUT/'whole-article-packet.json')+read(OUT/'additional-whole-counterparts.json')
assert len(packets)==19
key=('LEGITEXT000006074075','LEGIARTI000031720973')
owners=[]
paths=sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
for p in paths:
    for index,row in enumerate(read(p)):
        if (row['code_id'],row['source_id'])==key:owners.append((p,index,row))
assert len(owners)==1
p,index,owner=owners[0]
registry=read(ROOT/'registered-batches.json');entry=registry['|'.join(key)]
assert entry['source_sha256']==owner['source_sha256']
assert entry['proposed_sha256']==runner.digest(owner['proposed_xml'])
db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=15)
db.row_factory=sqlite3.Row;db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
guards=[]
try:
    for item in packets:
        a=item['article'];k=a['code_id'],a['id']
        live=db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone()
        assert dict(live)==a,k
        assert ingest.source_notes(db,*k)==item['source_NOTA'],k
        d=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
        assert (dict(d) if d else None)==item['draft'],k
        guards.append(dict(code_id=k[0],source_id=k[1],number=a['number'],state=a['state'],
            valid_from=a['valid_from'],valid_until=a['valid_until'],
            source_sha256=a['source_sha256'],source_NOTA_sha256=sha(item['source_NOTA'].encode()),
            whole_article_row_sha256=sha(json.dumps(a,ensure_ascii=False,sort_keys=True).encode()),
            whole_draft_row=item['draft']))
    item=next(x for x in packets if (x['article']['code_id'],x['article']['id'])==key)
    a=item['article'];d=item['draft']
    assert tuple(d[n] for n in ['source_sha256','status','proposed_xml','reason','review_notes'])==review_prior.draft_values(owner)
    before='le délai supplémentaire de quinze jours'
    after="le délai d'observations d'au moins quinze jours prévu à l'article R. 121-22, avec les règles transitoires fixées par cet article"
    assert owner['proposed_xml'].count(before)==1
    answer=copy.deepcopy(owner);answer['proposed_xml']=owner['proposed_xml'].replace(before,after)
    answer.pop('reference_coherence',None);answer.pop('substantive_impact_certificate',None)
    answer['reason'] += " Coordination du renvoi protecteur de R121-22 : désigner son délai minimal d'observations et ses règles transitoires, sans imposer de nouveau une prolongation systématique aux rectifications nouvelles. Cette correction n'est pas une réduction autonome supplémentaire."
    answer['review_notes'] = "Relecture parentale entière du 24 octobre 2026 : dix-neuf textes de source et propositions, motifs, notes, NOTA et bornes, dont trois versions historiques sans draft. Contradiction entre propositions : R121-22 permet pour les rectifications nouvelles le chevauchement des quinze jours avec l'enquête ; R121-23 qualifiait encore ces quinze jours de systématiquement supplémentaires. L'insertion renvoie à la durée minimale et à la transition propres à R121-22 : les rectifications déjà portées à la connaissance des intéressés gardent leur délai additionnel, sans réouverture de délai expiré. Les deux modalités d'information, la prolongation nécessaire pour assurer quinze jours pleins et la transmission après la clôture effective restent régies par R121-22. Les propositions L121-32/L121-34 et R121-23 convergent dans le retrait du circuit communal distinct et de son délai de deux mois ; aucune délibération séparée n'est rétablie. Les numéros 1° et 2°, l'arrêté préfectoral même en cas d'opposition, la motivation, les observations recueillies, les actes antérieurs et les recours demeurent. R121-24 conserve les publicités officielles, le dépôt et l'affichage, et les anciens décrets régulièrement pris, sans nouvelle annonce de presse. R121-17 protège le dossier foncier particulier ; L121-33 les terrains et distances historiques, L121-35/36 l'indemnisation, L121-37 l'exclusion de responsabilité et L121-51 son régime ultramarin distinct. Le chapitre CRPA, le décret de publicité foncière et les renvois domaniaux extérieurs ne sont pas intégralement vérifiés ici ; aucune concordance externe exhaustive ni validation par juriste n'est revendiquée. Ce délai d'enquête n'est aucun préavis de contrat de travail."
    answer['benefit_review'] += " La référence explicite aux règles transitoires de R121-22 conserve le délai additionnel déjà ouvert aux anciennes rectifications, ainsi que quinze jours au moins après les deux informations pour les rectifications nouvelles. La prolongation nécessaire demeure obligatoire ; aucune anticipation de clôture n'est permise. Les garanties foncières, indemnités, exonération de responsabilité, exceptions littorales et recours restent dans leur champ."
    answer['substantive_impact']['assessment'] += " La seule insertion nouvelle coordonne le délai d'observations déjà réformé dans R121-22 et n'ajoute aucun effet ni mesure à compter."
    answer['substantive_impact']['scope_limitations'] += " Les détails externes du CRPA et de la publicité foncière restent hors certification intégrale."
    previous=dict(source_sha256=d['source_sha256'],status=d['status'],proposed_xml=d['proposed_xml'],reason=d['reason'],review_notes=d['review_notes'],proposed_sha256=runner.digest(d['proposed_xml']),batch_row_sha256=review_prior.batch_row_sha256(owner))
    source=dict(code_id=key[0],source_id=key[1],number=a['number'],source_sha256=a['source_sha256'],source_xml=a['content_xml'],source_notes_xml=item['source_NOTA'],valid_from=a['valid_from'],valid_until=a['valid_until'],previous_draft=previous,impact_check_required=True,benefit_check_required=runner.mentions_possible_relief(a['content_xml']))
    companions=load_companions()
    if key in companions:source['source_companions']=companions[key]
    snapshot=refs.capture(db,[source],[answer])
    try:
        runner.validate_answer([answer],[source]);refs.accept_checks([answer],[source],snapshot)
        validation=dict(passed=True,ordinary_answer_benefit_impact_reference_checks=True)
    except Exception as e:validation=dict(passed=False,error=str(e),no_guard_removed=True)
    refs.check_guards(db,snapshot)
finally:db.close()
for p,b in stable.items():assert p.read_bytes()==b,str(p)
assert paths==sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
put('source.json',[source]);put('candidate-answer.json',[answer]);put('reference-targets.json',snapshot)
put('ordinary-validation.json',validation);put('current-pins.json',pins)
put('whole-owner-beforeimage.json',dict(owner_path=str(owners[0][0]),owner_index=index,owner_file_sha256=sha(stable[owners[0][0]]),whole_owner_row=owner,whole_owner_row_sha256=review_prior.batch_row_sha256(owner),whole_registry_entry=entry,registry_file_sha256=sha(stable[ROOT/'registered-batches.json']),exact_XML_change=dict(before=before,after=after)))
put('full-read-coverage-and-live-guards.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),full_texts_read=19,historical_versions_without_draft=3,article_guards=guards,second_readonly_transaction_matches_all=True,all77_pins_match=True,four_formal_policies_current=True))
put('CONTROL.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),state='PREPARED_NOT_REGISTERED',full_texts_read=19,new_bounded_textual_nonconvergence_requiring_coordination=1,enforceable_legal_conflict_not_established=True,candidate_count=1,ordinary_preflight=validation,XML_only_one_exact_substitution=True,reason_notes_benefit_and_existing_impact_metadata_freshly_qualified=True,no_additional_measure_or_savings_counted=True,first_eight_other_candidates_still_required=True,shared_reservations_not_acquired=True,full_global_registration_not_executed=True,canonical_mutations=0,models_launched=0,no_completed_changed=True,no_source_NOTA_changed=True,no_active_interruption_or_policy_change=True,external_CRPA_publicity_and_domanial_details_not_exhaustively_verified=True,admin_global_flags_resolved=0,jurist_approval=False,convergence_after_future_commit_still_required=True))
print(json.dumps(dict(folder=str(OUT),validation=validation,configured_targets=len(snapshot['targets']),canonical_mutations=0),ensure_ascii=False))
