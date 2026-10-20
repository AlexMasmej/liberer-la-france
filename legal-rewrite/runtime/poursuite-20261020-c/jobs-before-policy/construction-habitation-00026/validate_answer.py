import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from html import unescape
from pathlib import Path


sources = json.loads(Path("source.json").read_text())
answers = json.loads(Path("answer.json").read_text())
fields = set("code_id source_id source_sha256 number proposed_xml reason review_notes status".split())
identifiers = ("code_id", "source_id", "source_sha256", "number")
allowed = set("p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote".split())
assert len(sources) == len(answers) == 24
assert len({answer["source_id"] for answer in answers}) == 24
number_words = r"\b(?:deux|trois|quatre|cinq|six|huit|neuf|dix|dix-huit|soixante|soixante-cinq|quinze|vingt|cent|mille|millions|second|premier|deuxième|troisième|avant-dernier)\b"
for source, answer in zip(sources, answers):
    assert set(answer) == fields, source["number"]
    assert all(answer[key] == source[key] for key in identifiers), source["number"]
    assert answer["status"] == "rewrite_draft"
    assert all(isinstance(answer[key], str) and answer[key].strip() for key in ("proposed_xml", "reason", "review_notes"))
    xml = answer["proposed_xml"]
    root = ET.fromstring("<root>" + xml + "</root>")
    for node in root.iter():
        if node is root:
            continue
        assert node.tag in allowed, (source["number"], node.tag)
        assert all(key in ("colspan", "rowspan") and re.fullmatch(r"[0-9]+", value) for key, value in node.attrib.items())
    assert not re.search(r"texte inchangé|à compléter|\[\.\.\.\]|résumé|TODO", xml, re.I)
    original = unescape(re.sub(r"<[^>]*>", " ", source["source_xml"]))
    proposed = " ".join(root.itertext())
    assert re.sub(r"\s+", " ", original).strip() != re.sub(r"\s+", " ", proposed).strip()
    assert Counter(re.findall(r"\d+(?:[.,]\d+)?", original)) == Counter(re.findall(r"\d+(?:[.,]\d+)?", proposed)), source["number"]
    assert Counter(re.findall(number_words, original)) == Counter(re.findall(number_words, proposed)), source["number"]
    assert source["source_xml"].lower().count("<table") == xml.lower().count("<table"), source["number"]
    original_paragraphs = re.findall(r"<p\b[^>]*>(.*?)</p>", source["source_xml"], re.S)
    if original_paragraphs:
        substantive = [p for p in original_paragraphs if re.sub(r"<[^>]*>", "", p).strip()]
        assert len(substantive) == len(root.findall("p")), source["number"]
print("Validation réussie : 24 articles, identifiants exacts, XML conforme, nombres et alinéas conservés, aucun tableau omis.")
