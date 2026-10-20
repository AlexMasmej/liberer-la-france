import json
from pathlib import Path
sources = json.loads(Path('source.json').read_text())
drafts = []
for part in range(1, 4):
    drafts.extend(json.loads(Path(f'drafts/part-{part}.json').read_text()))
assert len(sources) == len(drafts) == 24
assert [a['number'] for a in sources] == [a['number'] for a in drafts]
for d in drafts:
    if d['number'] == 'L123-25':
        d['proposed_xml'] = d['proposed_xml'].replace('Celle-ci comprend les communes', 'La petite région agricole de ce plateau comprend les communes')
    if d['number'] == 'L123-24-1':
        d['proposed_xml'] = d['proposed_xml'].replace("dans le mois suivant leur saisine", "dans un délai d'un mois à compter de leur saisine")
    if d['number'] == 'L123-24-2':
        d['proposed_xml'] = d['proposed_xml'].replace("Dans le mois suivant cette notification", "Dans un délai d'un mois à compter de cette notification")
    if d['number'] == 'L131-3':
        d['proposed_xml'] = d['proposed_xml'].replace("Cette délibération intervient au plus tard trois ans après l'entrée en vigueur", "Cette délibération intervient dans un délai maximal de trois ans à compter soit de l'entrée en vigueur").replace("ou après la délibération maintenant ce schéma", "soit de la délibération maintenant ce schéma")
    if d['number'] == 'L131-7':
        d['proposed_xml'] = d['proposed_xml'].replace("Il délibère sur le maintien", "L'autorité compétente délibère sur le maintien")
        d['proposed_xml'] = d['proposed_xml'].replace("La délibération prévue au premier alinéa intervient au plus tard trois ans après l'entrée en vigueur", "La délibération prévue au premier alinéa intervient dans un délai maximal de trois ans à compter soit de l'entrée en vigueur").replace("ou après la délibération maintenant ce document", "soit de la délibération maintenant ce document")
        d['proposed_xml'] = d['proposed_xml'].replace("elle intervient au plus tard un an après l'entrée en vigueur", "elle intervient dans un délai maximal d'un an à compter soit de l'entrée en vigueur").replace("ou après la délibération le maintenant", "soit de la délibération le maintenant")
    if d['number'] == 'L131-8':
        d['proposed_xml'] = d['proposed_xml'].replace("Il délibère sur le maintien", "L'autorité compétente délibère sur le maintien")
        d['proposed_xml'] = d['proposed_xml'].replace("Cette délibération intervient au plus tard trois ans après l'entrée en vigueur", "Cette délibération intervient dans un délai maximal de trois ans à compter soit de l'entrée en vigueur").replace("ou après la délibération le maintenant", "soit de la délibération le maintenant")
answer = []
for src, draft in zip(sources, drafts):
    row = {key: src[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update({key: draft[key] for key in ('proposed_xml', 'reason', 'review_notes')})
    row['status'] = 'rewrite_draft'
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
