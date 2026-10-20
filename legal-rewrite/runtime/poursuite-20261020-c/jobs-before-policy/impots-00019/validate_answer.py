import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / "source.json").read_text())
answer = json.loads((ROOT / "answer.json").read_text())
fields = {
    "code_id", "source_id", "source_sha256", "number", "proposed_xml",
    "reason", "review_notes", "status",
}
allowed = set(
    "p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote".split()
)


def plain(element):
    return "".join(element.itertext())


def numbers(element):
    return collections.Counter(re.findall(r"\d+(?:[.,-]\d+)*", plain(element)))


def number_words(element):
    return collections.Counter(re.findall(
        r"\b(?:deux|trois|quatre|cinq|six|onze|quinze|quart|deuxième|troisième|quatrième|cinquième|dixième)\b",
        plain(element),
    ))


def anchor(element):
    return re.match(
        r"^(?:(?:I|II|III|IV|V|VI)(?: bis)?\.\s*(?:–\s*)?)?(?:\d+[°.](?:\s*\d+[°.])?|[a-h]\)|[ABC]\.\s*–|-)?",
        plain(element),
    ).group()


assert isinstance(answer, list) and len(answer) == len(sources) == 6
seen = set()
total = 0
for source, proposed in zip(sources, answer):
    assert set(proposed) == fields
    for key in ("code_id", "source_id", "source_sha256", "number"):
        assert proposed[key] == source[key], (source["number"], key)
    assert proposed["source_id"] not in seen
    seen.add(proposed["source_id"])
    assert proposed["status"] == "rewrite_draft"
    assert all(
        isinstance(proposed[key], str) and proposed[key].strip()
        for key in ("proposed_xml", "reason", "review_notes")
    )
    assert proposed["proposed_xml"].strip() != source["source_xml"].strip()
    before = ET.fromstring("<root>" + source["source_xml"] + "</root>")
    after = ET.fromstring("<root>" + proposed["proposed_xml"] + "</root>")
    assert len(before) == len(after)
    for element in after.iter():
        if element.tag == "root":
            continue
        assert element.tag in allowed
        assert all(
            key in ("rowspan", "colspan") and re.fullmatch(r"[0-9]+", value)
            for key, value in element.attrib.items()
        )
    for index, (before_p, after_p) in enumerate(zip(before, after)):
        location = (source["number"], index + 1)
        assert numbers(before_p) == numbers(after_p), (location, "chiffres")
        assert number_words(before_p) == number_words(after_p), (
            location, "nombres en lettres", number_words(before_p), number_words(after_p)
        )
        assert anchor(before_p) == anchor(after_p), (location, "subdivision")
    assert collections.Counter(e.tag for e in before.iter()) == collections.Counter(
        e.tag for e in after.iter()
    )
    total += len(before)
    print(source["number"], ":", len(after), "alinéas : contrôles structurels conformes")

before = ET.fromstring("<root>" + sources[2]["source_xml"] + "</root>")
after = ET.fromstring("<root>" + answer[2]["proposed_xml"] + "</root>")
for root in (before, after):
    sentences = re.split(r"\.\s+(?=[A-ZÀ])", plain(root[4]))
    assert len(sentences) == 2 and "70 %" in sentences[1]
    sentences = re.split(r"\.\s+(?=[A-ZÀ])", plain(root[8]))
    assert len(sentences) == 7 and "effectivement vers" in sentences[3]
    assert "reliquat" in plain(root[15])

quinquies = ET.fromstring("<root>" + answer[4]["proposed_xml"] + "</root>")
assert "cinquième alinéa" in plain(quinquies[5])
assert "Si le solde est positif" in plain(quinquies[4])
print("TOTAL :", len(answer), "articles,", total, "alinéas ; JSON, XML et renvois de phrase contrôlés.")
