import json,re,pathlib,sqlite3,hashlib,sys,html
P=pathlib.Path(__file__).parent
sys.path.insert(0,'legal-rewrite')
from register_batches import text,authorized_reduction,references
from ingest import source_notes
rows=json.loads((P/'candidates.json').read_text());source=json.loads((P/'source.json').read_text());by={a['number']:a for a in source}
report=json.loads((P/'report.json').read_text())
extra={
'L302-1':"Programmation autonome du logement, diagnostic, observatoires, objectifs d'offre et programme d'actions par commune. Aucun taux20/25 %, rattrapage, inventaire SRU ou carence. Les ajouts antérieurs de densification et leurs garanties sont conservés. La réserve générale sur les obligations de logement social vise les obligations autonomes subsistantes ; elle ne peut ressusciter celles abolies par L302-5V et la coordination L445-1.",
'L302-3':"Bilan annuel de réalisation du PLH et transmissions à trois et six ans. Objectifs issus de la programmation autonome, sans calcul ni sanction du quota SRU. Le second alinéa reste à sa place pour L301-5-1.",
'L302-4-1':"Applicabilité du PLH aux communes isolées de plus de20 000 habitants, sans quota SRU. Les huit paragraphes du I proposé de L302-4 sont identiques à la proposition antérieure : aucune cible n'a été déplacée. Réserve préexistante : son quatrième alinéa est le c), tandis que l'extension de périmètre EPCI est au cinquième. Aucun changement silencieux d'intention n'est présumé ; aucune ambiguïté nouvelle n'est créée.",
'R631-20':"Agrément de résidence hôtelière nouvelle : conditions techniques, accessibilité, décence et incendie. La référence à l'article187 de la loi2000-1208 identifie le fondement du décret de décence2002-120, sans rapport avec le quota de l'article55. Article intégralement lu, aucun candidat nouveau compté.",
'R631-21':"Agrément de résidence hôtelière rénovée : technique, décence, exceptions sanitaires encadrées et incendie. La référence à l'article187 de la loi2000-1208 n'institue aucun quota communal. Article intégralement lu, aucun candidat nouveau compté.",
'R823-2':"Demande et justificatifs des aides personnelles, attestation de décence et DPE, titre de séjour. L'article187 SRU fonde le décret de décence ; aucune condition20/25 % ou carence. Note historique d'entrée au1erjanvier2023 lue. Aucun candidat nouveau compté.",
'R863-4':"Adaptations des aides personnelles à Saint-Pierre-et-Miquelon : période de ressources, revenus/déductions, patrimoine et décence. L'article187 SRU ne renvoie pas au quota. Les neuf subdivisions et la note source sur les pensions prenant effet au1erseptembre2023 ont été lues, sans leur donner une autre portée. Aucun candidat nouveau compté."
}
report=[a for a in report if a['number'] not in extra and a['number']!='L431-1']
for n,why in extra.items():report.append({'number':n,'treatment':'retained_no_new_draft','reason':why,'source_id':by[n]['source_id']})
# L431-1 was a title-only false positive in the reference inventory.
pub=json.load(open('sites/liberer-la-retraite/dist/corpus/construction-habitation.json'))
a=next(a for a in pub if a['number']=='L431-1')
db=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True)
raw=db.execute('select content_xml,source_sha256 from articles where code_id=? and id=?',(a['code_id'],a['source_id'])).fetchone()
(P/'additional-evidence.json').write_text(json.dumps([{'code_id':a['code_id'],'source_id':a['source_id'],'number':a['number'],'source_xml':raw[0],'source_sha256':raw[1],'source_notes_xml':source_notes(db,a['code_id'],a['source_id']),'previous_draft':None}],ensure_ascii=False,indent=2)+'\n')
report.append({'number':'L431-1','source_id':a['source_id'],'treatment':'retained_no_new_draft','reason':"Garanties hypothécaires et subrogations des prêts sociaux. La loi2000-1208 est citée seulement comme date d'arrêt des nouvelles hypothèques au fonds de garantie et pour les anciennes créances de la CDC. Aucune condition de quota ; garanties des aides et actifs conservées. Source canonique entière lue avec code_id+source_id, pas la version ancienne trouvée par simple numéro."})
checks=[];fail=[]
for a in rows:
 key=a['code_id'],a['source_id'];s=by[a['number']]
 raw=db.execute('select content_xml,source_sha256,number from articles where code_id=? and id=?',key).fetchone()
 prev=db.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',key).fetchone()
 expected=s.get('previous_draft');previous_ok=(not prev and not expected) or bool(prev and expected and prev[0]==expected['source_sha256'] and hashlib.sha256((prev[1] or '').encode()).hexdigest()==expected['proposed_sha256'])
 source_ok=(raw[0]==s['source_xml'] and raw[1]==a['source_sha256'] and raw[2]==a['number'] and hashlib.sha256(raw[0].encode()).hexdigest()==s['source_content_sha256'])
 proposed,tables=text(a['proposed_xml']);original,ot=text(s['source_xml'],False)
 clean=proposed!=original and not re.search(r'TODO|<placeholder>|\[\s*(?:…|\.\.\.|à compléter|texte inchangé)\s*\]',proposed,re.I)
 reduced=authorized_reduction(a)
 before=(expected or {}).get('proposed_xml') or s['source_xml']
 p=re.findall(r'<p\b[^>]*>.*?</p>',before,re.S);q=re.findall(r'<p\b[^>]*>.*?</p>',a['proposed_xml'],re.S)
 check={'number':a['number'],'source_id':a['source_id'],'canonical_source_unchanged':source_ok,'previous_draft_snapshot_current':previous_ok,'markup_and_no_placeholder':clean,'source_tables':ot,'proposed_tables':tables,'paragraphs_before':len(p),'paragraphs_after':len(q),'changed_paragraph_numbers':[i+1 for i,(x,y) in enumerate(zip(p,q)) if x!=y],'source_references_removed':sorted(set(references(s['source_xml']))-set(references(a['proposed_xml']))),'references_added':sorted(set(references(a['proposed_xml']))-set(references(s['source_xml']))),'explicit_normative_reduction':reduced}
 checks.append(check)
 if not(source_ok and previous_ok and clean and tables>=ot):fail.append(a['number'])
