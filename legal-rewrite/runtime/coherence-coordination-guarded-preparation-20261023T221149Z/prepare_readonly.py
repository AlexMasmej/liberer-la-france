"""Stage three freshly guarded coordination candidates, without registering them."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, re, sqlite3, sys

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
WORK = ROOT / 'runtime/coherence-rollout-20261023T2042Z'
sys.path.insert(0, str(ROOT))
import ingest
import run_exhaustive as runner
import reference_coherence as references
import review_prior
from source_assets import load_companions

def sha(b):
    return hashlib.sha256(b).hexdigest()

def put(name, value):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')

def read(p):
    b = p.read_bytes()
    stable[p] = b
    return json.loads(b)

stable = {}
pins = read(WORK / 'resumption-observation-pins-v4.json')
pins['run_exhaustive.py'] = 'd826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
for name, expected in pins.items():
    assert sha((ROOT / name).read_bytes()) == expected, name
original = read(WORK / 'cch-financing-coordination-candidate.json')['candidates']
fiscal = read(WORK / 'fiscal-coherence-followup-and-candidate.json')['candidate']
candidates = original + [fiscal]
keys = {(a['code_id'], a['source_id']) for a in candidates}
owners = {}
paths = sorted(p for p in (ROOT / 'batches').glob('*/*.json')
               if re.fullmatch(r'(?:batch)?\d+\.json', p.name))
for p in paths:
    for i, row in enumerate(read(p)):
        key = (row['code_id'], row['source_id'])
        if key in keys:
            assert key not in owners, key
            owners[key] = (p, i, row)
assert set(owners) == keys
companions = load_companions()
sources, answers, owner_proofs = [], [], []
db = sqlite3.connect((ROOT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=15)
db.execute('BEGIN')
try:
    for candidate in candidates:
        key = (candidate['code_id'], candidate['source_id'])
        p, i, owner = owners[key]
        source = db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until '
                            'FROM articles WHERE code_id=? AND id=?', key).fetchone()
        current = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes '
                             'FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        assert current == review_prior.draft_values(owner), key
        prior = candidate['whole_beforeimage']
        assert all(owner[k] == v for k, v in prior.items()), key
        assert source[1] == candidate['source_sha256']
        if 'whole_source' in candidate:
            assert source[2:] == (candidate['whole_source'], candidate['valid_from'], candidate['valid_until'])
            assert ingest.source_notes(db, *key) == candidate['source_NOTA']
        previous = dict(source_sha256=current[0], status=current[1], proposed_xml=current[2],
                        reason=current[3], review_notes=current[4],
                        proposed_sha256=runner.digest(current[2]),
                        batch_row_sha256=review_prior.batch_row_sha256(owner))
        article = dict(code_id=key[0], source_id=key[1], number=source[0],
                       source_sha256=source[1], source_xml=source[2], valid_from=source[3],
                       valid_until=source[4], source_notes_xml=ingest.source_notes(db, *key),
                       previous_draft=previous, impact_check_required=True,
                       benefit_check_required=runner.mentions_possible_relief(source[2]))
        if key in companions:
            article['source_companions'] = companions[key]
        row = copy.deepcopy(owner)
        before = candidate.get('exact_before', candidate.get('only_change', {}).get('exact_before'))
        after = candidate.get('exact_after', candidate.get('only_change', {}).get('exact_after'))
        assert current[2].count(before) == 1
        assert current[2].replace(before, after) == candidate['proposed_xml']
        row['proposed_xml'] = candidate['proposed_xml']
        row.pop('reference_coherence', None)
        row.pop('substantive_impact_certificate', None)
        if key[0] == 'LEGITEXT000006074096':
            row['reason'] += " Coordination nécessaire : réserver expressément la dispense spéciale du 5° de L423-1-2, déjà applicable aux prêts et avances entrant dans son champ. Cette précision ne constitue pas un nouvel allègement distinct."
            row['review_notes'] += " Les deux dispositions générales L423-15 et L423-16 doivent être coordonnées ensemble avec L423-1-2(5). La dispense porte sur la déclaration préalable et le délai d'opposition prévus par ces articles, uniquement dans le champ spécial de L423-1-2. Les 5 %, alternatives du même groupe, contrôle effectif, ressources disponibles à long terme, plafonds livret A majoré de 1,5 point, information CGLLS et garanties antérieures demeurent. Les normes extérieures et l'ensemble du CCH ne sont pas certifiés par cette correction."
            row['benefit_review'] = "La dispense favorable du 5° de L423-1-2 reste ouverte dans son champ spécial aux situations futures éligibles et couvre déclaration et opposition. La mention ajoutée ne l'élargit pas. Les limites financières favorables, le plafond livret A majoré de 1,5 point et les garanties antérieures sont conservés intégralement ; aucun préavis de droit du travail n'est introduit dans ce régime de financement."
            # These exact passages anchor the existing SGA coordination; no new tax cut is claimed.
            source_plain = runner.impact_audit.plain(source[2])
            source_quote = ('il informe la société de garantie des organismes d\'habitations à loyer modéré contre les risques d\'opérations immobilières de la conclusion et des conditions de l\'avance.'
                            if source[0] == 'L423-15' else
                            'et la société de garantie des organismes d\'habitations à loyer modéré contre les risques d\'opérations immobilières mentionnée à l\'article L. 453-1 s\'il exerce une activité d\'accession à la propriété')
            assert source_quote in source_plain
            effect = dict(kind='coordination', measure_id='sru-sga-information-coordination',
                          description="Coordination du destinataire SGA après la suppression de sa mission légale ; la réserve de dispense ministérielle est rendue explicite sans nouvelle coupe autonome.",
                          before="Information SGA au titre de l'accession à la propriété, dans le champ décrit par la source entière.",
                          after="Pas d'information SGA pour les opérations nouvelles sur ce seul fondement ; obligations nécessaires aux garanties antérieures préservées.",
                          unit='legal_duty', affected_population="Organismes HLM consentant les avances ou prêts visés, selon les conditions propres à l'article.",
                          conditions_and_transition="Entrée en vigueur de la loi portant suppression des dispositions issues de la loi SRU ; garanties antérieures dans les limites expresses de L453-1 ; dispense ministérielle dans le seul champ spécial de L423-1-2(5).",
                          replacement_or_new_burdens="Aucune formalité de remplacement créée. L'information CGLLS et les conditions financières demeurent dans leur champ.",
                          source_quote=source_quote,
                          proposed_quote="le présent article n'impose plus d'information de la société de garantie mentionnée à l'ancien article L. 453-1 au seul titre de l'exercice d'une activité d'accession à la propriété.")
            row['substantive_impact'] = dict(version=1, classification='coordination_only',
                assessment="La proposition coordonne la suppression déjà acquise de la mission SGA et explicite une dispense spéciale déjà énoncée par L423-1-2(5). Elle ne constitue pas une nouvelle taxe ni un allègement autonome supplémentaire à compter.",
                scope_limitations="Aucun solde national ni effet budgétaire n'est établi. Les règles du code monétaire et financier, du code de commerce et les autres dispositions CCH restent à leur champ et hors certification exhaustive.",
                new_burdens_review="Aucune charge nouvelle identifiée dans l'insertion : ni déclaration, délai, registre ou condition supplémentaire. La réserve explicite limite la règle générale sans élargir la dispense spéciale ; conditions de financement et CGLLS inchangées.",
                effects=[effect])
        else:
            row['reason'] += " Coordination CRL : la rubrique I a ne vise expressément que les anciennes recettes demeurant imposables selon la transition de 234 nonies ; aucune nouvelle suppression d'impôt n'est comptée."
            row['review_notes'] += " La limite CRL dépend des recettes perçues avant l'entrée en vigueur de la loi supprimant cette contribution. Elle est distincte de la limite annuelle future de CVAE au II 3°. 234 nonies interdit déjà le rétablissement de taxe ou formalité pour les recettes nouvelles. Les autres rubriques et protections CFE, pertes, crédits et réserves déjà taxées demeurent byte-identiques. La chaîne complète des formulaires et des contreparties IS reste ouverte."
        sources.append(article)
        answers.append(row)
        owner_proofs.append(dict(code_id=key[0], source_id=key[1], owner_path=str(p),
            owner_index=i, owner_file_sha256=sha(stable[p]), whole_owner_row=owner,
            whole_owner_row_sha256=review_prior.batch_row_sha256(owner), only_XML_change=dict(before=before, after=after)))
    snapshot = references.capture(db, sources, answers)
    targets = []
    for code, number in [('LEGITEXT000006074096', 'L423-1-2'),
                         ('LEGITEXT000006069577', '234 nonies'),
                         ('LEGITEXT000006069574', '46 C')]:
        found = [(identifier,) for identifier, current_number in
                 db.execute('SELECT id,number FROM articles WHERE code_id=? AND valid_from<=? AND valid_until>?',
                            (code, '2026-10-18', '2026-10-18'))
                 if references.normalize(current_number) == references.normalize(number)]
        assert len(found) == 1, (code, number)
        identifier = found[0][0]
        view = references.view(db, code+'|'+identifier)
        view['valid_from'], view['valid_until'] = db.execute('SELECT valid_from,valid_until FROM articles WHERE code_id=? AND id=?', (code, identifier)).fetchone()
        targets.append(view)
    # Fresh whole-target readings supplied article-specific analyses for the
    # four configured dependencies of L423-16. No assessment is borrowed from
    # another referrer and any intervening target-body change still blocks.
    analyses = {
        'LEGITEXT000006072050|LEGIARTI000006901112': (
            '1b7be0af98978734f4057f70a2fb4a8225a7ca80c2545ba8ad5f79f7af9eca01',
            "Différence de champ : L1234-1 régit le préavis de licenciement des salariés, dont quinze jours calendaires pour les nouveaux contrats uniques et la transition propre aux anciens contrats. L423-16 régit des prêts entre organismes et son délai de quinze jours est une opposition ministérielle, pas un préavis salarial. La réserve de L423-1-2(5) n'importe aucune règle d'ancienneté, faute grave, préavis payé ou rupture dans ces prêts ; seule la dispense spéciale de déclaration/opposition demeure dans son champ."),
        'LEGITEXT000006072050|LEGIARTI000019071087': (
            '0a424087fd3feecf301564a0cb84a961f2da0ea518034152c6494836e516842e',
            "Différence de champ : L1221-2 concerne les contrats de travail privés nouveaux, leur durée indéterminée et la préservation des anciens contrats, exonérations et aides. Les prêts participatifs et autres prêts financiers de L423-16, notamment ses renvois au code monétaire et financier, ne sont pas des contrats d'emploi. Leur durée ou le long terme des ressources ne rétablit aucun CDD. La réserve ministérielle ne réduit ni les droits sociaux ni les avantages futurs des salariés et ne modifie aucun terme d'emploi."),
        'LEGITEXT000006072050|LEGIARTI000035644154': (
            '9b7995e6bf0920d79088da1bdde4530c3088ef1c8f730592709774f2a86fdeb8',
            "Différence de champ : L1234-9 détermine l'indemnité ordinaire de rupture à l'initiative de l'employeur et protège droits anciens, indemnités spéciales et créances acquises ; la NOTA vise les licenciements prononcés après l'ordonnance de2017. L423-16 traite contrôle capitalistique, ressources, prêts et information de la caisse, sans rupture d'emploi. Aucun seuil d'un an, taux0,20mois, plafond six mois ni exception de faute grave ne s'applique au prêt ou à la dispense ministérielle. Les conditions financières et protections salariales demeurent autonomes."),
        'LEGITEXT000006074096|LEGIARTI000048849256': (
            '8d556dd968bf97eff79aad52a64273efd6b5f8991a77ef746d372790028744c3',
            "Transition et champs compatibles : L452-1 identifie la CGLLS et maintient ses missions de garantie, aides et concours futurs, son versement ANRU de184millions jusqu'en2033 et le reversement ANCOLS. Sa proposition retire une approbation ministérielle individuelle de certaines subventions/conventions et coordonne les ressources du fonds sans rétablir les cotisations générale/additionnelle. L423-16 conserve l'information de cette caisse pour l'activité locative ; la dispense L423-1-2(5) porte sur la déclaration préalable aux ministres et leur opposition, pas sur cette information CGLLS. Aucun prélèvement nouveau ni affectation des fonds ANCOLS n'est créé par la coordination.")}
    cch16 = next(a for a in answers if a['source_id'] == 'LEGIARTI000037668236')
    needed = snapshot['requirements'][references.key(cch16)]
    assert set(needed) == set(analyses)
    cch16['reference_checks'] = []
    for identifier in needed:
        expected_hash, assessment = analyses[identifier]
        assert snapshot['targets'][identifier]['view_sha256'] == expected_hash, identifier
        cch16['reference_checks'].append(dict(target_key=identifier,
            view_sha256=expected_hash, assessment=assessment))
    validation = []
    for row, article in zip(answers, sources):
        try:
            runner.validate_answer([row], [article])
            references.accept_checks([row], [article], snapshot)
            validation.append(dict(source_id=row['source_id'], ordinary_answer_impact_benefit_and_reference_checks_passed=True))
        except Exception as error:
            validation.append(dict(source_id=row['source_id'], ordinary_checks_passed=False,
                                   error=str(error), no_guard_removed=True))
    references.check_guards(db, snapshot)
finally:
    db.close()
for p, before in stable.items():
    assert p.read_bytes() == before, str(p)
for name, expected in pins.items():
    assert sha((ROOT / name).read_bytes()) == expected, name
assert paths == sorted(p for p in (ROOT / 'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json', p.name))
put('source.json', sources)
put('candidate-answer.json', answers)
put('whole-owner-beforeimages.json', owner_proofs)
put('reference-targets.json', snapshot)
put('additional-semantic-counterparts.json', targets)
put('current-pins.json', pins)
put('ordinary-validation.json', validation)
put('CONTROL.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
    state='PREPARED_NOT_REGISTERED_SAFE_POINT_AND_FRESH_FULL_GUARDS_REQUIRED',
    articles=3, source_full_beforeimage_owner_NOTA_bounds_matched=True,
    source_database_readonly_transaction=True, canonical_mutations=0, models_launched=0,
    no_completed_markers_changed=True, no_response_replay=True,
    ordinary_checks_all_passed=all(x.get('ordinary_answer_impact_benefit_and_reference_checks_passed') for x in validation),
    no_full_global_registration_validation_or_independent_native_review_claimed=True,
    must_revalidate=['current whole source/NOTA/bounds', 'whole owner row and DB five fields',
                    'whole targets and current four policy guards', 'shared reservations at actual safe point',
                    'ordinary full registration validation', 'archive entire beforeimages before commit',
                    'DB/batch/registry/completed and reference convergence after commit'],
    legal_or_jurist_global_completion=False))
put('artifact-manifest.json', dict(files={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes()))
        for p in sorted(OUT.rglob('*')) if p.is_file()}))
print(json.dumps(dict(folder=str(OUT), validation=validation, canonical_mutations=0), ensure_ascii=False))
