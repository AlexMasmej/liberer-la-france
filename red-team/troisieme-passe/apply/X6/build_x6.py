"""Build apply/X6 and variant changes.json from production texts (read-only)."""
import json, sqlite3, sys, html, re, glob
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path('/Users/alexandremasmejean/Coding/libererlafrance/third-pass/apply')
db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
db.execute('pragma query_only=1')

CGI = 'LEGITEXT000006069577'; A2 = 'LEGITEXT000006069569'; A4 = 'LEGITEXT000006069576'
TRAV = 'LEGITEXT000006072050'; CSS = 'LEGITEXT000006073189'
POLICY = 'editorial_direction_2026_10_19'
AI = ' Revue IA, sans validation par un juriste.'


def plain(v):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', v or '')).split())


def cur(code, sid):
    src = db.execute('SELECT content_xml FROM articles WHERE code_id=? AND id=?', (code, sid)).fetchone()[0]
    d = db.execute('SELECT status, proposed_xml, reason, review_notes FROM drafts WHERE code_id=? AND source_id=?', (code, sid)).fetchone()
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


def effect(kind, mid, desc, before, after, unit, pop, trans, repl, sq, pq):
    return dict(kind=kind, measure_id=mid, description=desc, before=before, after=after, unit=unit,
                affected_population=pop, conditions_and_transition=trans, replacement_or_new_burdens=repl,
                source_quote=sq, proposed_quote=pq)


def impact(cls, assessment, scope, burdens, effects):
    return dict(version=1, classification=cls, assessment=assessment, scope_limitations=scope,
                new_burdens_review=burdens, effects=effects)


def check(code, sid, proposed, imp):
    src = plain(cur(code, sid)['source'])
    prop = plain(proposed)
    for e in imp['effects']:
        assert plain(e['source_quote']) in src, (sid, 'source_quote', e['source_quote'])
        assert plain(e['proposed_quote']) in prop, (sid, 'proposed_quote', e['proposed_quote'])
    for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(imp[k]) >= 40, (sid, k)


def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


GROUPS = {}


def add(group, obj, code, sid, proposed, reason, notes, overrides):
    if 'substantive_impact' in overrides:
        check(code, sid, proposed, overrides['substantive_impact'])
    GROUPS.setdefault(group, []).append(dict(objection=obj, code_id=code, source_id=sid, mode='replace',
                                             proposed_xml=proposed, reason=reason, review_notes=notes,
                                             overrides=overrides))


# ---------------------------------------------------------------- H091 : D5134-1 et D5134-3 (W08)
OBJ = 'AUDIT5-H091'
EJ_TRANS = ("<p>Les conventions et les contrats conclus sur le fondement des dispositions législatives relatives au "
            "contrat emploi-jeune avant leur abrogation restent régis, jusqu'à leur terme, par les dispositions qui leur "
            "étaient applicables. Les aides versées, les créances, les contrôles, les prescriptions et les recours qui s'y "
            "rapportent demeurent régis par ces dispositions.</p>")
d1 = ("<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. "
      "Les dispositions législatives relatives au contrat emploi-jeune, dont l'article L. 5134-1, étant abrogées, aucune "
      "condition d'activité, aucune exclusion de périodes de travail et aucune autre règle propre aux emplois-jeunes ne "
      "s'applique sur le fondement du présent article aux contrats conclus à compter de cette entrée en vigueur, y compris "
      "sous la forme du contrat de travail unique. Aucune pièce, déclaration ou condition de remplacement n'est exigée.</p>"
      + EJ_TRANS)
c = cur(TRAV, 'LEGIARTI000031831487')
imp = impact('coordination_only',
             "Abrogation d'un règlement d'application devenu sans base légale : D5134-1 précisait la condition d'activité du 2° de l'article L. 5134-1 (contrat emploi-jeune), abrogé avec tout le régime législatif ; la proposition antérieure y ajoutait des règles pour des contrats uniques futurs, sans objet.",
             "Texte abrogeant de 2015 non lu au JORF : la date d'abrogation provient du seul corpus LEGI (LEGIARTI000006903521, ABROGE, fin 2015-08-08). Les autres articles D5134-2 à D5134-13, attribués à d'autres groupes, ne sont pas traités ici. Aucun solde national n'est établi.",
             "Aucune charge nouvelle identifiée : l'abrogation ne crée aucune pièce, déclaration, condition ni délai ; les contrats et aides antérieurs gardent leur régime jusqu'à leur terme.",
             [effect('coordination', 'emplois-jeunes-reglement-orphelin-abrogation',
                      "Abrogation de la condition d'activité des emplois-jeunes, dont la loi est abrogée.",
                      "Condition d'activité du 2° de L. 5134-1 appréciée hors périodes de contrats aidés, étendue par la proposition antérieure aux contrats uniques futurs.",
                      "Aucune règle propre aux emplois-jeunes pour les contrats futurs ; régime antérieur conservé pour les contrats conclus avant l'abrogation législative.",
                      'regime', "Employeurs et jeunes relevant de l'ancien contrat emploi-jeune.",
                      "Contrats et conventions conclus avant l'abrogation législative régis jusqu'à leur terme par les règles antérieures.",
                      "Aucune pièce, déclaration ou condition de remplacement.",
                      "La condition d'activité prévue au 2° de l'article L. 5134-1",
                      "aucune condition d'activité, aucune exclusion de périodes de travail et aucune autre règle propre aux emplois-jeunes ne s'applique")])
add('W08z', OBJ, TRAV, 'LEGIARTI000031831487', d1,
    "Abrogation de coordination : le décret d'application précise la condition d'activité du 2° de l'article L. 5134-1, alors que cet article et l'ensemble du régime législatif du contrat emploi-jeune (L. 5134-1 à L. 5134-19, versions LEGI terminées le 8 août 2015) sont abrogés. La proposition antérieure ajoutait un alinéa organisant l'application de ce régime aux contrats uniques futurs, c'est-à-dire de nouvelles règles pour un dispositif éteint. Le règlement cesse d'organiser le régime pour l'avenir ; les contrats, conventions, aides et recours antérieurs restent régis par les règles qui leur étaient applicables. Aucune formalité de remplacement.",
    "Source et proposition antérieure lues en entier. Correction des notes antérieures : L5134-1 n'est pas « absent du corpus courant » ; sa seule version, LEGIARTI000006903521, y figure à l'état ABROGE (2008-05-01 → 2015-08-08), comme L5134-2 à L5134-19 ; les articles L5134-19-1 et suivants (contrat unique d'insertion) restent distincts et ne sont pas visés. L'abrogation ne rouvre ni ne supprime aucun droit né des conventions et contrats antérieurs. Les articles D5134-2 et suivants du même régime relèvent d'autres groupes (sweep M02) : leur alignement sur la même solution est laissé au coordinateur. Texte abrogeant de 2015 non consulté au JORF. Correction de la troisième passe (objection AUDIT5-H091, audit 5) : abrogation du règlement orphelin au lieu d'une coordination nouvelle avec le contrat unique, sans formalité de remplacement et avec maintien des situations antérieures." + AI,
    dict(change_type='full_repeal', repeal_policy_id=POLICY,
         repeal_scope="Abrogation de la condition d'activité des emplois-jeunes du 2° de L. 5134-1 abrogé, de l'exclusion des périodes de contrats aidés et de l'alinéa qui étendait ces règles aux contrats uniques futurs.",
         classification='coordination_only', substantive_impact=imp))

d3 = ("<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. "
      "Les dispositions législatives relatives au contrat emploi-jeune, dont l'article L. 5134-2, étant abrogées, aucune "
      "convention emploi-jeune ni aucun contenu de convention ne peut être organisé ou exigé sur le fondement du présent "
      "article, y compris pour des embauches sous contrat de travail unique. Aucune pièce, déclaration ou condition de "
      "remplacement n'est exigée.</p>" + EJ_TRANS)
