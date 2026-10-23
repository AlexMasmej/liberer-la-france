"""Five short idea pages, followed by complete-code downloads."""
from pathlib import Path
import argparse
import html
import json
import re
from initiative_notice import apply_to_sites

HERE = Path(__file__).resolve().parent
SITES = HERE.parent/'sites'
CENTRAL = 'https://www.libererlaretraite.com'
SUPPORT_URL = 'https://soutenir.unenouvelleenergie.fr/adhesion'
E = html.escape
CSS = '''@font-face{font-family:Editorial;src:url(fonts/serif.woff)}@font-face{font-family:Editorial;src:url(fonts/italic.woff);font-style:italic}@font-face{font-family:Plain;src:url(fonts/sans.woff)}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:#f4f0e7;color:#193b32;font:16px/1.6 Plain,Arial,sans-serif}a{color:inherit;text-underline-offset:4px}a:hover{color:#805c2d}a:focus-visible,button:focus-visible{outline:3px solid #a65c3c;outline-offset:4px}.skip{position:absolute;top:-80px;left:20px;z-index:100;background:#fff;padding:10px}.skip:focus{top:10px}header,main,footer{max-width:1080px;margin:auto;padding-inline:40px}header{display:flex;justify-content:space-between;align-items:center;gap:24px;padding-block:24px;border-bottom:1px solid #193b3238}.brand{font-size:12px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none}header nav{display:flex;gap:24px;font-size:13px}header nav a{text-decoration:none}section{padding:48px 0;border-bottom:1px solid #193b3238}.hero{padding-top:48px}.eyebrow{font-size:11px;letter-spacing:.13em;text-transform:uppercase;margin:0 0 18px}h1,h2,h3{font-family:Editorial,Georgia,serif;font-weight:400;line-height:1.08;margin:0}h1{font-size:clamp(54px,7vw,86px);letter-spacing:-.045em}h1 em,h2 em{font-weight:400;color:#49715e}h2{font-size:clamp(30px,4vw,45px);letter-spacing:-.025em}h3{font-size:26px;line-height:1.17}.lead{font-family:Editorial,Georgia,serif;font-size:25px;line-height:1.35;max-width:800px;margin:22px 0}.byline{font-size:12px;color:#50655b;margin:18px 0 0}.actions{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin-top:25px}.button{display:inline-block;padding:13px 20px;background:#193b32;color:#fff8ed;text-decoration:none;font-size:14px}.button:hover{color:#fff;background:#35624e}.text-link{font-size:13px}.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:34px;padding-top:22px;border-top:1px solid #193b3238}.metrics strong{display:block;font-family:Editorial,Georgia,serif;font-weight:400;font-size:32px;line-height:1.15}.metrics span{font-size:12px;display:block;margin-top:6px;max-width:220px}.ideas{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:30px 46px;margin-top:28px}.ideas article{border-top:1px solid #193b3238;padding-top:18px}.ideas .number{font-size:11px;display:block;margin-bottom:10px;color:#5b7065}.ideas p{margin:12px 0 0;font-size:15px;line-height:1.7}.funding{display:grid;grid-template-columns:1fr 1.4fr;gap:40px}.funding p{margin:0;font-size:15px;line-height:1.75}.downloads{background:#e8ecdf;padding:30px;margin-top:26px}.downloads>p{max-width:800px;font-size:14px}.download-list{margin-top:22px}.download-item{display:flex;align-items:center;justify-content:space-between;gap:25px;padding:20px 0;border-top:1px solid #193b3238}.download-item h3{font-size:23px}.download-item p{font-size:12px;margin:7px 0 0}.download-item .button{white-space:nowrap}.small{font-size:12px;color:#50655b;line-height:1.6}.download-note{margin-top:20px!important}.download-note strong{color:#193b32}.further{display:flex;flex-wrap:wrap;gap:12px 25px;font-size:13px;margin-top:25px}footer{padding-block:24px 32px;font-size:12px;color:#50655b}footer p{max-width:840px;margin:8px 0}.term{font:inherit;color:inherit;border:0;border-bottom:1px dotted;background:transparent;padding:0;cursor:help;text-align:left}#definition{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);width:min(90vw,560px);background:#193b32;color:#f7f4ea;padding:20px 24px;z-index:100;box-shadow:0 10px 35px #0003;border:1px solid #c6d8bc}[hidden]{display:none!important}@media(max-width:650px){header,main,footer{padding-inline:22px}header{gap:12px;align-items:flex-start}header nav{gap:15px;font-size:12px}.brand{max-width:130px}section{padding-block:34px}.hero{padding-top:34px}.lead{font-size:23px}.metrics{gap:12px}.metrics strong{font-size:26px}.metrics span{font-size:11px}.ideas,.funding{grid-template-columns:1fr;gap:26px}.ideas h3{font-size:25px}.download-item{align-items:flex-start;flex-direction:column;gap:12px}.downloads{padding:22px}.download-item .button{width:100%;text-align:center}.actions{gap:15px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{body{font-size:10pt;color:#000;background:#fff}header,nav.reform-network,.actions,.further,footer,#definition{display:none!important}main{max-width:none;padding:0}section{padding:18px 0}h1{font-size:33pt}h2{font-size:21pt}h3{font-size:15pt}.lead{font-size:14pt}.metrics{margin-top:12px;padding-top:10px}.metrics strong{font-size:19pt}.ideas{gap:18px 28px;margin-top:16px}.ideas p,.funding p{font-size:10pt;line-height:1.5}.ideas article{break-inside:avoid}.downloads{padding:14px;margin-top:12px}.download-item{padding:12px 0}.download-item .button{background:none;color:#000;padding:0}.downloads p{font-size:9pt}.downloads .button:after{content:' : ' attr(href);font-size:8pt;overflow-wrap:anywhere}.byline{font-size:9pt}}'''
GLOSSARY = {
    'capitalisation': 'Les versements sont investis pour financer une retraite future. Leur valeur dépend des placements.',
    'répartition': 'Les cotisations courantes financent les pensions versées aujourd’hui.',
    'abondements': 'Versements complémentaires financés par un employeur ou la solidarité.',
    'CSG': 'Contribution sociale généralisée, un prélèvement qui finance la protection sociale.',
    'PASS': 'Plafond annuel de la sécurité sociale, utilisé ici pour limiter le montant de l’allègement proposé.',
    'C3S': 'Contribution sociale de solidarité des sociétés, assise sur le chiffre d’affaires dans son champ d’application.',
    'péréquation': 'Redistribution de ressources entre collectivités pour réduire les écarts de moyens.',
}


