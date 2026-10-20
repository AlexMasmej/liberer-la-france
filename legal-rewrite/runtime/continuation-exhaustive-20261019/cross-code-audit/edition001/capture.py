from pathlib import Path
import json,sqlite3,hashlib,re,xml.etree.ElementTree as E,sys,time
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
slugs=['securite-sociale','construction-habitation','urbanisme','impots']+['impots-annexe-'+str(i)for i in range(1,5)]
work='LEGITEXT000006072050'
patterns={
 'explicit_work_code':r'code\s+du\s+travail',
 'fixed_term':r'contrat.{0,70}(?:dur[ée]e\s+d[ée]termin[ée]e|[àa]\s+terme)|\bCDD\b',
 'indefinite':r'contrat.{0,70}dur[ée]e\s+ind[ée]termin[ée]e|\bCDI\b',
 'mission_temporary':r'int[ée]rim|contrat[s]?\s+de\s+mission|travail(?:leurs?)?\s+temporair|salari[ée]s?\s+temporair|portage\s+salarial',
 'training_season_replacement':r'apprentis|professionnalis|emploi.{0,30}saisonn|salari[ée].{0,30}saisonn|contrat.{0,30}remplacement',
 'employment_termination':r'pr[ée]avis|licenciement|rupture.{0,35}contrat|indemnit[ée].{0,50}(?:d[ée]part|retraite|rupture|licenciement|fin\s+de\s+contrat|fin\s+de\s+mission)',
 'other_indemnity':r'indemnit[ée]',
}
patterns={k:re.compile(v,re.I|re.S)for k,v in patterns.items()}
# Membership in the previously integrated contract-unique work is documentary;
# actual equality with the current DB remains separately checked.
prior={}
for f in (B/'runtime/contrat-unique-20261019').rglob('registration.json'):
 try:
  af=f.with_name('answer.json')
  if not af.exists():continue
  for x in json.loads(af.read_text()):prior[(x['code_id'],x['source_id'])]={'path':str(af.relative_to(B)),'proposed_sha256':sha(x['proposed_xml'])}
 except (KeyError,ValueError,TypeError):pass
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
rows=[];inventory=[];totals={};started=time.time()
for slug in slugs:
 pub=json.loads((B.parent/'sites/liberer-la-retraite/dist/corpus'/(slug+'.json')).read_text());totals[slug]={'source_records_examined':len(pub),'captured':0}
 for item in pub:
  key=item['code_id'],item['source_id'];a=dict(c.execute('select * from articles where code_id=? and id=?',key).fetchone());plain=a['plain_text'];tags=[k for k,v in patterns.items()if v.search(plain)]
  # Read every canonical ARTICLE's outbound link table too; not just text matches.
  raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;doc=E.fromstring(raw)
  outgoing=[dict(x.attrib)for x in doc.findall('.//LIEN')if x.get('cidtexte')==work and x.get('sens')=='source']
  if outgoing:tags.append('outgoing_work_reference')
  if not tags:continue
  assert sha(raw)==a['source_sha256'];a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(c,*key);a['source_document_xml']=raw;a['source_document_sha256']=sha(raw);a['source_body_sha256']=sha(a['source_xml']);a['source_notes_sha256']=sha(a['source_notes_xml']);d=c.execute('select * from drafts where code_id=? and source_id=?',key).fetchone();a['previous_draft']=dict(d)if d else None;a['current_beforeimage_sha256']=sha(d['proposed_xml'])if d and d['proposed_xml']else None;a['source_url']='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id'];a['slug']=slug;a['inventory_tags']=tags;a['outgoing_work_links']=outgoing;a['previous_contract_unique_registration']=prior.get(key);a['benefit_check_required']=True
  if key in prior:category='previously_contract_unique_coordinated'if a['current_beforeimage_sha256']==prior[key]['proposed_sha256']else'previously_coordinated_but_current_draft_differs'
  else:category='other_existing_draft'if d and d['proposed_xml']else'not_yet_drafted'
  excerpt=[]
  for k in tags:
   if k not in patterns:continue
   for m in list(patterns[k].finditer(plain))[:3]:excerpt.append({'tag':k,'text':plain[max(0,m.start()-100):m.end()+150]})
  inv={k:a[k]for k in ['code_id','source_id','number','slug','source_sha256','source_body_sha256','source_notes_sha256','current_beforeimage_sha256']};inv.update({'tags':tags,'draft_category':category,'previous_contract_unique_registration':prior.get(key),'outgoing_work_links':outgoing,'excerpts':excerpt});inventory.append(inv);rows.append(a);totals[slug]['captured']+=1
c.rollback();c.close()
for n,v in [('all-captured-sources.json',rows),('reference-inventory.json',inventory),('capture-summary.json',{'scope':slugs,'counts':totals,'examined_source_records':sum(x['source_records_examined']for x in totals.values()),'captured_candidates':len(rows),'all_current_article_outbound_links_examined':True,'citation_direction':'Only sens=source outward references; incoming sens=cible alone are not a legal reference in this article.','draft_categories':{k:sum(x['draft_category']==k for x in inventory)for k in set(x['draft_category']for x in inventory)},'duration_seconds':round(time.time()-started,2),'sources_edited':False,'db_mutated':False})]:
 (P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(json.loads((P/'capture-summary.json').read_text()),ensure_ascii=False,indent=2))
