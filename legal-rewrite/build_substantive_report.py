"""Build an honest, snapshot-bound public account of declared material effects.

Call build(out, exportroot, dbpath, batchesroot) while the publisher already holds
its publication lock. This module takes no publication/writer lock and never
opens the canonical database. dbpath locates the policy and optional approved
audit file; a newer database cannot invalidate an otherwise coherent export.

Optional runtime/substantive-audits.json format:
{"version": 1, "audits": [{"code_id": "...", "source_id": "...",
 "assessment": {substantive_impact object}, "certificate": {version + guards},
 "reviewed_by": "...", "approved_at": "..."}]}
The worker field names substantive_impact/substantive_impact_certificate also
work. Approval is asserted by the owner-controlled file, never inferred from a
worker declaration or from matching hashes. No jurist approval is inferred.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import html
import json
import re
from urllib.parse import urlencode

import substantive_impact as impact_rules

VERSION = 1
LABELS = {
    'material_reduction': 'Allègement déclaré',
    'coordination_only': 'Coordination nécessaire',
    'editorial_only': 'Rédaction seule',
    'retained_necessary': 'Disposition nécessaire maintenue',
    'financing_transfer': 'Transfert de financement',
    'payment_timing_relief': 'Allègement du calendrier de paiement',
    'mixed': 'Effets mixtes ou charges nouvelles',
    'reserved': 'Emplacement réservé',
}
KIND_LABELS = {
    'tax_removed': 'Prélèvement supprimé', 'tax_reduced': 'Prélèvement réduit',
    'obligation_removed': 'Obligation supprimée', 'obligation_merged': 'Obligations fusionnées',
    'authorization_removed': 'Autorisation supprimée', 'regime_merged': 'Régimes fusionnés',
    'deadline_reduced': 'Délai réduit', 'compliance_cost_reduced': 'Coût de démarche réduit',
    'tax_increased': 'Prélèvement accru', 'obligation_added': 'Obligation ajoutée',
    'deadline_increased': 'Délai accru', 'complexity_added': 'Complexité ajoutée',
    'financing_transfer': 'Financement transféré', 'relief_preserved': 'Avantage préservé',
    'coordination': 'Coordination de la même mesure',
    'payment_deferred': 'Paiement reporté ou étalé, sans baisse permanente',
    'relief_extended': 'Avantage ou exonération étendus',
}

MEASURE_TITLES = {
    'cessation-common-return-ordinary-deadline': 'Déclarer une cessation dans le calendrier ordinaire',
    'cessation-common-return-single-channel': 'Supprimer l’avis fiscal de cessation séparé',
    'cessation-ir-ordinary-assessment': 'Mettre fin à l’imposition anticipée lors d’une cessation',
    'cfe-monthly-catchup-three-instalments': 'Étaler le rattrapage de CFE sur trois prélèvements',
    'contract-unique': 'Un contrat de travail unique, sans nouveau CDD',
    'crypto-global-option-revocable': 'Permettre de revenir sur le choix du barème pour les cryptomonnaies',
    'cvae-abolition-preserve-cfe-ceiling': 'Coordonner la suppression de la CVAE avec le plafonnement de CFE',
    'fiscal-reuse-already-held-evidence': 'Réutiliser les preuves déjà détenues par l’administration fiscale',
    'fiscal-transition-object-change-neutrality': 'Éviter une taxation déclenchée par le seul changement d’objet social',
    'fiscal-transition-opening-balance-common-filing': 'Retirer les dépôts fiscaux supplémentaires lors d’une transformation',
    'fiscal-transition-tax-values-preserved': 'Conserver les valeurs fiscales lors d’un changement de régime',
    'is-distribution-ordinaire': 'IS : conserver les bénéfices sans impôt ordinaire, taxer à la distribution',
    'monthly-option-current-year': 'Commencer la mensualisation sans attendre l’année suivante',
    'monthly-option-withdrawal-anytime': 'Sortir de la mensualisation à tout moment de l’année',
    'professional-transfer-receivables-no-three-month-limit': 'Assouplir le transfert des créances et dettes professionnelles',
    'property-company-conversion-neutrality-future': 'Étendre la neutralité fiscale des transformations de sociétés immobilières',
    'rcm-optional-support-reuse-evidence': 'Rendre facultatifs les supports fiscaux spéciaux quand les pièces ordinaires suffisent',
    'rcm-ordinary-records-no-extra-state': 'Réutiliser les documents comptables déjà conservés',
    'tax-account-secure-alternative-channel': 'Ne plus redemander les coordonnées bancaires déjà communiquées',
    'tax-payment-option-current-deadline': 'Choisir le paiement ou y renoncer jusqu’à son échéance',
    'tax-recovery-post-payment-fees-removed': 'Retirer les frais de poursuite après paiement intégral',
}
UNIT_LABELS = {
    'percent': 'pourcentage', 'euro': 'euros', 'legal_duty': 'obligation légale',
    'regime': 'régime', 'calendar_days': 'jours calendaires',
    'working_days': 'jours ouvrés', 'financing': 'financement', 'other': 'autre unité précisée dans le texte',
}


def _sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else (value or '').encode()).hexdigest()


def _assessment_sha(value):
    return _sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


def _key(row):
    return row['code_id'], row['source_id']


def _json(path):
    return json.loads(path.read_text())


def _exports(folder):
    coverage = _json(folder / 'coverage.json') if (folder / 'coverage.json').exists() else {}
    paths = [folder / (code['slug'] + '.json') for code in coverage.get('codes', [])]
    if not paths:
        paths = [p for p in sorted(folder.glob('*.json')) if not p.name.endswith('-structure.json')]
    records = []
    for path in paths:
        data = _json(path)
        if not isinstance(data, list):
            continue
        for article in data:
            if isinstance(article, dict) and {'code_id', 'source_id', 'source_xml'} <= article.keys():
                records.append(dict(article, slug=path.stem))
    return coverage, records


def _batches(folder):
    candidates = {}
    for path in sorted(folder.glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json', path.name):
            continue
        # Invalid canonical JSON is a local build defect, not an unassessed norm.
        rows = _json(path)
        if not isinstance(rows, list):
            raise ValueError('Article batch must be an array: ' + path.name)
        for row in rows:
            if isinstance(row, dict) and {'code_id', 'source_id'} <= row.keys():
                candidates.setdefault(_key(row), []).append(row)
    return candidates


def _well_formed(assessment, record):
    """Recheck anchors without inventing the prior-draft workflow history."""
    row = {'status': record.get('status', 'rewrite_draft'),
           'proposed_xml': record.get('proposed_xml'), 'substantive_impact': assessment}
    try:
        impact_rules.validate(row, record, required=True, enforce_workflow=False)
    except (ValueError, KeyError, TypeError, AttributeError):
        return False
    return True


def _dependencies_current(candidate, exported):
    guards = candidate.get('dependency_guards', [])
    if not isinstance(guards, list):
        return False
    for guard in guards:
        if not isinstance(guard, dict) or not {'code_id', 'source_id'} <= guard.keys():
            return False
        target = exported.get(_key(guard))
        if target is None:
            return False
        expected = {'source_sha256': target.get('source_sha256'),
                    'source_body_sha256': _sha(target.get('source_xml')),
                    'source_notes_sha256': _sha(target.get('source_notes_xml')),
                    'proposed_sha256': _sha(target.get('proposed_xml'))}
        if any(guard.get(k) != v for k, v in expected.items()):
            return False
    return True


def _checked(candidate, record, policy_sha, approved=False, exported=None):
    if approved:
        assessment = candidate.get('assessment', candidate.get('substantive_impact'))
        certificate = candidate.get('certificate', candidate.get('substantive_impact_certificate'))
        if not all(isinstance(candidate.get(k), str) and candidate[k].strip()
                   for k in ('reviewed_by', 'approved_at')):
            return None
    else:
        assessment = candidate.get('substantive_impact')
        certificate = candidate.get('substantive_impact_certificate')
        if candidate.get('status', 'rewrite_draft') != record.get('status', 'rewrite_draft'):
            return None
        if _sha(candidate.get('proposed_xml')) != _sha(record.get('proposed_xml')):
            return None
        if candidate.get('source_sha256') != record.get('source_sha256'):
            return None
    if not policy_sha or not isinstance(certificate, dict) or certificate.get('version') != VERSION:
        return None
    if not _dependencies_current(candidate, exported or {}):
        return None
    if not _well_formed(assessment, record):
        return None
    expected = {
        'source_sha256': record.get('source_sha256'),
        'source_notes_sha256': _sha(record.get('source_notes_xml')),
        'proposed_sha256': _sha(record.get('proposed_xml')),
        'assessment_sha256': _assessment_sha(assessment),
        'policy_sha256': policy_sha,
    }
    if not expected['source_sha256'] or any(certificate.get(k) != v for k, v in expected.items()):
        return None
    return assessment


def _approved(path):
    if not path.exists():
        return {}
    data = _json(path)
    if not isinstance(data, dict) or data.get('version') != VERSION or not isinstance(data.get('audits'), list):
        raise ValueError('Approved substantive audit manifest has an unsupported format')
    rows = {}
    for row in data['audits']:
        if not isinstance(row, dict) or not {'code_id', 'source_id'} <= row.keys():
            raise ValueError('Approved substantive audit is missing article identity')
        rows.setdefault(_key(row), []).append(row)
    return rows


def _unique(values):
    return {json.dumps(value, ensure_ascii=False, sort_keys=True): value for value in values}.values()


def _atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(content)
    temporary.replace(path)


def _render(report):
    esc = lambda value: html.escape(str(value), quote=True)
    coverage = report['coverage']
    chunks = ['''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Allègements proposés : effets documentés et limites</title>
<style>body{font:17px/1.65 system-ui,sans-serif;color:#173a32;background:#f5f1e8;margin:0}main{max-width:1160px;margin:auto;padding:32px 24px 80px}a{color:inherit}h1{font:clamp(36px,6vw,64px)/1.1 Georgia,serif}h2{margin-top:48px}p{max-width:85ch}.notice{padding:20px;background:#e2e8dd;border-left:4px solid #173a32}details{padding:18px 0;border-bottom:1px solid #a8b7aa}summary{cursor:pointer;font-weight:700}.table-wrap{overflow-x:auto}table{border-collapse:collapse;font-size:14px;min-width:850px;width:100%}th,td{text-align:left;vertical-align:top;padding:12px;border:1px solid #c5cec2}th{background:#e2e8dd}.evidence{font-size:14px;color:#456154}blockquote{margin:8px 0;padding-left:12px;border-left:2px solid #a8b7aa}li{margin:10px 0}</style></head><body><main>
<a href="/">← Le projet</a> · <a href="/corpus/">Lire les textes complets</a>
<h1>Quelles charges changeraient&nbsp;?</h1>
<p>Impôts, assiettes, obligations, délais : ce bilan présente les effets documentés des propositions de cette édition. Ces textes ne changent pas le droit en vigueur.</p>
<p class="notice"><strong>Économie nationale : inconnue. Réduction nette globale : non établie.</strong> Les effets de plusieurs articles ne s’additionnent pas automatiquement. Une obligation remplacée ou un financement transféré peut créer d’autres charges.</p>
<h2>Ce qui a été examiné</h2>''']
    chunks.append('<p>' + esc(coverage['current_approved_independent_reviews']) + ' articles ont reçu une contrelecture IA des textes complets. Le bilan reste partiel : ' + esc(coverage['unassessed_proposals']) + ' propositions restent à examiner.</p>')
    if coverage['current_worker_declarations']:
        chunks.append('<p>' + esc(coverage['current_worker_declarations']) + ' autres fiches de changements rédigées par les agents restent à contre-lire.</p>')
    chunks.append('<p>La concordance des textes et des empreintes vérifie l’intégrité de cette édition. Elle ne transforme pas les déclarations des agents en audit indépendant, en validation juridique ou en preuve d’économies. Les anciennes propositions sans appréciation restent non évaluées.</p>')
    chunks.append('<h2>Mesures et coordinations</h2><p>Les articles qui appliquent une même mesure sont regroupés. Les tableaux distinguent les allègements, les charges nouvelles et les règles nécessaires à leur application. Les montants et les démarches ne sont pas additionnés entre articles.</p>')
    if not report['measures']:
        chunks.append('<p>Aucun effet matériel ne dispose encore d’une appréciation actuelle vérifiée dans cette édition. Cela ne prouve ni absence d’effet ni absence d’allègement.</p>')
    for measure in report['measures']:
        effects = measure['effects']
        chunks.append('<details><summary>' + esc(MEASURE_TITLES.get(measure['measure_id'], effects[0]['description'])) + '</summary><div class="table-wrap"><table><thead><tr><th>Effet et article</th><th>Avant : taux et assiette, obligation ou délai</th><th>Après : taux et assiette, obligation ou délai</th><th>Personnes, conditions et transition</th><th>Remplacement ou charges nouvelles</th></tr></thead><tbody>')
        for effect in effects:
            article = effect['article']
            query = urlencode({'code': article['slug'], 'article': article['number']})
            label = 'Contrelecture IA approuvée' if effect['evidence_origin'] == 'approved_independent_review' else 'Déclaration de l’agent rédacteur'
            chunks.append('<tr><td>' + esc(KIND_LABELS[effect['kind']]) + '<br><a href="/corpus/?' + esc(query) + '">Article ' + esc(article['number']) + '</a><p class="evidence">' + esc(label) + '</p></td><td>' + esc(effect['before']) + '<blockquote>' + esc(effect['source_quote']) + '</blockquote></td><td>' + esc(effect['after']) + '<blockquote>' + esc(effect['proposed_quote']) + '</blockquote></td><td>' + esc(effect['affected_population']) + '<br>' + esc(effect['conditions_and_transition']) + '<br>Unité : ' + esc(UNIT_LABELS[effect['unit']]) + '</td><td>' + esc(effect['replacement_or_new_burdens']) + '</td></tr>')
        chunks.append('</tbody></table></div></details>')
    chunks.append('<h2>Analyse, charges nouvelles et limites par article</h2>')
    for article in report['articles']:
        assessment = article.get('assessment')
        if not assessment:
            continue
        chunks.append('<details><summary>Article ' + esc(article['number']) + ' — ' + esc(LABELS[assessment['classification']]) + '</summary><p>' + esc(assessment['assessment']) + '</p><p><strong>Charges nouvelles ou remplacées :</strong> ' + esc(assessment['new_burdens_review']) + '</p><p><strong>Limites :</strong> ' + esc(assessment['scope_limitations']) + '</p></details>')
    chunks.append('<h2>Méthode</h2><p>Rédaction seule, disposition maintenue et coordination ne sont pas comptées comme allègements supplémentaires. Les baisses de taux doivent être lues avec leurs assiettes, conditions, transitions et éventuels remplacements. Les transferts de financement sont présentés séparément d’une baisse de prélèvement. Ce bilan ne donne aucun score de progression vers une économie nationale.</p><p><a href="/corpus/substantive-impact.json">Données détaillées de cette édition</a></p></main></body></html>')
    return ''.join(chunks)


def build(out, exportroot, dbpath, batchesroot):
    """Read frozen raw exports; write only the report and its secondary page."""
    out, exportroot, dbpath, batchesroot = map(Path, (out, exportroot, dbpath, batchesroot))
    legal = dbpath.parent
    policy = legal / 'policy-coordinations.json'
    policy_bytes = policy.read_bytes() if policy.exists() else None
    policy_sha = _sha(policy_bytes) if policy_bytes is not None else None
    coverage, records = _exports(exportroot)
    candidates = _batches(batchesroot)
    approvals = _approved(legal / 'runtime/substantive-audits.json')
    occurrences = {}
    for record in records:
        occurrences[_key(record)] = occurrences.get(_key(record), 0) + 1
    exported = {_key(record): record for record in records if occurrences[_key(record)] == 1}
    articles = []
    for record in records:
        if not record.get('proposed_xml') and record.get('status') != 'retained_unchanged':
            continue
        item = {name: record.get(name) for name in ('code_id', 'source_id', 'number', 'slug', 'status')}
        item.update(evidence_status='unassessed', assessment=None)
        if occurrences[_key(record)] > 1:
            item['unassessed_reason'] = 'duplicate_export_identity'
        else:
            matching = []
            for row in _unique(candidates.get(_key(record), [])):
                assessment = _checked(row, record, policy_sha, exported=exported)
                if assessment is not None:
                    matching.append(assessment)
            if len(matching) == 1:
                item.update(evidence_status='worker_declaration', assessment=matching[0])
            else:
                item['unassessed_reason'] = 'missing_stale_or_ambiguous_assessment'
            approved = []
            for row in _unique(approvals.get(_key(record), [])):
                assessment = _checked(row, record, policy_sha, approved=True, exported=exported)
                if assessment is not None:
                    approved.append((assessment, row))
            if len(approved) == 1:
                assessment, row = approved[0]
                item.update(evidence_status='approved_independent_review', assessment=assessment,
                            reviewed_by=row['reviewed_by'], approved_at=row['approved_at'])
                item.pop('unassessed_reason', None)
        articles.append(item)
    # A policy edit during this read cannot silently certify a mixed edition.
    if (policy.read_bytes() if policy.exists() else None) != policy_bytes:
        for item in articles:
            item.update(evidence_status='unassessed', assessment=None,
                        unassessed_reason='policy_changed_during_build')
            item.pop('reviewed_by', None); item.pop('approved_at', None)
    measures = {}
    classifications = {category: 0 for category in sorted(impact_rules.CLASSES)}
    for article in articles:
        assessment = article.get('assessment')
        if assessment is None:
            continue
        classifications[assessment['classification']] += 1
        for effect in assessment['effects']:
            measure = measures.setdefault(effect['measure_id'], {'measure_id': effect['measure_id'], 'kinds': set(), 'effects': []})
            measure['kinds'].add(effect['kind'])
            measure['effects'].append(dict(effect, article={k: article[k] for k in ('code_id', 'source_id', 'number', 'slug')}, evidence_origin=article['evidence_status']))
    for measure in measures.values():
        measure['kinds'] = sorted(measure['kinds'])
    report = {
        'version': VERSION, 'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_snapshot': coverage.get('as_of'),
        'policy_sha256': policy_sha,
        'scope': 'Current exported proposals only; hash checks do not establish independent semantic review.',
        'national_savings': {'status': 'unknown', 'value': None, 'unit': 'EUR', 'reason': 'No supported national estimate is inferred from article counts, rates or agent declarations.'},
        'net_global_reduction': {'status': 'not_established', 'value': None},
        'aggregation': {'measure_ids_deduplicated': True, 'amounts_summed': False, 'article_counts_are_savings': False},
        'coverage': {
            'exported_articles': len(records),
            'exported_proposals': sum(bool(r.get('proposed_xml')) for r in records),
            'retained_sources': sum(r.get('status') == 'retained_unchanged' for r in records),
            'current_worker_declarations': sum(a['evidence_status'] == 'worker_declaration' for a in articles),
            'current_approved_independent_reviews': sum(a['evidence_status'] == 'approved_independent_review' for a in articles),
            'unassessed_proposals': sum(a['evidence_status'] == 'unassessed' and a['status'] != 'retained_unchanged' for a in articles),
            'unassessed_retained_sources': sum(a['evidence_status'] == 'unassessed' and a['status'] == 'retained_unchanged' for a in articles),
        },
        'classification_counts': classifications,
        'measures': [measures[key] for key in sorted(measures)], 'articles': articles,
        'semantic_review_by_jurist': False,
    }
    _atomic(out / 'substantive-impact.json', json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    _atomic(out.parent / 'bilan-allegements.html', _render(report))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('out', 'exportroot', 'dbpath', 'batchesroot'):
        parser.add_argument('--' + name, type=Path, required=True)
    arguments = parser.parse_args()
    build(arguments.out, arguments.exportroot, arguments.dbpath, arguments.batchesroot)
