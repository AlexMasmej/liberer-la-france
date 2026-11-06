#!/usr/bin/env python3
"""Build the bilingual arXiv source (English first, then French) from en/ and fr/.

arXiv accepts one submission per work; translations go in the same submission,
English first (https://info.arxiv.org/help/faq/multilang.html). en/main.tex and
fr/main.tex stay the sources of truth; this script writes bilingual/main.tex.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
en = (ROOT / "en" / "main.tex").read_text()
fr = (ROOT / "fr" / "main.tex").read_text()


def split(doc):
    head, body = doc.split("\\begin{document}\n", 1)
    body = body.rsplit("\\end{document}", 1)[0]
    return head, body


en_head, en_body = split(en)
fr_head, fr_body = split(fr)

# Preamble: the English one, with both languages loaded (English as main) and
# hyperref anchors that stay unique when counters restart for the French part.
head = en_head.replace("\\usepackage[english]{babel}", "\\usepackage[french,english]{babel}")
head = head.replace("\\usepackage[hidelinks]{hyperref}", "\\usepackage[hidelinks,hypertexnames=false]{hyperref}")
assert "[french,english]{babel}" in head and "hypertexnames=false" in head

# English part: announce the French version under the title.
en_note = (
    "\\maketitle\n\n"
    "\\begin{center}\\small\\emph{A French version of this paper follows, "
    "from page~\\pageref{fr:start}.}\\end{center}\n"
)
assert en_body.count("\\maketitle\n") == 1
en_body = en_body.replace("\\maketitle\n", en_note, 1)

# French part: prefix labels, references and citation keys so they do not
# collide with the English ones.
fr_body = re.sub(r"\\(label|ref|pageref|eqref)\{([^}]*)\}", r"\\\1{fr:\2}", fr_body)
fr_body = re.sub(
    r"\\cite\{([^}]*)\}",
    lambda m: "\\cite{" + ",".join("fr:" + k.strip() for k in m.group(1).split(",")) + "}",
    fr_body,
)
fr_body = re.sub(r"\\bibitem\{([^}]*)\}", r"\\bibitem{fr:\1}", fr_body)

# French title block, built by hand: article's \maketitle can only run once.
title = re.search(r"\\title\{(.*?)\}\n\n\\author", fr_head, re.S).group(1)
date = re.search(r"\\date\{(.*?)\}", fr_head).group(1)
fr_title = (
    "\\clearpage\n"
    "\\selectlanguage{french}\n"
    "\\label{fr:start}\n"
    "\\setcounter{section}{0}\\setcounter{figure}{0}\\setcounter{table}{0}"
    "\\setcounter{footnote}{0}\\setcounter{equation}{0}\n"
    "\\begin{center}\n"
    "{\\LARGE " + title + "\\par}\n"
    "\\vskip 1.5em\n"
    "{\\large\n"
    "\\begin{tabular}[t]{c}Alexandre Masmejean\\\\ \\small Indépendant\\end{tabular}\\hskip 1em\n"
    "\\begin{tabular}[t]{c}Nathalie Gouailhardou\\\\ \\small Indépendante\\end{tabular}\\hskip 1em\n"
    "\\begin{tabular}[t]{c}Kevin Primicerio\\\\ \\small Indépendant\\end{tabular}\\par}\n"
    "\\vskip 1em\n"
    "{\\large " + date + "\\par}\n"
    "\\vskip 0.5em\n"
    "{\\small\\emph{Version française de l'article qui précède.}\\par}\n"
    "\\end{center}\n"
    "\\vskip 1em\n"
)
assert fr_body.count("\\maketitle\n") == 1
fr_body = fr_body.replace("\\maketitle\n", fr_title, 1)

out = head + "\\begin{document}\n" + en_body + fr_body + "\\end{document}\n"
dest = ROOT / "bilingual"
dest.mkdir(exist_ok=True)
(dest / "main.tex").write_text(out)
print(f"wrote {dest / 'main.tex'} ({len(out.splitlines())} lines)")
