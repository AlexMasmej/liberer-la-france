import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
source_bytes = (ROOT / "source.json").read_bytes()
sources = json.loads(source_bytes)
notes = json.loads((ROOT / "notes.json").read_text())
allowed_tags = set("p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote".split())
fields = {"code_id", "source_id", "source_sha256", "number", "proposed_xml", "reason", "review_notes", "status"}
identifiers = ("code_id", "source_id", "source_sha256", "number")


def plain(text):
    return unescape(re.sub(r"<[^>]+>", " ", text))


def numbers(text):
    return Counter(re.findall(r"\d+(?:[-.]\d+)*", plain(text)))


def references(text):
    return Counter(re.findall(r"\b[LRD]\.\s*\d+(?:-\d+)*", plain(text)))


def alinea_count(text):
    pieces = re.split(r"</p>|(?:<br\s*/?>\s*){2,}", text)
    return sum(bool(plain(part).strip()) for part in pieces)


assert len(sources) == 14
assert len(notes) == 14
answer = []
report = []
for source in sources:
    number = source["number"]
    proposed = (ROOT / "drafts" / f"{number}.xml").read_text().strip()
    parsed = ET.fromstring(f"<root>{proposed}</root>")
    for node in parsed.iter():
        if node.tag == "root":
            continue
        assert node.tag in allowed_tags, (number, node.tag)
        for key, value in node.attrib.items():
            assert key in {"rowspan", "colspan"} and re.fullmatch(r"\d+", value), (number, key, value)
    assert numbers(source["source_xml"]) == numbers(proposed), (number, "chiffres")
    assert references(source["source_xml"]) == references(proposed), (number, "renvois")
    assert alinea_count(source["source_xml"]) == alinea_count(proposed), (number, "alinéas matériels")
    assert source["source_xml"].count("<table") == proposed.count("<table"), (number, "tableaux")
    assert plain(proposed).strip() != plain(source["source_xml"]).strip(), (number, "absence de réécriture")
    assert not any(marker in proposed for marker in ("```", "http://", "https://", "texte inchangé", "<br />+"))
    row = {key: source[key] for key in identifiers}
    row.update(proposed_xml=proposed, reason=notes[number]["reason"], review_notes=notes[number]["review_notes"], status="rewrite_draft")
    assert set(row) == fields
    assert all(isinstance(row[key], str) and row[key].strip() for key in fields)
    answer.append(row)
    report.append({"number": number, "source_characters": len(source["source_xml"]), "proposed_characters": len(proposed), "material_alineas": alinea_count(proposed), "numeric_tokens_preserved": True, "reference_occurrences_preserved": True, "xml_allowed": True})

assert len({row["source_id"] for row in answer}) == 14
assert (ROOT / "source.json").read_bytes() == source_bytes
(ROOT / "answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
reloaded = json.loads((ROOT / "answer.json").read_text())
assert len(reloaded) == 14
for source, result in zip(sources, reloaded):
    assert all(source[key] == result[key] for key in identifiers)
    assert result["proposed_xml"] == (ROOT / "drafts" / f"{source['number']}.xml").read_text().strip()
(ROOT / "validation.json").write_text(json.dumps({"article_count": len(answer), "manual_comparison": "Source et proposition relues intégralement, article par article ; corrections intégrées.", "articles": report}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"file": "answer.json", "articles": len(answer), "bytes": (ROOT / "answer.json").stat().st_size, "material_alineas": sum(row["material_alineas"] for row in report), "xml_numeric_and_reference_checks": "passed"}, ensure_ascii=False))