CSS += '''
.site-header{display:grid;grid-template-columns:minmax(0,1fr) auto auto;gap:24px}
.site-header .brand{min-width:0;max-width:none;overflow-wrap:anywhere}
.site-header nav{align-items:center}
.site-header .header-support{grid-column:3;grid-row:1;justify-self:end;white-space:nowrap;text-align:center;font-size:13px;line-height:1.4}
@media(max-width:650px){.site-header{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px 12px;align-items:center}.site-header nav{grid-column:1/-1;grid-row:2;justify-self:start}.site-header .header-support{grid-column:2;white-space:normal;font-size:12px;padding:11px 13px;max-width:100%;min-height:44px}}
'''


def support_link(class_name='text-link'):
    return f'<a class="{E(class_name, quote=True)}" href="{SUPPORT_URL}" target="_blank" rel="noopener noreferrer">Soutenir Nouvelle Énergie ↗</a>'


def support_cta():
    return '<div class="actions">'+support_link('button')+'<span>Le mouvement de David Lisnard.</span></div>'


def site_header(title, navigation):
    return '<header class="site-header"><a class="brand" href="/">'+E(title)+'</a><nav aria-label="Navigation principale">'+navigation+'</nav>'+support_link('button header-support')+'</header>'


def enrich(text):
    pattern = re.compile(r'\b('+'|'.join(map(re.escape, GLOSSARY))+r')\b', re.I)
    def term(match):
        key = next(k for k in GLOSSARY if k.casefold() == match[0].casefold())
        return f'<button type="button" class="term" data-definition="{E(GLOSSARY[key], quote=True)}" aria-expanded="false">{E(match[0])}</button>'
    return pattern.sub(term, E(text))


def filesize(size):
    return f'{size/1_000_000:.1f}'.replace('.', ',')+' Mo'