imp = impact('coordination_only',
             "Abrogation d'un règlement d'application devenu sans base légale : D5134-3 fixait le contenu de la convention emploi-jeune du 1° de l'article L. 5134-2, abrogé ; la proposition antérieure organisait encore des embauches aidées futures sous contrat unique.",
             "Texte abrogeant de 2015 non lu au JORF ; date d'abrogation tirée du corpus LEGI. D5134-2, D5134-4 et suivants ne sont pas traités ici. Aucun solde national n'est établi.",
             "Aucune charge nouvelle identifiée : l'abrogation ne crée aucune pièce, déclaration, condition ni délai ; les conventions et contrats antérieurs gardent leur régime et leurs règles de durée.",
             [effect('coordination', 'emplois-jeunes-reglement-orphelin-abrogation',
                      "Abrogation du contenu obligatoire de la convention emploi-jeune, dont la loi est abrogée.",
                      "Neuf rubriques de convention et alinéa ajouté sur les embauches futures sous contrat unique.",
                      "Aucune convention emploi-jeune organisée pour l'avenir ; conventions antérieures conservées.",
                      'regime', "Organismes employeurs signataires de conventions emploi-jeune et services de l'État.",
                      "Conventions et contrats antérieurs régis jusqu'à leur terme par les règles antérieures.",
                      "Aucune pièce, déclaration ou condition de remplacement.",
                      "La convention emploi-jeune mentionnée au 1° de l'article L. 5134-2 précise notamment",
                      "aucune convention emploi-jeune ni aucun contenu de convention ne peut être organisé ou exigé")])
add('W08z', OBJ, TRAV, 'LEGIARTI000018526703', d3,
    "Abrogation de coordination : le décret fixe le contenu de la convention emploi-jeune prévue au 1° de l'article L. 5134-2, alors que cet article et l'ensemble du régime législatif du contrat emploi-jeune sont abrogés (versions LEGI terminées le 8 août 2015). La proposition antérieure organisait encore, pour les embauches futures, la nature des contrats aidés et la durée de l'aide sous contrat unique : de nouvelles règles pour un dispositif éteint. Le règlement cesse d'organiser le régime pour l'avenir ; les conventions, contrats, aides et recours antérieurs restent régis par les règles qui leur étaient applicables, y compris leurs règles de durée. Aucune formalité de remplacement.",
    "Source et proposition antérieure lues en entier. Correction des notes antérieures : L5134-1 à L5134-11 ne sont pas introuvables ; ils figurent au corpus à l'état ABROGE (fin 2015-08-08), notamment L5134-2 (LEGIARTI000006903526) ; aucune éligibilité de nouvelles conventions ne subsiste. Les articles L5134-19-1 et suivants (contrat unique d'insertion) restent distincts. D5134-2, D5134-4 et suivants relèvent d'autres groupes (sweep M02) : leur alignement est laissé au coordinateur. Texte abrogeant de 2015 non consulté au JORF. Correction de la troisième passe (objection AUDIT5-H091, audit 5) : abrogation du règlement orphelin au lieu d'une coordination nouvelle avec le contrat unique ; conventions et contrats antérieurs préservés, sans formalité de remplacement." + AI,
    dict(change_type='full_repeal', repeal_policy_id=POLICY,
         repeal_scope="Abrogation du contenu obligatoire de la convention emploi-jeune du 1° de L. 5134-2 abrogé et de l'alinéa qui organisait des embauches aidées futures sous contrat unique.",
         classification='coordination_only', substantive_impact=imp))

# ---------------------------------------------------------------- H161 : annexe II 74 SI (J09)
OBJ = 'AUDIT5-H161'
sid = 'LEGIARTI000006293832'
c = cur(A2, sid); row = ROWS[(A2, sid)]
p74 = ("<p>Les pièces justifiant des frais ou charges mentionnés au III de l'article 150 VA et au II de l'article 150 VB du "
       "code général des impôts sont fournies par le contribuable sur demande de l'administration. Pour les cessions "
       "réalisées avant l'entrée en vigueur de la loi supprimant la condition de remploi prévue au 4° du II de l'article "
       "150 U du même code, il en est de même des pièces justifiant du remploi de l'indemnité pour le bénéfice de "
       "l'exonération prévue à ce 4°. Aucune justification de remploi n'est exigée pour les cessions réalisées à compter "
       "de cette date.</p>")
imp = impact('coordination_only',
             "Coordination avec 150 U proposé, qui supprime la condition de remploi de l'exonération des cessions sous déclaration d'utilité publique ou après délaissement pour les cessions réalisées à compter de la loi : la justification du remploi n'est plus demandée pour ces cessions, et reste possible pour les cessions antérieures.",
             "Formulaire 2048-IMM et commentaires administratifs hors corpus, non coordonnés ici. La production sur demande des frais et charges de 150 VA III et 150 VB II est inchangée. Aucun solde national n'est établi.",
             "Aucune charge nouvelle identifiée : aucune pièce, déclaration ni délai n'est ajouté ; la justification du remploi disparaît pour les cessions nouvelles et demeure, sur demande seulement, pour les cessions antérieures.",
             [effect('coordination', 'plus-values-expropriation-sans-remploi',
                      "Fin de la justification du remploi pour les cessions soumises au nouveau 4° de 150 U.",
                      "Pièces justifiant du remploi de l'indemnité fournies sur demande pour toute cession exonérée au titre du 4°.",
                      "Pièces de remploi demandées seulement pour les cessions antérieures à la loi ; aucune pour les cessions postérieures.",
                      'legal_duty', "Cédants d'immeubles expropriés ou délaissés.",
                      "Cessions réalisées à compter de l'entrée en vigueur de la loi supprimant le remploi ; cessions antérieures inchangées.",
                      "Aucune pièce ni attestation de remplacement.",
                      "Il en est de même des pièces justifiant du remploi de l'indemnité",
                      "Aucune justification de remploi n'est exigée pour les cessions réalisées à compter de cette date.")])
add('J09z', OBJ, A2, sid, p74,
    "Coordination nécessaire avec l'article 150 U proposé : son 4° du II n'exige plus le remploi de l'indemnité d'expropriation ou du prix de cession pour les cessions réalisées à compter de la loi (V de 150 U). La production sur demande des pièces de frais et charges de 150 VA III et 150 VB II est maintenue telle quelle. La justification du remploi est limitée aux cessions antérieures, qui conservent leur régime ; aucune justification n'est exigée pour les cessions nouvelles. Aucune formalité de remplacement.",
    "150 VA III, 150 VB II et 150 U (LEGIARTI000053544910, source, proposition, motif et notes) lus. Correction des notes antérieures : l'exonération d'expropriation proposée ne « garde » pas le remploi intégral sous douze mois ; 150 U proposé dispose au 4° du II que « l'exonération n'est subordonnée à aucune obligation de remploi de l'indemnité d'expropriation ou du prix de cession », et son V applique cette suppression aux cessions réalisées à compter de l'entrée en vigueur de la loi. Les forfaits de 7,5 % et 15 % de 150 VB ne sont pas transformés en dépenses réelles à justifier. La rédaction pour les cessions antérieures reprend la source (« remploi de l'indemnité ») sans l'étendre. Formulaires et commentaires administratifs hors corpus. Correction de la troisième passe (objection AUDIT5-H161, audit 5) : justification du remploi bornée aux cessions antérieures, conformément à 150 U proposé ; aucune pièce de remplacement." + AI,
    dict(status='rewrite_draft', classification='coordination_only', substantive_impact=imp,
         benefit_review="74 SI maintient la production sur demande, sans dépôt systématique, des pièces utiles aux déductions de 150 VA III et 150 VB II. L'exonération de 150 U II 4° est accessible sans remploi pour les cessions nouvelles, sans aucune pièce de remploi ; les cessions antérieures gardent leur exonération et la seule justification sur demande. Aucun avantage n'est fermé."))

# ---------------------------------------------------------------- H274 : CGI 219 bis
OBJ = 'AUDIT5-H274'
sid = 'LEGIARTI000036427378'
c = cur(CGI, sid)
p219 = c['source'].rstrip('\n') + ("\n<p>Pour les exercices ouverts à compter de l'entrée en vigueur de la loi qui insère les V et VI de "
       "l'article 219, le taux de 24 % prévu au premier alinéa est fixé à 20 %. Les taux de 10 % et de 15 % prévus aux 1° et "
       "2° sont maintenus. Les revenus mentionnés au premier alinéa demeurent imposés au titre de l'exercice au cours duquel "
       "ils sont réalisés, selon les règles propres du présent article. Les impositions des exercices antérieurs, ainsi que "
       "les créances, restitutions, prescriptions et recours qui s'y rapportent, restent régies par les règles qui leur "
       "étaient applicables.</p>\n")
