"""Resumable, bounded ten-record setup. No automatic or full import path."""
from pathlib import Path
from urllib.parse import quote
import argparse
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from past_memory import PastClient, PastError, save_json


def approved_records():
    payload = (ROOT/'test-records.proposed.json').read_bytes()
    approval = json.loads((ROOT/'approval.json').read_text())
    assert approval['test_import_approved'] is True
    assert hashlib.sha256(payload).hexdigest() == approval['records_sha256']
    records = json.loads(payload)
    assert len(records) == 10
    assert {r['audience'] for r in records} == {'orientations', 'coordinations'}
    for row in records:
        assert row['id'].startswith('legal-rewrite-test-')
        assert len(row['content']) < 32000
        assert datetime.datetime.fromisoformat(row['timestamp']).tzinfo is not None
        assert not re.search(r'past_[sm]k_|BEGIN (?:RSA |EC )?PRIVATE KEY|(?:API_KEY|GITHUB_TOKEN)\s*=\s*\S+', row['content'])
    return records


def ensure_binding(usage):
    binding = json.loads((ROOT/'project-binding.json').read_text())
    assert binding['project_slug'] == usage['project']['slug']
    assert binding['oauth_verified'] is True


def main(action):
    records = approved_records()
    plan = json.loads((ROOT/'plan.json').read_text())
    client = PastClient()
    if action == 'preflight':
        usage = client.request('GET', '/api/v1/usage')
        audiences = client.request('GET', '/api/v1/audiences')
        save_json(ROOT/'preflight.json', {'usage': usage, 'audiences': audiences})
        print(json.dumps({'project_slug': usage['project']['slug'], 'credits_left': usage['balance']['left'], 'audiences': [a['slug'] for a in audiences['audiences']]}))
        return
    usage = client.request('GET', '/api/v1/usage')
    ensure_binding(usage)
    if action == 'setup':
        scopes = []
        for slug, members in plan['audiences'].items():
            path = '/api/v1/audiences/'+slug
            try:
                audience = client.request('GET', path)
            except PastError as error:
                if error.status != 404:
                    raise
                audience = client.request('PUT', path, {'kind': 'fixed', 'name': 'Chantier juridique — '+slug, 'identities': members})
            assert audience['kind'] == 'fixed'
            assert set(audience['identities']) == set(members), 'Existing audience differs from approved plan; no replacement performed'
            scopes.append(audience)
        outsider = plan['outside_identity']
        try:
            client.request('GET', '/api/v1/identities/'+quote(outsider, safe=''))
        except PastError as error:
            if error.status != 404:
                raise
            client.request('PUT', '/api/v1/identities/'+quote(outsider, safe=''), {'traits': {}})
        readers = {}
        for identity in ['legal-rewrite', 'scope-test-orientations', 'scope-test-coordinations', outsider]:
            readers[identity] = client.request('GET', '/api/v1/identities/'+quote(identity, safe=''))
        assert set(readers['legal-rewrite']['audiences'])-{'project'} == set(plan['audiences'])
        assert set(readers['scope-test-orientations']['audiences'])-{'project'} == {'orientations'}
        assert set(readers['scope-test-coordinations']['audiences'])-{'project'} == {'coordinations'}
        assert not (set(readers[outsider]['audiences']) & set(plan['audiences']))
        save_json(ROOT/'access-verified.json', {'audiences': scopes, 'readers': readers})
        print('Both restricted audiences and all four reader scopes verified.')
    elif action == 'estimate':
        result = client.request('POST', '/api/v1/ingest/estimate', {'items': records, 'points': 'none'})
        assert result['dataPoints'] == 10 and result['fits']
        save_json(ROOT/'test-estimate.json', result)
        print(json.dumps({k:result[k] for k in ['dataPoints', 'bytes', 'credits', 'fits', 'balance']}))
    elif action == 'ingest':
        assert (ROOT/'access-verified.json').exists()
        estimate = json.loads((ROOT/'test-estimate.json').read_text())
        assert estimate['fits'] and estimate['dataPoints'] == 10
        if (ROOT/'test-ingestion.json').exists():
            print('Accepted ingestion already recorded; use poll. No duplicate send.')
            return
        digest = hashlib.sha256((ROOT/'test-records.proposed.json').read_bytes()).hexdigest()
        payload = {'items': records, 'idempotencyKey': 'legal-rewrite-test-'+digest[:32]}
        result = client.request('POST', '/api/v1/ingest/batch', payload)
        assert result['ingestionId']
        save_json(ROOT/'test-ingestion.json', result)
        print(json.dumps({'ingestionId': result['ingestionId'], 'status': result['status'], 'records': len(records)}))
    elif action in {'poll', 'explain'}:
        ingestion = json.loads((ROOT/'test-ingestion.json').read_text())
        result = client.request('GET', '/api/v1/ingest/'+quote(ingestion['ingestionId'], safe='')+('/explain' if action == 'explain' else ''))
        save_json(ROOT/('test-'+action+'.json'), result)
        print(json.dumps(result, ensure_ascii=False))
    elif action == 'recall':
        assert json.loads((ROOT/'test-poll.json').read_text())['status'] == 'completed'
        queries = plan['recall_queries']
        allowed = {r['id']: r['audience'] for r in records}
        timestamps = {r['id']: datetime.datetime.fromisoformat(r['timestamp']) for r in records}
        reports = []
        expected_by_query = [
            {'legal-rewrite-test-policy-preserved_benefits_2026_10_19', 'legal-rewrite-test-policy-cuts_and_reliefs_2026_10_19'},
            {'legal-rewrite-test-audit-cvae-independent-review', 'legal-rewrite-test-audit-cvae-cross-reform-review'},
            {'legal-rewrite-test-audit-logement-next-independent-review'}]
        for index, query in enumerate(queries):
            for reader in ['legal-rewrite', 'scope-test-orientations', 'scope-test-coordinations', plan['outside_identity']]:
                recall = client.request('POST', '/api/v1/recall', {'query': query, 'identity': reader, 'maxTokens': 4000, 'limit': 20})
                save_json(ROOT/f'recall-{index+1}-{reader}.json', recall)
                source_ids = set()
                for result in recall['results']:
                    for source in result.get('sources', []):
                        source_id = source['sourceId']
                        if source_id in allowed:
                            source_ids.add(source_id)
                            assert datetime.datetime.fromisoformat(source['occurredAt']) == timestamps[source_id]
                            if reader == 'scope-test-orientations':
                                assert allowed[source_id] == 'orientations'
                            if reader == 'scope-test-coordinations':
                                assert allowed[source_id] == 'coordinations'
                            assert reader != plan['outside_identity'], 'Scope isolation failed'
                if reader == 'legal-rewrite':
                    assert expected_by_query[index] & source_ids, 'Expected source not recalled'
                reports.append({'query': index+1, 'reader': reader, 'returned_documents': len(recall['results']), 'test_source_ids': sorted(source_ids), 'complete_response_characters': len(json.dumps(recall, ensure_ascii=False)), 'complete_response_tokens_chars_div_4': len(json.dumps(recall, ensure_ascii=False))/4, 'evidence_tokens_reported': recall.get('usedEvidenceTokens')})
        save_json(ROOT/'recall-verification.json', {'passed': True, 'queries': reports})
        print(json.dumps({'passed': True, 'recalls': len(reports), 'source_dates_verified': True, 'outside_reader_isolated': True}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['preflight', 'setup', 'estimate', 'ingest', 'poll', 'explain', 'recall'])
    args = parser.parse_args()
    try:
        main(args.action)
    except PastError as error:
        print(json.dumps({'error': error.code, 'http_status': error.status, 'request_id': error.request_id}), file=sys.stderr)
        raise SystemExit(1)
