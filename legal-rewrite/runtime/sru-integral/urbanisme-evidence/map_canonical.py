from pathlib import Path
import sqlite3,json,hashlib,xml.etree.ElementTree as E,collections,re
ROOT=Path('legal-rewrite');OUT=ROOT/'runtime/sru-integral/urbanisme-evidence';ASOF='2026-10-19'
conn=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);conn.row_factory=sqlite3.Row
urban='LEGITEXT000006074075';codes={r[0] for r in conn.execute('select distinct code_id from articles')}
# Identity is version ID + code, never a reused article number.
docs={};meta={};by_num=collections.defaultdict(list)
for code in [urban,'LEGITEXT000006069577','LEGITEXT000006069568','LEGITEXT000006069569','LEGITEXT000006069574','LEGITEXT000006069576']:
 for row in conn.execute('select a.*,d.xml from articles a join documents d on d.code_id=a.code_id and d.id=a.id and d.kind=? where a.code_id=?',('ARTICLE',code)):
  a=dict(row);key=(code,a['id']);raw=a.pop('xml');a['xml_sha256']=hashlib.sha256(raw).hexdigest();a['url']='https://www.legifrance.gouv.fr/codes/article_lc/'+a['id'];docs[key]=E.fromstring(raw);meta[key]=a;by_num[(code,a['number'])].append(key)

law='JORFTEXT000000207538';types={'CREATION','CREE','MODIFICATION','MODIFIE','ABROGATION','ABROGE'};direct=collections.defaultdict(list)
for key,r in docs.items():
 for l in r.findall('./LIENS/LIEN'):
  if l.get('cidtexte')==law or l.get('numtexte')=='2000-1208':
   if l.get('typelien') not in types:continue
   num=l.get('num')
   if not num:
    m=re.search(r'art\.?\s*(\d+)',l.text or '',re.I);num=m[1] if m else None
   if num and num.isdigit():direct[int(num)].append((key,{'attributes':dict(l.attrib),'text':l.text}))

def component(key):
 r=docs[key];known={key}
 for l in r.findall('./VERSIONS/VERSION/LIEN_ART'):
  k=key[0],l.get('id');
  if k in docs:known.add(k)
 return known

def lineage(start):
 current={};paths={};seen=set();todo=[(start,[])];unresolved=[];edges=[]
 while todo:
  key,path=todo.pop()
  if key in seen:continue
  group=component(key);seen|=group
  for k in group:
   a=meta[k]
   if a['valid_from']<=ASOF<a['valid_until'] and a['state']!='ABROGE':
    current[k]=a;paths[k]=path
   for l in docs[k].findall('./LIENS/LIEN'):
    if l.get('typelien')=='CONCORDANCE' and l.get('sens')=='cible':
     nk=l.get('cidtexte'),l.get('id')
     edge={'from_code':k[0],'from_id':k[1],'from_number':a['number'],'to_code':nk[0],'to_id':nk[1],'to_number':l.get('num'),'attributes':dict(l.attrib),'text':l.text}
     if nk in docs:
      if nk not in seen:todo.append((nk,path+[edge]))
      edges.append(edge)
     elif (l.get('id') or '').startswith('LEGIARTI'):unresolved.append(edge)
 result=[]
 for k,a in sorted(current.items()):
  # Proof of state + actual later editorial event labels, not a claim all content remains from SRU.
  changes=[]
  for g in component(k):
   for l in docs[g].findall('./LIENS/LIEN'):
    if l.get('typelien') in types and l.get('datesignatexte','')>'2000-12-13':
     item={'version_id':g[1],'relation':l.get('typelien'),'attributes':dict(l.attrib),'text':l.text}
     if item not in changes:changes.append(item)
  result.append({'code_id':k[0],'source_id':k[1],'number':a['number'],'state':a['state'],'valid_from':a['valid_from'],'valid_until':a['valid_until'],'source_sha256':a['source_sha256'],'source_url':a['url'],'concordance_path':paths[k],'later_normative_events':changes,'semantic_retention_verified':False})
 return result,sorted(seen),unresolved

initial=json.loads((ROOT/'runtime/sru-integral/original-articles.json').read_text());scope=set(range(1,55))|{73,90,92,93}|set(range(94,140))|set(range(202,210));records=[];used=set()
for original in initial:
 n=int(original['number'])
 if n not in scope:continue
 entries=[];families=set()
 for key,proof in direct[n]:
  family=tuple(sorted(component(key)))
  if family in families:continue
  families.add(family);descendants,seen,unresolved=lineage(key);used.update(seen)
  a=meta[key]
  entries.append({'original_code_id':key[0],'version_id':key[1],'original_target_number':a['number'],'source_state':a['state'],'source_valid_from':a['valid_from'],'source_valid_until':a['valid_until'],'source_url':a['url'],'direct_sru_relation':proof,'version_family':sorted({k[1] for k in component(key)}),'current_descendants':descendants,'unresolved_concordance_targets':unresolved})
 records.append({'original_article':str(n),'original_source_url':original['source_url'],'first_page_line':original['first_page_line'],'last_page_line':original['last_page_line'],'initial_text_sha256':hashlib.sha256(original['text'].encode()).hexdigest(),'contains_constitutional_censure':'non conformes à la Constitution' in original['text'],'initial_text':original['text'],'canonical_targets':entries,'external_or_uncaptured_targets_require_lookup':not bool(entries),'complete_normative_mapping':False})
report={'purpose':'Cartographie documentaire de filiation, aucun candidat de réécriture et aucune abrogation effectuée.','as_of':ASOF,'source_database':'corpus.sqlite, lecture seule','law_original':'JORFTEXT000000207538','law_consolidated':'LEGITEXT000005630252','number_reuse_guard':'VERSIONS/LIEN_ART + identifiants ; jamais le seul numéro.','warning':'Un descendant documentaire ne prouve pas que tout son texte actuel est issu de SRU. Les champs semantic_retention_verified restent faux jusqu’à comparaison de fond. Les dispositions actuelles d’autres lois ne doivent pas être abrogées en bloc.','original_articles':len(records),'direct_target_families':sum(len(r['canonical_targets']) for r in records),'records':records}
def write(name,data):
 p=OUT/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');t.replace(p)
write('canonical-lineage.json',report)
# Companion exact XML of the cited current/historical versions for subsequent human comparison.
write('canonical-sources.json',[{**meta[k],'document_xml':E.tostring(docs[k],encoding='unicode')} for k in sorted(used)])
print(json.dumps({k:v for k,v in report.items() if k!='records'},ensure_ascii=False,indent=2))
print('Canonical versions captured',len(used))
for r in records:
 entries=r['canonical_targets'];curr=sorted({a['number'] for e in entries for a in e['current_descendants']})
 print(r['original_article'],'direct',','.join(sorted({e['original_target_number'] for e in entries})),'=>',','.join(curr))
