from pathlib import Path
import json,re,hashlib,datetime
P=Path(__file__).resolve().parent
sha=lambda x:hashlib.sha256(x.encode()).hexdigest()
texta=json.loads((P/'crpa-definitions-primary-search.json').read_text());textb=json.loads((P/'crpa-primary-search.json').read_text());records=[]
for number,t,start,end,url in [
('L100-3',texta,'Au sens du présent code et sauf disposition contraire de celui-ci, on entend par :',"l'exercice de cette mission.",'https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031367308'),
('L113-12',texta,'Une personne présentant une demande ou produisant une déclaration à une administration ne peut être tenue',"défini à l'article L. 114-8.",'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045213328'),
('L114-8',textb,'I.-Les administrations échangent entre elles toutes les informations ou les données strictement nécessaires',"dans les conditions prévues à l'article L. 312-1-1.",'https://www.legifrance.gouv.fr/affichCodeArticle.do?categorieLien=cid&cidTexte=LEGITEXT000031366350&dateTexte=&idArticle=LEGIARTI000031367412'),
('L114-9',textb,"Les échanges d'informations ou de données entre administrations prévues à l'article L. 114-8 s'effectuent",'la liste des administrations chargées de les mettre à la disposition des autres administrations.','https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045213308')]:
 matches=[]
 for block in t.split('--------------------------------------------------------------------------------'):
  if start not in block or end not in block:continue
  for hit in re.finditer(re.escape(start),block):
   finish=block.find(end,hit.start())
   if finish<0:continue
   body=block[hit.start():finish+len(end)]
   if '...'in body or '[Button'in body or '##'in body:continue
   matches.append(body)
 assert matches,number
 body=min(matches,key=len);assert not('##'in body),number
 records.append(dict(number=number,body=body,body_sha256=sha(body),source_url=url,version_since='2016-01-01'if number=='L100-3'else'2022-02-23',provenance='Texte complet primaire renvoyé par recherche Légifrance ; extraction du corps, pas XML DILA original',capture_file='crpa-definitions-primary-search.json'if t is texta else'crpa-primary-search.json'))
(P/'crpa-primary-bodies.json').write_text(json.dumps(dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_xml_recovered=False,direct_open_status=403,records=records),ensure_ascii=False,indent=2)+'\n')
print([(x['number'],len(x['body']),x['body_sha256'])for x in records])
