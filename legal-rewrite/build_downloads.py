"""Export complete imported codes and clearly labelled, partial working rewrites."""
from pathlib import Path
import hashlib
import html
import io
import json
import zipfile
from source_assets import asset_path,load_companions
from coordination_downloads import load as load_coordinations, add_to_archive, unique_records
from initiative_notice import annotate

HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parent / 'sites/liberer-la-retraite/dist'
CORPUS = PUBLIC / 'corpus'
OUT = PUBLIC / 'downloads'
GROUPS = {
    'travail': ['travail'],
    'impots': ['impots', *[f'impots-annexe-{n}' for n in range(1, 5)]],
    'securite-sociale': ['securite-sociale'],
    'urbanisme': ['urbanisme'],
    'construction-habitation': ['construction-habitation'],
}
STYLE = '''body{font:17px/1.65 Georgia,serif;color:#193b32;max-width:900px;margin:50px auto;padding:0 24px}h1{line-height:1.1;font-size:42px}h2{font-size:24px}article{border-top:1px solid #b9c9bd;margin-top:35px;padding-top:20px}.meta,.state,aside{font:13px/1.6 Arial,sans-serif}.state{padding:12px;background:#edf1e8}.draft{border-left:4px solid #376c50;padding-left:16px}table{border-collapse:collapse;max-width:100%;display:block;overflow:auto}td,th{border:1px solid #bbb;padding:8px}a{color:inherit}aside{padding:18px;background:#edf1e8}nav{margin:30px 0}nav a{display:block}@media print{body{max-width:none;margin:0}article{break-inside:auto}h2{break-after:avoid}.meta{overflow-wrap:anywhere}}'''
STYLE += 'img{display:block;max-width:100%;height:auto;margin:20px 0}'
E = html.escape


def companion_html(companion):
    if not companion:return ''
    parts=['<details><summary>Compléments documentaires aux éléments absents du XML source</summary><p>'+E(companion.get('provenance_notes',''))+'</p>']
    for item in companion.get('documents',[]):
        parts.append('<p><a href="'+E(item['path'],quote=True)+'">'+E(item.get('label','Document source'))+'</a></p>')
    for item in companion.get('transcriptions',[]):
        location=(' — page '+str(item['page']) if item.get('page') is not None else (' — article '+str(item['article']) if item.get('article') else ''))
        parts.append('<p>'+E(item.get('label','Complément '+str(item['marker'])))+E(location)+' : '+E(item['text'])+'</p>')
    for item in companion.get('media',[]):
        location=' — page '+str(item['page']) if item.get('page') is not None else ''
        parts.append('<img src="'+E(item['path'],quote=True)+'" alt="Complément documentaire '+str(item['marker'])+E(location,quote=True)+'">')
    return ''.join(parts)+'</details>'


