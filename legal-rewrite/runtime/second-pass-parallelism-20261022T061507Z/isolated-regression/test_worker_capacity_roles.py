from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

import worker_capacity as capacity


class RoleCapacity(unittest.TestCase):
    def setUp(self):
        self.temporary=TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.runtime=Path(self.temporary.name)
        self.plan={'capacity':8,'current_workers':8,'role_limits':{'new':6,'review':2}}
        self.write('parallelism-plan.json',self.plan)

    def write(self,name,value):
        (self.runtime/name).write_text(json.dumps(value))

    def test_eight_requires_explicit_separate_roles(self):
        self.assertEqual(capacity.settings(self.runtime),self.plan)
        for bad in [{}, {'role_limits':None}, {'role_limits':{'new':8,'review':0}},
                    {'role_limits':{'new':6,'review':True}}, {'role_limits':{'new':6}},
                    {'role_limits':{'new':6,'review':2,'other':0}},
                    {'role_limits':{'new':6,'review':1}}]:
            with self.subTest(bad=bad):
                data=dict(self.plan)
                if not bad:data.pop('role_limits')
                else:data.update(bad)
                self.write('parallelism-plan.json',data)
                with self.assertRaises(ValueError):capacity.settings(self.runtime)

    def test_six_legacy_and_three_default_unchanged(self):
        self.write('parallelism-plan.json',{'capacity':6,'current_workers':4})
        self.assertEqual(capacity.slot_document(self.runtime,['manual']),{'workers':3})
        self.assertEqual(capacity.admission_limits(self.runtime,6),{'workers':6,'role_limits':None})
        (self.runtime/'parallelism-plan.json').unlink()
        self.assertEqual(capacity.settings(self.runtime),{'capacity':3,'current_workers':3})

    def test_manual_reservations_preserve_both_review_places(self):
        self.assertEqual(capacity.slot_document(self.runtime,['a','b']),
                         {'workers':6,'role_limits':{'new':4,'review':2}})
        with self.assertRaises(ValueError):capacity.slot_document(self.runtime,list(range(7)))

    def test_one_atomic_file_pauses_reviews_and_keeps_six_new(self):
        self.write('worker-limit.json',{'workers':6,'role_limits':{'new':6,'review':0}})
        self.assertEqual(capacity.admission_limits(self.runtime,8),
                         {'workers':6,'role_limits':{'new':6,'review':0}})

    def test_effective_counts_cannot_exceed_authorized_roles_or_total(self):
        invalid=[{'workers':8,'role_limits':{'new':7,'review':1}},
                 {'workers':8,'role_limits':{'new':5,'review':3}},
                 {'workers':6,'role_limits':{'new':6,'review':2}},
                 {'workers':9,'role_limits':{'new':6,'review':2}},
                 {'workers':True,'role_limits':{'new':6,'review':2}},
                 {'workers':8,'role_limits':{'new':6,'review':False}}]
        for document in invalid:
            with self.subTest(document=document):
                self.write('worker-limit.json',document)
                with self.assertRaises(ValueError):capacity.admission_limits(self.runtime,8)


if __name__=='__main__':unittest.main()
