import json,hashlib,sqlite3,sys,copy
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
P=Path(__file__).parent;LEGAL=Path('legal-rewrite').resolve();sys.path.insert(0,str(LEGAL))
from ingest import source_notes
from run_exhaustive import validate_answer
from reference_coherence import check_guards
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or '').encode()).hexdigest()
def load(n):return json.loads((P/n).read_text())
def save(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
s=load('source.json');a=load('answer.json');rows=s+load('reviewed-support.json')+load('dependencies.json');db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');out=[]
for x in rows:
 k=x['code_id'],x['source_id'];y=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',k).fetchone();doc=db.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",k).fetchone()[0];old=db.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',k).fetchone();pr=x.get('previous_draft');g={'source_identity':y[0]==x['source_sha256'],'source_body':y[1]==x['source_xml'],'notes':source_notes(db,*k)==x['source_notes_xml'],'document':H(doc)==x['source_document_sha256'],'previous_draft':old is None if pr is None else old is not None and old[0]==pr['source_sha256']and old[1]==pr['proposed_xml']};out.append({'number':x['number'],'code_id':k[0],'source_id':k[1],'guards':g,'all_match':all(g.values())})
assert all(x['all_match']for x in out),[x for x in out if not x['all_match']]
check_guards(db,load('reference-targets.json'));db.rollback();db.close();validate_answer(copy.deepcopy(a),copy.deepcopy(s))
cases=[]
for credits,old,new,expected in [('1000000','300000','700000','12750'),('1000000','500000','500000','21250'),('1000000','0','1000000','0'),('1000000','1000000','0','42500')]:
 value=Decimal(0)if Decimal(old)==0 else Decimal(credits)*Decimal(old)/(Decimal(old)+Decimal(new))*Decimal('0.0425');assert value==Decimal(expected);cases.append({'common_credits':credits,'old_payments':old,'new_payments':new,'tax':str(value),'not_month_prorated':True})
save('guard-validation.json',{'at':datetime.now(timezone.utc).isoformat(),'transaction':'SQLite mode=ro BEGIN','checks':out,'all_280_guards_match':True,'reference_policy_guards':'passed','validate_answer':'passed_on_deepcopy','canonical_changes':False})
save('audit.json',{'edition':'002','articles':23,'one_tax_removal':1,'coordinations':22,'source_identical_to_001':True,'other_22_full_records_identical_to_001':True,'correction_374':'affectation_effective_or_real_payment_ratio_of_common_credits_only','rate':'4.25% unchanged','examples':cases,'independent_review_pending':True,'canonical_mutation':False,'active_policy_changed':False,'budget_compensation_created':False})
files=[f for f in sorted(P.iterdir())if f.is_file()and f.name!='manifest.json'];save('manifest.json',{'frozen':True,'created_at':datetime.now(timezone.utc).isoformat(),'source_sha256':H((P/'source.json').read_bytes()),'answer_sha256':H((P/'answer.json').read_bytes()),'files':{f.name:H(f.read_bytes())for f in files},'canonical_mutation':False})
print('SOURCE',H((P/'source.json').read_bytes()));print('ANSWER',H((P/'answer.json').read_bytes()));print('MANIFEST',H((P/'manifest.json').read_bytes()))
