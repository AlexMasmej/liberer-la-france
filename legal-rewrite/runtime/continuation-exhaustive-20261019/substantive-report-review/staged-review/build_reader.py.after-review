"""Build a source-first legal reading interface; drafts are never fabricated."""
from pathlib import Path
import json,sys,html,shutil
from ingest import open_db,export_snapshot,HERE,atomic_json
from source_assets import safe_html,load_companions,asset_path,graphic_markers,recovery_complete

OUT=HERE.parent/'sites/liberer-la-retraite/dist/corpus'
OUT.mkdir(parents=True,exist_ok=True)
db=open_db(HERE/'corpus.sqlite')
db.execute('BEGIN')
STAGING=HERE/'runtime/export-source'
coverage=export_snapshot(db,sys.argv[1] if len(sys.argv)>1 else '2026-10-18',STAGING)
db.rollback();db.close()

companions=load_companions()
graphic_records=[]
for companion in companions.values():
    for field in ['media','documents']:
        for item in companion.get(field,[]):
            destination=OUT/item['path'];destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(asset_path(item['path']),destination)
for code in coverage['codes']:
    p=OUT/(code['slug']+'.json');records=json.loads((STAGING/p.name).read_text())
    for record in records:
        # The canonical XML already retains the complete source. Avoid sending
        # its duplicate plain-text representation for every long code article.
        record.pop('source_text',None)
        for key in ['source_xml','source_notes_xml','proposed_xml']:
            if record[key] is not None:
                record[key]=safe_html(record[key])
        companion=companions.get((record['code_id'],record['source_id']))
        if companion:record['source_companions']=companion
        if graphic_markers(record['source_xml']):graphic_records.append({'code_id':record['code_id'],'source_id':record['source_id'],'number':record['number'],'markers':len(graphic_markers(record['source_xml'])),'documentary_recovery_complete':recovery_complete(record['source_xml'],companion),'authenticated_jo_crosscheck_complete':bool(companion and companion.get('authenticated_jo_crosscheck_complete'))})
    atomic_json(p,records,compact=True)
    structure=code['slug']+'-structure.json';atomic_json(OUT/structure,json.loads((STAGING/structure).read_text()))
