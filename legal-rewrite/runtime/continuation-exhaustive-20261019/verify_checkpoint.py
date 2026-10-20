"""Freeze a local edition, then compare its actual public download and pages.

The running coordinator may accept further articles during this check. Only
the frozen, published edition is asserted here; this is no legal validation.
"""
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import fcntl
import hashlib
import json
import sys
import time
import zipfile

LEGAL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LEGAL))
from source_assets import safe_html

SITE = LEGAL.parent / "sites"
SLUGS = ["travail", "impots", "securite-sociale", "urbanisme",
         "construction-habitation", *[f"impots-annexe-{i}" for i in range(1, 5)]]
PAGES = {
    "retraite": ("liberer-la-retraite", "https://www.libererlaretraite.com/"),
    "embauche": ("nouveaudroitdutravail", "https://www.libererlembauche.com/"),
    "revenu": ("liberer-le-revenu", "https://www.libererlerevenu.com/"),
    "entreprise": ("liberer-lentreprise", "https://www.libererlentreprise.com/"),
    "logement": ("liberer-le-logement", "https://www.libererlelogement.com/"),
}
FIELDS = ["source_sha256", "source_xml", "source_notes_xml", "proposed_xml", "status"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(row, raw=False):
    values = {field: row[field] for field in FIELDS}
    if raw:
        for field in FIELDS:
            if field.endswith("_xml") and values[field] is not None:
                values[field] = safe_html(values[field])
    return sha(json.dumps(values, ensure_ascii=False, sort_keys=True).encode())


def fetch(url):
    request = Request(url, headers={"Cache-Control": "no-cache",
                                   "User-Agent": "Legal-rewrite-check/1.0"})
    with urlopen(request, timeout=120) as response:
        assert response.status == 200
        return response.read()


def run():
    folder = Path(__file__).resolve().parent / "checkpoint-verification" / str(int(time.time()))
    folder.mkdir(parents=True)
    with (LEGAL / "runtime/publication.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        published = json.loads((LEGAL / "runtime/last-published.json").read_text())
        manifest_bytes = (SITE / "liberer-la-retraite/dist/downloads/manifest.json").read_bytes()
        manifest = json.loads(manifest_bytes)
        assert published["all_sites_published"] and published["local_checks_passed"]
        assert published["drafted_articles"] == manifest["drafted_articles"]
        assert manifest["source_records"] == 30317
        assert manifest["exhaustive_rewriting_complete"] is False
        expected = {}
        for slug in SLUGS:
            for row in json.loads((LEGAL / "runtime/export-source" / (slug + ".json")).read_text()):
                key = row["code_id"] + "|" + row["source_id"]
                assert key not in expected
                expected[key] = fingerprint(row, raw=True)
        assert len(expected) == 30317
        archive_sha = sha((SITE / "liberer-la-retraite/dist/downloads/cinq-codes-complets.zip").read_bytes())
        page_sha = {label: sha((SITE / slug / "dist/index.html").read_bytes())
                    for label, (slug, _) in PAGES.items()}
        method_sha = sha((SITE / "liberer-lentreprise/dist/chiffrage-is-net.html").read_bytes())
        impact_sha = sha((SITE / "liberer-la-retraite/dist/corpus/substantive-impact.json").read_bytes())
        impact_page_sha = sha((SITE / "liberer-la-retraite/dist/bilan-allegements.html").read_bytes())
        freeze = {"drafted_articles": manifest["drafted_articles"],
                  "archive_sha256": archive_sha, "expected_records": expected,
                  "five_pages_sha256": page_sha, "method_sha256": method_sha,
                  "impact_sha256": impact_sha, "impact_page_sha256": impact_page_sha}
        (folder / "frozen-expectations.json").write_text(json.dumps(freeze, ensure_ascii=False) + "\n")
        (folder / "manifest.json").write_bytes(manifest_bytes)

    urls = {label: url for label, (_, url) in PAGES.items()}
    urls.update(archive="https://www.libererlaretraite.com/downloads/cinq-codes-complets.zip",
                manifest="https://www.libererlaretraite.com/downloads/manifest.json",
                method="https://www.libererlentreprise.com/chiffrage-is-net.html",
                impact="https://www.libererlaretraite.com/corpus/substantive-impact.json",
                impact_page="https://www.libererlaretraite.com/bilan-allegements.html")
    with ThreadPoolExecutor(max_workers=4) as pool:
        public = dict(pool.map(lambda item: (item[0], fetch(item[1])), urls.items()))
    assert public["manifest"] == manifest_bytes, "Public edition changed: rerun against the next frozen edition"
    payload = public.pop("archive")
    assert len(payload) == manifest["all"]["bytes"]
    assert sha(payload) == archive_sha, "Public archive differs from the checked local edition"
    checked = set()
    with zipfile.ZipFile(BytesIO(payload)) as common:
        assert common.testzip() is None
        inner = json.loads(common.read("manifest.json"))
        assert inner["downloads"] == manifest["downloads"]
        impact_file = inner['substantive_impact_report']
        assert common.read(impact_file['filename']) == public['impact']
        for item in inner["downloads"]:
            data = common.read(item["filename"])
            assert sha(data) == item["sha256"]
            with zipfile.ZipFile(BytesIO(data)) as archive:
                assert archive.testzip() is None
                for name in archive.namelist():
                    if name.startswith("coordinations/") or not name.endswith("/articles.json"):
                        continue
                    for row in json.loads(archive.read(name)):
                        key = row["code_id"] + "|" + row["source_id"]
                        assert key not in checked
                        assert fingerprint(row) == expected[key], key
                        checked.add(key)
    assert checked == set(expected)
    for label in PAGES:
        assert sha(public[label]) == page_sha[label], label
    assert sha(public["method"]) == method_sha
    assert sha(public["impact"]) == impact_sha
    assert sha(public["impact_page"]) == impact_page_sha
    impact = json.loads(public['impact'])
    assert impact['coverage']['exported_articles'] == 30317
    assert impact['coverage']['exported_proposals'] == manifest['drafted_articles']
    assert impact['national_savings']['status'] == 'unknown'
    assert impact['net_global_reduction']['status'] == 'not_established'
    assert impact['aggregation']['article_counts_are_savings'] is False
    housing = public["logement"].decode()
    assert "franchise TASCOM" in housing and "dérogations littorales" in housing
    employment = public["embauche"].decode()
    for phrase in ["contrat unique", "quinze jours", "avant un an", "0,20 mois", "six mois"]:
        assert phrase in employment, phrase
    assert "Les CDD restent possibles" not in employment
    method = public["method"].decode()
    assert "CIR" in method and "Bpifrance" in method and "Aucun solde français chiffré" in method
    withdrawn = "https://www.libererlaretraite.com/downloads/coordination-sru-plages.html"
    try:
        fetch(withdrawn)
        raise AssertionError("Withdrawn coastal repeal remains public")
    except HTTPError as error:
        assert error.code == 404
    report = {"checked_at_unix": int(time.time()), "drafted_articles": manifest["drafted_articles"],
              "all_current_records_compared": len(checked), "public_archive_sha256": archive_sha,
              "five_sites_verified": True, "contract_unique_summary_verified": True,
              "favorable_coastal_tascom_summary_verified": True, "net_fiscal_method_verified": True,
              "withdrawn_coastal_repeal_http_status": 404,
              "graphic_articles_unresolved": manifest["graphic_source_coverage"]["unresolved_articles"],
              "substantive_report_verified_online_and_offline": True,
              "current_impact_counter_readings": impact['coverage']['current_approved_independent_reviews'],
              "global_net_reduction_established": False,
              "exhaustive_rewriting_complete": False, "semantic_review_by_jurist": False}
    (folder / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
