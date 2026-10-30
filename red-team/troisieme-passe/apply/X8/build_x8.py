"""Build apply/X8 and its variant folders (<owner>y) from production texts, read-only.

Sixth audit (E01-E10), 13 gross defects: OGA chapter of annex II (371 A to 371 bis N), FSV chapter (R/D135),
CGI 244 bis and 244 bis A, 80 quindecies and 163 quinquies C, CSS R371-9 to R371-11, L311-5, D160-16,
D752-2-3, L759-23 (new), annex III 46 quater-0 ZF and ZD, CCH R165-2, R165-16, L165-5 and L165-6.
Nothing is written in production: the database is opened with mode=ro and query_only.
"""
import json, sqlite3, html, re, glob
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path('/Users/alexandremasmejean/Coding/libererlafrance/third-pass/apply')
db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
db.execute('pragma query_only=1')

CGI = 'LEGITEXT000006069577'; A2 = 'LEGITEXT000006069569'; A3 = 'LEGITEXT000006069574'
CSS = 'LEGITEXT000006073189'; CCH = 'LEGITEXT000006074096'
POLICY = 'editorial_direction_2026_10_19'
AI = ' Revue IA, sans validation par un juriste.'
OWNER = json.loads((HOME / 'assignment.json').read_text())['owner']


def plain(v):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', v or '')).split())


def cur(code, sid):
    src = db.execute('SELECT content_xml FROM articles WHERE code_id=? AND id=?', (code, sid)).fetchone()[0]
    d = db.execute('SELECT status, proposed_xml, reason, review_notes FROM drafts WHERE code_id=? AND source_id=?',
                   (code, sid)).fetchone()
    if d is None:
        return dict(source=src, status=None, proposed=None, reason=None, notes=None)
    return dict(source=src, status=d[0], proposed=d[1], reason=d[2], notes=d[3])


ROWS = {}
for f in glob.glob(str(PROD / 'batches/*/*.json')):
    try:
        data = json.loads(Path(f).read_text())
    except Exception:
        continue
    if isinstance(data, list):
        for r in data:
            if isinstance(r, dict) and 'source_id' in r and 'code_id' in r:
                ROWS[(r['code_id'], r['source_id'])] = r


def clean_html(xml):
    """Source HTML as an allowed proposal body: no attributes, paragraphs instead of bare <br/> lines."""
    x = re.sub(r'<(p|div|span|sup|sub|b|i|em|strong|u|li|ul|ol|blockquote)\s+[^>]*>', r'<\1>', xml or '')
    if '<p' not in x:
        parts = [p.strip() for p in re.split(r'(?:<br\s*/?>\s*)+', x) if p.strip()]
        x = ''.join(f'<p>{p}</p>' for p in parts)
    return x.strip()


def effect(kind, mid, desc, before, after, unit, pop, trans, repl, sq, pq):
    return dict(kind=kind, measure_id=mid, description=desc, before=before, after=after, unit=unit,
                affected_population=pop, conditions_and_transition=trans, replacement_or_new_burdens=repl,
                source_quote=sq, proposed_quote=pq)


def impact(cls, assessment, scope, burdens, effects):
    return dict(version=1, classification=cls, assessment=assessment, scope_limitations=scope,
                new_burdens_review=burdens, effects=effects)


def check(code, sid, proposed, imp):
    src = plain(cur(code, sid)['source'])
    prop = plain(proposed) if proposed else src
    for e in imp['effects']:
        assert plain(e['source_quote']) in src, (sid, 'source_quote', e['source_quote'])
        assert plain(e['proposed_quote']) in prop, (sid, 'proposed_quote', e['proposed_quote'])
    for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(imp[k]) >= 40, (sid, k)


def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:90], text.count(old))
    return text.replace(old, new)


GROUPS = {}


def group_for(code, sid):
    own = OWNER.get(f'{code}|{sid}')
    return 'X8' if own is None else own + 'y'


def add(obj, code, sid, proposed, reason, notes, overrides, mode='replace', loophole=False):
    imp = overrides.get('substantive_impact')
    if imp is None and mode == 'replace':
        imp = (ROWS.get((code, sid)) or {}).get('substantive_impact')
    if isinstance(imp, dict) and (proposed is not None or overrides.get('status') != 'retained_unchanged'):
        check(code, sid, proposed, imp)
    item = dict(objection=obj, code_id=code, source_id=sid, mode=mode, proposed_xml=proposed, reason=reason,
                review_notes=notes, overrides=overrides)
    if loophole:
        item['loophole_closure'] = True
    g = group_for(code, sid)
    assert all(c['source_id'] != sid for c in GROUPS.get(g, [])), sid
    GROUPS.setdefault(g, []).append(item)


# ====================================================================================== 1. OGA, annex II 371 A to 371 bis N
LAW = ("par le 6° de l'article 11 de la loi n° 2025-127 du 14 février 2025 de finances pour 2025 "
       "(« Les articles 1649 quater C à 1649 quater O sont abrogés »)")


def basis(subject, plural=True):
    verb = 'ont été abrogés' if plural else 'a été abrogé'
    return f"{subject} {verb}, avec l'ensemble des articles 1649 quater C à 1649 quater O de ce code, {LAW}."


B_C = basis("Les articles 1649 quater C et 1649 quater E du code général des impôts, qui prévoyaient l'agrément des "
            "centres de gestion et leurs missions,")
B_EBIS = basis("L'article 1649 quater E bis du code général des impôts, pour l'application duquel était organisée "
               "l'information de la clientèle des adhérents des centres de gestion agréés,", plural=False)
B_F = basis("Les articles 1649 quater F et 1649 quater H du code général des impôts, qui prévoyaient l'agrément des "
            "associations de membres des professions libérales et de titulaires de charges et offices et leurs missions,")
B_K = basis("Les articles 1649 quater C, 1649 quater F et 1649 quater K ter du code général des impôts, qui prévoyaient "
            "les agréments des centres de gestion, des associations agréées et des organismes mixtes de gestion,")
B_L = basis("Les articles 1649 quater L et 1649 quater M du code général des impôts, qui prévoyaient l'autorisation et "
            "la convention des professionnels de l'expertise comptable,")
NOREPL = "Aucun agrément, déclaration ni condition de remplacement n'est institué."


def p3(extra='', regime="l'agrément"):
    return (f"Les droits et obligations nés au titre des périodes antérieures à la suppression de {regime} restent régis "
            "par les dispositions alors applicables, y compris les prescriptions, restitutions et recours qui s'y "
            "rapportent. Les sanctions non définitives fondées sur les seules obligations supprimées relèvent de la loi "
            f"répressive plus douce. {extra}Les avantages fiscaux ayant un fondement légal autonome ne sont pas affectés. "
            "La présente abrogation ne fait revivre, pour la période écoulée depuis le 16 février 2025, aucune obligation "
            "que la loi a supprimée.")


OGA_SCOPE = ("Les arrêtés d'application, modèles de convention et formulaires ne sont pas au corpus. Le nombre de "
             "situations antérieures encore en cours n'est pas connu. Le texte JORF de l'article 11 de la loi "
             "n° 2025-127 est cité d'après la lecture faite par le groupe M05 le 29 octobre 2026.")
OGA_BURDEN = ("Aucune charge nouvelle identifiée : l'abrogation n'ajoute ni agrément, ni convention, ni déclaration, ni "
              "pièce, ni délai ; les obligations ayant un fondement autonome restent dans leur champ.")
OGA_NOTE = (" Correction de la troisième passe (objection {obj}, sixième audit, groupe X8) : abrogation pour l'avenir "
            "de l'article, dont le fondement législatif ({law}) est abrogé depuis le 16 février 2025 par l'article 11 de "
            "la loi n° 2025-127, afin de rendre cohérente toute la section des articles 371 A à 371 bis N ; même "
            "transition que les abrogations déjà faites (371 A, 371 E, 371 M, 371 Q, 371 X, 371 Z bis, 371 Z quater, "
            "371 bis A, 371 bis J), sans formalité de remplacement. Les mentions des présentes notes qui supposent le "
            "maintien de l'agrément, de son instruction, de sa durée, de son retrait ou du conventionnement sont "
            "périmées." + AI)
OGA_REASON = ("Coordination nécessaire : {what} {verb} {law} du code général des impôts, abrogé{s} avec tout le régime "
              "des centres de gestion, associations et organismes mixtes agréés et des professionnels conventionnés par le "
              "6° de l'article 11 de la loi n° 2025-127. {prev}L'article est abrogé pour l'avenir, avec la même transition "
              "que les articles déjà abrogés de la section, sans formalité ni condition de remplacement ; les droits et "
              "obligations des périodes antérieures restent régis par les règles alors applicables.")


def oga(obj, sid, bas, p2, extra, scope, eff_desc, before, after, pop, sq, pq, what, law, prev='', plural=True,
        regime="l'agrément", benefit=None, mid=None, verb='exécutait'):
    c = cur(A2, sid)
    proposed = (f"<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente réforme. {bas}</p>"
                f"<p>{p2}</p><p>{p3(extra, regime)}</p>")
    num = db.execute('SELECT number FROM articles WHERE code_id=? AND id=?', (A2, sid)).fetchone()[0]
    mid = mid or ('oga-' + re.sub(r'[^a-z0-9]+', '-', num.lower()).strip('-') + '-abrogation-fondement-abroge')
    imp = impact('coordination_only',
                 f"Abrogation, sans formalité de remplacement, d'un article d'exécution dont le fondement législatif "
                 f"({law} du code général des impôts) a été abrogé {LAW}.",
                 OGA_SCOPE, OGA_BURDEN,
                 [effect('coordination', mid, f"Fin d'un régime réglementaire privé de base légale le 16 février 2025 : {eff_desc}",
                         before, after, 'legal_duty', pop,
                         "À l'entrée en vigueur de la réforme ; périodes antérieures régies par les règles alors applicables ; "
                         "loi répressive plus douce pour les sanctions non définitives.",
                         "Aucun agrément, convention, déclaration ni formalité de remplacement.", sq, pq)])
    s = '' if not plural else 's'
    if what.startswith('les '):
        verb = {'exécutait': 'exécutaient', 'dépendait de': 'dépendaient de'}.get(verb, verb)
    reason = OGA_REASON.format(what=what, verb=verb, law=law, s=s, prev=prev)
    notes = (c['notes'] or '').rstrip() + OGA_NOTE.format(obj=obj, law=law)
    ov = dict(status='rewrite_draft', classification='coordination_only', change_type='full_repeal',
              repeal_policy_id=POLICY, repeal_scope=scope, reform_policy_id=None, removed_provisions=None,
              substantive_impact=imp,
              benefit_review=benefit or ("Aucune faveur en vigueur n'est retirée : le régime d'agrément et ses avantages "
                                         "ont été supprimés par la loi ; les avantages fiscaux ayant un fondement autonome "
                                         "et les droits des périodes antérieures sont préservés."))
    add(obj, A2, sid, proposed, reason, notes, ov)


E135, E223, E240 = 'AUDIT6-E135', 'AUDIT6-E223', 'AUDIT6-E240'
CENTRES = "Centres de gestion et leurs adhérents industriels, commerçants, artisans et agriculteurs."
ASSOS = "Associations de membres des professions libérales et de titulaires de charges et offices et leurs adhérents."
MIXTES = "Organismes mixtes de gestion et leurs adhérents."
PREV_REFORM = ("La proposition antérieure réformait au fond un régime dont la base légale avait déjà disparu, en le "
               "présentant comme maintenu. ")

# ---- centres de gestion
oga(E135, 'LEGIARTI000044174720', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucune qualité de centre agréé n'est requise ni reconnue sur le fondement du présent "
    "article pour fournir les services d'assistance en matière de gestion qu'il énumérait ; leur fourniture n'est "
    "restreinte par aucune disposition de la présente section. " + NOREPL,
    "Les prestations déjà convenues restent régies par les contrats qui les prévoient. ",
    "Abrogation de la faculté de services réservée aux centres bénéficiant de l'agrément de l'article 1649 quater C du CGI, abrogé en 2025, sans restreindre la fourniture de ces services.",
    "faculté de services des centres agréés.",
    "Faculté de fournir des services de gestion à toute entreprise, réservée aux centres agréés.",
    "Plus de qualité d'agréé requise ; aucune restriction de ces services dans la section.",
    CENTRES,
    "Les centres bénéficiant de l'agrément prévu par l'article 1649 quater C du code général des impôts peuvent fournir à toute entreprise",
    "leur fourniture n'est restreinte par aucune disposition de la présente section",
    "la faculté de services des centres agréés", "l'article 1649 quater C", plural=False, verb='dépendait de',
    benefit="La faculté de fournir les six catégories de services n'est pas restreinte : elle était liée à un agrément supprimé par la loi, et aucune limite d'objet ne subsiste dans la section après l'abrogation de 371 A.")

oga(E135, 'LEGIARTI000033238661', B_C,
    "À compter de cette date, aucun nombre minimal d'adhérents ni aucun nombre minimal de contrôles par bureau "
    "secondaire ne peut être exigé sur le fondement du présent article. " + NOREPL,
    "Les dispenses dont bénéficiaient les centres et bureaux établis en Corse, en Guadeloupe, en Guyane, en Martinique, à Mayotte et à La Réunion restent acquises pour les périodes antérieures. ",
    "Abrogation des seuils d'adhérents et de contrôles par bureau secondaire des centres de gestion agréés, dont l'agrément (CGI 1649 quater C et E) est abrogé en 2025.",
    "seuils d'adhérents des centres.",
    "Seuils de 500 puis 1 000 adhérents et de 500 adhérents et contrôles par bureau secondaire.",
    "Aucun seuil exigé sur ce fondement ; dispenses territoriales antérieures acquises.",
    CENTRES, "Le nombre des adhérents d'un centre doit être au minimum de cinq cents personnes physiques ou morales",
    "aucun nombre minimal d'adhérents ni aucun nombre minimal de contrôles par bureau secondaire ne peut être exigé",
    "les seuils d'adhérents des centres", "les articles 1649 quater C et 1649 quater E",
    prev="La proposition antérieure, déjà abrogative, supposait encore l'octroi, le renouvellement et le maintien d'un agrément. ")

oga(E135, 'LEGIARTI000033238655', B_C,
    "À compter de cette date, aucune convention d'assistance technique ne peut être exigée des centres sur le fondement "
    "du présent article, et aucun refus de convention ne peut y être fondé. Aucune convention, déclaration ni formalité "
    "de remplacement n'est instituée. La répression du refus collectif de l'impôt prévue à l'article 1747 du code "
    "général des impôts demeure applicable.",
    "Les conventions conclues antérieurement, les créances et les droits des tiers qui en résultent restent régis par leurs stipulations pour les périodes auxquelles elles se rapportent. ",
    "Abrogation de la convention d'assistance technique entre centres de gestion et administration fiscale et du refus de convention, fondés sur CGI 1649 quater E abrogé en 2025.",
    "convention d'assistance des centres.",
    "Convention d'assistance technique avec l'administration, rendue facultative par la proposition antérieure, et refus de convention.",
    "Aucune convention ni refus sur ce fondement ; article 1747 du CGI réservé.",
    CENTRES, "les centres doivent conclure avec l'administration fiscale une convention précisant le rôle du ou des agents",
    "aucune convention d'assistance technique ne peut être exigée des centres sur le fondement du présent article",
    "la convention d'assistance des centres", "l'article 1649 quater E", plural=False, prev=PREV_REFORM)

