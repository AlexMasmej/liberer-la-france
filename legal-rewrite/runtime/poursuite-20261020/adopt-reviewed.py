"""Adopt only registered, bounded counter-readings with exact current bodies."""
from pathlib import Path
from datetime import datetime,timezone
import json,sqlite3,sys,hashlib
B=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
sys.path.insert(0,str(B))
from ingest import source_notes
from substantive_impact import validate,certificate,digest
packages=[
 ('social/edition001','social-independent-review/review.json','Contrelecture intégrale par un agent IA distinct de l’auteur'),
 ('social-legislative-complement/edition001','social-independent-review/review.json','Contrelecture intégrale par un agent IA distinct de l’auteur'),
 ('fiscal/edition002','fiscal-independent-review/review-002.json','Contrelecture intégrale IA et vérification des quatre corrections de bilan'),
 ('logement/edition001','logement/edition001/root-guards.log','Contrelecture intégrale par le parent, distinct du rédacteur ; six cibles centrales relues'),
 ('logement/edition001/companion','logement/edition001/root-guards.log','Contrelecture intégrale par le parent, distinct du rédacteur ; coordination CU et CCH'),
 ('insertion-coherence/edition001','insertion-coherence/review-travail/review.json','Contrelecture intégrale par un agent IA distinct du parent rédacteur'),
 ('fiscal-1684/edition001','fiscal-1684-independent-review/edition001/independent-audit.json','Contrelectures intégrales par le parent et un agent IA distinct du rédacteur'),
 ('pea/edition001','pea-independent-review/review.json','Contrelecture intégrale par un agent IA distinct du parent rédacteur'),
 ('cfe-micro/edition001','cfe-additional-taxes-review/edition001/audit.json','Contrelecture par le parent puis par un agent IA indépendant des quatre articles et douze renvois pertinents'),
 ('microsocial/edition003','microsocial-independent-review/edition002/independent-audit.json','Contrelecture intégrale IA distincte du rédacteur ; corps identiques002/003, provenance actualisée'),
 ('microsocial-option-coordination/edition001','microsocial-option-coordination/edition001/validation.json','Contrelecture intégrale par le parent ; une date coordonnée avec L613-7'),
 ('pfu-petits-revenus/edition002','pfu-independent-review/review-002.json','Contrelecture intégrale IA et contre-exemples de calcul'),
 ('logement-vsd-classification/edition001','logement-independent-bilan-review/edition001/review.json','Parent et contrelecture fiscale indépendante : rectification du bilan, texte normatif identique'),
 ('logement-deduplication/edition001','logement-independent-bilan-review/edition001/review.json','Contrelecture fiscale indépendante puis application par le parent : un dossier commun, coordinations sectorielles dédupliquées')]
stamp=datetime.now(timezone.utc).isoformat();policy=digest((B/'policy-coordinations.json').read_text())
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
target=B/'runtime/substantive-audits.json';old=json.loads(target.read_text());prior={(a['code_id'],a['source_id']):a for a in old['audits']};adopted=[];skipped=[]
reviewed={}
for name,evidence,_ in packages:
 folder=P/name
 if (folder/'registration.json').exists() and (P/evidence).exists():
  sources={(x['code_id'],x['source_id']):x for x in json.loads((folder/'source.json').read_text())}
  for row in json.loads((folder/'answer.json').read_text()):
   key=row['code_id'],row['source_id'];reviewed[key]=(sources[key],row,name)
def dependency_guards(row,name):
 # These pins cover texts actually counter-read in this tranche, not every
 # reference in French law. A later edit invalidates the bounded approval.
 from reference_coherence import token_refs,normalize
 refs=token_refs(row.get('proposed_xml') or '')
 guards=[]
 for key,(source,target,other) in reviewed.items():
  if key==(row['code_id'],row['source_id']):continue
  if name!=other and normalize(target['number']) not in refs:continue
  current=db.execute('SELECT status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
  assert current==(target['status'],target['proposed_xml']),('Reviewed dependency superseded',key)
  guards.append(dict(code_id=key[0],source_id=key[1],number=target['number'],source_sha256=source['source_sha256'],source_body_sha256=digest(source['source_xml']),source_notes_sha256=digest(source['source_notes_xml']),proposed_sha256=digest(target['proposed_xml'])))
 if name=='pfu-petits-revenus/edition002':
  captured=json.loads((P/name/'integration-reference-targets.json').read_text())
  for key,target in captured['targets'].items():
   parts=key.split('|');current=db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',parts).fetchone()
   assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',parts).fetchone()==(target['source_sha256'],target['source_xml']),key
   assert source_notes(db,*parts)==target['source_notes_xml'],key
   assert (current[0] if current else None)==target['proposed_xml'],('PFU dependency superseded',key)
   if any(g['code_id']==parts[0] and g['source_id']==parts[1] for g in guards):continue
   guards.append(dict(code_id=parts[0],source_id=parts[1],number=target['number'],source_sha256=target['source_sha256'],source_body_sha256=digest(target['source_xml']),source_notes_sha256=digest(target['source_notes_xml']),proposed_sha256=digest(target['proposed_xml'])))
 return guards
try:
 for name,evidence,reviewer in packages:
  folder=P/name;proof=P/evidence
  if not(folder/'registration.json').exists()or not proof.exists():
   skipped.append(dict(package=name,reason='Registration or independent evidence still absent'));continue
  sources={(x['code_id'],x['source_id']):x for x in json.loads((folder/'source.json').read_text())}
  for row in json.loads((folder/'answer.json').read_text()):
   key=row['code_id'],row['source_id'];source=sources[key]
   official=db.execute('SELECT content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?',key).fetchone()
   current=db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
   if not official or not current or current!=(row['source_sha256'],row['status'],row['proposed_xml']):
    skipped.append(dict(package=name,source_id=key[1],reason='Whole proposal superseded or not current'));continue
   assert official==(source['source_xml'],source['source_sha256']),key
   assert source_notes(db,*key)==source['source_notes_xml'],key
   validate(row,source,required=True,enforce_workflow=False)
   entry=dict(code_id=key[0],source_id=key[1],assessment=row['substantive_impact'],certificate=certificate(row,source,policy),reviewed_by=reviewer,approved_at=stamp,evidence_file=str(proof.relative_to(B)),dependency_guards=dependency_guards(row,name),semantic_review_by_jurist=False)
   # Existing earlier audits retain their original policy/date; no blind rebinding.
   prior[key]=entry;adopted.append(dict(package=name,source_id=key[1],classification=entry['assessment']['classification']))
finally:db.close()
data=dict(version=1,scope='Bounded full-text AI counter-readings; neither a corpus-wide net impact balance nor a jurist audit',approved_at=stamp,policy_sha256=policy,audits=list(prior.values()))
tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');tmp.replace(target)
(P/'audit-adoption.json').write_text(json.dumps(dict(adopted=adopted,skipped=skipped,older_policy_certificates_not_rebound=True,global_net_reduction='not_established',national_savings=None),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(newly_current=len(adopted),stored_audits=len(prior),skipped=len(skipped),global_net_reduction=False)))
