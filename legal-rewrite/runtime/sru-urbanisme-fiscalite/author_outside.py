from pathlib import Path
import hashlib, html, json, re, sqlite3, xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
OUT = HERE / 'outside-companion'
OUT.mkdir(exist_ok=True)
existing_members = {a['source_id']: a.get('provenance', {}).get('article_member') for a in json.loads((OUT / 'manifest.json').read_text()).get('articles', [])} if (OUT / 'manifest.json').exists() else {}
db = sqlite3.connect(BASE / 'corpus.sqlite')
db.row_factory = sqlite3.Row
records = json.loads((HERE / 'outside-sources-consolidated.json').read_text())['current_candidates']
by = {r['number']: r for r in records}
final = HERE / 'outside-final-targets.json'
if final.exists():
    targets = json.loads(final.read_text())['articles']
else:
    targets = list({r['number']: r for r in json.loads((HERE / 'cibs-corrected-sources.json').read_text())}.values())
    targets += [r for r in json.loads((HERE / 'outside-targeted-sources.json').read_text()) if r['number'] == '15'][-1:]
by.update({r['number']: r for r in targets})

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def p(s): return '<p>' + html.escape(s, quote=False) + '</p>'
def clean(s):
    s = re.sub(r'\s+(?:border|align)="[^"]*"', '', s)
    return s.strip()
def replace(body, before, after):
    assert body.count(before) == 1, before
    return body.replace(before, after)

articles = []
def add(number, body, reason, review, removed=None, kind='code_article'):
    a = dict(by[number])
    a['kind'] = kind
    if kind == 'noncodified_article':
        a['code_id'] = 'LEGITEXT000053099709'
        a['title'] = 'Ordonnance n° 2025-1247 du 17 décembre 2025 — article 15, version issue de l’ordonnance n° 2026-671 du 27 juillet 2026'
        a['source_url'] = 'https://www.legifrance.gouv.fr/loda/article_lc/' + a['source_id']
    else:
        a['source_url'] = 'https://www.legifrance.gouv.fr/codes/article_lc/' + a['source_id']
        a['title'] = ({'LEGITEXT000006070633':'Code général des collectivités territoriales', 'LEGITEXT000006070299':'Code général de la propriété des personnes publiques', 'LEGITEXT000044595989':'Code des impositions sur les biens et services'}[a['code_id']] + ' — article ' + number)
    node = ET.fromstring(a['whole_article_xml'])
    note = node.find('NOTA/CONTENU')
    a['source_notes_xml'] = ((note.text or '') + ''.join(ET.tostring(c, encoding='unicode') for c in note)) if note is not None else ''
    a['source_state'] = node.findtext('META/META_SPEC/META_ARTICLE/ETAT')
    a['source_article_raw_sha256'] = a['source_sha256']
    a['source_body_sha256'] = sha(a['source_xml'])
    arc = db.execute('SELECT * FROM archives WHERE name=?', (a['archive'],)).fetchone()
    assert arc is not None and arc['complete'] == 1
    a['provenance'] = {'provider':'DILA — LEGI', 'archive':a['archive'], 'archive_sha256':arc['sha256'], 'archive_source_url':arc['source_url'], 'article_member':a.get('archive_member') or existing_members.get(a['source_id']), 'source_method':'XML DILA intégral ; stock et mises à jour officielles disponibles rejouées jusqu’au 18 octobre 2026.'}
    a['proposed_xml'] = clean(body)
    a['proposed_sha256'] = sha(a['proposed_xml'])
    a['reason'] = reason
    a['review_notes'] = review
    a['status'] = 'proposal_not_adopted'
    a['prior_proposal_sha256'] = None
    a['excluded_from_30317_counter'] = True
    if removed:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    else:
        a['change_type'] = 'normative_coordination'
    articles.append(a)

old_geo = 'dans des communes de plus de 15 000 habitants en forte croissance démographique identifiées en application des dispositions du dernier alinéa du II de l\'article L. 302-5 du code de la construction et de l\'habitation'
new_geo = 'dans les communes figurant sur la liste des communes de plus de 15 000 habitants en forte croissance démographique en vigueur la veille de l’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux'
for number in ('L2252-2', 'L3231-4-1', 'L4253-2'):
    body = replace(by[number]['source_xml'], old_geo, new_geo)
    body += p('Le périmètre de cette dernière liste est maintenu à la seule fin du II du présent article, indépendamment de tout quota communal, constat de carence ou inventaire de logements sociaux. Il ne crée ni nouvelle garantie ni nouvelle procédure de classement, d’inventaire ou de collecte de données au titre des anciens quotas. Les garanties et cautionnements valablement accordés avant cette entrée en vigueur demeurent régis par leurs conditions légales et contractuelles, sans extension automatique de leur objet ou de leur montant.')
    add(number, body,
        'Conserver le champ géographique de la dérogation aux plafonds de garanties d’emprunts sans maintenir un classement communal SRU ou ouvrir de nouvelles garanties locales.',
        'Source, notes et version intégrales lues. I, bénéficiaires, prêts, opérations d’aménagement et deux conditions du II conservés. La première branche géographique reste celle de l’article 1406 bis du CGI ; la seconde est figée à la liste en vigueur la veille de la réforme, sans extension à toute commune dépassant 15 000 habitants. Même choix géographique autonome que L151-22 II proposé, sans dépendance à un nouvel inventaire. Aucune nouvelle dépense, garantie, compensation ou règle de responsabilité créée. La liste ancienne reposait sur deux critères distincts de R302-14 III : croissance démographique et pression sur la demande ; ils ne sont pas transformés en nouveau classement.')

