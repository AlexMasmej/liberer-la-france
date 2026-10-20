import copy,hashlib,importlib.util,io,json,sqlite3,sys,unittest
from pathlib import Path
from decimal import Decimal as D
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));from ingest import source_notes
from run_exhaustive import validate_answer
p=ROOT/'runtime/poursuite-20261020/pfu-petits-revenus/edition002';out=Path(__file__).parent
H=lambda v:hashlib.sha256(v if isinstance(v,bytes) else (v or '').encode()).hexdigest()
def load(n):return json.loads((p/n).read_text())
def rows(n):x=load(n);return x if isinstance(x,list) else [x]
assert H((p/'source.json').read_bytes())=='b7e6514c7ae2ee03d28862af8517ec7d34d485183159a556796f91315978b53c'
assert H((p/'answer.json').read_bytes())=='ca756e125f49930e24302c7c38cd2590ce4f6fc4dcb21a0c0ad4e5f859bef349'
# The full thirteen earlier sources/notes/prior proposals remain identical to those already read.
for n in ['source-all.json','references.json']:
 assert (p/n).read_bytes()==(p.parent/'edition001'/n).read_bytes(),n
sources=rows('source-all.json')+rows('references.json')+rows('additional-reference.json')+rows('additional-reference-loss.json');expected=load('source.json');answer=load('answer.json');validate_answer(copy.deepcopy(answer),expected)
new=answer[0]['proposed_xml'];old=expected[0]['previous_draft']['proposed_xml'];start=new.index('<p>C. – 1°');end=new.index('<p>2. Par dérogation',start);assert new[:start]+new[end:]==old
c=sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN');checks=[]
for s in sources:
 k=(s['code_id'],s['source_id']);a=c.execute('select * from articles where code_id=? and id=?',k).fetchone();raw=c.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",k).fetchone()[0];notes=source_notes(c,*k);d=c.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();pr=s.get('previous_draft')
 g={'source_identity':a['source_sha256']==s['source_sha256'],'source_body':a['content_xml']==s['source_xml'],'source_notes':notes==s['source_notes_xml'],'source_document':H(raw)==(H(s['source_document_xml']) if 'source_document_xml' in s else s['source_sha256']),'previous_draft':d is None if pr is None else d is not None and d['source_sha256']==pr['source_sha256'] and d['proposed_xml']==pr['proposed_xml']}
 checks.append({'number':s['number'],'code_id':k[0],'source_id':k[1],'source_url':s.get('source_url','https://www.legifrance.gouv.fr/codes/article_lc/'+k[1]),'source_sha256':s['source_sha256'],'body_sha256':H(s['source_xml']),'notes_sha256':H(s['source_notes_xml']),'document_sha256':H(raw),'previous_proposed_sha256':H(pr['proposed_xml']) if pr else None,'guards':g,'all_match':all(g.values())})