imp = impact('material_reduction',
             "Baisse du taux de l'impôt sur les sociétés applicable aux revenus patrimoniaux des organismes sans but lucratif de 24 % à 20 %, pour que ce régime dérogatoire, conçu comme favorable, ne dépasse pas le taux normal de 20 % institué par le V de 219 proposé. Les taux de 10 % et 15 % sont inchangés ; l'imposition reste annuelle.",
             "Le régime reste annuel : aucun report à une distribution, que ces organismes ne pratiquent pas, n'est accordé, afin de ne pas créer d'avantage au-delà du droit commun proposé. Coût budgétaire non chiffré ; égalité devant les charges publiques non examinée sur source primaire. 206, 1668, 119 bis, 187 et annexe III 362 non modifiés.",
             "Aucune charge nouvelle identifiée : aucune déclaration, option ni condition nouvelle ; liquidation et paiement inchangés (annexe III 362, dispense d'acomptes de 1668).",
             [effect('tax_reduced', 'is-revenus-patrimoniaux-osbl-taux-20',
                      "Alignement du taux de 219 bis sur le taux normal de 20 % de 219 proposé.",
                      "24 % sur les revenus du 5 de l'article 206 (loyers, fermages, revenus de capitaux non exonérés) des établissements publics, associations et collectivités sans but lucratif.",
                      "20 % sur la même assiette pour les exercices ouverts à compter de l'entrée en vigueur du V de 219 ; 10 % et 15 % inchangés.",
                      'percent', "Établissements publics, associations, fondations et collectivités sans but lucratif imposés sur leurs revenus patrimoniaux.",
                      "Exercices ouverts à compter de l'entrée en vigueur de la loi insérant les V et VI de 219 ; exercices antérieurs régis par les règles antérieures.",
                      "Aucune formalité de remplacement.",
                      "le taux de l'impôt sur les sociétés est fixé à 24 % en ce qui concerne les revenus visés au 5 de l'article 206",
                      "le taux de 24 % prévu au premier alinéa est fixé à 20 %")])
add('X6', OBJ, CGI, sid, p219,
    "Réforme de fond limitée à un alignement : 219 proposé fixe le taux normal à 20 % du bénéfice affecté à une distribution, ne taxe pas le bénéfice conservé et n'admet aucun taux de catégorie supérieur à 20 % (VI, 1), tout en laissant les revenus non lucratifs de 219 bis à « leurs règles propres » (VI, 2). Le maintien du taux de 24 % aurait rendu ce régime dérogatoire, conçu comme favorable, plus lourd que le droit commun proposé. Le taux est ramené à 20 % pour les exercices ouverts à compter de l'entrée en vigueur de la réforme de 219 ; les taux de 10 % et de 15 % sont maintenus. L'imposition reste annuelle : ces organismes ne distribuent pas, et l'application du report à la distribution vaudrait exonération, avantage que le projet n'a pas décidé. Exercices antérieurs inchangés.",
    "206 et 219 proposés lus (206, 12 ; 219, V, 2 et VI, 1 et 2) : « le taux normal est de 20 % du bénéfice avant IS affecté à la distribution » ; « Aucun taux de catégorie supérieur au taux normal 20 % n'est maintenu » ; « les revenus non lucratifs de l'article 219 bis [...] conservent leurs règles propres ». Correction du motif antérieur : il affirmait qu'« aucun conflit avec les 20 % de l'IS ordinaire à la distribution n'est établi », alors qu'un organisme sans but lucratif aurait payé chaque année 24 % sur ses revenus patrimoniaux, une société commerciale rien sur son bénéfice conservé et 20 % à la distribution. Les renvois de 1668 (dispense d'acomptes), 119 bis et 187 (taux du 2°), 234 quaterdecies et annexe III 362 et 381 quater restent exacts. Le 1er janvier 1987 délimite les émissions de titres, pas la réforme. Aucun report à la distribution n'est étendu à ces revenus : ce serait un avantage au-delà du droit commun proposé. Coût non chiffré ; égalité devant l'impôt non examinée sur source primaire (à confirmer). Correction de la troisième passe (objection AUDIT5-H274, audit 5) : taux de 24 % ramené à 20 % pour les exercices relevant de 219 réformé, sans nouvel avantage au-delà du droit commun proposé ; aucune formalité nouvelle." + AI,
    dict(status='rewrite_draft', classification='material_reduction', substantive_impact=imp,
         benefit_review="Les taux de 10 % sur produits de titres de créance et titres émis à compter du 1er janvier 1987, et de 15 % sur dividendes, sont maintenus. Le taux général de 24 % est ramené à 20 %, au niveau du taux normal de 219 proposé, sans report à une distribution. Les exonérations personnelles de 206 ne sont ni retirées ni subordonnées à une distribution."))

# ---------------------------------------------------------------- H056 : annexe IV 50 sexies G, H, I
OBJ = 'AUDIT5-H056'
LOI290 = "l'entrée en vigueur de la loi abrogeant l'article 290 quater du code général des impôts"
sid = 'LEGIARTI000006300412'; c = cur(A4, sid); row = ROWS[(A4, sid)]
pG = c['proposed'] + ("<p>Les premier et troisième alinéas ne s'appliquent qu'aux billets, coupons et systèmes afférents aux "
      "spectacles organisés avant " + LOI290 + ". Pour les spectacles organisés à compter de cette date, aucune comptabilité "
      "des billets, aucune présentation de coupons ou de billets non utilisés et aucun dispositif de vérification de la "
      "conformité aux cahiers des charges ne sont exigés sur le fondement du présent article ; aucun billet, registre, "
      "équipement ou relevé de remplacement n'est exigé. Pour ces spectacles, le deuxième alinéa ne s'applique qu'aux "
      "vérifications qui ont un fondement légal distinct. Pour les spectacles antérieurs, les billets, coupons et systèmes "
      "déjà constitués restent soumis aux règles de conservation et de contrôle qui leur étaient applicables, sans mise en "
      "conformité.</p>")
imp = dict(row['substantive_impact'])
imp['assessment'] = ("Coordination de la présentation des coupons avec leur caractère facultatif pour les cartes occasionnelles de D, et coordination avec l'abrogation de 290 quater : la comptabilité des billets, leur présentation et les dispositifs de contrôle de conformité ne s'appliquent plus qu'aux spectacles antérieurs ; l'accès des agents ne subsiste, pour les spectacles futurs, que sur un fondement légal distinct.")
imp['scope_limitations'] = imp['scope_limitations'] + " Cahier des charges du 8 mars 1993, reprise CIBS L. 216-48 et sanctions de contributions indirectes hors corpus, non réécrits ; 50 sexies C, D et E non traités ici."
imp['effects'] = list(imp['effects']) + [effect('coordination', 'billetterie-fiscale-sectorielle-suppression',
    "Fin de la comptabilité, de la présentation et des dispositifs de contrôle des billets pour les spectacles postérieurs à l'abrogation de 290 quater.",
    "Comptabilité des billets, présentation sur réquisition et dispositifs de vérification de conformité aux cahiers des charges, sans limite dans le temps.",
    "Règles limitées aux spectacles antérieurs ; aucune exigence sur ce fondement pour les spectacles futurs.",
    'legal_duty', "Exploitants de spectacles.",
    "Spectacles organisés à compter de l'entrée en vigueur de la loi abrogeant 290 quater ; pièces anciennes conservées sans mise en conformité.",
    "Aucun billet, registre, équipement ou relevé de remplacement.",
    "Les caisses automatisées et les systèmes informatisés sont pourvus de dispositifs",
    "aucune comptabilité des billets, aucune présentation de coupons ou de billets non utilisés et aucun dispositif de vérification de la conformité aux cahiers des charges ne sont exigés")]
NOTE_290 = (" Correction de la troisième passe (objection AUDIT5-H056, audit 5) : 290 quater proposé (LEGIARTI000018619290) est abrogé et dispose que « Les obligations particulières des exploitants [...] prises pour l'application du présent article cessent de s'appliquer pour l'avenir » ; 50 sexies B proposé (V) exclut déjà, pour les spectacles futurs, toute remise de billet, tout contrôle d'entrée et toute conformité au cahier des charges de 1993. ")
add('X6', OBJ, A4, sid, pG,
    c['reason'] + " Troisième passe (AUDIT5-H056) : coordination avec l'abrogation de 290 quater et le V de 50 sexies B ; les premier et troisième alinéas sont bornés aux spectacles antérieurs et le deuxième ne vaut plus, pour les spectacles futurs, que pour les vérifications ayant un fondement légal distinct. Aucune formalité de remplacement.",
    c['notes'] + NOTE_290 + "Le présent article est aligné : comptabilité, présentation et dispositifs de contrôle limités aux spectacles antérieurs ; pièces anciennes conservées sans mise en conformité. Le cahier des charges de 1993, la reprise CIBS L. 216-48 et les sanctions de contributions indirectes sont hors corpus ; 50 sexies C, D et E, qui gardent des mentions liées aux billets, ne sont pas traités ici." + AI,
    dict(substantive_impact=imp,
         benefit_review=row.get('benefit_review', '') + " Pour les spectacles organisés après l'abrogation de 290 quater, aucune comptabilité ni présentation de billets n'est exigée sur ce fondement."))

