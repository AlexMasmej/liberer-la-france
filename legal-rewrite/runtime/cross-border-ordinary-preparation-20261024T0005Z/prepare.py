"""Prepare current sources/metadata/whole reference texts without registration."""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,sqlite3,sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime'
OLD=R/'cross-border-coherence-followup-20261023T230543Z'
sys.path.insert(0,str(ROOT))
import ingest,run_exhaustive as runner,reference_coherence as refs,review_prior
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_bytes())
def put(n,o):
    with (OUT/n).open('x') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')
pins=read(R/'coherence-rollout-20261023T2042Z/resumption-observation-pins-v4.json')|{'run_exhaustive.py':'d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'}
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
assert sha((OLD/'artifact-manifest.json').read_bytes())=='28846b3ff04163f2ebc272e4528003573381b81440317180d1efeeea9358694e'
for n,d in read(OLD/'artifact-manifest.json')['files'].items():assert sha((OLD/n).read_bytes())==d['sha256'],n
candidates=read(OLD/'candidate-texts.json');prior_owners=read(OLD/'whole-owner-beforeimages.json')
owners={};stable={};sources=[];answers=[]
registry_b=(ROOT/'registered-batches.json').read_bytes();registry=json.loads(registry_b)
db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
try:
    for candidate in candidates:
        key=candidate['code_id'],candidate['source_id'];proof=next(a for a in prior_owners if (a['code_id'],a['source_id'])==key)
        p=Path(proof['owner_path']);b=p.read_bytes();stable[p]=b;owner=json.loads(b)[proof['owner_index']]
        assert owner==proof['whole_owner_row'],key
        src=db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
        current=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
        assert current==review_prior.draft_values(owner),key
        assert src[1]==candidate['source_sha256'] and src[3:]==(candidate['valid_from'],candidate['valid_until'])
        assert ingest.source_notes(db,*key)==candidate['source_NOTA']
        assert registry['|'.join(key)]==dict(source_sha256=owner['source_sha256'],proposed_sha256=runner.digest(owner['proposed_xml']))
        previous=dict(zip(['source_sha256','status','proposed_xml','reason','review_notes'],current))
        previous.update(proposed_sha256=runner.digest(current[2]),batch_row_sha256=review_prior.batch_row_sha256(owner))
        source=dict(code_id=key[0],source_id=key[1],number=src[0],source_sha256=src[1],source_xml=src[2],
            valid_from=src[3],valid_until=src[4],source_notes_xml=ingest.source_notes(db,*key),previous_draft=previous,
            impact_check_required=True,benefit_check_required=runner.mentions_possible_relief(src[2]))
        row=copy.deepcopy(owner);row.update(status='rewrite_draft',proposed_xml=candidate['proposed_xml'],
            reason=candidate['proposed_reason'],prior_proposal_sha256=runner.digest(current[2]))
        row.pop('reference_coherence',None);row.pop('substantive_impact_certificate',None)
        row.pop('reference_checks',None)
        row['review_notes']="Lecture parentale entière des64textes du paquet transfrontalier230543Z, dont sources/NOTA/propositions et bornes. " + candidate['substantive_impact_plan'] + " Les renvois configurés sont recapturés entiers pour une analyse propre à ce reférant. Ni tous les renvois du code, ni le droit européen, ni le champ commercial externe au corpus ne sont certifiés. L229-3 commerce a été lu sur la seule page officielle au13mai2026 ; sa référence à la société européenne et au titreV appelle une qualification séparée. Aucune modification des sources ou NOTA, aucune incrimination étendue par inférence."
        if row['number'].startswith('L'):
            quote_before=("représentant au comité de la société issue d'une fusion transfrontalière" if row['number']=='L2411-12' else
                ('7° ter' if row['number']=='L2413-1' else '2° ter')+" Membre du groupe spécial de négociation et représentant au comité de la société issue de la fusion transfrontalière ;")
            quote_after=quote_before.replace("d'une fusion transfrontalière","d'une opération transfrontalière").replace('de la fusion transfrontalière',"d'une opération transfrontalière")
            mission=row['number']=='L2413-1'
            transition=("Interruptions de mission et notifications de non-renouvellement à compter de l'entrée en vigueur ; anciens et nouveaux contrats couverts, pas de nouveaux CDD, droits antérieurs et protections déjà applicables préservés." if mission else
                "Licenciements engagés à compter de l'entrée en vigueur de la loi ; contrats antérieurs comme nouveaux et protections déjà applicables préservés.")
            effects=[]
            if mission:
                effects=copy.deepcopy(owner['substantive_impact']['effects'])
            for kind,unit,description in [
                ('relief_extended','regime',"Rendre explicite la protection des représentants au comité des autres opérations transfrontalières, dans le prolongement de la même extension de L2411-1."),
                ('obligation_added','legal_duty',"Disposer expressément de la portée corrélative de l'autorisation protectrice et de la procédure dans les opérations autres que les fusions, sans présumer la charge nulle.")]:
                effects.append(dict(kind=kind,measure_id='protection-operations-transfrontalieres',description=description,
                    before="La catégorie du comité nomme expressément la fusion ; les autres protections ne sont pas toutes de même champ et ne permettent pas de déclarer tout représentant déjà couvert.",
                    after="La catégorie du comité vise une opération transfrontalière, avec conservation des autres mandats et de l'autorisation ou de la procédure protectrice.",
                    unit=unit,affected_population=("Salariés temporaires protégés et entreprises de travail temporaire prenant une décision de mission." if mission else "Représentants au comité concernés par les autres opérations et leurs employeurs envisageant un licenciement."),
                    conditions_and_transition=transition,replacement_or_new_burdens="Même extension protectrice que L2411-1, sans double décompte ; champ procédural explicite plus large, coût non chiffré. Aucun formulaire, registre ou délai supplémentaire propre à cette insertion.",
                    source_quote=quote_before,proposed_quote=quote_after))
            row['substantive_impact']=dict(version=1,classification='mixed',
                assessment="Par rapport à la source officielle entière, la catégorie de comité est expressément étendue de la fusion aux opérations transfrontalières. Cette extension protectrice a une contrainte patronale corrélative ; elle coordonne la même mesure de L2411-1, sans nouvelle réduction de charges à compter. "+("Les coordinations du contrat unique et des intermissions déjà proposées sont également conservées." if mission else "Toutes les autres catégories et la procédure source sont conservées."),
                scope_limitations="Aucun solde national ni absence de charge supplémentaire n'est établi. Les organes L2374-4, le groupe de négociation et les catégories européennes ont leurs champs propres. Les normes européennes et les procédures extérieures non fournies restent hors certification ; aucune incrimination n'est étendue.",
                new_burdens_review="L'extension peut imposer une autorisation ou une procédure protectrice à des situations autres que les fusions ; cette charge corrélative est identifiée sous la même measure_id que L2411-1. Aucun registre ou formulaire n'est ajouté. Les décisions de mission et de rupture d'emploi restent distinctes ; aucune double autorisation pour une seule décision n'est inventée.",effects=effects)
            row['benefit_review']="Les protections favorables de toutes les catégories sont conservées et la catégorie du comité est étendue de façon explicite aux autres opérations, pour les situations futures définies par la transition. Le groupe spécial de négociation et les organes sociaux ont leurs fondements propres ; aucune protection déjà applicable n'est réduite. Les procédures, autorisations, mandats antérieurs, rémunérations, ancienneté et voies de recours demeurent à leur champ. Le préavis de quinze jours et l'indemnité ordinaire du contrat unique ne remplacent aucune autorisation ni procédure spéciale. Les contrats antérieurs et futurs éligibles demeurent couverts ; aucun nouveau CDD n'est permis."
        else:
            row['substantive_impact']=dict(version=1,classification='coordination_only',
                assessment="La proposition coordonne la suppression des envois systématiques déjà décidée par L2371-5, au lieu de conserver même un envoi unique. R2372-17 et R2373-5 sont une seule mesure ; aucun second allègement matériel ni coût national n'est compté. L'information des salariés, les conditions de participation et les pouvoirs légaux de contrôle demeurent.",
                scope_limitations="La qualification commerciale de L229-3 pour les diverses opérations et le cadre européen restent ouverts. Les pouvoirs légaux de contrôle ne sont pas supprimés ; la correction n'établit pas une concordance de tous les renvois ni un solde net du corpus.",
                new_burdens_review="Aucune déclaration, attestation, dépôt ou conservation supplémentaire n'est créée en remplacement de l'envoi automatique. Les conditions commerciales de constitution et d'immatriculation, l'information des représentants et salariés ainsi que les contrôles sur leurs bases légales restent applicables sans extension de leur champ.",
                effects=[dict(kind='coordination',measure_id='participation-transfrontaliere-fin-envois-inspection',
                    description="Coordonner les règlements avec la même suppression législative des envois systématiques à l'inspection, sans retirer le contrôle de participation.",
                    before="La source entière exige la transmission à l'inspection des éléments fournis pour attester les modalités de participation ; les deux règlements décrivent le même envoi.",
                    after="L'envoi systématique n'est plus exigé au seul titre de la constitution ; aucun dépôt substitutif, contrôles et information des salariés préservés.",
                    unit='legal_duty',affected_population="Sociétés, filiales, établissements et dirigeants concernés par les opérations du titreVII, avec accord ou régime subsidiaire.",
                    conditions_and_transition="Même entrée en vigueur que la loi supprimant les transmissions de L2371-5 ; envois encore pendants pour opérations engagées ou réalisées également dispensés, autres actes et recours antérieurs conservés sous la loi répressive plus douce.",
                    replacement_or_new_burdens="Aucune formalité de remplacement ; les conditions commerciales et pouvoirs légaux de contrôle demeurent dans leur champ propre.",
                    source_quote="sont transmis à l'agent de contrôle de l'inspection du travail.",
                    proposed_quote=("ne font l'objet d'aucune transmission systématique à l'agent de contrôle de l'inspection du travail au seul titre de la constitution de la société issue de l'opération transfrontalière." if row['number']=='R2372-17' else "Aucun envoi, déclaration ou attestation de remplacement n'est exigé à ce titre."))])
            row['benefit_review']="La suppression de l'envoi administratif automatique ne retire aucun droit de participation, aucune information interne et aucune voie de recours des salariés ou de leurs représentants. Les pouvoirs légaux d'inspection et le contrôle commercial distinct sont conservés. Les envois encore à effectuer bénéficient de la même dispense, les envois réguliers antérieurs ne sont pas à refaire ; aucun nouveau dépôt ni condition de conservation ne remplace l'envoi retiré. Aucune exonération fiscale ou sociale n'est réduite et aucun coût national n'est inventé."
        row['policy_review_id']='substantive_outcomes_2026_10_19'
        sources.append(source);answers.append(row)
        owners['|'.join(key)]=dict(path=str(p),index=proof['owner_index'],file_sha256=sha(b),whole_row=owner,whole_row_sha256=review_prior.batch_row_sha256(owner),registry_entry=registry['|'.join(key)])
    snapshot=refs.capture(db,sources,answers)
    for target in snapshot['targets'].values():
        target['valid_from'],target['valid_until']=db.execute('SELECT valid_from,valid_until FROM articles WHERE code_id=? AND id=?',(target['code_id'],target['source_id'])).fetchone()
    refs.check_guards(db,snapshot)
finally:db.close()
for p,b in stable.items():assert p.read_bytes()==b,p
assert (ROOT/'registered-batches.json').read_bytes()==registry_b
for n,h in pins.items():assert sha((ROOT/n).read_bytes())==h,n
put('source.json',sources);put('candidate-answer-before-reference-assessments.json',answers)
put('whole-owner-beforeimages.json',owners);put('reference-targets.json',snapshot);put('current-pins.json',pins)
put('PREPARATION.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),canonical_mutations=0,models_launched=0,
    whole_owners_registry_and_five_fields_match=True,all77_pins_match=True,reference_target_readings_and_specific_assessments_still_required=True,
    ordinary_validation_not_yet_claimed=True,configured_targets=len(snapshot['targets']),registered=False))
print(json.dumps(dict(articles=len(sources),targets=len(snapshot['targets']),requirements={next(a['number'] for a in sources if refs.key(a)==k):[snapshot['targets'][t]['number'] for t in v] for k,v in snapshot['requirements'].items()}),ensure_ascii=False))
