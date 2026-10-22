"""Whole legislative companion articles, outside the five-code inventory."""
from pathlib import Path
import hashlib
import html
import json
import re
from urllib.parse import urlsplit

from register_batches import text as legal_text
from source_assets import safe_html
from initiative_notice import annotate

HERE = Path(__file__).resolve().parent


def check_supporting_source(article):
    for key in ['title', 'source_url', 'source_date', 'source_xml', 'source_sha256']:
        if not isinstance(article.get(key), str) or not article[key].strip():
            raise ValueError('Incomplete supporting source: '+key)
    url = urlsplit(article['source_url'])
    if url.scheme != 'https' or not (url.hostname or '').endswith('.gouv.fr'):
        raise ValueError('Expected an official French supporting source URL')
    if hashlib.sha256(article['source_xml'].encode()).hexdigest() != article['source_sha256']:
        raise ValueError('Supporting source fingerprint mismatch')
    if article.get('status') != 'source_reference_only' or article.get('proposed_xml') is not None:
        raise ValueError('Supporting sources cannot count as new proposals')
    original, _ = legal_text(article['source_xml'], strict=False)
    if not original.strip():
        raise ValueError('Empty supporting source')


def load(root=None):
    result = []
    for path in sorted((root or HERE/'coordinations').glob('*/manifest.json')):
        slug = path.parent.name
        if not re.fullmatch(r'[a-z][a-z0-9-]*', slug):
            raise ValueError('Invalid coordination directory')
        item = json.loads(path.read_text())
        if item.get('outside_code_inventory') is not True or not item.get('articles'):
            raise ValueError('Coordination must be explicitly outside the code inventory')
        for article in item['articles']:
            for key in ['number', 'title', 'source_url', 'source_date', 'source_xml',
                        'source_sha256', 'proposed_xml', 'reason', 'review_notes']:
                if not isinstance(article.get(key), str) or not article[key].strip():
                    raise ValueError('Incomplete coordination article: '+key)
            url = urlsplit(article['source_url'])
            if url.scheme != 'https' or not (url.hostname or '').endswith('.gouv.fr'):
                raise ValueError('Expected an official French source URL')
            if hashlib.sha256(article['source_xml'].encode()).hexdigest() != article['source_sha256']:
                raise ValueError('Coordination source fingerprint mismatch')
            original, _ = legal_text(article['source_xml'], strict=False)
            proposal, _ = legal_text(article['proposed_xml'])
            if not original.strip() or not proposal.strip() or original == proposal:
                raise ValueError('Coordination needs a whole source and a distinct proposal')
            if article.get('source_notes_xml'):
                notes = re.sub(r'<br\s+clear=([\"\'])none\1\s*/?>', '<br>', article['source_notes_xml'], flags=re.I)
                legal_text(notes)
        for reference in item.get('supporting_sources', []):
            check_supporting_source(reference)
        result.append(item | {'slug': slug})
    return result


def unique_records(records):
    by_name = {}
    for record in records:
        name = record['filename']
        if name in by_name and by_name[name] != record:
            raise ValueError('Conflicting coordination records: '+name)
        by_name[name] = record
    return list(by_name.values())


def document(item):
    e = html.escape
    parts = ['<!doctype html><html lang="fr"><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<title>'+e(item['title'])+'</title>',
             '<style>body{max-width:900px;margin:40px auto;padding:0 24px;color:#193b32;',
             'font:17px/1.6 Georgia,serif}h1,h2{line-height:1.2}aside{background:#edf1e8;',
             'padding:16px}article{border-top:1px solid;padding-top:24px;margin-top:30px}',
             'a{color:inherit}table{border-collapse:collapse}td,th{border:1px solid;padding:8px}',
             '.proposal{border-left:4px solid #376c50;padding-left:18px}</style>',
             '<h1>'+e(item['title'])+'</h1>',
             '<aside>Coordination législative hors des cinq codes et de leurs annexes. ',
             'Les articles ci-dessous sont joints en entier, avec leur source et leur proposition. ',
             'Ils ne sont pas ajoutés au compteur de réécriture des codes. ',
             'Propositions indépendantes rédigées par les agents IA d’@alexmasmej ; ',
             'elles ne modifient pas le droit en vigueur.</aside>']
    if item.get('scope_note'):
        parts += ['<p>'+e(item['scope_note'])+'</p>']
    for a in item['articles']:
        parts += ['<article><h2>'+e(a['title'])+'</h2><p>Source : <a href="',
                  e(a['source_url'], quote=True)+'">'+e(a['source_date'])+'</a></p>',
                  '<h3>Texte source intégral</h3>']
        if a.get('valid_from'):
            parts += ['<p>Version source : '+e(a['valid_from'])+' → '+e(a.get('valid_until', ''))+
                      ' · État LEGI : '+e(a.get('source_state', 'non renseigné'))+'</p>']
        parts += [safe_html(a['source_xml'])]
        if a.get('source_notes_xml'):
            parts += ['<details><summary>Notes du texte source</summary>'+safe_html(a['source_notes_xml'])+'</details>']
        parts += [
                  '<h3>Article proposé intégral</h3><div class="proposal">',
                  a['proposed_xml']+'</div><aside><strong>Changement proposé</strong><p>',
                  e(a['reason'])+'</p><strong>Points à vérifier</strong><p>',
                  e(a['review_notes'])+'</p></aside></article>']
    if item.get('supporting_sources'):
        parts += ['<h2>Sources complémentaires</h2><p>Ces textes sont fournis pour vérifier ',
                  'les coordinations. Ils ne portent aucune proposition nouvelle et ne sont ',
                  'pas ajoutés au nombre d’articles réécrits.</p>']
        for reference in item['supporting_sources']:
            parts += ['<details><summary>'+e(reference['title'])+'</summary><p>Source : <a href="',
                      e(reference['source_url'], quote=True)+'">'+e(reference['source_date'])+'</a></p>']
            if reference.get('valid_from'):
                parts += ['<p>Version source : '+e(reference['valid_from'])+' → '+
                          e(reference.get('valid_until', ''))+' · État LEGI : '+
                          e(reference.get('source_state', 'non renseigné'))+'</p>']
            parts += [safe_html(reference['source_xml'])]
            if reference.get('source_notes_xml'):
                parts += ['<h3>Notes du texte source</h3>', safe_html(reference['source_notes_xml'])]
            parts += ['</details>']
    return annotate(''.join(parts)+'</html>')


def add_to_archive(archive, output, group, items):
    records = []
    for item in items:
        if group not in item.get('groups', ['impots']):
            continue
        name = 'coordination-'+item['slug']+'.html'
        payload = document(item).encode()
        (output/name).write_bytes(payload)
        prefix = 'coordinations/'+item['slug']+'/'
        archive.writestr(prefix+'source-et-proposition-integrales.html', payload)
        archive.writestr(prefix+'articles.json', json.dumps(item, ensure_ascii=False, indent=2))
        records.append({'title': item['title'], 'filename': name,
                        'sha256': hashlib.sha256(payload).hexdigest(),
                        'bytes': len(payload), 'articles': len(item['articles']),
                        'archive_html': prefix+'source-et-proposition-integrales.html',
                        'archive_json': prefix+'articles.json',
                        'outside_code_inventory': True})
    return records