sid = 'LEGIARTI000006301332'; c = cur(A4, sid); row = ROWS[(A4, sid)]
pH = c['proposed'] + ("<p>Les quatre premiers alinéas ne s'appliquent qu'aux spectacles organisés avant " + LOI290 + ". "
      "Pour les spectacles organisés à compter de cette date, aucun relevé des billets émis n'est exigé sur le fondement du "
      "présent article et aucun registre ou document de remplacement n'est exigé ; les obligations distinctes de "
      "comptabilisation et de déclaration des recettes demeurent applicables dans leur champ propre. Les relevés établis "
      "pour les spectacles antérieurs restent tenus à la disposition des agents des impôts et conservés dans les conditions "
      "qui leur étaient applicables.</p>")
imp = dict(row['substantive_impact'])
imp['assessment'] = imp['assessment'] + " Troisième passe : coordination avec l'abrogation de 290 quater ; le relevé quotidien ne s'applique plus qu'aux spectacles antérieurs."
imp['effects'] = list(imp['effects']) + [effect('coordination', 'billetterie-fiscale-sectorielle-suppression',
    "Fin du relevé quotidien des billets émis pour les spectacles postérieurs à l'abrogation de 290 quater.",
    "Relevé quotidien par catégorie de places : billets émis, prix et recette, sans limite dans le temps.",
    "Relevé limité aux spectacles antérieurs ; aucune exigence sur ce fondement pour les spectacles futurs.",
    'legal_duty', "Exploitants de spectacles.",
    "Spectacles organisés à compter de l'entrée en vigueur de la loi abrogeant 290 quater ; relevés anciens conservés.",
    "Aucun registre ni document de remplacement ; obligations comptables et déclaratives de droit commun inchangées.",
    "un relevé comportant, pour chaque catégorie de places : le nombre de billets émis",
    "aucun relevé des billets émis n'est exigé sur le fondement du présent article")]
add('X6', OBJ, A4, sid, pH,
    c['reason'] + " Troisième passe (AUDIT5-H056) : coordination avec l'abrogation de 290 quater ; le relevé quotidien des billets émis est borné aux spectacles antérieurs, les obligations comptables et déclaratives de droit commun restant applicables. Aucune formalité de remplacement.",
    c['notes'] + NOTE_290 + "Le présent article est aligné : relevé quotidien limité aux spectacles antérieurs, relevés anciens conservés." + AI,
    dict(substantive_impact=imp,
         removed_provisions=list(row['removed_provisions']) + ["Relevé quotidien des billets émis, prix et recettes par catégorie de places pour les spectacles organisés après l'abrogation de 290 quater supprimé."]))

sid = 'LEGIARTI000006300414'; c = cur(A4, sid); row = ROWS[(A4, sid)]
pI = replace_once(c['proposed'],
    "<p>I. – Tout utilisateur d'un système de billetterie informatisée doit se conformer au cahier des charges annexé à l'arrêté du 8 mars 1993 modifié.</p>",
    "<p>I. – Tout utilisateur d'un système de billetterie informatisée doit se conformer au cahier des charges annexé à l'arrêté du 8 mars 1993 modifié. Le présent I ne s'applique qu'aux systèmes utilisés pour des spectacles organisés avant " + LOI290 + " ; pour les spectacles organisés à compter de cette date, aucune conformité à ce cahier des charges n'est exigée sur le fondement du présent article et aucun équipement de remplacement n'est exigé.</p>")
pI = replace_once(pI, "Les obligations de conformité du I et les contrôles de l'article 50 sexies G demeurent applicables.",
    "Pour les spectacles organisés avant " + LOI290 + ", les obligations de conformité du I et les contrôles de l'article 50 sexies G demeurent applicables.")
imp = dict(row['substantive_impact'])
imp['assessment'] = ("Réforme de fond : suppression du II déclaratif entier, des huit rubriques techniques, des fac-similés et de l'information sur chaque modification du système. Troisième passe : coordination avec l'abrogation de 290 quater ; la conformité au cahier des charges de 1993 du I et les contrôles de 50 sexies G ne s'appliquent plus qu'aux spectacles antérieurs.")
imp['effects'] = list(imp['effects']) + [effect('coordination', 'billetterie-fiscale-sectorielle-suppression',
    "Fin de la conformité au cahier des charges de 1993 pour les spectacles postérieurs à l'abrogation de 290 quater.",
    "Conformité de tout système de billetterie informatisée au cahier des charges de 1993, sans limite dans le temps.",
    "Conformité limitée aux systèmes utilisés pour des spectacles antérieurs.",
    'legal_duty', "Utilisateurs de systèmes de billetterie informatisée.",
    "Spectacles organisés à compter de l'entrée en vigueur de la loi abrogeant 290 quater ; systèmes en service non remplacés.",
    "Aucun équipement, déclaration ni registre de remplacement.",
    "Tout utilisateur d'un système de billetterie informatisée doit se conformer au cahier des charges",
    "aucune conformité à ce cahier des charges n'est exigée sur le fondement du présent article")]
add('X6', OBJ, A4, sid, pI,
    "Réforme de fond : suppression du II déclaratif entier, des huit rubriques techniques, des fac-similés et de l'information sur chaque modification du système. Troisième passe (AUDIT5-H056) : la loi proposée abroge 290 quater et met fin pour l'avenir aux obligations prises pour son application ; le I (conformité au cahier des charges de 1993) et le renvoi aux contrôles de 50 sexies G sont bornés aux spectacles antérieurs, en cohérence avec le V de 50 sexies B. Aucun équipement ni formalité de remplacement.",
    c['notes'] + NOTE_290 + "Le présent article est aligné : le I et la phrase du II qui maintenait « les obligations de conformité du I et les contrôles de l'article 50 sexies G » sont limités aux spectacles antérieurs. La justification antérieure du maintien du I (« ne pas soustraire les autres utilisateurs à la conformité technique ») est sans objet pour les spectacles futurs, tout le dispositif reposant sur 290 quater." + AI,
    dict(substantive_impact=imp,
         removed_provisions=list(row['removed_provisions']) + ["Conformité au cahier des charges de 1993 des systèmes de billetterie utilisés pour les spectacles organisés après l'abrogation de 290 quater supprimée."]))

# ---------------------------------------------------------------- H117 : CGI 1729 C ter
OBJ = 'AUDIT5-H117'
sid = 'LEGIARTI000039250301'; c = cur(CGI, sid); row = ROWS[(CGI, sid)]
p1729 = replace_once(c['source'].strip('\n'),
    "L'amende ne s'applique pas aux manquements à l'obligation déclarative prévue au dernier alinéa du II de l'article 1649 AG.",
    "L'amende ne s'applique pas aux manquements à l'obligation de déclaration annuelle de l'utilisation d'un dispositif transfrontière prévue au dernier alinéa du II de l'article 1649 AG dans sa rédaction antérieure à la loi supprimant cette déclaration.")
