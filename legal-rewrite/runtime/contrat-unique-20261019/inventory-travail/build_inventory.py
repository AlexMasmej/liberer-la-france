from pathlib import Path
import collections, datetime, hashlib, html, json, re, sqlite3, sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from ingest import source_notes
from run_exhaustive import mentions_possible_relief

export = ROOT / 'runtime/export-source/travail.json'
export_rows = json.loads(export.read_text())
db = sqlite3.connect('file:' + str(ROOT / 'corpus.sqlite') + '?mode=ro', uri=True)
db.execute('BEGIN')
code = 'LEGITEXT000006072050'
sources = {r[0]:r for r in db.execute('SELECT id,number,content_xml,source_sha256,valid_from,valid_until FROM articles WHERE code_id=?', (code,))}
drafts = {r[0]:r for r in db.execute('SELECT source_id,source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=?', (code,))}
core = {'L1221-2','L1231-1','R1221-34','L1524-1'} | {f'L1221-{n}' for n in range(19,27)} | {f'L1234-{n}' for n in range(1,19)} | {'L1234-17-1'} | {f'L1237-{n}' for n in [1,6,7,10,13]} | {f'R1234-{n}' for n in [1,2,4,5]}
core |= {'L1226-20','L1226-4-3','L1237-18-1','L1233-68','L1233-72-1'}
assert len(core)==45
read = core | {f'L1221-{n}' for n in range(1,9)} | {'L1221-5-1','L1221-18'} | {f'L1231-{n}' for n in range(1,6)} | {f'L1232-{n}' for n in range(1,7)} | {f'L1234-{n}' for n in range(19,21)} | {f'L1237-{n}' for n in range(1,17)} | {'L1237-1-1','R1237-13'}
read |= {f'L1233-{n}' for n in [1,2,3,4,5,15,16]} | {f'L1235-{n}' for n in [1,2,3,4,5]} | {'L1235-2-1','L1235-3-1'}
read |= set('L1225-4 L1225-34 L1225-66 L1226-2-1 L1226-4 L1226-4-3 L1226-9 L1226-12 L1226-14 L1226-15 L1226-19 L5213-9 L1236-8 L1236-9 L1251-58-1 L1251-58-2 L1251-58-4 L1254-7 L6222-7 L6222-16 L6222-18 L6222-18-2 L6222-19 L6325-5 L6325-6 L6325-7 L5132-5 L5134-24 L5134-25 L5134-69 L5134-71 L7112-2 L7112-3 L7112-4 L7112-5 L7313-9 L7313-11 L7313-12 L7313-13 L1111-2 L2253-1 L3322-2 L4154-1 L4154-2 L4154-3 L5422-1 L6324-1 L6324-3 L6324-5 L6324-6 L1254-8 L1254-13 L1254-16 L1254-17 L1254-18 L1254-19 L5132-6 L5132-11-1 L5132-15-1 L3123-33 L3123-34 L7221-2 L1331-2 L3141-28'.split())
read |= {f'L1223-{n}' for n in range(5,10)} | {f'L1251-{n}' for n in [11,12,14,15,26,28,32,33,39,40]} | {'L1254-9'}

