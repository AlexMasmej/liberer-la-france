import sqlite3,json,hashlib,re,html,collections,sys
from pathlib import Path
P=Path(__file__).parent
sys.path.insert(0,'legal-rewrite')
from run_exhaustive import validate_answer
s=json.loads((P/'source.json').read_text());rows=json.loads((P/'answer.json').read_text());validate_answer(rows,s)
c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
def text(x):return html.unescape(re.sub('<[^>]*>',' ',x))
def refs(x):return collections.Counter(re.sub(r'\s+','',x) for x in re.findall(r'[LRD]\.\s*(?:\*\s*)?\d+(?:\s*-\s*\d+)+',text(x)))
checks=[]
for src,r in zip(s,rows):
 old=c.execute('select * from drafts where code_id=? and source_id=?',(src['code_id'],src['source_id'])).fetchone();sha=hashlib.sha256((old['proposed_xml']or'').encode()).hexdigest()if old else None
 assert sha==src['current_beforeimage_sha256'],('Draft changed since snapshot',src['number'])
 raw=c.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",(src['code_id'],src['source_id'])).fetchone()[0]
 assert hashlib.sha256(raw).hexdigest()==src['source_sha256']
 assert refs(src['source_xml'])==refs(r['proposed_xml']),(src['number'],refs(src['source_xml'])-refs(r['proposed_xml']),refs(r['proposed_xml'])-refs(src['source_xml']))
 assert not re.search(r'suppression|supprimé|cessent|cesse|abrogation|nouvelle dérogation',r['proposed_xml'],re.I)
 assert not any(x in r for x in ['repeal_policy_id','repeal_scope','removed_provisions','change_type'])
 checks.append({'article':src['number'],'source_sha256':src['source_sha256'],'current_beforeimage_sha256':sha,'proposed_sha256':hashlib.sha256(r['proposed_xml'].encode()).hexdigest(),'guard_still_matches_db':True,'all_numbered_source_article_references_preserved':True,'obsolete_repeal_clauses_absent':True,'repeal_metadata_absent':True})
proposals={r['number']:r['proposed_xml']for r in rows}
assert '5 janvier 1986' in proposals['L121-28'] and '5 janvier 1986' in proposals['R121-7']
assert 'bande des cent mètres mentionnée à l’article L. 121-16' in proposals['R121-7'].replace("'",'’')
for name in ['Guadeloupe','Guyane','Martinique','La Réunion','Mayotte']:assert name in proposals['R121-36']
assert '3° Les schémas' in proposals['L104-2']
assert '5° Les schémas' in proposals['R151-52']
target_ids={a['source_id']for a in s};extra=[]
pattern=re.compile(r'sch.ma.{0,50}(?:plage|L\.\s*121-28)|(?:L\.\s*121-(?:28|29|30)|R\.\s*121-(?:7|8|36))(?!\d)',re.I)
for a in c.execute('select * from drafts'):
 if a['source_id']in target_ids:continue
 body=a['proposed_xml']or''
 if pattern.search(body):extra.append({'code_id':a['code_id'],'source_id':a['source_id'],'proposed_xml':body,'reason':a['reason'],'scope_warning':'Mention only; may be a numbering homonym outside urbanisme. Must not infer repeal from a bare number.'})
policy=Path('legal-rewrite/policy-coordinations.json');lines=policy.read_text().splitlines();policy_hits=[{'line':i+1,'text':line}for i,line in enumerate(lines)if 'SRU42' in line and re.search('supprimer|cess|dérogation',line,re.I)]
out={'validate_answer':'passed','articles':checks,'other_database_draft_mentions':extra,'policy_mentions_for_root':policy_hits,'external_companions_root_action_required':['L341-16: retain source reference L121-29, disable deleted-companion proposal','R122-17: retain source I50° L121-28, disable deleted-companion proposal'],'checks_do_not_claim_live_db_already_restored':True,'registered':False,'published':False,'answer_sha256':hashlib.sha256((P/'answer.json').read_bytes()).hexdigest()}
t=P/'checks.json.tmp';t.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');t.replace(P/'checks.json');print(json.dumps({'eight_guards_stable':True,'source_references_match':True,'other_draft_mentions':len(extra),'policy_mentions':len(policy_hits),'answer_sha256':out['answer_sha256']},ensure_ascii=False))
