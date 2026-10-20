from pathlib import Path
import hashlib, json, sqlite3, sys, xml.etree.ElementTree as E

H = Path(__file__).resolve().parent
B = H.parents[1]
OUT = B / 'runtime/sru-integral/collectivites-candidates/001'
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(B))
from run_exhaustive import validate_answer

db = sqlite3.connect('file:' + str(B/'corpus.sqlite') + '?mode=ro', uri=True)
db.row_factory = sqlite3.Row
requested = [('LEGITEXT000006074096','L302-1'),('LEGITEXT000006074075','L510-1'),('LEGITEXT000006074096','L424-2'),('LEGITEXT000006074096','R*442-3-3'),('LEGITEXT000006074096',"Annexe à l'article R422-1")]
sources = []
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
for code, num in requested:
    r = db.execute('SELECT * FROM articles WHERE code_id=? AND number=? AND valid_from<=? AND valid_until>?', (code,num,'2026-10-18','2026-10-18')).fetchall()
    assert len(r) == 1
    r = dict(r[0])
    doc = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", (code,r['id'])).fetchone()[0]
    raw = doc.decode() if isinstance(doc,bytes) else doc
    assert sha(raw) == r['source_sha256']
    node = E.fromstring(raw)
    notes = node.find('NOTA/CONTENU')
    notes_xml = ((notes.text or '') + ''.join(E.tostring(c,encoding='unicode')for c in notes)) if notes is not None else ''
    prior = db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?', (code,r['id'])).fetchone()
    prior = dict(prior) if prior else None
    if prior:
        prior['proposed_sha256'] = sha(prior['proposed_xml']) if prior['proposed_xml'] else None
    sources.append({'code_id':code,'source_id':r['id'],'number':num,'source_sha256':r['source_sha256'],'source_xml':r['content_xml'],'source_notes_xml':notes_xml,'whole_article_xml':raw,'valid_from':r['valid_from'],'valid_until':r['valid_until'],'source_state':r['state'],'source_archive':r['archive'],'source_url':'https://www.legifrance.gouv.fr/codes/article_lc/'+r['id'],'previous_draft':prior})

by = {a['number']:a for a in sources}
rows = []
def base(num):
    a = by[num]
    return a['previous_draft']['proposed_xml'] if a['previous_draft'] and a['previous_draft']['proposed_xml'] else a['source_xml']
def replace(body, old, new):
    assert body.count(old) == 1, old
    return body.replace(old,new)
def add(num, body, reason, review, removed=None, repeal=None):
    a=by[num]
    r={k:a[k]for k in ('code_id','source_id','source_sha256','number')}
    r.update(proposed_xml=body,status='rewrite_draft',reason=reason,review_notes=review,prior_proposal_sha256=a['previous_draft']['proposed_sha256'] if a['previous_draft'] else None)
    if removed:
        r.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
    if repeal:
        r.update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope=repeal)
    rows.append(r)

body = replace(base('L302-1'), "<p>À Paris, Marseille et Lyon, les maires d'arrondissement ou leurs représentants participent à l'élaboration de ce programme.</p>", "<p>À compter de l’entrée en vigueur de la loi abrogeant la loi n° 2000-1208 du 13 décembre 2000, la participation des maires d’arrondissement de Paris, Marseille et Lyon ou de leurs représentants à l’élaboration du programme n’est plus exigée sur le seul fondement du présent article. Les programmes adoptés, les consultations déjà réalisées et les droits antérieurement valablement constitués ne sont pas remis en cause de ce seul fait. Les modalités de consultation disposant d’un fondement légal distinct demeurent applicables.</p>")
body = replace(body, 'ni aux obligations de logement social.', 'ni aux obligations de logement social disposant d’un fondement légal distinct des quotas communaux et objectifs de rattrapage abrogés.')
add('L302-1',body,
    'Supprimer la participation obligatoire des maires d’arrondissement introduite par l’article 58 SRU, tout en conservant les autres règles et le projet antérieur intégral du PLH ; borner sa clause générale aux obligations sociales autonomes pour ne pas rétablir les quotas abrogés.',
    'Source actuelle, notes et proposition antérieure lues entièrement. La phrase du second alinéa du I reprend exactement SRU 58 et subsiste dans la version du 21 février 2026. Ce deuxième alinéa devient la transition de suppression, sans déplacement des autres alinéas. Les I à IV, six ans, observatoires trois ans, cinq catégories de recensement, typologies, seuils 30 000/10 000 et date du 1er mars 2014 restent conservés, de même que les ajouts antérieurs sur densification, réseaux et financement explicité. Le dernier alinéa désignant les EPCI reste à sa place pour L302-4-1. Aucune réouverture automatique des PLH adoptés. La note fiscale 2027 source ne fixe pas la date de cette abrogation. Le PLH lui-même précède SRU et n’est pas supprimé en bloc.',
    ['Suppression de la seule participation obligatoire des maires d’arrondissement de Paris, Marseille et Lyon au PLH créée par SRU 58, sans procédure consultative de remplacement.'])

