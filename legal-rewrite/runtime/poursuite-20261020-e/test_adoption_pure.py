"""Execute only the pure guard transformation extracted by AST, never the helper."""
from pathlib import Path
import ast,copy,json,unittest
P=Path(__file__).resolve().parent
class Primitives:
 @staticmethod
 def key(x):return x['code_id']+'|'+x['source_id']
 @staticmethod
 def require(ok,msg):
  if not ok:raise ValueError(msg)
 @staticmethod
 def dependency_matches(a,b):return all(k in a and a[k]==b[k]for k in ['code_id','source_id','source_sha256','source_body_sha256','source_notes_sha256','proposed_sha256'])
tree=ast.parse((P/'adopt_reviewed.py').read_text());node=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='refresh_context_guards');ns={'copy':copy,'c':Primitives};exec(compile(ast.Module(body=[node],type_ignores=[]),'pure AST only','exec'),ns);run=ns['refresh_context_guards']
class Tests(unittest.TestCase):
 def setUp(self):
  self.g=dict(code_id='code',source_id='id',number='n',source_sha256='s',source_body_sha256='b',source_notes_sha256='n',proposed_sha256='old')
  self.a=dict(certificate={'opaque':'never rewritten'},assessment={'opaque':'same'},source_body_sha256='own',reviewed_by='prior',approved_at='prior',dependency_guards=[copy.deepcopy(self.g)])
  self.k='code|id';self.now=dict(self.g,proposed_sha256='new')
 def test_unchanged(self):
  out,delta=run(self.a,{self.k:self.g},{});self.assertEqual(out,self.a);self.assertEqual(delta,[])
 def test_approved_proposal_only(self):
  before=copy.deepcopy(self.a);out,delta=run(self.a,{self.k:self.now},{self.k:self.now});self.assertEqual(self.a,before);self.assertEqual(out['certificate'],self.a['certificate']);self.assertEqual(out['assessment'],self.a['assessment']);self.assertEqual(len(delta),1);self.assertEqual(out['dependency_guards'][0],self.now)
 def test_unknown_context_blocks(self):
  with self.assertRaises(ValueError):run(self.a,{self.k:self.now},{})
 def test_wrong_future_blocks(self):
  with self.assertRaises(ValueError):run(self.a,{self.k:self.now},{self.k:dict(self.now,proposed_sha256='wrong')})
 def test_raw_source_change_blocks(self):
  changed=dict(self.now,source_sha256='changed')
  with self.assertRaises(ValueError):run(self.a,{self.k:changed},{self.k:changed})
 def test_body_change_blocks(self):
  changed=dict(self.now,source_body_sha256='changed')
  with self.assertRaises(ValueError):run(self.a,{self.k:changed},{self.k:changed})
 def test_notes_change_blocks(self):
  changed=dict(self.now,source_notes_sha256='changed')
  with self.assertRaises(ValueError):run(self.a,{self.k:changed},{self.k:changed})
 def test_missing_old_pin_blocks(self):
  del self.a['dependency_guards'][0]['proposed_sha256']
  with self.assertRaises(ValueError):run(self.a,{self.k:self.now},{self.k:self.now})
 def test_duplicate_blocks(self):
  self.a['dependency_guards'].append(copy.deepcopy(self.g))
  with self.assertRaises(ValueError):run(self.a,{self.k:self.now},{self.k:self.now})
 def test_missing_actual_blocks(self):
  with self.assertRaises(KeyError):run(self.a,{}, {})
if __name__=='__main__':
 suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests);result=unittest.TextTestRunner(verbosity=1).run(suite)
 (P/'adoption-pure-tests.json').write_text(json.dumps(dict(tests=result.testsRun,success=result.wasSuccessful(),helper_imported=False,helper_main_executed=False,DB_access=False,active_mutation=False),indent=2)+'\n')
 if not result.wasSuccessful():raise SystemExit(1)
