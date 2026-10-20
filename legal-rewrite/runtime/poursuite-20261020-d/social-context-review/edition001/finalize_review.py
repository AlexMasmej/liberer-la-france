import pathlib, json, hashlib, sqlite3, sys, datetime, re

H = pathlib.Path('legal-rewrite').resolve()
D = pathlib.Path(__file__).resolve().parent
E = H / 'runtime/poursuite-20261020-e/social-coordination'
sys.path.insert(0, str(H))
from ingest import source_notes
import reference_coherence as rc

def read(p): return json.loads(p.read_text())
def dump(p, x): p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def sha(x): return hashlib.sha256((x or '').encode()).hexdigest()
def file_sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def key(x): return x['code_id'] + '|' + x['source_id']
def digest(x): return sha(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
c = sqlite3.connect('file:' + str(H/'corpus.sqlite') + '?mode=ro', uri=True)
c.row_factory = sqlite3.Row
c.execute('BEGIN')

def current(k):
    code, sid = k.split('|')
    a = c.execute('select * from articles where code_id=? and id=?', (code,sid)).fetchone()
    d = c.execute('select * from drafts where code_id=? and source_id=?', (code,sid)).fetchone()
    raw = c.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'", (code,sid)).fetchone()
    xml = raw['xml'] if raw else None
    if isinstance(xml, bytes): xml = xml.decode()
    return {'source_sha256':a['source_sha256'], 'source_body_sha256':sha(a['content_xml']),
            'source_notes_sha256':sha(source_notes(c,code,sid)), 'proposed_sha256':sha(d['proposed_xml'] if d else None),
            'raw_document_sha256':sha(xml), 'draft_exists':bool(d), 'status':d['status'] if d else None}

captured = read(D/'captured-guard-records.json')
fresh = []
for old in captured:
    new = current(key(old))
    delta = {f:{'captured':old[f], 'current':v} for f,v in new.items() if old[f] != v}
    fresh.append({'key':key(old), 'number':old['number'], 'unchanged':not delta, 'delta':delta})
assert all(x['unchanged'] for x in fresh), [x for x in fresh if not x['unchanged']]
old_ledger = read(D/'ledger-before.json')
new_ledger = read(H/'runtime/substantive-audits.json')
Ckeys = {x['key'] for x in read(D/'C-adoption.json')['adopted']}
oldC = {key(x):x for x in old_ledger['audits'] if key(x) in Ckeys}
new_by_key = {key(x):x for x in new_ledger['audits']}
ledger_checks = [{'key':k,'old_audit_sha256':digest(a),'current_audit_sha256':digest(new_by_key[k]),
                  'unchanged':a == new_by_key[k]} for k,a in sorted(oldC.items())]
assert len(oldC)==144 and all(x['unchanged'] for x in ledger_checks)
policies = {name:{'captured_sha256':file_sha(D/name),'current_sha256':file_sha(H/name)}
            for name in ['policy-coordinations.json','site-summaries.json']}
assert all(x['captured_sha256']==x['current_sha256'] for x in policies.values())
dump(D/'final-guards.json', {'checked_at':now,'mode':'SQLite mode=ro BEGIN; no writes',
     'records':fresh,'unchanged_record_count':len(fresh),'C_audit_record_checks':ledger_checks,
     'current_ledger_count':len(new_ledger['audits']),'policies':policies,
     'scope':'No claim of semantic equivalence of other policy versions or of all dependency texts.'})

details = {
 'L243-6-7':('material_reduction','Convention désormais sans terme de cinq ans et sans visa ministériel : deux obstacles d’une même mesure. Traitement des agents, contrôle commun et contradictoire conservés. Ni exonération de dette ni changement de cotisations.'),
 'L243-7-6':('material_reduction','Suppression prospective de la majoration de 10 % pour non-conformité répétée, y compris sur observations anciennes. Principal et sanctions autonomes conservés ; seules les sanctions anciennes définitives légalement dues restent recouvrables, avec loi plus douce pour les non définitives. R243-18/-19 et R243-59 nécessitent les coordinations E : aucune chaîne réglementaire complète n’est déclarée déjà cohérente.'),
 'L243-12':('coordination_only','Mise à jour du renvoi au Code du travail L3243-4 ; conservation des cinq ans de double des bulletins, sans confondre les six ans de pièces du contrôle de L243-16. Aucun nouveau gain matériel.'),
 'L243-15':('material_reduction','L’attestation provisoire du nouvel indépendant n’est plus subordonnée à toutes les formalités génériques de création : activité régulièrement déclarée et première échéance restent exigées. Les obligations de création autonomes ne sont pas abrogées. Vigilance, garanties spécifiques de l’intérim, plans d’apurement, contestation et exception familiale conservés.')}
J = read(D/'job-current.json'); A = read(D/'job-answer.json')
findings=[]
for row,answer in zip(J,A):
    cls, conclusion = details.get(row['number'], ('retained_necessary', answer['reason']))
    findings.append({'key':key(row),'number':row['number'],'entire_source_read':True,'entire_notes_read':True,
       'entire_effective_proposal_read':True,'proposal_is_source_retention':answer['proposed_xml'] is None,
       'source_sha256':row['source_sha256'], **row['guards'], 'finding':cls,'conclusion':conclusion,
       'no_new_contract_or_rupture_rule':True,'national_savings':None,'semantic_review_by_jurist':False})
dump(D/'article-findings.json', {'job':'securite-sociale-00046','articles':findings,
     'summary':{'count':24,'material_article_changes':3,'material_measure_families':3,
       'coordination_only':1,'source_retained':20,'source_and_notes_characters':sum(len(x['source_xml'])+len(x['source_notes_xml']) for x in J)},
     'limit':'Bounded independent AI reading of these 24 complete articles and targeted contexts; no national savings estimate and no validation of all other accepted lots.'})

# Future E bodies are separate proposals, never current target views.
future=[]
for f in [E/'edition001',E/'complement-r243-59/edition001']:
    for s,a in zip(read(f/'source.json'),read(f/'answer.json')):
        future.append({'key':key(s),'number':s['number'],'pack':str(f.relative_to(H)),
          'source_sha256':s['source_sha256'],'source_body_sha256':sha(s['source_xml']),
          'source_notes_sha256':sha(s['source_notes_xml']), 'current_before':current(key(s)),
          'future_proposed_sha256':sha(a['proposed_xml']),'future_status':a['status'],
          'answer_file_sha256':file_sha(f/'answer.json'),'future_is_not_current':True})
excluded={x['key'] for x in future if x['number'] in ['R243-17','R243-18','R243-19']}
remaining=sorted(Ckeys-excluded)
assert len(remaining)==141
direct=read(D/'C-real-referrers-three-targets.json')
imp=read(D/'C-dependency-impact.json')
compat={'version':1,'prepared_at':now,'status':'proposal_only_not_adopted','audit_keys':remaining,
 'excluded_old_C_audits_requiring_explicit_replacement':sorted(excluded),
 'old_C_audit_records':ledger_checks,'mechanical_guard_differences':imp['changed_targets'],
 'current_target_under_review':'LEGITEXT000006073189|LEGIARTI000041396065',
 'future_E_views':future,
 'bounded_conclusion':'No operative new obligation or lost safeguard identified for the other 141 C articles from the prospective repeal of L243-7-6 and the three proposed regulatory coordinations. Literal-reference inventory of C sources and proposals finds only R243-17/-18/-19 for L243-7-6 or R243-18/-19. Among the 141, only R243-59-6-A refers to R243-59: the first visit and dispatch of the III observations letter, read in full, remain unchanged. This is not a rereading of the other 140 full C bodies or a legal validation of their complete dependency chains.',
 'full_C_bodies_reread_for_this_bounded_review':['R243-17','R243-18','R243-19','R243-59-6-A'],
 'references_inventory':direct,
 'three_fiscal_target_changes':'Outside this social review; require the separately delivered fiscal review and its exact guards. No approval is rebound here.',
 'conditions_for_any_later_adoption':[
   'Re-read exact committed E target bodies after actual registration; compare each against its separate expected future SHA, sources, notes and status. A future view must never be labelled current before that capture.',
   'For all 141, preserve each existing assessment, own source/body/notes/proposal and all other guards exactly; compare per-record audit digest, not only a global ledger file digest.',
   'Allow only the explicitly reviewed L243-7-6 change, the separately approved three fiscal changes and, after their guarded commit, R243-18/R243-19/R243-59. Any unlisted delta blocks renewal.',
   'Replace the three old C R243-17/-18/-19 assessments explicitly with new E analyses, rather than renewing their obsolete justifications.',
   'Reissue only affected reference checks and certificates from the actual post-commit snapshot, including R243-59-6-A where required. All other own bodies remain byte-identical.',
   'Require the captured current policy file hashes to remain exact; no semantic policy-version equivalence is inferred.'],
 'policy_guards':policies,'no_ledger_write':True,'national_savings':None,'semantic_review_by_jurist':False}
dump(D/'compatibility-141.proposed.json',compat)

# Read-only final check of all four E before-images and all 18 full reverse references.
own=[]
for f in [E/'edition001',E/'complement-r243-59/edition001']:
    S=read(f/'source.json'); snap=read(f/'reference-targets.json');rc.check_guards(c,snap)
    for s in S:
        view=rc.view(c,key(s));assert view['source_xml']==s['source_xml'] and view['source_notes_xml']==s['source_notes_xml']
        d=c.execute('select * from drafts where code_id=? and source_id=?',(s['code_id'],s['source_id'])).fetchone()
        prev=s.get('previous_draft')
        assert (d is None) if prev is None else bool(d) and all(d[k]==v for k,v in prev.items() if k!='proposed_sha256')
        own.append({'key':key(s),'number':s['number'],'before_image_exact':True,'state':current(key(s))})
refs=read(E/'complement-r243-59/edition001/R243-59-referrers-inventory.json')['records']
reverse_checks=[]
for r in refs:
    v=rc.view(c,key(r))
    assert v['source_xml']==r['source_xml'] and v['source_notes_xml']==r['source_notes_xml'] and v['proposed_xml']==r['proposed_xml'],r['number']
    reverse_checks.append({'key':key(r),'number':r['number'],'complete_source_notes_effective_text_read':True,'fresh_current_guards':current(key(r))})
c.rollback();c.close()
dump(E/'final-guards.json', {'checked_at':now,'mode':'SQLite mode=ro BEGIN; no writes','before_images':own,
 'reverse_reference_count':len(reverse_checks),'reverse_references':reverse_checks,'policy_guards':policies,
 'not_a_registration':True})
print('Frozen checks:',len(fresh),'records;',len(ledger_checks),'old C audits unchanged; E own',len(own),'; reverse references',len(reverse_checks))
