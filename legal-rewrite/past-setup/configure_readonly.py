"""Keep the new account connection read-only until the import plan is approved."""
from pathlib import Path
import copy
import os
import re
import tempfile
import tomllib

path = Path.home()/'.codex/config.toml'
original = path.read_text()
before = tomllib.loads(original)
server = before['mcp_servers']['past']
assert server['url'] == 'https://app.past.dev/mcp'
tools = ['get_viewer', 'get_plan', 'get_credit_balance', 'get_project']
expected = copy.deepcopy(before)
expected['mcp_servers']['past'].update(enabled_tools=tools, default_tools_approval_mode='writes')
pattern = r'(?ms)^(\[mcp_servers\.past\]\s*\n)(.*?)(?=^\[|\Z)'
match = re.search(pattern, original)
assert match
body = match.group(2)
for name in ['enabled_tools', 'default_tools_approval_mode']:
    assert name not in server, 'Refusing to overwrite an existing tool policy'
body = body.rstrip()+'\nenabled_tools = ["get_viewer", "get_plan", "get_credit_balance", "get_project"]\ndefault_tools_approval_mode = "writes"\n\n'
updated = original[:match.start(2)]+body+original[match.end(2):]
assert tomllib.loads(updated) == expected
assert path.read_text() == original, 'Configuration changed concurrently'
with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, prefix='.past-setup-', delete=False) as temporary:
    temporary.write(updated)
    temporary_path = Path(temporary.name)
os.chmod(temporary_path, path.stat().st_mode & 0o777)
temporary_path.replace(path)
print('Past account connection limited to four read-only setup tools; no memory was uploaded.')
