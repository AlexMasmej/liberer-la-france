from pathlib import Path
import json,re,gzip,tarfile,hashlib,xml.etree.ElementTree as ET

HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
source=json.loads((HERE/'outside-sources.json').read_text())
records={(x['code_id'],x['source_id']):x for x in source['current_candidates']}
codes={'LEGITEXT000006070633':'CGCT','LEGITEXT000006070299':'CG3P','LEGITEXT000044595989':'CIBS'}
DATE='2026-10-18'
pattern=re.compile(rb'L\.?\s*302\s*-\s*[5-9]')
manifest=json.loads((BASE/'archive-manifest.json').read_text())
for item in manifest:
    if item['name'].startswith('Freemium'):continue
    path=Path('/private/tmp/legi-updates')/item['name']
    with gzip.open(path,'rb')as gz:
        with tarfile.open(fileobj=gz,mode='r|')as archive:
            for member in archive:
                if not member.isfile()or not member.name.endswith('.xml'):continue
                code=next((p for p in member.name.split('/')if p in codes),None)
                if not code:continue
                raw=archive.extractfile(member).read();node=ET.fromstring(raw)
                if node.tag!='ARTICLE':continue
                identifier=node.findtext('META/META_COMMUN/ID');key=(code,identifier);meta='META/META_SPEC/META_ARTICLE/'
                start=node.findtext(meta+'DATE_DEBUT');end=node.findtext(meta+'DATE_FIN');number=node.findtext(meta+'NUM')
                selected=bool(pattern.search(raw))or key in records or number in('L2334-17','L4424-26-5','L221-66','L221-67')
                if not selected:continue
                if not(start and end and start<=DATE<end):records.pop(key,None);continue
                content=node.find('BLOC_TEXTUEL/CONTENU');body=(content.text or '')+''.join(ET.tostring(child,encoding='unicode')for child in content)if content is not None else ''
                records[key]={'code_id':code,'code':codes[code],'source_id':identifier,'number':number,'valid_from':start,'valid_until':end,'source_sha256':hashlib.sha256(raw).hexdigest(),'source_xml':body,'whole_article_xml':raw.decode(),'archive':item['name'],'archive_source_url':item.get('url')or item.get('source_url'),'source_url':'https://www.legifrance.gouv.fr/codes/article_lc/'+identifier}
        while gz.read(1024*1024):pass

result=source|{'as_of':DATE,'current_candidates':[x for x in records.values()if x['valid_from']<=DATE<x['valid_until']],'consolidation':'Official stock plus all466daily updates replayed by articleID; explicit removal when a revised version expires. No additional database import.','archives_scanned':len(manifest)}
(HERE/'outside-sources-consolidated.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('CONSOLIDATED',len(result['current_candidates']),'articles through',DATE)