def plain(s): return ' '.join(html.unescape(re.sub('<[^>]*>',' ',s or '')).split())
def refs(s): return sorted(set(re.sub(r'[.\s]','',v).upper() for v in re.findall(r'\b(?:LO|[LRDA])\.?\s*\d{1,5}(?:\s*-\s*\d+[A-Za-z]*)+', plain(s), re.I)))
def category(a):
    n=a['number']; cats=[]
    if n in core: cats.append('noyau_45')
    if re.match(r'^[LRD]124', n):cats.append('cdd_integral_70')
    if re.match(r'^[LRD]1251-',n):cats.append('interim_integral')
    if re.match(r'^[LRD]6222-',n) or n=='L6221-1':cats.append('apprentissage_contrat')
    if re.match(r'^[LRD]6325-',n):cats.append('professionnalisation')
    if re.match(r'^[LRD]6324-',n):cats.append('reconversion')
    if re.match(r'^[LRD]1254-',n):cats.append('portage_salarial')
    if re.match(r'^[LRD](1223|1236|1252|1253|7112|7313)-',n) or n.startswith(('L7221-','L7121-','L7123-')) or n in {f'L3123-{i}' for i in range(33,38)}:cats.append('autres_contrats_speciaux')
    if re.match(r'^[LRD](5132|5134)-',n):cats.append('insertion_contrats_aides')
    if re.match(r'^[LRD]1233-',n):cats.append('licenciement_economique_integral')
    if re.match(r'^[LRD]1235-',n):cats.append('contentieux_rupture')
    if n in read:cats.append('lecture_integrale_source_notes_effectuee')
    if re.match(r'^L(1225|1226|2411|2412|2413|2421|2422)-',n) or n=='L5213-9':cats.append('protections_rupture')
    s=plain(a['source_xml']+' '+a.get('proposed_xml',''))
    if re.search(r'contrats? (?:de travail )?à durée déterminée|\bCDD\b',s,re.I):cats.append('mention_cdd')
    r=set(refs(a['source_xml']))|set(refs(a.get('proposed_xml','')))
    if any(re.match(r'^[LRD]124',v) for v in r):cats.append('renvoi_titre_cdd')
    if r & core:cats.append('renvoi_noyau')
    if re.search(r'préavis|indemnité de licenciement|période d.essai',s,re.I):cats.append('mention_preavis_indemnite_essai')
    return cats

