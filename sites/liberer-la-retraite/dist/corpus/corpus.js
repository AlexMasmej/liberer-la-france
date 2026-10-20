
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
