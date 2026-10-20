import json,re,sys,xml.etree.ElementTree as E
s=json.load(open('source.json')); a=json.load(open('answer.json'))
def pars(x):
 r=E.fromstring('<div>'+x+'</div>')
 if r.findall('p'): return [' '.join(''.join(p.itertext()).split()) for p in r.findall('p')]
 return [re.sub(r'\s+',' ',p).strip() for p in re.split(r'<br\s*/?>',x) if re.sub(r'\s+',' ',p).strip()]
lo,hi=map(int,sys.argv[1:])
for src,out in zip(s[lo:hi],a[lo:hi]):
 print('\nARTICLE',src['number'])
 for i,(p,q) in enumerate(zip(pars(src['source_xml']),pars(out['proposed_xml'])),1):
  print(i,'SOURCE :',p)
  print('PROPOSITION :',q)
 for ts,to in zip(E.fromstring('<div>'+src['source_xml']+'</div>').findall('table'),E.fromstring('<div>'+out['proposed_xml']+'</div>').findall('table')):
  print('TABLEAU SOURCE / PROPOSITION :')
  for j,(rs,ro) in enumerate(zip(ts.findall('.//tr'),to.findall('.//tr')),1):
   f=lambda r:[' '.join(''.join(c.itertext()).split()) for c in r]
   print(j,'SOURCE :',f(rs),'PROPOSITION :',f(ro))
 print('NOTE SOURCE :',repr(src['source_notes_xml']))