facts = {
 'L1221-2':'Le CDI reste seulement la forme normale ; le second alinéa autorise expressément le CDD.',
 'L1221-19':'Le projet enregistré conserve trois mois pour les trois catégories et protège les anciens contrats.',
 'L1221-21':'Le projet interdit le renouvellement des nouveaux CDI mais maintient les anciens essais.',
 'L1221-25':'Le texte conserve 24 h, 48 h, deux semaines et un mois ; deux semaines ne sont pas quinze jours calendaires. L’indemnité de prévenance est distincte de l’indemnité ordinaire de rupture.',
 'L1221-26':'Le départ du salarié en essai conserve 48 h ou 24 h, incompatible avec quinze jours sans coordination.',
 'L1231-1':'Le titre entier reste exclu pendant l’essai, donc une nouvelle règle générale de quinze jours ne suffit pas seule.',
 'L1234-1':'Préavis actuel par ancienneté : moins de six mois selon règles collectives/usages, puis un mois et deux mois ; exception de faute grave et priorité plus favorable.',
 'L1234-8':'Le préavis dépend de deux seuils d’ancienneté destinés à disparaître pour les nouveaux contrats ; exception des élus locaux à conserver dans l’ancien régime.',
 'L1234-9':'Projet enregistré : ouverture après huit mois ; part nouvelle 0,20 mois/an plafonnée à six mois ; part antérieure préservée. La nouvelle franchise doit viser moins d’un an et le calcul doit utiliser l’ancienneté totale au seuil, préavis inclus.',
 'L1234-12':'Force majeure : dispense actuelle du préavis et de l’indemnité ; conflit à traiter explicitement avec les quinze jours pour les nouveaux contrats.',
 'L1234-13':'Sinistre de force majeure : indemnité spéciale équivalente au préavis plus indemnité de licenciement ; ne pas supprimer le préavis payé au titre de la franchise ordinaire.',
 'L1234-15':'Droit local : un jour, une semaine, quinze jours ou six semaines selon rémunération.',
 'L1234-16':'Droit local : six semaines pour catégories spéciales.',
 'L1234-17-1':'Droit local applicable aussi à la démission et priorité aux délais plus longs.',
 'L1237-1':'Démission : préavis fixé par loi, conventions ou usages, sans durée uniforme.',
 'L1237-7':'Mise à la retraite : minimum indexé sur L1234-9 ; le projet protège la part antérieure et le fait générateur propre.',
 'L1237-9':'Départ volontaire à la retraite : indemnité spéciale distincte, sans assimilation automatique à la nouvelle indemnité ordinaire employeur.',
 'L1237-13':'Quinze jours calendaires de rétractation, pas de préavis ; indemnité spécifique de rupture amiable indexée sur L1234-9 sans condition minimale d’ancienneté à importer mécaniquement.',
 'R1237-13':'Quinze jours de mise en demeure d’abandon de poste ; ce délai ne vaut pas préavis de démission.',
 'L1223-6':'Mission export : minimum proratisé de licenciement sans condition d’ancienneté, en conflit avec une franchise générale non réservée.',
 'L1236-8':'Fin de chantier déjà assimilée à une cause réelle et sérieuse de rupture d’un CDI ; ce contrat n’est pas un CDD à abroger.',
 'L1226-4':'Inaptitude non professionnelle : fin immédiate à notification, préavis non exécuté non payé mais compté pour indemnité ; coordination nécessaire.',
 'L1226-14':'Inaptitude professionnelle : indemnité spéciale double et équivalent préavis, distincts de l’indemnité ordinaire.',
 'L1225-34':'Grossesse médicalement constatée : départ sans préavis ni indemnité due par la salariée ; aucune suppression silencieuse.',
 'L1225-66':'Élever l’enfant : information quinze jours avant, mais dispense de préavis ; ne pas confondre les deux notions.',
 'L5213-9':'Préavis doublé des salariés handicapés, plafonné à trois mois, donc quinze jours de droit commun ne produisent pas automatiquement quinze jours pour tous.',
 'L7112-2':'Journalistes : un ou deux mois, avec renvoi croisé au préavis général.',
 'L7112-3':'Journalistes : indemnité spéciale employeur d’un mois/an ou fraction, maximum quinze mensualités, sans franchise d’un an dans la source.',
 'L7112-5':'Clause de conscience/cession : indemnité possible à initiative journaliste et dispense particulière de préavis.',
 'L7313-9':'VRP : un, deux ou trois mois de préavis.',
 'L7313-13':'VRP : indemnité de clientèle ; créance spécifique à distinguer de la rupture ordinaire.',
 'L1241-1':'Le titre CDD exclut expressément apprentissage et contrat de mission : son abrogation seule ne crée pas le contrat universel.',
 'L1243-2':'Départ anticipé pour CDI : un jour/semaine, maximum deux semaines ; note applicable aux contrats en cours.',
 'L1243-4':'Rupture anticipée employeur : salaires jusqu’au terme plus précarité ; ne pas effacer les créances des CDD antérieurs.',
 'L1243-8':'Prime de précarité de 10 %, distincte de l’indemnité CDI ; transition indispensable.',
 'L1243-9':'Taux de précarité ramenable à 6 % par accord avec contreparties formation.',
 'L1243-11':'Ancienneté conservée et essai déduit lors du passage CDD/CDI ; préserver ces droits lors d’une conversion.',
 'L1251-58-1':'Le CDI intérimaire existe déjà ; il conserve missions commerciales et lettres de mission distinctes du lien d’emploi.',
 'L1251-58-4':'Le CDI intérimaire exclut déjà plusieurs règles de mission : essai, rupture anticipée, prime de fin de mission, carence.',
 'L1254-7':'Portage autorisé à durée déterminée ou indéterminée : supprimer la seule autorisation CDD générale ne suffit pas.',
 'L6222-7':'Apprentissage à durée limitée ou CDI ; sa phase de formation n’est pas un terme imposé au CDI.',
 'L6222-18':'Apprentissage : rupture libre pendant 45 jours de formation pratique puis motifs/procédure propres, médiateur et liquidation renvoyant au CDD.',
 'L6325-5':'Professionnalisation : CDD ou CDI écrit, renvoi direct à L1242-3.',
 'L6324-3':'Reconversion externe : CDI ou CDD d’au moins six mois et essai obligatoire ; notes d’entrée en vigueur de 2026 à préserver.',
 'L5132-5':'Insertion : CDD de quatre à vingt-quatre mois, prolongations, sortie sans préavis et renvoi L1243-2.',
 'L2253-1':'Primauté de branche pour durée/renouvellement/carence CDD, missions, chantier et renouvellement essai : supprimer les compétences devenues sans objet, sans supprimer minima et garanties étrangères à la réforme.',
 'L1111-2':'Passer les remplaçants CDD en CDI modifie le décompte d’effectifs si l’exclusion spécifique des remplaçants n’est pas coordonnée.',
 'L4154-2':'La sécurité renforcée vise CDD/intérim/stagiaires ; conversion en CDI ne doit pas rendre les nouveaux entrants dangereux invisibles au dispositif.',
 'L5422-1':'Privation involontaire, rupture conventionnelle et démission restent distinctes pour l’assurance chômage ; disparition CDD affecte aussi le double refus de CDI.',
 'L3141-28':'Indemnité compensatrice des congés acquis due quelle que soit initiative ; la franchise d’un an ne doit pas l’effacer.',
}

