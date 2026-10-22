"""Check the exported reading flow, including offline formula companions."""
from pathlib import Path,PurePosixPath
from html.parser import HTMLParser
import hashlib,json,zipfile
from coordination_downloads import unique_records

PUBLIC=Path(__file__).resolve().parent.parent/'sites/liberer-la-retraite/dist'


class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if (tag,key) in {('img','src'),('a','href')} and value:self.links.append(value)


def check():
    root=PUBLIC/'downloads';manifest=json.loads((root/'manifest.json').read_text())
    coverage=json.loads((PUBLIC/'corpus/coverage.json').read_text())
    count=0;media=0;documents=0;coordination_records=[]
    for item in manifest['downloads']:
        path=root/item['filename']
        if hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Archive hash mismatch')
        with zipfile.ZipFile(path) as archive:
            damaged=archive.testzip()
            if damaged:raise ValueError('Damaged archive member: '+damaged)
            names=set(archive.namelist());sub=json.loads(archive.read('manifest.json'))
            n=0
            for code in sub['codes']:
                slug=code['slug'];records=json.loads(archive.read(slug+'/articles.json'))
                if len(records)!=code['source_records']:raise ValueError('Incomplete code data')
                drafted=sum(bool(a['proposed_xml']) for a in records)
                if drafted!=code['drafted_articles']:raise ValueError('Incorrect draft count')
                n+=drafted
                for name in [slug+'/texte-source-integral.html',slug+'/version-de-travail-integrale.html']:
                    p=Links();p.feed(archive.read(name).decode())
                    for link in p.links:
                        if link.startswith(('https://','http://','#','mailto:')):continue
                        target=str(PurePosixPath(name).parent/link)
                        if target not in names:raise ValueError('Broken offline link: '+target)
            if n!=item['drafted_articles']:raise ValueError('Incorrect package count')
            for related in sub.get('outside_code_inventory_coordinations',[]):
                content=archive.read(related['archive_html'])
                if content!=(root/related['filename']).read_bytes():raise ValueError('Coordination differs online and offline')
                if hashlib.sha256(content).hexdigest()!=related['sha256']:raise ValueError('Coordination hash mismatch')
                data=json.loads(archive.read(related['archive_json']))
                if data.get('outside_code_inventory') is not True:raise ValueError('Coordination misclassified as code article')
                if len(data['articles'])!=related['articles']:raise ValueError('Incorrect coordination article count')
                for article in data['articles']:
                    if hashlib.sha256(article['source_xml'].encode()).hexdigest()!=article['source_sha256']:raise ValueError('Coordination source mismatch')
                coordination_records.append(related)
            count+=n;media+=sum(n.endswith(('.png','.jpg','.webp')) for n in names);documents+=sum(n.endswith('.pdf') for n in names)
    if count!=manifest['drafted_articles']:raise ValueError('Incorrect global draft count')
    if count!=sum(c['drafted'] for c in coverage['codes']):raise ValueError('Reader and download snapshots differ')
    if manifest['source_records']!=sum(c['imported_versions'] for c in coverage['codes']):raise ValueError('Reader and download inventories differ')
    if manifest['exhaustive_rewriting_complete']:raise ValueError('This edition has not passed a complete release audit')
    unique_coordinations=unique_records(coordination_records)
    if unique_coordinations!=manifest.get('outside_code_inventory_coordinations',[]):raise ValueError('Incorrect global coordination inventory')
    impact=manifest.get('substantive_impact_report')
    if impact:
        with zipfile.ZipFile(root/manifest['all']['filename']) as common:
            payload=common.read(impact['filename'])
            if hashlib.sha256(payload).hexdigest()!=impact['sha256'] or len(payload)!=impact['bytes']:raise ValueError('Impact report archive hash mismatch')
            if payload!=(PUBLIC/'corpus/substantive-impact.json').read_bytes():raise ValueError('Impact report differs online and offline')
            report=json.loads(payload)
            if report['coverage']['exported_articles']!=manifest['source_records'] or report['coverage']['exported_proposals']!=count:raise ValueError('Impact report and code editions differ')
            if report['national_savings']['status']!='unknown' or report['net_global_reduction']['status']!='not_established':raise ValueError('Unsupported global savings claim')
            if report['aggregation']['amounts_summed'] or report['aggregation']['article_counts_are_savings']:raise ValueError('Article counts cannot establish net savings')
    result={'source_records':manifest['source_records'],'drafted_articles':count,'local_formula_images':media,'companion_pdfs':documents,'offline_links':'all present','archives':'hashes and CRC valid','exhaustive_rewriting_complete':False}
    result['legislative_coordination_articles_outside_code_inventory']=sum(r['articles'] for r in unique_coordinations)
    print(json.dumps(result,ensure_ascii=False,indent=2));return result


if __name__=='__main__':check()
