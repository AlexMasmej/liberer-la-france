"""Pin the parent's whole-source reading and separately read merged CSS bodies."""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,sqlite3,sys
P=Path(__file__).resolve().parent;B=P.parents[1]
sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from ingest import source_notes
import reference_coherence as rc
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
F=P/'social/edition002';O=P/'social/edition001'
m=read(F/'manifest.json');assert m.get('frozen') is True
for n,h in m.get('files',m.get('files_sha256',{})).items():assert sha(F/n)==h,n
ss,aa=read(F/'source.json'),read(F/'answer.json')
old_s={rc.key(s):s for s in read(O/'source.json')};old_a={rc.key(a):a for a in read(O/'answer.json')}
assert len(ss)==len(aa)==24
merged_bodies={'L242-12-1','L243-6','L243-6-5','R243-15','R243-45-1'}
for s,a in zip(ss,aa):
    assert rc.key(s)==rc.key(a)
    old=old_s[rc.key(s)]
    assert all(s[f]==old[f] for f in ('source_sha256','source_xml','source_notes_xml'))
    if a['number'] not in merged_bodies:assert a['proposed_xml']==old_a[rc.key(a)]['proposed_xml'],a['number']
for number in ['L242-12-1','L243-6','L243-6-5']:
    s=next(s for s in ss if s['number']==number);a=next(a for a in aa if a['number']==number)
    assert a['proposed_xml']==s['previous_draft']['proposed_xml'],number
for number in ['L244-2','R243-48']:
    a=next(a for a in aa if a['number']==number)
    assert a['substantive_impact']['classification']=='coordination_only'
validate_answer(copy.deepcopy(aa),copy.deepcopy(ss))
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
for s in ss+read(F/'context.json'):
    k=s['code_id'],s['source_id']
    assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone()==(s['source_sha256'],s['source_xml']),k
    assert source_notes(db,*k)==s['source_notes_xml'],k
    old=s.get('previous_draft');current=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
    assert current==((old['source_sha256'],old['proposed_xml'])if old else None),k
rc.check_guards(db,read(F/'reference-targets.json'));db.close()
review=dict(approved_at=datetime.now(timezone.utc).isoformat(),reviewer='Parent distinct du rédacteur social et du worker CLI',
    whole_sources_and_notes_read=24,whole_original_proposals_read=10,
    whole_actual_CLI_beforeimages_read=5,whole_merged_bodies_separately_read=5,
    critical_contexts_read_entire=['L151-1','L243-6-4','R142-1','R155-1','R151-1','R155-4','R244-1','R243-8','R243-8-1','L243-1-2','L243-7','L243-7-1 A','L243-7-2','L243-12-1','R243-59','L133-5-4','R243-16','R243-20','R243-21','R133-14'],
    external_primary_bodies_read=['Civil2044','CPC641','CPC642','CommerceR521-20','CRPAL112-8/9/10/15etR112-16'],
    source_notes_beforeimages_and_reference_guards=True,blocking_findings=[],
    findings=[
        'Les trois améliorations CLI sont conservées exactement, sans retour aux candidats natifs plus restrictifs.',
        'R243-15 I/IV retire effectivement les majorations propres au calcul provisoire ; DOETH III et retard de paiement ordinaire restent distincts.',
        'R243-45-1 IV/V/VIII ne rétablit ni approbation particulière ni rapport annuel ; concessions, communication, contrôle autonome et recours restent.',
        'La régularisation conserve le principal réellement dû ; prise en compte anticipée des exonérations et base non majorée ne sont pas des baisses de taux.',
        'Remboursement AT-MP d’office classé mixed : démarche privée retirée et traitement ajouté à l’organisme, coût net inconnu.',
        'Notifications L244-2/R243-48 reclassées coordination_only : aucun gain CRPA existant recompté.',
        'Préavis individuel quinze jours et barème de rupture ne sont pas transformés en délais de contrôle ni remises de cotisations.'
    ],
    limits=['Lecture indépendante bornée aux textes désignés, pas validation juridique globale des régimes externes.','Cibles intrapaquet effectivement modifiées à recapturer et certificats à réémettre après enregistrement/politique C.','Ni baisse nette globale de complexité ni économie nationale démontrée.'],
    answer_sha256=sha(F/'answer.json'),source_sha256=sha(F/'source.json'),manifest_sha256=sha(F/'manifest.json'),
    national_net_savings=None,semantic_review_by_jurist=False)
out=P/'social-independent-review/edition002';out.mkdir(parents=True,exist_ok=True)
(out/'review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print('24 CSS whole-source dispositions independently reviewed; no canon mutation')