imp = impact('coordination_only',
             "Coordination du renvoi avec 1649 AG proposé : le dernier alinéa de son II n'est plus la déclaration annuelle d'utilisation mais la clause qui la supprime pour l'avenir ; l'exclusion d'amende vise désormais cette déclaration dans sa rédaction antérieure, pour les échéances anciennes. Plafonds de 5 000, 10 000 et 100 000 € inchangés.",
             "Directive 2011/16/UE (art. 8 bis ter et 25 bis) non consultée ; 1649 AD et 1649 AE non relus en entier dans cette passe. Aucun solde national n'est établi.",
             "Aucune charge nouvelle identifiée : aucune obligation ni sanction n'est ajoutée ; l'exclusion d'amende existante est seulement rattachée à la disposition qu'elle visait.",
             [effect('coordination', 'dac6-fin-suivi-annuel-utilisation',
                      "Renvoi de l'exclusion d'amende rattaché à la déclaration annuelle supprimée.",
                      "Exclusion d'amende visant le dernier alinéa du II de 1649 AG, devenu la clause de suppression.",
                      "Exclusion d'amende visant la déclaration annuelle d'utilisation dans la rédaction antérieure de 1649 AG.",
                      'legal_duty', "Contribuables concernés par un dispositif transfrontière.",
                      "Échéances antérieures à la suppression : exclusion d'amende maintenue ; échéances postérieures : aucune obligation.",
                      "Aucune obligation ni sanction de remplacement.",
                      "L'amende ne s'applique pas aux manquements à l'obligation déclarative prévue",
                      "l'obligation de déclaration annuelle de l'utilisation d'un dispositif transfrontière prévue au dernier alinéa du II de l'article 1649 AG dans sa rédaction antérieure")])
add('X6', OBJ, CGI, sid, p1729,
    "Maintien de la sanction encadrant les déclarations et notifications de dispositifs transfrontières : plafonds de 10 000 €, de 5 000 € pour la première infraction et de 100 000 € par année inchangés. Coordination du deuxième alinéa avec 1649 AG proposé, dont le dernier alinéa du II supprime pour l'avenir la déclaration annuelle d'utilisation : l'exclusion d'amende vise cette déclaration dans sa rédaction antérieure, pour les échéances anciennes, au lieu d'un alinéa qui ne prévoit plus aucune obligation. Aucune obligation ni sanction nouvelle.",
    c['notes'] + " Correction de la troisième passe (objection AUDIT5-H117, audit 5) : 1649 AG proposé (LEGIARTI000051215673) remplace le dernier alinéa de son II par « Aucune déclaration annuelle de l'utilisation d'un dispositif transfrontière n'est exigée du contribuable sur le fondement du présent article pour les échéances postérieures à l'entrée en vigueur de la loi » ; ses notes demandaient l'adaptation « hors lot » du renvoi de 1729 C ter. Le renvoi est rattaché à la déclaration annuelle dans la rédaction antérieure de 1649 AG : l'exclusion d'amende reste acquise pour les échéances anciennes et l'obligation supprimée ne peut plus être sanctionnée." + AI,
    dict(status='rewrite_draft', classification='coordination_only', substantive_impact=imp))

# ---------------------------------------------------------------- H068 : travail L7123-10
OBJ = 'AUDIT5-H068'
sid = 'LEGIARTI000006904606'; c = cur(TRAV, sid); row = ROWS[(TRAV, sid)]
old_last = ("<p>Pour les contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, la fin de la prestation et le versement de cette indemnité ne mettent pas fin au contrat de travail à durée indéterminée. Cette indemnité de congé payé demeure due pour chaque prestation, sans condition d'ancienneté ; elle est distincte du préavis et de l'indemnité ordinaire de rupture. Les droits à congés payés et indemnités des contrats antérieurs sont conservés.</p>")
new_last = ("<p>Les trois alinéas précédents demeurent applicables aux contrats conclus avant l'entrée en vigueur de la loi "
            "instituant le contrat de travail unique. Pour les contrats conclus à compter de cette entrée en vigueur, la fin d'une "
            "prestation ne met pas fin au contrat de travail à durée indéterminée et les trois alinéas précédents ne s'appliquent "
            "pas : le salarié acquiert et prend ses congés payés dans les conditions de droit commun, sans que leur prise "
            "effective puisse être remplacée par leur paiement pendant la poursuite de l'emploi. À la fin effective du contrat, "
            "il conserve, quelle que soit la durée de son emploi, la garantie d'une indemnité compensatrice des congés acquis et "
            "non pris, qui ne peut être inférieure au dixième de la rémunération totale perçue au titre des périodes ayant ouvert "
            "ces congés ; les congés effectivement pris et les sommes déjà versées au même titre sont pris en compte sans double "
            "indemnisation. Cette indemnité est distincte du préavis et de l'indemnité ordinaire de rupture ; elle n'est soumise "
            "ni à la condition d'un an ni au plafond de six mois de cette dernière. Les droits à congés payés et indemnités des "
            "contrats antérieurs sont conservés ; la seule conversion d'un contrat antérieur en contrat unique ne déclenche pas "
            "leur indemnisation.</p>")
pL = replace_once(c['proposed'], old_last, new_last)
imp = dict(row['substantive_impact'])
imp['assessment'] = ("Coordination du paiement spécial des congés des mannequins avec le contrat unique, alignée sur L1242-16 et L1251-58-4 proposés : les contrats antérieurs gardent l'indemnité versée à chaque prestation ; pour les contrats uniques, les congés sont pris en nature et la garantie du dixième est versée à la fin effective du contrat, sans paiement des congés pendant la poursuite de l'emploi ni double indemnisation.")
imp['scope_limitations'] = ("Directive 2003/88/CE (article 7) et jurisprudence de la Cour de justice non consultées sur source primaire ; accords collectifs des mannequins et R7123-10 et R7123-11 non relus. Le calendrier de prise des congés entre prestations n'est pas réglé ici. Aucun solde national n'est établi.")
imp['new_burdens_review'] = ("Aucune charge nouvelle identifiée : aucune formalité, déclaration ni délai n'est ajouté ; le droit commun des congés payés s'applique à un contrat à durée indéterminée et le minimum du dixième est conservé à la fin du contrat.")
imp['effects'] = [effect('coordination', 'contrat-unique-duree-indeterminee',
    "Congés des mannequins sous contrat unique pris en nature, garantie du dixième à la fin effective du contrat.",
    "Indemnité compensatrice de congé payé versée à chaque fin de prestation, y compris pendant la poursuite du contrat unique.",
    "Contrats antérieurs : indemnité par prestation conservée ; contrats uniques : congés de droit commun et indemnité d'au moins un dixième à la fin effective du contrat.",
    'regime', "Mannequins salariés des agences de mannequins et agences employeurs.",
    "Contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat unique ; contrats antérieurs et conversions sans indemnisation déclenchée.",
    "Aucune formalité de remplacement ; aucune condition d'ancienneté ni plafond.",
    "L'indemnité est versée à la fin de la prestation.",
    "sans que leur prise effective puisse être remplacée par leur paiement pendant la poursuite de l'emploi")]
add('X6', OBJ, TRAV, sid, pL,
    "Coordination des congés des mannequins avec le contrat unique, alignée sur L1242-16 et L1251-58-4 proposés : les trois alinéas d'origine (indemnité pour chaque prestation, minimum du dixième, versement à la fin de la prestation) restent applicables aux contrats antérieurs. Pour les contrats uniques, la fin d'une prestation ne rompt pas le contrat ; les congés sont pris en nature et ne peuvent être remplacés par un paiement pendant la poursuite de l'emploi ; à la fin effective du contrat, la garantie d'une indemnité d'au moins un dixième est conservée, sans condition d'ancienneté ni plafond et sans double indemnisation. La proposition antérieure maintenait le paiement à chaque prestation pendant un emploi qui se poursuit, ce qui laissait ouverte une double indemnisation ou un rachat du congé, contrairement aux choix du projet pour les CDD et l'intérim en CDI.",
    "Lus : L7123-5, L7123-3, L7123-4, L1242-16 proposé (« Cette garantie ne permet pas de remplacer la prise effective des congés par leur paiement pendant la poursuite de l'emploi »), L1251-58-4 proposé (« L'exclusion de l'article L. 1251-19 ne supprime ni les congés payés du salarié employé à durée indéterminée ») et L3141-1. Correction des notes antérieures : la proposition antérieure ne se bornait pas à rendre l'indemnité « compatible avec la poursuite de l'emploi » ; elle faisait coexister le paiement par prestation et le droit annuel au congé, sans dire si l'un remplace l'autre. Différence de champ avec L1234-9 : l'indemnité de congé n'est pas l'indemnité ordinaire de rupture ; ni le seuil d'un an ni le plafond de six mois ne lui sont applicables. Le préavis de quinze jours calendaires de L1234-1 proposé n'est pas modifié. Transition : contrats antérieurs régis par les trois premiers alinéas ; une conversion ne déclenche pas à elle seule l'indemnisation. Conformité à l'article 7 de la directive 2003/88/CE et à la jurisprudence de la Cour de justice (Robinson-Steele, C-131/04 et C-257/04) à confirmer sur source primaire. Correction de la troisième passe (objection AUDIT5-H068, audit 5) : congés en nature et garantie du dixième à la fin effective du contrat unique, en cohérence avec L1242-16 et L1251-58-4 ; aucune formalité nouvelle." + AI,
    dict(substantive_impact=imp))