oga(E135, 'LEGIARTI000033238650', B_C,
    "À compter de cette date, aucune condition relative à la situation fiscale ou pénale des personnes qui dirigent ou "
    "administrent un centre, aucun certificat ni aucune attestation ne peut être exigé sur le fondement du présent "
    "article, faute d'agrément à délivrer ou à maintenir. Les sanctions, interdictions et incapacités prononcées sur un "
    "autre fondement demeurent applicables. " + NOREPL, "",
    "Abrogation des conditions d'intégrité des dirigeants exigées pour l'agrément des centres de gestion (CGI 1649 quater C abrogé en 2025) et de leurs certificats.",
    "conditions d'intégrité des dirigeants des centres.",
    "Conditions fiscales et pénales des dirigeants vérifiées pour l'agrément, sans certificat dans la proposition antérieure.",
    "Aucune condition sur ce fondement ; sanctions et incapacités autonomes réservées.",
    CENTRES, "que les personnes qui les dirigent ou les administrent ont respecté leurs obligations déclaratives et de paiement",
    "aucune condition relative à la situation fiscale ou pénale des personnes qui dirigent ou administrent un centre",
    "les conditions d'intégrité des dirigeants des centres", "l'article 1649 quater C", plural=False, prev=PREV_REFORM)

oga(E135, 'LEGIARTI000033238633', B_C,
    "À compter de cette date, aucune stipulation statutaire relative à la publicité, à la mention de l'agrément, à "
    "l'information de l'administration sur les statuts et les dirigeants, à l'assurance de responsabilité civile "
    "professionnelle, à l'information des adhérents en cas de retrait, au montant des cotisations ni à la sous-traitance "
    "des missions de contrôle ne peut être exigée sur le fondement du présent article. Les règles générales relatives à "
    "la publicité, à l'information loyale et au secret professionnel demeurent applicables. " + NOREPL,
    "Les contrats d'assurance en cours restent régis par leurs stipulations. ",
    "Abrogation des clauses statutaires obligatoires des centres de gestion agréés (publicité, mention d'agrément, assurance, cotisation, sous-traitance), liées à l'agrément abrogé en 2025.",
    "clauses statutaires obligatoires des centres.",
    "Sept engagements statutaires obligatoires des centres agréés.",
    "Aucune clause exigée sur ce fondement ; règles générales de publicité et de secret réservées.",
    CENTRES, "Les statuts des centres doivent contenir des stipulations selon lesquelles les centres s'engagent",
    "aucune stipulation statutaire relative à la publicité, à la mention de l'agrément",
    "les clauses statutaires des centres agréés", "les articles 1649 quater C et 1649 quater E", prev=PREV_REFORM,
    benefit="La faculté de cotisation réduite n'est pas retirée : les centres restent libres de fixer leurs cotisations ; seule disparaît l'obligation de cotisation identique attachée à l'agrément.")

