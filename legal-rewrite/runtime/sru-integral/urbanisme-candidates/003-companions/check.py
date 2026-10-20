import json,re,html,hashlib,sys,collections
from pathlib import Path
P=Path(__file__).parent
sources=json.loads((P/'source.json').read_text());rows=json.loads((P/'answer.json').read_text())
sys.path.insert(0,'legal-rewrite')
from run_exhaustive import validate_answer
validate_answer(rows,sources)
def text(s):return html.unescape(re.sub('<[^>]*>',' ',s))
def labels(s):
 out=[]
 for p in re.findall(r'<p[^>]*>(.*?)</p>',s,re.S):
  t=text(p).strip();m=re.match(r'(?:([IVX]+)\.\s*[–-]|(\d+)(?:°)?\s*(bis|ter)?\s*[°.]?)',t)
  if m:out.append((m[1],m[2],m[3]))
 return out
def refs(s):return collections.Counter(re.sub(r'\s+','',m) for m in re.findall(r'[LRD]\.\s*\d+[\s-]*\d*(?:-\d+)*',text(s)))
checks=[]
for s,r in zip(sources,rows):
 ps=re.findall(r'<p>(.*?)</p>',r['proposed_xml'],re.S)
 main=''.join('<p>'+p+'</p>' for p in ps[:-1])
 source_refs=refs(s['source_xml']);prop_refs=refs(main)
 removed='L.121-29' if s['number']=='L341-16' else 'L.121-28'
 source_refs[removed]-=1
 assert +source_refs==+prop_refs,(s['number'],source_refs-prop_refs,prop_refs-source_refs)
 if s['number']=='R122-17':assert labels(s['source_xml'])==labels(main)
 checks.append({'article':s['number'],'raw_xml_sha_matches':hashlib.sha256((P/(s['source_id']+'.xml')).read_bytes()).hexdigest()==s['source_sha256'],'retained_reference_multiset_matches':True,'source_reference_removed_only':removed,'numbered_rubrics_preserved':True if s['number']=='R122-17' else 'not_applicable','source_note_present':bool(s['source_notes_xml'].strip()),'manual_normative_review':'Full sources/notes read. R122-17 all seven sections, 2026 changes, Natura2000 conditions, I1 exception/II14 continuation, III one-year limit, IV exceptions and deadline-reset/notice, V-VI revision/modification, VII scope compared; no other normative deletion intended.'})
out={'checks':checks,'validate_answer':'passed','all_sru_complete':False,'registered':False,'published':False,'answer_sha256':hashlib.sha256((P/'answer.json').read_bytes()).hexdigest()}
t=P/'checks.json.tmp';t.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');t.replace(P/'checks.json');print(json.dumps(out,ensure_ascii=False,indent=2))
