import fcntl,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import publish_snapshot as m

class CoalescingTests(unittest.TestCase):
 def test_busy_publication_does_not_validate_or_overwrite_owner_report(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);runtime=root/'runtime';runtime.mkdir();report=runtime/'publication.json';report.write_text('{}')
   with (runtime/'publication.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    with patch.object(m,'HERE',root),patch.object(m,'open_db') as db,patch.object(m,'register') as register:
     result=m.publish(True)
     self.assertEqual(result['status'],'publication_in_progress');self.assertTrue(result['publication_pending']);db.assert_not_called();register.assert_not_called()
    self.assertEqual(report.read_text(),'{}')
   with patch.object(m,'HERE',root),patch.object(m,'open_db',side_effect=RuntimeError('validation reached')):
    with self.assertRaisesRegex(RuntimeError,'validation reached'):m.publish(True)
if __name__=='__main__':unittest.main()
