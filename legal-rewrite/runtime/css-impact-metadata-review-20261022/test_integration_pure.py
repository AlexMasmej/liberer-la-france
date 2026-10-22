"""Pure guard/merge checks. No active imports, DB connection or commit call."""
from pathlib import Path
import ast
import copy
import json
import runpy

OUT = Path(__file__).resolve().parent
ns = runpy.run_path(str(OUT / 'integrate_guarded.py'), run_name='_pure_test')
changes, merge, Refusal = ns['changes'], ns['merge_resolution'], ns['Refusal']
original = json.loads((OUT / 'original-job/answer.json').read_text())
candidate = json.loads((OUT / 'answer.metadata-only.json').read_text())
assert changes(original, candidate) == [('/2/substantive_impact/classification', 'financing_transfer', 'mixed')]
mutated = copy.deepcopy(candidate)
mutated[2]['proposed_xml'] += '<p>Change interdite.</p>'
assert len(changes(original, mutated)) == 2
old = [{'job': 'unrelated', 'resolution': '/preserved', 'accepted_articles': 24}]
entry = {'job': 'this-job', 'resolution': '/proof', 'accepted_articles': 12}
merged = merge(copy.deepcopy(old), entry)
assert merged == old + [entry] and old == [{'job': 'unrelated', 'resolution': '/preserved', 'accepted_articles': 24}]
assert merge(merged, entry) == merged
for bad in (merged + [entry], old + [dict(entry, resolution='/conflict')]):
    try:
        merge(bad, entry)
        raise AssertionError('Conflict accepted')
    except Refusal:
        pass
module = ast.parse((OUT / 'integrate_guarded.py').read_text())
commit_calls = [n for n in ast.walk(module) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'commit']
assert len(commit_calls) == 1
assert all(not (isinstance(n, ast.Import) and any(a.name in ('subprocess', 'signal') for a in n.names)) for n in ast.walk(module))
assert all(not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ('execute', 'executescript') and n.args and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str) and n.args[0].value.lstrip().upper().startswith(('UPDATE ', 'INSERT ', 'DELETE ', 'CREATE '))) for n in ast.walk(module))
print(json.dumps({'passed': True, 'single_approved_leaf': True, 'normative_mutation_detected': True,
                  'ledger_preserves_unrelated_entries': True, 'ledger_idempotent': True,
                  'ledger_conflicts_and_duplicates_refused': True, 'single_commit_call_site': True,
                  'no_process_operations_or_direct_DB_mutations': True,
                  'commit_called': False, 'apply_executed': False}, indent=2))
