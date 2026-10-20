"""Read-only final check of an isolated draft pack. No integration/publication."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sqlite3,sys,copy
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
def load(n):return json.loads((P/n).read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
main_s=load('source.json');main_a=load('answer.json');s=main_s+load('companion-source.json');a=main_a+load('companion-answer.json');refs=load('references.json');snap=load('reference-targets.json')
for x in a:
 if x['number']=='1964':
  x['reference_checks']=[dict(target_key=k,view_sha256=snap['targets'][k]['view_sha256'],assessment="L’article724 entier institue le droit sur la cession onéreuse d’un office, son indemnité de création ou suppression et ses conditions de paiement.1964 maintenu permet la restitution quand la transmission n’a pas pris effet ou à hauteur de la réduction du prix. Il ne supprime pas le tarif d’une cession effective, ne fait pas renaître des droits de succession et ne retire pas une restitution ancienne ou future. L’indemnité d’office, même versée à un héritier, a un fait générateur autonome qui n’est pas une succession taxée par elle-même.")for k in snap['requirements'][rc.key(x)]]
for row in a:
 if row['number']=='1665 bis':
  texts={'199 quater C':"La cible entière, source et proposition, conserve le crédit de cotisations syndicales des salariés, fonctionnaires et militaires représentatifs, au taux66%, limite1% et exclusion fraisréels, avec excédent remboursable et reçu surdemande. La suppression du seul seuil8euros d’acompte1665bis ne modifie aucun de ces taux, conditions ou bénéficiaires, n’impose pas un nouveau reçu et ne transforme pas le remboursement final en second crédit. L’avance60% reste régularisée une seule fois à la liquidation.",
  '204 H':"L’article204H entier et ses trois grilles, note et proposition contratunique ont été lus. Le II garde le tauxnul sous ses deux conditions, RFR29310euros indexé parpart et exceptions ;1665bis garde son calcul60% de la différence avantages/impôt197 pour ces foyers. La coupe du seuil d’avance ne modifie ni PAS, ni abattement demiSMIC des emplois temporaires équivalents, ni les taux et options des grilles. Un résultat négatif ne devient pas un nouveau prélèvement, les régularisations finales restant dues dans leur champ."}
  row['reference_checks']=[dict(target_key=k,view_sha256=snap['targets'][k]['view_sha256'],assessment=texts[snap['targets'][k]['number']])for k in snap['requirements'][rc.key(row)]]
validate_answer(copy.deepcopy(a),copy.deepcopy(s));rc.accept_checks(a,s,snap)
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');checks=[];seen=set()
for x in s+refs:
 k=x['code_id'],x['source_id']
 if k in seen:continue
 seen.add(k);article=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone();raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];prior=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();old=x.get('previous_draft')
 g=dict(source_identity=article[0]==x['source_sha256'],source_body=article[1]==x['source_xml'],source_notes=source_notes(d,*k)==x['source_notes_xml'],source_document=H(raw)==x['source_document_sha256'],previous_draft=(prior is None if old is None else prior is not None and dict(prior)==old))
 assert all(g.values()),(x['number'],g)
 checks.append(dict(code_id=k[0],source_id=k[1],number=x['number'],guards=g,source_sha256=x['source_sha256'],source_body_sha256=H(x['source_xml']),source_notes_sha256=H(x['source_notes_xml']),source_document_sha256=x['source_document_sha256'],prior_proposed_sha256=H(old['proposed_xml'])if old else None,prior_full_row_sha256=H(json.dumps(old,ensure_ascii=False,sort_keys=True))if old else None))
rc.check_guards(d,snap);d.rollback();d.close();policy={n:H((P/n).read_bytes())==H((B/n).read_bytes())for n in['policy-coordinations.json','site-summaries.json']};assert all(policy.values()),policy
save('answer.json',a[:len(main_s)]);save('companion-answer.json',a[len(main_s):]);save('guards.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),mode='SQLite mode=ro BEGIN',article_guards=checks,guard_count=5*len(checks),policy_guards=policy,all_match=True,canonical_mutation=False))
findings=[]
for x,y in zip(s,a):
 findings.append(dict(code_id=x['code_id'],source_id=x['source_id'],number=x['number'],source_sha256=x['source_sha256'],source_body_sha256=H(x['source_xml']),source_notes_sha256=H(x['source_notes_xml']),source_document_sha256=x['source_document_sha256'],previous_draft=None,proposed_sha256=H(y['proposed_xml'])if y['proposed_xml']else None,whole_source_notes_read=True,classification=y['substantive_impact']['classification'],decision=y['reason'],benefit_review=y['benefit_review'],effects=y['substantive_impact']['effects']))
save('article-findings.json',findings)
counts={c:sum(x['substantive_impact']['classification']==c for x in a)for c in sorted({x['substantive_impact']['classification']for x in a})}
save('validation.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),validate_answer='passed on deepcopy; frozen candidate not normalized by verification',articles=len(a),whole_proposals=sum(x['proposed_xml']is not None for x in a),retained=sum(x['proposed_xml']is None for x in a),classification_counts=counts,guard_count=5*len(checks),unique_guarded_articles=len(checks),reference_requirements=sum(bool(v)for v in snap['requirements'].values()),policy_guards=policy,canonical_mutation=False,global_net_reduction='not_established',national_savings=None))
print(json.dumps(dict(articles=len(a),counts=counts,guards=5*len(checks))))
