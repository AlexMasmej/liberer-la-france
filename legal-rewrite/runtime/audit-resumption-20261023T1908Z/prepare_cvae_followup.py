"""Prepare a read-only guard-change packet; does not qualify the whole review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sqlite3, sys

sys.dont_write_bytecode = True
OP = Path(__file__).resolve().parent
ROOT = OP.parents[1]
sys.path.insert(0, str(ROOT))
from ingest import source_notes

AUDIT = ROOT / 'runtime/global-reference-audit-20261023T1908Z'
ORIGIN = ROOT / 'runtime/cvae-semantic-recheck-20261022T103000Z'
OUT = ROOT / 'runtime/cvae-guard-change-followup-20261023T1912Z'
OUT.mkdir(exist_ok=False)

def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else (b or '').encode()).hexdigest()

def save(name, value):
    with (OUT / name).open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')

origin_manifest_bytes = (ORIGIN / 'artifact-manifest.json').read_bytes()
assert sha(origin_manifest_bytes) == '9772b0e19d495979d553edf9d0c776ba5d321172b0d653816025a6133a4cfad5'
origin_manifest = json.loads(origin_manifest_bytes)
originals = []
origin_pins = {}
for name in ('review-packet.json', 'review-dependencies.json'):
    b = (ORIGIN / name).read_bytes()
    expected = origin_manifest['files'][name]
    assert sha(b) == expected['sha256'] and len(b) == expected['bytes']
    origin_pins[name] = expected
    originals.extend(json.loads(b)['articles'])
assert len(originals) == 13 and len({x['key'] for x in originals}) == 13
inheritance = json.loads((AUDIT / 'semantic-review-inheritance.json').read_text())
review = next(x for x in inheritance['reviews'] if x['label'] == 'CVAE')
guards = {x['key']: x for x in review['article_guards']}
assert not review['classification_applies_to_new_snapshot']
assert all(x['matches'] for x in review['policies'].values())
changed = {k for k, x in guards.items() if not x['matches_prior_guard']}
assert changed == {'LEGITEXT000006069574|LEGIARTI000026348025', 'LEGITEXT000006069574|LEGIARTI000053218832'}
con = sqlite3.connect((AUDIT / 'corpus.snapshot.sqlite').resolve().as_uri() + '?mode=ro', uri=True)
con.row_factory = sqlite3.Row
con.execute('PRAGMA query_only=ON')
con.execute('BEGIN')
current = []
comparisons = []
for old in originals:
    code, identifier = old['key'].split('|')
    article = dict(con.execute('SELECT * FROM articles WHERE code_id=? AND id=?', (code, identifier)).fetchone())
    draft = dict(con.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?', (code, identifier)).fetchone())
    doc = dict(con.execute("SELECT * FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", (code, identifier)).fetchone())
    xml = doc.pop('xml')
    xml = xml.decode() if isinstance(xml, bytes) else xml
    notes = source_notes(con, code, identifier)
    guard = guards[old['key']]['new_snapshot_guard']
    assert sha(xml) == guard['article_document_sha256'] == article['source_sha256']
    assert sha(article['content_xml']) == guard['source_body_sha256']
    assert sha(notes) == guard['source_notes_sha256']
    assert sha(draft['proposed_xml']) == guard['proposal_sha256']
    assert draft['source_sha256'] == guard['draft_source_sha256']
    row = dict(article, key=old['key'], draft=draft, article_document_xml=xml,
               article_document_metadata=doc, source_notes_xml=notes,
               snapshot_guard=guard, version_boundaries_checked=True)
    current.append(row)
    if old['key'] in changed:
        comparisons.append(dict(key=old['key'], number=article['number'], old=old, current=row,
                                source_body_notes_version_unchanged=all(old[k] == article[k] for k in ('content_xml','valid_from','valid_until','source_sha256')) and old['source_notes_xml'] == notes,
                                prior_guard=guards[old['key']]['prior_guard'], new_snapshot_guard=guard))
con.rollback()
con.close()
save('current-thirteen-article-packet.json', dict(snapshot=str(AUDIT / 'corpus.snapshot.sqlite'), query_only=True,
     audit_id=inheritance['audit_id'], articles=current, semantic_full_read_count_this_followup=2))
save('two-changed-article-comparison.json', dict(articles=comparisons, comparison_scope='Two changed articles read in full; remaining eleven exact guards checked only.'))
for name, pin in review['policies'].items():
    b = (AUDIT / name).read_bytes()
    assert sha(b) == pin['new_snapshot_sha256']
    (OUT / name).write_bytes(b)
save('ORIGIN.json', dict(prepared_at_utc=datetime.now(timezone.utc).isoformat(), audit=str(AUDIT),
     audit_id=inheritance['audit_id'], audit_manifest_sha256=sha((AUDIT / 'artifact-manifest.json').read_bytes()),
     origin=str(ORIGIN), origin_manifest_sha256=sha(origin_manifest_bytes), origin_files=origin_pins,
     original_review_id=review['review_id'], whole_packet_articles=13, changed_articles_full_read=2,
     unchanged_article_guards=11, unchanged_policy_guards=4, full_fresh_CVAE_review_complete=False,
     inherited_CVAE_classification_applicable=False, canonical_mutations=0, jurist_review=False))
report = '''# Suivi des deux changements CVAE

Le nouvel audit 1908Z a correctement refusé de reconduire la revue CVAE : les propositions des articles 46 C et 39 de l'annexe III ont changé. Leurs sources entières, notes, bornes de version et empreintes de document sont inchangées. Les onze autres gardes d'article et les quatre politiques correspondent à l'origine publiée sous empreinte.

Les deux sources et propositions, anciennes et nouvelles, ainsi que leurs motifs et notes actuels ont été lus intégralement pour ce suivi. Le dossier rassemble aussi les treize textes actuels, mais leur extraction et la concordance des onze autres gardes ne sont pas une nouvelle lecture sémantique de ces onze textes.

Pour 46 C, la suppression future du tableau CVAE reste explicite, à compter des années d'imposition débutant le 1er janvier de l'année suivant l'entrée en vigueur de la loi de suppression. Les obligations antérieures et les définitions et obligations autonomes de plafonnement de CFE sont expressément conservées. Le texte ajoute cependant des coordinations substantielles sur les sociétés civiles, la contribution sur les revenus locatifs, l'impôt sur les sociétés et l'usage de données déjà accessibles. Leurs interactions et renvois doivent être réexaminés avant toute nouvelle conclusion sur les treize articles.

Pour 39, la suppression des données CVAE futures et la conservation des obligations des années antérieures restent explicites, avec le même seuil annuel. Les nouvelles réductions portant sur le code APE, les bases de formation dans ce circuit fiscal, une ligne de rémunération nette et les totaux demandent leur propre contrôle des déclarations autonomes, transitions et protections. Les huit champs suisses restent présents ; leur conformité internationale n'est pas certifiée par ce suivi. La note de source sur l'entrée en vigueur au 1er janvier 2026 reste distincte des dates futures du projet.

Cette comparaison n'établit pas à elle seule une contradiction nouvelle dans les deux clauses CVAE examinées. Elle ne renouvelle pas la conclusion de cohérence sur les treize textes et ne clôt aucun signalement global. Une relecture fraîche des treize textes, des cibles modifiées et de leurs transitions reste requise. Aucun texte canonique ni preuve publiée n'a été modifié et aucune réponse ancienne n'a été rejouée.
'''
(OUT / 'REPORT.md').write_text(report)
files = {p.name:dict(bytes=p.stat().st_size, sha256=sha(p.read_bytes())) for p in sorted(OUT.iterdir()) if p.is_file()}
save('artifact-manifest.json', dict(files=files))
print(json.dumps(dict(folder=str(OUT), manifest_sha256=sha((OUT/'artifact-manifest.json').read_bytes()), semantic_full_review_complete=False)))