def download_cards(slugs, manifest, local=False):
    cards = []
    for slug in slugs:
        item = next(x for x in manifest['downloads'] if x['slug'] == slug)
        href = ('/downloads/' if local else CENTRAL+'/downloads/')+item['filename']
        annexes = ' · annexes I à IV incluses' if slug == 'impots' else ''
        count = item['drafted_articles']
        drafted_label = '1 article proposé' if count == 1 else f'{count} articles proposés'
        related = ''.join('<p>Coordination hors code jointe : <a href="'+('/downloads/' if local else CENTRAL+'/downloads/')+E(ref['filename'],quote=True)+'">'+E(ref['title'])+'</a>.</p>' for ref in item.get('outside_code_inventory_coordinations',[]))
        cards.append(f'<div class="download-item"><div><h3>{E(item["title"])}</h3><p>Texte intégral{annexes} · ZIP · {filesize(item["bytes"])} · {drafted_label}</p>{related}</div><a class="button" href="{href}" download>Télécharger le code ↓</a></div>')
    return ''.join(cards)


def network(items, active):
    names = ['Emploi', 'Revenu', 'Entreprise', 'Logement', 'Retraite']
    return '<nav class="reform-network" aria-label="Les cinq réformes">'+''.join(f'<a href="https://{x["domain"]}/"'+(' aria-current="page"' if x['slug']==active else '')+'>'+name+'</a>' for x,name in zip(items,names))+'</nav>'


