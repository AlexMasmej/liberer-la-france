from pathlib import Path
import json,hashlib,sqlite3,re
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;B=P.parents[3]
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
def load(n):return json.loads((P/n).read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
s=load('source.json');a=load('answer.json');refs=load('references.json');all_by={x['number']:x for x in refs+s if x['code_id']=='LEGITEXT000006069577'}
all_by.update({'annIII '+x['number']:x for x in refs if x['code_id']!='LEGITEXT000006069577'})
answers={x['code_id']+'|'+x['source_id']:x for x in a}
M={
'849':{'658':'Une seule copie ; conserve les supports et exceptions du I658 expressément réservés.'},
'850':{'1837':'Affirmation du prix et incrimination de la fausse affirmation ; anti-fraude maintenue.'},
'853':{'635':'Actes et décisions restent présentés dans les cas et délais légaux, seul bordereau distinct retiré.','658':'Le support de présentation des actes reste régi par658 ; aucun original utile retiré.'},
'854':{},
'855':{'658':'Champ exact des minutes/expéditions et exemptions de taxation des copies.','1704':'Quittance conservée, date/service/référence disponibles, pas suppression de la preuve.','862':'Retrait de la reproduction intégrale doit être effectif aussi dans le champ des remises862.'},
'856':{'855':'Même mesure de remplacement des transcriptions par références : règle sœur et portée conservées.'},
'857':{'1704':'La quittance et la preuve de paiement restent disponibles malgré le format simplifié ; restitution conservée.'},
'860':{'647':'Distinction des deux circuits de formalité fusionnée/enregistrement séparé.','annIII 253':'Exemplaire unique déjà proposé en C, transmis entre services, même mesure sans nouveau gain.','annIII 255':'Mentions utiles conservées et absence de rétablissement du projet distinct de liquidation supprimé.','annIII 256':'Canaux de transmission et non-double envoi cohérents.','annIII 257':'Refus et irrégularités matérielles ; la réduction des exemplaires ne retire pas les contrôles essentiels.','1402':'La mutation cadastrale exige toujours la publicité préalable.','870':'Désignation cadastrale et sécurité des droits conservées.'},
'862':{'635':'Champ limité des greffiers/INPI conservé aux actes5°,7°,7°bis.','855':'Coordination expresse vers les mentions simplifiées sans transcription entière.','1701':'Paiement préalable et gratuité des nouveaux décès distincts, pas délivrance inconditionnelle généralisée.','1840 C':'Responsabilité pour retard demeure ; pas suppression indirecte des obligations de fond.'},
'863':{'850':'Affirmation du prix conservée ; avertissement aux parties ne devient pas sans objet.','1837':'Sanctions de l’affirmation frauduleuse préservées dans leur champ distinct.'},
'864':{'1754':'Solidarité de complicité de dissimulation du prix, champV5 conservé.','1729':'Majorations de mauvaise foi/fraude distinctes et non supprimées.','1840 B':'Destitution liée au prix clandestin de cession d’office conservée.'},
'865':{'1704':'Ventilation des sommes effectivement perçues demeure identifiable ; facture des débours contrôlable.'},
'866':{'849':'Exclusion de confusion : le double civil remis/conservé n’est pas le double fiscal849 dont la nouvelle signature est retirée.'},
'867':{'868':'Fusion de deux seuls répertoires fiscaux ; toutes catégories de documents et champs propres conservés.'},
'868':{'867':'Répertoire fiscal unique facultatif, règles de cote/paraphe et catégories inchangées ; pas de second registre fiscal.'},
'870':{'1402':'Cadastre et préalable de publicité, garanties distinctes du nombre d’exemplaires.'},
'871':{'873':'La simplification du prix en chiffres ne change pas les catégories habilitées aux ventes.','876':'Les courtiers déjà habilités gardent leur champ ; pas d’extension commerciale silencieuse.'},
'873':{'871':'Autorités de vente habilitées inchangées.','876':'Le renvoi des courtiers hérite de la liberté de format et des mentions/signatures maintenues.'},
'876':{'871':'Champ des ventes et professionnels habilités source maintenu.','873':'Renvoi dynamique aux procès-verbaux simplifiés, pas de rétablissement des prix en lettres.'},
'877':{'664':'TPF corrélative et formalité fusionnée, distinction avec enregistrement.','647':'Les circuits avant/après enregistrement restent distincts.','1701':'Les certificats successoraux supprimés pour décès nouveaux ne sont pas recréés par le maintien de la preuve d’une autre exemption.'},
'886':{'887':'Modes de paiement conservés, seul minimum et non ensemble de la contribution supprimé.','890':'Toute exemption de timbre garde sa dispense de formalité.','891':'Remise0,50% liée aux machines reste autorisée sans relèvement d’une charge.'},
'887':{'886':'Le maintien de tous les modes ne doit pas faire revivre le plancher supprimé.'},
'888':{'887':'Identification du timbre mobile dans le champ des supports permis ; pas de remplacement ni équipement neuf.'},
'889':{'887':'Le visa en débet reste un moyen de paiement existant, non remplacé par du comptant obligatoire.','890':'Dispense de formalité attachée aux exemptions de timbre intacte.','891':'Aucune suppression indirecte de remise sur les machines.','1704':'Même famille de liberté du format des quittances déjà en D ; pas nouvelle mesure mère.'}
}
def guard(x,proposal):return dict(code_id=x['code_id'],source_id=x['source_id'],number=x['number'],source_sha256=x['source_sha256'],source_body_sha256=H(x['source_xml']),source_notes_sha256=H(x['source_notes_xml']),proposed_sha256=H(proposal))
rows=[]
for x in s:
 deps=[]
 for n,why in M[x['number']].items():
  y=all_by[n];k=y['code_id']+'|'+y['source_id'];old=(y.get('previous_draft')or{}).get('proposed_xml');future=answers[k]['proposed_xml']if k in answers else old
  deps.append(dict(code_id=y['code_id'],source_id=y['source_id'],number=y['number'],justification=why,whole_source_notes_current_proposal_read=True,current_guard=guard(y,old),future_guard=guard(y,future),future_intrapaquet_proposal=k in answers and future is not None,source_document_sha256=y['source_document_sha256'],source_path='source.json'if k in answers else'references.json'))
 extra=[]
 if x['number']=='849':extra.append(dict(code_id='LEGITEXT000006069583',source_id='LEGIARTI000039280712',number='L106',source_path='external-primary-sources.json',whole_text_read=True,external_not_a_canonical_candidate=True,source_text_sha256=load('external-primary-sources.json')[0]['source_text_sha256'],justification='Copie archivée qualifiée expressément de double849, droits de communication et secret conservés ; pas abrogation du LPF.'))
 if x['number']=='867':
  h=load('historical-635-2019.json');extra.append(dict(code_id=h['article']['code_id'],source_id=h['article']['id'],number='635 at2019-12-31',source_path='historical-635-2019.json',source_sha256=h['article']['source_sha256'],whole_text_notes_read=True,historical_only_not_a_canonical_candidate=True,justification='Cible historique expressément voulue par867, notamment3°/4°1 et5°/6°2. Aucun remplacement silencieux par la635actuelle.'))
 rows.append(dict(code_id=x['code_id'],source_id=x['source_id'],number=x['number'],dependencies=deps,documentary_dependencies=extra,retained_external_references_not_claimed_rewritten=(["Règles civiles/professionnelles externes conservées ; périmètre détaillé dans unresolved-coordinations.json, pas de validation exhaustive de ces autres codes."]if x['number']in ['854','862','864','866','867','868','871','876']else[])))
save('article-dependency-map.json',dict(version=1,status='isolated_evidence_not_a_certificate',future_intrapaquet_guards_require_postregistration_capture=True,each_row_specifically_justified=True,no_all_context_pinning=True,rows=rows))
# Examine existing dependency guards without renewing them or pretending the whole audited corpus was re-read.
ledger=B/'runtime/substantive-audits.json';lr=ledger.read_bytes();l=json.loads(lr);ck={x['key']for x in json.loads((B/'runtime/poursuite-20261020-c/audit-adoption.json').read_text())['adopted']};dk=set()
for fn in ['answer.json','companion-answer.json']:
 for v in json.loads((B/'runtime/poursuite-20261020-d/fiscal/edition002'/fn).read_text()):dk.add(v['code_id']+'|'+v['source_id'])
future={x['code_id']+'|'+x['source_id']:x for x in a if x['proposed_xml']is not None};changes=[]
for row in l['audits']:
 k=row['code_id']+'|'+row['source_id'];phase='C'if k in ck else'D'if k in dk else'prior'
 for g in row.get('dependency_guards',[]):
  t=g['code_id']+'|'+g['source_id']
  if t not in future:continue
  f=future[t];ns=H(f['proposed_xml']);old=g.get('proposed_sha256')
  if old==ns:continue
  changes.append(dict(phase=phase,referrer_code_id=row['code_id'],referrer_source_id=row['source_id'],target_code_id=f['code_id'],target_source_id=f['source_id'],target_number=f['number'],recorded_guard=g,future_proposed_sha256=ns,changed_fields=['proposed_sha256'],current_guard_not_recertified=True))
# Guard counts do not prove real legal dependence. A source/proposal mention scan records candidates only.
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');direct=[];capt=[]
for key in sorted(ck|dk):
 code,id=key.split('|');x=d.execute('select number,content_xml,source_sha256 from articles where code_id=?and id=?',(code,id)).fetchone();old=d.execute('select *from drafts where code_id=?and source_id=?',(code,id)).fetchone();body=old['proposed_xml']if old and old['proposed_xml']else x['content_xml'];matches=[]
 for t,f in future.items():
  n=f['number'];pat=re.compile(r'(?<![\dA-Za-z])'+re.escape(n)+r'(?![\dA-Za-z])',re.I)
  for m in pat.finditer(body):matches.append(dict(target_key=t,target_number=n,context=body[max(0,m.start()-140):m.end()+150]))
 if matches:
  direct.append(dict(code_id=code,source_id=id,number=x['number'],phase='C'if key in ck else'D',matched_contexts=matches))
  capt.append(dict(code_id=code,source_id=id,number=x['number'],source_xml=x['content_xml'],source_sha256=x['source_sha256'],previous_draft=dict(old)if old else None))
d.rollback();d.close()
save('C-D-dependency-impact.json',dict(captured_at=datetime.now(timezone.utc).isoformat(),ledger_sha256=H(lr),stored_audits=len(l['audits']),changes=changes,counts={phase:dict(guard_changes=sum(x['phase']==phase for x in changes),affected_audits=len({(x['referrer_code_id'],x['referrer_source_id'])for x in changes if x['phase']==phase}))for phase in ['C','D','prior']},current_vs_future_separate=True,actual_referrer_candidates=direct,no_recertification_or_active_mutation=True,no_all_C_D_semantic_reread_claimed=True))
save('C-D-direct-referrer-captures.json',capt)
print('map24 rows',sum(len(x['dependencies'])for x in rows),'exact edges; impacts',len(changes),'referrer candidates',[(x['phase'],x['number'])for x in direct])
