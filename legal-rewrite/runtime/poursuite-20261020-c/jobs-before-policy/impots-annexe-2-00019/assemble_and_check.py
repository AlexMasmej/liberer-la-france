import collections
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
source_path = ROOT / "source.json"
source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
sources = json.loads(source_path.read_text())
notes = json.loads((ROOT / "editorial_notes.json").read_text())
assert len(sources) == len(notes) == 24

identifier_fields = ("code_id", "source_id", "source_sha256", "number")
expected_fields = set(identifier_fields) | {
    "proposed_xml", "reason", "review_notes", "status"
}
allowed_tags = {
    "p", "br", "table", "thead", "tbody", "tfoot", "tr", "th", "td", "b",
    "strong", "i", "em", "u", "sup", "sub", "ul", "ol", "li", "div",
    "span", "blockquote"
}


def text_content(xml):
    return html.unescape(re.sub(r"<[^>]+>", " ", xml))


def numeric_tokens(xml):
    # Separate enumeration commas, notably the source's "articles 3,5".
    return collections.Counter(re.findall(r"\d+(?:-\d+)*", text_content(xml)))


def labels(xml):
    found = re.findall(
        r"(?:^|[>\n])\s*([IVX]+\.\s*[–-]\s*\d+°|[IVX]+\.\s*[–-]|\d+°|\d+\.|[a-z]\))",
        xml,
    )
    return [re.sub(r"\s+", "", value).replace("–", "-") for value in found]


def normalized_text(xml):
    return " ".join(text_content(xml).split())


answer = []
audit = []
for index, (source, note) in enumerate(zip(sources, notes)):
    if index in (10, 16):
        fragment_paths = [ROOT / "fragments" / f"{index:02d}{part}.xml" for part in ("a", "b")]
    else:
        fragment_paths = [ROOT / "fragments" / f"{index:02d}.xml"]
    proposed = "".join(path.read_text() for path in fragment_paths).strip()
    assert proposed and normalized_text(proposed) != normalized_text(source["source_xml"])
    tree = ET.fromstring("<root>" + proposed + "</root>")
    for element in tree.iter():
        if element.tag == "root":
            continue
        assert element.tag in allowed_tags, (source["number"], element.tag)
        for key, value in element.attrib.items():
            assert key in {"rowspan", "colspan"} and re.fullmatch(r"\d+", value)
    assert labels(source["source_xml"]) == labels(proposed), source["number"]
    source_numbers, proposed_numbers = numeric_tokens(source["source_xml"]), numeric_tokens(proposed)
    assert not (source_numbers - proposed_numbers), (source["number"], source_numbers - proposed_numbers)
    # One anaphoric reference in 294 quater is made explicit as "article 787 C".
    expected_extra = collections.Counter({"787": 1}) if index == 18 else collections.Counter()
    assert proposed_numbers - source_numbers == expected_extra, source["number"]
    source_tables = len(re.findall(r"<table(?:\s|>)", source["source_xml"]))
    proposed_tables = len(list(tree.iter("table")))
    assert source_tables == proposed_tables, source["number"]
    assert note["reason"].strip() and note["review_notes"].strip()
    item = {field: source[field] for field in identifier_fields}
    item.update(
        proposed_xml=proposed,
        reason=note["reason"],
        review_notes=note["review_notes"],
        status="rewrite_draft",
    )
    assert set(item) == expected_fields
    answer.append(item)
    audit.append({
        "number": source["number"],
        "source_characters": len(source["source_xml"]),
        "proposed_characters": len(proposed),
        "source_p_elements": source["source_xml"].count("<p>"),
        "proposed_p_elements": proposed.count("<p>"),
        "tables": proposed_tables,
    })

assert len({item["source_id"] for item in answer}) == 24
output_path = ROOT / "answer.json"
output_path.write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
roundtrip = json.loads(output_path.read_text())
assert roundtrip == answer
assert hashlib.sha256(source_path.read_bytes()).hexdigest() == source_digest
for source, item in zip(sources, roundtrip):
    assert all(item[field] == source[field] for field in identifier_fields)

print(json.dumps({
    "output_file": output_path.name,
    "article_count": len(roundtrip),
    "status_counts": dict(collections.Counter(item["status"] for item in roundtrip)),
    "total_proposed_characters": sum(len(item["proposed_xml"]) for item in roundtrip),
    "source_file_unchanged_during_assembly": True,
    "audit": audit,
}, ensure_ascii=False, indent=2))
