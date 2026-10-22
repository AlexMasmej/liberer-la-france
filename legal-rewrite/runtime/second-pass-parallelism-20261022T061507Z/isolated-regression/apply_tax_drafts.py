"""Apply explicit reform edits to entire source articles, retaining all other text.

This does not silently replace every instance of a rate or count an unchanged
article as rewritten. The full resulting article is stored and downloadable.
"""
from ingest import HERE,open_db,source_notes,source_evidence
import json,xml.etree.ElementTree as ET
db=open_db(HERE/'corpus.sqlite')
changes=[
 {
  'code':'LEGITEXT000006069577','number':'154 quinquies',
  'old':'<p>II. – La contribution afférente',
  'new':'<p>Par dérogation au premier alinéa du présent I, la contribution prélevée au taux de 6,6 % sur les rémunérations salariées versées par un employeur de droit privé, en application du 1° du I de l’article L. 136-8 du code de la sécurité sociale, est admise en déduction à hauteur de 6,6 points du montant brut des rémunérations au titre desquelles elle a été acquittée.</p>\n<p>II. – La contribution afférente',
  'reason':'Article 154 quinquies reproduit en entier, avec ajout au I d’une déductibilité de 6,6 points pour la CSG salariale privée proposée. Les autres catégories, taux et régimes de déduction sont conservés.',
  'notes':'Coordination directe avec la rédaction proposée du 1° du I de l’article L. 136-8 du CSS. Le régime fiscal des avantages d’actionnariat salarié et les situations particulières doivent être vérifiés ; financement et entrée en vigueur doivent être communs aux deux articles.'
 },
 {
  'code':'LEGITEXT000006069577','number':'219',
  'old':"Le taux normal de l'impôt est fixé à 25 %.",
  'new':"Le taux normal de l'impôt est fixé à 20 %.",
  'reason':'Article 219 réécrit en entier avec une modification ciblée : taux normal national de l’IS de 25 % à 20 %. Tous les autres alinéas et régimes de cet article sont reproduits sans changement.',
  'notes':'La part locale éventuelle de 0 à 5 points nécessite un dispositif distinct. Les régimes dérogatoires et taux spécifiques, notamment ceux qui restent à 25 %, sont conservés dans ce lot et doivent être arbitrés explicitement. Financement, entrée en vigueur et coordination avec les autres dispositifs fiscaux restent à établir.'
 },
 {
  'code':'LEGITEXT000006073189','number':'L136-8',
  'old':"1° A 9,2 % pour la contribution sociale mentionnée à l'article L. 136-1 ;",
  'new':"1° À 9,2 % pour la contribution sociale mentionnée à l’article L. 136-1. Ce taux est ramené à 6,6 % pour les rémunérations salariées versées par un employeur de droit privé. Les autres revenus d’activité ainsi que les revenus de remplacement conservent les taux qui leur sont applicables, sous réserve des dérogations prévues au présent article ;",
  'reason':'Article L. 136-8 réécrit en entier avec une baisse ciblée de CSG salariale de 9,2 % à 6,6 % pour les rémunérations versées par un employeur de droit privé. Les autres alinéas, taux, seuils et règles sont reproduits sans changement.',
  'notes':'La déductibilité doit être coordonnée avec l’article 154 quinquies du CGI, et l’affectation des recettes avec les comptes sociaux. Il faut expertiser le périmètre des employeurs de droit privé, les assiettes et les régimes particuliers. La CRDS n’est pas modifiée. L’entrée en vigueur doit être conditionnée au financement voté et à la coordination retraite.'
 }
]
result=[]
for change in changes:
 rows=db.execute('SELECT id,content_xml,source_sha256,valid_from,valid_until FROM articles WHERE code_id=? AND number=? AND valid_from<=? AND valid_until>?',(change['code'],change['number'],'2026-10-18','2026-10-18')).fetchall()
 if len(rows)!=1:raise RuntimeError('Source version is missing or ambiguous for '+change['number'])
 identifier,source,sha,start,end=rows[0]
 if source.count(change['old'])!=1:raise RuntimeError('Target wording is not unique for '+change['number'])
 proposed=source.replace(change['old'],change['new'],1)
 ET.fromstring('<CONTENU>'+proposed+'</CONTENU>')
 db.execute('INSERT OR REPLACE INTO drafts VALUES(?,?,?,?,?,?,?)',(change['code'],identifier,sha,'rewrite_draft',proposed,change['reason'],change['notes']))
 db.execute('INSERT OR REPLACE INTO draft_sources VALUES(?,?,?,?,?)',(change['code'],identifier,source_evidence(source,source_notes(db,change['code'],identifier)),start,end))
 result.append({'code_id':change['code'],'source_id':identifier,'number':change['number'],'source_sha256':sha,'status':'rewrite_draft','proposed_xml':proposed,'reason':change['reason'],'review_notes':change['notes']})
db.commit()
(HERE/'tax-drafts-bound.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(len(result),'complete tax articles drafted; source lengths retained:',[len(r['proposed_xml']) for r in result])
