# arXiv submission package

arXiv accepts one submission per work and asks for translations to be included in the same submission, English first (https://info.arxiv.org/help/faq/multilang.html). The package is therefore a single bilingual paper.

| File | Content |
|---|---|
| `arxiv.tar.gz` | LaTeX source to upload: `bilingual/main.tex`, English (pp. 1--21) then French (pp. 22--43); bibliography inline, no figures to attach |
| `source-code-of-law-bilingual.pdf` | Compiled preview of the bilingual submission (43 pages) |
| `source-code-of-law-en.pdf`, `code-source-du-droit-fr.pdf` | English and French versions on their own, for reading |
| `en/main.tex`, `fr/main.tex` | Sources of truth; `python3 build_bilingual.py` regenerates `bilingual/main.tex` from them |
| `en/abstract.txt` | Plain-text abstract for the arXiv form (English; 1,571 characters, limit 1,920) |
| `fr/abstract.txt` | French abstract, for reference |

Suggested metadata:
- Title (EN): The Source Code of Law: AI Agents Rewrite and Red-Team 30,000 Articles of French Law
- Title (FR, inside the PDF only; the arXiv title field is the English one): Le code source du droit : des agents d'IA réécrivent et passent au red-teaming 30 000 articles du droit français
- Authors: Alexandre Masmejean, Nathalie Gouailhardou, Kevin Primicerio (all independent; every author must approve the final manuscript and the contribution statement before submission)
- Primary category: cs.CY (Computers and Society); cross-lists: cs.AI, cs.CL, econ.GN (General Economics)
- Comments: Bilingual: English version (21 pages) followed by the French version (22 pages). 2 figures, 10 tables in each. Code and data: https://github.com/AlexMasmej/liberer-la-france
- License: CC BY 4.0 (suggested)

Sources compile with pdflatex (TeX Live) and were checked with tectonic. After any change to `en/main.tex` or `fr/main.tex`, rerun `build_bilingual.py`, recompile, and rebuild `arxiv.tar.gz`.
