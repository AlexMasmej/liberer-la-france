import json
from pathlib import Path

root = Path(__file__).resolve().parent
sources = json.loads((root / "source.json").read_text())
metadata = json.loads((root / "draft_metadata.json").read_text())
assert len(sources) == 20
assert set(metadata) == {source["number"] for source in sources}

answer = []
for source in sources:
    number = source["number"]
    if number == "73":
        fragments = [root / "drafts" / f"73-{i}.xml" for i in range(1, 4)]
    else:
        fragments = [root / "drafts" / f"{number}.xml"]
    proposed = "\n".join(fragment.read_text().strip() for fragment in fragments)
    answer.append({
        "code_id": source["code_id"],
        "source_id": source["source_id"],
        "source_sha256": source["source_sha256"],
        "number": number,
        "proposed_xml": proposed,
        "reason": metadata[number]["reason"],
        "review_notes": metadata[number]["review_notes"],
        "status": "rewrite_draft",
    })

(root / "answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
