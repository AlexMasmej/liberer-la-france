import json,os,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import publish_snapshot as m

class RuntimeTests(unittest.TestCase):
 def test_runtime_changes_only_child_path_preserving_environment(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);folder=root/'lts';folder.mkdir();node=folder/'node';node.write_text('fixture');node.chmod(0o700)
   (root/'publication-runtime.json').write_text(json.dumps({'node_bin_directory':str(folder)}))
   with patch.object(m,'HERE',root),patch.dict(os.environ,{'PATH':'/existing','EXAMPLE_PRESERVED':'yes'},clear=True):
    result=m.deployment_environment()
    self.assertEqual(result['PATH'],str(folder)+os.pathsep+'/existing')
    self.assertEqual(result['EXAMPLE_PRESERVED'],'yes');self.assertEqual(os.environ['PATH'],'/existing')
    self.assertNotIn('NODE_TLS_REJECT_UNAUTHORIZED',result)
 def test_missing_runtime_fails_closed(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);(root/'publication-runtime.json').write_text(json.dumps({'node_bin_directory':str(root/'absent')}))
   with patch.object(m,'HERE',root),patch.dict(os.environ,{},clear=True):
    with self.assertRaisesRegex(ValueError,'unavailable'):m.deployment_environment()
 def test_tls_disable_is_rejected(self):
  with patch.dict(os.environ,{'NODE_TLS_REJECT_UNAUTHORIZED':'0'}):
   with self.assertRaisesRegex(ValueError,'TLS certificate'):m.deployment_environment()
if __name__=='__main__':unittest.main()