def build_fiscal_method(out, items):
    """Keep the detailed evaluation framework off the two-page summary."""
    data = json.loads((HERE/'fiscal-net-method.json').read_text())
    references = {ref['id']: ref for ref in data['references']}
    sections = []
    for section in data['sections']:
        body = ''.join(f'<p>{E(text)}</p>' for text in section['paragraphs'])
        if section.get('formula'):
            body += f'<p class="equation">{E(section["formula"])}</p>'
        if section.get('table'):
            table = section['table']
            heads = ''.join(f'<th scope="col">{E(text)}</th>' for text in table['headers'])
            rows = ''.join('<tr><th scope="row">'+E(row[0])+'</th><td>'+E(row[1])+'</td></tr>' for row in table['rows'])
            body += f'<div class="table-wrap" role="region" aria-label="Canaux du chiffrage" tabindex="0"><table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table></div>'
        if section.get('sources'):
            links = ' · '.join(f'<a href="{E(references[key]["url"], quote=True)}">{E(references[key]["label"])}</a>' for key in section['sources'])
            body += f'<p class="small">Sources : {links}.</p>'
        sections.append(f'<section><h2>{E(section["title"])}</h2>{body}</section>')
    style = '.method{max-width:980px}.method h1{max-width:850px}.method h2{max-width:780px}.method section>p{max-width:820px}.method .eyebrow{margin-top:0}.method .equation{padding:20px;background:#e8ecdf;font-weight:600}.table-wrap{overflow-x:auto;margin-top:24px}table{width:100%;border-collapse:collapse;font-size:14px;text-align:left}th,td{padding:16px 12px;vertical-align:top;border-bottom:1px solid #193b3238}thead th{background:#e8ecdf}tbody th{width:23%;min-width:130px;font-weight:600}.method .small{font-size:12px;overflow-wrap:anywhere}@media(max-width:650px){th,td{padding:12px 8px}table{font-size:13px}.method h1{font-size:48px}}@media print{.method h1{font-size:30pt}.method h2{font-size:20pt}table{font-size:9pt}tr{break-inside:avoid}}'
    (out/'chiffrage-is-net.html').write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(data['title'])} — Libérer l’entreprise</title><meta name="description" content="{E(data['description'],quote=True)}"><link rel="canonical" href="https://www.libererlentreprise.com/chiffrage-is-net.html"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="summary.css"><link rel="stylesheet" href="network.css"><style>{style}</style></head><body>{network(items,'entreprise')}<a class="skip" href="#main">Aller au contenu</a>{site_header('Libérer l’entreprise · Version IA', '<a href="/#financement">Retour aux mesures</a>')}<main class="method" id="main"><section class="hero"><p class="eyebrow">Méthode de chiffrage · {E(data['date'])}</p><h1>{E(data['title'])}</h1><p class="lead">{E(data['lead'])}</p><p class="small">{E(data['status'])}</p></section>{''.join(sections)}<section><a class="button" href="/#telecharger">Lire les propositions dans les codes ↓</a></section></main><footer>{support_cta()}<p>Cadre d’évaluation proposé par les agents IA d’<a href="https://x.com/alexmasmej">@alexmasmej</a>. Les sources citées étayent les mécanismes et la méthode ; elles ne constituent pas un chiffrage de la réforme française.</p><p><a href="/">Retour à Libérer l’entreprise</a></p></footer></body></html>''')


def main(only=None):
    items = json.loads((HERE/'site-summaries.json').read_text())
    manifest = json.loads((SITES/'liberer-la-retraite/dist/downloads/manifest.json').read_text())
    (SITES/'liberer-la-retraite/dist/progress-widget.html').write_text((HERE/'progress-widget.html').read_text())
    # Reuse the same glossary interaction on short pages and the retained long version.
    original_js = (SITES/'liberer-la-retraite/dist/reader.js').read_text()
    glossary_js = original_js[original_js.index('const tip='):original_js.index('function progress')]
    for item in items:
        if only and item['slug'] != only:
            continue
        out = SITES/item['directory']/'dist'
        archive = out/'avant-projet.html'
        if not archive.exists():
            archive.write_bytes((out/'index.html').read_bytes())
        metrics = ''.join(f'<div><strong>{E(v)}</strong><span>{E(label)}</span></div>' for v,label in item['metrics'])
        ideas = ''.join(f'<article><span class="number">0{n}</span><h3>{E(title)}</h3><p>{enrich(body)}</p></article>' for n,(title,body) in enumerate(item['ideas'],1))
        if item.get('references'):
            ideas += '<p class="small">Sources du modèle : '+ ' · '.join(f'<a href="{E(ref["url"], quote=True)}">{E(ref["label"])}</a>' for ref in item['references'])+'</p>'
        local = item['slug'] == 'retraite'
        hub = '/telechargements/' if local else CENTRAL+'/telechargements/'
        reader = ('/corpus/' if local else CENTRAL+'/corpus/')+'?code='+item['reader']
        all_href = ('/downloads/' if local else CENTRAL+'/downloads/')+manifest['all']['filename']
        description = E(item['lead'], quote=True)
        finance_detail = ('<p style="margin-top:16px"><a href="chiffrage-is-net.html">Voir la méthode : recettes, aides, dette et scénarios ↗</a></p>' if item['slug'] == 'entreprise' else '')
        (out/'index.html').write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(item['title'])} — Les idées, les codes complets</title><meta name="description" content="{description}"><meta name="theme-color" content="#193b32"><link rel="canonical" href="https://{item['domain']}/"><link rel="icon" href="favicon.svg" type="image/svg+xml"><meta property="og:title" content="{E(item['title'])}"><meta property="og:description" content="{description}"><meta property="og:image" content="https://{item['domain']}/og.png"><meta property="og:url" content="https://{item['domain']}/"><link rel="stylesheet" href="summary.css"><link rel="stylesheet" href="network.css"><script src="summary.js" defer></script><style>body{{padding-bottom:200px}}.rewrite-fab{{position:fixed;z-index:1000;right:12px;bottom:max(12px,env(safe-area-inset-bottom));width:290px;max-width:calc(100vw - 24px);height:190px;border:0}}@media print{{.rewrite-fab{{display:none}}}}</style></head><body>{network(items,item['slug'])}<a class="skip" href="#main">Aller au contenu</a>{site_header(item['title']+' · Version IA', '<a href="#mesures">Les idées</a><a href="#telecharger">Les codes ↓</a>')}<main id="main"><section class="hero"><p class="eyebrow">{item['number']} / Cinq réformes · L’essentiel en deux pages</p><h1>Libérer<br><em>{E(item['noun'])}.</em></h1><p class="lead">{E(item['lead'])}</p><div class="actions"><a class="button" href="#telecharger">Télécharger les codes complets ↓</a><a class="text-link" href="#mesures">Comprendre les mesures</a></div><p class="byline">Conçu et rédigé par les agents IA d’<a href="https://x.com/alexmasmej">@alexmasmej</a>.</p><div class="metrics" aria-label="Chiffres et objectifs proposés">{metrics}</div></section><section id="mesures"><p class="eyebrow">Les mesures proposées</p><h2>Ce qu’on change.<br><em>Concrètement.</em></h2><div class="ideas">{ideas}</div></section><section id="financement" class="funding"><div><p class="eyebrow">La contrepartie</p><h2>{E(item['finance_title'])}</h2></div><div><p>{enrich(item['finance'])}</p>{finance_detail}</div></section><section id="telecharger"><p class="eyebrow">Aller au texte</p><h2>Les idées ici.<br><em>Les codes à emporter.</em></h2><div class="downloads"><p>Les codes dans leur longueur, avec leurs parties législatives et réglementaires. Chaque ZIP contient le texte source, une version de travail complète et les données article par article. Les documents HTML se lisent hors ligne dans un navigateur.</p><div class="download-list">{download_cards(item['codes'],manifest,local)}</div><p class="small download-note"><strong>Réécriture intégrale en cours.</strong> Sur les cinq codes et les annexes du CGI : {manifest['drafted_articles']} propositions d’articles rédigées. Ce nombre mesure la couverture, pas le nombre d’allègements. <a href="https://www.libererlaretraite.com/bilan-allegements.html">Bilan des changements réels</a>. Les articles encore à traiter restent en texte source, marqués « À réécrire ». Les fichiers ne sont donc pas des codes intégralement réécrits. {manifest.get("graphic_source_coverage",{}).get("unresolved_articles",0)} articles comportent encore des éléments graphiques ou modèles à retrouver.</p></div><div class="further"><a href="{all_href}" download>Les cinq codes + annexes en un ZIP ({filesize(manifest['all']['bytes'])}) ↓</a><a href="{hub}">Tous les téléchargements</a><a href="{reader}">Comparer article par article ↗</a></div></section></main><footer>{support_cta()}<p>Propositions indépendantes. Sources : fonds officiel LEGI / DILA, corpus au 18 octobre 2026. Aucun changement du droit en vigueur par cette publication.</p><p><a href="avant-projet.html">Avant-projet initial, détails et sources</a> · <a href="https://www.legifrance.gouv.fr/">Vérifier sur Légifrance ↗</a></p></footer><div id="definition" role="tooltip" hidden></div><iframe class="rewrite-fab" src="https://www.libererlaretraite.com/progress-widget.html" title="Pourcentage du corpus traité — cinq codes"></iframe></body></html>''')
        if item['slug'] == 'entreprise':
            build_fiscal_method(out, items)
        (out/'summary.css').write_text(CSS)
        (out/'summary.js').write_text("'use strict';\n"+glossary_js+"\nif(/^#article-/.test(location.hash))location.replace('avant-projet.html'+location.hash);\n")
        print(f'Built concise landing: {item["domain"]}')
    if not only or only == 'retraite':
        out = SITES/'liberer-la-retraite/dist/telechargements'
        out.mkdir(exist_ok=True)
        (out/'index.html').write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Télécharger les cinq codes complets</title><link rel="stylesheet" href="../summary.css"><link rel="stylesheet" href="../network.css"></head><body>{network(items,'retraite')}{site_header('Les cinq réformes · Version IA', '<a href="/">Les idées</a>')}<main><section><p class="eyebrow">Les textes à emporter</p><h1>Les codes.<br><em>En entier.</em></h1><p class="lead">Cinq codes, les quatre annexes du CGI et les premières propositions de réécriture. Des fichiers consultables hors ligne.</p><div class="actions"><a class="button" href="/downloads/{manifest['all']['filename']}" download>Tout télécharger · ZIP · {filesize(manifest['all']['bytes'])} ↓</a><a href="/corpus/">Comparer en ligne ↗</a></div><div class="downloads"><p><strong>État de la réécriture : {manifest['drafted_articles']} propositions d’articles sur {manifest['source_records']:,} entrées sources.</strong> Ce nombre mesure la couverture, pas les simplifications. <a href="/bilan-allegements.html">Voir le bilan des changements réels</a>. La réécriture exhaustive n’est pas terminée. Chaque archive contient un texte source intégral et une version de travail complète où les articles encore à traiter restent marqués « À réécrire ».</p><p>Ouvrez les fichiers HTML dans votre navigateur pour lire, rechercher ou imprimer. Les données JSON et la structure sont également incluses. Les textes sources, notes et éventuelles versions concurrentes sont conservés.</p>{download_cards([x['slug'] for x in manifest['downloads']],manifest,True)}</div><p class="small">Source : fonds LEGI / DILA, corpus au 18 octobre 2026. Propositions non relues par un juriste. <a href="/downloads/manifest.json">Inventaire et empreintes des fichiers</a>.</p></section></main><footer>{support_cta()}Conçu et rédigé par les agents IA d’<a href="https://x.com/alexmasmej">@alexmasmej</a>. Les propositions ne modifient pas le droit en vigueur.</footer></body></html>''')


    # Download documents already carry this notice before their hashes and ZIPs
    # are generated. The idempotent pass also covers archives and reader pages.
    apply_to_sites(SITES/item['directory']/'dist' for item in items
                   if not only or item['slug']==only)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', choices=['embauche','revenu','entreprise','logement','retraite'])
    main(parser.parse_args().site)
