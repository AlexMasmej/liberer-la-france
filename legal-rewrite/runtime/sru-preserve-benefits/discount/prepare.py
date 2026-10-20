from pathlib import Path
import copy,datetime,hashlib,json,re,sys,tarfile,xml.etree.ElementTree as ET
sys.path.insert(0,str(Path('legal-rewrite').resolve()))
from run_exhaustive import validate_answer
from register_batches import Markup
folder=Path(__file__).parent
manifest=Path('legal-rewrite/coordinations/sru-quotas/manifest.json')
before_bytes=manifest.read_bytes(); before=json.loads(before_bytes)
a=next(x for x in before['articles'] if x['number']=='R3211-15' and x['code_id']=='LEGITEXT000006070299')
sha=lambda s:hashlib.sha256(s.encode() if isinstance(s,str) else s).hexdigest()
assert sha(a['proposed_xml'])==a['proposed_sha256']=='2f76c79c37803af249deac0fcd5f9430b13109253076e175e63463903f2e57fe'
assert sha(a['source_xml'])==a['source_sha256']=='c220156c73003b2687fc8100c5eb5acd8b7128318245b75788feb9475c04b305'
archive=Path('/private/tmp/legi-updates')/a['archive']
with archive.open('rb') as f: archive_sha=hashlib.file_digest(f,'sha256').hexdigest()
assert archive_sha==a['provenance']['archive_sha256']
with tarfile.open(archive,'r:gz') as tf: raw=tf.extractfile(a['provenance']['article_member']).read()
assert sha(raw)==a['source_article_raw_sha256']
root=ET.fromstring(raw)
def inner(node):
 return (node.text or '')+''.join(ET.tostring(c,encoding='unicode') for c in node)
