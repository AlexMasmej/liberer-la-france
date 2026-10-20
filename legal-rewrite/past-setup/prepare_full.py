"""Prepare a reviewable full scope; quote its byte sizes without its texts.

This script has no ingestion route. The separate full-import approval is
required before these proposed documents or later revisions are ingested.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parent
LEGAL = ROOT.parent
sys.path.insert(0, str(LEGAL))
from past_memory import PastClient, save_json


def prepare():
    captured = datetime.datetime.now(datetime.timezone.utc).isoformat()
    policy_path = LEGAL/'policy-coordinations.json'
    policy = json.loads(policy_path.read_text())
    approved = json.loads((ROOT/'test-records.proposed.json').read_text())
    previous_policy_ids = {row['metadata']['source_section']: row['id'] for row in approved if row['audience']=='orientations'}
    previous_audit_ids = {row['metadata']['source_path']: row['id'] for row in approved if row['audience']=='coordinations'}
    records = []
    for section, value in policy.items():
        body = json.dumps(value, ensure_ascii=False, indent=2)
        records.append({
            'id': previous_policy_ids.get(section, 'legal-rewrite-policy-'+section),
            'label': 'Orientation de réécriture — '+section,
            'timestamp': captured, 'audience': 'orientations',
            'content': f'Orientation de réécriture : {section}\nInstantané capturé le {captured}. Cette date est celle de la capture, pas une date historique de décision.\n\n'+body,
            'metadata': {'kind': 'policy_snapshot', 'source_path': 'legal-rewrite/policy-coordinations.json', 'source_section': section, 'body_sha256': hashlib.sha256(body.encode()).hexdigest()}})
    paths = {row['metadata']['source_path'] for row in approved if row['audience']=='coordinations'}
    paths |= {'legal-rewrite/runtime/fiscal-net-20261019/estonian-evidence.md',
              'legal-rewrite/runtime/fiscal-net-20261019/french-aid-accounting.md'}
    for source in sorted(paths):
        path = LEGAL.parent/source
        assert path.resolve().is_relative_to(LEGAL.resolve()) and path.suffix == '.md'
        body = path.read_text()
        label = path.parent.name if path.name=='audit.md' else path.stem
        records.append({
            'id': previous_audit_ids.get(source, 'legal-rewrite-audit-'+label),
            'label': 'Audit de coordination — '+label,
            'timestamp': captured, 'audience': 'coordinations',
            'content': f'Audit : {label}\nInstantané capturé le {captured}. Cette date est celle de la capture, pas une date historique de rédaction.\n\n'+body,
            'metadata': {'kind': 'audit_snapshot', 'source_path': source, 'body_sha256': hashlib.sha256(body.encode()).hexdigest()}})
    assert len({row['id'] for row in records}) == len(records)
    assert all(len(row['content']) < 32000 for row in records)
    save_json(ROOT/'full-records.proposed.json', records)
    credits = sum(max(1, math.ceil(len(row['content'].encode())/350)) for row in records)
    proposal = {'captured_at': captured, 'status': 'proposed_not_ingested', 'data_points': len(records),
                'policy_documents': len(policy), 'audit_documents': len(paths),
                'content_bytes': sum(len(row['content'].encode()) for row in records),
                'ingestion_credits_local_estimate': credits,
                'records_sha256': hashlib.sha256((ROOT/'full-records.proposed.json').read_bytes()).hexdigest(),
                'future_sync_scope': 'Only revisions of these exact policy sections and seven audit files; no new sources without a scope update.',
                'full_import_approved': False, 'automatic_ingestion_approved': False}
    save_json(ROOT/'full-proposal.json', proposal)
    print(json.dumps(proposal, ensure_ascii=False))


def quote_sizes():
    assert json.loads((ROOT/'recall-verification.json').read_text())['passed']
    records = json.loads((ROOT/'full-records.proposed.json').read_text())
    # The documented items quote is based on UTF-8 bytes, rounded per item.
    # Equal-size placeholders price the exact cut without sending extra texts.
    sizes = [{'id': f'quote-size-{i}', 'content': 'x'*len(row['content'].encode()),
              'timestamp': row['timestamp'], 'audience': row['audience']}
             for i, row in enumerate(records)]
    client = PastClient()
    binding = json.loads((ROOT/'project-binding.json').read_text())
    usage = client.request('GET', '/api/v1/usage')
    assert usage['project']['slug'] == binding['project_slug']
    result = client.request('POST', '/api/v1/ingest/estimate', {'items': sizes, 'points': 'none'})
    assert result['dataPoints'] == len(records)
    assert result['bytes'] == sum(len(row['content'].encode()) for row in records)
    assert result['credits'] == sum(math.ceil(len(row['content'].encode())/350) for row in records)
    report = {'method': 'stateless API quote using equal-UTF8-byte placeholders per proposed document',
              'remaining_document_texts_sent': False, 'any_new_memory_ingested': False,
              'result': result}
    save_json(ROOT/'full-estimate.json', report)
    print(json.dumps({key:result[key] for key in ['dataPoints', 'bytes', 'credits', 'fits', 'balance']}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'quote-sizes'])
    action = parser.parse_args().action
    prepare() if action=='prepare' else quote_sizes()