# ---------------------------------------------------------------- H198 : css A932-4-1 (W02)
OBJ = 'AUDIT5-H198'
sid = 'LEGIARTI000028651627'; c = cur(CSS, sid); row = ROWS[(CSS, sid)]
pA = c['source'].strip('\n')
pA = replace_once(pA, "<p>III.-L'équivalence actuarielle prévue à l'article R. 932-4-14 est établie dans les conditions suivantes : </p>",
    "<p>III.-L'équivalence actuarielle prévue à l'article R. 932-4-14, dans sa rédaction antérieure à son abrogation au 31 décembre 2017, est établie dans les conditions suivantes : </p>")
pA = replace_once(pA, "<p>IV.-Les calculs de la provision mathématique théorique, mentionnée à l'article R. 932-4-15, des équivalences actuarielles prévues à l'article R. 932-4-14 et la répartition des droits prévue à l'article R. 932-4-20 sont effectués en utilisant les tables de mortalité appropriées mentionnées à l'article A. 931-10-10 applicables aux contrats de rente viagère souscrits à compter du 1er janvier 2007, et à l'aide d'un taux au plus égal au plus élevé des deux taux suivants : </p>",
    "<p>IV.-Les calculs de la répartition des droits prévue à l'article R. 932-4-20 sont effectués en utilisant les tables de mortalité appropriées applicables aux contrats de rente viagère souscrits à compter du 1er janvier 2007, mentionnées à l'article A. 931-10-10 dans sa rédaction antérieure à son abrogation au 1er janvier 2016, et à l'aide d'un taux au plus égal au plus élevé des deux taux suivants : </p>")
pA = pA + ("\n<p>Les calculs de la provision mathématique théorique mentionnée à l'article R. 932-4-15 effectués sous l'empire de "
           "la rédaction de cet article antérieure au 31 décembre 2017, ainsi que ceux des équivalences actuarielles mentionnées "
           "au III, sont effectués selon les mêmes modalités. Depuis cette date, les conditions d'évaluation de la provision "
           "mathématique théorique sont celles fixées par l'arrêté auquel renvoie le dernier alinéa de l'article R. 932-4-15.</p>")
imp = impact('coordination_only',
             "Coordination des renvois morts : R932-4-14 (équivalence actuarielle) est abrogé au 31 décembre 2017 et A931-10-10 (tables) au 1er janvier 2016 ; R932-4-15 en vigueur renvoie l'évaluation de la provision mathématique théorique à l'arrêté prévu à R441-21 du code des assurances. Le III et les calculs de provision ne valent plus que pour les périodes antérieures ; la répartition des droits de R932-4-20 garde les tables et le taux du IV.",
             "Arrêté prévu à R441-21 du code des assurances et tables actuelles hors corpus ; aucun renvoi de remplacement aux tables n'est inventé : les tables restent identifiées par la rédaction antérieure de A931-10-10. Textes abrogeants de 2015 et 2017 non lus au JORF. Aucun solde national n'est établi.",
             "Aucune charge nouvelle identifiée : aucun calcul, état ni délai n'est ajouté ; les taux, tables et l'étalement historique sont conservés pour leur champ.",
             [effect('coordination', 'ip-retraite-points-renvois-abroges',
                      "Renvois à R932-4-14 et A931-10-10 abrogés neutralisés, provision théorique renvoyée à l'arrêté désigné par R932-4-15.",
                      "Calculs de provision mathématique théorique, d'équivalences et de répartition des droits fondés sur R932-4-14 et A931-10-10 abrogés.",
                      "Répartition des droits selon les tables et le taux du IV ; provision théorique et équivalences selon ces modalités pour les seules périodes antérieures au 31 décembre 2017.",
                      'regime', "Institutions de prévoyance et unions gérant des opérations collectives de L. 932-24, et leurs participants.",
                      "Calculs afférents aux périodes antérieures inchangés ; étalement jusqu'à l'exercice 2015 conservé.",
                      "Aucune obligation de remplacement.",
                      "L'équivalence actuarielle prévue à l'article R. 932-4-14 est établie dans les conditions suivantes",
                      "Les calculs de la répartition des droits prévue à l'article R. 932-4-20 sont effectués")])
add('W02z', OBJ, CSS, sid, pA,
    "Coordination des renvois : le III organisait l'équivalence actuarielle de R932-4-14, abrogé au 31 décembre 2017, et le IV imposait les tables de A931-10-10, abrogé au 1er janvier 2016, ainsi qu'une méthode de calcul de la provision mathématique théorique que R932-4-15 en vigueur renvoie désormais à l'arrêté prévu à R441-21 du code des assurances. Le III et les calculs de provision et d'équivalence sont bornés aux périodes antérieures ; la répartition des droits de R932-4-20, dont les bases techniques sont fixées par arrêté, garde les tables et le taux du IV. Les I et II, les taux de 75 %, 60 %, 3,5 % et 1,5 % et l'étalement historique jusqu'à 2015 sont conservés. Aucune obligation nouvelle.",
    "I à IV et NOTA relus intégralement : 65 ans, 45 ans, vingt ans, produit des coefficients, 2007, huit années, 75 % et 60 %, plafond 3,5 %, alternative 1,5 %, étalement jusqu'à 2015 et exercice 2013 conservés. L932-24, R932-4-4, R932-4-15 et R932-4-20 lus en entier. Correction des notes antérieures : R932-4-14 et A931-10-10 ne sont pas absents de l'extraction ; ils figurent au corpus à l'état ABROGE (R932-4-14, LEGIARTI000006755189, fin 2017-12-31 ; A931-10-10, LEGIARTI000027896850, fin 2016-01-01). R932-4-15 (LEGIARTI000036332440) dispose : « Les conditions d'évaluation de la provision mathématique théorique mentionnée au premier alinéa sont fixées par l'arrêté prévu au premier alinéa de l'article R. 441-21 du code des assurances. » R932-4-20 (LEGIARTI000036332531) renvoie la répartition des droits à des « bases techniques définies par arrêté du ministre chargé de la sécurité sociale », que le IV continue de fournir. Les tables restent désignées par la rédaction antérieure de A931-10-10, faute de cible actuelle au corpus ; aucun renvoi alternatif n'est inventé. Arrêté R441-21 du code des assurances hors corpus. Correction de la troisième passe (objection AUDIT5-H198, audit 5) : renvois morts structurants neutralisés et provision théorique renvoyée à l'arrêté que désigne R932-4-15, sans changement des taux ni obligation nouvelle." + AI,
    dict(status='rewrite_draft', classification='coordination_only', substantive_impact=imp))

# ---------------------------------------------------------------- H228 : CGI 200, deux versions (A3)
OBJ = 'AUDIT5-H228'
OLD200 = "<p>1. Les contribuables domiciliés en France au sens de l'article 4 B bénéficient d'une réduction d'impôt sur le revenu égale à 66 % des dons et versements qu'ils effectuent, y compris les abandons exprès de revenus ou de produits. Ces sommes sont retenues dans la limite de 20 % du revenu imposable lorsqu'elles sont versées au profit :</p>"
NEW200 = "<p>1. Ouvrent droit à une réduction d'impôt sur le revenu égale à 66 % de leur montant, dans la limite de 20 % du revenu imposable, les dons et versements, y compris les abandons exprès de revenus ou de produits, effectués par les contribuables domiciliés en France au sens de l'article 4 B au profit :</p>"
for sid in ('LEGIARTI000053543932', 'LEGIARTI000053154489'):
    c = cur(CGI, sid); row = ROWS[(CGI, sid)]
    p = replace_once(c['proposed'], OLD200, NEW200)
    add('A3z', OBJ, CGI, sid, p,
        c['reason'] + " Troisième passe (AUDIT5-H228) : le chapeau du 1 est rétabli dans la structure de la source, la réduction de 66 % et la limite de 20 % ne visant que les dons et versements effectués au profit des organismes énumérés aux a à g.",
        c['notes'] + " Correction de la troisième passe (objection AUDIT5-H228, audit 5) : la reformulation du chapeau du 1 accordait la réduction de 66 % à « des dons et versements qu'ils effectuent », sans restriction, et ne rattachait l'énumération qu'à la limite de 20 % ; lue à la lettre, elle ouvrait la réduction à tout don, sans plafond hors des organismes listés, contrairement aux 3, 4 bis et 6 et au motif. Le chapeau reprend la structure de la source : « Ouvrent droit à une réduction d'impôt sur le revenu égale à 66 % de leur montant, dans la limite de 20 % du revenu imposable, les dons et versements [...] au profit : ». Taux, plafonds, catégories a à g, allègements de preuve et d'agrément et transitions inchangés ; même correction sur les deux versions (LEGIARTI000053543932 et LEGIARTI000053154489)." + AI,
        dict(substantive_impact=row['substantive_impact']))