oga(E135, 'LEGIARTI000006295036', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucun engagement statutaire spécifique ne peut être exigé sur le fondement du présent "
    "article. Les informations recueillies par les centres, y compris au titre des périodes antérieures, demeurent "
    "couvertes par les obligations de secret professionnel et de confidentialité qui leur sont applicables par ailleurs, "
    "et les engagements de secret déjà souscrits conservent leurs effets pour ces informations. " + NOREPL, "",
    "Abrogation de l'engagement statutaire des centres de gestion agréés d'exiger le secret de leurs collaborateurs, lié à l'agrément abrogé en 2025, sans lever le secret applicable aux informations recueillies.",
    "engagement statutaire de secret des centres.",
    "Engagement statutaire d'exiger le secret professionnel des collaborateurs.",
    "Plus d'engagement statutaire ; secret applicable par ailleurs et engagements souscrits conservés.",
    CENTRES, "Les centres s'engagent à exiger de toute personne collaborant à leurs travaux le respect du secret professionnel.",
    "demeurent couvertes par les obligations de secret professionnel et de confidentialité qui leur sont applicables par ailleurs",
    "l'engagement de secret des centres agréés", "l'article 1649 quater C", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ")

oga(E135, 'LEGIARTI000033238629', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucune demande d'agrément ne peut être remise ni instruite, et aucune pièce ni aucun "
    "récépissé ne peut être exigé ou délivré sur le fondement du présent article ; les demandes encore pendantes sont "
    "sans objet. " + NOREPL, "",
    "Abrogation du dépôt des demandes d'agrément des centres de gestion, de leurs pièces et du récépissé, l'agrément de CGI 1649 quater C étant abrogé en 2025.",
    "demande d'agrément des centres.",
    "Dépôt d'une demande d'agrément avec dossier de pièces et récépissé.",
    "Aucune demande, pièce ni récépissé sur ce fondement.",
    CENTRES, "Les demandes d'agrément sont remises au directeur départemental ou, le cas échéant, régional des finances publiques du département dans lequel le centre de gestion a son siège.",
    "aucune demande d'agrément ne peut être remise ni instruite",
    "la demande d'agrément des centres", "l'article 1649 quater C", plural=False, prev=PREV_REFORM)

oga(E135, 'LEGIARTI000033238627', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucune décision d'agrément ne peut être prise sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la compétence du directeur régional pour l'agrément des centres de gestion, l'agrément de CGI 1649 quater C étant abrogé en 2025.",
    "décision d'agrément des centres.",
    "Décision d'agrément prise par le directeur régional des finances publiques.",
    "Aucune décision d'agrément sur ce fondement.",
    CENTRES, "La décision d'agrément est prise par le directeur régional des finances publiques",
    "aucune décision d'agrément ne peut être prise sur le fondement du présent article",
    "la compétence de décision d'agrément des centres", "l'article 1649 quater C", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ")

oga(E135, 'LEGIARTI000033238621', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucun délai d'instruction ne court et aucune acceptation tacite d'une demande d'agrément "
    "ne peut naître sur le fondement du présent article. " + NOREPL,
    "Les décisions de refus antérieures, leur motivation et les recours qui s'y rapportent conservent leur régime. ",
    "Abrogation du délai d'instruction et de l'acceptation tacite des demandes d'agrément des centres de gestion, l'agrément de CGI 1649 quater C étant abrogé en 2025.",
    "délai d'instruction et acceptation tacite.",
    "Délai d'instruction, ramené à deux mois par la proposition antérieure, et acceptation tacite de l'agrément.",
    "Aucun délai ni acceptation tacite sur ce fondement.",
    CENTRES, "L'absence de décision dans le délai fixé vaut acceptation de la demande.",
    "aucune acceptation tacite d'une demande d'agrément ne peut naître sur le fondement du présent article",
    "l'instruction des demandes d'agrément des centres", "l'article 1649 quater C", plural=False, prev=PREV_REFORM)

oga(E135, 'LEGIARTI000006295052', basis("L'article 1649 quater C du code général des impôts, qui prévoyait l'agrément "
                                          "des centres de gestion,", plural=False),
    "À compter de cette date, aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut "
    "être prévu ou exigé sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la durée et du renouvellement de l'agrément des centres de gestion, l'agrément de CGI 1649 quater C étant abrogé en 2025.",
    "durée et renouvellement de l'agrément.",
    "Agrément de trois ans renouvelable, rendu sans limitation de durée par la proposition antérieure.",
    "Aucune durée ni renouvellement sur ce fondement.",
    CENTRES, "L'agrément est délivré pour une période de trois ans.",
    "aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut être prévu ou exigé",
    "la durée de l'agrément des centres", "l'article 1649 quater C", plural=False,
    prev="La proposition antérieure rendait l'agrément perpétuel et renvoyait aux contrôles de l'article 371 E, lui-même abrogé. ")

oga(E135, 'LEGIARTI000033238617', B_C,
    "À compter de cette date, aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article. " + NOREPL,
    "Les décisions de retrait antérieures, leur motivation et les recours qui les concernent conservent leur régime. ",
    "Abrogation du retrait d'agrément des centres de gestion et de ses motifs, l'agrément de CGI 1649 quater C et E étant abrogé en 2025.",
    "retrait d'agrément des centres.",
    "Retrait d'agrément pour six motifs, après mise en demeure.",
    "Aucun retrait sur ce fondement ; décisions et recours antérieurs conservés.",
    CENTRES, "peut lui retirer l'agrément", "aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article",
    "le retrait d'agrément des centres", "les articles 1649 quater C et 1649 quater E", prev=PREV_REFORM)

oga(E135, 'LEGIARTI000033228679', B_C,
    "À compter de cette date, aucune interdiction de présenter une demande d'agrément ou de siéger au conseil "
    "d'administration d'un centre, d'une association ou d'un organisme mixte ne résulte du présent article, y compris "
    "pour la durée restant à courir d'une interdiction antérieure, et aucune attestation de son absence n'est exigible. "
    "Les interdictions et incapacités fondées sur d'autres dispositions demeurent applicables. " + NOREPL,
    "Les décisions antérieures de non-renouvellement ou de retrait ne sont pas annulées par cette abrogation. ",
    "Abrogation de l'interdiction biennale de nouvelle demande d'agrément et de siéger frappant un centre et ses administrateurs, l'agrément de CGI 1649 quater C étant abrogé en 2025.",
    "interdictions biennales.",
    "Interdiction de nouvelle demande et de siéger pendant deux ans après retrait ou non-renouvellement.",
    "Aucune interdiction ni attestation sur ce fondement.",
    CENTRES, "ne peut déposer de nouvelle demande d'agrément au cours des deux années suivant ladite décision",
    "aucune interdiction de présenter une demande d'agrément ou de siéger au conseil d'administration",
    "l'interdiction biennale des centres", "les articles 1649 quater C et 1649 quater E",
    prev="La proposition antérieure, déjà abrogative, réservait encore « les conditions propres à l'examen d'une nouvelle demande ». ")

oga(E240, 'LEGIARTI000033238595', B_EBIS,
    "À compter de cette date, aucun affichage ni aucune reproduction dans la correspondance ou les documents "
    "professionnels de la qualité d'adhérent d'un centre de gestion agréé ne peut être exigé sur le fondement du présent "
    "article. Aucune affiche, mention ni formalité de remplacement n'est instituée. Les règles relatives aux moyens de "
    "paiement et à l'information du consommateur ayant un fondement autonome demeurent applicables dans leur champ propre.",
    "",
    "Abrogation de l'affichage et de la mention de la qualité d'adhérent d'un centre de gestion agréé, exécutant CGI 1649 quater E bis abrogé en 2025.",
    "information de la clientèle des adhérents.",
    "Affichage dans les locaux et, dans la source, reproduction dans la correspondance de la qualité d'adhérent.",
    "Aucun affichage ni mention sur ce fondement.",
    "Adhérents des centres de gestion et leur clientèle.", "L'information mentionnée à l'article 371 LA comprend",
    "aucun affichage ni aucune reproduction dans la correspondance ou les documents professionnels",
    "l'information de la clientèle des adhérents", "l'article 1649 quater E bis", plural=False,
    prev="La proposition antérieure maintenait un affichage que l'article 371 LA, déjà abrogé, déclarait ne plus pouvoir être imposé. ")

oga(E240, 'LEGIARTI000033238588', B_EBIS,
    "À compter de cette date, aucun texte ni modèle d'information de la clientèle n'est prévu ni imposé sur le "
    "fondement du présent article. Aucune affiche, mention ni formalité de remplacement n'est instituée.", "",
    "Abrogation du texte d'information de la clientèle des adhérents de centres de gestion agréés, exécutant CGI 1649 quater E bis abrogé en 2025.",
    "texte d'information de la clientèle.",
    "Texte imposé, rendu modèle facultatif par la proposition antérieure.",
    "Aucun texte ni modèle sur ce fondement.",
    "Adhérents des centres de gestion et leur clientèle.", "Le texte prévu à l'article 371 LB est le suivant",
    "aucun texte ni modèle d'information de la clientèle n'est prévu ni imposé",
    "le texte d'information de la clientèle", "l'article 1649 quater E bis", plural=False, prev=PREV_REFORM)

oga(E240, 'LEGIARTI000006295060', B_EBIS,
    "À compter de cette date, aucune information des adhérents, confirmation écrite ni vérification de l'exécution "
    "d'obligations d'information de la clientèle ne peut être exigée sur le fondement du présent article. Aucune "
    "déclaration ni formalité de remplacement n'est instituée.", "",
    "Abrogation de l'information des adhérents et du contrôle par le centre de l'affichage de la qualité d'adhérent, exécutant CGI 1649 quater E bis abrogé en 2025.",
    "contrôle de l'information de la clientèle.",
    "Information des adhérents par le centre, confirmation écrite et vérification de l'exécution.",
    "Aucune information, confirmation ni vérification sur ce fondement.",
    "Centres de gestion et leurs adhérents.",
    "Ceux-ci doivent informer par écrit le centre de gestion agréé dont ils sont membres de l'exécution de ces obligations.",
    "aucune information des adhérents, confirmation écrite ni vérification de l'exécution",
    "le contrôle de l'information de la clientèle", "l'article 1649 quater E bis", plural=False,
    prev="La proposition antérieure maintenait que « le centre s'assure de leur exécution effective ». ")

oga(E240, 'LEGIARTI000006295061', basis("Les articles 1649 quater C, 1649 quater E et 1649 quater E bis du code général "
                                          "des impôts, qui prévoyaient l'agrément des centres de gestion, leurs missions et "
                                          "l'information de la clientèle de leurs adhérents,"),
    "À compter de cette date, aucune exclusion ne peut être prononcée sur le fondement du présent article, y compris "
    "pour des manquements antérieurs et dans les procédures en cours. Les articles 371 LA à 371 LD et 371 E étant "
    "abrogés à la même date, aucune obligation d'information de la clientèle ni procédure d'exclusion ne subsiste sur "
    "leur fondement. " + NOREPL,
    "Les exclusions antérieurement prononcées ne sont pas annulées de plein droit ; les recours qui les concernent demeurent ouverts selon leurs règles. ",
    "Abrogation de l'exclusion des adhérents de centres de gestion pour manquements à l'information de la clientèle, liée à CGI 1649 quater E bis abrogé en 2025.",
    "exclusion des adhérents.",
    "Exclusion obligatoire pour manquements graves ou répétés à l'information de la clientèle.",
    "Aucune exclusion sur ce fondement ; articles 371 LA à 371 LD et 371 E abrogés à la même date.",
    "Adhérents des centres de gestion.", "les adhérents sont exclus du centre dans les conditions prévues à l'article 371 E",
    "Les articles 371 LA à 371 LD et 371 E étant abrogés à la même date",
    "l'exclusion des adhérents des centres", "les articles 1649 quater E et 1649 quater E bis",
    prev="La proposition antérieure, déjà abrogative, déclarait « maintenues » les obligations d'information des articles 371 LA à 371 LD et « applicables » les garanties de l'article 371 E, alors que ces articles sont abrogés. ")

# ---- associations agréées
oga(E223, 'LEGIARTI000044174772', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations de membres des professions libérales et de titulaires de "
                                          "charges et offices,", plural=False),
    "À compter de cette date, aucune qualité d'association agréée n'est requise ni reconnue sur le fondement du présent "
    "article pour fournir les services d'assistance en matière de gestion qu'il énumérait ; leur fourniture n'est "
    "restreinte par aucune disposition de la présente section. " + NOREPL,
    "Les prestations déjà convenues restent régies par les contrats qui les prévoient. ",
    "Abrogation de la faculté de services réservée aux associations bénéficiant de l'agrément de l'article 1649 quater F du CGI, abrogé en 2025, sans restreindre la fourniture de ces services.",
    "faculté de services des associations agréées.",
    "Faculté de fournir des services de gestion à tout professionnel, réservée aux associations agréées.",
    "Plus de qualité d'agréée requise ; aucune restriction de ces services dans la section.",
    ASSOS,
    "Les associations bénéficiant de l'agrément prévu par l'article 1649 quater F du code général des impôts peuvent fournir à tout professionnel",
    "leur fourniture n'est restreinte par aucune disposition de la présente section",
    "la faculté de services des associations agréées", "l'article 1649 quater F", plural=False, verb='dépendait de',
    benefit="La faculté de fournir les six catégories de services n'est pas restreinte : elle était liée à un agrément supprimé par la loi, et aucune limite d'objet ne subsiste dans la section après l'abrogation de 371 M.")

oga(E223, 'LEGIARTI000033238577', B_F,
    "À compter de cette date, aucun nombre minimal d'adhérents ni aucun nombre minimal de contrôles par bureau "
    "secondaire ne peut être exigé sur le fondement du présent article. " + NOREPL,
    "Les dispenses dont bénéficiaient les associations et bureaux établis en Corse, en Guadeloupe, en Guyane, en Martinique, à Mayotte et à La Réunion restent acquises pour les périodes antérieures. ",
    "Abrogation des seuils d'adhérents et de contrôles par bureau secondaire des associations agréées, dont l'agrément (CGI 1649 quater F et H) est abrogé en 2025.",
    "seuils d'adhérents des associations.",
    "Seuils de 500 puis 1 000 adhérents et de 500 adhérents et contrôles par bureau secondaire.",
    "Aucun seuil exigé sur ce fondement ; dispenses territoriales antérieures acquises.",
    ASSOS, "Le nombre des adhérents d'une association doit être au minimum de cinq cents personnes physiques ou morales",
    "aucun nombre minimal d'adhérents ni aucun nombre minimal de contrôles par bureau secondaire ne peut être exigé",
    "les seuils d'adhérents des associations", "les articles 1649 quater F et 1649 quater H",
    prev="La proposition antérieure, déjà abrogative, supposait encore l'agrément et son maintien. ")

oga(E223, 'LEGIARTI000033238571', B_F,
    "À compter de cette date, aucune convention d'assistance technique ne peut être exigée des associations sur le "
    "fondement du présent article, et aucun refus de convention ne peut y être fondé. Aucune convention, déclaration ni "
    "formalité de remplacement n'est instituée. La répression du refus collectif de l'impôt prévue à l'article 1747 du "
    "code général des impôts demeure applicable.",
    "Les conventions conclues antérieurement, les créances et les droits des tiers qui en résultent restent régis par leurs stipulations pour les périodes auxquelles elles se rapportent. ",
    "Abrogation de la convention d'assistance technique entre associations agréées et administration fiscale et du refus de convention, fondés sur CGI 1649 quater H abrogé en 2025.",
    "convention d'assistance des associations.",
    "Convention d'assistance technique avec l'administration, rendue facultative par la proposition antérieure, et refus de convention.",
    "Aucune convention ni refus sur ce fondement ; article 1747 du CGI réservé.",
    ASSOS, "les associations doivent conclure avec l'administration fiscale une convention précisant le rôle du ou des agents",
    "aucune convention d'assistance technique ne peut être exigée des associations sur le fondement du présent article",
    "la convention d'assistance des associations", "l'article 1649 quater H", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000006295066', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations,", plural=False),
    "À compter de cette date, aucune condition relative aux personnes qui dirigent ou administrent une association, "
    "aucun certificat ni aucune attestation ne peut être exigé sur le fondement du présent article ni par renvoi à "
    "l'article 371 D, abrogé à la même date. " + NOREPL, "",
    "Abrogation du renvoi aux conditions d'intégrité des dirigeants de l'article 371 D pour les associations agréées, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "conditions d'intégrité des dirigeants des associations.",
    "Associations soumises aux obligations de l'article 371 D.",
    "Aucune condition sur ce fondement ; 371 D abrogé à la même date.",
    ASSOS, "Les associations sont soumises aux obligations prévues à l'article 371 D.",
    "ni par renvoi à l'article 371 D, abrogé à la même date",
    "le renvoi aux conditions de l'article 371 D", "l'article 1649 quater F", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238558', B_F,
    "À compter de cette date, aucune clause statutaire relative à la publicité, à la mention de l'agrément, à "
    "l'information de l'administration sur les statuts et les dirigeants, à l'assurance de responsabilité civile "
    "professionnelle, au secret, à l'information des adhérents en cas de retrait, au montant des cotisations ni à la "
    "sous-traitance des missions de contrôle ne peut être exigée sur le fondement du présent article. Les règles "
    "générales relatives à la publicité, à l'information loyale et au secret professionnel demeurent applicables. " + NOREPL,
    "Les contrats d'assurance en cours restent régis par leurs stipulations ; les informations déjà recueillies demeurent couvertes par les obligations de secret qui leur sont applicables. ",
    "Abrogation des clauses statutaires obligatoires des associations agréées (publicité, mention d'agrément, certificat, assurance, secret, cotisation, sous-traitance), liées à l'agrément abrogé en 2025.",
    "clauses statutaires obligatoires des associations.",
    "Huit engagements statutaires obligatoires des associations agréées.",
    "Aucune clause exigée sur ce fondement ; règles générales réservées.",
    ASSOS, "Les statuts doivent comporter des clauses selon lesquelles les associations s'engagent",
    "aucune clause statutaire relative à la publicité, à la mention de l'agrément",
    "les clauses statutaires des associations agréées", "les articles 1649 quater F et 1649 quater H", prev=PREV_REFORM,
    benefit="La faculté de cotisation réduite n'est pas retirée : les associations restent libres de fixer leurs cotisations ; seule disparaît l'obligation de cotisation identique attachée à l'agrément.")

oga(E223, 'LEGIARTI000033238552', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations,", plural=False),
    "À compter de cette date, aucune demande d'agrément ne peut être remise ni instruite, et aucune pièce ni aucun "
    "récépissé ne peut être exigé ou délivré sur le fondement du présent article ; les demandes encore pendantes sont "
    "sans objet. " + NOREPL, "",
    "Abrogation du dépôt des demandes d'agrément des associations, de leurs pièces et du récépissé, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "demande d'agrément des associations.",
    "Dépôt d'une demande d'agrément avec dossier de pièces et récépissé.",
    "Aucune demande, pièce ni récépissé sur ce fondement.",
    ASSOS, "Les demandes d'agrément sont remises au directeur départemental ou, le cas échéant, régional des finances publiques du département dans lequel l'association a son siège.",
    "aucune demande d'agrément ne peut être remise ni instruite",
    "la demande d'agrément des associations", "l'article 1649 quater F", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000025622281', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations,", plural=False),
    "À compter de cette date, aucune décision d'agrément ne peut être prise sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la compétence du directeur régional ou départemental pour l'agrément des associations, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "décision d'agrément des associations.",
    "Décision d'agrément prise par le directeur régional, ou départemental outre-mer, des finances publiques.",
    "Aucune décision d'agrément sur ce fondement.",
    ASSOS, "La décision d'agrément est prise par le directeur régional des finances publiques de la région dans laquelle l'association a son siège.",
    "aucune décision d'agrément ne peut être prise sur le fondement du présent article",
    "la compétence de décision d'agrément des associations", "l'article 1649 quater F", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ")

oga(E223, 'LEGIARTI000006295074', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations,", plural=False),
    "À compter de cette date, aucun délai d'instruction ne court et aucune acceptation tacite d'une demande d'agrément "
    "ne peut naître sur le fondement du présent article. " + NOREPL,
    "Les décisions de refus antérieures, leur motivation et les recours qui s'y rapportent conservent leur régime. ",
    "Abrogation du délai d'instruction et de l'acceptation tacite des demandes d'agrément des associations, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "délai d'instruction et acceptation tacite.",
    "Délai de quatre mois et acceptation tacite de l'agrément.",
    "Aucun délai ni acceptation tacite sur ce fondement.",
    ASSOS, "L'absence de décision dans le délai fixé vaut acceptation de la demande.",
    "aucune acceptation tacite d'une demande d'agrément ne peut naître sur le fondement du présent article",
    "l'instruction des demandes d'agrément des associations", "l'article 1649 quater F", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ")

oga(E223, 'LEGIARTI000006295078', basis("L'article 1649 quater F du code général des impôts, qui prévoyait l'agrément "
                                          "des associations,", plural=False),
    "À compter de cette date, aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut "
    "être prévu ou exigé sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la durée et du renouvellement de l'agrément des associations, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "durée et renouvellement de l'agrément.",
    "Agrément de trois ans renouvelable, rendu sans limitation de durée par la proposition antérieure.",
    "Aucune durée ni renouvellement sur ce fondement.",
    ASSOS, "L'agrément est délivré pour une période de trois ans.",
    "aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut être prévu ou exigé",
    "la durée de l'agrément des associations", "l'article 1649 quater F", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238548', B_F,
    "À compter de cette date, aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article. " + NOREPL,
    "Les décisions de retrait antérieures, leur motivation et les recours qui les concernent conservent leur régime. ",
    "Abrogation du retrait d'agrément des associations et de ses motifs, dont le renvoi au e du 3° de 371 Q abrogé, l'agrément de CGI 1649 quater F et H étant abrogé en 2025.",
    "retrait d'agrément des associations.",
    "Retrait d'agrément après mise en demeure, notamment pour défaut d'exclusion exigée par le e du 3° de l'article 371 Q.",
    "Aucun retrait sur ce fondement ; décisions et recours antérieurs conservés.",
    ASSOS, "peut lui retirer l'agrément", "aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article",
    "le retrait d'agrément des associations", "les articles 1649 quater F et 1649 quater H",
    prev="La proposition antérieure renvoyait encore au e du 3° de l'article 371 Q, abrogé par le projet. ")

oga(E223, 'LEGIARTI000033228882', B_F,
    "À compter de cette date, aucune interdiction de présenter une demande d'agrément ou de siéger au conseil "
    "d'administration d'un centre, d'une association ou d'un organisme mixte ne résulte du présent article, y compris "
    "pour la durée restant à courir d'une interdiction antérieure, et aucune attestation de son absence n'est exigible. "
    "Les interdictions et incapacités fondées sur d'autres dispositions demeurent applicables. " + NOREPL,
    "Les décisions antérieures de non-renouvellement ou de retrait ne sont pas annulées par cette abrogation. ",
    "Abrogation de l'interdiction biennale de nouvelle demande d'agrément et de siéger frappant une association et ses administrateurs, l'agrément de CGI 1649 quater F étant abrogé en 2025.",
    "interdictions biennales.",
    "Interdiction de nouvelle demande et de siéger pendant deux ans après retrait ou non-renouvellement.",
    "Aucune interdiction ni attestation sur ce fondement.",
    ASSOS, "ne peut déposer de nouvelle demande d'agrément au cours des deux années suivant ladite décision",
    "aucune interdiction de présenter une demande d'agrément ou de siéger au conseil d'administration",
    "l'interdiction biennale des associations", "les articles 1649 quater F et 1649 quater H",
    prev="La proposition antérieure, déjà abrogative, réservait encore les « conditions de fond » des nouvelles demandes. ")

oga(E223, 'LEGIARTI000033238525', basis("Les articles 1649 quater F et 1649 quater G du code général des impôts, qui "
                                          "prévoyaient l'agrément des associations, l'engagement des ordres et "
                                          "organisations professionnelles et les mentions des notes d'honoraires,"),
    "À compter de cette date, aucune recommandation ne peut être imposée aux ressortissants des ordres et organisations "
    "professionnels sur le fondement du présent article, l'engagement prévu à l'article 371 X étant lui-même abrogé. "
    "Les obligations comptables, déclaratives et de facturation ayant un fondement autonome, notamment celles qui "
    "résultent de l'article 99 du code général des impôts et de l'article L. 97 du livre des procédures fiscales, "
    "demeurent applicables dans leur champ propre. " + NOREPL, "",
    "Abrogation des recommandations imposées par l'engagement des ordres (371 X, abrogé) aux adhérents des associations agréées, liées à CGI 1649 quater F abrogé en 2025.",
    "recommandations des ordres.",
    "Cinq recommandations faites aux ressortissants en exécution de l'engagement de l'article 371 X.",
    "Aucune recommandation imposée sur ce fondement ; obligations autonomes réservées.",
    "Ordres et organisations des professions libérales et leurs ressortissants.",
    "Par l'engagement prévu à l'article 371 X, les ordres et organisations mentionnés à l'article précité s'obligent notamment",
    "aucune recommandation ne peut être imposée aux ressortissants des ordres et organisations professionnels",
    "les recommandations des ordres", "les articles 1649 quater F et 1649 quater G",
    prev="La proposition antérieure maintenait ces recommandations alors que l'article 371 X, qui les fonde, est abrogé et dispose qu'elles ne peuvent plus être imposées. ")

oga(E223, 'LEGIARTI000033238521', B_F,
    "À compter de cette date, aucune exclusion ne peut être prononcée sur le fondement du présent article, y compris "
    "pour des manquements antérieurs et dans les procédures en cours ; les recommandations de l'article 371 Y et le e du "
    "3° de l'article 371 Q, auxquels il renvoie, sont abrogés à la même date. " + NOREPL,
    "Les exclusions antérieurement prononcées ne sont pas annulées de plein droit ; les recours qui les concernent demeurent ouverts selon leurs règles. ",
    "Abrogation de l'exclusion des adhérents d'associations agréées pour manquements aux recommandations de 371 Y, liée à l'agrément de CGI 1649 quater F abrogé en 2025.",
    "exclusion des adhérents des associations.",
    "Exclusion pour manquements graves et répétés aux recommandations de l'article 371 Y.",
    "Aucune exclusion sur ce fondement ; 371 Y et 371 Q abrogés.",
    ASSOS, "les adhérents des associations agréées sont exclus de l'association",
    "aucune exclusion ne peut être prononcée sur le fondement du présent article",
    "l'exclusion des adhérents des associations", "les articles 1649 quater F et 1649 quater H",
    prev="La proposition antérieure renvoyait au e du 3° de l'article 371 Q, abrogé par le projet. ")

# ---- organismes mixtes
oga(E223, 'LEGIARTI000033238706', B_K,
    "À compter de cette date, aucun nombre minimal d'adhérents, aucune condition de croissance de leur nombre ni aucune "
    "condition propre aux bureaux secondaires ne peut être exigé sur le fondement du présent article. " + NOREPL,
    "Les dispenses dont bénéficiaient les organismes établis en Corse, en Guadeloupe, en Guyane, en Martinique, à Mayotte et à La Réunion restent acquises pour les périodes antérieures. ",
    "Abrogation des seuils d'adhérents des organismes mixtes de gestion agréés, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "seuils d'adhérents des organismes mixtes.",
    "Seuil de 500 adhérents, 1 000 dans les trois ans et conditions des bureaux secondaires.",
    "Aucun seuil exigé sur ce fondement ; dispenses territoriales antérieures acquises.",
    MIXTES, "Le nombre des adhérents d'un organisme mixte respecte le seuil minimum de cinq cents personnes physiques ou morales",
    "aucun nombre minimal d'adhérents, aucune condition de croissance de leur nombre",
    "les seuils d'adhérents des organismes mixtes", "l'article 1649 quater K ter", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238701', B_K,
    "À compter de cette date, aucune condition relative aux personnes qui dirigent ou administrent un organisme mixte, "
    "aucun certificat ni aucune attestation ne peut être exigé sur le fondement du présent article ni par renvoi à "
    "l'article 371 D, abrogé à la même date. " + NOREPL, "",
    "Abrogation du renvoi aux conditions d'intégrité des dirigeants de l'article 371 D pour les organismes mixtes, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "conditions d'intégrité des dirigeants des organismes mixtes.",
    "Organismes mixtes soumis aux conditions de l'article 371 D.",
    "Aucune condition sur ce fondement ; 371 D abrogé à la même date.",
    MIXTES, "Les organismes mixtes sont soumis aux obligations prévues à l'article 371 D.",
    "ni par renvoi à l'article 371 D, abrogé à la même date",
    "le renvoi aux conditions de l'article 371 D", "l'article 1649 quater K ter", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238697', B_K,
    "À compter de cette date, aucune stipulation statutaire relative à la gestion de l'organisme, aux services et "
    "documents à fournir, à l'élaboration des déclarations, aux engagements et obligations des adhérents, à leur "
    "exclusion, à l'examen périodique de sincérité, à la traçabilité des missions de contrôle ni au contrôle de "
    "l'administration ne peut être exigée sur le fondement du présent article, qui renvoie aux articles 371 E et 371 Q, "
    "abrogés. Aucun examen, compte rendu, communication de documents ni contrôle de remplacement n'est institué.",
    "Les documents fournissant une vision exhaustive des opérations comptables d'un adhérent, encore détenus, sont détruits et ne sont pas transmis à l'administration fiscale. Les prestations déjà dues aux adhérents restent régies par les statuts et contrats qui les prévoient. ",
    "Abrogation des clauses statutaires, missions de contrôle et exclusions des organismes mixtes renvoyant à 371 E et 371 Q abrogés, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "clauses statutaires et missions des organismes mixtes.",
    "Sept clauses statutaires, missions de contrôle et exclusion des adhérents par renvoi à 371 E et 371 Q.",
    "Aucune clause, mission ni exclusion sur ce fondement ; documents exhaustifs détruits.",
    MIXTES, "Les statuts de l'organisme mixte prévoient les conditions de participation à sa gestion",
    "qui renvoie aux articles 371 E et 371 Q, abrogés",
    "les clauses statutaires des organismes mixtes", "les articles 1649 quater C, 1649 quater F et 1649 quater K ter",
    prev="La proposition antérieure renvoyait encore aux articles 371 E et 371 Q, abrogés par le projet. ")

oga(E223, 'LEGIARTI000033238695', B_K,
    "À compter de cette date, aucune clause statutaire reprenant les engagements des articles 371 EA, 371 EB et "
    "371 QA, abrogés à la même date, ni aucune règle de cotisation ne peut être exigée sur le fondement du présent "
    "article. Les informations déjà recueillies demeurent couvertes par les obligations de secret qui leur sont "
    "applicables. " + NOREPL, "",
    "Abrogation des engagements statutaires et de la règle de cotisation des organismes mixtes agréés, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "engagements statutaires et cotisation des organismes mixtes.",
    "Engagements des articles 371 EA, 371 EB et 371 QA et cotisation unique plafonnant les écarts à 20 %.",
    "Aucun engagement ni règle de cotisation sur ce fondement.",
    MIXTES, "Les statuts des organismes mixtes comportent les clauses selon lesquelles ces organismes prennent les engagements",
    "ni aucune règle de cotisation ne peut être exigée sur le fondement du présent article",
    "les engagements statutaires des organismes mixtes", "l'article 1649 quater K ter", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ",
    benefit="La faculté de cotisation réduite ou différenciée n'est pas retirée : les organismes restent libres de fixer leurs cotisations ; seule disparaît la règle attachée à l'agrément.")

oga(E223, 'LEGIARTI000033238693', basis("L'article 1649 quater K ter du code général des impôts, qui prévoyait "
                                          "l'agrément des organismes mixtes de gestion,", plural=False),
    "À compter de cette date, aucune demande d'agrément ne peut être remise ni instruite, et aucune pièce ni aucun "
    "récépissé ne peut être exigé ou délivré sur le fondement du présent article ; les demandes encore pendantes sont "
    "sans objet. " + NOREPL, "",
    "Abrogation du dépôt des demandes d'agrément des organismes mixtes, de leurs pièces et du récépissé, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "demande d'agrément des organismes mixtes.",
    "Dépôt d'une demande d'agrément avec dossier de pièces et récépissé.",
    "Aucune demande, pièce ni récépissé sur ce fondement.",
    MIXTES, "Les demandes d'agrément sont remises au directeur départemental ou, le cas échéant, régional des finances publiques du département dans lequel l'organisme de gestion a son siège.",
    "aucune demande d'agrément ne peut être remise ni instruite",
    "la demande d'agrément des organismes mixtes", "l'article 1649 quater K ter", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238691', basis("L'article 1649 quater K ter du code général des impôts, qui prévoyait "
                                          "l'agrément des organismes mixtes de gestion,", plural=False),
    "À compter de cette date, aucune décision d'agrément ne peut être prise sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la compétence du directeur régional pour l'agrément des organismes mixtes, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "décision d'agrément des organismes mixtes.",
    "Décision d'agrément prise par le directeur régional des finances publiques.",
    "Aucune décision d'agrément sur ce fondement.",
    MIXTES, "La décision d'agrément est prise par le directeur régional des finances publiques de la région dans laquelle l'organisme de gestion demandeur a son siège.",
    "aucune décision d'agrément ne peut être prise sur le fondement du présent article",
    "la compétence de décision d'agrément des organismes mixtes", "l'article 1649 quater K ter", plural=False,
    prev="Le maintien antérieur reposait sur un agrément que la loi a supprimé. ")

oga(E223, 'LEGIARTI000033238689', basis("L'article 1649 quater K ter du code général des impôts, qui prévoyait "
                                          "l'agrément des organismes mixtes de gestion,", plural=False),
    "À compter de cette date, aucun délai d'instruction ne court et aucune acceptation tacite d'une demande d'agrément "
    "ne peut naître sur le fondement du présent article. " + NOREPL,
    "Les décisions de refus antérieures, leur motivation et les recours qui s'y rapportent conservent leur régime. ",
    "Abrogation du délai d'instruction et de l'acceptation tacite des demandes d'agrément des organismes mixtes, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "délai d'instruction et acceptation tacite.",
    "Délai d'instruction, ramené à deux mois par la proposition antérieure, et acceptation tacite de l'agrément.",
    "Aucun délai ni acceptation tacite sur ce fondement.",
    MIXTES, "L'absence de décision dans le délai fixé vaut acceptation de la demande.",
    "aucune acceptation tacite d'une demande d'agrément ne peut naître sur le fondement du présent article",
    "l'instruction des demandes d'agrément des organismes mixtes", "l'article 1649 quater K ter", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238687', basis("L'article 1649 quater K ter du code général des impôts, qui prévoyait "
                                          "l'agrément des organismes mixtes de gestion,", plural=False),
    "À compter de cette date, aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut "
    "être prévu ou exigé sur le fondement du présent article. " + NOREPL, "",
    "Abrogation de la durée et du renouvellement de l'agrément des organismes mixtes, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "durée et renouvellement de l'agrément.",
    "Agrément de trois ans renouvelable, rendu sans limitation de durée par la proposition antérieure.",
    "Aucune durée ni renouvellement sur ce fondement.",
    MIXTES, "L'agrément est délivré pour une période de trois ans.",
    "aucune durée, aucun renouvellement ni aucun examen de renouvellement d'agrément ne peut être prévu ou exigé",
    "la durée de l'agrément des organismes mixtes", "l'article 1649 quater K ter", plural=False, prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238685', B_K,
    "À compter de cette date, aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article. " + NOREPL,
    "Les décisions de retrait antérieures, leur motivation et les recours qui les concernent conservent leur régime. ",
    "Abrogation du retrait d'agrément des organismes mixtes et de ses motifs, dont le renvoi à la convention de 371 Z quater abrogé, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "retrait d'agrément des organismes mixtes.",
    "Retrait d'agrément après mise en demeure, notamment pour non-respect de la convention de l'article 371 Z quater.",
    "Aucun retrait sur ce fondement ; décisions et recours antérieurs conservés.",
    MIXTES, "peut lui retirer l'agrément", "aucun retrait d'agrément ne peut être prononcé sur le fondement du présent article",
    "le retrait d'agrément des organismes mixtes", "l'article 1649 quater K ter", plural=False,
    prev="La proposition antérieure renvoyait encore à la convention de l'article 371 Z quater, abrogé par le projet. ")

oga(E223, 'LEGIARTI000033238683', B_K,
    "À compter de cette date, aucune interdiction de présenter une demande d'agrément ou de siéger au conseil "
    "d'administration d'un centre, d'une association ou d'un organisme mixte ne résulte du présent article, y compris "
    "pour la durée restant à courir d'une interdiction antérieure, et aucune attestation de son absence n'est exigible. "
    "Les interdictions et incapacités fondées sur d'autres dispositions demeurent applicables. " + NOREPL,
    "Les décisions antérieures de non-renouvellement ou de retrait ne sont pas annulées par cette abrogation. ",
    "Abrogation de l'interdiction biennale de nouvelle demande d'agrément et de siéger frappant un organisme mixte et ses administrateurs, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "interdictions biennales.",
    "Interdiction de nouvelle demande et de siéger pendant deux ans après retrait ou non-renouvellement.",
    "Aucune interdiction ni attestation sur ce fondement.",
    MIXTES, "ne peut déposer de nouvelle demande d'agrément au cours des deux années suivant ladite décision",
    "aucune interdiction de présenter une demande d'agrément ou de siéger au conseil d'administration",
    "l'interdiction biennale des organismes mixtes", "l'article 1649 quater K ter", plural=False,
    prev="La proposition antérieure, déjà abrogative, réservait encore « les conditions d'examen d'une nouvelle demande ». ")

oga(E240, 'LEGIARTI000033238677', basis("Les articles 1649 quater E bis et 1649 quater K ter du code général des "
                                          "impôts, qui prévoyaient l'information de la clientèle des adhérents et "
                                          "l'agrément des organismes mixtes de gestion,"),
    "À compter de cette date, aucune information de la clientèle sur la qualité d'adhérent d'un organisme mixte de "
    "gestion agréé ni sur ses conséquences en matière d'acceptation des règlements ne peut être exigée sur le fondement "
    "du présent article, et aucune exclusion ne peut y être fondée, y compris pour des manquements antérieurs. Aucune "
    "affiche, mention ni formalité de remplacement n'est instituée. Les règles relatives aux moyens de paiement et à "
    "l'information du consommateur ayant un fondement autonome demeurent applicables dans leur champ propre.",
    "Les exclusions antérieurement prononcées ne sont pas annulées de plein droit ; les recours qui les concernent demeurent ouverts selon leurs règles. ",
    "Abrogation de l'information de la clientèle des adhérents d'organismes mixtes et de l'exclusion qui la sanctionne, exécutant CGI 1649 quater E bis abrogé en 2025.",
    "information de la clientèle et exclusion.",
    "Information de la clientèle sur la qualité d'adhérent, sous peine d'exclusion.",
    "Aucune information ni exclusion sur ce fondement.",
    "Adhérents industriels, commerçants, artisans et agriculteurs des organismes mixtes.",
    "la clientèle des industriels, commerçants, artisans et agriculteurs est informée de leur qualité d'adhérent d'un organisme mixte de gestion agréé",
    "aucune information de la clientèle sur la qualité d'adhérent d'un organisme mixte de gestion agréé",
    "l'information de la clientèle des adhérents des organismes mixtes",
    "les articles 1649 quater E bis et 1649 quater K ter", prev=PREV_REFORM)

oga(E223, 'LEGIARTI000033238674', basis("Les articles 1649 quater F et 1649 quater K ter du code général des impôts, "
                                          "qui prévoyaient l'agrément des associations et des organismes mixtes de "
                                          "gestion,"),
    "À compter de cette date, aucune recommandation ne peut être imposée aux membres des professions libérales et "
    "titulaires de charges et offices adhérents d'un organisme mixte sur le fondement du présent article, et aucune "
    "exclusion ne peut y être fondée, y compris pour des manquements antérieurs ; les articles 371 Y et 371 Z sexies, "
    "auxquels il renvoie, sont abrogés à la même date. Les obligations comptables, déclaratives et de facturation ayant "
    "un fondement autonome demeurent applicables dans leur champ propre. " + NOREPL,
    "Les exclusions antérieurement prononcées ne sont pas annulées de plein droit ; les recours qui les concernent demeurent ouverts selon leurs règles. ",
    "Abrogation des recommandations et exclusions des adhérents libéraux d'organismes mixtes renvoyant à 371 Y et 371 Z sexies abrogés, l'agrément de CGI 1649 quater K ter étant abrogé en 2025.",
    "recommandations et exclusion des adhérents libéraux.",
    "Respect des recommandations de l'article 371 Y, sous peine d'exclusion.",
    "Aucune recommandation ni exclusion sur ce fondement.",
    "Adhérents libéraux et titulaires de charges et offices des organismes mixtes.",
    "les membres des professions libérales et titulaires de charges et offices adhérents d'un organisme mixte agréé respectent les recommandations prévues à l'article 371 Y",
    "aucune recommandation ne peut être imposée aux membres des professions libérales",
    "les recommandations des adhérents libéraux des organismes mixtes",
    "les articles 1649 quater F et 1649 quater K ter", prev=PREV_REFORM)

# ---- professionnels de l'expertise comptable conventionnés (371 bis A à 371 bis N)
oga(E223, 'LEGIARTI000033238745', B_L,
    "À compter de cette date, aucun contrôle du respect des engagements de la convention prévue à l'article 371 bis B, "
    "abrogé, ne peut être organisé et aucune transmission de résultats au commissaire du Gouvernement n'est exigée sur "
    "le fondement du présent article. Aucune convention, déclaration ni formalité de remplacement n'est instituée. Les "
    "contrôles de qualité et procédures disciplinaires ayant un fondement autonome demeurent régis par leurs textes propres.",
    "Les contrôles régulièrement engagés avant cette date au titre des conventions antérieures, les droits de la défense et les recours qui s'y rapportent restent régis par les dispositions alors applicables. ",
    "Abrogation du contrôle du respect des engagements de la convention de l'article 371 bis B, abrogée, et de la transmission de ses résultats, CGI 1649 quater L et M étant abrogés en 2025.",
    "contrôle des engagements de la convention.",
    "Contrôle de qualité du respect des engagements de la convention, sans périodicité dans la proposition antérieure.",
    "Aucun contrôle ni transmission sur ce fondement ; contrôles engagés conservés.",
    "Professionnels de l'expertise comptable antérieurement conventionnés.",
    "Le respect des engagements prévus par la convention est examiné, une fois au moins tous les trois ans",
    "aucun contrôle du respect des engagements de la convention prévue à l'article 371 bis B",
    "le contrôle des engagements de la convention", "les articles 1649 quater L et 1649 quater M",
    regime='la convention',
    prev="La proposition antérieure maintenait l'examen d'une convention que les articles 371 bis B et 371 bis C, abrogés, ne permettent plus de conclure. ")

# ---- targeted fixes on already-abrogated articles
# 371 A (M05) : stale note sentence (E135, F10)
sid = 'LEGIARTI000044176875'; c = cur(A2, sid)
notes = replace_once(c['notes'], "L’interdiction générale du mandat et son exception limitée à la télétransmission demeurent. ",
                     "")
notes += (" Correction de la troisième passe (objection AUDIT6-E135, sixième audit, groupe X8) : suppression de la phrase "
          "périmée des notes selon laquelle « l'interdiction générale du mandat et son exception limitée à la "
          "télétransmission demeurent » ; l'article est abrogé et cette interdiction cesse de s'appliquer. Les autres "
          "articles de la section qui organisaient encore l'agrément (371 A bis à 371 K, 371 LB à 371 LE, 371 M bis à "
          "371 Z, 371 Z ter à 371 Z sexdecies, 371 bis G) sont abrogés dans les mêmes termes." + AI)
add(E135, A2, sid, c['proposed'], c['reason'], notes, {})

# 371 bis K (A8) : contradiction with 371 bis A abrogated
sid = 'LEGIARTI000033238721'; c = cur(A2, sid)
p = replace_once(c['proposed'],
                 "Après la fin d'une suspension, l'inscription au tableau de l'ordre des experts-comptables ou à la suite "
                 "de celui-ci produit les effets prévus à l'article 371 bis A, sans nouvelle demande d'autorisation.",
                 "La fin d'une suspension ne fait naître aucune autorisation ni convention fiscale, l'article 371 bis A "
                 "étant lui-même abrogé ; elle n'appelle aucune demande à ce titre.")
reason = ("Abrogation de fond : le délai de deux ans, la nouvelle enquête de moralité et la « nouvelle convention » "
          "soumise aux articles 371 bis B et 371 bis C, abrogés, n'ont plus d'objet depuis l'abrogation des articles "
          "1649 quater L et 1649 quater M du CGI par l'article 11 de la loi n° 2025-127. La proposition antérieure "
          "faisait produire à la fin d'une suspension « les effets prévus à l'article 371 bis A », alors que cet article "
          "est abrogé et dispose qu'aucune autorisation ne peut être délivrée, exigée ni réputée acquise : la phrase est "
          "remplacée, sans formalité de remplacement. Aucun titre retiré n'est rétabli et aucune suspension n'est levée.")
notes = (c['notes'].rstrip() + " Correction de la troisième passe (objection AUDIT6-E223, sixième audit, groupe X8) : "
         "la phrase qui renvoyait aux « effets prévus à l'article 371 bis A » est remplacée, cet article étant abrogé "
         "(groupe J10me) ; la mention des notes « 371 bis A (autorisation de plein droit par l'inscription) » est "
         "périmée, ainsi que celle de 371 bis J « maintenu », désormais abrogé." + AI)
add(E223, A2, sid, p, reason, notes, {})

# 371 bis N (none) : reference to obligations "subsistant" in 371 bis M, abrogated
sid = 'LEGIARTI000033230882'; c = cur(A2, sid)
p = replace_once(c['proposed'],
                 "Les obligations d'information subsistant à l'article 371 bis M et les règles de responsabilité et de "
                 "résiliation ayant un fondement autonome demeurent applicables.",
                 "L'article 371 bis M étant abrogé à la même date, aucune obligation d'information n'y subsiste ; les "
                 "règles de responsabilité et de résiliation ayant un fondement autonome demeurent applicables.")
notes = (c['notes'].rstrip() + " Correction de la troisième passe (objection AUDIT6-E223, sixième audit, groupe X8) : "
         "la proposition réservait les « obligations d'information subsistant à l'article 371 bis M », alors que cet "
         "article est entièrement abrogé (objection RT-P1-ANNEXES-03) ; la phrase est alignée. La note « L'abrogation "
         "ne supprime pas l'affichage conservé au 1° de M » est périmée." + AI)
add(E223, A2, sid, p, c['reason'], notes, {})

# ====================================================================================== 2. FSV, CSS R/D135
FSV_FACT = ("Le fonds de solidarité vieillesse a été supprimé au 1er janvier 2026 par l'abrogation des articles "
            "L. 135-1 à L. 135-5 (article 24 de la loi n° 2025-199 du 28 février 2025) ; ses droits et obligations ont "
            "été dévolus à cette date à la Caisse nationale d'assurance vieillesse, et ses dépenses relèvent depuis lors "
            "de la branche mentionnée au 3° de l'article L. 200-2 en application de l'article L. 222-2-1.")
E069 = 'AUDIT6-E069'
FSV_SCOPE = ("Le XXII de l'article 24 de la loi n° 2025-199 (dévolution à la Caisse nationale d'assurance vieillesse) "
             "est cité d'après la lecture faite par l'audit E09 sur Légifrance le 29 octobre 2026 ; les textes de "
             "dissolution, de liquidation et l'arrêté d'approbation des comptes 2025 ne sont pas au corpus.")
FSV_BURDEN = ("Aucune charge nouvelle : ni convention, ni déclaration, ni approbation de remplacement ; les droits et "
              "créances antérieurs sont conservés et les sommes dues par la branche restent dues.")
FSV_NOTE = (" Correction de la troisième passe (objection AUDIT6-E069, sixième audit, groupe X8) : le fonds de "
            "solidarité vieillesse est supprimé au 1er janvier 2026 (L. 135-1 LEGIARTI000037290440 et L. 135-2 "
            "LEGIARTI000042683484 figurent au corpus à l'état ABROGE à cette date, avec un lien ABROGE vers l'article 24 "
            "de la loi n° 2025-199 ; L. 135-3 à L. 135-5 aussi) ; les mentions des présentes notes qui les disent absents "
            "du corpus, ou qui supposent le fonctionnement futur du fonds, sont périmées. {what} Même solution que "
            "R135-2, R135-6 et R135-14 (variantes W02ma et W04ma) ; transferts à la Caisse nationale d'assurance "
            "vieillesse conservés ; aucune formalité de remplacement." + AI)


def fsv(sid, last_p, what, eff_desc, before, after, sq, pq, reason_add, cls_keep=True, strip_last=None, mid=None):
    c = cur(CSS, sid)
    row = ROWS.get((CSS, sid)) or {}
    base = c['proposed'] if c['proposed'] else clean_html(c['source'])
    if strip_last:
        base = replace_once(base, strip_last, '')
    proposed = base.rstrip() + f"<p>{last_p}</p>"
    num = db.execute('SELECT number FROM articles WHERE code_id=? AND id=?', (CSS, sid)).fetchone()[0]
    eff = effect('coordination', mid or ('fsv-suppression-' + re.sub(r'[^a-z0-9]+', '-', num.lower()).strip('-')),
                 eff_desc, before, after, 'regime' if 'versement' in eff_desc else 'legal_duty',
                 "Fonds de solidarité vieillesse en liquidation, Caisse nationale d'assurance vieillesse et régimes concernés.",
                 "Depuis le 1er janvier 2026 ; exercices antérieurs, régularisations et recours régis par les règles alors applicables.",
                 "Aucune formalité de remplacement.", sq, pq)
    old = row.get('substantive_impact')
    if isinstance(old, dict) and old.get('classification') != 'retained_necessary':
        imp = json.loads(json.dumps(old))
        imp['effects'] = imp['effects'] + [eff]
        imp['scope_limitations'] = imp['scope_limitations'].rstrip() + ' ' + FSV_SCOPE
        ov = dict(substantive_impact=imp)
    else:
        imp = impact('coordination_only',
                     "Coordination avec la suppression législative du fonds de solidarité vieillesse au 1er janvier 2026 : " + what,
                     FSV_SCOPE, FSV_BURDEN, [eff])
        ov = dict(status='rewrite_draft', classification='coordination_only', substantive_impact=imp,
                  benefit_review="Aucune faveur ni prise en charge n'est retirée : les sommes restent dues dans la mesure où la loi les met à la charge de la branche vieillesse, et les droits nés des exercices antérieurs sont conservés.")
    reason = (c['reason'] or '').rstrip() + ' ' + reason_add
    notes = (c['notes'] or '').rstrip() + FSV_NOTE.format(what=what)
    add(E069, CSS, sid, proposed, reason, notes, ov)


ORG_TAIL = (" il ne demeure applicable, le cas échéant, qu'à la clôture des comptes du fonds et aux opérations de "
            "dissolution et de liquidation afférentes aux exercices antérieurs à cette date, assurées par cette caisse, "
            "dans la mesure où les dispositions qui les régissent n'en disposent pas autrement. Aucune formalité de "
            "remplacement n'est instituée.")
FIN_TAIL = (" ne sont dus que dans la mesure où ils sont pris en charge par cette branche en application de l'article "
            "L. 222-2-1 ; les mentions du fonds et de l'article L. 135-2 s'entendent alors de la Caisse nationale "
            "d'assurance vieillesse, au titre de cette branche, et de l'article L. 222-2-1. Les versements afférents aux "
            "exercices antérieurs, leurs régularisations et les recours qui s'y rapportent restent régis par les "
            "dispositions alors applicables. Aucune formalité de remplacement n'est instituée.")

fsv('LEGIARTI000006747019', FSV_FACT + " Le présent article ne régit plus aucun établissement pour l'avenir ;" + ORG_TAIL,
    "l'article ne régit plus l'établissement supprimé et ne demeure applicable qu'à sa liquidation.",
    "Fin de l'organisation d'un établissement supprimé par la loi.",
    "Établissement public administratif sous double tutelle.",
    "Plus d'établissement pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Le fonds de solidarité vieillesse est un établissement public de l'Etat à caractère administratif",
    "Le présent article ne régit plus aucun établissement pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")
fsv('LEGIARTI000031285230', FSV_FACT + " Le présent article ne régit plus aucune réunion ni délibération du conseil "
    "d'administration pour l'avenir ;" + ORG_TAIL,
    "l'article ne régit plus les délibérations d'un conseil supprimé.",
    "Fin des règles de délibération du conseil d'un établissement supprimé.",
    "Réunions, quorum et majorité du conseil d'administration du fonds.",
    "Plus de réunion ni délibération pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Le conseil d'administration se réunit sur convocation de son président.",
    "Le présent article ne régit plus aucune réunion ni délibération du conseil d'administration pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")
fsv('LEGIARTI000031285225', FSV_FACT + " Le présent article ne confère plus aucune compétence au conseil "
    "d'administration pour l'avenir ;" + ORG_TAIL,
    "l'article ne confère plus de compétences à un conseil supprimé.",
    "Fin des compétences du conseil d'un établissement supprimé.",
    "Huit compétences du conseil d'administration du fonds.",
    "Plus de compétence pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Le conseil d'administration a pour rôle",
    "Le présent article ne confère plus aucune compétence au conseil d'administration pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")
fsv('LEGIARTI000031285222', FSV_FACT + " Le présent article ne régit plus aucune délibération pour l'avenir ;" + ORG_TAIL,
    "l'abrogation de l'approbation des délibérations ne vaut que pour la liquidation.",
    "Fin des règles de délibération d'un établissement supprimé.",
    "Délibérations exécutoires dès leur adoption selon la proposition antérieure.",
    "Plus de délibération pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Les délibérations du conseil d'administration sont exécutoires",
    "Le présent article ne régit plus aucune délibération pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article ne régit plus de délibérations futures.")
fsv('LEGIARTI000031285209', FSV_FACT + " Le présent article ne confère plus aucune attribution au président du fonds "
    "pour l'avenir ;" + ORG_TAIL,
    "l'article ne confère plus d'attributions au président d'un établissement supprimé.",
    "Fin des attributions du président d'un établissement supprimé.",
    "Douze attributions du président du fonds.",
    "Plus d'attribution pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Le président du fonds exerce les attributions suivantes",
    "Le présent article ne confère plus aucune attribution au président du fonds pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")

# R135-8 : the transition on future conventions is replaced by the limitation
c8 = cur(CSS, 'LEGIARTI000046790589')
m = re.search(r'<p>La suppression de l’approbation ministérielle de la convention de gestion.*?</p>', c8['proposed'], re.S)
assert m
fsv('LEGIARTI000046790589', FSV_FACT + " Le présent article ne régit plus aucune convention ni aucun avenant nouveau "
    "et ne confie plus aucune mission au président du fonds pour l'avenir ;" + ORG_TAIL.replace(
        "Aucune formalité de remplacement n'est instituée.",
        "Les créances, remboursements de frais et droits des tiers nés de la convention de gestion antérieure sont "
        "préservés. Aucune convention, approbation, déclaration ni formalité nouvelle n'est exigée de ce fait."),
    "l'article ne régit plus de convention ni d'opérations futures et ne demeure applicable qu'à la clôture et à la liquidation.",
    "Fin de la convention de gestion d'un établissement supprimé.",
    "Convention de gestion avec la CNAV, compte rendu, liquidation des dépenses et agent comptable du fonds, avec transition pour les conventions futures.",
    "Plus de convention ni d'opération future ; clôture et liquidation assurées par la CNAV ; créances antérieures préservées.",
    "La gestion administrative, financière et comptable du fonds donne lieu à une convention",
    "Le présent article ne régit plus aucune convention ni aucun avenant nouveau",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026 et ses droits et obligations dévolus à la Caisse nationale d'assurance vieillesse, la transition qui appliquait la suppression de l'approbation aux conventions futures est remplacée par une limitation de l'article à la clôture des comptes et à la liquidation du fonds.",
    strip_last=m.group(0))
fsv('LEGIARTI000033085469', FSV_FACT + " Le présent article ne régit plus aucune communication d'informations au fonds "
    "ni aucun acompte versé par lui pour l'avenir ;" + ORG_TAIL,
    "l'article ne régit plus les informations et acomptes d'un établissement supprimé.",
    "Fin des communications et acomptes d'un établissement supprimé.",
    "Communication d'informations au fonds et acomptes versés par lui.",
    "Plus de communication ni d'acompte pour l'avenir ; régularisations de liquidation assurées par la CNAV.",
    "Les organismes qui servent les prestations financées par le fonds de solidarité vieillesse sont tenus de lui communiquer",
    "Le présent article ne régit plus aucune communication d'informations au fonds",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")
fsv('LEGIARTI000006747034', FSV_FACT + " À compter de cette date, les subventions et remises de gestion prévues au "
    "présent article" + FIN_TAIL.replace('ne sont dus que dans la mesure où ils sont pris', 'ne sont dues que dans la mesure où elles sont prises'),
    "les subventions et remises de gestion ne restent dues que dans la mesure où la branche vieillesse les prend en charge.",
    "Rattachement des versements de gestion à la branche qui a repris les dépenses du fonds.",
    "Subventions et remises de gestion versées par le fonds aux organismes débiteurs.",
    "Sommes dues seulement dans la mesure de leur prise en charge par la branche vieillesse, gérée par la CNAV.",
    "reçoivent du Fonds de solidarité vieillesse des subventions et des remises de gestion",
    "les subventions et remises de gestion prévues au présent article ne sont dues que dans la mesure où elles sont prises en charge par cette branche",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, les subventions et remises ne restent dues que dans la mesure où la branche vieillesse les prend en charge en application de l'article L. 222-2-1.")
fsv('LEGIARTI000031285191', FSV_FACT + " Le présent article ne régit plus aucune convention conclue par le fonds pour "
    "l'avenir ;" + ORG_TAIL,
    "l'article ne régit plus les conventions d'un établissement supprimé.",
    "Fin des conventions de versement d'un établissement supprimé.",
    "Conventions entre le fonds et les régimes, administrations ou services.",
    "Plus de convention pour l'avenir ; liquidation assurée par la CNAV.",
    "Les modalités de versement des sommes constitutives des dépenses du fonds",
    "Le présent article ne régit plus aucune convention conclue par le fonds pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds.")
fsv('LEGIARTI000038790137', FSV_FACT + " À compter de cette date, les données mentionnées au premier alinéa sont "
    "transmises à la seule Caisse nationale d'assurance vieillesse, dans la mesure où elles demeurent nécessaires au "
    "calcul des sommes prises en charge par cette branche ; aucune transmission n'est due au fonds. Aucune formalité de "
    "remplacement n'est instituée.",
    "les données ne sont plus transmises au fonds supprimé.",
    "Fin de la transmission de données à un établissement supprimé.",
    "Transmission des données au fonds et à la CNAV.",
    "Transmission à la seule CNAV, dans la mesure nécessaire ; aucune au fonds.",
    "transmet au fonds de solidarité vieillesse et à la Caisse nationale d'assurance vieillesse les données statistiques et comptables",
    "aucune transmission n'est due au fonds",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, les données ne sont plus transmises qu'à la Caisse nationale d'assurance vieillesse.")
fsv('LEGIARTI000031283544', FSV_FACT + " Le présent article ne régit plus aucune opération du fonds pour l'avenir ;" + ORG_TAIL,
    "l'article ne régit plus les opérations comptables d'un établissement supprimé.",
    "Fin des règles comptables propres à un établissement supprimé.",
    "Opérations financières et comptables du fonds selon D. 122-2, D. 122-5 et D. 122-6.",
    "Plus d'opération pour l'avenir ; clôture et liquidation assurées par la CNAV.",
    "Les modalités suivant lesquelles sont effectuées les opérations financières et comptables du fonds",
    "Le présent article ne régit plus aucune opération du fonds pour l'avenir",
    "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, l'article est limité à la clôture des comptes et à la liquidation du fonds, assurées par la Caisse nationale d'assurance vieillesse.")
for sid, what_v, sq in [
        ('LEGIARTI000043495346', "le versement forfaitaire prévu au présent article", "Le versement forfaitaire résultant de l'application du 5° de l'article L. 135-2"),
        ('LEGIARTI000049795157', "les versements forfaitaires prévus au présent article", "Le versement du fonds de solidarité vieillesse est réparti entre le régime général et le régime des salariés agricoles"),
        ('LEGIARTI000043495357', "le versement forfaitaire prévu au présent article", "Le versement forfaitaire résultant du a du 2° de l'article L. 135-2"),
        ('LEGIARTI000053335371', "les versements forfaitaires prévus au présent article", "Les versements forfaitaires résultant de l'application des a et b du 2° de l'article L. 135-2"),
        ('LEGIARTI000043495335', "le versement forfaitaire prévu au présent article", "de l'application du a du 2° de l'article L. 135-2 est égal au produit"),
        ('LEGIARTI000043495313', "le versement forfaitaire prévu au présent article", "de l'application du a du 2° de l'article L. 135-2 est égal au produit"),
        ('LEGIARTI000043495298', "le versement forfaitaire prévu au présent article", "de l'application du a du 2° de l'article L. 135-2 est égal au produit"),
        ('LEGIARTI000043495324', "le versement forfaitaire prévu au présent article", "de l'application du 7° de l'article L. 135-2 est égal au produit")]:
    tail = FIN_TAIL if what_v.startswith('les') else FIN_TAIL.replace('ne sont dus que dans la mesure où ils sont pris',
                                                                      "n'est dû que dans la mesure où il est pris")
    fsv(sid, FSV_FACT + " À compter de cette date, " + what_v + tail,
        "le versement de financement des périodes validées ne reste dû que dans la mesure où la branche vieillesse le prend en charge.",
        "Rattachement d'un versement forfaitaire à la branche qui a repris les dépenses du fonds.",
        "Versement forfaitaire du fonds aux régimes au titre des périodes validées.",
        "Versement dû seulement dans la mesure de sa prise en charge par la branche vieillesse, gérée par la CNAV, selon la même formule.",
        sq, "À compter de cette date, " + what_v,
        "Correction de la troisième passe : le fonds étant supprimé depuis le 1er janvier 2026, la formule ne s'applique plus qu'aux sommes prises en charge par la branche vieillesse en application de l'article L. 222-2-1, la Caisse nationale d'assurance vieillesse se substituant au fonds ; les exercices antérieurs gardent leur régime.")

# ====================================================================================== 3. Other defects
# ---- E191 : CGI 244 bis and 244 bis A (loophole closure: no observable distribution without French establishment)
E191 = 'AUDIT6-E191'
sid = 'LEGIARTI000045765440'; c = cur(CGI, sid); row = ROWS[(CGI, sid)]
old5 = ("Lorsque les profits relèvent de l'impôt sur les sociétés de droit commun exigible à la distribution, dans le "
        "champ des V et VI de l'article 219, le prélèvement n'est pas opéré du seul fait de leur réalisation ou de leur "
        "conservation, y compris en trésorerie. Leur imposition suit le fait générateur, les taux normaux ou plus "
        "favorables, les règles d'assiette et les protections contre le double emploi propres à ce régime. Dans les "
        "autres cas,")
new5 = ("Lorsque les profits relèvent de l'impôt sur les sociétés de droit commun exigible à la distribution, dans le "
        "champ des V et VI de l'article 219, et sont rattachés à un établissement stable situé en France, le prélèvement "
        "n'est pas opéré du seul fait de leur réalisation ou de leur conservation, y compris en trésorerie ; leur "
        "imposition suit le fait générateur, les taux normaux ou plus favorables, les règles d'assiette et les "
        "protections contre le double emploi propres à ce régime. Pour les autres profits relevant de ce champ, réalisés "
        "par une personne qui n'a pas d'établissement en France et dont aucune distribution ne peut ainsi être constatée "
        "en France, le prélèvement est opéré lors de leur réalisation ; il est liquidé aux taux prévus aux 2 et 3 du V et "
        "au VI de l'article 219, appliqués au profit avant impôt, sans la majoration prévue pour les montants nets "
        "distribués, sous réserve du taux de 75 % prévu au premier alinéa. Il tient lieu de l'impôt sur les sociétés dû "
        "à raison de ces profits ; le montant net correspondant est inscrit au compte prévu au 1 du XI de l'article 209 "
        "et ne supporte aucun second impôt sur les sociétés lors de sa distribution. Dans les autres cas,")
p = replace_once(c['proposed'], old5, new5)
p = replace_once(p, "tout prélèvement versé en méconnaissance de la première phrase est restituable",
                 "tout prélèvement versé au-delà de l'impôt ainsi déterminé est restituable")
imp = json.loads(json.dumps(row['substantive_impact']))
imp['effects'][0]['proposed_quote'] = "et sont rattachés à un établissement stable situé en France, le prélèvement n'est pas opéré du seul fait de leur réalisation ou de leur conservation"
imp['effects'].append(effect('coordination', 'is-distribution-non-residents-sans-etablissement',
                             "Maintien du prélèvement à la réalisation pour les profits du régime de distribution réalisés sans établissement en France, aux taux de ce régime.",
                             "Prélèvement au taux normal à la réalisation, imputable sur l'IS ; la proposition antérieure le supprimait sans fait générateur de remplacement.",
                             "Prélèvement à la réalisation aux taux du V et du VI de l'article 219, tenant lieu d'IS, sans second impôt à la distribution.",
                             'percent', "Sociétés sans établissement en France réalisant des profits de l'article 35 sur des immeubles français.",
                             "Profits relevant des périodes du régime de distribution ; périodes antérieures inchangées.",
                             "Aucune formalité nouvelle : déclaration et paiement selon l'article 244 quater A, comme dans la source.",
                             "Il s'impute sur le montant de l'impôt sur les sociétés dû par le cédant au titre de l'année de réalisation des profits.",
                             "le prélèvement est opéré lors de leur réalisation ; il est liquidé aux taux prévus aux 2 et 3 du V et au VI de l'article 219"))
imp['scope_limitations'] = imp['scope_limitations'].rstrip() + (
    " Réserve F9 à confirmer : la différence entre l'imposition à la réalisation des sociétés sans établissement en "
    "France et le report à la distribution des sociétés résidentes doit être confrontée à l'article 63 du TFUE ; les "
    "justifications tirées de la répartition équilibrée du pouvoir d'imposer et de l'efficacité du recouvrement n'ont pas "
    "été vérifiées sur source primaire.")
add(E191, CGI, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E191) : pour une société sans "
    "établissement en France, la distribution n'est pas un fait générateur observable par la France (le e du 1 du V de "
    "l'article 219 et le XII de l'article 209 ne visent que l'établissement stable) ; supprimer le prélèvement à la "
    "réalisation rendait l'impôt sur les sociétés de ces profits immobiliers français non recouvrable, contrairement à "
    "l'objet déclaré du projet, qui diffère l'impôt sans l'abandonner. Le prélèvement est donc maintenu à la réalisation "
    "pour ces seuls profits, aux taux du régime de distribution et à titre libératoire, comme le prévoit déjà le 1 bis du "
    "V de l'article 219 pour les bénéfices qui sortent du régime ; il reste suspendu pour les profits rattachés à un "
    "établissement stable. Aucune formalité nouvelle.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E191, sixième audit, groupe X8 ; "
    "fermeture de faille à revoir par l'auteur) : le cinquième alinéa distingue désormais les profits rattachés à un "
    "établissement stable (report à la distribution, e du 1 du V de l'article 219) et les profits des personnes sans "
    "établissement en France (prélèvement à la réalisation, liquidé aux taux du 2 et du 3 du V et du VI de l'article 219 "
    "sur le profit avant impôt, libératoire de l'IS, montant net inscrit au compte du 1 du XI de l'article 209 sans "
    "second impôt). Le taux de 75 % des États ou territoires non coopératifs est réservé. Même coordination au III bis "
    "de l'article 244 bis A. Réserve F9 (article 63 du TFUE) à confirmer." + AI,
    dict(substantive_impact=imp), loophole=True)

sid = 'LEGIARTI000048806274'; c = cur(CGI, sid)
oldA = ("Pour les plus-values relevant du champ des V et VI de l'article 219, les règles d'assiette du III et le présent "
        "III bis ne rendent pas exigible un prélèvement du seul fait de la cession ou de la conservation du bénéfice, y "
        "compris en trésorerie. L'imposition suit la distribution, les taux et fractions d'assiette plus favorables, ainsi "
        "que les règles de non-double imposition de ce régime. Pour cet impôt sur les sociétés à la distribution, les "
        "obligations de déclaration et de paiement relèvent de l'article 1668 ; les échéances liées à la cession prévues "
        "aux IV et IV bis du présent article ne lui sont pas applicables.")
newA = ("Pour les plus-values relevant du champ des V et VI de l'article 219 qui sont rattachées à un établissement "
        "stable situé en France, les règles d'assiette du III et le présent III bis ne rendent pas exigible un prélèvement "
        "du seul fait de la cession ou de la conservation du bénéfice, y compris en trésorerie. L'imposition suit la "
        "distribution, les taux et fractions d'assiette plus favorables, ainsi que les règles de non-double imposition de "
        "ce régime. Pour cet impôt sur les sociétés à la distribution, les obligations de déclaration et de paiement "
        "relèvent de l'article 1668 ; les échéances liées à la cession prévues aux IV et IV bis du présent article ne lui "
        "sont pas applicables. Pour les autres plus-values relevant de ce champ, réalisées par une personne ou un "
        "organisme qui n'a pas d'établissement en France auquel elles sont rattachées et dont aucune distribution ne peut "
        "ainsi être constatée en France, le prélèvement est exigible lors de la cession ; il est liquidé aux taux prévus "
        "aux 2 et 3 du V et au VI de l'article 219, appliqués à la plus-value avant impôt, sans la majoration prévue pour "
        "les montants nets distribués. Il tient lieu de l'impôt sur les sociétés dû à raison de ces plus-values ; le "
        "montant net correspondant est inscrit au compte prévu au 1 du XI de l'article 209 et ne supporte aucun second "
        "impôt sur les sociétés lors de sa distribution.")
p = replace_once(c['proposed'], oldA, newA)
row = ROWS[(CGI, sid)]
imp = json.loads(json.dumps(row['substantive_impact']))
imp['effects'].append(effect('coordination', 'is-distribution-non-residents-sans-etablissement',
                             "Maintien du prélèvement à la cession pour les plus-values du régime de distribution réalisées sans établissement en France, aux taux de ce régime.",
                             "Prélèvement au taux normal à la cession, imputable sur l'IS ; la proposition antérieure le supprimait sans fait générateur de remplacement.",
                             "Prélèvement à la cession aux taux du V et du VI de l'article 219, tenant lieu d'IS, sans second impôt à la distribution.",
                             'percent', "Personnes morales non résidentes sans établissement en France cédant des biens immobiliers français.",
                             "Plus-values relevant des périodes du régime de distribution ; cessions antérieures inchangées.",
                             "Aucune formalité nouvelle : paiement lors de l'enregistrement selon le IV, comme dans la source.",
                             "sont soumises au prélèvement selon le taux prévu au deuxième alinéa du I de l'article 219",
                             "le prélèvement est exigible lors de la cession ; il est liquidé aux taux prévus aux 2 et 3 du V et au VI de l'article 219"))
imp['scope_limitations'] = imp['scope_limitations'].rstrip() + (
    " Réserve F9 à confirmer : imposition à la cession des seules personnes sans établissement en France, à confronter à "
    "l'article 63 du TFUE.")
add(E191, CGI, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E191) : même coordination qu'à "
    "l'article 244 bis ; pour une personne sans établissement en France, aucune distribution ne peut être constatée en "
    "France, de sorte que la suspension du prélèvement rendait l'impôt non recouvrable. Le prélèvement est maintenu à la "
    "cession pour ces seules plus-values, aux taux du régime de distribution et à titre libératoire ; il reste suspendu "
    "pour les plus-values rattachées à un établissement stable. Aucune formalité nouvelle.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E191, sixième audit, groupe X8 ; "
    "fermeture de faille à revoir par l'auteur) : le 1 du III bis distingue les plus-values rattachées à un établissement "
    "stable (report à la distribution) et celles des personnes sans établissement en France (prélèvement à la cession aux "
    "taux du 2 et du 3 du V et du VI de l'article 219, libératoire de l'IS, montant net inscrit au compte du 1 du XI de "
    "l'article 209). La dernière phrase du V (restitution de ce qui n'était pas exigible selon le III bis) reste exacte. "
    "Réserve F9 (article 63 du TFUE) à confirmer." + AI,
    dict(substantive_impact=imp), loophole=True)

# ---- E103 : 163 quinquies C (c of 2° of 1 of II) and 80 quindecies (reason)
E103 = 'AUDIT6-E103'
sid = 'LEGIARTI000041464278'; c = cur(CGI, sid); row = ROWS[(CGI, sid)]
p = replace_once(c['proposed'], "<p>c) Les distributions auxquelles donnent droit ces actions sont versées au moins cinq "
                                "ans après la date d'émission de ces actions ;</p>", "<p>c) Abrogé ;</p>")
p = replace_once(p, "Aucune disposition réglementaire ne peut rétablir le réinvestissement ou le blocage fiscal supprimé.</p>",
                 "Aucune disposition réglementaire ne peut rétablir le réinvestissement ou le blocage fiscal supprimé. La "
                 "suppression de la condition de délai prévue au c du 2° du 1 du II s'applique aux distributions perçues à "
                 "compter de l'entrée en vigueur de la loi supprimant la même condition au c du 2° du 8 du II de l'article "
                 "150-0 A ; les distributions perçues antérieurement demeurent régies par les dispositions qui leur étaient "
                 "applicables, sans restitution générale.</p>")
imp = json.loads(json.dumps(row['substantive_impact']))
imp['effects'].append(effect('coordination', 'carried-interest-fin-delai-cinq-ans',
                             "Alignement des distributions de sociétés de capital-risque sur la suppression du délai de cinq ans décidée au 8 du II de l'article 150-0 A.",
                             "Distributions des actions à droits différents versées au moins cinq ans après leur émission, sous peine d'imposition comme salaires (80 quindecies).",
                             "Plus de délai de cinq ans, comme pour la cession des mêmes actions selon 150-0 A proposé.",
                             'legal_duty', "Salariés et dirigeants porteurs d'actions de sociétés de capital-risque à droits différents.",
                             "Distributions perçues à compter de la loi supprimant la condition au 150-0 A ; distributions antérieures inchangées.",
                             "Aucune formalité de remplacement.",
                             "c) Les distributions auxquelles donnent droit ces actions sont versées au moins cinq ans après la date d'émission de ces actions ;",
                             "La suppression de la condition de délai prévue au c du 2° du 1 du II s'applique aux distributions perçues"))
removed = list(row.get('removed_provisions') or []) + [
    "Condition de versement des distributions d'actions de sociétés de capital-risque à droits différents au moins cinq ans après leur émission (c du 2° du 1 du II)."]
add(E103, CGI, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E103) : le 8 du II de l'article "
    "150-0 A proposé supprime le délai de cinq ans pour les parts et actions à droits différents, y compris les actions "
    "de sociétés de capital-risque ; le maintenir ici pour les seules distributions de ces mêmes actions faisait imposer "
    "comme salaire (article 80 quindecies) une distribution avant cinq ans alors que la cession avant cinq ans relève des "
    "plus-values. La seule façon de lever cette contradiction sans rétablir une contrainte supprimée est de retirer le c "
    "du 2° : c'est une cohérence avec la coupe déjà décidée, non un choix nouveau. Les autres conditions (prix, catégorie "
    "unique, 1 % et 0,5 %, rémunération normale) et le délai de conservation de cinq ans de l'exonération du 2 sont "
    "inchangés.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E103, sixième audit, groupe X8) : "
    "c du 2° du 1 du II abrogé par cohérence avec le c du 2° du 8 du II de l'article 150-0 A proposé (même mesure "
    "carried-interest-fin-delai-cinq-ans, comptée une fois) ; transition pour les distributions perçues à compter de la "
    "même loi. Le délai de conservation de cinq ans du 2° du 2 (exonération des actionnaires ordinaires) est distinct et "
    "conservé." + AI,
    dict(removed_provisions=removed, substantive_impact=imp))

sid = 'LEGIARTI000041464266'; c = cur(CGI, sid)
reason = replace_once(c['reason'],
                      "Les conditions examinées par renvoi sont le prix réel d'acquisition, la catégorie commune, la "
                      "participation minimale, l'horizon de cinq ans et, pour les fonds concernés, le remboursement préalable "
                      "des autres porteurs, ainsi que la rémunération normale.",
                      "Les conditions examinées par renvoi sont le prix réel d'acquisition, la catégorie commune, la "
                      "participation minimale et, pour les fonds concernés, le remboursement préalable des autres porteurs, "
                      "ainsi que la rémunération normale ; la durée minimale de cinq ans, supprimée au 8 du II de l'article "
                      "150-0 A et au 1 du II de l'article 163 quinquies C proposés, n'en fait plus partie pour les gains et "
                      "distributions postérieurs à cette suppression.")
add(E103, CGI, sid, None, reason,
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E103, sixième audit, groupe X8) : "
    "motif rectifié, la condition de cinq ans n'étant plus commune aux renvois (150-0 A et 163 quinquies C proposés) ; "
    "texte officiel maintenu sans changement." + AI, {})

