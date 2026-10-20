"""Examples and boundary checks for edition002; no external calls or tax simulator."""
from decimal import Decimal as D
from pathlib import Path
import unittest,json
Z=D(0)
def reduction(groups,r,s):
    # tuples (B plafond base, A usual forfait IR preserving losses, T actual PS)
    gs=[min(a,max(Z,a+t-D('.2')*b))if b>0 else Z for b,a,t in groups]
    g=sum(gs,Z);cut=max(Z,g-D('.5')*max(Z,r-s));ratio=cut/g if g else Z
    return cut,[a-ratio*x for (b,a,t),x in zip(groups,gs)]
def settle(groups,r,s,foreign=None,other_ir=Z,nonrefundable=Z,refundable=Z,advance=Z,pfl_paid=Z,foreign_paid=Z):
    cut,irs=reduction(groups,r,s);foreign=foreign or [Z]*len(irs)
    # Ordinary convention here has a French-tax ceiling; never refunds foreign tax.
    ir=sum((max(Z,a-min(f,a))for a,f in zip(irs,foreign)),Z)+other_ir
    ir=max(Z,ir-nonrefundable)
    signed=ir-refundable-advance
    due=max(Z,signed);refund=max(Z,-signed)
    social=sum((t for b,a,t in groups),Z)
    return dict(cut=cut,ir_after_cap=irs,ir_before_refundable=ir,due=due,refund=refund,
                french_cash=pfl_paid+advance+due-refund+social,
                all_cash=pfl_paid+advance+due-refund+social+foreign_paid)
