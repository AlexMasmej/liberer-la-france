from pathlib import Path
import json, hashlib, sys, importlib.util, datetime
P=Path(__file__).resolve().parent
ROOT=P.parents[2]
BASE=ROOT/'runtime/poursuite-20261020-d/graphic-sources/source-snapshot.json'
IDS=['LEGIARTI000006813811','LEGIARTI000032792438','LEGIARTI000039048613','LEGIARTI000049362876','LEGIARTI000019493914']
def sha(b): return hashlib.sha256(b).hexdigest()
def write(path,d):
    (P/path).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
data=[x for x in json.loads(BASE.read_text()) if x['source_id'] in IDS]
assert len(data)==5
write('source-snapshot.json',data)
(P/'canonical').mkdir(exist_ok=True)
guards=[]
for x in data:
    raw=x['raw_document_xml'].encode()
    (P/'canonical'/f"{x['source_id']}.xml").write_bytes(raw)
    guards.append({'source_id':x['source_id'],'raw_document_sha256':sha(raw),'expected_sha256':x['source_sha256'],'raw_document_hash_matches':sha(raw)==x['source_sha256'],'source_body_sha256':sha(x['source_xml'].encode()),'notes_sha256':sha(x['source_notes_xml'].encode()),'baseline_file_sha256':sha(BASE.read_bytes())})
assert all(x['raw_document_hash_matches'] for x in guards)
write('baseline-guards.json',guards)
spec=importlib.util.spec_from_file_location('source_assets_ro',ROOT/'source_assets.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
missing={
 IDS[0]:['Légende POS intégrale de l’arrêté du 11 mai 1984, art. 2, publiée au numéro complémentaire du JO du 17 juillet 1984 ; tous symboles, intitulés et notes.'],
 IDS[1]:['Formule de la valeur VN dans JO 0150 du 29 juin 2016, texte 48, décret 2016-855, art. 2.','Formule du taux tN dans le même texte.'],
 IDS[2]:['Formule intégrale de l’engagement total : JO 0303 du 30 décembre 2007, texte 157, décret 2007-1941, art. 1.'],
 IDS[3]:['Formule intégrale du facteur β_t à partir de z_t.','Équation intégrale déterminant le taux annuel i, JO 0303 du 31 décembre 2010, texte 67, décret 2010-1728, art. 1.'],
 IDS[4]:['Modèle entier CERFA 30-0812, avec cadres, rubriques, mentions, renvois et éventuel verso ; rattachement/version à prouver.','Modèle entier CERFA 30-0813, mêmes vérifications.']}
url={IDS[0]:'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006813811',IDS[1]:'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032791452',IDS[2]:'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017767416',IDS[3]:'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023333871',IDS[4]:'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019493914'}
version={IDS[0]:'Source canonique en vigueur depuis le 17 juillet 1984. Ne pas substituer la légende SUP de R126-1 ni le standard CNIG 2014 adapté.',IDS[1]:'Source canonique créée par décret 2016-855, art. 2, en vigueur depuis le 30 juin 2016. Les deux formules doivent correspondre au même décret et aux définitions canoniques.',IDS[2]:'Source canonique D453-7 en vigueur depuis le 1er septembre 2019. Sa formule est explicitement conservée par renvoi à l’ancien R453-7 de 2007 ; les contrôles du II et les renvois D453-2 courants ne doivent pas être remplacés par la version 2007.',IDS[3]:'Source canonique en vigueur depuis le 4 avril 2024. Préserver le tableau courant 75/55 points de base et la NOTA visant les offres émises à compter du 1er avril 2024 ; ne reprendre de 2010 que les deux graphiques que la source actuelle désigne.',IDS[4]:'Source canonique en vigueur depuis le 18 septembre 2008. Ne pas recomposer les modèles à partir des rubriques 2°/4° et ne pas importer les mentions historiques de Dalloz ou un CERFA moderne non concordé.'}
records=[]
for x in data:
    i=x['source_id']
    rec={'code_id':x['code_id'],'source_id':i,'source_sha256':x['source_sha256'],'number':x['number'],'expected_markers':len(m.graphic_markers(x['source_xml'])),'documentary_recovery_complete':False,'authenticated_jo_crosscheck_complete':False,'status':'pending_primary_documentary_recovery_do_not_activate','media':[],'transcriptions':[],'documents':[],'primary_reference_url':url[i],'missing_elements':missing[i],'canonical_version_concordance_notes':version[i],'canonical_notes_preserved':True,'source_read_in_full':True,'notes_read_in_full':True,'proposed_xml':None,'provenance_notes':'Notices isolées de recherche. Aucun registre actif, base, lot, pièce jointe active ou publication modifié. Les résultats de recherche et réponses HTML de protection ne constituent pas des pièces récupérées.'}
    write('registry-proposal/records/'+i+'.json',rec); records.append(rec)
loaded=m.load_companions(P/'registry-proposal')
checks=[{'source_id':x['source_id'],'source_assets_schema_load_passed':(x['code_id'],x['source_id']) in loaded,'recovery_complete':m.recovery_complete(x['source_xml'],loaded[(x['code_id'],x['source_id'])])}for x in data]
assert all(not c['recovery_complete'] for c in checks)
write('companion-record-proposals.json',records)
write('companion-validation.json',checks)
print(json.dumps({'sources':len(data),'all_xml_hashes_match':True,'loaded_companions':len(loaded),'recovery_complete_count':sum(c['recovery_complete'] for c in checks)}))