# ---- E152 : CSS R371-9 to R371-11 (L371-12 abrogated in 1990)
E152 = 'AUDIT6-E152'
sid = 'LEGIARTI000006749482'; c = cur(CSS, sid)
src = clean_html(c['source'])
p = replace_once(src, ", sous réserve de l'application des dispositions de l'article L. 371-12", "")
imp = impact('coordination_only',
             "Retrait du seul renvoi à l'article L. 371-12, abrogé depuis le 25 janvier 1990 : l'égalité de traitement et "
             "l'absence de participation aux frais des assurés sociaux indigents sont conservées sans réserve devenue sans objet.",
             "Le texte abrogeant L. 371-12 n'est connu que par le corpus LEGI (LEGIARTI000006742726, ABROGE au 25 janvier "
             "1990) ; le relais éventuel par le code de l'action sociale et des familles n'est pas au corpus.",
             "Aucune charge nouvelle : ni condition, ni pièce, ni délai ; la faveur existante est conservée telle quelle.",
             [effect('coordination', 'aide-sociale-l371-12-renvoi-mort',
                     "Retrait d'une réserve renvoyant à un article abrogé en 1990.",
                     "Absence de participation aux frais sous réserve de L. 371-12.",
                     "Absence de participation aux frais, sans la réserve devenue sans objet.",
                     'legal_duty', "Assurés sociaux indigents.",
                     "Dès l'entrée en vigueur ; situations antérieures inchangées.",
                     "Aucune formalité de remplacement.",
                     "sous réserve de l'application des dispositions de l'article L. 371-12",
                     "ils ne supportent aucune participation aux frais de traitement.")])
