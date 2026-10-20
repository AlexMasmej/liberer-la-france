from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[3]
records=json.loads((ROOT/'sites/liberer-la-retraite/dist/corpus/construction-habitation.json').read_text())
out=[]
pdf=ROOT/'legal-rewrite/attachments/apl/bareme-ministere-2024.pdf'
url='https://www.ecologie.gouv.fr/sites/default/files/documents/Brochure-bareme-2024-APL.pdf'
for a in records:
    if a['number'] not in {'D832-11','D832-25'}:continue
    tables=re.findall(r'<table>.*?</table>',a['source_xml'],re.S)
    if a['number']=='D832-11':
        body='''<p>Le coefficient « K » mentionné au 2° de l'article D. 832-10 est calculé selon la formule suivante :</p>
<p>K = 0,95 − R / (cm × N).</p>
<p>Pour l'application de cette formule :</p>
<p>1° « K » désigne le coefficient de prise en charge. Il est arrondi à deux décimales par défaut et plafonné à 0,95 ;</p>
<p>2° « R » désigne les ressources du ménage, appréciées conformément à la section 2 du chapitre II du titre II du présent livre et arrondies à la centaine d'euros supérieure ;</p>
<p>3° « cm » désigne le coefficient multiplicateur fixé par arrêté ;</p>
<p>4° « N » désigne le nombre de parts résultant du barème suivant :</p>'''+tables[0]
        transcriptions=[{'marker':1,'page':44,'text':'K = 0,95 − R / (cm × N)','verified_visually':True}]
        note='La brochure emploie cm3 pour distinguer le barème accession ; la proposition conserve le symbole cm défini au 3° de cet article. Le montant 22 111,33 de la brochure reste une valeur fixée par arrêté et n’est pas figé dans le code.'
    else:
        body='''<p>Le coefficient « K » défini au 2° de l'article D. 832-24 est calculé conformément au 1° du présent article.</p>
<p>Par exception, le 2° s'applique aux logements-foyers de jeunes travailleurs conventionnés après le 30 septembre 1990 et aux résidences sociales conventionnées après le 31 décembre 1994 en application du 5° de l'article L. 831-1, mentionnés au 1° de l'article R. 832-21.</p>
<p>1° K = 0,95 − (R − r × N) / (cm × N).</p>
<p>Dans cette formule :</p>
<p>a) « K » désigne le coefficient de prise en charge. Il est arrondi à deux décimales par défaut et plafonné à 0,95 ;</p>
<p>b) « R » désigne les ressources du ménage, appréciées selon la section 2 du chapitre II du titre II du présent livre et arrondies à la centaine d'euros supérieure ;</p>
<p>c) « r » désigne un coefficient fixé par arrêté ;</p>
<p>d) « cm » désigne un coefficient multiplicateur fixé par arrêté ;</p>
<p>e) « N » désigne le nombre de parts résultant du barème suivant :</p>'''+tables[0]+'''
<p>2° K = 0,90 − R / (cm × N).</p>
<p>Dans cette formule :</p>
<p>a) « K » désigne le coefficient de prise en charge. Il est arrondi à deux décimales par défaut et plafonné à 0,90 ;</p>
<p>b) « R » désigne les ressources du ménage, appréciées selon la section 2 du chapitre II du titre II du présent livre et arrondies à la centaine d'euros supérieure ;</p>
<p>c) « cm » désigne un coefficient multiplicateur fixé par arrêté ;</p>
<p>d) « N » désigne le nombre de parts résultant du barème suivant :</p>'''+tables[1]
        transcriptions=[{'marker':1,'page':31,'text':'K = 0,95 − (R − r × N) / (cm × N)','verified_visually':True},{'marker':2,'page':31,'text':'K = 0,90 − R / (cm × N)','verified_visually':True}]
        note='La brochure distingue cm1 et cm2 ; la proposition garde cm dans chacun des deux régimes, conformément aux définitions du code. Les montants r=1 217,26, cm1=13 393,40 et cm2=21 420,91 ne sont pas ajoutés au code : ils relèvent de l’arrêté. Les deux barèmes N, seuils, arrondis et dates de conventionnement restent distincts.'
    review='Réécriture à droit constant proposée. Formule(s) absente(s) du XML LEGI retrouvée(s) dans la brochure officielle du ministère, édition avril 2024, et vérifiée(s) visuellement. Cette brochure est une source documentaire, pas un extrait du JO authentifié : confrontation à l’original JO encore à effectuer. '+note+' Aucune validation par un juriste revendiquée.'
    out.append({k:a[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':body,'reason':'Explicite le calcul et ses paramètres, réintègre la formule documentaire manquante et conserve intégralement les tableaux, plafonds, arrondis et champs de bénéficiaires. Aucun changement de fond recherché.','review_notes':review,'status':'rewrite_draft'})
    companion={'code_id':a['code_id'],'source_id':a['source_id'],'media':[],'documents':[{'path':'apl/bareme-ministere-2024.pdf','sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'url':url,'label':'Ministère — Aides personnelles au logement, éléments de calcul, avril 2024'}],'transcriptions':transcriptions,'expected_markers':len(transcriptions),'documentary_recovery_complete':True,'authenticated_jo_crosscheck_complete':False,'provenance_notes':review}
    (ROOT/'legal-rewrite/attachments/records'/('apl-'+a['number']+'.json')).write_text(json.dumps(companion,ensure_ascii=False,indent=2))
Path(__file__).with_name('001.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
