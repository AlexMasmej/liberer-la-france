from pathlib import Path
import sys,json,sqlite3,copy,hashlib
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent;mode=sys.argv[1];code=P if mode=='legacy' else P/'runtime/cch-template-diagnostic-20261022T100424Z/integration/candidate';sys.path.insert(0,str(code))
import run_exhaustive as run,register_batches as reg
# Test-only path root for relative diagnostics; real validators unchanged.
reg.HERE=P
s=json.loads((P/'runtime/cch-template-diagnostic-20261022T100424Z/evidence/construction-habitation-00195/source.json').read_text())[0];row=json.loads((O/'batch-row.json').read_text());assert hashlib.sha256(row['proposed_xml'].encode()).hexdigest()=='5f3b0755692a643bb671d9e82529a66aa1599e3f0a8e8c51bfa1184e85768d41'
results=[]
for name,old,new in [('current',None,None),('invented_capital','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.','Le capital statutaire est fixé à 100 euros.'),('invented_notice','dont la durée en mois est fixée dans les statuts','dont la durée est de quinze jours')]:
 a=copy.deepcopy(row)
 if old:a['proposed_xml']=a['proposed_xml'].replace(old,new)
 # Do not carry old generated certificates into local lexical/gate experiment.
 for k in ('substantive_impact_certificate','reference_coherence'):a.pop(k,None)
 for gate in ('validate_answer','validate_batches'):
  try:
   if gate=='validate_answer':run.validate_answer([copy.deepcopy(a)],[s])
   else:
    d=sqlite3.connect(':memory:');d.executescript('CREATE TABLE articles(code_id,id,number,source_sha256,content_xml,valid_from,valid_until); CREATE TABLE documents(code_id,id,kind,xml); CREATE TABLE drafts(code_id,source_id,source_sha256,proposed_xml);');d.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)',(s['code_id'],s['source_id'],s['number'],s['source_sha256'],s['source_xml'],s['valid_from'],s['valid_until']));d.execute('INSERT INTO documents VALUES(?,?,?,?)',(s['code_id'],s['source_id'],'ARTICLE','<ARTICLE><NOTA><CONTENU></CONTENU></NOTA></ARTICLE>'));b=O/'test-batches'/mode/name/'isolated';b.mkdir(parents=True,exist_ok=True);(b/'00001.json').write_text(json.dumps([a],ensure_ascii=False));reg.validate_batches(d,b.parent);d.close()
   result={'accepted':True}
  except Exception as e:result={'accepted':False,'error':str(e)}
  results.append(dict(case=name,gate=gate,**result))
(O/(mode+'-gate-results.json')).write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