body = replace(by['R3211-15']['source_xml'], '<p>3° La contribution du programme de logements à la réalisation des objectifs assignés, le cas échéant, à la commune, en application des dispositions de l\'article L. 302-5 du code de la construction et de l\'habitation ; </p>', '<p>3° Abrogé ;</p>')
body += p('VII. – La suppression du critère du 3° du III s’applique aux décisions accordant une décote prises à compter de l’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux. Elle ne remet pas en cause les cessions et conventions de décote antérieurement valablement conclues, les droits des tiers ou les obligations indépendantes de ces quotas. Les autres critères du III, les fourchettes du IV et les modalités des V et VI demeurent applicables ; aucun droit général à révision du prix, restitution ou indemnisation des cessions antérieures n’est créé.')
add('R3211-15', body,
    'Supprimer le seul critère de décote fondé sur les objectifs communaux SRU, tout en conservant les aides foncières, leurs critères autonomes et toutes les fourchettes de décote.',
    'Les I à VI, catégories 1/2/3, leurs logements et assimilations, critères III 1°/2°/4°/5°, pondération de surface et calcul global sont maintenus. Tableau intégral : trois zones et trois catégories, fourchettes 0–50/75/100 %, 0–35/50/75 %, 0–25/35/50 %. Le III 3° est seul abrogé, avec numérotation conservée. VII opère la transition pour les décisions nouvelles ; aucune annulation automatique d’un contrat antérieur. L3211-7 reste un régime autonome et n’est pas réécrit ici.',
    ['Suppression du critère de majoration de la décote lié à la contribution aux objectifs de logements sociaux assignés à la commune en application de L302-5.'])

future_start = '2027-01-01'
body = replace(by['L231-66']['source_xml'], '4° Lorsqu\'il n\'est pas situé dans un quartier prioritaire de la politique de la ville, il remplit les conditions de proximité avec des logements locatifs sociaux déterminées par décret ;', '4° Abrogé ;')
body += p('La suppression de la condition du 4° prend effet à la plus tardive des deux dates suivantes : la date d’entrée en vigueur du présent article prévue par l’ordonnance n° 2026-671 du 27 juillet 2026, ou la date d’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux. Elle concerne les livraisons et travaux dont le fait générateur intervient à compter de cette date, sans droit général au remboursement de la taxe afférente aux faits générateurs antérieurs. Les autres conditions, dates et régimes d’application de la recodification restent inchangés.')
body += p('La condition de proximité, de proportion de logements sociaux dans la commune ou de mixité du programme supprimée au 4° ne peut être rétablie par les mesures réglementaires prises pour l’application du présent article ou par le maintien transitoire du II de l’article 279-0 bis A du code général des impôts. Les opérations, contrats et droits déjà valablement engagés sont préservés dans les conditions du V de l’article L. 302-5 du code de la construction et de l’habitation.')
add('L231-66', body,
    'Coordonner la définition du logement intermédiaire destinée à entrer en vigueur en 2027 avec la suppression des conditions de proximité et de mixité de l’ancien article 279-0 bis A du CGI.',
    'Source intégrale à entrée différée au 1er janvier 2027, non présentée comme droit applicable au 18 octobre 2026. L’ancien L221-66 a été modifié mort-né le 29 juillet 2026 ; il n’est pas la cible. Maintien des ressources, loyers, localisation, résidence principale, exclusion du logement social et nouveau 5° relatif à construction neuve/travaux aboutissant à immeuble neuf. Seul 4° abrogé, numérotation conservée. Transition opératoire coordonnée avec le III proposé de CGI 279-0 bis A et l’article 15 de l’ordonnance 2025-1247 ; aucune anticipation de la recodification, aucun nouveau taux, aucune restitution générale.',
    ['Suppression de la condition de proximité avec des logements locatifs sociaux et de la délégation au décret qui pourrait recréer la condition de mixité sociale supprimée du régime de TVA du logement intermédiaire.'])