add(E152, CSS, sid, p,
    "Coordination nécessaire : la réserve « sous réserve de l'application des dispositions de l'article L. 371-12 » "
    "renvoie à un article abrogé depuis le 25 janvier 1990, qui permettait de remplacer le régime par des règlements "
    "départementaux d'aide sociale. Elle est retirée ; l'égalité de traitement et l'absence de participation aux frais "
    "de traitement des assurés sociaux indigents sont conservées sans changement.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E152, sixième audit, groupe X8) : "
    "L371-12 figure au corpus (LEGIARTI000006742726), à l'état ABROGE depuis le 25 janvier 1990 ; la mention « L371-12 "
    "n'a pas été trouvé comme article autonome » est inexacte. Seul le renvoi mort est retiré ; R371-10 et R371-11, qui "
    "organisaient les règlements pris sur ce fondement, sont abrogés." + AI,
    dict(status='rewrite_draft', classification='coordination_only', substantive_impact=imp,
         benefit_review="La faveur « ils ne supportent aucune participation aux frais de traitement » est conservée, sans la réserve renvoyant à un article abrogé."))

for sid, scope, sq, what in [
        ('LEGIARTI000006749483', "Abrogation des règles de durée et de fin des règlements d'aide sociale de L. 371-12, abrogé en 1990, sous lequel aucun règlement ne peut plus être pris.",
         "Les règlements prévus à l'article L. 371-12 sont valables pour un an au moins.", "la durée et la fin des règlements d'aide sociale"),
        ('LEGIARTI000006749484', "Abrogation du régime de remboursement des frais médicaux sous un règlement d'aide sociale de L. 371-12, abrogé en 1990, sous lequel aucun règlement ne peut plus exister.",
         "En cas d'application d'un règlement ne prévoyant l'inscription sur les listes d'assistance que pour l'hospitalisation",
         "le remboursement des frais sous un règlement d'aide sociale")]:
    c = cur(CSS, sid)
    p = ("<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. "
         "L'article L. 371-12, qui prévoyait les règlements départementaux d'aide sociale auxquels il s'appliquait, est "
         "abrogé depuis le 25 janvier 1990 ; aucun règlement ne peut plus être pris ni appliqué sur ce fondement. Aucune "
         "formalité ni condition de remplacement n'est instituée.</p>"
         "<p>Cette abrogation ne remet en cause ni les prestations et dispenses de participation prévues par la loi et par "
         "l'article R. 371-9, ni les créances nées sous l'empire des règlements antérieurement pris sur ce fondement, qui "
         "restent régies par les dispositions alors applicables, avec les recours qui s'y rapportent.</p>")
    imp = impact('coordination_only',
                 f"Abrogation d'un article réglementaire qui organisait {what} prévus par L. 371-12, abrogé depuis le 25 "
                 "janvier 1990 ; la proposition antérieure réformait un régime sans base légale depuis trente-six ans.",
                 "Le texte abrogeant L. 371-12 n'est connu que par le corpus LEGI (LEGIARTI000006742726). L'existence de "
                 "règlements antérieurs encore appliqués n'est pas connue.",
                 "Aucune charge nouvelle : ni règlement, ni pièce, ni délai ; les prestations et dispenses légales et les "
                 "créances antérieures sont conservées.",
                 [effect('coordination', 'aide-sociale-l371-12-renvoi-mort',
                         "Abrogation d'un règlement d'application dont la base légale est abrogée depuis 1990.",
                         "Règles applicables aux règlements de L. 371-12, réformées par la proposition antérieure.",
                         "Article abrogé ; prestations, dispenses et créances antérieures conservées.",
                         'regime', "Caisses primaires, praticiens et assurés sociaux bénéficiaires de l'aide sociale.",
                         "Dès l'entrée en vigueur ; créances et recours antérieurs régis par les règles alors applicables.",
                         "Aucune formalité de remplacement.", sq,
                         "aucun règlement ne peut plus être pris ni appliqué sur ce fondement")])
    add(E152, CSS, sid, p,
        f"Coordination nécessaire : l'article organise {what} prévus par l'article L. 371-12, abrogé depuis le 25 janvier "
        "1990. La proposition antérieure le réformait au fond pour des règlements « adoptés à compter de l'entrée en "
        "vigueur du présent décret », alors qu'aucun règlement ne peut plus être pris sur ce fondement. L'article est "
        "abrogé, sans formalité de remplacement ; les prestations et dispenses légales et les créances antérieures sont "
        "conservées.",
        (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E152, sixième audit, groupe X8) : "
        "L371-12 figure au corpus (LEGIARTI000006742726), à l'état ABROGE depuis le 25 janvier 1990 ; les mentions « L371-12 "
        "absent du corpus » sont inexactes. L'article est abrogé ; l'allègement antérieurement proposé n'avait pas d'objet."
        + AI,
        dict(classification='coordination_only', change_type='full_repeal', repeal_policy_id=POLICY, repeal_scope=scope,
             reform_policy_id=None, removed_provisions=None, substantive_impact=imp,
             benefit_review="Aucune faveur effective n'est retirée : aucun règlement ne peut exister depuis 1990 ; l'absence de participation des assurés indigents est conservée à l'article R. 371-9."))