coverage['graphic_source_coverage']={'affected_articles':len(graphic_records),'documented_articles':sum(r['documentary_recovery_complete'] for r in graphic_records),'unresolved_articles':sum(not r['documentary_recovery_complete'] for r in graphic_records),'articles':graphic_records}
coverage['normative_source_recovery_complete']=not coverage['graphic_source_coverage']['unresolved_articles']
coverage['exhaustive_rewriting_complete']=False
atomic_json(OUT/'coverage.json',coverage)
progress={'source_snapshot':coverage['as_of'],'scope':'5 complete codes plus 4 CGI annexes','official_archives_imported':467,'official_source_records':sum(c['imported_versions'] for c in coverage['codes']),'drafted_articles':sum(c['drafted'] for c in coverage['codes']),'retained_unchanged':sum(c['retained_unchanged'] for c in coverage['codes']),'jurist_reviewed_articles':sum(c['reviewed'] for c in coverage['codes']),'exhaustive_rewriting_complete':False,'graphic_source_coverage':coverage['graphic_source_coverage'],'reader_url':'https://libererlaretraite.com/corpus/','live_job_status':'runtime/exhaustive/status.json','next_work':'Continue full article drafting and cross-reference coordination; recover unresolved documentary formulas. Imported or unchanged text is not counted as rewritten.'}
atomic_json(HERE/'progress.json',progress)
from build_substantive_report import build as build_impact_report
build_impact_report(OUT,STAGING,HERE/'corpus.sqlite',HERE/'batches')
(OUT/'index.html').write_text('''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Réécriture des textes officiels avec l’IA — Chantier intégral</title><meta name="description" content="Cinq codes français : lire la source officielle, la proposition et l’avancement article par article."><link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="reader.css"><script src="corpus.js" defer></script></head><body><a class="skip" href="#main">Aller au contenu</a><header><a class="brand" href="/">Retraite, version IA</a><a href="#source">Sources & méthode</a></header><main id="main"><section class="corpus-hero"><p class="eyebrow">CHANTIER DE RÉÉCRITURE INTÉGRALE</p><h1>Le droit français.<br><em>Article par article.</em></h1><p class="lead">Le texte officiel, la proposition de réécriture et chaque changement, côte à côte.</p><p>Travail réalisé par les agents IA d’<a href="https://x.com/alexmasmej">@alexmasmej</a>.</p><p class="notice" id="stage" role="status">Chargement de l’état du corpus…</p><div id="coverage" class="coverage"></div></section><section class="reading-controls"><label for="code">Choisir un code</label><select id="code"></select><label for="query">Chercher un article ou une expression</label><input id="query" type="search" placeholder="Ex. L1221-2, cotisations, permis…"><label for="status">Afficher</label><select id="status"><option value="all">Tous les articles</option><option value="rewritten">Réécritures rédigées</option><option value="pending">À traiter</option></select><p id="count" aria-live="polite"></p><div class="pager"><button id="previous" type="button">← Précédents</button><span id="page"></span><button id="next" type="button">Suivants →</button></div></section><section id="articles" aria-label="Articles du code"></section><section id="source"><p class="eyebrow">SOURCES & MÉTHODE</p><h2>Les textes officiels.<br><em>Des changements vérifiables.</em></h2><p>Les textes sources proviennent du fonds officiel LEGI de la DILA. Chaque article conserve son numéro, son identifiant, sa période de validité et un lien vers Légifrance. Les parties législatives et réglementaires sont conservées dans leur ordre d’origine.</p><p>Le corpus est reconstitué à partir d’un fonds complet et des mises à jour officielles datées. Tant que cette chaîne et le sommaire ne sont pas réconciliés, l’inventaire est indiqué comme partiel. Les articles officiels affichés seuls ne sont pas comptés comme réécrits.</p><p>La proposition est un texte de travail indépendant. Le nombre de propositions mesure la couverture du corpus ; il ne mesure pas les baisses de prélèvements ou de complexité. Chaque changement réel doit être documenté avec son état avant/après, ses renvois et les charges éventuellement nouvelles. <a href="/bilan-allegements.html">Consulter le bilan des changements</a>. Les premières synthèses en 18 ou 40 articles servent d’orientations ; elles ne remplacent pas les codes officiels.</p><p><a href="https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides">Source officielle DILA / LEGI ↗</a> · <a href="coverage.json">État détaillé du corpus</a></p></section></main><footer>Réécriture avec l’IA · Aucun changement du droit en vigueur par cette publication.</footer></body></html>''')
(OUT/'reader.css').write_text('''
.corpus-hero{padding-top:65px}h1{font-size:clamp(44px,6vw,90px)}.corpus-hero .lead{margin:28px 0}.notice{background:#e0e6d6;padding:20px;max-width:960px}.coverage{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-top:30px}.coverage>div{border-top:1px solid;padding:15px 0}.coverage b{display:block}.coverage span{font-size:14px}.reading-controls{padding-top:36px;padding-bottom:25px;display:grid;grid-template-columns:1fr 2fr 1fr;gap:12px;align-items:end}.reading-controls label{font-size:12px;grid-row:1}.reading-controls input,.reading-controls select{min-width:0;width:100%;padding:13px;border:1px solid #8eaa98;background:#fffaf1;color:#173a32;font:inherit;grid-row:2}.reading-controls #count{grid-column:1/-1;font-size:14px}.pager{grid-column:1/-1;display:flex;align-items:center;gap:20px}.pager button{padding:10px 16px;background:#17453b;color:white;border:0;cursor:pointer}.pager button:disabled{opacity:.4;cursor:default}#articles{padding-top:20px}.legal-article{padding:32px 0;border-top:1px solid #173a3240}.legal-article h2{font-size:30px;margin:15px 0}.legal-article .path{font-size:12px;max-width:100ch}.legal-columns{display:grid;grid-template-columns:1fr 1fr;gap:24px}.legal-columns>div{min-width:0;padding:20px;background:#fffaf1}.legal-columns h3{font:13px Arial,sans-serif;text-transform:uppercase;letter-spacing:.08em;margin-bottom:20px}.legal-text{font-size:16px;line-height:1.75;overflow-wrap:anywhere}.legal-text p,.legal-text li{font:inherit;font-family:Plain,Arial,sans-serif;line-height:1.75;letter-spacing:normal}.legal-text table{display:block;max-width:100%;overflow:auto;font-size:14px}.legal-text td{padding:8px}.pending{color:#52645c;font-style:italic}.source-meta{font-size:12px}.change-reason{padding:15px 0;font-size:14px}#articles>p{font-size:18px}@media(max-width:750px){.coverage{grid-template-columns:1fr}.reading-controls{display:flex;flex-direction:column;align-items:stretch}.legal-columns{grid-template-columns:1fr}.legal-columns>div{padding:15px}.pager{gap:10px;justify-content:space-between}}
''')
(OUT/'corpus.js').write_text('''
'use strict';
const $=s=>document.querySelector(s), pageSize=20;
let metadata=null,articles=[],page=0,requestToken=0;
const labels={source_imported:'À réécrire',rewrite_draft:'Réécriture proposée',reviewed:'Réécriture relue',retained_unchanged:'Conservé sans modification',repeal_proposed:'Abrogation proposée',source_changed_review_required:'Source modifiée : relecture nécessaire'};
function element(tag,cls,text){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;}
function render(){
 const q=$('#query').value.trim().toLocaleLowerCase('fr'),status=$('#status').value;
 const exactNumber=articles.some(a=>a.number.toLocaleLowerCase('fr')===q);
 const filtered=articles.filter(a=>(!q||(exactNumber?a.number.toLocaleLowerCase('fr')===q:(a.number+' '+a.source_xml.replace(/<[^>]*>/g,' ')+' '+(a.reason||'')).toLocaleLowerCase('fr').includes(q)))&&(status==='all'||(status==='rewritten'?Boolean(a.proposed_xml):!a.proposed_xml&&a.status!=='retained_unchanged')));
 const pages=Math.max(1,Math.ceil(filtered.length/pageSize));page=Math.min(page,pages-1);
 $('#count').textContent=filtered.length+' article(s) dans l’inventaire importé de ce code.';
 $('#page').textContent=(page+1)+' / '+pages;$('#previous').disabled=page===0;$('#next').disabled=page>=pages-1;
 const target=$('#articles');target.replaceChildren();
 if(!filtered.length){target.append(element('p',null,'Aucun article correspondant dans le corpus importé pour le moment.'));return;}
 for(const a of filtered.slice(page*pageSize,(page+1)*pageSize)){
  const item=element('article','legal-article');item.id=a.source_id;
  item.append(element('p','path',a.path.join(' / ')),element('h2',null,'Article '+a.number));
  const meta=element('p','source-meta',(labels[a.status]||a.status)+' · État LEGI : '+(a.source_state||'non renseigné')+' · Version source : '+a.valid_from+' → '+(a.valid_until==='2999-01-01'?'sans date de fin connue':a.valid_until)+' · ');
  const link=element('a',null,'Légifrance ↗');link.href=a.source_url;link.target='_blank';link.rel='noopener noreferrer';meta.append(link);const permanent=element('a',null,'Lien vers cet article');permanent.href='?code='+encodeURIComponent($('#code').value)+'&article='+encodeURIComponent(a.number);meta.append(document.createTextNode(' · '),permanent);item.append(meta);
  if(a.source_conflict_ids&&a.source_conflict_ids.length>1)item.append(element('p','notice','Plusieurs versions de cet article occupent la même place dans les données officielles importées. Elles sont conservées et signalées pour vérification ; aucune n’est choisie silencieusement comme seule version applicable.'));
  const cols=element('div','legal-columns'),original=element('div'),proposed=element('div');
  original.append(element('h3',null,'Texte officiel'));const src=element('div','legal-text');src.innerHTML=a.source_xml;original.append(src);
  if(a.source_companions){const c=a.source_companions,box=element('details','source-companions');box.append(element('summary',null,'Formules et documents sources complémentaires'));box.append(element('p',null,c.provenance_notes||''));for(const d of c.documents||[]){const p=element('p'),link=element('a',null,d.label||'Document source');link.href=d.path;link.target='_blank';link.rel='noopener';p.append(link);box.append(p);}for(const t of c.transcriptions||[])box.append(element('p',null,(t.label||'Complément '+t.marker)+(t.page!=null?' — page '+t.page:(t.article?' — article '+t.article:''))+' : '+t.text));for(const m of c.media||[]){const image=element('img');image.src=m.path;image.alt='Complément documentaire '+m.marker+(m.page!=null?' — page '+m.page:'');image.loading='lazy';box.append(image);}original.append(box);}
  if(a.source_notes_xml){const notes=element('div','legal-text');notes.append(element('h3',null,'Notes officielles d’application'));const noteBody=element('div');noteBody.innerHTML=a.source_notes_xml;notes.append(noteBody);original.append(notes);}
  proposed.append(element('h3',null,'Proposition de réécriture'));
  if(a.proposed_xml){const draft=element('div','legal-text');draft.innerHTML=a.proposed_xml;proposed.append(draft);}
  else proposed.append(element('p','pending',a.status==='retained_unchanged'?'Article conservé dans la version proposée ; aucune réécriture n’est revendiquée.':'La réécriture de cet article n’a pas encore été rédigée.'));
  cols.append(original,proposed);item.append(cols);
  if(a.reason)item.append(element('p','change-reason','Changement proposé : '+a.reason));
  if(a.review_notes)item.append(element('p','change-reason','Points à vérifier : '+a.review_notes));
  target.append(item);
 }
}
async function loadCode(){
 const token=++requestToken;$('#articles').replaceChildren(element('p',null,'Chargement du texte officiel…'));
 try{const response=await fetch($('#code').value+'.json');if(!response.ok)throw Error('Source indisponible');const data=await response.json();if(token!==requestToken)return;articles=data;page=0;render();}
 catch(error){if(token===requestToken)$('#articles').replaceChildren(element('p',null,'Le texte n’a pas pu être chargé. Réessayez en choisissant le code.'));}
}
$('#code').addEventListener('change',loadCode);$('#query').addEventListener('input',()=>{page=0;render();});$('#status').addEventListener('change',()=>{page=0;render();});
$('#previous').addEventListener('click',()=>{page--;render();});$('#next').addEventListener('click',()=>{page++;render();});
(async()=>{try{const r=await fetch('coverage.json');if(!r.ok)throw Error();metadata=await r.json();
 const complete=metadata.sources_complete&&metadata.codes.every(c=>c.inventory_reconciled);
 $('#stage').textContent=(complete?'Inventaire source reconstitué':'Import officiel en cours : inventaire partiel')+' · Date de référence visée : '+metadata.as_of+'. Les compteurs ci-dessous distinguent l’import de la réécriture.';
 for(const code of metadata.codes){const tile=element('div');tile.append(element('b',null,code.title),element('span',null,code.imported_versions+' articles sources affichables · '+code.drafted+' propositions (couverture, pas allègements) · '+code.retained_unchanged+' textes maintenus · '+code.reviewed+' relues'));$('#coverage').append(tile);const option=element('option',null,code.title);option.value=code.slug;$('#code').append(option);}
 const requested=new URLSearchParams(location.search);const desired=requested.get('code');if(requested.get('article'))$('#query').value=requested.get('article');if(metadata.codes.some(c=>c.slug===desired))$('#code').value=desired;
 await loadCode();
 }catch(error){$('#stage').textContent='L’état du corpus n’a pas pu être chargé. Aucun inventaire complet n’est revendiqué.';}})();
''')
print(json.dumps({'output':str(OUT),'source_complete':coverage['sources_complete'],'codes':[{k:c[k] for k in ['title','imported_versions','drafted','inventory_reconciled']} for c in coverage['codes']]},ensure_ascii=False))

with (OUT/'reader.css').open('a') as stylesheet:
    stylesheet.write('\n.legal-text img,.source-companions img{display:block;max-width:100%;height:auto;margin:16px 0}.source-companions{font:14px/1.6 Arial,sans-serif;overflow-wrap:anywhere;margin:20px 0}.source-companions summary{cursor:pointer;font-weight:700}.source-companions p{font:14px/1.6 Arial,sans-serif;letter-spacing:normal}\n')
