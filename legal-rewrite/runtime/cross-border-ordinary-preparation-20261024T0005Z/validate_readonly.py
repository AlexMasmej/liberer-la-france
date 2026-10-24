"""Run ordinary answer/benefit/impact/reference checks on freshly captured inputs."""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,sqlite3,sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sys.path.insert(0,str(ROOT))
import ingest,run_exhaustive as runner,reference_coherence as refs,review_prior
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_bytes())
def put(n,d):
    with (OUT/n).open('x') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
sources=read(OUT/'source.json');answers=copy.deepcopy(read(OUT/'candidate-answer-before-reference-assessments.json'))
snapshot=read(OUT/'reference-targets.json');pins=read(OUT/'current-pins.json')
owners=read(OUT/'whole-owner-beforeimages.json')
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
# These are specific assessments of L2413-1 after reading all five complete
# target sources, proposals, NOTA and version boundaries in reference-targets.
assessments={
 'L1234-1':"Champs articulés : L1234-1 fixe quinze jours calendaires pour les nouveaux contrats uniques, y compris faute grave avec paiement si exécution impossible, et maintient l'ancien régime pour les contrats antérieurs. Il conserve expressément procédures collectives et autorisations protectrices. L2413-1 protège la décision de mission et distingue cette décision de la rupture de l'emploi : le préavis ne remplace aucune autorisation, aucune fin de mission n'autorise une rupture automatique et aucun délai d'autorisation n'est ramené à quinze jours.",
 'L1221-2':"Coordination compatible du contrat et de la mission : la proposition L1221-2 interdit tout nouveau terme d'emploi, y compris au retour d'un remplacé ou en fin de mission, conserve les anciens termes et droits et empêche le renouvellement futur d'un CDD. Les avantages restent ouverts aux situations futures de même objet. L2413-1 conserve exactement ces garanties dans ses quatre paragraphes déjà proposés ; l'ajout protecteur transfrontalier ne recrée ni CDD ni terme d'emploi et ne ferme aucune aide future éligible.",
 'L1234-9':"Différence de fait générateur : L1234-9 régit l'indemnité ordinaire d'une rupture à l'initiative de l'employeur, avec seuil d'un an à la fin effective incluant préavis,0,20mois par année totale au prorata et plafond six mois, exception faute grave, transition des anciens contrats et indemnités spéciales préservées. La NOTA source2017 porte sur les licenciements postérieurs à cette ordonnance. L2413-1 ne fixe aucune indemnité de fin de mission et ne conditionne aucun statut protecteur au seuil d'un an ; l'autorisation de mission ne dispense pas d'une autorisation de rupture distincte.",
 'L2314-22':"Le renvoi du1° demeure articulé à la source entière et à sa proposition : L2314-22 maintient les conditions de rattachement électoral tant que subsiste le contrat, y compris sans mission. Le refus d'une nouvelle mission par le salarié ou l'entreprise ne radie pas à lui seul le salarié ; les anciennes opérations électorales et recours restent sous leurs règles antérieures. Le1° de L2413-1 distingue déjà cette nouvelle mission de l'ancien contrat de mission, sans restaurer un nouveauCDD. L'extension du7°ter ne change ni ce1°, ni les mandats, ni l'ancienneté, ni le calendrier électoral.",
 'L231-11':"Le11° conserve les membres de conseil/administrateurs de caisse dans leur catégorie distincte du comité transfrontalier7°ter. La source de L231-11 renvoie à l'ancien L412-18 ; sa proposition conserve autorisation, six mois après mandat, trois mois pour candidats et prolongation saisonnière, avec références contemporaines et maintien des anciens contrats. Son renvoi à L2413-1 pour l'ancien travail temporaire reste opérant : aucune autorisation de mission n'est retirée, l'absence de mission ne termine pas l'emploi unique, et les quinze jours ne remplacent pas le statut. Cette analyse porte sur la version cible fournie et ne certifie pas toutes ses autres contreparties ni une autre version historique du même numéro."
}
row=next(a for a in answers if a['number']=='L2413-1');needed=snapshot['requirements'][refs.key(row)]
assert {snapshot['targets'][k]['number'] for k in needed}==set(assessments)
row['reference_checks']=[dict(target_key=k,view_sha256=snapshot['targets'][k]['view_sha256'],assessment=assessments[snapshot['targets'][k]['number']]) for k in needed]
for a in answers:
    if a['number']=='R2373-5':
        a['repeal_scope']="Abrogation du fondement réglementaire redondant de transmission systématique des justificatifs de participation, à la même borne que L2371-5 ; aucun envoi de remplacement, contrôles légaux et droits antérieurs préservés."
        a['repeal_policy_id']='editorial_direction_2026_10_19'
db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
try:
    for source in sources:
        key=source['code_id'],source['source_id'];proof=owners['|'.join(key)]
        current=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
        assert current==review_prior.draft_values(proof['whole_row']),key
        assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()==(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until']),key
        assert ingest.source_notes(db,*key)==source['source_notes_xml'],key
        owner=json.loads(Path(proof['path']).read_bytes())[proof['index']];assert owner==proof['whole_row'],key
        registry=read(ROOT/'registered-batches.json');assert registry['|'.join(key)]==proof['registry_entry'],key
    refs.check_guards(db,snapshot)
    results=[]
    for a,s in zip(answers,sources):
        try:
            runner.validate_answer([a],[s]);refs.accept_checks([a],[s],snapshot)
            results.append(dict(number=a['number'],ordinary_answer_benefit_impact_and_reference_checks_passed=True))
        except Exception as e:
            results.append(dict(number=a['number'],ordinary_checks_passed=False,error=str(e),no_guard_removed=True))
    refs.check_guards(db,snapshot)
finally:db.close()
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
put('candidate-answer.json',answers);put('ordinary-validation.json',results)
put('CONTROL.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),state='FIVE_CANDIDATES_ORDINARY_CHECKED_NOT_REGISTERED',
    ordinary_checks_all_passed=all(r.get('ordinary_answer_benefit_impact_and_reference_checks_passed') for r in results),
    configured_whole_targets_read=5,article_specific_assessments_for_L2413_1=5,
    new_body_and_metadata_guards_preserved=True,no_canonical_mutations=True,no_models_launched=True,
    no_shared_reservations_taken=True,no_completed_markers_changed=True,no_full_registration_or_global_validation_claimed=True,
    required_before_integration=['fresh whole owner/source/NOTA/version/five-field/registry guards',
       'fresh whole reference targets and current policies', 'actual common reservations and ordinary full registration validation',
       'durable full beforeimage archive before commit', 'DB/batch/registry/completed confrontation and semantic convergence afterwards'],
    external_commerce_and_European_limits_preserved=True,global_or_jurist_completion=False))
print(json.dumps(results,ensure_ascii=False))
