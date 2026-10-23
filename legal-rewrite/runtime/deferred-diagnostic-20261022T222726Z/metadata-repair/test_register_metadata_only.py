"""Isolated scope/lock guards only: never invokes main or canonical writes."""
from pathlib import Path
import copy, fcntl, importlib.util, json, tempfile, unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('repair',HERE/'register_metadata_only.py')
repair=importlib.util.module_from_spec(spec);spec.loader.exec_module(repair)

class Scope(unittest.TestCase):
    def setUp(self):
        self.original=json.loads((HERE/'answer.original.json').read_text())
        self.candidate=json.loads((HERE/'answer.candidate.json').read_text())
    def test_one_space_only(self):self.assertTrue(repair.assert_patch_scope(self.original,self.candidate))
    def reject(self,mutate):
        mutant=copy.deepcopy(self.candidate);mutate(mutant)
        with self.assertRaises(ValueError):repair.assert_patch_scope(self.original,mutant)
    def test_other_normative_text(self):self.reject(lambda a:a[0].update(proposed_xml='<p>Inventé.</p>'))
    def test_other_reason(self):self.reject(lambda a:a[0].update(reason='Autre motif'))
    def test_other_review(self):self.reject(lambda a:a[0].update(review_notes='Autre note'))
    def test_other_metadata(self):self.reject(lambda a:a[0].update(fake=True))
    def test_source_hash(self):self.reject(lambda a:a[0].update(source_sha256='0'*64))
    def test_number(self):self.reject(lambda a:a[0].update(number='autre'))
    def test_order(self):self.reject(lambda a:a.reverse())
    def test_missing_article(self):self.reject(lambda a:a.pop())
    def test_extra_article(self):self.reject(lambda a:a.append(copy.deepcopy(a[0])))
    def test_original_without_correction(self):
        with self.assertRaises(ValueError):repair.assert_patch_scope(self.original,self.original)
    def test_two_spaces_rejected(self):
        def alter(a):
            for r in a:
                if r['source_id']==repair.KEY[1]:r['substantive_impact']['effects'][0]['proposed_quote']=repair.AFTER.replace('; 3°',';  3°')
        self.reject(alter)
    def test_other_effect_field(self):
        def alter(a):
            for r in a:
                if r['source_id']==repair.KEY[1]:r['substantive_impact']['effects'][0]['description']+=' autre'
        self.reject(alter)

class Locks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for name in repair.LOCKS:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.touch()
    def tearDown(self):self.temp.cleanup()
    def test_all_locks_held_and_inventory_twice(self):
        calls=[]
        def idle():calls.append(True);return {'idle':True}
        with repair.drained_locks(self.root,idle):
            for name in repair.LOCKS:
                with (self.root/name).open('a') as stream:
                    with self.assertRaises(BlockingIOError):fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        self.assertEqual(len(calls),2)
    def test_each_busy_lock_refuses(self):
        for name in repair.LOCKS:
            with self.subTest(lock=name),(self.root/name).open('a') as stream:
                fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
                with self.assertRaises(ValueError):
                    with repair.drained_locks(self.root,lambda:{'idle':True}):self.fail('Lock bypassed')
    def test_unknown_inventory_refuses(self):
        def unknown():raise TimeoutError('Inventory unavailable')
        with self.assertRaises(TimeoutError):
            with repair.drained_locks(self.root,unknown):self.fail('Unknown treated as empty')
    def test_busy_lock_release(self):
        with (self.root/repair.LOCKS[2]).open('a') as occupied:
            fcntl.flock(occupied,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with self.assertRaises(ValueError):
                with repair.drained_locks(self.root,lambda:{}):pass
        with repair.drained_locks(self.root,lambda:{'idle':True}):pass

class Inventory(unittest.TestCase):
    def test_coordinator_present(self):
        row={'pid':123,'ppid':1,'args':['python3',str(repair.HERE/'run_exhaustive.py')]}
        with self.assertRaises(ValueError):repair.assert_idle_inventory([row])
    def test_native_worker_present(self):
        row={'pid':123,'ppid':1,'args':['codex','exec','--output-last-message',str(repair.HERE/'runtime/exhaustive/jobs/fake/result.json')]}
        with self.assertRaises(ValueError):repair.assert_idle_inventory([row])
    def test_invalid_inventory(self):
        with self.assertRaises(ValueError):repair.assert_idle_inventory({'unknown':True})
    def test_explicit_fixture_empty(self):self.assertTrue(repair.assert_idle_inventory([])['inventory_observed'])

class Owners(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.old=repair.HERE;repair.HERE=Path(self.temp.name)
        (repair.HERE/'batches/test').mkdir(parents=True)
        (repair.HERE/'registered-batches.json').write_text('{}')
        self.batch=repair.HERE/'batches/test/00002.json';self.keys={repair.KEY}
    def tearDown(self):repair.HERE=self.old;self.temp.cleanup()
    def test_no_owner(self):self.assertEqual(repair.assert_no_owners(self.keys,self.batch),{})
    def test_existing_owner(self):
        (repair.HERE/'batches/test/00001.json').write_text(json.dumps([{'code_id':repair.KEY[0],'source_id':repair.KEY[1]}]))
        with self.assertRaises(ValueError):repair.assert_no_owners(self.keys,self.batch)
    def test_existing_registry_owner(self):
        (repair.HERE/'registered-batches.json').write_text(json.dumps({'|'.join(repair.KEY):{}}))
        with self.assertRaises(ValueError):repair.assert_no_owners(self.keys,self.batch)
    def test_existing_batch_path(self):
        self.batch.write_text('[]')
        with self.assertRaises(ValueError):repair.assert_no_owners(self.keys,self.batch)

if __name__=='__main__':unittest.main(verbosity=2)