# ---- E302 : CSS L311-5 (recycled number L1235-16)
E302 = 'AUDIT6-E302'
sid = 'LEGIARTI000044628937'; c = cur(CSS, sid); row = ROWS[(CSS, sid)]
p = replace_once(c['proposed'],
                 "ou au 8° de l’article L. 1233-68 du code du travail, l’indemnité prévue au deuxième alinéa de l’article "
                 "L. 1235-16 du même code ou l’un des revenus de remplacement mentionnés à l’article L. 5421-2 de ce code",
                 "ou au 8° de l’article L. 1233-68 du code du travail ou l’un des revenus de remplacement mentionnés à "
                 "l’article L. 5421-2 du même code")
p = p.rstrip() + ("<p>La suppression de la mention de l'article L. 1235-16 du code du travail, qui désignait la "
                  "contribution afférente à l'ancienne convention de reclassement personnalisé, ne prive pas du maintien "
                  "de leurs droits les personnes qui en bénéficiaient à l'entrée en vigueur de la loi portant la présente "
                  "rédaction.</p>")
imp = json.loads(json.dumps(row['substantive_impact']))
imp['effects'] = [effect('coordination', 'maintien-social-renvoi-l1235-16-vestige',
                         "Retrait d'un renvoi recyclé à L. 1235-16 au lieu de sa requalification en indemnité de réparation.",
                         "Renvoi de 2008 à L. 1235-16, qui visait la contribution de la convention de reclassement personnalisé ; la proposition antérieure y rattachait l'indemnité de réparation après annulation d'un PSE.",
                         "Plus de renvoi à L. 1235-16 ; maintien des droits des bénéficiaires en cours.",
                         'legal_duty', "Personnes percevant les allocations et revenus de remplacement visés.",
                         "Dès l'entrée en vigueur ; bénéficiaires en cours protégés.",
                         "Aucune formalité de remplacement.",
                         "aux articles L. 1233-65 à L. 1233-69 et L. 1235-16",
                         "ne prive pas du maintien de leurs droits les personnes qui en bénéficiaient")]
