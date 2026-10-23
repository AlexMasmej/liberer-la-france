"""Seal a fresh, bounded CVAE review from whole articles already read."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sqlite3, sys, xml.etree.ElementTree as E
sys.dont_write_bytecode=True
OP=Path(__file__).resolve().parent
ROOT=OP.parents[1]
sys.path.insert(0,str(ROOT))
from ingest import source_notes
R=ROOT/'runtime'
AUDIT=R/'global-reference-audit-20261023T1908Z'
ORIGIN=R/'cvae-semantic-recheck-20261022T103000Z'
FOLLOWUP=R/'cvae-guard-change-followup-20261023T1912Z'
OUT=R/'cvae-semantic-recheck-20261023T1956Z'
OUT.mkdir(exist_ok=False)

def sha(b):return hashlib.sha256(b if isinstance(b,bytes) else (b or '').encode()).hexdigest()
def save(n,d):
    with (OUT/n).open('x') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
def plain(x):return ''.join(E.fromstring('<root>'+(x or '')+'</root>').itertext())
def read(p):return json.loads(p.read_text())

assert sha((FOLLOWUP/'artifact-manifest.json').read_bytes())=='055c3e74cb79a5f912296c68d35bb1e0525354ff06db036de699eb9a0452cdcb'
assert sha((ORIGIN/'artifact-manifest.json').read_bytes())=='9772b0e19d495979d553edf9d0c776ba5d321172b0d653816025a6133a4cfad5'
manifest={x['key']:x for x in map(json.loads,(AUDIT/'article-manifest.jsonl').open())}
packet=read(FOLLOWUP/'current-thirteen-article-packet.json')
primary=packet['articles']
assert len(primary)==13
db=sqlite3.connect((AUDIT/'corpus.snapshot.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
extra=[]
for number in ['234 nonies','172 bis','1655 ter','217 quindecies','1641']:
    rows=db.execute('SELECT a.* FROM articles a JOIN drafts d ON a.code_id=d.code_id AND a.id=d.source_id WHERE a.number=? AND a.code_id=?',(number,'LEGITEXT000006069577')).fetchall()
    assert len(rows)==1
    a=dict(rows[0]);a['key']=a['code_id']+'|'+a['id']
    a['draft']=dict(db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(a['code_id'],a['id'])).fetchone())
    doc=dict(db.execute("SELECT * FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(a['code_id'],a['id'])).fetchone())
    xml=doc.pop('xml');a['article_document_xml']=xml.decode() if isinstance(xml,bytes) else xml
    a['article_document_metadata']=doc;a['source_notes_xml']=source_notes(db,a['code_id'],a['id']);a['snapshot_guard']=manifest[a['key']]
    extra.append(a)
db.close()
articles=primary+extra
assert len({a['key'] for a in articles})==18
guards={}
validation=[]
coverage=[]
guard_names=['source_sha256','source_body_sha256','source_notes_sha256','article_document_sha256','article_document_stored_sha256','proposal_sha256','draft_source_sha256','draft_status']
for i,a in enumerate(articles):
    g=manifest[a['key']];d=a['draft']
    assert sha(a['content_xml'])==g['source_body_sha256']
    assert sha(a['source_notes_xml'])==g['source_notes_sha256']
    assert sha(a['article_document_xml'])==g['article_document_sha256']==g['article_document_stored_sha256']
    assert sha(d['proposed_xml'])==g['proposal_sha256']
    assert a['source_sha256']==d['source_sha256']==g['source_sha256']==g['draft_source_sha256']
    assert a['valid_from']==g['valid_from'] and a['valid_until']==g['valid_until']
    guards[a['key']]={k:g[k] for k in guard_names}
    coverage.append(dict(key=a['key'],number=a['number'],role='CVAE_primary_or_internal_dependency' if i<13 else 'additional_context_read_in_full',source_body_characters=len(a['content_xml']),proposal_characters=len(d['proposed_xml'] or ''),notes_characters=len(a['source_notes_xml']),reason_characters=len(d['reason']),review_notes_characters=len(d['review_notes']),source_and_proposal_notes_reasons_read_in_full=True))
    (OUT/f'read-{i:02d}.txt').write_text('\n'.join([a['key'],a['number'],a['valid_from'],a['valid_until'],'SOURCE',plain(a['content_xml']),'NOTA',plain(a['source_notes_xml']),'PROPOSITION',plain(d['proposed_xml']),'MOTIF',d['reason'],'NOTES',d['review_notes']]))
    validation.append(dict(key=a['key'],all_snapshot_guards_match=True,whole_source_document_and_boundaries_checked=True))
old_primary={a['key'] for a in read(ORIGIN/'review-packet.json')['articles']}
save('review-packet.json',dict(snapshot=str(AUDIT/'corpus.snapshot.sqlite'),sqlite_mode='ro',query_only=True,articles=[a for a in primary if a['key'] in old_primary]))
save('review-dependencies.json',dict(articles=[a for a in primary if a['key'] not in old_primary]+extra))
save('full-read-coverage.json',dict(articles=coverage,CVAE_group_articles=13,additional_context_articles=5,not_a_global_semantic_or_jurist_review=True))
analyses={
 '46 C':('transition_compatible',"Le III vise explicitement les années débutant au 1er janvier suivant l'année d'entrée en vigueur de la loi de suppression, comme 1586 ter et octies. Les années antérieures, contrôles, restitutions, prescriptions et recours restent préservés. La valeur ajoutée et la période de CFE ne créent aucune nouvelle déclaration CVAE. Le champ repris de172bis et l'exclusion1655ter ont été lus entièrement. Le eCRL suit l'encaissement de234nonies, frontière distincte de la CVAE."),
 '38':('transition_compatible',"Le3°duII retire le tableau CVAE suivant la même date explicite que1586ter ; la clause finale de simplification des dépôts réserve expressément cette transition. Un dépôt tardif relatif à une année ancienne ne dispense donc pas des obligations anciennes. Le réemploi des données ne crée pas de CVAE future. La rubrique CRL duIa appelle un nettoyage explicite du formulaire et du texte, mais234nonies interdit déjà son rétablissement par renvoi pour les recettes nouvelles : aucune nouvelle taxe n'est établie par ce seul renvoi."),
 '344 quindecies':('difference_de_periode_compatible',"Les deux abattements99% de LaPoste visent2025 et restent utilisables pour rectifications/restitutions ultérieures. Le renvoi à1586ter est historique ; la clause finale exclut toute CVAE future et conserve le fondement propre des avantages des autres années dans1635sexies.99% n'est ni taux d'impôt ni décret automatique d'une autre année."),
 '39':('transition_compatible',"Les1°g et2°l suppriment les données exclusivement CVAE selon la même frontière annuelle que1586ter/octies et conservent les obligations anciennes. L'avant-dernier alinéa de réemploi et la dernière transition sur les nouvelles coupes ne déplacent pas cette frontière. Source,NOTA2026, proposition et notes sont lues entièrement. Les nouvelles coupes APE/formation/net/totaux et les normes sociales ou suisses extérieures ne sont pas certifiées globalement par cette revue CVAE."),
 '1586 quinquies':('definition_autonome_maintenue',"LeI1–5 reste une règle de période pour la CFE et les impôts maintenus, leII retire seulement l'annualisation propre au barème CVAE futur et leIII conserve les règles anciennes.1647Bsexies maintient sa propre annualisation de valeur ajoutée. Le renvoi au premier alinéa de1586ter atteint effectivement une date explicite et ne réinstitue ni impôt ni déclaration."),
 '1586 sexies':('definition_autonome_maintenue',"Les définitions sectoriellesIàVII restent intégrales :95%,80/85%,7,6M€, BNC,foncier,banques,gestion financière,financement,assurances et plus-values de création sont préservés. Le préambule et la clause finale bornent leur utilisation aux avantages et impôts maintenus pour les années futures. Aucune assiette ou déclaration CVAE future n'en résulte. La recodification différée2030 reste un chantier explicite."),
 '238 bis HW':('renvoi_historique_volontaire_protection_autonome',"La définition de valeur ajoutée est figée à la veille de l'entrée de la loi et détachée de toute condition de paiement ou d'assujettissement CVAE. Les contrats15ans, ratio2,5kWh/€,55%,8000heures et600000€ restent intacts.238bisHV et217quindecies préservent l'amortissement50%, la période2023–2028 et le non-double emploi, sans imposer une distribution pour constater l'avantage. Les modalités européennes/loi2023extérieures restent non vérifiées.")
}
all_findings=[]
for line in (AUDIT/'findings.jsonl').open():
    f=json.loads(line)
    if f.get('source_key') in {a['key'] for a in primary}:all_findings.append(f)
save('current-scope-structural-findings.json',dict(findings=all_findings,administratively_resolved=0))
result=[]
for number,(classification,analysis) in analyses.items():
    a=next(a for a in primary if a['number']==number)
    result.append(dict(number=number,source_key=a['key'],classification=classification,analysis=analysis,source_guard=guards[a['key']],effective_inconsistency_established=False,resolved=False))
limits=[
 'Revue limitée aux interactions CVAE des13textes, avec5contreparties supplémentaires lues ; pas de certification de tous leurs autres renvois.',
 'Date de promulgation inconnue ; aucune actualisation au-delà du corpus figé au18octobre2026.',
 'Versions et calendriers différés2027–2030, recodification1647BsexiesA et compagnons hors noyau restent à coordonner ; ABROGE_DIFF ne signifie pas abrogation déjà applicable.',
 'Portée de laQPC2014-413 et modalités duVIarticle86loi2023-175, droit européen, normes DSN et franco-suisses, formulaires et téléprocédures restent hors certification exhaustive.',
 'Les nouvelles coordinations IS des46C/39/38 et238bisHV requièrent leurs propres contrôles :209/219 et autres contreparties ne sont pas intégralement requalifiés dans cette revue.',
 'Nettoyage explicite duIaannexeIII38/CRL et des formulaires2065/2072 à poursuivre ;234nonies interdit déjà les formalités propres aux recettes nouvelles.',
 'Aucune incohérence CVAE effective établie dans le seul groupe lu ne signifie absence globale de contradictions, résolution administrative ou validation par juriste.'
]
findings=dict(audit_id=read(AUDIT/'summary.json')['audit_id'],snapshot_path=str(AUDIT/'corpus.snapshot.sqlite'),snapshot_capture_sha256=read(AUDIT/'capture.json')['snapshot_sha256'],review_type='fresh_semantic_recheck_after_full_read',articles_read_in_full=18,CVAE_group_articles=13,additional_context_articles=5,findings_reviewed=7,historical_findings_reviewed=7,effective_inconsistencies_established=0,resolved_findings=0,findings=result,limits=limits,still_in_analysis=['global_priority_contradictions','CVAE_2027_2030_external_calendars','CRL_annexeIII38_wording_and_forms','IS_distribution_external_dependencies','CCH_L423_15_16','three_normative_source_holds'],semantic_review_by_jurist=False,automatic_change=False,active_state_modified=False,reviewed_at_utc=datetime.now(timezone.utc).isoformat())
findings['review_id']=sha(json.dumps(findings,ensure_ascii=False,sort_keys=True,separators=(',',':')))
save('findings-reviewed.json',findings)
policies={}
for name in ['corpus.json','policy-coordinations.json','site-summaries.json','reference-focus-extra.json']:
    b=(AUDIT/name).read_bytes();assert sha(b)==sha((ROOT/name).read_bytes())
    policies[name]=dict(current_sha256=sha(b),matches_snapshot=True)
save('policy-evidence.json',policies)
live=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);live.row_factory=sqlite3.Row;live.execute('PRAGMA query_only=ON');live.execute('BEGIN')
live_checks=[]
for a in articles:
    key=(a['code_id'],a['id']);d=dict(live.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone());s=dict(live.execute('SELECT * FROM articles WHERE code_id=? AND id=?',key).fetchone())
    assert all(d[k]==a['draft'][k] for k in ['source_sha256','status','proposed_xml','reason','review_notes']),a['key']
    assert all(s[k]==a[k] for k in ['content_xml','source_sha256','valid_from','valid_until']),a['key']
    assert source_notes(live,*key)==a['source_notes_xml']
    live_checks.append(dict(key=a['key'],whole_source_notes_boundaries_and_five_fields_match=True))
live.close()
save('live-final-state-check.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),sqlite_mode='ro',query_only=True,articles=live_checks,all_match=True))
save('final-state-check.json',dict(scope='Frozen1908Z snapshot; separate live check does not certify all other articles.',checked_at_utc=datetime.now(timezone.utc).isoformat(),all_match=True,articles={k:dict(current_guard=g,matches_snapshot=True) for k,g in guards.items()},policies=policies))
save('validation.json',dict(passed=True,checks=validation,policy_checks=policies,sqlite_mode='ro',query_only=True,scope='18 exact current guards and whole text/NOTA/document hashes; no automatic semantic certification.'))
save('prior-evidence-manifest.json',dict(origin=str(ORIGIN),manifest_sha256=sha((ORIGIN/'artifact-manifest.json').read_bytes()),limited_followup=str(FOLLOWUP),followup_manifest_sha256=sha((FOLLOWUP/'artifact-manifest.json').read_bytes()),current_audit_manifest_sha256=sha((AUDIT/'artifact-manifest.json').read_bytes())))
save('corrections.proposed.json',dict(corrections=[],reason='No effective CVAE contradiction established within the reviewed scope; wider coordination limits stay open.'))
(OUT/'REPORT.md').write_text('''# Relecture fraîche CVAE orientée contradictions

Les treize sources, propositions, notes, motifs et bornes ont été relus intégralement sur le snapshot1908Z, y compris les deux propositions46C/39 modifiées. Cinq contreparties supplémentaires ont été lues entièrement :234nonies,172bis,1655ter,217quindecies et1641. Les18gardes et les quatre politiques ont été recalculées ; les18sources/NOTA/bornes et cinq champs de proposition correspondent encore en transaction de lecture seule à la base vivante au contrôle final.

Sept situations historiques ont été qualifiées de nouveau. Dans ce seul périmètre, aucune contradiction CVAE effective n'est établie : même frontière annuelle future, obligations et droits des anciennes années préservés, définitions de valeur ajoutée/période et plafonds CFE maintenus, abattements99%LaPoste2025 et fondement futur protégés, accès au dispositif électrique indépendant du paiement de laCVAE. Les13textes relus ne sont pas13nouvelles acceptations de seconde passe et ne gonflent aucun compteur.

Les clauses nouvelles46C/39 ne sont pas réputées validées globalement. La bascule CRL par encaissement est distincte de la bascule annuelle CVAE.234nonies interdit déjà son rétablissement par renvoi ; l'expression de la rubriqueCRL38Ia et les formulaires restent à nettoyer. Les circuits sociaux, IS209/219, normes DSN/franco-suisses, QPC, modalités européennes et calendriers différés2027–2030 demeurent hors certification exhaustive. Les réserves précises figurent dans findings-reviewed.json.

Aucune correction canonique n'est proposée faute de contradiction CVAE démontrée dans le seul groupe. Aucun signalement structurel n'est administrativement résolu, aucun texte, politique, source ou audit publié n'a été changé et aucune validation par juriste n'est affirmée. Cette qualification fraîche peut être utilisée seulement sous ses18gardes exactes et limites ; elle ne remplace pas l'examen des autres contradictions prioritaires.
''')
files={p.name:dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(OUT.iterdir()) if p.is_file()}
save('artifact-manifest.json',dict(files=files))
print(json.dumps(dict(folder=str(OUT),manifest_sha256=sha((OUT/'artifact-manifest.json').read_bytes()),review_id=findings['review_id'],whole_articles_read=18,effective_CVAE_inconsistencies_established=0,other_scopes_open=True)))
