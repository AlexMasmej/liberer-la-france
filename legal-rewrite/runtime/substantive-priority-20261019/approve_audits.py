"""Adopt bounded full-text AI audits only while their exact texts are current."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sqlite3
import sys

LEGAL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LEGAL))
from ingest import source_notes
from substantive_impact import validate, certificate, digest

BASE = LEGAL / 'runtime/continuation-exhaustive-20261019'
POLICY_SHA = digest((LEGAL / 'policy-coordinations.json').read_text())
STAMP = datetime.now(timezone.utc).isoformat()
approved = []
skipped = []


def adopt(db, item, reviewer, evidence):
    key = item['code_id'], item['source_id']
    official = db.execute('SELECT number,content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?', key).fetchone()
    current = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    notes = source_notes(db, *key)
    if (not official or not current or official[2] != item['source_sha256']
            or current[0] != official[2] or digest(current[2]) != item['proposed_sha256']):
        skipped.append({'code_id': key[0], 'source_id': key[1], 'reason': 'A later whole-article proposal superseded the audited snapshot'})
        return
    if 'source_body_sha256' in item:
        assert digest(official[1]) == item['source_body_sha256'], key
    if 'source_notes_sha256' in item:
        assert digest(notes) == item['source_notes_sha256'], key
    if 'source_notes_xml' in item:
        assert notes == item['source_notes_xml'], key
    dependencies = item.get('dependency_guards', [])
    for guard in dependencies:
        dep_key = guard['code_id'], guard['source_id']
        target = db.execute('SELECT content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?', dep_key).fetchone()
        draft = db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?', dep_key).fetchone()
        if (not target or target[1] != guard['source_sha256']
                or digest(target[0]) != guard['source_body_sha256']
                or digest(source_notes(db, *dep_key)) != guard['source_notes_sha256']
                or digest(draft[0] if draft else None) != guard['proposed_sha256']):
            skipped.append({'code_id': key[0], 'source_id': key[1], 'reason': 'An audited dependency changed after the full-text reading'})
            return
    source = {'source_xml': official[1], 'source_notes_xml': notes, 'source_sha256': official[2]}
    row = {'proposed_xml': current[2], 'status': current[1], 'substantive_impact': item['substantive_impact']}
    validate(row, source, required=True, enforce_workflow=False)
    approved.append({'code_id': key[0], 'source_id': key[1],
                     'assessment': item['substantive_impact'],
                     'certificate': certificate(row, source, POLICY_SHA),
                     'reviewed_by': reviewer, 'approved_at': STAMP,
                     'evidence_file': str(evidence.relative_to(LEGAL)),
                     'dependency_guards': dependencies,
                     'semantic_review_by_jurist': False})


db = sqlite3.connect('file:' + str(LEGAL / 'corpus.sqlite') + '?mode=ro', uri=True)
db.execute('BEGIN')
try:
    path = BASE / 'recent-fiscal-audit/article-findings.json'
    for item in json.loads(path.read_text()):
        adopt(db, item, 'Agent IA fiscalité — relecture distincte du rédacteur du lot', path)
    path = BASE / 'recent-logement-audit/article-results.json'
    for item in json.loads(path.read_text())['article_results']:
        adopt(db, item, 'Agent IA logement — relecture distincte du rédacteur du lot', path)
    for name in ['core-measures-audit', 'core-fiscal-measures-audit']:
        path = BASE / name / 'article-findings.json'
        if not path.exists():
            continue
        for item in json.loads(path.read_text()):
            if name == 'core-measures-audit' and item['number'] in {'L1221-2', 'L1234-1', 'L1234-9'}:
                reviewer = 'Contrelecture intégrale par le parent ; contribution antérieure de l’agent auteur déclarée'
            else:
                reviewer = 'Agent IA — relecture des sources et propositions entières distincte de la déclaration du worker'
            adopt(db, item, reviewer, path)
    for name in ['recent-logement-audit/candidate/edition002', 'd241-history-audit/edition002',
                 'recent-fiscal-audit/candidate/edition003']:
        path = BASE / name / 'answer.json'
        registration = path.parent / 'registration.json'
        if not registration.exists():
            continue
        sources = {(row['code_id'], row['source_id']): row for row in json.loads((path.parent / 'source.json').read_text())}
        for row in json.loads(path.read_text()):
            source = sources[row['code_id'], row['source_id']]
            item = row | {'proposed_sha256': digest(row['proposed_xml']),
                          'source_notes_xml': source['source_notes_xml'],
                          'source_body_sha256': digest(source['source_xml'])}
            adopt(db, item, 'Contrelecture IA du parent et relecture IA distincte du rédacteur', path)
    # The concrete counterexample raised by the user was read in full by root.
    key = 'LEGITEXT000006069577', 'LEGIARTI000006302199'
    official = db.execute('SELECT content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?', key).fetchone()
    current = db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    adopt(db, {'code_id': key[0], 'source_id': key[1], 'source_sha256': official[1],
               'source_body_sha256': digest(official[0]), 'proposed_sha256': digest(current[0]),
               'substantive_impact': {
                   'version': 1, 'classification': 'editorial_only', 'effects': [],
                   'assessment': 'L’article 1 A du CGI conserve l’impôt annuel sur le revenu, ses huit catégories de revenus, la déduction des charges et les renvois 14 à 155 et 156 à 168. La reformulation ne démontre aucune baisse de taux, d’assiette, de déclaration ou d’autorisation.',
                   'scope_limitations': 'Cette comparaison porte sur cet article et sa proposition entière. Elle ne chiffre pas l’IR des foyers, ne modifie pas son barème et ne mesure pas le solde de complexité des codes.',
                   'new_burdens_review': 'Aucune obligation nouvelle identifiée dans la proposition par rapport à la source de cet article ; les règles fiscales existantes restent en place. La contribution à une réduction nette demeure nulle ou non démontrée, sans économie attribuée à cette rédaction.'}},
          'Contrelecture intégrale par le parent — distincte du rédacteur du lot',
          LEGAL / 'runtime/substantive-priority-20261019/approve_audits.py')
finally:
    db.close()

target = LEGAL / 'runtime/substantive-audits.json'
if target.exists():
    old = json.loads(target.read_text())
    new_keys = {(a['code_id'], a['source_id']) for a in approved}
    approved += [a for a in old['audits'] if (a['code_id'], a['source_id']) not in new_keys]
data = {'version': 1, 'scope': 'Bounded full-text AI counter-readings, not a corpus-wide net-impact or jurist audit',
        'approved_at': STAMP, 'policy_sha256': POLICY_SHA, 'audits': approved}
temporary = target.with_suffix('.tmp')
temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
temporary.replace(target)
(Path(__file__).parent / 'audit-adoption.json').write_text(json.dumps(
    {'audit_entries': len(approved), 'superseded_snapshots_not_newly_approved': skipped,
     'national_savings': None, 'net_global_reduction': 'not_established'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'audit_entries': len(approved), 'superseded_snapshots_skipped': len(skipped),
                  'global_net_reduction_established': False}))