# ---------------------------------------------------------------- H309 : travail R5212-2-3 à R5212-2-5
OBJ = 'AUDIT5-H309'
OETH_TRANS = "<p>Les droits, délais et recours nés avant cette date sont préservés.</p>"
NOTE_OETH = ("Correction des notes antérieures : L5212-5-1 n'est pas « absent » ni d'une portée « non vérifiable » ; sa seule version applicable, LEGIARTI000031597729, figure au corpus à l'état ABROGE (2016-01-01 → 2020-01-01), les versions LEGIARTI000037388700 et LEGIARTI000038610087 étant MODIFIE_MORT_NE ; R5212-1, R5212-2-1 et R5212-2-2 sont abrogés à la même date. Depuis, la déclaration relève de la DSN auprès de l'organisme de D5212-5 (D5212-8 proposé) et le rescrit sur l'obligation d'emploi relève de l'article L. 243-6-3 du code de la sécurité sociale, dont le I proposé dispose : « Ces organismes répondent également aux demandes portant sur l'obligation d'emploi des travailleurs handicapés » et le III : « La décision est opposable pour l'avenir à tous les organismes mentionnés au premier alinéa du I tant que la situation de fait exposée ou la législation appliquée n'ont pas été modifiées ». La procédure de l'Agefiph, sans base légale ni opposabilité à l'organisme de recouvrement, est abrogée ; l'absence de caducité et la durée illimitée voulues par le projet sont assurées par L243-6-3 (sans limite de durée) ; l'éventuelle suppression d'une caducité dans les dispositions réglementaires d'application de L243-6-3 (R243-43-x, non relues) est laissée à l'auteur. Correction de la troisième passe (objection AUDIT5-H309, audit 5) : abrogation des articles R5212-2-3 à R5212-2-5, sans demande ni formalité de remplacement, avec maintien des droits antérieurs.")
specs = [
 ('X6', 'LEGIARTI000033310292',
  "<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. L'article L. 5212-5-1, qui prévoyait la demande de prise de position de l'employeur auprès de l'association mentionnée à l'article L. 5214-1, étant abrogé, les demandes portant sur l'obligation d'emploi des travailleurs handicapés relèvent de l'article L. 243-6-3 du code de la sécurité sociale. Aucune demande, pièce ou déclaration de remplacement n'est exigée sur le fondement du présent article ; les demandes déjà adressées à l'association n'ont pas à être renouvelées sur ce fondement.</p>" + OETH_TRANS,
  "Abrogation de la demande de prise de position auprès de l'association de L. 5214-1 et de ses mentions obligatoires, fondées sur L. 5212-5-1 abrogé.",
  "La demande de l'employeur mentionnée au premier alinéa de l'article L. 5212-5-1",
  "les demandes portant sur l'obligation d'emploi des travailleurs handicapés relèvent de l'article L. 243-6-3 du code de la sécurité sociale"),
 ('Y06z', 'LEGIARTI000033310296',
  "<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. L'article L. 5212-5-1 étant abrogé, la complétude, la caducité, le délai de réponse et la modification des positions de l'association mentionnée à l'article L. 5214-1 ne sont plus organisés par le présent article ; la déclaration relative à l'obligation d'emploi est souscrite dans les conditions des articles L. 5212-5 et D. 5212-8, sans déclaration rectificative propre au présent article. Aucune demande, pièce ou déclaration de remplacement n'est exigée. Les déclarations et rectifications afférentes aux années antérieures restent régies par leurs règles propres.</p>" + OETH_TRANS,
  "Abrogation de l'instruction par l'association de L. 5214-1 des demandes de prise de position fondées sur L. 5212-5-1 abrogé, de leur caducité et des déclarations liées.",
  "La demande est réputée complète si, dans un délai de quinze jours",
  "la complétude, la caducité, le délai de réponse et la modification des positions de l'association mentionnée à l'article L. 5214-1 ne sont plus organisés par le présent article"),
 ('X6', 'LEGIARTI000033310299',
  "<p>Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente modification. L'article L. 5212-5-1 étant abrogé, les positions de l'association mentionnée à l'article L. 5214-1 ne reçoivent plus de durée de validité sur le fondement du présent article ; les décisions rendues sur l'obligation d'emploi des travailleurs handicapés en application de l'article L. 243-6-3 du code de la sécurité sociale sont opposables dans les conditions du III de cet article. Les positions notifiées antérieurement conservent les effets que leur attachaient les dispositions alors applicables ; aucune position expirée n'est rétablie.</p>" + OETH_TRANS,
  "Abrogation de la durée de validité des positions de l'association de L. 5214-1 prises sur le fondement de L. 5212-5-1 abrogé.",
  "la position prise par l'association mentionnée à l'article L. 5214-1 est valable cinq ans",
  "les positions de l'association mentionnée à l'article L. 5214-1 ne reçoivent plus de durée de validité sur le fondement du présent article"),
]
for grp, sid, body, scope, sq, pq in specs:
    c = cur(TRAV, sid)
    imp = impact('coordination_only',
                 "Abrogation d'un règlement d'application devenu sans base légale : la procédure de prise de position de l'Agefiph sur l'obligation d'emploi reposait sur L5212-5-1, abrogé au 1er janvier 2020 ; le rescrit opposable relève désormais des URSSAF, CGSS et MSA en application de L243-6-3 du code de la sécurité sociale.",
                 "Loi n° 2018-771 et décrets de 2019 non lus au JORF ; dates tirées du corpus LEGI. Dispositions réglementaires d'application de L243-6-3 (R243-43-x) non relues. Aucun solde national n'est établi.",
                 "Aucune charge nouvelle identifiée : aucune demande, pièce ou déclaration de remplacement ; le rescrit de L243-6-3 existe déjà et n'est pas modifié.",
                 [effect('coordination', 'rescrit-oeth-agefiph-sans-base-legale',
                          "Abrogation de la procédure de rescrit OETH de l'Agefiph, sans base légale depuis 2020.",
                          "Procédure de prise de position de l'Agefiph réaménagée par la proposition antérieure (caducité supprimée, durée illimitée).",
                          "Aucune procédure Agefiph ; rescrit opposable de L243-6-3 du CSS.",
                          'regime', "Employeurs assujettis à l'obligation d'emploi des travailleurs handicapés.",
                          "Droits, délais et recours nés avant l'abrogation préservés ; positions antérieures conservent leurs effets.",
                          "Aucune demande, pièce ou déclaration de remplacement.", sq, pq)])
    add(grp, OBJ, TRAV, sid, body,
        "Abrogation de coordination : l'article organisait la procédure de prise de position de l'association mentionnée à l'article L. 5214-1 (Agefiph) prévue par l'article L. 5212-5-1, abrogé au 1er janvier 2020 avec le passage de la déclaration à la DSN et du recouvrement aux URSSAF et à la MSA. Le rescrit opposable sur l'obligation d'emploi relève de l'article L. 243-6-3 du code de la sécurité sociale, sans limite de durée tant que la situation et la législation sont inchangées. Maintenir et réaménager une procédure concurrente sans base légale ni opposabilité laissait croire à l'employeur qu'il était couvert. Aucune formalité de remplacement ; droits antérieurs préservés.",
        "Source et proposition antérieure lues en entier, avec R5212-2-3 à R5212-2-5, L5212-5, L5214-1, D5212-8 et L243-6-3 du code de la sécurité sociale. " + NOTE_OETH + AI,
        dict(change_type='full_repeal', repeal_policy_id=POLICY, repeal_scope=scope,
             classification='coordination_only', substantive_impact=imp))