rows=[];mismatches=[]
for order,a in enumerate(export_rows):
    src=sources[a['source_id']]
    assert a['source_sha256']==src[3] and a['source_xml']==src[2],a['source_id']
    d=drafts.get(a['source_id']);enriched=a.copy();enriched['proposed_xml']=d[3] if d and d[3] else ''
    cats=category(enriched)
    if not cats:continue
    notes=source_notes(db,code,a['source_id'])
    if notes.strip()!=a['source_notes_xml'].strip():mismatches.append(a['source_id'])
    row={k:a[k] for k in ['code_id','source_id','number','path','source_url']}
    row.update(structure_order=order,source_sha256=src[3],source_xml=src[2],source_notes_xml=notes,valid_from=src[4],valid_until=src[5],categories=cats,source_and_notes_read_in_full=(a['number'] in read or bool(re.match(r'^[LRD]124',a['number']))),draft_status=d[2] if d else 'not_drafted',existing_proposed_xml=d[3] if d else None,existing_proposed_sha256=hashlib.sha256(d[3].encode()).hexdigest() if d and d[3] else None,existing_reason=d[4] if d else None,existing_review_notes=d[5] if d else None,source_references=refs(src[2]),draft_references=refs(d[3]) if d else [],links_to_core=sorted((set(refs(src[2]))|set(refs(d[3]) if d else []))&core),article_specific_conflict=facts.get(a['number']),review_state='source_notes_read_and_conflict_identified' if a['number'] in facts else ('source_notes_read_no_final_disposition' if a['number'] in read or re.match(r'^[LRD]124',a['number']) else 'structural_or_reference_candidate_not_yet_read_in_full'))
    rows.append(row)
counts=collections.Counter(c for r in rows for c in r['categories'])
data=dict(task='contrat_unique_inventory_read_only',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),canonical_code_id=code,export_source_sha256=hashlib.sha256(export.read_bytes()).hexdigest(),source_export_records=len(export_rows),canonical_source_verified_against_db=True,notes_mismatches=mismatches,database_open_mode='read_only_snapshot_transaction',active_policy_changed=False,existing_drafts_changed=False,inventory_does_not_mean_articles_rewritten=True,core_exact_numbers=sorted(core),category_counts=dict(counts),inventoried_records=len(rows),drafted_records=sum(r['existing_proposed_xml'] is not None for r in rows),read_in_full_records=sum(r['source_and_notes_read_in_full'] for r in rows),records=rows)
(HERE/'inventaire.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
core_rows=[r for r in rows if r['number'] in core]
assert len(core_rows)==45 and not any(re.match(r'^[LRD]124',r['number']) for r in core_rows)
for r in core_rows:
    r['benefit_check_required']=mentions_possible_relief(r['source_xml'])
    if r['existing_proposed_xml'] is not None:
        r['previous_draft']={'source_sha256':r['source_sha256'],'status':r['draft_status'],'proposed_xml':r['existing_proposed_xml'],'reason':r['existing_reason'],'review_notes':r['existing_review_notes'],'proposed_sha256':r['existing_proposed_sha256']}
(HERE/'source.json').write_text(json.dumps(core_rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:data[k] for k in ['inventoried_records','drafted_records','read_in_full_records','category_counts','notes_mismatches']},ensure_ascii=False,indent=2))
