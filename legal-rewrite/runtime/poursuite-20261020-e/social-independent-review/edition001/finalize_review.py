"""Independent read-only verification; writes isolated review evidence only."""
from pathlib import Path
import json,sqlite3,hashlib,sys,copy,re
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
base=B/'runtime/poursuite-20261020-e/social-coordination';packs=[base/'edition001',base/'complement-r243-59/edition001'];expected=[('46b7e86da226c423cf94c1948dd460a03d79f0e0fe79f27347d95c303004f5d9','8ced38d1de77327a25f2862fe698a7e12a2d1c7e58a1c691c06496e9684356c7'),('1c07e5d51674da1b949b272b1a2c1763d1849e2cf01b2c4b38b5106832ea7592','4622a98ac16e19485fad22a1f70bc7b4fdf1e6f1e633fc67eebdaac475ce4255')]
manifest_expected=['9831f7210a9a28dab7417b205b49b9a0337256657e77b67902b2b6be8b5b5150','32efc5b74c970dc2110c42193e8a77e6abc3b7b4e964d85c74f8fae7a784e36a']
read_materials=[];packages=[];sources=[];answers=[];snapshots=[]
for folder,(sh,ah)in zip(packs,expected):
 assert H((folder/'source.json').read_bytes())==sh;assert H((folder/'answer.json').read_bytes())==ah
 mf=folder/'manifest.json';assert mf.exists(),'Await final frozen manifest '+str(folder)
 assert H(mf.read_bytes())==manifest_expected[len(packages)],'Final manifest changed'
 manifest=json.loads(mf.read_text())
 for file,sha in manifest['files'].items():assert H((folder/file).read_bytes())==sha,(folder,file)
 for file,sha in manifest.get('external_evidence',{}).items():assert H((B/file).read_bytes())==sha,file
 s=json.loads((folder/'source.json').read_text());a=json.loads((folder/'answer.json').read_text());snap=json.loads((folder/'reference-targets.json').read_text())
 validate_answer(copy.deepcopy(a),copy.deepcopy(s));rc.accept_checks(copy.deepcopy(a),copy.deepcopy(s),snap)
 sources+=s;answers+=a;snapshots.append(snap)
 packages.append(dict(path=str(folder.relative_to(B)),source_sha256=sh,answer_sha256=ah,manifest_sha256=H(mf.read_bytes()),reference_targets_sha256=H((folder/'reference-targets.json').read_bytes())))
 read_materials.append(dict(package_path=str(folder.relative_to(B)),source=s,answer=a,manifest=manifest,reference_targets=snap))
# Reconfirm all23 complete source/notes/current proposals and raw documents against the actual capture.
cap=json.loads((P/'actual-read-capture.json').read_text());d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');guards=[]
for x in cap['rows']:
 k=(x['code_id'],x['source_id']);a=d.execute('select source_sha256,content_xml from articles where code_id=?and id=?',k).fetchone();raw=d.execute("select xml from documents where code_id=?and id=?and kind='ARTICLE'",k).fetchone()[0];old=d.execute('select *from drafts where code_id=?and source_id=?',k).fetchone();prior=dict(old)if old else None
 g=dict(source_identity=a[0]==x['source_sha256'],source_body=a[1]==x['source_xml'],notes=source_notes(d,*k)==x['source_notes_xml'],raw_document=H(raw)==x['source_document_sha256'],previous_draft=prior==x['previous_draft']);assert all(g.values()),(x['number'],g);guards.append(dict(code_id=k[0],source_id=k[1],number=x['number'],guards=g))
for snap in snapshots:rc.check_guards(d,snap)
d.rollback();d.close()
by={a['number']:a for a in answers};sb={a['number']:a for a in sources};paragraphs=lambda v:re.findall(r'<p>.*?</p>',v,re.S)
a=paragraphs(sb['R243-59']['source_xml']);b=paragraphs(by['R243-59']['proposed_xml']);assert len(a)==len(b);diff=[i for i,(x,y)in enumerate(zip(a,b))if x!=y];assert len(diff)==3
# All unmodified paragraphs, sequence and key safeguards are exact, not inferred from a lexical similarity score.
checks=dict(R243_59_exactly_three_paragraphs_changed=len(diff)==3,R243_59_all_other_paragraphs_exact=all(a[i]==b[i]for i in range(len(a))if i not in diff),R243_17_remains_null=by['R243-17']['proposed_xml']is None,R243_19_first_four_source_paragraphs_preserved_except_one_target=by['R243-19']['proposed_xml'].startswith(sb['R243-19']['source_xml'].replace('L. 243-7-2, L. 243-7-6, L. 243-7-7','L. 243-7-2, L. 243-7-7')),R243_59_ordinal_references_not_shifted=all((t in sb['R243-59']['source_xml'])and(t in by['R243-59']['proposed_xml'])for t in ['huitième alinéa du présent III','dixième alinéa du même III','deuxième et troisième alinéas du présent IV','troisième alinéa du I']),single_measure_no_new_cuts=all(a['substantive_impact']['classification']=='coordination_only'for a in answers if a['proposed_xml']is not None))
assert all(checks.values())
findings={
 'R243-18':'La fenêtre de six ans, son point de départ et l’assiette limitée au manquement répété sont conservés pour les seules sanctions définitives antérieures légalement dues. Le renvoi interne devient l’alinéa précédent après insertion du cadrage ; aucune sanction nouvelle ne naît d’observations anciennes. Conforme à la suppression deL243-7-6.',
 'R243-17':'Maintien/null justifié : les exemptions de majoration initiale,0,1% après paiement sous30jours et dispense après retard administratif de plus de2mois restent. Le renvoi àL243-7-6 ne crée pas une sanction ; sa suppression législative ferme les nouvelles applications et n’efface pas automatiquement les exceptions de situations anciennes définitivement sanctionnées.',
 'R243-19':'Le seul fondementL243-7-6 sort de la liquidation ordinaire. Le mois de paiement et les régimes de recouvrement/recours demeurent ; les anciens définitifs sont explicitement réservés sans nouvelle notification rouvrant les délais. Les sanctions autonomes, majorations ordinaires, DOETH et seuls reliquatsC3S restent dans leur champ.',
 'R243-59':'Trois paragraphes modifiés à leur emplacement : énumération des sanctions, constat de non-conformité destiné au10%, menace après observations sans redressement. Tous autres paragraphes exacts : avis30jours, charte opposable, conseil, copies hors locaux, motivation/contradictoire30–60jours, mainlevées et remboursement du crédit sous1mois. Aucun nouveau délai ni document. Les renvois ordinaux conservés ne sont pas implicitement corrigés comme une rectification officielle.'}
