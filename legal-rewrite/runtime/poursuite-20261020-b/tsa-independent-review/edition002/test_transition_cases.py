"""Illustrations arithmétiques bornées, sans simulation fiscale nationale."""
import unittest
from decimal import Decimal as D

def tax_credit_envelope(credits, old_paid, new_paid):
    total=old_paid+new_paid
    return D('0.0425')*credits*old_paid/total if total else D(0)

def annual_due(gross,abatement=D(0)):
    tax=max(D(0),gross-abatement)
    if tax<=1200:return D(0)
    return tax-D('0.75')*(2040-tax) if tax<=2040 else tax

class TransitionCases(unittest.TestCase):
    def test_old_half_of_common_budget(self):
        self.assertEqual(tax_credit_envelope(D(1000000),D(500000),D(500000)),D(21250))
    def test_uneven_payments_not_calendar_half(self):
        actual=tax_credit_envelope(D(1000000),D(300000),D(700000))
        self.assertEqual(actual,D(12750));self.assertNotEqual(actual,D(21250));self.assertNotEqual(actual,D(42500))
    def test_no_old_payments_or_no_payments(self):
        self.assertEqual(tax_credit_envelope(D(1000000),D(0),D(700000)),D(0))
        self.assertEqual(tax_credit_envelope(D(1000000),D(0),D(0)),D(0))
    def test_direct_and_common_disjoint(self):
        # 100k directly old + 600k common (one third old), 300k directly new.
        tax=D('0.0425')*D(100000)+tax_credit_envelope(D(600000),D(200000),D(400000))
        self.assertEqual(tax,D(12750))
    def test_full_annual_franchise(self):
        self.assertEqual(annual_due(D(1100)),D(0));self.assertEqual(annual_due(D(1200)),D(0))
    def test_full_annual_decote(self):
        self.assertEqual(annual_due(D(1600)),D(1270))
    def test_full_annual_association_abatement(self):
        self.assertEqual(annual_due(D(50000),D(24256)),D(25744))
        self.assertNotEqual(annual_due(D(50000),D(24256)),D(37872))
    def test_advance_only_one_imputation(self):
        advance,liability=D(5000),D(3500);refund=max(D(0),advance-liability)
        self.assertEqual(refund,D(1500));self.assertEqual(advance-refund,liability)
    def test_actual_residual_social_allocation_only(self):
        portions=[D(x)for x in ['.5835','.1074','.2477','.0614']]
        self.assertEqual(sum(portions),D(1));self.assertEqual(sum(D(1000)*x for x in portions),D(1000))
        self.assertEqual(sum(D(0)*x for x in portions),D(0))
    def test_peec_independent_of_tsa(self):
        self.assertEqual(D(1000000)*D('.0045'),D(4500))
        # Illustration of the autonomous rate, not a finding of employer eligibility.

if __name__=='__main__':unittest.main()
