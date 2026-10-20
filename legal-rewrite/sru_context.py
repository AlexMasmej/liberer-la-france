"""Attach primary SRU text to candidate descendants; identity is not norm lineage."""
from pathlib import Path
import json


def contexts(folder):
    folder = Path(folder)
    original = folder/'original-articles.json'
    if not original.exists():
        return {}
    initial = {a['number']: a for a in json.loads(original.read_text())}
    matches = {}

    def add(code, identifier, number, evidence):
        number = str(number)
        if not code or not identifier or number not in initial:
            return
        entry = matches.setdefault((code, identifier), {})
        origin = entry.setdefault(number, {
            'original_article': number, 'source_url': initial[number]['source_url'],
            'initial_text': initial[number]['text'],
            'original_jo_table_missing': number == '52', 'documentary_evidence': []})
        if evidence not in origin['documentary_evidence']:
            origin['documentary_evidence'].append(evidence)

    path = folder/'habitat-inventory.json'
    if path.exists():
        for item in json.loads(path.read_text())['articles']:
            for target in item.get('current_review_targets', []):
                if target.get('current_slot_verified'):
                    add(target.get('code_id'), target.get('source_id'), item['sru_article'], {
                        'kind': 'current_slot_for_review',
                        'warning': 'Current article identity does not prove that its whole norm came from SRU.'})
    path = folder/'urbanisme-evidence/canonical-lineage.json'
    if path.exists():
        for item in json.loads(path.read_text())['records']:
            for family in item.get('canonical_targets', []):
                for target in family.get('current_descendants', []):
                    add(target.get('code_id'), target.get('source_id'), item['original_article'], {
                        'kind': 'documentary_concordance',
                        'historical_source_id': family.get('version_id'),
                        'historical_number': family.get('original_target_number'),
                        'source_url': family.get('source_url'),
                        'warning': 'Compare normative content; family links and reused numbers are not proof of surviving SRU rules.'})
    path = folder.parent/'sru-urbanisme-fiscalite/full-law-map.json'
    if path.exists():
        data = json.loads(path.read_text())
        records = data if isinstance(data, list) else data.get('entries', [])
        for item in records:
            for target in item.get('current_references', []):
                add(target.get('code_id', target.get('owner')), target.get('source_id'), item.get('sru_article', ''),
                    {'kind': 'supplementary_documentary_map', 'warning': 'Verify the exact surviving clause before repeal.'})
    return {key: [entries[n] for n in sorted(entries, key=int)] for key, entries in matches.items()}


def priority(job):
    return not any(article.get('sru_context') for article in job[2])
