def guarded_review_origins(prior_inheritance, previous):
    result = {r['label']: Path(r['folder']) for r in prior_inheritance['reviews']}
    for label, entry in previous.get('semantic_review_overrides', {}).items():
        if label not in result or label not in {'L1242-2', 'CVAE'}:
            raise ValueError('Unknown semantic review override')
        folder = Path(entry['folder'])
        manifest_name = 'semantic-review-manifest.json' if label == 'L1242-2' else 'artifact-manifest.json'
        if file_sha(folder / manifest_name) != entry['manifest_sha256']:
            raise ValueError('Semantic review override manifest changed')
        result[label] = folder
    return result