body = replace(base('L510-1'), ' par la politique de la ville relatives notamment au développement du logement social et de la mixité sociale,', ' par la politique de la ville,')
body += '<p>VII. – La suppression du critère spécifique relatif au développement du logement social et de la mixité sociale, introduit au second alinéa du I par l’article 70 de la loi n° 2000-1208 du 13 décembre 2000, s’applique aux décisions d’agrément prises à compter de l’entrée en vigueur de la loi portant cette suppression. Les agréments, conventions et droits des tiers antérieurement valablement constitués ne sont pas annulés ou réécrits automatiquement ; les voies ordinaires de modification et de recours restent ouvertes. Les autres critères, compétences et procédures du présent article demeurent applicables, sous réserve des règles relatives à l’application de la loi répressive plus douce aux sanctions non définitives.</p>'
add('L510-1',body,
    'Retirer seulement le critère spécifique ajouté par SRU 70 3° à la décision d’agrément, sans abroger le régime d’agrément antérieur, l’équilibre habitat/activités ou ses autres fondements.',
    'Source et note actuelles lues entièrement ; aucun projet antérieur. Article 70 1° et 2° censurés dans le texte promulgué, donc non réintroduits et non comptés comme normes à supprimer. Le 3° ajoutait exactement « relatives notamment au développement du logement social et de la mixité sociale », toujours présent en 2026. I à VI, champ industriel/commercial/etc., conventions, Ile-de-France, date 1er janvier 1995, pouvoir réglementaire, bilan et sanctions conservés. VII applique le retrait aux décisions nouvelles, protège les prescriptions et conventions déjà valablement constituées, réserve la loi répressive plus douce. La note de la loi de finances 2026 à effet au 1er janvier 2026 est conservée comme note source ; elle n’est pas la date de notre réforme.',
    ['Suppression du seul critère de décision d’agrément propre au développement du logement social et de la mixité sociale inséré par SRU 70 3°, sans suppression des autres critères et contrôles de l’agrément.'])

add('L424-2',
    '<p>Le présent article est abrogé à compter de l’entrée en vigueur de la loi abrogeant la loi n° 2000-1208 du 13 décembre 2000.</p><p>Cette abrogation met fin, pour l’avenir, à l’habilitation spéciale des organismes d’habitations à loyer modéré à participer aux actions de développement à caractère social prévues au présent article, y compris dans son champ géographique ultérieurement étendu. Elle ne remet pas en cause les contrats, opérations, aides et droits des tiers antérieurement valablement engagés ou constitués, ni les créances légalement nées à leur titre. Leur exécution et leurs voies ordinaires de modification, de contrôle et de recours demeurent régies par les règles qui leur sont applicables. Les compétences des organismes disposant d’un fondement légal distinct ne sont ni supprimées ni étendues par la présente abrogation.</p>',
    'Abroger l’habilitation spéciale créée par SRU 69, y compris son extension géographique de 2018 qui se rattache au même pouvoir ; préserver contrats, aides, créances et compétences légales distinctes.',
    'Texte initial de SRU 69, deux versions canoniques de L424-2, source et note actuelles entièrement lues ; aucune proposition antérieure. Création au 14 décembre 2000, puis rédaction de l’article 88 de la loi 2018-1021 du 23 novembre 2018 : quartiers prioritaires/contrats de ville et logements hors zones tendues. Une seule habilitation facultative, sans autre dispositif autonome dans l’article. Les deux coordinations réglementaires indispensables sont fournies dans ce même lot : retrait du seul renvoi dans R*442-3-3 et du seul 28° de la clause 3 de l’Annexe à R422-1. Le renvoi homonyme urbanisme R*423-4 concerne le L424-2 du code de l’urbanisme et reste distinct. Aucun remboursement général ni extinction des contrats déjà engagés.',
    repeal='Habilitation spéciale des organismes HLM à participer aux actions de développement social issue de SRU 69 et son extension géographique directement rattachée à cette habilitation.')

