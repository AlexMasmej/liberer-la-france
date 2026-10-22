"""Traceable correction of our earlier complete CGI154quinquies proposal."""
import hashlib,json,time
from ingest import HERE,open_db,source_evidence,source_notes,atomic_json
from register_batches import writer_lock

code='LEGITEXT000006069577';identifier='LEGIARTI000054336634'
old="est admise en déduction à hauteur de 6,6 points du montant brut des rémunérations au titre desquelles elle a été acquittée."
new="est intégralement admise en déduction du montant brut des rémunérations au titre desquelles elle a été acquittée. Le montant déduit ne peut excéder la contribution effectivement acquittée ; il est déterminé sur l'assiette ayant servi à son prélèvement, après application des abattements légalement applicables à cette assiette."

with writer_lock():
    db=open_db(HERE/'corpus.sqlite')
    try:
        source=db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',(code,identifier)).fetchone()
        draft=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',(code,identifier)).fetchone()
        evidence=db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',(code,identifier)).fetchone()
        assert source and draft and draft[0]==source[1]
        assert evidence==(source_evidence(source[2],source_notes(db,code,identifier)),source[3],source[4])
        if new in draft[2]:raise SystemExit('Correction already registered; no change')
        assert draft[2].count(old)==1,'Earlier target wording changed; manual comparison required'
        before={'code_id':code,'source_id':identifier,'source_sha256':draft[0],'status':draft[1],'proposed_xml':draft[2],'reason':draft[3],'review_notes':draft[4]}
        after=before|{'number':source[0],'proposed_xml':draft[2].replace(old,new,1),'reason':'Article intégral avec déductibilité complète de la CSG salariale privée proposée à6,6%. La déduction est limitée à la contribution réellement acquittée et utilise son assiette après abattements ; les autres catégories et régimes de déduction sont conservés.','review_notes':'Correction de notre proposition antérieure : écrire6,6points du brut pouvait être compris comme une déduction supérieure à la CSG payée lorsque son assiette est abattue. La nouvelle phrase retient le montant réellement acquitté, sans modifier les assiettes ni le taux de CSG. À3000euros bruts sur assiette98,25%, la contribution proposée est194,535euros avant arrondis, et sa déduction ne peut dépasser ce montant ; le gain net avant impôt de la baisse de taux reste76,635euros avant arrondis. Le II, y compris sa dérogation de2026, les autres taux et les notes officielles sont conservés. Coordonner financement et entrée en vigueur avec L136-8, et vérifier les avantages d’actionnariat salarié et situations particulières. Proposition non validée par un juriste.'}
        atomic_json(HERE/'revisions/cgi154-deduction-base-20261019.json',{'updated_at_unix':int(time.time()),'purpose':'Correct deduction basis without exceeding actual CSG payment','before':before,'after':after})
        atomic_json(HERE/'batches/fiscalite/012.json',[after])
        registry_path=HERE/'registered-batches.json';registry=json.loads(registry_path.read_text())
        registry[code+'|'+identifier]={'source_sha256':source[1],'proposed_sha256':hashlib.sha256(draft[2].encode()).hexdigest(),'adopted_prior_project_draft_for_documented_revision':'revisions/cgi154-deduction-base-20261019.json'}
        atomic_json(registry_path,registry)
    finally:db.close()
print('Complete prior proposal preserved; correction staged for source-bound validation.')
