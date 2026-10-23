from pathlib import Path
import sys,json,copy,sqlite3,hashlib
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;C=D/'candidate';O=D.parent;P=O.parents[1];sys.path.insert(0,str(C))
import run_exhaustive as run,register_batches as reg,reference_coherence as refs
s=json.loads((D/'evidence/construction-habitation-00195/source.json').read_text())[0];row=json.loads((O/'batch-row.json').read_text());results=[]
def test(name,a,expect=False,source=None):
 source=source or s
 for gate in ('validate_answer','validate_batches'):
  try:
   if gate=='validate_answer':run.validate_answer([copy.deepcopy(a)],[source])
   else:
    d=sqlite3.connect(':memory:');d.executescript('CREATE TABLE articles(code_id,id,number,source_sha256,content_xml,valid_from,valid_until);CREATE TABLE documents(code_id,id,kind,xml);CREATE TABLE drafts(code_id,source_id,source_sha256,proposed_xml);');d.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)',(source['code_id'],source['source_id'],source['number'],source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until']));d.execute('INSERT INTO documents VALUES(?,?,?,?)',(source['code_id'],source['source_id'],'ARTICLE','<ARTICLE><NOTA><CONTENU>'+source.get('source_notes_xml','')+'</CONTENU></NOTA></ARTICLE>'));b=C/'variant-test-batches'/'isolated';b.mkdir(parents=True,exist_ok=True);(b/'00001.json').write_text(json.dumps([a],ensure_ascii=False));reg.validate_batches(d,b.parent);d.close()
   ok=True;err=None
  except Exception as e:ok=False;err=str(e)
  results.append({'name':name,'gate':gate,'accepted':ok,'expected':expect.get(gate,False) if isinstance(expect,dict) else expect,'error':err})
a=copy.deepcopy(row)
for k in ('reference_coherence','substantive_impact_certificate'):a.pop(k,None)
test('current reviewed Annexe II',a,True)
mutations=[
('capital digits','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.','Le capital statutaire est fixé à 100 euros.'),
('capital words','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.','Le capital statutaire est fixé à cent euros.'),
('nominal fixed','La valeur nominale des parts sociales, exprimée en euros, est fixée dans les statuts.','La valeur nominale des parts sociales est de 10 euros.'),
('currency','exprimé en euros','exprimé en dollars'),
('notice fixed months','dont la durée en mois est fixée dans les statuts','dont la durée est de trois mois'),
('notice fixed days','dont la durée en mois est fixée dans les statuts','dont la durée est de quinze jours'),
('notice unit days','dont la durée en mois est fixée dans les statuts','dont la durée en jours est fixée dans les statuts'),
('concrete name','La dénomination choisie par les associés et inscrite dans les statuts','La dénomination Exemple'),
('concrete address',"Le siège social est fixé à l'adresse inscrite dans les statuts.",'Le siège social est fixé à Paris.'),
('remove parameter',"Le siège social est fixé à l'adresse inscrite dans les statuts.",''),
('duplicate parameter',"Le siège social est fixé à l'adresse inscrite dans les statuts.","Le siège social est fixé à l'adresse inscrite dans les statuts. Le siège social est fixé à l'adresse inscrite dans les statuts."),
('different decision maker','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.','Le montant du capital statutaire, exprimé en euros, est fixé par le président.'),
('remove fixation','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.','Le capital est variable.'),
('capital minimum','Il ne peut être inférieur à celui exigé par le deuxième alinéa de l\'article 27 de la loi du 10 septembre 1947 précitée,','Il peut être inférieur au minimum légal,'),
('capital quarter','inférieure au quart du capital le plus élevé','inférieure au dixième du capital le plus élevé'),
('capital ceiling',"ni supérieur au plafond d'émission fixé par l'assemblée générale extraordinaire.",'sans plafond.'),
('capital 50pct','limite de 50 %','limite de 80 %'),
('silence refusal','Le refus d\'agrément résulte soit',"L'agrément résulte soit"),
('silence approval',"l'agrément est considéré comme donné","l'agrément est considéré comme refusé"),
('purchase floor','le prix ne peut être inférieur','le prix peut être inférieur'),
('three months','un délai de trois mois','un délai de neuf mois'),
('six months','un délai de six mois','un délai de douze mois'),
('five years','pendant cinq années','pendant dix années'),
('livret rate','majoré de 1,5 point','majoré de 3 points'),
('board size','vingt-deux membres','trente membres'),
('tenants','trois administrateurs en qualité','un administrateur en qualité'),
('free transfer','Les parts sociales peuvent être librement cédées à un autre associé.','Les parts sociales ne peuvent être cédées.'),
('capital publication','ne sont pas assujettis aux formalités de dépôt et de publication','sont assujettis aux formalités de dépôt et de publication'),
('withdrawal nominal','obtenir le remboursement de sa ou de ses parts sociales à la valeur nominale','obtenir un remboursement discrétionnaire'),
('note4 expansion','Cette clause devient obligatoire dans le cas contraire.','Cette clause est toujours facultative.'),
('note4 removal','(4) Cette clause est facultative','Cette clause est facultative'),
('liquidation threshold','la portion d\'actif qui excéderait la moitié du capital social','la totalité de l\'actif'),
('cooperative revision','La société fait procéder périodiquement','La société peut faire procéder'),
]
for name,old,new in mutations:
 b=copy.deepcopy(a);assert old in b['proposed_xml'],name;b['proposed_xml']=b['proposed_xml'].replace(old,new,1);test(name,b)