body = replace(by['L231-67']['source_xml'], '2° Le 4° de l\'article L. 231-66 n\'est pas applicable.', '2° Abrogé.')
body += p('La suppression du 2° prend effet à la même date et selon les mêmes règles temporelles que la suppression du 4° de l’article L. 231-66. Le plafond du prix des services non individualisables prévu au 1° demeure applicable. Aucun nouveau critère de proportion ou de proximité de logements sociaux n’est exigé du seul fait de cette coordination ; les droits relatifs aux opérations et faits générateurs antérieurs suivent les mêmes dispositions transitoires.')
add('L231-67', body,
    'Supprimer le renvoi devenu sans objet à l’exception de proximité propre aux résidences-services, sans supprimer le plafond du prix de leurs services.',
    'Source future intégrale lue, à effet au 1er janvier 2027. 1° conservé, 2° abrogé à la date de suppression du 4° de L231-66 ; aucune nouvelle condition ni suppression du plafond. L’ancien L221-67 modifié mort-né n’est pas réécrit comme norme courante. La transition de L231-66 fournit le fait générateur et la préservation des situations antérieures.',
    ['Suppression de l’exception au 4° de L231-66 devenue sans objet après abrogation de la condition générale de proximité avec le parc locatif social.'])

body = replace(by['15']['source_xml'], '3° du I et II de l\'article 279-0 bis A', '3° du I de l\'article 279-0 bis A')
body = replace(body, '3° et 4° de l\'article L. 231-66', '3° de l\'article L. 231-66')
body += p('Par dérogation au premier alinéa, la suppression du 4° du I et du II de l’article 279-0 bis A du code général des impôts par la loi supprimant les quotas communaux obligatoires de logements sociaux prend effet selon le III de cet article, sans attendre l’entrée en vigueur de dispositions réglementaires. Le maintien transitoire prévu au présent article ne s’applique pas aux conditions de proportion de logements sociaux dans la commune, de mixité du programme ou de proximité supprimées par cette loi.')
body += p('Pour les livraisons et travaux dont le fait générateur est postérieur à l’entrée en vigueur de cette loi, aucune mesure réglementaire de reprise du 3° du I de l’article 279-0 bis A ou d’application de l’article L. 231-66 du code des impositions sur les biens et services ne peut rétablir ces seules conditions supprimées. Le 3° de ce dernier article conserve son seul objet de localisation géographique ; le 4° est supprimé dans les conditions temporelles prévues par sa nouvelle rédaction.')
body += p('Les autres lignes du tableau, les autres conditions fiscales et les autres dates de la recodification demeurent inchangées. Aucun droit général au remboursement d’une taxe afférente à un fait générateur antérieur n’est créé. Les opérations, contrats et droits déjà valablement engagés sont préservés dans les conditions du V de l’article L. 302-5 du code de la construction et de l’habitation.')
add('15', body,
    'Empêcher la table de transfert réglementaire de maintenir indéfiniment l’ancien II du CGI 279-0 bis A ou d’autoriser sa recréation par décret après suppression des quotas et des conditions de mixité correspondantes.',
    'Article 15 actuel intégral lu, en vigueur depuis le 29 juillet 2026 ; version modifiée par l’article 2 de l’ordonnance 2026-671. Toutes les lignes et cellules du tableau sont conservées ; seule la ligne 279-0 bis A est coordonnée : maintien du transfert géographique du 3° I vers L231-66 3°, retrait du II et de la délégation L231-66 4°. Le paragraphe dérogatoire rend la suppression immédiate selon le III proposé du CGI sans attendre le décret de reprise. Le relais au 1er janvier 2027 ne rétablit pas les conditions supprimées. Les autres reports et régimes de TVA ne sont pas modifiés.',
    ['Suppression du maintien transitoire et de la délégation réglementaire permettant de faire survivre ou réintroduire le II de CGI 279-0 bis A relatif aux proportions de logements sociaux dans la commune et à la mixité sociale du programme.'], kind='noncodified_article')

manifest = {'title':'Candidats de coordination hors corpus — suppression des quotas communaux SRU', 'as_of':'2026-10-18', 'status':'candidate_not_registered_not_published', 'outside_code_inventory':True, 'excluded_from_30317_counter':True, 'articles':articles, 'consolidation_notes':[
    'Les sources XML intégrales, notes, dates, états et empreintes sont distincts des propositions. Aucune source synchronisée ni base n’a été modifiée.',
    'Rejeu du stock DILA et de 466 mises à jour disponibles jusqu’au 18 octobre 2026 pour les renvois CGCT/CG3P. Rejeu supplémentaire pour les deux futures dispositions CIBS et l’article 15 ; leur date différée ne les fait pas compter comme dispositions déjà en vigueur.',
    'Les L221-66 et L221-67 initialement envisagés ont été modifiés mort-nés avant leur date d’effet. Les véritables cibles différées sont L231-66 et L231-67, au 1er janvier 2027.',
    'Ce lot sécurise les coordinations de quotas engagées avant l’élargissement de la demande à toute la loi SRU de 2000. Il ne prétend pas accomplir cette abrogation générale ni supprimer ses autres descendants.',
]}
(OUT/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles':len(articles), 'numbers':[a['number']for a in articles]}, ensure_ascii=False))
