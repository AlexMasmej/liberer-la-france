import json,hashlib,re,sqlite3,sys
from pathlib import Path
P=Path(__file__).parent
sys.path.insert(0,'legal-rewrite')
from run_exhaustive import validate_answer
rows=json.loads((P/'answer.json').read_text());sources=json.loads((P/'source.json').read_text());before=json.loads((P/'beforeimages.json').read_text());validate_answer(rows,sources)
c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True)
checks=[]
for row,source,prior in zip(rows,sources,before):
 assert row['source_id']==prior['source_id'];assert len(row['benefit_review'])>=100
 raw=c.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",(source['code_id'],source['source_id'])).fetchone()[0]
 assert hashlib.sha256(raw).hexdigest()==source['source_sha256']
 cur=c.execute('select proposed_xml from drafts where code_id=? and source_id=?',(source['code_id'],source['source_id'])).fetchone()
 current_sha=hashlib.sha256((cur[0]or'').encode()).hexdigest()if cur else None;assert current_sha==prior['current_beforeimage_sha256']
 checks.append({'number':row['number'],'source_sha_matches':True,'current_beforeimage_still_matches':True,'benefit_review_characters':len(row['benefit_review']),'proposed_sha256':hashlib.sha256(row['proposed_xml'].encode()).hexdigest(),'classification':row['change_type']})
by={a['number']:a['proposed_xml']for a in rows};d14=by['D912-14'];d15=by['D912-15'];ann=by["Annexes à l'article D912-15"]
assert 'chaque année' in d14 and 'ministre chargé de la sécurité sociale' in d14 and '31 août' in d14
assert 'conjointement' in d14 and 'distinctement identifiables' in d14 and 'confidentialité' in d14
assert 'pas soumis à un délai distinct' in d14 and 'deux mois' not in d14
assert 'Aucune ventilation statistique' in d15 and 'n’a pas à présenter' in d15.replace("'",'’')
for t in ['1°','2°','3°','autres prestations non directement contributives','coût effectif','part des primes','frais de gestion','frais d’acquisition','brutes de réassurance','exercice précédent']:
 assert t in d15.replace("'",'’'),t
for name in ['E1-0','E1-1','E2-1','E2-2','E2-3','E2-4','E3']:assert name in d15 and name in ann
assert 'ne sont plus imposés' in d15 and 'ne sont plus obligatoires' in ann
assert 'pas de refaire un rapport déjà transmis' in d14
assert 'ne dispensent pas de remettre un rapport annuel encore dû' in d14
assert 'pas de condition supplémentaire' in d15
comp=json.loads((P.parent/'d912-15-companion-candidate.json').read_text())
assert comp['documentary_recovery_complete']is True and comp['authenticated_jo_crosscheck_complete']is False
assert hashlib.sha256((P.parent/'d912-15-jo-copie.pdf').read_bytes()).hexdigest()==comp['documents'][0]['sha256']
for media in comp['media']:
 local=P.parent/('d912-table-'+str(media['page'])+'.png');assert hashlib.sha256(local.read_bytes()).hexdigest()==media['sha256']
out={'validate_answer':'passed','articles':checks,'manual_legislative_compatibility_review':{'L912_1_annual_report_to_minister_retained':True,'all_three_statutory_topics_retained':True,'R912_2_benefit_eligibility_and_branch_control_unmodified':True,'higher_level_exemptions_and_dispenses_unmodified':True,'formats_and_redundant_collection_removed_only_in_assigned_reporting_rules':True},'source_models_coverage':{'E1-0':'Page3 entière : catégories entreprises<20/20–<100/100–<500/≥500, effectifs, garanties, cellules noires conservées dans original ; tranches détaillées retirées de la proposition.','E1-1':'Page4 : garanties et cotisations forfaitaires/proportionnelles, tranchesA/B/C ; pas de format nouveau obligatoire.','E2-1_E2-2_E2-3_E2-4':'Page4 : bénéficiaires, parts%, montants cotisations et prestations€, quatre catégories de solidarité ; contenu substantiel connu conservé, état séparé supprimé.','E3':'Page4 : huit colonnes équilibre, cotisations/primes/prestations/provisions brutes de réassurance, ratio et frais, produits financiers ; faits utiles conservés sans tableau imposé.'},'transition_review':'New transmission rules apply immediately, including outstanding reports for older exercises; annual obligation still due; no rework of reports already filed, no mandatory reinstatement of old templates for corrections.','documentary_recovery_complete':True,'authenticated_jo_crosscheck_complete':False,'answer_sha256':hashlib.sha256((P/'answer.json').read_bytes()).hexdigest(),'registered':False,'database_modified':False,'attachments_modified':False,'published':False}
t=P/'checks.json.tmp';t.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');t.replace(P/'checks.json');print(json.dumps({'validate_answer':'passed','articles':3,'source_and_media_hashes_match':True,'answer_sha256':out['answer_sha256']},ensure_ascii=False))
