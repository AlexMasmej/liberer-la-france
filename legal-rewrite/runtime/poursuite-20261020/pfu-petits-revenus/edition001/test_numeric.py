"""Isolated arithmetic examples of the proposed rule, not a household tax simulator."""
from decimal import Decimal as D
import unittest,json
from pathlib import Path

def calc(groups,r,s,usual_total=None,usual_remaining=None):
    # Each tuple is (actual taxable base, assigned French IR after specific credits,
    # social levies on that exact taxable fraction). Advances never enter here.
    u=sum((j for b,j,t in groups),D(0)) if usual_total is None else usual_total
    f=u if usual_remaining is None else max(D(0),usual_remaining)
    ratio=min(D(1),f/u)if u>0 else D(0)
    gs=[min(j*ratio,max(D(0),j*ratio+t-D('.2')*b))if b>0 else D(0)for b,j,t in groups]
    c=max(D(0),sum(gs,D(0))-D('.5')*max(D(0),r-s))
    return c,f-c

def ordinary(b):return b,b*D('.128'),b*D('.186')
class Numeric(unittest.TestCase):
    def test_zero_and_offset_losses(self):
        self.assertEqual(calc([(D(0),D(0),D(0))],D(0),D(29579))[0],0)
        # 12,000 gain with an imputable 12,000 loss: base zero, not proceeds.
        self.assertEqual(calc([ordinary(D(12000)-D(12000))],D(25000),D(29579))[0],0)
    def test_below_ceiling_no_credit(self):
        self.assertEqual(calc([(D(10000),D(0),D(1860))],D(10000),D(29579))[0],0)
    def test_full_ordinary_ceiling(self):
        c,ir=calc([ordinary(D(10000))],D(29579),D(29579));self.assertEqual(c,D(1140));self.assertEqual(ir+D(1860),D(2000))
    def test_indexed_quotient_threshold(self):
        # 29,579 is a current illustrative bracket boundary, never a fixed legal cap.
        for parts in [D(1),D('1.5'),D(2),D('2.25')]:
            s=parts*D(29579);self.assertEqual(calc([ordinary(D(10000))],s,s)[0],D(1140))
            self.assertEqual(calc([ordinary(D(10000))],s+D(1),s)[0],D('1139.5'))
    def test_no_cliff_and_tail_end(self):
        s=D(29579);g=[ordinary(D(10000))]
        for k in range(0,2500):
            c0=calc(g,s+D(k),s)[0];c1=calc(g,s+D(k+1),s)[0]
            self.assertGreaterEqual(c0-c1,0);self.assertLessEqual(c0-c1,D('.5'))
        self.assertEqual(calc(g,s+D(2280),s)[0],0)
    def test_new_capital_euro_changes_tax_at_most_point_seven(self):
        s=D(29579)
        for k in range(0,4000):
            b=D(10000+k);c0=calc([ordinary(b)],s+D(k),s)[0]
            c1=calc([ordinary(b+1)],s+D(k+1),s)[0]
            delta=D('.314')-(c1-c0)
            self.assertGreaterEqual(delta,0);self.assertLessEqual(delta,D('.7'))
    def test_counterexample_dry_threshold_and_rate_one(self):
        # A dry cap jumps 1,140 for one extra RFR euro. A one-euro withdrawal
        # plus the .20 tax on one new capital euro produces a marginal 1.20.
        self.assertEqual(D(3140)-D(2000),D(1140))
        self.assertEqual(D('.2')+D(1),D('1.2'))
    def test_barreme_favourable_and_dividend_abatement(self):
        # Explicit global barème option at zero IR is 18.6%, better than 20%.
        c,ir=calc([ordinary(D(10000))],D(10000),D(29579));self.assertEqual(ir+D(1860),D(2000));self.assertLess(D(1860),D(2000))
        # Under forfait no 40% dividend abatement: B=10,000, IR before cap=1,280.
        self.assertEqual(ordinary(D(10000))[1],D(1280))
        # 11% barème on eligible dividends: .60 base, before CSG deduction/décote.
        self.assertEqual(D(10000)*D('.6')*D('.11'),D(660))
    def test_insurance_abattement_single_and_couple(self):
        for gross,abat,expected in [(D(5000),D(4600),D('18.8')),(D(10000),D(9200),D('37.6'))]:
            b=gross-abat;ir=b*D('.075');covered_social=b*D('.172')
            c,left=calc([(b,ir,covered_social)],D(20000),D(29579));self.assertEqual(c,expected)
            self.assertEqual(left+covered_social,b*D('.2'))
            # Social levies on exempt products remain due and do not create credit.
            self.assertEqual(gross*D('.172')-covered_social,abat*D('.172'))
    def test_pea_exempt_no_base_no_credit(self):
        c,_=calc([(D(0),D(0),D(0))],D(20000),D(29579));self.assertEqual(c,0)
        # An exempt PEA still owing its own social levy is outside B and G.
        self.assertEqual(D(10000)*D('.186'),D(1860))
    def test_favourable_group_not_used_to_dilute_other_relief(self):
        groups=[ordinary(D(10000)),(D(10000),D(0),D(750))]
        self.assertEqual(calc(groups,D(20000),D(29579))[0],D(1140))
    def test_foreign_credit_no_foreign_tax_refund(self):
        c,left=calc([(D(10000),D(280),D(1860))],D(20000),D(29579));self.assertEqual(c,D(140));self.assertEqual(left,D(140))
        self.assertEqual(calc([(D(10000),D(0),D(1860))],D(20000),D(29579))[0],0)
    def test_nonassigned_advantages_before_cap(self):
        # Household IR=2,560, general credit=1,280, half IR relates to covered income.
        c,left=calc([ordinary(D(10000))],D(20000),D(29579),D(2560),D(1280))
        self.assertEqual(c,D(500));self.assertEqual(left,D(780))
        self.assertEqual(calc([ordinary(D(10000))],D(20000),D(29579),D(2560),D(0))[0],0)
    def test_advance_refunded_once_after_cap(self):
        c,ir=calc([ordinary(D(10000))],D(20000),D(29579));advance=D(1280)
        refund=max(D(0),advance-ir);self.assertEqual(refund,D(1140))
        self.assertEqual(advance-refund+D(1860),D(2000))
        c,ir=calc([(D(10000),D(280),D(1860))],D(20000),D(29579))
        self.assertEqual(advance-ir,D(1140));self.assertEqual(c,D(140))
        # 1,000 convention credit plus 140 new cap, not a second 1,000 refund.
        self.assertEqual(advance-ir,D(1000)+c)
    def test_transition_and_rounding_no_monthly_reset(self):
        s=D('44368.5');c,_=calc([ordinary(D(10000))],s+D('.01'),s)
        self.assertEqual(c,D('1139.995'))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Numeric)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    Path(__file__).with_name('numeric-results.json').write_text(json.dumps(dict(tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),network=False,scope='Arithmétique isolée, pas simulateur fiscal exhaustif ni preuve d’équilibre budgétaire'),ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