body = replace(base('R*442-3-3'), "Pour l'application de l'article L. 424-2, de l'article L. 442-3-1,", "Pour l'application de l'article L. 442-3-1,")
add('R*442-3-3',body,
    'Retirer le seul renvoi à l’habilitation L424-2 abrogée, sans supprimer le zonage autonome applicable aux quatre autres dispositifs de logement.',
    'Source et note vide lues entièrement ; aucun projet antérieur. Restent L442-3-1, I L442-3-3, I L442-3-4 et L442-5-2, l’arrêté ministériel, la référence h du 1 I CGI 31 et le critère de tension la plus forte. Aucune commune n’entre ou ne sort du zonage par cette simple suppression de référence. Les transitions propres aux autres dispositions ne sont pas déplacées.',
    ['Suppression de la seule mention de L424-2 dans le champ d’application du zonage réglementaire, l’habilitation spéciale de cet article étant abrogée.'])

body = replace(base("Annexe à l'article R422-1"), '<p>28° De participer, en application de l\'article L. 424-2 du code de la construction et de l\'habitation, à des actions de développement à caractère social d\'intérêt direct pour les habitants des quartiers d\'habitat social, dans le cadre des contrats de ville conclus en application de l\'article 27 de la loi n° 99-533 du 25 juin 1999 d\'orientation pour l\'aménagement et le développement durable du territoire ;</p>', '<p>28° Abrogé. Le retrait de cette habilitation statutaire s’applique à compter de l’entrée en vigueur de l’abrogation de l’article L. 424-2, sous les mêmes dispositions transitoires pour les contrats, opérations, aides et droits des tiers antérieurement valablement engagés ou constitués ;</p>')
add("Annexe à l'article R422-1",body,
    'Supprimer uniquement la faculté statutaire du 28° de la clause 3 reprenant l’habilitation SRU L424-2, en conservant intégralement les autres clauses des statuts types.',
    'Annexe entière de 24 478 caractères et note vide lues ; aucun projet antérieur. Toutes les clauses 1 à 17, les deux versions de gouvernance de la clause 7, les mentions à compléter propres au formulaire officiel et les rubriques 1° à 35° de l’objet social restent intégrales ; seul 28° devient abrogé avec transition. Maintien notamment des missions autonomes d’accompagnement et de prestations sociales 4°/10°/25° : elles ne sont pas supprimées par analogie. Les autres chiffres, capital, prix symbolique, délais, réserves et plafonds de dividende restent inchangés. Le renvoi obsolète de ce 28° à la loi 1999-533 n’est pas transféré vers une autre habilitation. Aucun résumé ni disparition de partie longue.',
    ['Suppression du seul 28° de la clause 3 des statuts types des sociétés anonymes HLM, qui réitérait l’habilitation spéciale de développement social créée par SRU 69.'])

validate_answer(rows,sources)
(OUT/'source.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
(OUT/'candidates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
proof={'status':'validated_not_registered','articles':[{k:a[k]for k in ('number','source_id','source_sha256','prior_proposal_sha256')}|{'proposed_sha256':sha(a['proposed_xml'])}for a in rows], 'source_and_notes_read_complete':True, 'previous_proposals_read_complete':True, 'validation':'validate_answer passed', 'registered':False, 'published':False}
(OUT/'validation.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print('VALIDATED',len(rows))