imp['assessment'] = ("Coordination : le renvoi à L. 1235-16, issu de 2008 (contribution de la convention de reclassement "
                     "personnalisé), est un vestige depuis que ce numéro désigne l'indemnité due après annulation d'un PSE ; "
                     "il est retiré au lieu d'ouvrir un maintien de droits nouveau à une indemnité de réparation. Les autres "
                     "alinéas sont inchangés.")
add(E302, CSS, sid, p,
    "Coordination de renvoi nécessaire : la mention de L1235-16 date de 2008 et visait la contribution de deux mois liée "
    "à la convention de reclassement personnalisé (L1235-16, LEGIARTI000018767000) ; depuis 2013, ce numéro désigne "
    "l'indemnité d'au moins six mois due après annulation de la validation ou de l'homologation d'un PSE. La proposition "
    "antérieure faisait de cette indemnité de réparation un revenu ouvrant le maintien de la qualité d'assuré, droit "
    "nouveau né d'une lecture erronée du numéro et non décidé. Le vestige est retiré, avec une clause qui protège les "
    "bénéficiaires en cours. Les autres alinéas (chômage après congé parental, reprise insuffisante, indemnités maladie "
    "nulles ou maternité de faible niveau) sont intégralement maintenus.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E302, sixième audit, groupe X8) : "
    "renvoi recyclé ; la version de 2008 de L311-5 (LEGIARTI000024641022) visait « L. 1233-65 à L. 1233-69 et L. 1235-16 » "
    "quand L1235-16 (LEGIARTI000018767000) était la contribution CRP ; l'actuel L1235-16 (LEGIARTI000031013981) est une "
    "indemnité de réparation. Conflit de source neutralisé par le retrait du vestige ; les mentions des présentes notes qui "
    "présentent l'indemnité du deuxième alinéa de L1235-16 comme ouvrant le maintien sont périmées. La coordination de "
    "D622-2 n'est plus nécessaire sur ce point." + AI,
    dict(substantive_impact=imp))

# ---- E114 : CSS D160-16 (orphan "du même article")
sid = 'LEGIARTI000041967929'; c = cur(CSS, sid)
p = replace_once(c['proposed'], "L'assuré en est informé dans les conditions du dernier alinéa du même article.",
                 "L'assuré en est informé dans les conditions du dernier alinéa de l'article D. 160-15.")
add('AUDIT6-E114', CSS, sid, p, c['reason'],
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E114, sixième audit, groupe X8) : "
    "le renvoi « du dernier alinéa du même article » n'avait plus d'antécédent depuis le remplacement du renvoi source aux "
    "deux derniers alinéas de D. 160-15 ; il vise désormais expressément le dernier alinéa de l'article D. 160-15 "
    "(information sous un mois par tout moyen permettant d'en rapporter la preuve), sans formalité nouvelle." + AI, {})

# ---- E148 : CSS D752-2-3 (third alinéa of L752-1 becomes the fourth in 2028)
sid = 'LEGIARTI000034730990'; c = cur(CSS, sid)
p = replace_once(c['proposed'], "la caisse de mutualité sociale agricole mentionnée au troisième alinéa de l'article L. 752-1",
                 "la caisse de mutualité sociale agricole chargée, en application de l'article L. 752-1, de l'application de "
                 "la législation de sécurité sociale à Saint-Barthélemy")
notes = replace_once(c['notes'], "Successeur de L752-1 au 1er janvier 2028 absent. ",
                     "")
add('AUDIT6-E148', CSS, sid, p, c['reason'],
    notes.rstrip() + " Correction de la troisième passe (objection AUDIT6-E148, sixième audit, groupe X8) : la version de "
    "L752-1 applicable au 1er janvier 2028 existe au corpus (LEGIARTI000054466934, ordonnance n° 2026-647) ; elle insère "
    "l'alinéa de la caisse de Mayotte, de sorte que la caisse de Saint-Barthélemy passe au quatrième alinéa. Le renvoi "
    "est rédigé sans numéro d'alinéa, valable avant et après 2028, sans changement de fond. Les mêmes renvois de D752-2-1, "
    "D752-2-2, D752-2-4, D752-2-5 et D752-2-6 relèvent des groupes Z01 et Z02 (pistes S19a du sixième balayage)." + AI, {})

# ---- E261 : CSS L759-23 (Mayotte, 2028), new proposal carrying the L755-19 reform
sid = 'LEGIARTI000054474815'; c = cur(CSS, sid)
p = clean_html(c['source'])
p = replace_once(p, "<p>“L'allocation de base n'est pas cumulable avec :</p>\n<p>“a) Les allocations familiales au titre "
                    "d'un seul enfant à charge ;</p>\n<p>“b) Le complément familial défini à l'article L. 755-16.” ;</p>",
                 "<p>“L'allocation de base est cumulable avec les allocations familiales et leurs majorations pour âge "
                 "servies au titre d'un seul enfant à charge, lorsque les conditions propres à chacune de ces prestations "
                 "sont remplies. Elle n'est pas cumulable avec le complément familial défini à l'article L. 755-16.” ;</p>")
p = replace_once(p, "<p>“L'allocation de base n'est pas cumulable avec les allocations familiales au titre d'un seul enfant "
                    "à charge.</p>",
                 "<p>“L'allocation de base de la prestation d'accueil du jeune enfant est cumulable avec les allocations "
                 "familiales et leurs majorations pour âge servies au titre d'un seul enfant à charge, lorsque les "
                 "conditions propres à chacune de ces prestations sont remplies.</p>")
