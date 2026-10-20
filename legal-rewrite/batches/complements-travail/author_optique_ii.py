from pathlib import Path
import json,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[3];A=ROOT/'legal-rewrite/attachments'
a=next(x for x in json.loads((A/'rayonnements-optiques/source-reserved-snapshot.json').read_text()) if x['source_id']=='LEGIARTI000023018851')
root=E.fromstring('<r>'+a['source_xml']+'</r>');tables=list(root.iter('table'))
assert len(tables)==8
for t in tables:
 for el in t.iter():el.attrib={k:v for k,v in el.attrib.items() if k in {'rowspan','colspan'}}
def setcell(t,r,c,x):
 el=list(list(tables[t].iter('tr'))[r])[c];attrs=dict(el.attrib);el.clear();el.attrib.update(attrs);sub=E.fromstring('<x>'+x+'</x>');el.text=sub.text
 for child in list(sub):el.append(child)
# Corrections de transcription confrontées visuellement au tableau européen2.2, p24.
setcell(1,2,4,'1,8 × 10<sup>−5</sup> – 5 × 10<sup>−5</sup>')
setcell(1,3,2,'1 mm pour t ≤ 0,3 s ; 1,5 × t<sup>0,375</sup> mm pour 0,3 s &lt; t &lt; 10 s')
setcell(1,3,4,'H = 30 J·m<sup>−2</sup>')
setcell(1,11,1,'H = 630 J·m<sup>−2</sup> ; si t &lt; 1,6 × 10<sup>−4</sup> s, H = 5,6 × 10<sup>3</sup> × t<sup>0,25</sup> J·m<sup>−2</sup> ; voir note d')
setcell(1,12,1,'H = 10<sup>3</sup> J·m<sup>−2</sup> ; si t &lt; 1,0 × 10<sup>−3</sup> s, H = 5,6 × 10<sup>3</sup> × t<sup>0,25</sup> J·m<sup>−2</sup> ; voir note d')
setcell(1,13,0,'311')
for row,base,cut in [(13,'1,6','6,7 × 10<sup>−3</sup>'),(14,'2,5','4,0 × 10<sup>−2</sup>'),(15,'4,0','2,6 × 10<sup>−1</sup>'),(16,'6,3','1,6 × 10<sup>0</sup>')]:
 setcell(1,row,1,'H = '+base+' × 10<sup>3</sup> J·m<sup>−2</sup> ; si t &lt; '+cut+' s, H = 5,6 × 10<sup>3</sup> × t<sup>0,25</sup> J·m<sup>−2</sup> ; voir note d')
setcell(1,17,2,'H = 5,6 × 10<sup>3</sup> × t<sup>0,25</sup> J·m<sup>−2</sup>')
setcell(1,24,3,'H = 5,6 × 10<sup>3</sup> × t<sup>0,25</sup> J·m<sup>−2</sup>')
# Table2.4 : signe et unité perdus dans le XML.
setcell(2,1,0,'Longueur d’onde<sup>a</sup> [nm]')
setcell(2,4,5,'H = 1,1 × 10<sup>4</sup> C<sub>A</sub> t<sup>0,25</sup> [J·m<sup>−2</sup>]')
# Nettoyage des coquilles d’unités dans les tableaux de paramètres.
for t in tables:
 for el in t.iter():
  if el.text:el.text=el.text.replace('[mard]','[mrad]').replace('(mard)','(mrad)')
  if el.tail:el.tail=el.tail.replace('[mard]','[mrad]').replace('(mard)','(mrad)')
