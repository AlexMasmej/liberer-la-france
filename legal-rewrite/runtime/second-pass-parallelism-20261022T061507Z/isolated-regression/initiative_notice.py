"""Visible independence notice required by the Nouvelle Énergie initiative guide.

Presentation metadata stays outside the articles and their source payloads.
Source: https://adherent.unenouvelleenergie.fr/initiatives/guide
"""
from pathlib import Path
import re

NOTICE = ('Initiative indépendante de soutiens. Ce site ne dépend ni de '
          'Nouvelle Énergie ni de David Lisnard.')
MARKER = 'data-initiative-independence="true"'
FRAGMENT = ('<p '+MARKER+' class="initiative-independence" role="note" '
            'style="margin:18px 0 0;padding:12px 14px;border-top:1px solid #193b3238;'
            'background:#f4f0e7;color:#193b32;font:12px/1.6 Arial,sans-serif">'
            +NOTICE+'</p>')


def annotate(document):
    """Add one visible notice without changing any existing article markup."""
    if MARKER in document:
        return document
    footers=list(re.finditer(r'</footer\s*>',document,re.I))
    if footers:
        position=footers[-1].start()
        return document[:position]+FRAGMENT+document[position:]
    ending=re.search(r'</(?:body|html)\s*>',document,re.I)
    position=ending.start() if ending else len(document)
    return document[:position]+'<footer>'+FRAGMENT+'</footer>'+document[position:]


def apply_to_sites(roots):
    updated=[]
    for root in roots:
        for path in sorted(Path(root).rglob('*.html')):
            if '.vercel' in path.parts:
                continue
            original=path.read_text()
            result=annotate(original)
            if result!=original:
                path.write_text(result)
                updated.append(str(path))
    return updated
