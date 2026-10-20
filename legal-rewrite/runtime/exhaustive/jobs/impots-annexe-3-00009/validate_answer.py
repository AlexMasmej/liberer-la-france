import json
import re
from collections import Counter
from html import unescape
from pathlib import Path
from xml.etree import ElementTree as ET


sources = json.loads(Path("source.json").read_text())
answers = json.loads(Path("answer.json").read_text())
fields = {"code_id", "source_id", "source_sha256", "number", "proposed_xml", "reason", "review_notes", "status"}
tags = {"p", "br", "table", "thead", "tbody", "tfoot", "tr", "th", "td", "b", "strong", "i", "em", "u", "sup", "sub", "ul", "ol", "li", "div", "span", "blockquote"}
assert len(sources) == len(answers) == 24
assert len({a["source_id"] for a in answers}) == 24


def plain(xml):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", xml))).strip()


for source, answer in zip(sources, answers):
    assert set(answer) == fields
    for key in ("code_id", "source_id", "source_sha256", "number"):
        assert source[key] == answer[key]
    assert answer["status"] == "rewrite_draft"
    assert all(isinstance(answer[k], str) and answer[k].strip() for k in ("proposed_xml", "reason", "review_notes"))
    tree = ET.fromstring("<root>" + answer["proposed_xml"] + "</root>")
    for element in tree.iter():
        if element.tag == "root":
            continue
        assert element.tag in tags
        assert all(k in {"rowspan", "colspan"} and re.fullmatch(r"[0-9]+", v) for k, v in element.attrib.items())
    before, after = plain(source["source_xml"]), plain(answer["proposed_xml"])
    assert before != after
    assert not re.search(r"texte inchangé|à réécrire|TODO|\.\.\.|…", after, re.I)
    before_nums = Counter(re.findall(r"\d+(?:[ -]\d+)*", before))
    after_nums = Counter(re.findall(r"\d+(?:[ -]\d+)*", after))
    before_ps = len(re.findall(r"<p\b", source["source_xml"]))
    after_ps = len(re.findall(r"<p\b", answer["proposed_xml"]))
    before_markers = re.findall(r"(?:^|>)\s*((?:[IVX]+|[1-9]\d*)\s*[.°]|[a-z][.)])", source["source_xml"])
    after_markers = re.findall(r"(?:^|>)\s*((?:[IVX]+|[1-9]\d*)\s*[.°]|[a-z][.)])", answer["proposed_xml"])
    assert all(after_markers.count(m) >= before_markers.count(m) for m in before_markers), (answer["number"], before_markers, after_markers)
    assert Counter(re.findall(r"<(?:table|tr|td|th)\b", source["source_xml"])) == Counter(re.findall(r"<(?:table|tr|td|th)\b", answer["proposed_xml"]))
    print(answer["number"], f"paragraphes {before_ps}->{after_ps}", f"caractères {len(before)}->{len(after)}")
    if before_nums != after_nums:
        print("  Occurrences numériques retirées :", dict(before_nums - after_nums))
        print("  Occurrences numériques ajoutées :", dict(after_nums - before_nums))

print("VALIDATION STRUCTURELLE RÉUSSIE : 24 articles complets, identifiants conformes, XML autorisé, subdivisions et tableaux contrôlés.")
