import json
from pathlib import Path
sources=json.loads(Path('source.json').read_text())
metadata={}
for batch in range(1,4):
    metadata.update(json.loads(Path(f'metadata_{batch}.json').read_text()))
answer=[]
for i,a in enumerate(sources):
    row={k:a[k] for k in ['code_id','source_id','source_sha256','number']}
    row['proposed_xml']=Path(f'fragments/{i:02d}.xml').read_text().strip()
    row.update(metadata[str(i)])
    row['status']='rewrite_draft'
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
print('Articles assemblés :',len(answer))