p = p.rstrip() + ("<p>Les prestations dues au titre des périodes antérieures à l'entrée en vigueur de la loi portant "
                  "réforme de l'article L. 755-19 restent régies, à Mayotte, par les règles qui leur étaient applicables, "
                  "avec leurs droits à rectification et à recours.</p>")
imp = impact('material_reduction',
             "Report, dans l'adaptation mahoraise du 11° de L. 759-23 applicable du 1er janvier 2028 au 31 mars 2030, de la "
             "seule réforme de L. 755-19 : cumul de l'allocation de base de la PAJE avec les allocations familiales servies "
             "pour un seul enfant. Sans proposition, cette version future rétablissait à Mayotte le non-cumul supprimé dans "
             "les collectivités de L. 751-1, qui incluent Mayotte à compter du 1er janvier 2028.",
             "Mesure comptée une fois avec la proposition de L. 755-19 (même measure_id). Les autres adaptations mahoraises "
             "(plafonds, revenu professionnel minimal, taux de la base mensuelle, calendrier de convergence) sont reprises "
             "sans changement ; la coordination éventuelle de L. 531-3 n'est pas faite ici. Coût non chiffré ; l'objection "
             "RT-FUTCSS-30 avait laissé ce point à l'auteur (variante B01).",
             "Aucune charge nouvelle : ni demande, ni pièce, ni condition supplémentaire ; le non-cumul avec le complément "
             "familial est conservé.",
             [effect('relief_extended', 'cumul-paje-allocations-familiales-premier-enfant',
                     "Cumul de l'allocation de base et des allocations familiales pour un seul enfant, reporté à Mayotte.",
                     "Non-cumul à Mayotte jusqu'au 31 mars 2030 dans l'adaptation de L. 755-19.",
                     "Cumul ouvert lorsque les conditions propres à chaque prestation sont remplies.",
                     'regime', "Familles mahoraises allocataires d'un seul enfant.",
                     "Périodes à compter du 1er janvier 2028 ; périodes antérieures inchangées.",
                     "Aucune formalité de remplacement.",
                     "L'allocation de base n'est pas cumulable avec les allocations familiales au titre d'un seul enfant à charge.",
                     "L'allocation de base de la prestation d'accueil du jeune enfant est cumulable avec les allocations familiales")])
add('AUDIT6-E261', CSS, sid, p,
    "Report de la réforme de L755-19 dans l'adaptation mahoraise : la proposition de L755-19 ouvre, dans les collectivités "
    "de L751-1, le cumul de l'allocation de base de la PAJE avec les allocations familiales et leurs majorations servies "
    "pour un seul enfant. Dès le 1er janvier 2028, L751-1 inclut Mayotte (LEGIARTI000054466946), mais le 11° de cette "
    "version de L759-23, issue de l'ordonnance n° 2026-647, appliquait L755-19 « dans la rédaction suivante » et y "
    "rétablissait le non-cumul jusqu'au 31 mars 2030. La présente proposition reporte la seule réforme du cumul dans les "
    "a et b du 11° ; le non-cumul avec le complément familial et toutes les autres adaptations propres à Mayotte sont "
    "conservés.",
    "Version VIGUEUR_DIFF du 1er janvier 2028 au 31 mars 2036, lue en entier avec sa NOTA (article 9 de l'ordonnance "
    "n° 2026-647 du 22 juillet 2026). Seuls les a et b du 11° sont modifiés ; les autres numéros (1° à 10°, 12° à 14°) sont "
    "repris sans changement, attributs de mise en forme retirés. Le cumul est rédigé dans les termes de la proposition de "
    "L755-19 (« lorsque les conditions propres à chacune de ces prestations sont remplies ») et n'ouvre aucun droit aux "
    "allocations familiales à qui n'y est pas éligible ; les règles mahoraises d'accès à ces allocations (8° et 9°) restent "
    "inchangées. Point laissé à l'auteur : le plafond « revenu professionnel minimal » de la rédaction mahoraise de L755-19 "
    "n'est pas coordonné avec la proposition de L531-3. Correction de la troisième passe (objection AUDIT6-E261, sixième "
    "audit, groupe X8, variante B01y ; RT-FUTCSS-30, laissée en arbitrage par B01, est tranchée dans le sens de la "
    "rédaction de L755-19 proposée, qui vise toutes les collectivités de L751-1)." + AI,
    dict(change_type='normative_reduction', reform_policy_id=POLICY,
         removed_provisions=["Non-cumul de l'allocation de base de la PAJE avec les allocations familiales servies pour un seul enfant, dans l'adaptation mahoraise de L755-19 (a et b du 11°)."],
         policy_review_id='substantive_outcomes_2026_10_19', impact_check_required=True, benefit_check_required=False,
         benefit_review="Le cumul est ouvert à Mayotte comme dans les autres collectivités de L751-1 ; toutes les autres prestations, plafonds et convergences mahoraises sont conservés.",
         substantive_impact=imp), mode='new')

# ---- E136 : annex III 46 quater-0 ZF and ZD (223 A alinéas)
E136 = 'AUDIT6-E136'
sid = 'LEGIARTI000031391602'; c = cur(A3, sid)
p = replace_once(c['proposed'], "formé en application du deuxième alinéa du I ou des premier et deuxième alinéas du II de "
                                "l'article 223 A du code général des impôts",
                 "formé en application des premier, quatrième ou cinquième alinéas du I de l'article 223 A du code "
                 "général des impôts")
p = replace_once(p, "au sens du troisième alinéa du I de l'article 223 A précité", "au sens du deuxième alinéa du I de "
                 "l'article 223 A précité")
p = replace_once(p, "dans les conditions de détention du I et des troisième et quatrième alinéas du II de l'article 223 A",
                 "dans les conditions mentionnées au sixième alinéa du I de l'article 223 A")
add(E136, A3, sid, p,
    "Coordination : l'assimilation d'une détention de 95 % à 100 % reste entière avec ses exclusions, et la condition "
    "d'inscription des titres à l'actif du bilan fiscal de l'établissement stable assure le périmètre français, sans "
    "dossier ni agrément supplémentaire. Correction de la troisième passe (sixième audit, E136) : la proposition antérieure "
    "« recalait » les renvois sur une structure de l'article 223 A qui n'existe ni dans la source ni dans la proposition "
    "de 223 A (dont le I garde six alinéas et le II un seul) ; les renvois exacts de la source sont rétablis, comme dans "
    "l'article 223 L proposé.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E136, sixième audit, groupe X8) : "
    "223 A proposé (LEGIARTI000048834056) conserve au I ses six alinéas (1er groupe vertical ; 2e société mère détenue "
    "par l'entité mère non résidente, définie dans cet alinéa ; 3e conditions de non-détention ; 4e comptes combinés ; "
    "5e organe central ; 6e titres salariés et fiducie) et n'a qu'un alinéa au II (déclaration des résultats de "
    "référence) ; ses notifications figurent au III. Les renvois proposés au « deuxième alinéa du I ou [aux] premier et "
    "deuxième alinéas du II », au « troisième alinéa du I » et aux « troisième et quatrième alinéas du II » étaient morts "
    "ou décalés et sont remplacés par ceux de la source ; les notes antérieures qui décrivaient une autre structure de "
    "223 A sont périmées." + AI, {})

sid = 'LEGIARTI000038650663'; c = cur(A3, sid)
p = c['proposed']
for old, new in [
        ("notifiées au service des impôts de la société mère selon le IV de cet article",
         "notifiées au service des impôts de la société mère selon le III de cet article"),
        ("la nature du lien qui les unit à la tête du groupe formé en application du II de l'article 223 A du code général des impôts",
         "la nature du lien qui les unit à la tête du groupe formé en application du quatrième ou du cinquième alinéa du I de l'article 223 A du code général des impôts"),
        ("la désignation des entités intermédiaires mentionnées au deuxième alinéa du I de l'article 223 A",
         "la désignation des entités intermédiaires mentionnées au premier alinéa du I de l'article 223 A"),
        ("la désignation de l'entité mère non résidente et des entités étrangères interposées mentionnées au troisième alinéa du I de l'article 223 A",
         "la désignation de l'entité mère non résidente et des entités étrangères interposées mentionnées au deuxième alinéa du I de l'article 223 A"),
        ("conformément au IV de l'article 223 A", "conformément au III de l'article 223 A"),
        ("Les conditions de combinaison prévues au II de l'article 223 A", "Les conditions de combinaison prévues au quatrième alinéa du I de l'article 223 A")]:
    p = replace_once(p, old, new)
add(E136, A3, sid, p, c['reason'],
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E136, sixième audit, groupe X8) : "
    "même décalage qu'au 46 quater-0 ZF. Dans 223 A proposé, les sociétés intermédiaires sont définies au premier alinéa "
    "du I, l'entité mère non résidente et les sociétés étrangères au deuxième, les groupes combinés et bancaires aux "
    "quatrième et cinquième alinéas du I, et les notifications et variations de périmètre au III (deuxième et troisième "
    "alinéas), comme le confirme le 7 de l'article 223 L proposé ; le IV traite du régime de distribution. Les renvois "
    "au IV, au II et aux deuxième et troisième alinéas du I sont corrigés (les expressions « entités intermédiaires » et "
    "« entités étrangères interposées » de la proposition désignent les « sociétés intermédiaires » et « sociétés "
    "étrangères » de 223 A) ; la phrase des notes « 223 A proposé : I "
    "alinéas 2 et 3 pour les intermédiaires et le groupe horizontal, II pour les réseaux, IV pour notifications » est "
    "inexacte. Aucune formalité ajoutée ; les allègements de la proposition sont conservés." + AI, {})

# ---- E268 : CCH R165-2 (J07), R165-16, L165-5, L165-6
E268 = 'AUDIT6-E268'
sid = 'LEGIARTI000043819313'; c = cur(CCH, sid); row = ROWS[(CCH, sid)]
p = replace_once(c['proposed'], "Il est également responsable de la transmission des éléments de suivi de l'agenda "
                                "d'accessibilité programmée prévus à l'article R. 165-16 et de l'attestation d'achèvement "
                                "de cet agenda prévue à l'article R. 165-17.",
                 "Il est également responsable de la transmission de l'attestation d'achèvement de cet agenda prévue à "
                 "l'article R. 165-17.")
p = replace_once(p, "Les éléments de suivi mentionnés au I ne comprennent pas les documents dispensés par l'article "
                    "L. 165-5, dans les conditions d'application dans le temps de cette dispense.",
                 "À compter de l'abrogation de l'article R. 165-16, aucun document de suivi de l'agenda n'incombe au "
                 "propriétaire ou à l'exploitant au titre du présent article, y compris pour les transmissions restant à "
                 "effectuer ; aucun document de remplacement n'est exigé.")
imp = json.loads(json.dumps(row['substantive_impact']))
for e in imp['effects']:
    if e['measure_id'] == 'adap-suppression-rapports-intermediaires':
        e['measure_id'] = 'adap-suppression-rapports-suivi'
        e['proposed_quote'] = "aucun document de suivi de l'agenda n'incombe au propriétaire ou à l'exploitant au titre du présent article"
        e['after'] = "Aucun document de suivi de l'agenda ; seule l'attestation d'achèvement de R. 165-17 reste transmise."
removed = ["Responsabilité de transmettre l'attestation initiale de conformité supprimée par L164-2.",
           "Responsabilité de transmettre les documents de suivi de l'article R. 165-16, abrogé par le projet."]
add(E268, CCH, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E268) : R165-16 est abrogé et "
    "supprime tous les documents de suivi, y compris le bilan de fin d'agenda ; le I ne renvoie plus à cet article et le "
    "IV n'exclut plus seulement les documents dispensés par L165-5, ce qui laissait croire qu'un bilan final resterait dû. "
    "L'attestation d'achèvement de R165-17, ses échéances et les contrôles sont inchangés.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E268, sixième audit, groupe X8, "
    "variante J07y) : renvoi à R165-16, abrogé, retiré du I ; IV aligné sur la suppression de tous les documents de suivi. "
    "La note « R165-16 proposé maintient un bilan à mi-parcours et retire le bilan final » est périmée : R165-16 est "
    "abrogé en entier. L165-5 et L165-6 sont coordonnés dans le même sens." + AI,
    dict(removed_provisions=removed, substantive_impact=imp))

sid = 'LEGIARTI000041569725'; c = cur(CCH, sid)
p = replace_once(c['proposed'], "ni les pouvoirs de contrôle, ni le bilan de fin d'agenda, ni l'attestation d'achèvement.",
                 "ni les pouvoirs de contrôle, ni l'attestation d'achèvement.")
add(E268, CCH, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E268) : la mention « ni le bilan de "
    "fin d'agenda » est retirée pour aligner la loi sur la suppression de ce bilan déjà retenue à l'article R. 165-16 "
    "proposé ; la loi n'impose ni n'interdit ce bilan, que le décret ne prévoit plus.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E268, sixième audit, groupe X8) : "
    "R165-16 proposé est abrogé en entier, bilan final compris ; la note « conserver bilan final » est périmée. "
    "L'attestation d'achèvement, ses échéances et les contrôles sont inchangés." + AI, {})

sid = 'LEGIARTI000041569727'; c = cur(CCH, sid); row = ROWS[(CCH, sid)]
p = replace_once(c['proposed'], "Les sanctions relatives aux documents de suivi ne s'appliquent pas aux points de "
                                "situation et bilans intermédiaires dispensés par l'article L. 165-5.",
                 "Les sanctions relatives aux documents de suivi ne s'appliquent pas aux points de situation et bilans "
                 "intermédiaires dispensés par l'article L. 165-5, ni au bilan de fin d'agenda lorsque le décret mentionné "
                 "à cet article ne le prévoit pas.")
imp = json.loads(json.dumps(row['substantive_impact']))
for e in imp['effects']:
    if e['measure_id'] == 'adap-suppression-rapports-intermediaires':
        e['proposed_quote'] = ("Les sanctions relatives aux documents de suivi ne s'appliquent pas aux points de situation "
                               "et bilans intermédiaires dispensés par l'article L. 165-5")
add(E268, CCH, sid, p,
    (c['reason'] or '').rstrip() + " Correction de la troisième passe (sixième audit, E268) : la sanction ne peut viser "
    "le bilan de fin d'agenda lorsque le décret ne le prévoit plus (R165-16 abrogé) ; aucune sanction nouvelle.",
    (c['notes'] or '').rstrip() + " Correction de la troisième passe (objection AUDIT6-E268, sixième audit, groupe X8) : "
    "coordination avec l'abrogation entière de R165-16 ; la sanction de l'absence d'attestation d'achèvement est "
    "inchangée ; loi répressive plus douce pour les sanctions non définitives, selon le dernier alinéa." + AI,
    dict(substantive_impact=imp))

sid = 'LEGIARTI000043819353'; c = cur(CCH, sid)
notes = replace_once(c['notes'], "Coordination nécessaire hors lot : L165-5 proposé conserve encore les mots « ni le bilan "
                                 "de fin d'agenda » ; retirer cette réserve et rendre sa dispense cohérente avec les trois "
                                 "documents supprimés ici, y compris les transmissions anciennes non effectuées.",
                     "L165-5 proposé ne réserve plus le bilan de fin d'agenda (troisième passe, objection AUDIT6-E268).")
add(E268, CCH, sid, c['proposed'], c['reason'],
    notes.rstrip() + " Correction de la troisième passe (objection AUDIT6-E268, sixième audit, groupe X8) : notes seules "
    "mises à jour ; L165-5, L165-6 et R165-2 sont désormais coordonnés avec l'abrogation entière du présent article." + AI, {})

# ====================================================================================== write
for g, changes in sorted(GROUPS.items()):
    folder = HOME / g
    folder.mkdir(exist_ok=True)
    (folder / 'changes.json').write_text(json.dumps(dict(group=g, changes=changes, requests=[], skipped=[]),
                                                    ensure_ascii=False, indent=1))
    print(g, len(changes))