rows=[]
for x in sources:
 y=by[x['number']];z=next(z for z in cap['rows']if z['code_id']==x['code_id']and z['source_id']==x['source_id']);rows.append(dict(code_id=x['code_id'],source_id=x['source_id'],number=x['number'],source_sha256=x['source_sha256'],source_body_sha256=H(x['source_xml']),source_notes_sha256=H(x['source_notes_xml']),source_document_sha256=z['source_document_sha256'],previous_proposed_sha256=z['prior_proposed_sha256'],proposed_sha256=H(y['proposed_xml']),whole_source_notes_previous_and_proposal_read=True,verdict='approved_bounded',finding=findings[x['number']]))
report=dict(version=1,reviewed_at=datetime.now(timezone.utc).isoformat(),verdict='approved_for_guarded_registration_and_actual_postcommit_recertification',reviewer='Agent IA fiscalité, distinct du rédacteur',packages=packages,article_findings=rows,critical_identity_count=len(cap['rows']),guard_count=len(guards)*5,all_guards_match=True,structural_checks=checks,concrete_defects=[],correction_candidates=[],same_measure_id='urssaf-majoration-non-conformite-suppression',postcommit_plan_path=str((base/'post-commit-reissue-plan.json').relative_to(B)),postcommit_plan_sha256=H((base/'post-commit-reissue-plan.json').read_bytes()),no_new_material_reduction_counted=True,
 C141_bounded_compatibility=dict(verdict='compatible_conditional_on_exact_postcommit_views_and_parent_approval',literal_inventory='C141-literal-inventory-independent.json',actual_remaining_referrer='LEGITEXT000006073189|LEGIARTI000047435216',whole_remaining_C_referrer_read=True,finding='R243-59-6-A renvoie au début de contrôle duI et à l’envoi de la lettre duIII. Ces définitions restent exactement dansR243-59 ; la suppression du10% ne modifie pas leurs dates. Aucune nouvelle obligation ou perte de garantie identifiée par ce changement borné.',whole_141_semantic_reread=False,other_140_not_claimed_reread=True,existing_D_fiscal_changes_not_reapproved_by_this_social_review=True,no_ledger_adoption=True),
 required_postcommit_actions=['Recapturer les vraies vues après les inscriptionsE, notammentR243-59 ; comparer les trois futurs corps exacts auxhashs proposés avant toute réémission.','Soumettre les nouvelles analyses de références à l’approbation root ; aucun certificat futur de ce dossier ne vaut certificat actuel.','Pour les141, conserver l’analyse propre et les corps/sources/notes inchangés, vérifier toutes autres gardes et arrêter en cas de divergence non explicitement examinée. Les trois anciens auditsC R243-17/-18/-19 nécessitent leur remplacement tracé par les nouvelles analysesE.','Les corrections fiscalesD ont leur preuve séparée ; aucune réattestation globale ou approbation implicite de leurs autres chaînes.'],
 limits=['Les18referrers du repérage de l’auteur ne sont pas tous présentés comme relus sémantiquement ; le referrer restant deC a été lu entier.','Les ordinals source demeurent à leur emplacement ; aucune réparation silencieuse d’une ambiguïté préexistante n’est revendiquée.','Aucune validation juridique professionnelle ni clôture sémantique globale des141ou du corpus ; coûts et économies nationaux non chiffrés.'],source_primary_basis='DILA documents entiers capturés localement, empreintes vérifiées en SQLite mode=ro BEGIN',policy_sha256=rc.policy_state(),canonical_mutation=False,native_certificates_issued=False,ledger_mutation=False,publication=False,semantic_review_by_jurist=False,national_savings=None)
save('review.json',report);save('checks.json',dict(guards=guards,structural_checks=checks,validate_answer='passed_on_deepcopy',reference_checks='passed_against_actual_precommit_views_only'));save('audited-frozen-packages.json',read_materials)
files={f.name:H(f.read_bytes())for f in sorted(P.iterdir())if f.is_file()and f.name!='manifest.json'};save('manifest.json',dict(version=1,status='frozen_independent_review_no_commit',files_sha256=files,packages=packages,canonical_mutation=False))
print('review SHA',H((P/'review.json').read_bytes()));print('manifest SHA',H((P/'manifest.json').read_bytes()))