serialize=lambda i:E.tostring(tables[i],encoding='unicode',short_empty_elements=False)
body='''<p>RAYONNEMENTS OPTIQUES LASER</p>
<p>Les grandeurs d’exposition sont choisies selon la longueur d’onde et la durée du rayonnement. Une même source peut nécessiter le respect de plusieurs limites biophysiques.</p>
<p>Les limites des tableaux 2.2, 2.3 et 2.4 s’appliquent aux risques correspondants du tableau 2.1. Les coefficients CA, CB, CC, T1, T2, αmin et γ et les corrections d’exposition répétitive sont déterminés par les tableaux 2.5 et 2.6.</p>
<p>Tableau 2.1 — Risques associés aux rayonnements.</p>'''+serialize(0)+'''
<p>Tableau 2.2 — Limites d’exposition de l’œil au laser, durée inférieure à 10 s.</p>'''+serialize(1)+'''
<p>a) Si une longueur d’onde correspond à deux limites, la plus restrictive s’applique.</p>
<p>b) Pour 1 400 ≤ λ &lt; 10<sup>5</sup> nm, le diamètre limite est de 1 mm si t ≤ 0,3 s et de 1,5 × t<sup>0,375</sup> mm si 0,3 s &lt; t &lt; 10 s. Pour 10<sup>5</sup> ≤ λ &lt; 10<sup>6</sup> nm, il est de 11 mm.</p>
<p>c) Faute de données pour ces durées d’impulsion, la CIPRNI recommande d’utiliser les limites de luminance énergétique pour 1 ns.</p>
<p>d) Les valeurs correspondent à une impulsion. Pour plusieurs impulsions émises dans un intervalle Tmin du tableau 2.6, leurs durées sont additionnées ; cette somme remplace t dans 5,6 × 10<sup>3</sup> × t<sup>0,25</sup>.</p>
<p>Tableau 2.3 — Limites d’exposition de l’œil au laser, durée supérieure à 10 s, avec ses quatre notes d’application.</p>
<p><img src="media/optique-ii-tableau-2-3.png" alt="Tableau 2.3 complet : limites UV, lésions rétiniennes photochimiques et thermiques, IRA, IRB et IRC, diaphragmes, conditions temporelles et quatre notes"></p>
<p>Tableau 2.4 — Limites d’exposition de la peau au laser.</p>'''+serialize(2)+'''
<p>Tableau 2.5 — Coefficients et paramètres de calcul.</p>'''+''.join(serialize(i) for i in [3,4,5,6])+'''
<p>Tableau 2.6 — Les trois règles suivantes s’appliquent cumulativement aux expositions répétitives d’un laser pulsé ou à balayage :</p>
<p>1° Une impulsion d’un train ne dépasse pas la limite d’une impulsion unique de même durée ;</p>
<p>2° Un groupe ou sous-groupe d’impulsions délivré pendant t ne dépasse pas la limite correspondant à t ;</p>
<p>3° Chaque impulsion d’un groupe ne dépasse pas la limite d’une impulsion unique multipliée par Cp = N<sup>−0,25</sup>, N désignant le nombre d’impulsions. Cette troisième règle concerne les limites protégeant des lésions thermiques ; toutes les impulsions délivrées en moins de Tmin sont traitées comme une impulsion unique.</p>'''+serialize(7)+'''
<p>Grandeurs et calculs :</p>
<p>E = dP/dA, en W·m<sup>−2</sup> ; H = ∫<sub>0</sub><sup>t</sup> E(t) dt, en J·m<sup>−2</sup>.</p>
<p>dP : puissance en watts ; dA : surface en mètres carrés.</p>
<p>E(t) et E : éclairement énergétique ou densité de puissance incidente par unité de surface, en W·m<sup>−2</sup> ; ces valeurs proviennent de mesures ou du fabricant.</p>
<p>H : exposition énergétique, intégrale temporelle de l’éclairement énergétique, en J·m<sup>−2</sup>.</p>
<p>t : durée d’exposition en secondes ; λ : longueur d’onde en nanomètres.</p>
<p>γ : angle du cône limitant le champ de mesure ; γm : champ de mesure ; α : angle apparent de la source. Ces angles sont exprimés en milliradians.</p>
<p>Le diaphragme limite est la surface circulaire servant au calcul de l’éclairement et de l’exposition énergétiques moyens.</p>
<p>G : luminance énergétique intégrée sur la durée d’exposition, énergie par unité de surface rayonnante et d’angle solide, en J·m<sup>−2</sup>·sr<sup>−1</sup>.</p>'''
review='Source française intégrale et notes lues. Le tableau 2.3 absent du XML est restitué depuis la directive 2006/25/CE, consolidation française au 1er janvier 2014, p. 25, avec ses quatre notes, vérifiée visuellement. Les huit tableaux HTML français présents sont conservés ; des coquilles manifestes du XML sont corrigées par confrontation aux tableaux européens 2.2/2.4/2.5 : unité mm au lieu de min, borne 1,8×10^-5–5×10^-5, longueur 311 au lieu de 3111, puissances 10^3 perdues, opérateurs et t^0,25, nm au lieu de mn, unités Jm^-2 et mrad. Les valeurs et cas restants, les trois règles cumulatives, les sept bandes Tmin et les définitions sont conservés. La directive est un document normatif européen, pas le JO français authentifié : confrontation au JO du 4 juillet 2010, texte 11, restant à effectuer pour confirmer toutes les transpositions nationales et corrections de transcription. Aucune réduction des seuils ni validation juridique revendiquée.'
row={k:a[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':body,'reason':'Réorganise intégralement la sélection des limites, les huit tableaux présents, le tableau manquant et les règles cumulatives d’impulsions ; explicite les grandeurs et corrige les corruptions typographiques documentées sans modifier volontairement un seuil de protection.','review_notes':review,'status':'rewrite_draft'}
Path(__file__).with_name('002.json').write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
pdf=A/'rayonnements-optiques/directive-2006-25-ce-fr-2014.pdf';img=A/'media/optique-ii-tableau-2-3.png'
rec={'code_id':a['code_id'],'source_id':a['source_id'],'expected_markers':1,'documents':[{'path':str(pdf.relative_to(A)),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'url':'https://op.europa.eu/o/opportal-service/download-handler?identifier=e041a6cb-b992-414b-a541-bb39ecbf465e&format=pdfa1a&language=fr&productionSystem=cellar&part=','label':'Office des publications — directive 2006/25/CE, français, consolidation 2014'}],'media':[{'marker':1,'path':str(img.relative_to(A)),'page':25,'sha256':hashlib.sha256(img.read_bytes()).hexdigest(),'verified_visually':True,'label':'Tableau 2.3, toutes limites et quatre notes'}],'transcriptions':[],'documentary_recovery_complete':True,'authenticated_jo_crosscheck_complete':False,'provenance_notes':review}
(A/'records/travail-annexe-ii.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');print('AnnexeII',len(body),'caractères,',len(tables),'tablesHTML+image2.3')
