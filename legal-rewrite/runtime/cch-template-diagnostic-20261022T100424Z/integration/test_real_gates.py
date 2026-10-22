import copy, hashlib, json, sqlite3, sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
MODE=sys.argv[1];CODE=ROOT/MODE
sys.path.insert(0,str(CODE))
import run_exhaustive as run
import register_batches as register
import reference_coherence as refs
EVIDENCE=ROOT.parent/'evidence'
results=[]
def db_for(sources):
    db=sqlite3.connect(':memory:')
    db.executescript('CREATE TABLE articles(code_id,id,number,source_sha256,content_xml,valid_from,valid_until); CREATE TABLE documents(code_id,id,kind,xml); CREATE TABLE drafts(code_id,source_id,source_sha256,proposed_xml);')
    for s in sources:
        db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)',(s['code_id'],s['source_id'],s['number'],s['source_sha256'],s['source_xml'],s['valid_from'],s['valid_until']))
        db.execute('INSERT INTO documents VALUES(?,?,?,?)',(s['code_id'],s['source_id'],'ARTICLE','<ARTICLE><NOTA><CONTENU>'+s.get('source_notes_xml','')+'</CONTENU></NOTA></ARTICLE>'))
    return db

def gate(name,kind,rows,sources,expect):
    rows=copy.deepcopy(rows)
    try:
        if kind=='validate_answer':run.validate_answer(rows,copy.deepcopy(sources))
        else:
            folder=CODE/'test-batches'/'isolated';folder.mkdir(parents=True,exist_ok=True)
            (folder/'00001.json').write_text(json.dumps(rows,ensure_ascii=False))
            db=db_for(sources)
            try:register.validate_batches(db,folder.parent)
            finally:db.close()
        accepted=True;error=None
    except Exception as exc:accepted=False;error=type(exc).__name__+': '+str(exc)
    results.append({'name':name,'gate':kind,'accepted':accepted,'expected':expect,'error':error})

pairs=[]
for d in sorted(EVIDENCE.iterdir()):
    sources=json.loads((d/'source.json').read_text());rows=json.loads((d/'answer.json').read_text());pairs.extend(zip(sources,rows))
    for kind in ['validate_answer','validate_batches']:
        gate(d.name,kind,rows,sources,MODE=='candidate')
    try:
        refs.accept_checks(copy.deepcopy(rows),sources,json.loads((d/'reference-targets.json').read_text()))
        results.append({'name':d.name,'gate':'accept_checks','accepted':True,'expected':True})
    except Exception as exc:results.append({'name':d.name,'gate':'accept_checks','accepted':False,'expected':True,'error':str(exc)})
if MODE=='candidate':
 for s,a in pairs:
    for kind in ['validate_answer','validate_batches']:
        gate(s['source_id']+' individual',kind,[a],[s],True)
        for marker in ['[…]','[...]','[ … ]','[à compléter]','[texte inchangé]','TODO','&lt;placeholder&gt;','[&#8230;]']:
            b=copy.deepcopy(a);b['proposed_xml']+='<p>'+marker+'</p>';gate(s['source_id']+' new '+marker,kind,[b],[s],False)
        for name,mutate in [('bad source hash',lambda b:b.update(source_sha256='bad')),('bad HTML',lambda b:b.update(proposed_xml=b['proposed_xml']+'<script>x</script>')),('bad impact',lambda b:b.update(substantive_impact={'version':999}))]:
            b=copy.deepcopy(a);mutate(b);gate(s['source_id']+' '+name,kind,[b],[s],False)
        if s.get('benefit_check_required') and kind=='validate_answer':
            b=copy.deepcopy(a);b.pop('benefit_review',None);gate(s['source_id']+' missing benefit',kind,[b],[s],False)
        if s['source_id'].endswith(('952','995')):
            for name,old,new in [('invented capital','[…]','100'),('removed fields','[…]',''),('invented name','est :, société','est : Exemple, société'),('invented seat','fixé à :.','fixé à Paris.'),('missing capital heading','5. Capital social',''),('changed capital clause','euros','francs')]:
                b=copy.deepcopy(a);b['proposed_xml']=b['proposed_xml'].replace(old,new,1);gate(s['source_id']+' '+name,kind,[b],[s],False)
            if s['source_id'].endswith('995'):
                b=copy.deepcopy(a);b['proposed_xml']=b['proposed_xml'].replace('préavis de mois','préavis de quinze jours');gate(s['source_id']+' invented notice',kind,[b],[s],False)
            for label,source_change in [('source bytes changed',{'source_xml':s['source_xml']+' '}),('source notes changed',{'source_notes_xml':'Changed notes'})]:
                changed=dict(s,**source_change)
                gate(s['source_id']+' '+label,kind,[a],[changed],False)
            for label,old,new in [('omitted governance','8A. Conseil', 'Conseil'),('extra duplicate field','[…]','[…] […]')]:
                b=copy.deepcopy(a);b['proposed_xml']=b['proposed_xml'].replace(old,new,1);gate(s['source_id']+' '+label,kind,[b],[s],False)
            b=copy.deepcopy(a);body=b['proposed_xml'];start=body.index('5. Capital social');end=body.index('6. Modification du capital social' if s['source_id'].endswith('952') else '6. Variabilité du capital');block=body[start:end];b['proposed_xml']=body[:start]+body[end:]+block;gate(s['source_id']+' moved capital',kind,[b],[s],False)
(ROOT/(MODE+'-test-results.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2))
failed=[r for r in results if r['accepted']!=r['expected']]
print(MODE,len(results),'tests;',len(failed),'unexpected outcomes')
for r in failed:print(json.dumps(r,ensure_ascii=False))
raise SystemExit(bool(failed))