# Critical earlier cooperative reform is preserved exactly outside the four SRU paragraphs.
a=next(a for a in rows if a['number']=='L422-3');b=by['L422-3']['previous_draft']['proposed_xml'];q=a['proposed_xml'];bp=re.findall(r'<p\b[^>]*>.*?</p>',b,re.S);qp=re.findall(r'<p\b[^>]*>.*?</p>',q,re.S)
coop_ok=len(bp)==len(qp)==72 and [i+1 for i,(x,y) in enumerate(zip(bp,qp)) if x!=y]==[31,47,55,60]
plh_before=re.findall(r'<p\b[^>]*>.*?</p>',by['L302-4']['previous_draft']['proposed_xml'],re.S)[:8]
plh_after=re.findall(r'<p\b[^>]*>.*?</p>',next(a for a in rows if a['number']=='L302-4')['proposed_xml'],re.S)[:8]
inventory=json.load(open('legal-rewrite/runtime/sru-reference-inventory.json'));invkeys={(a['code_id'],a['source_id']) for a in inventory}
initial=source[:24]
audit={'scope':'SRU legislative CCH outside core, plus seven assigned classification checks and L431-1 false positive','candidate_count':len(rows),'examined_articles':len(report),'newly_rewritten_sources':sum(by[a['number']].get('previous_draft') is None for a in rows),'existing_proposals_revised':sum(by[a['number']].get('previous_draft') is not None for a in rows),'retained_without_new_count':sum(a['treatment']=='retained_no_new_draft' for a in report),'initial24_present_in_inventory':len(initial)==24 and all((a['code_id'],a['source_id']) in invkeys for a in initial),'cooperative_reform_preserved_72_paragraphs':coop_ok,'plh_I_eight_paragraphs_identical':plh_before==plh_after,'duplicate_source_ids':len(rows)!=len({(a['code_id'],a['source_id']) for a in rows}),'database_writes':False,'numbered_batches_written':False,'publication':False,'failures':fail,'checks':checks}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(P/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in audit.items() if k!='checks'},ensure_ascii=False,indent=2))
assert not fail and coop_ok and plh_before==plh_after