for name,phrase in [('move seat',"Le siège social est fixé à l'adresse inscrite dans les statuts."),('move capital','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.')]:
 b=copy.deepcopy(a);b['proposed_xml']=b['proposed_xml'].replace(phrase,'',1)+'<p>'+phrase+'</p>';test(name,b)
for name,phrase in [('truncated capital despite heading', 'Le capital effectif est variable et entièrement libéré lors de la souscription de parts sociales.'),('remove reserve protection','Ce remboursement ne comporte aucune part de fonds de réserve.'),('remove optional note1','(1) Le présent alinéa ainsi que les quatre alinéas suivants sont facultatifs et peuvent être ajoutés ou retirés par décision de l’assemblée générale de la société.')]:
 b=copy.deepcopy(a);phrase=phrase.replace('’',"'");assert phrase in b['proposed_xml'];b['proposed_xml']=b['proposed_xml'].replace(phrase,'',1);test(name,b)
for mark in ['[…]','[...]','[ … ]','TODO','&lt;placeholder&gt;','[&#8230;]']:
 b=copy.deepcopy(a);b['proposed_xml']+='<p>'+mark+'</p>';test('new marker '+mark,b)
for field,value in [('source_sha256','bad'),('source_xml',s['source_xml']+' '),('source_notes_xml','altered')]:test('source '+field,a,source=dict(s,**{field:value}))
b=copy.deepcopy(a);b['substantive_impact']={'version':999};test('bad impact',b)
b=copy.deepcopy(a);b.pop('benefit_review');test('missing benefit (flagged source)',b,{'validate_answer':False,'validate_batches':True},source=dict(s,benefit_check_required=True))
# Both real immutable historical snapshot guard and existing current certificate remain stale.
db=sqlite3.connect((P/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
try:
 try:refs.check_guards(db,json.loads((D/'evidence/construction-habitation-00195/reference-targets.json').read_text()));ok=True;err=None
 except Exception as e:ok=False;err=str(e)
 results.append({'name':'stale original reference snapshot','gate':'check_guards','accepted':ok,'expected':False,'error':err})
 guards=row['reference_coherence']['targets'];ok=all(refs.guard(refs.state(db,k))==v for k,v in guards.items());results.append({'name':'current draft certificate guards','gate':'state+guard','accepted':ok,'expected':False})
finally:db.close()
(D/'variant-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));bad=[r for r in results if r['accepted']!=r['expected']];print(json.dumps({'tests':len(results),'unexpected':bad},ensure_ascii=False,indent=2));raise SystemExit(bool(bad))