# ---------------------------------------------------------------- H160 : annexe II 371 ter A à H
OBJ = 'AUDIT5-H160'
CERT_COMMON = ("L'article 1649 quater N du code général des impôts, qui prévoyait la convention des certificateurs à l'étranger "
               "pour l'application du c du 1° du 7 de l'article 158 du même code, et ce 1° étant abrogés, aucune demande de "
               "convention n'est reçue ni instruite et aucune convention n'est conclue, renouvelée ou reconduite sur le "
               "fondement des articles 371 ter A à 371 ter H. Aucune déclaration, attestation, information des clients ou "
               "adhérents ni pièce de remplacement n'est exigée.")
CERT_TRANS = ("<p>Les impositions des périodes antérieures, ainsi que les contrôles, restitutions, prescriptions et recours qui "
              "s'y rapportent, restent régis par les règles qui leur étaient applicables.</p>")
cert = [
 ('LEGIARTI000033231158', "La délivrance de la convention et les justificatifs exigés à l'appui de la demande sont sans objet.",
  "Abrogation de la délivrance de la convention de certificateur à l'étranger et des justificatifs d'identité, de résidence et de moralité fiscale exigés à l'appui de la demande.",
  "La convention prévue à l'article 1649 quater N du code général des impôts est délivrée"),
 ('LEGIARTI000033231168', "Aucune demande de conventionnement n'est remise, aucun récépissé n'est délivré et aucune acceptation tacite ne naît sur son fondement.",
  "Abrogation de la remise des demandes de conventionnement, du récépissé, du délai de quatre mois et de l'acceptation tacite des conventions de certificateur à l'étranger.",
  "Les demandes de conventionnement, accompagnées des justificatifs désignés à l'article 371 ter A"),
 ('LEGIARTI000033231171', "Aucun refus ni aucune convention n'est notifié sur son fondement.",
  "Abrogation des motifs de refus, de la notification motivée et de l'envoi de la convention type des certificateurs à l'étranger fondés sur 1649 quater N.",
  "Le directeur général des finances publiques peut refuser de conclure la convention"),
 ('LEGIARTI000033231174', "Les conventions n'étant plus conclues, la règle d'incessibilité et d'intransmissibilité est sans objet.",
  "Abrogation de la règle d'incessibilité et d'intransmissibilité des conventions de certificateur à l'étranger, devenues sans base légale.",
  "La convention n'est ni cessible ni transmissible."),
 ('LEGIARTI000033231176', "Les conventions en cours à cette date prennent fin sans formalité ; leur fin n'appelle ni dénonciation ni information des clients ou adhérents.",
  "Abrogation de la durée triennale, de la reconduction, du renouvellement et de l'information des clients en cas de non-renouvellement des conventions de certificateur à l'étranger.",
  "La convention est conclue pour une période de trois ans."),
 ('LEGIARTI000033231196', "Aucun engagement de contrôle ni compte rendu de mission n'est exigé sur son fondement, y compris pour les missions en cours.",
  "Abrogation des engagements d'indépendance, de contrôle des déclarations et de compte rendu de mission souscrits par les certificateurs à l'étranger.",
  "Le demandeur s'engage par la convention"),
 ('LEGIARTI000033231198', "Aucune résiliation n'est prononcée et aucune information des clients ou adhérents n'est exigée sur son fondement.",
  "Abrogation de la résiliation pour manquement des conventions de certificateur à l'étranger et de l'information des clients qui s'y attache.",
  "Le directeur général des finances publiques peut résilier la convention"),
 ('LEGIARTI000033231201', "Le délai de deux ans avant le dépôt d'une nouvelle demande est sans objet, aucune demande n'étant plus reçue.",
  "Abrogation du délai de carence de deux ans avant une nouvelle demande de convention de certificateur à l'étranger, la procédure n'existant plus.",
  "ne peut déposer une nouvelle demande de convention qu'à l'expiration d'un délai de deux ans"),
]
for sid, spec_txt, scope, sq in cert:
    c = cur(A2, sid); row = ROWS[(A2, sid)]
    body = ("<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi de réforme. " + spec_txt + " "
            + CERT_COMMON + "</p>" + CERT_TRANS)
    imp = impact('coordination_only',
                 "Abrogation d'un règlement d'application sans base légale ni objet : la convention des certificateurs à l'étranger reposait sur 1649 quater N, abrogé le 16 février 2025, et ne servait qu'à l'application du c du 1° du 7 de l'article 158 (majoration de 1,25), lui-même abrogé.",
                 "Article 11 de la loi n° 2025-127 du 14 février 2025 non lu au JORF ; aucun article en vigueur du CGI ne mentionne plus les certificateurs à l'étranger dans le corpus. Arrêté fixant le modèle de convention hors corpus. Aucun solde national n'est établi.",
                 "Aucune charge nouvelle identifiée : l'abrogation ne crée aucune demande, attestation, information ni pièce de remplacement ; aucune majoration n'est rétablie.",
                 [effect('coordination', 'certificateurs-etranger-fin-regime-sans-base-legale',
                          "Abrogation du chapitre des conventions de certificateurs à l'étranger.",
                          "Procédure de convention des certificateurs à l'étranger maintenue et réformée par les propositions antérieures.",
                          "Aucune convention ni procédure ; impositions antérieures régies par les règles antérieures.",
                          'regime', "Professionnels et organismes établis dans l'UE ou l'EEE et leurs clients ou adhérents domiciliés en France.",
                          "À compter de l'entrée en vigueur de la loi de réforme ; conventions en cours éteintes sans formalité ; périodes antérieures inchangées.",
                          "Aucune déclaration, attestation, information ni pièce de remplacement.",
                          sq, "aucune demande de convention n'est reçue ni instruite et aucune convention n'est conclue, renouvelée ou reconduite")])
    ov = dict(status='rewrite_draft', change_type='full_repeal', repeal_policy_id=POLICY, repeal_scope=scope,
              classification='coordination_only', substantive_impact=imp)
    if row.get('benefit_review'):
        ov['benefit_review'] = ("Aucun avantage n'est retiré : la convention n'avait d'effet que pour écarter la majoration de 1,25 du c du 1° du 7 de l'article 158, abrogée, et 1649 quater N est abrogé depuis le 16 février 2025. Les impositions, restitutions et recours des périodes antérieures restent régis par les règles antérieures.")
    prior = c['notes'] or ''
    add('X6', OBJ, A2, sid, body,
        "Abrogation de coordination : le chapitre 371 ter A à 371 ter H organise la convention des certificateurs à l'étranger prévue par l'article 1649 quater N du CGI, abrogé depuis le 16 février 2025, et cette convention ne servait que pour l'application du c du 1° du 7 de l'article 158, abrogé dans la version en vigueur de cet article (« 1° ( Abrogé) »). Le chapitre est donc sans base légale et sans objet ; le maintenir et le réformer comme un régime vivant était une anomalie. Il est abrogé dans son ensemble, sans formalité de remplacement ; les impositions et recours des périodes antérieures restent régis par les règles antérieures.",
        "Lus : 371 ter A à 371 ter H (sources et propositions), CGI 1649 quater N (LEGIARTI000031768541, ABROGE, 2016-01-01 → 2025-02-16 : « Pour l'application du c du 1° du 7 de l'article 158 ») et CGI 158 en vigueur (LEGIARTI000054373673, 7 : « Ces dispositions s'appliquent : 1° ( Abrogé) »). Les articles 371 ter I à 371 ter S de la même annexe (commissions des valeurs locatives) sont sans rapport et ne sont pas touchés. Correction des notes antérieures : le maintien ou l'abrogation n'est plus laissé en suspens ; l'objet même du régime (majoration de 1,25 pour les non-adhérents) est abrogé, ce qui lève la réserve sur un transfert. Réserve : article 11 de la loi n° 2025-127 non lu au JORF ; s'il transférait le régime vers un autre fondement, les renvois seraient à réécrire au lieu d'abroger. Correction de la troisième passe (objection AUDIT5-H160, audit 5 ; lien avec RT-P1-ANNEXES-05) : abrogation d'ensemble de 371 ter A à 371 ter H, sans formalité de remplacement." + AI,
        ov)

# ---------------------------------------------------------------- write
for g, changes in GROUPS.items():
    folder = HOME / g
    folder.mkdir(exist_ok=True)
    out = dict(group=g, changes=changes, requests=[], skipped=[])
    (folder / 'changes.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(g, len(changes))
