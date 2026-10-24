"""Capture current bounded semantic findings and text candidates, never register."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, re, sqlite3, sys
import xml.etree.ElementTree as ET

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
sys.path.insert(0, str(ROOT))
from ingest import source_notes
from review_prior import batch_row_sha256, draft_values

def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(x): return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
def fsha(p): return sha(p.read_bytes())
def put(name, value):
    with (OUT/name).open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2); f.write('\n')

packet_names = ['whole-article-packet.json', 'additional-D237-whole-article-packet.json',
                'six-additional-counterparts.json', 'two-procedure-counterparts.json']
packets = {name: json.loads((OUT/name).read_bytes()) for name in packet_names}
articles = [a for rows in packets.values() for a in rows]
by_number = {a['number']: a for a in articles}
assert len(articles) == len(by_number) == 64
input_hashes = {str(OUT/name): fsha(OUT/name) for name in packet_names}
pins = json.loads((ROOT/'runtime/coherence-rollout-20261023T2042Z/resumption-observation-pins-v4.json').read_bytes())
pins['run_exhaustive.py'] = 'd826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
for name, h in pins.items(): assert fsha(ROOT/name) == h, name
policies = {n: pins[n] for n in ['corpus.json', 'policy-coordinations.json',
                                 'site-summaries.json', 'reference-focus-extra.json']}

def fresh_check():
    db = sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro', uri=True, timeout=15)
    db.execute('PRAGMA query_only=ON'); db.execute('BEGIN')
    try:
        for a in articles:
            key = a['code_id'], a['source_id']
            expected = (a['number'], a['source_sha256'], a['source_xml'], a['valid_from'], a['valid_until'])
            assert db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone() == expected, key
            assert source_notes(db, *key) == a['source_NOTA'], key
            assert db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key).fetchone() == tuple(a['draft'][k] for k in ['source_sha256','status','proposed_xml','reason','review_notes']), key
    finally: db.close()

fresh_check()

def anchor(number, field, quote):
    a = by_number[number]
    body = a['source_xml'] if field == 'source_xml' else a['draft']['proposed_xml']
    assert body is not None and quote in body, (number, quote)
    return dict(number=number, code_id=a['code_id'], source_id=a['source_id'], field=field,
                whole_field_sha256=sha(body.encode()), exact_quote=quote,
                start=body.index(quote), end=body.index(quote)+len(quote))

findings = [
    dict(id='automatic-inspection-transmission', qualification='contradiction_effective_entre_propositions',
         articles=['L2371-5','R2372-17','R2373-5','D2372-13','L8112-1','L8113-4'],
         anchors=[anchor('L2371-5','proposed_xml',"aucune transmission systématique à l'inspection du travail n'est exigée au seul titre de la constitution de la société issue de l'opération transfrontalière"),
                  anchor('R2372-17','proposed_xml',"sont transmis à l'agent de contrôle de l'inspection du travail"),
                  anchor('R2372-17','proposed_xml','Cette transmission est effectuée une seule fois'),
                  anchor('R2373-5','proposed_xml',"La transmission des éléments relatifs à la participation des salariés demeure régie par l'article R. 2372-17"),
                  anchor('D2372-13','proposed_xml',"aucune transmission systématique de ces informations à l'agent de contrôle de l'inspection du travail n'est exigée")],
         assessment="La proposition législative supprime tout envoi automatique des noms et des justificatifs au seul titre de la constitution ; le règlement proposé exige encore un envoi, même unique, et l'autre règlement le maintient après abrogation. Leur rédaction n'est donc pas convergente. D2372-13 est déjà coordonné. La hiérarchie des normes empêche de déduire que le règlement pourrait juridiquement recréer l'obligation contre la loi future. Les pouvoirs légaux de contrôle, les documents existants, l'information des salariés et le contrôle commercial demeurent autonomes.",
         action='Deux candidats réglementaires préparés ensemble, à la même borne future que L2371-5 ; aucune nouvelle coupe autonome comptée.'),
    dict(id='protected-representatives-operation-scope', qualification='coordination_necessaire',
         articles=['L2371-1','L2374-4','L2411-1','L2411-12','L2413-1','L2421-3','L2421-4','L2421-10'],
         anchors=[anchor('L2411-1','proposed_xml',"représentant au comité de la société issue d'une opération transfrontalière"),
                  anchor('L2411-12','source_xml',"représentant au comité de la société issue d'une fusion transfrontalière"),
                  anchor('L2413-1','proposed_xml','7° ter Membre du groupe spécial de négociation et représentant au comité de la société issue de la fusion transfrontalière'),
                  anchor('L2421-4','source_xml','2° ter Membre du groupe spécial de négociation et représentant au comité de la société issue de la fusion transfrontalière')],
         assessment="L2411-1 a déjà choisi et explicité une extension protectrice aux autres opérations et sa contrainte patronale corrélative. Trois contreparties, dont L2421-4 identifié lors de cette lecture, restent limitées à la fusion. Le groupe de négociation bénéficie déjà d'une rédaction générique dans L2411-12 ; L2374-4 protège d'autres organes. Il serait faux d'en déduire la disparition de toutes les protections. Préparer l'alignement ciblé des trois catégories de comité et de leur procédure, sans remplacer toutes les occurrences fusion du titre VII.",
         action="Trois candidats complets : autorisation de licenciement, décision de mission et rattachement procédural, avec leurs faits générateurs propres et les mêmes protections des droits antérieurs. Ce n'est pas une baisse d'obligations ; pas d'extension pénale implicite."),
    dict(id='seat-allocation-reference', qualification='coordination_deja_presente_dans_la_proposition',
         articles=['L2373-5','L2373-6','L2373-7','L2373-8'],
         anchors=[anchor('L2373-8','proposed_xml','L. 2373-5 et L. 2373-6')],
         assessment="Les dispositions entières 5/6 déterminent les sièges, 7 la désignation ; la proposition 8 corrige le renvoi aux 5/6 et protège les mandats antérieurs. Convergence limitée constatée, aucun signalement global administrativement résolu."),
    dict(id='specific-fusion-exceptions', qualification='difference_de_champ',
         articles=['L2371-2','L2371-3','L2372-4','L2374-1','L2372-6-1','L2374-2'],
         assessment="Les exemptions, renonciations, seuils de décision et options propres à la fusion ne sont pas rendus généraux par l'extension de protection du comité. Les garanties de niveau équivalent pour transformation/scission et la protection de quatre ans des opérations internes ultérieures demeurent ; pas de substitution globale fusion/opération."),
    dict(id='penal-scope', qualification='point_non_verifiable_en_totalite', articles=['L2375-1'],
         assessment="Le texte pénal maintient un champ fusion et la proposition retire l'emprisonnement en conservant amende et loi plus douce. Ne pas étendre une incrimination par simple coordination du statut protecteur. Articulation européenne et régime des autres opérations à qualifier séparément."),
    dict(id='negotiation-start', qualification='articulation_preexistante_a_qualifier',
         articles=['L2352-9','D2352-14','D2372-14'],
         assessment="Le législatif fait commencer les négociations dès constitution du groupe ; les deux règlements sources font partir les six mois de la première réunion. Les propositions de liberté de support ne créent pas ce décalage. Il n'autorise pas à retarder les négociations. Pas de contradiction nouvelle des propositions établie sur ce seul rapprochement ; calendrier européen et articulation exacte à vérifier."),
    dict(id='commercial-reference-scope', qualification='renvoi_exterieur_a_qualifier',
         articles=['R2372-17','R2373-5','D2373-1'],
         assessment="L229-3 commerce a été lu en entier sur la page officielle datée du 13 mai 2026 : société européenne formée par fusion et implication au titre V du code du travail. Le renvoi des règlements du titre VII nécessite donc une qualification de champ avec les dispositions commerciales propres aux autres opérations. La page exacte au 18 octobre était inaccessible via l'outil ; aucune équivalence ou actualisation au-delà de la page obtenue n'est certifiée. La correction des envois automatiques conserve ce renvoi et les formalités commerciales autonomes ; elle ne prétend pas résoudre cette seconde question.",
         external_evidence='official-commerce-retrieval.json')]

candidates = []
def add(number, edits, appendix, reason, impact):
    a = by_number[number]; before = a['draft']['proposed_xml'] or a['source_xml']; after = before
    for old, new in edits:
        assert after.count(old) == 1, (number, old)
        after = after.replace(old, new)
    after += appendix
    ET.fromstring('<body>'+after+'</body>')
    candidates.append(dict(number=number, code_id=a['code_id'], source_id=a['source_id'],
        kind='parental_text_candidate_not_registration_answer', source_sha256=a['source_sha256'],
        whole_beforeimage=copy.deepcopy(a['draft']), source_NOTA=a['source_NOTA'],
        valid_from=a['valid_from'],valid_until=a['valid_until'],
        exact_edits=[dict(before=x,after=y) for x,y in edits], appended_xml=appendix,
        proposed_xml=after, proposed_xml_sha256=sha(after.encode()),
        proposed_reason=reason, substantive_impact_plan=impact,
        ordinary_full_validation_passed=False, registered=False))

protection = "Coordination de l'extension protectrice déjà décidée dans L2411-1 ; contrainte patronale corrélative explicitement conservée, aucun allègement à compter. Ne pas importer le préavis de quinze jours ou l'indemnité ordinaire dans le statut protecteur ; ne pas étendre une incrimination."
add('L2411-12',[("issue d'une fusion transfrontalière", "issue d'une opération transfrontalière")],
    "<p>L'extension de la protection des représentants au comité de la société aux opérations autres que les fusions s'applique aux licenciements engagés à compter de l'entrée en vigueur de la loi portant la présente réforme, pour les contrats antérieurs comme pour les contrats nouveaux. Elle ne réduit aucune protection déjà applicable sur un autre fondement.</p>\n",
    "Aligner le comité sur le champ protecteur de L2411-1 ; les quatre catégories et l'autorisation préalable de l'inspecteur restent intégrales.", protection)
add('L2413-1',[("7° ter Membre du groupe spécial de négociation et représentant au comité de la société issue de la fusion transfrontalière", "7° ter Membre du groupe spécial de négociation et représentant au comité de la société issue d'une opération transfrontalière")],
    "\n<p>L'extension du 7° ter aux opérations autres que les fusions s'applique aux interruptions de mission et aux notifications de non-renouvellement intervenant à compter de l'entrée en vigueur de la loi portant la présente réforme, pour les contrats antérieurs comme pour les contrats nouveaux. Elle ne réduit aucune protection déjà applicable sur un autre fondement et ne permet aucune conclusion, aucun renouvellement ni aucune reconduction à durée déterminée interdits par les dispositions précédentes.</p>\n",
    "Coordonner le 7° ter sans déplacer les dix-sept catégories ni les quatre paragraphes déjà proposés sur mission/emploi, autorisations distinctes, intermissions, droits anciens, conversion et aides futures.", protection)
add('L2421-4',[("2° ter Membre du groupe spécial de négociation et représentant au comité de la société issue de la fusion transfrontalière", "2° ter Membre du groupe spécial de négociation et représentant au comité de la société issue d'une opération transfrontalière")],
    "<p>L'extension du 2° ter aux opérations autres que les fusions s'applique aux licenciements engagés à compter de l'entrée en vigueur de la loi portant la présente réforme, pour les contrats antérieurs comme pour les contrats nouveaux. Elle ne réduit aucune protection déjà applicable sur un autre fondement.</p>\n",
    "Coordonner aussi le rattachement procédural, et pas seulement les deux listes matérielles. Les six catégories et le régime de L2421-3, y compris saisine directe sans CSE, compétence, mise à pied et annulation de ses effets en cas de refus, sont conservés.", protection)

r = by_number['R2372-17']['draft']['proposed_xml']
new_first = by_number['R2372-17']['source_xml'].replace('<p>Les éléments fournis', "<p>À compter de l'entrée en vigueur de la loi supprimant les transmissions systématiques prévues à l'article L. 2371-5, les éléments fournis")
new_first = new_first.replace("sont transmis à l'agent de contrôle de l'inspection du travail.", "ne font l'objet d'aucune transmission systématique à l'agent de contrôle de l'inspection du travail au seul titre de la constitution de la société issue de l'opération transfrontalière.")
new_r = new_first + "<p>Cette dispense couvre la société, la filiale ou l'établissement concernés et leurs dirigeants, que les modalités de participation résultent d'un accord ou des dispositions subsidiaires. Aucun envoi, déclaration ou attestation de remplacement n'est exigé à ce titre. Les obligations d'information des salariés et de leurs représentants, les conditions légales de constitution et d'immatriculation et le contrôle de la régularité des modalités de participation demeurent applicables. Les pouvoirs légaux de contrôle et de présentation ou de communication des documents dans le cadre de ces contrôles ne sont pas modifiés.</p>\n<p>La dispense s'applique également aux transmissions non encore effectuées à cette date pour les opérations déjà engagées ou réalisées. Les transmissions régulièrement effectuées ne sont pas à refaire. La régularité des autres actes et les droits et recours nés avant cette date restent régis par les règles qui leur étaient applicables, sous réserve de l'application de la loi répressive plus douce.</p>\n"
add('R2372-17',[(r,new_r)],'',
    "Retirer l'envoi systématique encore exigé, même unique, conformément à L2371-5 proposé, tout en conservant les pièces et conditions de participation, le contrôle commercial autonome et les pouvoirs légaux d'inspection.",
    "Même mesure que la suppression des envois automatiques de L2371-5 ; coordination nécessaire, aucune seconde baisse autonome ou économie chiffrée. L229-3 commerce et le cadre européen demeurent à qualifier, sans suppression de leur contrôle.")
old = by_number['R2373-5']['draft']['proposed_xml']
new = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les transmissions systématiques prévues à l'article L. 2371-5. L'absence de transmission systématique à l'inspection du travail prévue à l'article R. 2372-17 s'applique également lorsque les modalités de participation résultent des dispositions subsidiaires, y compris aux transmissions non encore effectuées pour des opérations déjà engagées ou réalisées. Aucun envoi, déclaration ou attestation de remplacement n'est exigé à ce titre. Les transmissions régulièrement effectuées conservent leurs effets et ne sont pas renouvelées au seul motif de cette abrogation. Les pouvoirs légaux de contrôle, les conditions de constitution et d'immatriculation, le contrôle de la régularité des modalités de participation et l'information des salariés et de leurs représentants demeurent applicables. Les contrôles et recours relatifs aux opérations antérieures demeurent ouverts dans les conditions qui leur sont applicables, sous réserve de l'application de la loi répressive plus douce.</p>"
add('R2373-5',[(old,new)],'',
    "Maintenir l'abrogation du doublon sans conserver par son renvoi une transmission automatique contraire à L2371-5. Même borne future et même dispense des envois encore pendants que R2372-17 ; contrôles et recours préservés.",
    "Coordination indissociable de R2372-17 et L2371-5 ; aucune double comptabilisation de formalité supprimée ni retrait de la participation ou du contrôle commercial.")

keys = {(c['code_id'],c['source_id']) for c in candidates}
owners = {}; paths = sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
batch_hashes = {}
for p in paths:
    b = p.read_bytes(); batch_hashes[str(p)] = sha(b)
    for i, row in enumerate(json.loads(b)):
        key = row['code_id'], row['source_id']
        if key not in keys: continue
        assert key not in owners, key
        a = next(a for a in articles if (a['code_id'],a['source_id']) == key)
        assert draft_values(row) == tuple(a['draft'][k] for k in ['source_sha256','status','proposed_xml','reason','review_notes']), key
        owners[key] = dict(code_id=key[0],source_id=key[1],owner_path=str(p),owner_index=i,
                           owner_file_sha256=sha(b),whole_owner_row=row,whole_owner_row_sha256=batch_row_sha256(row))
assert set(owners) == keys
reg_p = ROOT/'registered-batches.json'; reg_b = reg_p.read_bytes(); registry = json.loads(reg_b)
for key, owner in owners.items():
    reg = registry['|'.join(key)]; row = owner['whole_owner_row']
    assert reg == dict(source_sha256=row['source_sha256'],proposed_sha256=sha((row['proposed_xml'] or '').encode())), key
    owner['registry_entry'] = reg

fresh_check()
for p,h in input_hashes.items(): assert fsha(Path(p)) == h, p
for p,h in batch_hashes.items(): assert fsha(Path(p)) == h, p
assert reg_p.read_bytes() == reg_b
assert paths == sorted(p for p in (ROOT/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name))
for name,h in pins.items(): assert fsha(ROOT/name) == h, name

coverage = []
for a in articles:
    coverage.append(dict(number=a['number'],code_id=a['code_id'],source_id=a['source_id'],
       source_sha256=a['source_sha256'],source_body_sha256=sha(a['source_xml'].encode()),
       source_NOTA_sha256=sha(a['source_NOTA'].encode()),valid_from=a['valid_from'],valid_until=a['valid_until'],
       five_field_draft_sha256=sha(canonical(a['draft'])),source_proposal_reason_review_notes_NOTA_read_in_full=True,
       source_and_five_field_live_recheck_twice=True))
put('candidate-texts.json',candidates)
put('whole-owner-beforeimages.json',list(owners.values()))
put('findings-qualified.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),findings=findings,
    whole_articles_read=64,proposed_text_contradiction_groups_established=1,administratively_resolved_findings=0,
    semantic_scope_limited=True,global_legal_validation=False,jurist_validation=False))
put('full-read-coverage-and-live-guards.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
    sqlite_mode='ro',query_only=True,current64_guards_rechecked_in_two_transactions=True,
    articles=coverage,four_current_formal_policies=policies,all77_pins_checked=pins,
    old_limited_review_inheritance_not_forced=True,registry_sha256=sha(reg_b),
    all_active_batch_hashes_stable=batch_hashes))
put('CONTROL.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),state='SEMANTIC_QUALIFICATION_AND_FIVE_TEXT_CANDIDATES_PREPARED_NOT_REGISTERED',
    full_articles_read=64,proposed_text_contradiction_groups=1,protection_coordination_includes_L2421_4=True,
    five_current_full_owner_rows_and_registry_captured=True,ordinary_full_validation_passed=False,
    canonical_mutations=0,models_launched=0,completed_markers_changed=0,response_replay=False,
    must_revalidate=['all current source/NOTA/version and five-field guards',
      'whole owner rows and registry under actual shared reservations',
      'whole target texts and current four policies',
      'benefit and substantive-impact metadata with correct same-measure accounting',
      'every configured reference assessment, including external limits',
      'ordinary full answer and registration validation',
      'durable full archives before commit; DB/batch/registry/completed afterwards',
      'reference and semantic convergence across all affected texts'],
    no_global_or_jurist_completion=True,
    open_limits=['European whole instruments and later versions not verified',
      'Commerce L229-3 official page obtained at 2026-05-13 only; external cross-border scheme not certified',
      'penal scope not broadened by inferred coordination',
      'pre-existing negotiation start articulation still open',
      'remaining five-code/four-annex review work and three normative reserves remain open']))
print(json.dumps(dict(whole_articles=64,findings=len(findings),text_candidates=len(candidates),
    source_NOTA_bounds_five_fields_stable=True,whole_owner_and_registry_verified=True,canonical_mutations=0),ensure_ascii=False))