def ordinary(b):return b,b*D('.128'),b*D('.186')
class Numeric(unittest.TestCase):
    def test_zero_and_compensated_losses(self):
        self.assertEqual(reduction([(Z,Z,Z)],D(10000),D(29579))[0],0)
        self.assertEqual(reduction([ordinary(D(12000)-D(12000))],D(10000),D(29579))[0],0)
    def test_ordinary_full_cap_and_advance_once(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579),advance=D(1280))
        self.assertEqual(x['cut'],D(1140));self.assertEqual(x['refund'],D(1140));self.assertEqual(x['french_cash'],D(2000))
    def test_autonomous_pfl_refund_counterexample(self):
        # 5,000 PFU interest; 7,200 old insurance products, PFL 540 covered by
        # the couple's 9,200 abatement, hence autonomous refundable credit 540.
        x=settle([ordinary(D(5000))],D(30000),D(59158),refundable=D(540),advance=D(640),pfl_paid=D(540))
        self.assertEqual(x['cut'],D(570));self.assertEqual(x['ir_after_cap'],[D(70)])
        self.assertEqual(x['refund'],D(1110));self.assertEqual(x['french_cash'],D(1000))
        # Existing social tax on the old insurance is separate and unchanged.
        old_social=D(7200)*D('.172');self.assertEqual(x['french_cash']+old_social,D('2238.4'))
    def test_edition001_bug_including_its_final_bound(self):
        # U=F=100, J=640, min(1,F/U)=1; G=570 but final001 bound is F=100.
        old_g=min(D(640),max(Z,D(640)+D(930)-D(1000)))
        old_credit=min(D(100),old_g);self.assertEqual(old_credit,D(100))
        old_refund=D(640)-max(Z,D(100)-old_credit)
        self.assertEqual(D(540)+D(640)-old_refund+D(930),D(1470))
        # 470 more than002: its credit540 refund was only partly effective in001.
        self.assertEqual(D(1470)-D(1000),D(470))
    def test_autonomous_refund_without_any_pfu_base(self):
        x=settle([],D(10000),D(59158),refundable=D(540),pfl_paid=D(540));self.assertEqual(x['cut'],0);self.assertEqual(x['refund'],D(540));self.assertEqual(x['french_cash'],0)
    def test_full_foreign_credit_no_extra_foreign_refund(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579),foreign=[D(1000)],advance=D(1280),foreign_paid=D(1000))
        self.assertEqual(x['cut'],D(1140));self.assertEqual(x['ir_before_refundable'],0)
        self.assertEqual(x['refund'],D(1280));self.assertEqual(x['french_cash'],D(1860));self.assertEqual(x['all_cash'],D(2860))
    def test_partial_foreign_credit_with_actual_liability(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579),foreign=[D(50)],advance=D(1280),foreign_paid=D(50))
        self.assertEqual(x['ir_before_refundable'],D(90));self.assertEqual(x['refund'],D(1190));self.assertEqual(x['french_cash'],D(1950));self.assertEqual(x['all_cash'],D(2000))
    def test_other_refundable_credit_preserved_once(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579),refundable=D(2000),advance=D(1280))
        self.assertEqual(x['refund'],D(3140));self.assertEqual(x['french_cash'],0)
    def test_nonrefundable_general_credit_keeps_own_limit(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579),nonrefundable=D(2000),advance=D(1280))
        self.assertEqual(x['refund'],D(1280));self.assertEqual(x['french_cash'],D(1860))
    def test_loan_loss_distinct_bases(self):
        # Interest10,000/loss6,000: IR512, social1,860, plafond base10,000.
        x=settle([(D(10000),D(512),D(1860))],D(20000),D(29579),advance=D(1280))
        self.assertEqual(x['cut'],D(372));self.assertEqual(x['ir_after_cap'],[D(140)]);self.assertEqual(x['french_cash'],D(2000))
        self.assertGreater(x['french_cash']/D(4000),D('.2')) # no false20% of IR loss-net base
    def test_loan_loss_zero_ir_remains_more_favourable(self):
        x=settle([(D(5000),Z,D(930))],D(20000),D(29579),advance=D(640));self.assertEqual(x['cut'],0);self.assertEqual(x['french_cash'],D(930))
    def test_cpi_loss_excluded_socially_same_two_base_rule(self):
        x=settle([(D(10000),D(512),D(1860))],D(20000),D(29579));self.assertEqual(x['french_cash'],D(2000))
    def test_common_securities_losses_stay_net_in_both_bases(self):
        b=D(10000)-D(6000);x=settle([ordinary(b)],D(20000),D(29579));self.assertEqual(x['french_cash'],D(800))
    def test_fully_offset_common_gains(self):
        x=settle([ordinary(Z)],D(20000),D(29579));self.assertEqual(x['cut'],0);self.assertEqual(x['french_cash'],0)
    def test_insurance_abatement_not_recreated(self):
        for products,abat in [(D(5000),D(4600)),(D(10000),D(9200))]:
            b=products-abat;x=settle([(b,b*D('.075'),b*D('.172'))],D(20000),D(29579))
            self.assertEqual(x['french_cash'],b*D('.2'))
            self.assertEqual(products*D('.172')-b*D('.172'),abat*D('.172'))
    def test_gain_abatement_excludes_corresponding_social_fraction(self):
        # Qualifying500k fixed abatement;510k gain.1417IV reintegrates the
        # abatement into RFR:510k here, not20k. No claim of low-income eligibility.
        b=D(510000)-D(500000);x=settle([ordinary(b)],D(510000),D(29579))
        self.assertEqual(x['cut'],Z);self.assertEqual(x['french_cash'],D(3140))
        self.assertEqual(D(500000)*D('.186'),D(93000)) # outside new cap, unchanged
        self.assertEqual(x['french_cash']+D(93000),D(96140))
    def test_pea_exempt_not_recreated(self):
        x=settle([],D(20000),D(29579));self.assertEqual(x['cut'],0);self.assertEqual(x['french_cash'],0)
    def test_below_twenty_no_unused_room_between_groups(self):
        x=settle([ordinary(D(10000)),(D(10000),Z,D(750))],D(20000),D(29579));self.assertEqual(x['cut'],D(1140));self.assertEqual(x['french_cash'],D(2750))
    def test_barreme_global_option_can_remain_better(self):
        x=settle([ordinary(D(10000))],D(20000),D(29579));self.assertEqual(x['french_cash'],D(2000));self.assertLess(D(1860),x['french_cash'])
        self.assertEqual(D(10000)*D('.6')*D('.11'),D(660)) # barème40% abatement, never forfait
    def test_threshold_indexed_parts(self):
        for parts in [D(1),D('1.5'),D(2),D('2.25')]:
            s=parts*D(29579);self.assertEqual(reduction([ordinary(D(10000))],s,s)[0],D(1140));self.assertEqual(reduction([ordinary(D(10000))],s+D(1),s)[0],D('1139.5'))
    def test_smoothing_continuous_fixed_base(self):
        s=D(29579)
        for k in range(2500):
            c0=reduction([ordinary(D(10000))],s+D(k),s)[0];c1=reduction([ordinary(D(10000))],s+D(k+1),s)[0]
            self.assertGreaterEqual(c0-c1,Z);self.assertLessEqual(c0-c1,D('.5'))
        self.assertEqual(reduction([ordinary(D(10000))],s+D(2280),s)[0],0)
    def test_smoothing_one_new_ordinary_capital_euro(self):
        s=D(29579)
        for k in range(4000):
            b=D(10000+k);v0=settle([ordinary(b)],s+D(k),s)['french_cash'];v1=settle([ordinary(b+1)],s+D(k+1),s)['french_cash']
            self.assertGreaterEqual(v1-v0,Z);self.assertLessEqual(v1-v0,D('.7'))
    def test_smoothing_allocation_by_g(self):
        g=[ordinary(D(5000)),ordinary(D(10000))];cut,irs=reduction(g,D(29579)+D(100),D(29579))
        self.assertEqual(cut,D(1710)-D(50));self.assertAlmostEqual(sum(irs),D(1920)-cut)
    def test_no_rounded_intermediate_step(self):
        s=D('44368.5');self.assertEqual(reduction([ordinary(D(10000))],s+D('.01'),s)[0],D('1139.995'))
    def test_old_bad_smoothing_counterexamples(self):
        self.assertEqual(D(3140)-D(2000),D(1140));self.assertGreater(D('.2')+D(1),D(1))
    def test_synthetic_social_above_twenty_not_false_cap(self):
        # Not asserted to be an actual covered French regime. Explicit guard:
        # a reduction of IR alone cannot refund social tax exceeding the cap.
        x=settle([(D(4000),D(512),D(1860))],D(20000),D(29579));self.assertEqual(x['cut'],D(512));self.assertEqual(x['french_cash'],D(1860));self.assertGreater(x['french_cash'],D(800))

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Numeric))
    Path(__file__).with_name('numeric-results.json').write_text(json.dumps(dict(tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),network=False,coverage='Liquidation isolée avec réduction, crédits étrangers, crédits autonomes restituables, acomptes et solde de trésorerie ; pas simulateur fiscal complet'),ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