body=inner(root.find('./BLOC_TEXTUEL/CONTENU'))
notes=inner(root.find('./NOTA/CONTENU'))
assert body==a['source_xml']
assert notes==a['source_notes_xml']==''
expected=copy.deepcopy(a)
expected.update({'source_document_xml':raw.decode(),'source_document_sha256':sha(raw),'current_beforeimage':copy.deepcopy(a),'current_beforeimage_sha256':sha(a['proposed_xml']),'current_manifest_path':str(manifest),'current_manifest_sha256':sha(before_bytes)})
candidate=copy.deepcopy(a)
old='<p>3° Abrogé ;</p>'
new='<p>3° La contribution du programme de logements à la réalisation de logements sociaux au sens du IV de l’article L. 302-5 du code de la construction et de l’habitation, sans condition tenant à un quota communal, à un objectif de rattrapage ou à un constat de carence ;</p>'
assert candidate['proposed_xml'].count(old)==1
candidate['proposed_xml']=candidate['proposed_xml'].replace(old,new)
old_transition='VII. – La suppression du critère du 3° du III s’applique'
new_transition='VII. – La nouvelle rédaction du 3° du III s’applique'
assert candidate['proposed_xml'].count(old_transition)==1
candidate['proposed_xml']=candidate['proposed_xml'].replace(old_transition,new_transition)
candidate['proposed_sha256']=sha(candidate['proposed_xml'])
candidate['reason']='Préserver le facteur favorable de décote du III 3° en le rattachant directement à la réalisation de logements sociaux, sans quota, rattrapage ni carence. Les catégories, fourchettes, taux et autres critères de la décote demeurent inchangés.'
candidate['review_notes']='Source officielle entière I à VI, tableau complet et note DILA vide lus ; proposition courante entière I à VII relue et avant-image capturée. Le III indique que la décote est d’autant plus élevée que les critères sont satisfaits : supprimer son 3° pouvait donc réduire un avantage. Le critère devient autonome et vise uniquement la définition des logements sociaux conservée au IV du L302-5 proposé, sans reprendre les obligations communales abrogées des anciens I/II. Il peut désormais être retenu dans toute commune, même sans ancien objectif SRU : cette ouverture favorable est explicite, sans nouvelle liste, inventaire, collecte ou justificatif spécifique. Aucune décote maximale automatique ni nouvelle catégorie éligible n’est créée ; l’équilibre financier, les autres circonstances locales et les plafonds continuent de s’appliquer. Les cinq autres subdivisions et les autres critères du III sont repris intégralement, ainsi que les quatre lignes et seize cellules du tableau ; seule la première phrase du VII est coordonnée, pour les décisions prises à compter de l’entrée en vigueur et sans remise en cause automatique des cessions antérieures. Texte compagnon hors compteur des 30 317 ; aucune registration ni publication dans ce paquet.'
candidate['change_type']='normative_coordination'
candidate.pop('removed_provisions',None)
validate_answer([candidate],[expected])
parser=Markup();parser.feed(candidate['proposed_xml']);parser.result()
src_parser=Markup(False);src_parser.feed(a['source_xml']);src_parser.result()
assert (parser.tables,parser.rows,parser.cells)==(src_parser.tables,src_parser.rows,src_parser.cells)==(1,4,16)
prior_paras=re.findall(r'<p>.*?</p>',a['proposed_xml'],re.S)
new_paras=re.findall(r'<p>.*?</p>',candidate['proposed_xml'],re.S)
changes=[{'paragraph':i+1,'before':x,'after':y} for i,(x,y) in enumerate(zip(prior_paras,new_paras)) if x!=y]
assert len(prior_paras)==len(new_paras) and len(changes)==2
assert candidate['proposed_xml'].replace(new,old).replace(new_transition,old_transition)==a['proposed_xml']
assert '3° Abrogé' not in candidate['proposed_xml']
assert manifest.read_bytes()==before_bytes
checks={'validate_answer':'passed','article':'R3211-15','source_body_sha256':sha(body),'source_raw_article_sha256':sha(raw),'source_archive_sha256':archive_sha,'source_notes_empty_verified':True,'current_beforeimage_sha256':sha(a['proposed_xml']),'proposed_sha256':candidate['proposed_sha256'],'active_manifest_path':str(manifest),'active_manifest_sha256':sha(before_bytes),'active_manifest_unchanged':True,'source_tables':src_parser.tables,'proposed_tables':parser.tables,'rows':parser.rows,'cells':parser.cells,'complete_paragraphs':len(new_paras),'only_two_paragraphs_changed':True,'changes':changes,'registered':False,'published':False,'excluded_from_30317_counter':True}
notes={'finding':'Le III 3° actuel est un facteur de hausse du montant de décote, et non une obligation de construire ou un seuil d’accès. Sa suppression dans notre brouillon pouvait affaiblir une aide foncière.','decision':'Restaurer le facteur favorable sur un fondement autonome, compatible avec la suppression des quotas et la priorité au maintien des avantages.','scope_extension':'Le critère peut désormais bénéficier à des programmes dans une commune sans objectifs SRU : ouverture favorable explicite. Aucune garantie de décote maximale et aucun nouveau plafond.','source_primary_online_checked':'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038929095','online_source_version':'Version en vigueur depuis le 1er septembre 2019, consultée le 19 octobre 2026 ; texte I à VI et tableau concordants avec le XML archivé.','source_validation':'SHA du corps distinct de celui du document XML DILA intégral ; archive, membre exact et note vide vérifiés.','dependency':'Le IV de L302-5 est conservé dans le projet comme définition autonome des logements sociaux ; le renvoi ne ressuscite ni les anciens I/II ni les quotas.','transition':'Nouvelle rédaction applicable aux décisions de décote prises à compter de l’entrée en vigueur ; cessions et conventions antérieures, droits des tiers et obligations indépendantes préservés ; aucun remboursement ou droit général à révision créé.','minimal_diff':'III 3° et seule première phrase du VII. Le reste du texte courant demeure identique octet pour octet, y compris tableau et catégories.','integration':'Parent uniquement : remplacer cette seule entrée de coordinations/sru-quotas/manifest.json après vérification du SHA de l’avant-image. Pas de mutation DB ni batch, pas d’activation automatique.','legal_review':'Contrôle technique et cohérence interne ; ne vaut pas validation juridique exhaustive.'}
for name,data in [('expected.json',[expected]),('answer.json',[candidate]),('validation.json',checks),('notes.json',notes),('guards.json',[{k:expected[k] for k in ['code_id','source_id','number','source_sha256','current_beforeimage_sha256','current_manifest_path','current_manifest_sha256']}])]:
 (folder/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(folder/'source-document.xml').write_bytes(raw)
(folder/'proposed-article.xml').write_text(candidate['proposed_xml']+'\n')
print(json.dumps({k:v for k,v in checks.items() if k!='changes'},ensure_ascii=False,indent=2))
