"""Preserve public static sites and add the source-first corpus entry point."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlsplit
import re,subprocess,json,hashlib

HERE=Path(__file__).resolve().parent
SITES=[
 ('embauche','https://libererlembauche.com','nouveaudroitdutravail','prj_zahNFYxGRdJXSMA8mbNwl4POToxM','travail'),
 ('revenu','https://libererlerevenu.com','liberer-le-revenu','prj_FY6QVdGPCjjfSnDG6j7Z1UL3yC6g','impots'),
 ('entreprise','https://libererlentreprise.com','liberer-lentreprise','prj_jWrUP6fckXn68VHV08S6NtVD0cPQ','impots'),
 ('logement','https://libererlelogement.com','liberer-le-logement','prj_t5M7thvfbgoLQpQkHp1GSnzPsqC3','urbanisme')]

class Assets(HTMLParser):
 def __init__(self):super().__init__();self.urls=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);u=''
  if tag in {'script','img'} or (tag=='link' and a.get('rel') in {'stylesheet','icon','apple-touch-icon'}):u=a.get('href',a.get('src',''))
  if tag=='a' and a.get('href','').endswith('.pdf'):u=a['href']
  if tag=='meta' and a.get('property') in {'og:image','og:image:secure_url'}:u=a.get('content','')
  if u and not u.startswith(('#','data:')):self.urls.add(u)

def fetch(url,path):
 path.parent.mkdir(parents=True,exist_ok=True)
 subprocess.run(['curl','-fsSL','--retry','1','--max-time','30',url,'-o',str(path)],check=True)

for slug,origin,project,identifier,code in SITES:
 root=HERE.parent/'sites'/project;dist=root/'dist';dist.mkdir(parents=True,exist_ok=True)
 source=dist/'index.original.html';fetch(origin,source);original=source.read_text()
 assets=Assets();assets.feed(original);pending=[urljoin(origin+'/',u) for u in assets.urls];done=set()
 allowed={urlsplit(origin).netloc,project+'.vercel.app'}
 while pending:
  url=pending.pop()
  if url in done:continue
  done.add(url);parsed=urlsplit(url)
  if parsed.scheme!='https' or parsed.netloc not in allowed:continue
  relative=parsed.path.lstrip('/')
  path=(dist/relative).resolve()
  if not path.is_relative_to(dist.resolve()) or not relative:raise ValueError('Invalid public asset path')
  fetch(url,path)
  if path.suffix=='.css':
   for u in re.findall(r'url\([\'\"]?([^\)\'\"]+)',path.read_text()):
    if not u.startswith('data:'):pending.append(urljoin(url,u))
 notice=f'''<aside class="rewrite-status" aria-label="État du chantier"><strong>Réécriture intégrale des textes officiels, avec l’IA</strong><p>Le texte court ci-dessous est l’avant-projet initial. Le chantier porte désormais sur les codes complets, article par article, avec la source officielle et chaque changement.</p><a href="https://libererlaretraite.com/corpus/?code={code}">Lire les textes et suivre la réécriture →</a></aside>'''
 edited=re.sub(r'<a\b[^>]*href="https://soutenir\.unenouvelleenergie\.fr/adhesion"[^>]*>.*?</a>','',original,flags=re.S)
 edited=edited.replace('</header>','</header>'+notice,1)
 style='''<style>.rewrite-status{box-sizing:border-box;max-width:1400px;margin:24px auto;padding:22px clamp(20px,5vw,70px);background:#e0e6d6;color:#173a32;font:16px/1.5 Arial,sans-serif;border-block:1px solid #173a3230}.rewrite-status p{max-width:900px;margin:9px 0}.rewrite-status a{color:inherit;text-decoration:underline}.rewrite-status strong{font-size:18px}</style>'''
 edited=edited.replace('</head>',style+'</head>')
 (dist/'index.html').write_text(edited)
 source.unlink()
 (root/'.vercel').mkdir(exist_ok=True)
 (root/'.vercel/project.json').write_text(json.dumps({'orgId':'team_m7zLS15LnoyaB6RyJ0zKsHYj','projectId':identifier,'projectName':project}))
 (dist/'.vercel').mkdir(exist_ok=True)
 (dist/'.vercel/project.json').write_text((root/'.vercel/project.json').read_text())
 (root/'source-provenance.json').write_text(json.dumps({'origin':origin,'source_html_sha256':hashlib.sha256(original.encode()).hexdigest(),'project_id':identifier,'change':'Link full-code reader; label initial summary; remove membership CTA'},indent=2))
 print('Prepared',slug,'with',len(done),'public assets',flush=True)