def document(code, records, working, date):
    drafted = sum(bool(a['proposed_xml']) for a in records)
    retained = sum(a['status']=='retained_unchanged' for a in records)
    label = 'Version de travail intégrale — réécriture partielle' if working else 'Texte source intégral importé'
    parts = [f'<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(code["title"])} — {label}</title><style>{STYLE}</style><body>',
             f'<h1>{E(code["title"])}</h1><p>{label} · Corpus au {date}</p>',
             f'<aside>{len(records):,} entrées sources, parties législatives et réglementaires importées. Les identifiants et éventuelles versions concurrentes sont conservés. Source : fonds officiel LEGI / DILA. Cette édition indépendante ne remplace pas Légifrance.</aside>']
    if working:
        parts.append(f'<p><strong>{drafted} propositions de réécriture ; {len(records)-drafted-retained} entrées encore à traiter ; {retained} textes maintenus après examen.</strong> Les articles restant à traiter sont reproduits dans leur version source et marqués « À réécrire ». Les textes maintenus ne sont pas comptés comme réécrits ni comme allègements. Le nombre de propositions mesure la couverture, pas les simplifications. Aucune relecture par un juriste n’est revendiquée.</p>')
    parts.append('<nav aria-label="Grandes parties">')
    seen = set()
    for a in records:
        path = a['path'][0] if a['path'] else 'Articles'
        if path not in seen:
            seen.add(path)
            parts.append(f'<a href="#{E(a["source_id"])}">{E(path)}</a>')
    parts.append('</nav>')
    for a in records:
        proposed = working and bool(a['proposed_xml'])
        parts.extend([f'<article id="{E(a["source_id"])}"><p class="meta">{E(" / ".join(a["path"]))}</p><h2>Article {E(a["number"])}</h2>',
                      f'<p class="meta">Source : <a href="{E(a["source_url"], quote=True)}">{E(a["source_id"])}</a> · Version : {E(a["valid_from"])} → {E(a["valid_until"])} · État LEGI : {E(a["source_state"] or "non renseigné")}</p>'])
        if working:
            parts.append('<p class="state">Proposition IA — non relue par un juriste</p>' if proposed else ('<p class="state">Texte maintenu après examen — aucune réduction de charge revendiquée</p>' if a['status']=='retained_unchanged' else '<p class="state">À réécrire — texte source conservé, sans validation du fond</p>'))
        if a.get('source_conflict_ids'):
            parts.append('<p class="state">Versions concurrentes signalées : '+E(', '.join(a['source_conflict_ids']))+'. Aucune sélection silencieuse.</p>')
        parts.append('<div'+(' class="draft"' if proposed else '')+'>'+(a['proposed_xml'] if proposed else a['source_xml'])+'</div>')
        parts.append(companion_html(a.get('source_companions')))
        if a.get('source_notes_xml'):
            parts.append('<details><summary>Notes du texte source</summary>'+a['source_notes_xml']+'</details>')
        if proposed or a['status']=='retained_unchanged':
            parts.append('<aside><strong>Changement proposé</strong><p>'+E(a.get('reason') or '')+'</p><strong>Points à vérifier</strong><p>'+E(a.get('review_notes') or '')+'</p></aside>')
        parts.append('</article>')
    parts.append('</body></html>')
    return annotate(''.join(parts))


