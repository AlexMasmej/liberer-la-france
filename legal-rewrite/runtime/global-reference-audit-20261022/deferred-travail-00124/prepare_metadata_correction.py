"""Prepare one metadata-only repair; validate copies, never register anything."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[2]
JOB = PROJECT / 'runtime/exhaustive/jobs/travail-00124'
sys.path.insert(0, str(PROJECT))
import substantive_impact as impact
import reference_coherence as references
from run_exhaustive import validate_answer, policy_is_current
from register_batches import validate_batches
from ingest import source_notes


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value or b'').hexdigest()


def write(name, value):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def read_json(name):
    return json.loads((JOB / name).read_text())


names = ('source.json', 'answer.json', 'reference-targets.json', 'coordination.json',
         'policy.json', 'policy-fingerprint.json', 'validation-failure.json',
         'result.json', 'result-schema.json', 'build_answer.py',
         'errors-1.log', 'errors-2.log', 'errors-3.log')
input_hashes = {name: {'sha256': sha((JOB / name).read_bytes()), 'bytes': (JOB / name).stat().st_size}
                for name in names}
source, original, snapshot = read_json('source.json'), read_json('answer.json'), read_json('reference-targets.json')
write('source.frozen.json', source)
write('answer.original.json', original)
write('reference-targets.frozen.json', snapshot)
write('validation-failure.original.json', read_json('validation-failure.json'))
assert len(source) == len(original) == 24
assert read_json('result.json') == {'output_file': 'answer.json', 'article_count': 24}

before_checks = []
for row, canonical in zip(original, source):
    try:
        impact.validate(deepcopy(row), canonical, required=bool(canonical.get('impact_check_required')))
        result = {'passed': True}
    except ValueError as error:
        result = {'passed': False, 'error': str(error)}
    before_checks.append({'number': row['number'], 'source_id': row['source_id'], **result})
failed = [row for row in before_checks if not row['passed']]
assert len(failed) == 1 and failed[0]['number'] == 'L5214-1 B'
assert failed[0]['error'] == 'Duplicate measure and effect in one article'
try:
    validate_answer(deepcopy(original), source)
except ValueError as error:
    original_normal_failure = str(error)
else:
    raise AssertionError('Expected original answer to reproduce the normal failure')
assert original_normal_failure == 'Duplicate measure and effect in one article'

corrected = deepcopy(original)
index = next(i for i, row in enumerate(corrected) if row['number'] == 'L5214-1 B')
row = corrected[index]
effects = row['substantive_impact']['effects']
assert len(effects) == 3
assert len({(effect['measure_id'], effect['kind']) for effect in effects}) == 1
assert effects[0]['kind'] == 'obligation_removed'
assert effects[0]['measure_id'] == 'handicap-convention-fin-circuits-separes'
combined = deepcopy(effects[0])
for field in ('description', 'before', 'after'):
    combined[field] = ' '.join(str(i + 1) + ') ' + effect[field] for i, effect in enumerate(effects))
for field in ('unit', 'affected_population', 'conditions_and_transition', 'replacement_or_new_burdens'):
    assert len({effect[field] for effect in effects}) == 1, field


def continuous_quote(body, quote_field):
    plain = impact.plain(body)
    spans = []
    for effect in effects:
        quote = impact.plain(effect[quote_field])
        start = plain.index(quote)
        spans.append((start, start + len(quote)))
    start, end = min(a for a, _ in spans), max(b for _, b in spans)
    quote = plain[start:end]
    # No paraphrase or ellipsis; every old quote is verbatim in one continuous
    # passage of the full article, including context between the three duties.
    assert quote in plain
    assert all(effect[quote_field] in quote for effect in effects)
    return quote


combined['source_quote'] = continuous_quote(source[index]['source_xml'], 'source_quote')
combined['proposed_quote'] = continuous_quote(row['proposed_xml'], 'proposed_quote')
row['substantive_impact']['effects'] = [combined]

# The sole JSON change is the merged metadata array of this article.
expected = deepcopy(original)
expected[index]['substantive_impact']['effects'] = [combined]
assert corrected == expected
for old, new in zip(original, corrected):
    assert old.get('proposed_xml') == new.get('proposed_xml')
    for field in set(old) - {'substantive_impact'}:
        assert old[field] == new[field], (old['number'], field)
    for field in set(old['substantive_impact']) - {'effects'}:
        assert old['substantive_impact'][field] == new['substantive_impact'][field]
    if old['number'] != 'L5214-1 B':
        assert old == new
write('answer.corrected.json', corrected)
write('validation-batches/candidate/00124.json', corrected)

# The normal worker validators add certificates to their arguments. Run only
# against an ephemeral deep copy and discard the generated certificates.
checked = validate_answer(deepcopy(corrected), source)
references.accept_checks(checked, source, snapshot)
db = sqlite3.connect((PROJECT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=2)
db.execute('PRAGMA query_only=ON')
try:
    references.check_guards(db, snapshot)
    current_sources, preexisting_drafts = [], []
    for canonical in source:
        key = canonical['code_id'], canonical['source_id']
        current = db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone()
        expected_source = (canonical['number'], canonical['source_sha256'], canonical['source_xml'], canonical['valid_from'], canonical['valid_until'])
        notes_match = source_notes(db, *key) == canonical.get('source_notes_xml', '')
        current_sources.append({'number': canonical['number'], 'source_id': canonical['source_id'],
                                'source_and_dates_match': current == expected_source, 'notes_match': notes_match})
        existing = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        if existing:
            preexisting_drafts.append({'number': canonical['number'], 'source_id': canonical['source_id'],
                'source_sha256': existing[0], 'status': existing[1], 'proposed_sha256': sha(existing[2]),
                'proposed_is_null': existing[2] is None})
    records, diagnostics, batches = validate_batches(db, OUT / 'validation-batches')
finally:
    db.close()
assert len(records) == 24
assert all(item['source_and_dates_match'] and item['notes_match'] for item in current_sources)
assert policy_is_current(JOB)
assert all(sha((JOB / name).read_bytes()) == entry['sha256'] for name, entry in input_hashes.items())

preserved_facts = []
for i, effect in enumerate(effects):
    preserved_facts.append({'original_effect_index': i, 'measure_id': effect['measure_id'], 'kind': effect['kind'],
        'description': effect['description'], 'before': effect['before'], 'after': effect['after'],
        'source_quote': effect['source_quote'], 'proposed_quote': effect['proposed_quote'],
        'all_descriptive_fields_preserved_verbatim': all(effect[field] in combined[field] for field in ('description', 'before', 'after')),
        'both_original_quotes_preserved_verbatim_in_continuous_quotes':
            effect['source_quote'] in combined['source_quote'] and effect['proposed_quote'] in combined['proposed_quote']})

guards = {'job_input_files': input_hashes,
    'current_policy_files': {name: sha((PROJECT / name).read_bytes()) for name in ('policy-coordinations.json', 'site-summaries.json', 'reference-focus-extra.json')},
    'validator_implementation_files': {name: sha((PROJECT / name).read_bytes()) for name in ('substantive_impact.py', 'run_exhaustive.py', 'reference_coherence.py', 'register_batches.py')},
    'corrected_answer_sha256': sha((OUT / 'answer.corrected.json').read_bytes()),
    'per_article_proposal_hashes': [{'number': old['number'], 'source_id': old['source_id'],
        'source_sha256': old['source_sha256'], 'proposed_is_null': old['proposed_xml'] is None,
        'before_sha256': sha(old['proposed_xml']), 'after_sha256': sha(new['proposed_xml']),
        'strict_string_equality': old['proposed_xml'] == new['proposed_xml']}
        for old, new in zip(original, corrected)],
    'reference_snapshot_sha256': input_hashes['reference-targets.json']['sha256'],
    'recheck_all_guards_before_any_registration': True}
write('guards.json', guards)
write('before-after-proof.json', {'modified_article': row['number'], 'source_id': row['source_id'],
    'only_modified_json_path': '/' + str(index) + '/substantive_impact/effects',
    'all_24_proposed_xml_strictly_identical': True, 'all_other_articles_strictly_identical': True,
    'all_statuses_reasons_review_notes_benefits_and_reference_checks_unchanged': True,
    'original_effects': effects, 'merged_effect': combined, 'fact_preservation': preserved_facts,
    'original_effect_count': sum(len(a['substantive_impact']['effects']) for a in original),
    'corrected_effect_count': sum(len(a['substantive_impact']['effects']) for a in corrected),
    'counting': 'One measure/effect entry with three documented removed duties, not three invented measure IDs and not the removal of any substantive fact.',
    'no_active_file_changed': True, 'no_certificate_saved_in_candidate': all('substantive_impact_certificate' not in a and 'reference_coherence' not in a for a in corrected)})
write('validation.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'original_normal_validation_error': original_normal_failure, 'original_impact_validation_by_article': before_checks,
    'corrected_normal_validate_answer': 'passed_24_articles',
    'corrected_reference_accept_checks': 'passed_19_assessments',
    'current_reference_check_guards': 'passed', 'current_policy_check': 'passed',
    'current_canonical_sources_and_notes': current_sources,
    'current_preexisting_drafts': preexisting_drafts,
    'isolated_batch_validation': {'passed': True, 'articles': len(records), 'diagnostics': diagnostics, 'files': batches},
    'impact_certificates_created_in_memory_and_discarded': sum('substantive_impact_certificate' in a for a in checked),
    'reference_certificates_created_in_memory_and_discarded': sum('reference_coherence' in a for a in checked),
    'certificates_saved_to_active_files': False, 'database_committed': False,
    'writer_lock_used': False, 'draft_slot_reserved': False, 'new_drafting_cli_started': False,
    'job_inputs_still_match_initial_hashes': True, 'legal_review': False})
pending = [
    "L5213-13-1 conserve explicitement une formulation source incomplète (« à la suite d'une entreprise adaptée »); aucune complétion législative n'est inventée par cette correction de métadonnées.",
    "L5214-1 B conserve le signalement du nom institutionnel historique du conseil national; sa vérification institutionnelle ne relève pas du doublon et n'est pas prétendue résolue.",
    "Les décrets, les aides et les renvois nouveaux internes au lot L5213-13-1 et L5214-1 B restent soumis à la coordination éditoriale indiquée dans les review_notes inchangées. Les contrôles du catalogue contrat unique ne valent pas revue juridique globale.",
    "Un autre rédacteur ou une politique ultérieure peut modifier un élément gardé après ce contrôle; root doit refaire les gardes avant tout enregistrement et s'arrêter en cas de divergence.",
]
write('diagnosis.json', {'job': 'travail-00124', 'failure': original_normal_failure,
    'cause': "L5214-1 B possède trois objets distincts pour la même paire (handicap-convention-fin-circuits-separes, obligation_removed). La fonction substantive_impact.validate interdit toute répétition de cette paire dans un article.",
    'semantic_basis_for_merge': [
        "Les trois sous-effets appartiennent au même dispositif de convention pluriannuelle et retirent ses circuits obligatoires séparés: comité de suivi, transmission pour avis national, avis régional des organismes déjà associés.",
        "Les parties, les rubriques 1° à 5°, les services, aides et moyens, l'évaluation, les déclinaisons et plans régionaux sont conservés dans le texte inchangé. Fusionner les métadonnées ne rétablit aucun circuit ni ne supprime une aide.",
        "Le kind reste obligation_removed et la measure_id reste identique; les trois descriptions et couples avant/après sont réunis, les passages de preuve couvrent continûment toutes les citations originales.",
        "La baisse du nombre d'objets effects de 10 à 8 corrige la représentation; les trois obligations retirées restent explicitement documentées dans un seul effet. Aucun nouveau gain national ou montant d'économie n'est avancé.",
    ], 'candidate_status': 'metadata_only_ready_for_root_guarded_registration_decision',
    'pending_issues_not_fixed': pending, 'registration_authorized_or_performed_by_this_helper': False})
text = [
    '# Correction préparée — travail-00124', '',
    "Le rejet provient uniquement des trois objets d'impact de L5214-1 B ayant la même paire measure_id/kind. La correction fusionne ces objets; elle garde les trois obligations retirées et chacune de leurs preuves dans des passages continus exacts.", '',
    'Les 24 proposed_xml sont strictement identiques avant/après, y compris les valeurs null des 18 maintiens. Les six propositions, les avantages, raisons, notes et 19 analyses de renvoi sont inchangés.', '',
    'Validations réussies sur des copies en mémoire: validate_answer, substantive_impact.validate, reference_coherence.accept_checks, check_guards et validate_batches sur une arborescence isolée. Les sources/notes et politiques courantes correspondent aux captures du lot.', '',
    "Aucun enregistrement, verrou d'écriture, créneau, nouveau CLI de rédaction ni certificat actif. Les certificats produits par les validateurs ont été jetés avec les copies en mémoire. Root doit revérifier guards.json avant toute inscription.", '',
    '## Réserves conservées', '',
] + ['- ' + item for item in pending]
(OUT / 'REPORT.md').write_text('\n'.join(text) + '\n')
write('artifact-manifest.json', {'job': 'travail-00124', 'files': {
    str(path.relative_to(OUT)): {'sha256': sha(path.read_bytes()), 'bytes': path.stat().st_size}
    for path in sorted(OUT.rglob('*')) if path.is_file() and path.name != 'artifact-manifest.json'},
    'original_inputs_guarded': input_hashes, 'no_active_mutations': True})
print(json.dumps({'candidate': str(OUT / 'answer.corrected.json'), 'articles': 24,
    'proposed_xml_strictly_identical': True, 'original_error_reproduced': original_normal_failure,
    'normal_validation': 'passed', 'reference_accept_checks': 'passed',
    'current_source_reference_policy_guards': 'passed', 'isolated_batch_validation': 'passed',
    'preexisting_drafts': len(preexisting_drafts), 'no_active_mutations': True}, ensure_ascii=False))
