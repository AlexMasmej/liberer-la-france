"""Write isolated proposals and patches, never the canonical pipeline files."""
from pathlib import Path
import difflib, hashlib, json

FOLDER = Path(__file__).resolve().parent
LEGAL = FOLDER.parents[2]
changes = {
    'run_exhaustive.py': [
        ("from sru_context import contexts as sru_contexts, priority as sru_priority\n",
         "from sru_context import contexts as sru_contexts, priority as sru_priority\nfrom contrat_unique_priority import article_priority as cu_article_priority, priority as cu_priority, mixed_priority as cu_mixed_priority\n"),
        ("pending.sort(key=lambda a:not bool(a.get('sru_context')))",
         "pending.sort(key=lambda a:(cu_article_priority(a),not bool(a.get('sru_context'))))"),
        ("if chunk and (size+n>45000 or len(chunk)>=24):",
         "if chunk and (cu_article_priority(chunk[0])!=cu_article_priority(article) or size+n>45000 or len(chunk)>=24):"),
        ("jobs.sort(key=lambda j:(sru_priority(j),j[1],SLUGS.index(j[0])))",
         "jobs.sort(key=lambda j:(cu_priority(j),sru_priority(j),j[1],SLUGS.index(j[0])))"),
        ("scheduled=interleave_jobs(jobs,review_prior.build_jobs(sources))\n",
         "scheduled=interleave_jobs(jobs,review_prior.build_jobs(sources))\n        # Keep stable new/review interleaving within each contract-priority band.\n        scheduled.sort(key=cu_mixed_priority)\n"),
    ],
    'review_prior.py': [
        ("from sru_context import priority as sru_priority\n",
         "from sru_context import priority as sru_priority\nfrom contrat_unique_priority import article_priority as cu_article_priority, priority as cu_priority\n"),
        ("articles.sort(key=lambda a:not bool(a.get('sru_context')))",
         "articles.sort(key=lambda a:(cu_article_priority(a),not bool(a.get('sru_context'))))"),
        ("if chunk and (size+amount>45000 or len(chunk)>=12):",
         "if chunk and (cu_article_priority(chunk[0])!=cu_article_priority(article) or size+amount>45000 or len(chunk)>=12):"),
        ("key=sru_priority)", "key=lambda job:(cu_priority(job),sru_priority(job)))"),
    ],
}
guards = {}
for name, replacements in changes.items():
    original = (LEGAL/name).read_text()
    updated = original
    for before, after in replacements:
        if updated.count(before) != 1:
            raise ValueError('Expected one unchanged patch anchor: '+name+': '+before)
        updated = updated.replace(before, after)
    compile(updated, str(LEGAL/name), 'exec')
    (FOLDER/(name+'.base.txt')).write_text(original)
    (FOLDER/(name+'.proposed.txt')).write_text(updated)
    patch = ''.join(difflib.unified_diff(original.splitlines(True), updated.splitlines(True),
        fromfile='a/legal-rewrite/'+name, tofile='b/legal-rewrite/'+name))
    (FOLDER/(name+'.patch')).write_text(patch)
    guards[name] = {'canonical_sha256':hashlib.sha256(original.encode()).hexdigest(),
                    'proposed_sha256':hashlib.sha256(updated.encode()).hexdigest()}
helper = (FOLDER/'contrat_unique_priority.proposed.py.txt').read_text()
(FOLDER/'contrat_unique_priority.py.patch').write_text(''.join(difflib.unified_diff([], helper.splitlines(True),
    fromfile='/dev/null', tofile='b/legal-rewrite/contrat_unique_priority.py')))
(FOLDER/'pipeline-patch-guards.json').write_text(json.dumps(guards,indent=2)+'\n')
print(json.dumps(guards,indent=2))
