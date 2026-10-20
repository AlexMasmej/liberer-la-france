from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];A=ROOT/'legal-rewrite/attachments'
src=json.loads((A/'rayonnements-optiques/source-reserved-snapshot.json').read_text())
a=next(x for x in src if x['source_id']=='LEGIARTI000040477365')
images=[('optique-i-formules-integrales.png',14,'Formules intégrales a à o et domaines spectraux associés'),('optique-i-formules-discretes-a-d.png',14,'Formules discrètes a à d'),('optique-i-formules-discretes-e-o.png',15,'Formules discrètes e à o'),('optique-i-tableau-1-1-a-f.png',17,'Tableau 1.1, lignes a à f : limites UV et lumière bleue'),('optique-i-tableau-1-1-g-n.png',18,'Tableau 1.1, lignes g à n : limites thermiques rétiniennes et infrarouges'),('optique-i-tableau-1-1-o-notes.png',19,'Tableau 1.1, ligne o et deux notes : peau et petites sources'),('optique-i-tableau-1-2.png',20,'Tableau 1.2 : pondération spectrale S, première partie'),('optique-i-tableaux-1-2-suite-1-3.png',21,'Tableau 1.2, suite, et tableau 1.3 : pondérations B et R')]
body='''<p>RAYONNEMENTS OPTIQUES INCOHÉRENTS</p>
<p>Les grandeurs d’exposition sont choisies selon le domaine spectral du rayonnement émis. Leurs valeurs sont calculées avec les expressions ci-dessous et comparées aux limites correspondantes du tableau 1.1. Une même source peut nécessiter plusieurs grandeurs et le respect de plusieurs limites.</p>
<p>Les repères a à o des expressions correspondent aux lignes du tableau 1.1.</p>
<p>1° Calcul par intégration :</p>'''
body+='<p><img src="media/'+images[0][0]+'" alt="'+images[0][2]+'"></p>'
body+='<p>2° Les expressions précédentes peuvent être remplacées par les sommes discrètes suivantes, avec les pondérations des tableaux 1.2 et 1.3 :</p>'
for n,_,alt in images[1:3]:body+='<p><img src="media/'+n+'" alt="'+alt+'"></p>'
body+='''<p>3° Définitions et unités :</p>
<p>Eλ(λ,t) et Eλ : éclairement énergétique spécifique ou densité de puissance spectrique ; puissance rayonnée incidente par unité de surface, exprimée en W·m<sup>−2</sup>·nm<sup>−1</sup>. Ces valeurs résultent de mesures ou sont communiquées par le fabricant.</p>
<p>Eeff : éclairement énergétique efficace ultraviolet, calculé de 180 à 400 nm avec la pondération S(λ), en W·m<sup>−2</sup>.</p>
<p>H : exposition énergétique, intégrale temporelle de l’éclairement énergétique, en J·m<sup>−2</sup>.</p>
<p>Heff : exposition énergétique efficace pondérée par S(λ), en J·m<sup>−2</sup>.</p>
<p>EUVA : éclairement énergétique total ultraviolet A, intégré de 315 à 400 nm, en W·m<sup>−2</sup>.</p>
<p>HUVA : exposition énergétique dans la bande 315 à 400 nm, intégrée ou sommée sur le temps et la longueur d’onde, en J·m<sup>−2</sup>.</p>
<p>S(λ) : pondération spectrale sans dimension des effets des UV sur les yeux et la peau, définie au tableau 1.2.</p>
<p>t et Δt : durée d’exposition, en secondes ; λ : longueur d’onde, en nanomètres ; Δλ : largeur de bande des intervalles de calcul ou de mesure, en nanomètres.</p>
<p>Lλ(λ) et Lλ : luminance énergétique spécifique de la source, en W·m<sup>−2</sup>·sr<sup>−1</sup>·nm<sup>−1</sup>.</p>
<p>R(λ) : pondération spectrale sans dimension des lésions thermiques de l’œil dues aux rayonnements visibles et IRA, définie au tableau 1.3.</p>
<p>LR : luminance énergétique efficace pondérée par R(λ), en W·m<sup>−2</sup>·sr<sup>−1</sup>.</p>
<p>B(λ) : pondération spectrale sans dimension des lésions photochimiques de l’œil dues à la lumière bleue, définie au tableau 1.3.</p>
<p>LB : luminance énergétique efficace pondérée par B(λ), en W·m<sup>−2</sup>·sr<sup>−1</sup>.</p>
<p>EB : éclairement énergétique efficace pondéré par B(λ), en W·m<sup>−2</sup>.</p>
<p>EIR : éclairement énergétique total infrarouge dans la bande 780 à 3 000 nm, en W·m<sup>−2</sup>.</p>
<p>Epeau : éclairement énergétique total visible, IRA et IRB dans la bande 380 à 3 000 nm, en W·m<sup>−2</sup>.</p>
<p>Hpeau : exposition énergétique intégrée ou sommée sur le temps et la longueur d’onde dans la bande 380 à 3 000 nm, en J·m<sup>−2</sup>.</p>
<p>α : angle apparent : l’angle sous-tendu par une source apparente, telle que vue en un point de l’espace, exprimé en milliradians (mrad). La source apparente est l’objet réel ou virtuel qui forme l’image rétinienne la plus petite possible.</p>
<p>4° Valeurs limites et pondérations :</p>'''
for n,_,alt in images[3:]:body+='<p><img src="media/'+n+'" alt="'+alt+'"></p>'
review='Réécriture documentaire proposée sans changement de seuil. Le XML français ne reproduit ni l’annexe initiale ni sa modification. Les expressions et tableaux 1.1 à 1.3 sont récupérés intégralement dans l’annexe I de la directive 2006/25/CE, version française consolidée au 1er janvier 2014, pages 14 à 21, téléchargée via l’Office des publications et vérifiée visuellement. La définition α/source apparente est celle ajoutée en droit français par l’article 3 du décret 2019-1547, consulté sur Légifrance. Les seuils, bornes, unités, 221 pondérations S(λ), pondérations B/R et deux notes du tableau1.1 restent représentés. La directive est une source normative européenne, pas le fac-similé authentifié du JO français de 2010 ou 2019 : confrontation des tableaux français encore à effectuer. Aucune validation juridique revendiquée.'
row={k:a[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':body,'reason':'Réorganise le choix des grandeurs, les calculs, les définitions et les limites, restitue toutes les formules et tous les tableaux absents du XML, et conserve explicitement la définition française ajoutée en 2019. Aucun allègement des seuils de protection.','review_notes':review,'status':'rewrite_draft'}
Path(__file__).with_name('001.json').write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
pdf=A/'rayonnements-optiques/directive-2006-25-ce-fr-2014.pdf'
url='https://op.europa.eu/o/opportal-service/download-handler?identifier=e041a6cb-b992-414b-a541-bb39ecbf465e&format=pdfa1a&language=fr&productionSystem=cellar&part='
record={'code_id':a['code_id'],'source_id':a['source_id'],'expected_markers':2,'documents':[{'path':str(pdf.relative_to(A)),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'url':url,'label':'Office des publications — directive 2006/25/CE, français, consolidation 2014'}],'media':[{'marker':1,'path':'media/'+n,'page':page,'sha256':hashlib.sha256((A/'media'/n).read_bytes()).hexdigest(),'verified_visually':True,'label':alt} for n,page,alt in images],'transcriptions':[{'marker':2,'text':'α : angle apparent : l’angle sous-tendu par une source apparente, telle que vue en un point de l’espace, exprimé en milliradians (mrad). La source apparente est l’objet réel ou virtuel qui forme l’image rétinienne la plus petite possible.','url':'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039699711','article':'3','verified_against_official_text':True}],'documentary_recovery_complete':True,'authenticated_jo_crosscheck_complete':False,'provenance_notes':review}
(A/'records/travail-annexe-i.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('AnnexeI :',len(body),'caractères,',len(images),'images,companion2marqueurs')
