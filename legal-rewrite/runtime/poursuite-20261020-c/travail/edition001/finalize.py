from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sqlite3,sys,copy
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
def load(n):return json.loads((P/n).read_text())
def save(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
sources,answers=load('source.json'),load('answer.json')
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
snapshot=rc.capture(db,sources,answers)
for x in load('context.json'):
 key=x['code_id'],x['source_id'];k=rc.key(x)
 assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()==(x['source_sha256'],x['source_xml']),k
 assert source_notes(db,*key)==x['source_notes_xml'],k
 old=x.get('previous_draft');now=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
 assert now==((old['source_sha256'],old['proposed_xml'])if old else None),k
 snapshot['targets'][k]=rc.view(db,k)
assessments={
 'L1234-1':"Source et proposition entières lues : quinze jours calendaires pour les contrats uniques nouveaux, contrats antérieurs et procédures collectives/protections réservés. Les mentions de préavis du bulletin et l'information sur les accords ne fixent pas d'autre durée ; le présent lot ne modifie ni notification ni paiement de ce préavis.",
 'L1221-2':"Source et proposition entières lues : les nouvelles embauches sont en contrat unique à durée indéterminée ; une mission ou formation n'en fixe pas la fin automatique. Les textes d'information et de bulletin n'autorisent aucun nouveauCDD et restent applicables aux anciens contrats selon leurs règles propres.",
 'L1234-9':"Source, note et proposition entières lues : pas d'indemnité ordinaire avant un an ; ensuite0,20mois par année totale au prorata des mois complets, plafond6mois, rupture à l'initiative employeur et exception fautegrave selon la cible. Bulletin accepté n'est pas renonciation ; aucune de ces conditions ni les droits antérieurs/spéciaux n'est modifiée par ce lot.",
 'R1221-34':"Source, note et proposition entières lues : le13° identifie les conventions et accords, distinct du10° sur la rupture et les quinzejours. R2262-1 conserve cette information et n'impose pas un second document si les exigences applicables sont déjà remplies ; les quatorze catégories d'informations ne sont pas supprimées.",
 'R1221-35':"Source, note et proposition entières lues : information13° sur les accords au plus tard unmois après embauche ; les mentions1°à5°,7°,11°/12° sousseptjours sont distinctes. Le brouillon dispense déjà de répéter une information complète individuellement remise selonR1221-39 ; les textes du lot ne rétablissent ni double remise ni délai de septjours pour le13°.",
 'R5122-18':"Source, note2023 et proposition entières lues : indemnité activitépartielle60%brut sousplafond4,5SMIC et100%net en formation ; limites au nethabituel et planchers temporaires/tempspartiel distincts. Le16° deR3243-1 conserve heures/taux/sommes affichés ; aucun nouveau taux ni perte de garantie pour anciens/nouveaux contrats ne résulte du maintien du bulletin.",
 'R844-1':"Source entière et note2026 sur congé supplémentaire de naissance lues ; pas de projet actuel. LeII définit le montant net social pour les revenus concernés avec exclusions de financement et contributions salarié, les autres ressources et prestations restant distinctes. Maintenir le9°bis deR3243-1 ne change ni assiette de prestations ni cotisations et conserve les données nécessaires.",
}
for row in answers:
 needs=snapshot['requirements'].get(rc.key(row),[])
 if needs:row['reference_checks']=[dict(target_key=k,view_sha256=snapshot['targets'][k]['view_sha256'],assessment=assessments[snapshot['targets'][k]['number']])for k in needs]
rc.accept_checks(answers,sources,snapshot)
validate_answer(answers,sources)
for s in sources:
 key=s['code_id'],s['source_id'];assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()==(s['source_sha256'],s['source_xml'])
 assert source_notes(db,*key)==s['source_notes_xml']
 raw=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw
 assert raw==s['source_document_xml']
 old=s.get('previous_draft');assert db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()==((old['source_sha256'],old['proposed_xml'])if old else None)
for f in ['policy-coordinations.json','site-summaries.json']:assert H((P/f).read_bytes())==H((B/f).read_bytes())
rc.check_guards(db,snapshot);db.close()
save('answer.json',answers);save('reference-targets.json',snapshot)
save('validation.json',dict(validated_at=datetime.now(timezone.utc).isoformat(),articles=len(sources),source_body_notes_document_prior_exact=True,external_target_guards=len(snapshot['targets']),schema_passes=True,policies_match=True,canonical_mutation=False))
save('audit.json',dict(scope='21 entrées canoniques ; sources et notes entières, dépendances nommées ; aucun audit global des cinq codes',new_measures=['accords-liste-annuelle-modifications-supprimee','bulletin-electronique-raccordement-cpa-facultatif','bulletin-electronique-preavis-information-mois-supprime'],existing_measure_not_recounted='information-collective-support-unique',proposals=sum(bool(a['proposed_xml'])for a in answers),retained_necessary=sum(a['proposed_xml']is None for a in answers),no_archive_duration_reduced=True,no_salary_tax_rate_changed=True,known_outside_scope=['Modèles ministériels2016/2023 : pas de réécriture ni d’abrogation annoncée, primaire2016 intégral non récupéré ;R3243-2 entier conservé.','Raccordement matériel du compteCPA non inspecté ; aucun service présumé disponible et aucune économie nationale estimée.','Dispositions autonomes information/consultation et protection des données non abrogées par suppression d’une liste ou d’un raccordement.'],national_savings=None,net_global_reduction='not_established',semantic_review_by_jurist=False))
files={str(f.relative_to(P)):H(f.read_bytes())for f in P.rglob('*')if f.is_file()and f.name!='manifest.json'}
save('manifest.json',dict(frozen=True,files=files,canonical_mutation=False,review_required=True))
print('Frozen21 articles;7 full proposals,14 necessary retentions;3 new distinct measures; guards exact.')