def build():
    OUT.mkdir(exist_ok=True)
    coverage = json.loads((CORPUS/'coverage.json').read_text())
    codes = {c['slug']: c for c in coverage['codes']}
    downloads = []
    companions=load_companions()
    coordinations=load_coordinations()
    published_coordinations=[]
    for group, slugs in GROUPS.items():
        name = f'{group}-complet.zip'
        code_ids={codes[slug]['code_id'] for slug in slugs}
        graphic_records=[r for r in coverage.get('graphic_source_coverage',{}).get('articles',[]) if r['code_id'] in code_ids]
        manifest = {'as_of': coverage['as_of'], 'exhaustive_rewriting_complete': False, 'jurist_reviewed_articles': 0, 'graphic_source_coverage':graphic_records,'normative_source_recovery_complete':all(r['documentary_recovery_complete'] for r in graphic_records),'codes': []}
        with zipfile.ZipFile(OUT/name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            included=set()
            for slug in slugs:
                code = codes[slug]
                records = json.loads((CORPUS/f'{slug}.json').read_text())
                assert len(records) == code['imported_versions']
                for working, filename in [(False, 'texte-source-integral.html'), (True, 'version-de-travail-integrale.html')]:
                    z.writestr(f'{slug}/{filename}', document(code, records, working, coverage['as_of']))
                z.writestr(f'{slug}/articles.json', json.dumps(records, ensure_ascii=False, separators=(',', ':')))
                z.writestr(f'{slug}/structure.json', (CORPUS/f'{slug}-structure.json').read_bytes())
                for article in records:
                    companion=companions.get((article['code_id'],article['source_id']))
                    if not companion:continue
                    if article.get('source_companions')!=companion:raise ValueError('Rebuild reader before downloads: companion metadata changed')
                    for field in ['media','documents']:
                        for item in companion.get(field,[]):
                            entry=f'{slug}/'+item['path']
                            if entry not in included:z.write(asset_path(item['path']),entry);included.add(entry)
                manifest['codes'].append({'slug': slug, 'title': code['title'], 'source_records': len(records), 'drafted_articles': sum(bool(a['proposed_xml']) for a in records),'retained_unchanged':sum(a['status']=='retained_unchanged' for a in records),'pending':sum(not a['proposed_xml'] and a['status']!='retained_unchanged' for a in records)})
            related=add_to_archive(z,OUT,group,coordinations)
            manifest['outside_code_inventory_coordinations']=related
            published_coordinations.extend(related)
            z.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
            z.writestr('LISEZ-MOI.txt', f'''CODES COMPLETS — ÉDITION DE TRAVAIL AU {coverage['as_of']}

Ouvrez les fichiers HTML dans un navigateur, sans connexion ni installation.
Ils sont consultables, recherchables et imprimables. Chaque dossier contient :
- texte-source-integral.html : toutes les entrées sources importées ;
- version-de-travail-integrale.html : les propositions disponibles remplacent
  les articles correspondants ; les autres textes restent marqués À réécrire ;
- articles.json : source, proposition, provenance et points de vérification ;
- structure.json : sommaire officiel importé.
- les PDF et images documentaires disponibles : formules et tableaux non
  reproduits dans l'export texte, avec provenance dans articles.json.
- coordinations/ si présent : articles complets de textes hors des cinq codes,
  source et proposition réunies, sans ajout au compteur de réécriture des codes.

La réécriture exhaustive n'est PAS terminée. Aucun code de cette archive
n'est présenté comme entièrement réécrit. Les entrées source non réécrites
ne sont pas des articles approuvés ou revus par un juriste. Certaines entrées
sont des annexes ou des versions concurrentes, signalées dans les documents.
Certains éléments graphiques et anciens modèles ne sont pas reproduits dans
le fonds texte : leur récupération reste indiquée dans manifest.json.
Les compléments documentaires disponibles sont joints avec leur provenance ;
une consolidation ministérielle n'est pas un Journal officiel authentifié.
Source : fonds officiel LEGI / DILA. Les données proviennent du stock du
13 juillet 2025 et des mises à jour jusqu'au 18 octobre 2026.
Les propositions sont indépendantes, rédigées avec l'IA pour @alexmasmej.
Elles ne modifient pas le droit en vigueur. Vérification officielle : Légifrance.
''')
        payload = (OUT/name).read_bytes()
        downloads.append({'slug': group, 'title': codes[group]['title'], 'filename': name, 'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest(), 'source_records': sum(c['source_records'] for c in manifest['codes']), 'drafted_articles': sum(c['drafted_articles'] for c in manifest['codes']), 'retained_unchanged':sum(c['retained_unchanged'] for c in manifest['codes']), 'outside_code_inventory_coordinations':related})
    impact_path=CORPUS/'substantive-impact.json'
    impact_payload=impact_path.read_bytes() if impact_path.exists() else None
    impact_file={'filename':'bilan-allegements.json','sha256':hashlib.sha256(impact_payload).hexdigest(),'bytes':len(impact_payload)} if impact_payload is not None else None
    with zipfile.ZipFile(OUT/'cinq-codes-complets.zip', 'w', compression=zipfile.ZIP_STORED) as z:
        for item in downloads:
            z.write(OUT/item['filename'], item['filename'])
        if impact_payload is not None:z.writestr('bilan-allegements.json',impact_payload,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('manifest.json', json.dumps({'as_of': coverage['as_of'], 'exhaustive_rewriting_complete': False, 'downloads': downloads,'substantive_impact_report':impact_file}, ensure_ascii=False, indent=2))
    result = {'as_of': coverage['as_of'], 'source_records': sum(x['source_records'] for x in downloads), 'drafted_articles': sum(x['drafted_articles'] for x in downloads), 'retained_unchanged':sum(x['retained_unchanged'] for x in downloads), 'exhaustive_rewriting_complete': False,'graphic_source_coverage':coverage.get('graphic_source_coverage',{}), 'downloads': downloads, 'all': {'filename': 'cinq-codes-complets.zip', 'bytes': (OUT/'cinq-codes-complets.zip').stat().st_size}}
    result['outside_code_inventory_coordinations']=unique_records(published_coordinations)
    result['substantive_impact_report']=impact_file
    (OUT/'manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f'Exported {result["source_records"]} source records, {result["drafted_articles"]} drafts, five complete-code packages including CGI annexes.')
    return result


if __name__ == '__main__':
    build()
