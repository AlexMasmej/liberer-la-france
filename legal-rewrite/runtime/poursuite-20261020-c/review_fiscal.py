"""Record the parent's bounded whole-text counter-reading; never edit canon."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, sqlite3, sys

P = Path(__file__).resolve().parent
B = P.parents[1]
sys.path.insert(0, str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc

def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
F = P / 'fiscal/edition001'
m = read(F/'manifest.json')
for name, expected in m['files'].items():
    assert sha(F/name) == expected, name
db = sqlite3.connect('file:' + str(B/'corpus.sqlite') + '?mode=ro', uri=True)
db.execute('BEGIN')
entries = read(F/'source.json') + read(F/'references.json') + read(F/'direct-dependencies-read.json')
seen = set()
for s in entries:
    k = s['code_id'], s['source_id']
    if k in seen: continue
    seen.add(k)
    assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', k).fetchone() == (s['source_sha256'], s['source_xml']), k
    assert source_notes(db, *k) == s['source_notes_xml'], k
    d = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', k).fetchone()
    old = s.get('previous_draft')
    assert d == ((old['source_sha256'], old['proposed_xml']) if old else None), k
for sub in [F, F/'csi-coordination']:
    ss, aa = read(sub/'source.json'), read(sub/'answer.json')
    validate_answer(copy.deepcopy(aa), copy.deepcopy(ss))
    rc.check_guards(db, read(sub/'reference-targets.json'))
db.close()
review = dict(
    approved_at=datetime.now(timezone.utc).isoformat(),
    reviewer='Parent distinct de l’auteur fiscal',
    frozen_manifest_sha256=sha(F/'manifest.json'),
    sources_and_notes_read_entire=49,
    whole_proposed_bodies_read=30,
    retained_without_rewrite=19,
    fiscal_contexts_read_entire=34,
    direct_dependencies_read_entire=8,
    automatic_reference_targets_read_entire=6,
    current_source_notes_before_images_and_policy_guards=True,
    blocking_findings=[],
    findings=[
        '879 supprime la CSI pour les demandes nouvelles, y compris relatives à des actes anciens ; anciens avantages et restitutions préservés.',
        '881 II autonome conservé exactement ; 881 L garde les catégories, réductions historiques et suppression des garanties successorales futures.',
        '1020 conserve son 0,70 % dans son champ ; 1039 ne bascule pas au proportionnel et 1053 déjà exonéré est réservé.',
        '679/680 et autres fixes ciblés ne créent pas de taxation proportionnelle de substitution ; 691 bis conserve les engagements et prolongations 1594-0 G.',
        '1961 garde au même rang les trois alinéas sources et les restitutions historiques ; aucune restitution générale des anciennes dettes.',
        '674 retire le relèvement au minimum de 25 €, sans promettre une économie uniforme de 25 €.',
        'Une seule mesure CSI, une famille de droits fixes ciblés et un minimum retiré ; les 19 maintiens ne sont pas des simplifications nouvelles.'
    ],
    limitations=[
        'Pas de lecture complète ni réécriture revendiquée des décrets, arrêtés, formulaires ou codes externes listés dans unresolved-coordinations.json.',
        'Coût des services de publicité foncière et perte de recettes à chiffrer ; aucun autofinancement ni solde net national établi.',
        'Lecture IA bornée ; pas de contrôle par un juriste, pas de bilan global de simplification des cinq codes.'
    ],
    national_net_savings=None,
    semantic_review_by_jurist=False,
    answer_sha256=sha(F/'answer.json'),
    companion_answer_sha256=sha(F/'csi-coordination/answer.json'),
)
out = P/'fiscal-independent-review/edition001'
out.mkdir(parents=True, exist_ok=True)
(out/'review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(approved_articles=49, source_context_guards=len(seen), new_distinct_measure_families=3, canonical_mutation=False)))
