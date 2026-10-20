from pathlib import Path
import tarfile,gzip,json,re,xml.etree.ElementTree as ET,hashlib

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
TARGETS={'LEGITEXT000006070633':'CGCT','LEGITEXT000006070299':'CG3P','LEGITEXT000044595989':'CIBS'}
DATE='2026-10-19'
pattern=re.compile(rb'L\.?\s*302\s*-\s*[5-9]')
manifest=json.loads((BASE/'archive-manifest.json').read_text())
records={};done=[]
for index,item in enumerate(manifest):
    path=Path('/private/tmp/legi-global-20250713.tar.gz')if item['name'].startswith('Freemium')else Path('/private/tmp/legi-updates')/item['name']
    if not path.exists():raise FileNotFoundError(path)
    with gzip.open(path,'rb')as gz:
        with tarfile.open(fileobj=gz,mode='r|')as archive:
            for member in archive:
                if not member.isfile()or not member.name.endswith('.xml'):continue
                code=next((p for p in member.name.split('/')if p in TARGETS),None)
                if not code:continue
                raw=archive.extractfile(member).read()
                if not pattern.search(raw)and not any(n.encode() in raw for n in ['L2334-17','L4424-26-5','L221-66']):continue
                node=ET.fromstring(raw)
                if node.tag!='ARTICLE':continue
                identifier=node.findtext('META/META_COMMUN/ID');meta='META/META_SPEC/META_ARTICLE/'
                start=node.findtext(meta+'DATE_DEBUT');end=node.findtext(meta+'DATE_FIN')
                if not(start and end and start<=DATE<end):continue
                content=node.find('BLOC_TEXTUEL/CONTENU')
                body=(content.text or '')+''.join(ET.tostring(child,encoding='unicode')for child in content)if content is not None else ''
                number=node.findtext(meta+'NUM')
                key=(code,identifier)
                records[key]={'code_id':code,'code':TARGETS[code],'source_id':identifier,'number':number,'valid_from':start,'valid_until':end,'source_sha256':hashlib.sha256(raw).hexdigest(),'source_xml':body,'whole_article_xml':raw.decode(),'archive':item['name'],'archive_source_url':item.get('url')or item.get('source_url'),'source_url':'https://www.legifrance.gouv.fr/codes/article_lc/'+identifier}
        while gz.read(1024*1024):pass
    done.append(item['name'])
    if index%50==0:print('scanned',index+1,'archives;',len(records),'selected records',flush=True)

result={'as_of':DATE,'archives_scanned':len(done),'current_candidates':list(records.values()),'scope':'Only selected outside-code articles; not an import or complete code rewrite.'}
(HERE/'outside-sources.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('COMPLETE',len(records),'current candidate articles',flush=True)