c.rollback();c.close();assert all(x['all_match'] for x in checks)
spec=importlib.util.spec_from_file_location('frozen_pfu_tests002',p/'test_numeric.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);log=io.StringIO();test=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(m));(out/'numeric-tests-002.log').write_text(log.getvalue())
assert not test.failures and not test.errors
# Independent whole cash calculations use operative C (not the author's helper).
def literal(groups,R,S,foreign=None,autonomous_credit=D(0),advances=D(0),pfl_paid=D(0)):
 gs=[min(A,max(D(0),A+T-D('.2')*B)) if B>0 else D(0) for B,A,T in groups];g=sum(gs,D(0));reduction=max(D(0),g-D('.5')*max(D(0),R-S));pieces=[reduction*x/g if g else D(0) for x in gs];irs=[A-x for (B,A,T),x in zip(groups,pieces)];foreign=foreign or [D(0)]*len(groups);after=sum((max(D(0),x-min(x,f)) for x,f in zip(irs,foreign)),D(0));balance=after-autonomous_credit-advances;due=max(D(0),balance);refund=max(D(0),-balance);social=sum((x[2] for x in groups),D(0));return {'reduction':reduction,'ir_after_reduction':irs,'due':due,'refund':refund,'French_cash_excluding_uncovered_PS':pfl_paid+advances+due-refund+social}
examples=[]
for name,args in [
('PFL540_and_advance640',dict(groups=[(D(5000),D(640),D(930))],R=D(12200),S=D(59158),autonomous_credit=D(540),advances=D(640),pfl_paid=D(540))),
('loan_loss6000_preserved',dict(groups=[(D(10000),D(512),D(1860))],R=D(4000),S=D(29579),advances=D(1280))),
('ordinary_full_cap',dict(groups=[(D(10000),D(1280),D(1860))],R=D(20000),S=D(29579),advances=D(1280))),
('foreign_credit1000_ceiling_recalculated',dict(groups=[(D(10000),D(1280),D(1860))],R=D(20000),S=D(29579),foreign=[D(1000)],advances=D(1280))),
('insurance_covered_fraction_only',dict(groups=[(D(400),D(30),D('68.8'))],R=D(20000),S=D(29579))),
('fixed_abatement_realistic_RFR',dict(groups=[(D(10000),D(1280),D(1860))],R=D(510000),S=D(29579)))]:
 x=literal(**args);examples.append({'case':name,'result':x})
assert examples[0]['result']['refund']==D(1110) and examples[0]['result']['French_cash_excluding_uncovered_PS']==D(1000)
assert examples[1]['result']['reduction']==D(372) and examples[1]['result']['French_cash_excluding_uncovered_PS']==D(2000)
assert examples[2]['result']['French_cash_excluding_uncovered_PS']==D(2000)
assert examples[3]['result']['French_cash_excluding_uncovered_PS']==D(1860)
assert examples[4]['result']['French_cash_excluding_uncovered_PS']==D(80)
assert examples[5]['result']['reduction']==0
findings=[
{'id':'refundable-credit-restitution-distinct-pfl','status':'resolved_in_002','evidence':'C1 réduit A avant les crédits ; C5 maintient distinctement le crédit125-0A et ses restitutions, sans le déduire deA ni l’assimiler à une avance. Le contre-exemple donne D570,IR70,restitution1110 et soldeIR+PS1000 sur les intérêts ; ancienPFL rendu intégralement.'},
{'id':'numeric-tests-missing-final-bound','status':'resolved_by_architecture_change_and_full_cash_tests','evidence':'U/F et la borne contradictoire disparaissent entièrement. La réduction ne dépasse pasA par construction. Tests comprenant PFL déjà payé, crédit autonome, avances, impôt restant et restitution exécutés ; cycle complet vérifié indépendamment.'},
{'id':'divergent-social-and-ir-bases','status':'resolved_for_two_explicit_approved_losses','evidence':'B réintègre uniquement les pertes effectivement imputées enIR de125-00A et150-0BquinquiesIII2 quand L136-6 exclut leur imputation sociale ; A reste calculé après ces pertes. Les pertes communes restent nettes, les fractions exonérées/abattues horsB. L’exemple10k/6k donne plafond2k surB10k, pas20%duB_IR4k.'},
{'id':'fixed-abatement-test-RFR','status':'resolved_in_final_frozen_tests_and_note','evidence':'Le premier test algébrique utilisait RFR20k pour un gain510k/abattement500k, incompatible avec la réintégration1417IV. Le gel final a corrigé le test et la note en RFR510k et D0 ; la règle normativeC4 était et reste correcte. Vérification réaliste indépendante conforme.'}]
review={'edition':'002','verdict':'no_remaining_concrete_normative_defect_in_bounded_review','source_sha256':H((p/'source.json').read_bytes()),'answer_sha256':H((p/'answer.json').read_bytes()),'proposal_sha256':H(new),'whole_sources_notes_previous_proposals_read':15,'all_other_proposal_text_exactly_preserved':True,'five_guards_per_article':checks,'all_75_current_guards_match':True,'tests':{'frozen_author_tests':test.testsRun,'failures':len(test.failures),'errors':len(test.errors),'independent_literal_cash_examples':examples,'scope':'Arithmétique et conformité de la formule au texte, pas simulateur complet ni certification des sources étrangères.'},'findings':findings,'substantive_assessment':{
'qualifying_income_and_gains':'Champ1B seulement ; produit imposable ou gain net, jamais prix de cession ni capital remboursé. Les pertes et abattements légaux restent dansA ; B ne réintègre que les deux exceptions expresses de pertes non déductibles socialement.',
'preferential_regimes':'Taux7,5%, abattements4600/9200,40%dividendes au barème, PEA et autres exonérations, affiliations européennes et option globale rectifiable conservés ; pas de requalification en revenu taxable d’une fraction exonérée.',
'IR_and_PS':'Réduction du seulIR, PS effectivement dus surB, fractions abattues horsplafond et taux propres conservés. La CSG salariée6,6% et le minimuminternationalIS ne sont pas transposés. Aucun impôt étranger remboursable par ce mécanisme.',
'credits_and_advances':'Après réductionA, crédits existants selon leurchamp et limites. Crédit étranger plafonné à l’IR français recalculé : moins de crédit imputable peut accompagner moins d’IR sans hausse du net. Crédit autonome restituable et avances comptés chacun unefois.',
'eligibility':'RFR et parts annéeN, réintégrations1417IV et seuil197tranche11% dynamique. Effet de la réduction sur l’impôt, pas surRFR lui-même. NiN−1 niN−2 repris des dispositifs d’acompte.',
'phaseout':'D=max(0,ΣG−0,50max(0,R−S)), allocation proportionnelle àG sans accroître un impôt de groupe. Continuité de ce seul retrait, pas de garantie sur les autres taux marginaux du foyer.',
'no_increase':'Pour les mêmes faits et choix, chaqueG∈[0,A], puis chaqueA_prime∈[0,A] ; un groupe déjà plus favorable garde sonA. Les crédits/réductions suivent leurs règles, les crédits restituables fixes restent, et le crédit étranger limité au nouvelIR ne peut faire augmenter le net français. Aucun prélèvement nouveau.',
'classification':'mixed : baisse effective IR, une mesure dédupliquée, calcul de groupes/bases/lissage ajouté ; aucune preuve d’allègement administratif global ni de solde budgétaire.'},
'limits':['Pas de plafond universel pour toute taxe sur toute épargne : sommes horsB et impôts étrangers restent distincts.','SiT>20%B pour une autre situation ou un taux futur, une réduction limitée àA ne peut rembourser l’excédent social ; NOTE002 le reconnaît et le test synthétique le démontre. Les deux différences d’assiette légales identifiées sont coordonnées, sans certifier tout cas futur.','Les conventions fiscales entières et formulaires externes ne sont pas tous réécrits ; aucun corpus juridique extérieur déclaré achevé.','Historique desPS déjà acquittés d’assurance-vie : attribution et disponibilité des données à confirmer pour la mise en œuvre, aucune déclaration autonome inventée.','Le coût budgétaire/comportemental et de traitement administratif est inconnu. Le20%, le seuil et0,50 ne sont pas attribués à DavidLisnard.'],
'primary_web_checks':[{'url':'https://www.impots.gouv.fr/particulier/les-revenus-mobiliers','supports':'31,4%ordinaire2026 quand bases coïncident ; exceptions sociales17,2% distinctes.'},{'url':'https://www.impots.gouv.fr/particulier/lassurance-vie-et-le-pea-0','supports':'Assurance-vie : taux et abattements autonomes, régimes préférentiels etPS distincts.'},{'url':'https://bofip.impots.gouv.fr/bofip/3951-PGP.html/identifiant=BOI-RPPM-RCM-20-10-20-50-20140211','supports':'Crédit restituable sur PFL assurance-vie et différence capital/produit ; corroboration source125-0A entière.'}],
'canonical_mutation':False}
serialized=json.dumps(review,ensure_ascii=False,indent=2,default=str)+'\n';(out/'review-edition002.json').write_text(serialized);(out/'review.json').write_text(serialized)
files=[p/'source.json',p/'answer.json',p/'source-all.json',p/'references.json',p/'additional-reference.json',p/'additional-reference-loss.json',p/'test_numeric.py',p/'NOTE.md',out/'review-edition001.json',out/'review-edition002.json'];(out/'manifest.json').write_text(json.dumps({'reviewed_edition':'002','files':{str(f.relative_to(ROOT)):H(f.read_bytes()) for f in files},'canonical_mutation':False},ensure_ascii=False,indent=2)+'\n');print('review002 SHA',H(serialized));print('guards',len(checks)*5,'tests',test.testsRun)
