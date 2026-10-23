from pathlib import Path
import tempfile,unittest,hashlib
from unittest.mock import patch
import interpreter_guard as g

class Interpreter(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='interpreter-binding-offline-');self.addCleanup(self.temp.cleanup)
        self.wrapper=Path(self.temp.name).resolve()/'launcher';self.image=Path(self.temp.name).resolve()/'Python'
        self.wrapper.write_bytes(b'fixture launcher bytes');self.image.write_bytes(b'fixture loaded image')
        for name,value in [('WRAPPER',self.wrapper),('IMAGE',self.image),('WRAPPER_SHA',g.sha(self.wrapper.read_bytes())),('IMAGE_SHA',g.sha(self.image.read_bytes()))]:
            p=patch.object(g,name,value);p.start();self.addCleanup(p.stop)
        self.loaded=patch.object(g,'loaded_images',return_value='p42\nftxt\nn'+str(self.image)+'\n');self.loaded.start();self.addCleanup(self.loaded.stop)
        self.tail=['-u','/fixture/project/run_exhaustive.py','--workers','8','--recover-new-before-reviews']
    def verify(self,**kw):
        return g.bind_interpreter(kw.get('observed',str(self.image)),kw.get('requested',str(self.wrapper)),kw.get('actual',self.tail),kw.get('requested_tail',self.tail),kw.get('pid',42))
    def test_exact_physical_pair_and_loaded_image_pass(self):
        result=self.verify();self.assertEqual(result['actual_pid'],42);self.assertTrue(result['argument_tail_identical'])
    def test_request_symlink_is_resolved_to_exact_pinned_launcher(self):
        link=Path(self.temp.name)/'python3';link.symlink_to(self.wrapper);self.verify(requested=str(link))
    def test_changed_tail_or_process_id_blocks(self):
        for pid in (0,True,None):
            with self.subTest(pid=pid),self.assertRaises(ValueError):self.verify(pid=pid)
        with self.assertRaises(ValueError):self.verify(actual=self.tail+['--different'])
    def test_unreviewed_interpreter_path_blocks_even_with_familiar_name(self):
        unknown=Path(self.temp.name)/'python3.14';unknown.write_bytes(self.image.read_bytes())
        with self.assertRaises(ValueError):self.verify(observed=str(unknown))
    def test_launcher_or_image_change_blocks(self):
        self.wrapper.write_bytes(b'changed')
        with self.assertRaises(ValueError):self.verify()
        self.wrapper.write_bytes(b'fixture launcher bytes');self.image.write_bytes(b'changed')
        with self.assertRaises(ValueError):self.verify()
    def test_lsof_must_identify_this_actual_loaded_image(self):
        with patch.object(g,'loaded_images',return_value='p42\nftxt\nn/unrelated/Python\n'),self.assertRaises(ValueError):self.verify()
    def test_image_change_during_observation_blocks(self):
        def observe(pid):
            self.image.write_bytes(b'intervening image');return 'p42\nftxt\nn'+str(self.image)+'\n'
        with patch.object(g,'loaded_images',side_effect=observe),self.assertRaises(ValueError):self.verify()
    def test_unknown_lsof_is_not_an_empty_success(self):
        self.loaded.stop()
        class Result:returncode=1;stdout=''
        with patch.object(g.subprocess,'run',return_value=Result()),self.assertRaises(ValueError):g.loaded_images(42)
        Result.returncode=0;Result.stdout='p99\nftxt\nn'+str(self.image)+'\n'
        with patch.object(g.subprocess,'run',return_value=Result()),self.assertRaises(ValueError):g.loaded_images(42)

if __name__=='__main__':unittest.main()
