"""Produce a bibliographic research record from already retrieved evidence only.

No network requests, database mutations, or active corpus changes.
All output is confined to this script's research directory.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name: str, value: object) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def fields(path: Path) -> list[dict]:
    root = ET.fromstring(path.read_bytes())
    out = []
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] == "datafield":
            out.append({"tag": node.attrib["tag"], "subfields": [
                {"code": child.attrib.get("code"), "value": child.text}
                for child in node
            ]})
    return out


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    old, current, former_r43435, new_r43432 = json.loads(
        (HERE / "version-chain-source-packet.json").read_text()
    )
    source_snapshot = PROJECT / "runtime/source-recovery-20261022/css/source-snapshot.json"
    jo_pdf = PROJECT / "runtime/source-recovery-20261022/css/documents/JORF_NC_19821230_303.pdf"
    comparison = json.loads((HERE / "ophthalmology-text-comparison.json").read_text())
    assert comparison["equal"] and comparison["changes"] == []

    selected = {}
    for name in ["bnf-cb34794207x.xml", "bnf-cb348253640.xml", "bnf-cb343631778.xml",
                 "bnf-cb37577169k.xml", "sudoc-035910356-unimarc.response",
                 "sudoc-035910348-unimarc.response"]:
        selected[name] = fields(HERE / name)
    save("catalogue-evidence-selected.json", selected)

    summary = {
        "at_utc": now,
        "status": "bibliographic_identity_and_physical_leads_established_facsimile_not_retrieved",
        "scope": "Barème d'invalidité en matière d'accidents du travail mis en place par le décret 82-1135 du 23 décembre 1982; schéma des quadranopsies manquant au chapitre 6.1.6 de l'annexe I.",
        "missing_graphic_resolved": False,
        "automatic_changes": [],
        "official_bibliography": {
            "author": "France. Ministère des affaires sociales et de la solidarité nationale",
            "title": "Accidents du travail, barème indicatif d'invalidité : [décret n° 82-1135 du 23 décembre 1982...]",
            "place": "Paris", "publisher": "Journaux officiels", "year": 1983,
            "extent": "30 p. : ill. ; 30 cm", "series": "Journal officiel de la République française, brochure 4010",
            "isbn": "2-11-071045-4", "bnf_ark": "ark:/12148/cb34794207x",
            "catalogue_url": "https://catalogue.bnf.fr/ark:/12148/cb34794207x",
            "evidence": "bnf-cb34794207x.xml",
            "call_number": "4-FW PIECE-1627",
            "location": "BnF, Tolbiac, Rez-de-Jardin, Droit, économie, politique, magasin",
            "digitization_link_in_record": False,
            "limitation": "Catalogue evidence identifies a printed official edition; its contents and diagram have not been consulted. Brochure 4010 is not a Documents administratifs issue number."
        },
        "sudoc_1983": {
            "ppn": "035910356", "catalogue_url": "https://www.sudoc.fr/035910356",
            "edition": "Ed. mise à jour en Février 1983.",
            "publisher": "Paris : Direction des Journaux officiels, 1983",
            "extent": "30 p. ; 21 cm", "isbn": "2-11-071045-4",
            "library": "Bibliothèque interuniversitaire Cujas, Paris", "rcr": "751052119",
            "call_number": "M/96.616-4010 ed.1983", "call_number_fields": ["915$a", "999$z"],
            "collection_field_225v": "3010",
            "discrepancies_preserved": [
                "SUDOC 225v gives 3010, whereas its exemplar call number and BnF give 4010.",
                "SUDOC describes a 21 cm edition; BnF describes a 30 cm edition. Identical physical manifestations are not assumed."
            ],
            "limitation": "February 1983 is an edition-update statement, not proof of the original Documents administratifs publication date."
        },
        "later_official_edition": {
            "bnf_ark": "ark:/12148/cb348253640", "year": 1984,
            "catalogue_url": "https://catalogue.bnf.fr/ark:/12148/cb348253640",
            "call_number": "4-FW-5338 (1984)",
            "sudoc_ppn": "035910348", "edition": "Ed. mise à jour en Décembre 1984.",
            "cujas_call_number": "M/96.616-4010 ed.1984",
            "chambery_library": "CHAMBERY-CENTRE FAVRE", "chambery_rcr": "731372202",
            "chambery_call_number": "346.03 acc",
            "limitation": "Useful comparison edition, not a demonstrated facsimile of the original Documents administratifs annex."
        },
        "documents_administratifs_periodical": {
            "paper_issn": "0242-6773", "paper_bnf_ark": "ark:/12148/cb343631778",
            "sudoc_ppn": "039373738", "paper_call_number": "LC2-3190 (DOCUMENTS ADMINISTRATIFS)",
            "paper_holding_record_checked": "1994- (does not establish paper holdings for 1983)",
            "microfiche_bnf_ark": "ark:/12148/cb37577169k",
            "catalogue_url": "https://catalogue.bnf.fr/ark:/12148/cb37577169k",
            "microfiche_holdings": [
                {"call_number": "A2-MF 00015", "location": "Tolbiac, Haut-de-Jardin, Droit, économie, politique, salle D, libre accès", "holdings": "1981-2000"},
                {"call_number": "MICROFICHE M-35141", "location": "Tolbiac, Rez-de-Jardin, Droit, économie, politique, magasin", "holdings": "1906-1941;1945-2001"}
            ],
            "finding_aids": "Record describes page/issue concordance and paper-issue/microfiche concordance tables. The paper-periodical record describes an annual table accompanying the last issue of each year.",
            "exact_annex_issue": None, "exact_annex_date": None,
            "limitation": "Holdings demonstrate a physical route covering 1982-1983, not inspection of a particular issue or confirmation of the annex's actual publication."
        },
        "primary_decree_evidence": {
            "title_from_print": "Décret n° 82-1135 du 23 décembre 1982 modifiant le décret n° 46-2959 du 31 décembre 1946 et le décret n° 73-598 du 29 juin 1973 en ce qui concerne le barème indicatif d'invalidité en matière d'accidents du travail",
            "publication": "JORF du 30 décembre 1982, n° 303, p. 3975-3976",
            "existing_pdf": str(jo_pdf), "sha256": sha(jo_pdf),
            "pdf_pages_read_and_visually_checked": [75, 76],
            "printed_pages": [3975, 3976],
            "article_1": "Adds the barème annex reference after the first paragraph of article 124 of decree 46-2959.",
            "article_2": "Adds the barème annex reference after the second paragraph of I of article 29 of decree 73-598.",
            "note_1": "Annex publication is announced in the next Documents administratifs issue; no actual issue number or date is supplied.",
            "article_3": "Applicable from 1 January 1983.",
            "facsimile_of_annex_present": False
        },
        "version_chain": [
            {"stage": "1982-1983 primary annex", "status": "decree checked; printed annex not retrieved", "unproved_link": "Actual graphics and their continuity into the later codified text"},
            {"stage": "1985-12-21 to 2006-02-06", "source_id": old["id"], "number": old["number"], "source_sha256": old["source_sha256"], "document_sha256": old["document_sha256"], "evidence": "version-chain-source-packet.json", "placeholder_present": True},
            {"stage": "1993-01-20", "text": "Décret 93-74 du 18 janvier 1993, article 1", "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000361429", "scope_checked": "Initial text adds chapter 16 (immune system); it does not reproduce or amend the ophthalmology diagram."},
            {"stage": "2006 renumbering", "text": "Décret 2006-111 du 2 février 2006, article 1 VII 1°", "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000261498", "scope_checked": "Articles R434-34 to R434-38 become R434-31 to R434-35; former R434-35 becomes R434-32.", "date_caution": "Underlying R434-32 article metadata start 2006-02-05; annex version metadata start 2006-02-06. Dates are reported as stored, not harmonized."},
            {"stage": "Since 2006-02-06 in frozen corpus", "source_id": current["id"], "number": current["number"], "source_sha256": current["source_sha256"], "document_sha256": current["document_sha256"], "placeholder_present": True, "text_comparison": "No differences between the 1985-2006 and subsequent ophthalmology plain texts after removal of whitespace only. This proves neither the missing image's content nor its unchanged legal status."}
        ],
        "rejected_replacement": {
            "natlex_59989": {"url": "https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/59989/FRA-59989.pdf", "observation": "Légifrance consolidation generated 20 August 2021, 3300 pages; PDF p.3201 (zero-based3200) retains the same [cliché non reproduit] placeholder. It is not the 1983 facsimile.", "downloaded_locally": False},
            "cnam_2013": "Not used as an adopted annex or substitute for the missing original graphic.",
            "ucanss_1983": "BnF cb347683422 describes a separate UCANSS VII-142 p. edition with additif 4 p.; not promoted to a primary JO facsimile."
        },
        "next_verifiable_steps": [
            "Consult the BnF Documents administratifs microfiche annual tables for late 1982 and early 1983, using their paper/microfiche concordances to identify the issue announced on 30 December 1982.",
            "Consult the BnF 1983 official brochure (4-FW PIECE-1627) or Cujas February 1983 edition (M/96.616-4010 ed.1983); photograph/scan the title, edition, publication/imprint and chapter6.1.6 together.",
            "Compare that image with a verified later official edition, record all publication details and applicable version links, and only then consider a guarded corpus supplement."
        ],
        "limits": [
            "No exact Documents administratifs issue/date established; no invented date inferred from a catalogue creation timestamp, a brochure number, or an edition-update month.",
            "No primary annex facsimile or quadranopsies diagram recovered online. Lack of a digitization link in checked catalogue records does not prove that no digitization exists anywhere.",
            "No direct contact with archives/libraries, no purchase or reproduction order, no authentication or CAPTCHA bypass.",
            "No database, corpus, source, policy, batch, active companion, drafting limit, process or coordinator modified."
        ],
        "local_provenance": {"source_snapshot": str(source_snapshot), "source_snapshot_sha256": sha(source_snapshot), "historical_snapshot": "runtime/global-reference-audit-20261022/corpus.snapshot.sqlite", "snapshot_queries": "Four indexed code_id,id article/document lookups; no new snapshot and no live database scan.", "extracted_packet": "version-chain-source-packet.json"}
    }
    save("summary.json", summary)

    web = [
        {"url": "https://catalogue.bnf.fr/rechercher.do?index=SujConstr&numNotice=11982876_11931476_", "observation": "Official BnF subject-results list exposes 1983 and1984 Journaux officiels editions; complete records retrieved through public SRU, saved here."},
        {"url": "https://api.bnf.fr/fr/api-sru-catalogue-general", "observation": "Official documentation for the public SRU catalogue API used for the saved records."},
        {"url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000361429", "observation": "Initial 1993 decree read on Légifrance; chapter16 added, not a reproduction of chapter6."},
        {"url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000261498", "observation": "Initial 2006 decree read on Légifrance; article1 VII1 renumbers R434-35 as R434-32."},
        {"url": "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019323362/1995-06-24", "observation": "Historical ophthalmology article confirms 1985-2006 period; complete article/documents separately read from frozen corpus."},
        {"url": "https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/59989/FRA-59989.pdf", "observation": "Web PDF text identified as a 2021 Légifrance consolidation; quadranopsies page still lacks graphic."},
        {"url": "https://www.legifrance.gouv.fr/liste/docAdmin", "observation": "Parent-reported catalogue inspection covered2006-2026 only; not independently repeated in this research."}
    ]
    save("primary-web-observations.json", web)
    save("search-log.json", {
        "at_utc": now,
        "note": "Representative searches actually run; negative results are bounded discovery observations, not proof of nonexistence.",
        "web_query_groups": [
            ['"barème indicatif" "1983" "4010"', '"Documents administratifs" "1983" "invalidité"', '"82-1135" "annexe" "documents"'],
            ['"barème" "accidents du travail" "Documents administratifs" "1983"', '"invalidité" "J.O." "1983" "D.A."', '"barème" "1983" "Documents administratifs" "janvier"'],
            ['site:francearchives.gouv.fr "barème" "invalidité" "1982"', 'site:archives-nationales.culture.gouv.fr "82-1135"', 'site:dila.premier-ministre.gouv.fr "archives" "documents administratifs"'],
            ['site:circulaires.ameli.fr "82-1135"', 'site:circulaires.ameli.fr "indicatif" "invalidité" "1983"', 'site:circulaires.ameli.fr "barème" "quadranopsies"']
        ],
        "catalogue_fetch_logs": ["bnf-fetches.json", "catalogue-crosssearch-fetches.json", "sudoc-record-fetches.json", "additional-fetches.json"],
        "negative_or_failed_routes": [
            "Internet Archive Documents administratifs title/year1982-1983 query returned one unrelated Québec vocabulary; no target annex.",
            "Internet Archive barème title or ISBN2110710454 query returned no records.",
            "Gallica SRU returned403; no circumvention attempted.",
            "Ameli public date/title query connection reset; indexed web searches did not locate an original1983 annex facsimile.",
            "Some direct catalogue/Légifrance web opens returned403 or unavailable; public BnF and SUDOC catalogue APIs succeeded."
        ]
    })

    report = """# Barème du décret 82-1135 : référence retrouvée, image encore manquante

La référence d'une édition officielle de 1983 et des exemplaires consultables est établie. **Le fac-similé de l'annexe et le schéma des quadranopsies n'ont pas été retrouvés ; le point graphique reste non résolu.** Le jour et le numéro des *Documents administratifs* ne sont pas établis.

## Référence bibliographique vérifiée

France. Ministère des affaires sociales et de la solidarité nationale. *Accidents du travail, barème indicatif d'invalidité : [décret n° 82-1135 du 23 décembre 1982...]*. Paris : Journaux officiels, 1983. 30 p. : ill. ; 30 cm. Collection *Journal officiel de la République française*, brochure **4010**. ISBN **2-11-071045-4**. [BnF, notice cb34794207x](https://catalogue.bnf.fr/ark:/12148/cb34794207x).

Exemplaire BnF : **4-FW PIECE-1627**, Tolbiac, Rez-de-Jardin, Droit, économie, politique, magasin. La notice ne fournit aucun lien de numérisation. Cela n'établit pas une absence de numérisation ailleurs. Le numéro4010 est celui d'une brochure, pas celui d'un numéro de *Documents administratifs*.

Le [SUDOC, PPN035910356](https://www.sudoc.fr/035910356), décrit une **édition mise à jour en février1983**, Paris : Direction des Journaux officiels, 30p.,21cm, même ISBN. Localisation confirmée : **bibliothèque Cujas**, RCR751052119, cote **M/96.616-4010 ed.1983** (champs915$a et999$z). Deux divergences de catalogue sont conservées : son champ225v indique3010 et son format21cm, contre4010 et30cm à la BnF. L'identité matérielle des deux éditions n'est pas présumée ; février1983 n'est pas assimilé à une date de publication de l'annexe originale.

Comparaison possible avec l'édition1984 : [BnF cb348253640](https://catalogue.bnf.fr/ark:/12148/cb348253640), cote **4-FW-5338 (1984)** ; [SUDOC035910348](https://www.sudoc.fr/035910348), mise à jour décembre1984, Cujas **M/96.616-4010 ed.1984** et Centre Favre, Chambéry, **346.03 acc**. Le contenu de ces exemplaires n'a pas été consulté.

## Piste précise pour le numéro des Documents administratifs

La collection sur microfiches est décrite par la [BnF, cb37577169k](https://catalogue.bnf.fr/ark:/12148/cb37577169k). Deux états de collection couvrent1982-1983 :

| Cote | Lieu indiqué | État de collection |
| --- | --- | --- |
| **A2-MF 00015** | Tolbiac, Haut-de-Jardin, salleD, libre accès | 1981–2000 |
| **MICROFICHE M-35141** | Tolbiac, Rez-de-Jardin, Droit, économie, politique, magasin | 1906–1941 ;1945–2001 |

La notice décrit des tables de concordance entre pages, numéros papier et microfiches. La notice de la série papier [cb343631778](https://catalogue.bnf.fr/ark:/12148/cb343631778), ISSN0242-6773, mentionne une table annuelle avec le dernier numéro de chaque année. Sa cote **LC2-3190 (DOCUMENTS ADMINISTRATIFS)** ne porte cependant qu'un état1994– dans l'exemplaire contrôlé : elle ne prouve pas une collection papier1983.

La prochaine consultation précise serait celle des tables annuelles fin1982 et début1983, puis du numéro annoncé par le décret. Aucun numéro, jour de parution, pagination d'annexe ou numéro de microfiche individuel n'est déduit sans cette consultation.

## Ce qui est établi dans la chaîne documentaire

Le PDF1982 déjà présent a été lu et vérifié visuellement aux pages75–76, imprimées3975–3976. Le titre imprimé porte bien sur la modification des décrets46-2959 et73-598. Les articles1 et2 y ajoutent la référence au barème annexé ; l'article3 indique l'application au1erjanvier1983. La note(1), p.3975, annonce une publication dans le prochain numéro des *Documents administratifs* sans le dater. Ce PDF contient le décret, pas l'annexe recherchée. Aucun téléchargement1982/1984/2004 n'a été refait.

Les documents ARTICLE complets et textes historiques ont été lus dans le snapshot existant, par quatre recherches indexées(code_id,id). **LEGIARTI000019323362**, annexeI à R434-35(7), couvre21décembre1985–6février2006. **LEGIARTI000028675462**, annexeI à R434-32(7), commence le6février2006. Après retrait des seuls espaces, leurs textes d'ophtalmologie sont identiques, y compris la mention du cliché manquant. Cette égalité ne fournit pas l'image et ne démontre pas sa continuité depuis1982.

Le [décret93-74, version initiale, art.1](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000361429) ajoute le chapitre16 sur le système immunitaire. Il ne reproduit pas et ne modifie pas le schéma d'ophtalmologie. Le [décret2006-111, version initiale, art.1VII1°](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000261498) renumérote les articlesR434-34 àR434-38 : l'ancienR434-35 devientR434-32. Les métadonnées de l'article support débutent le5février2006 et celles de l'annexe le6février : ces dates sont rapportées séparément, sans harmonisation juridique automatique.

**Maillon encore absent :** confrontation de la publication primaire de l'annexe1982–1983, schéma compris, avec la codification1985 et une édition ultérieure officielle. L'origine juridique générale est documentée ; l'identité du graphique n'est pas prouvée.

## Sources écartées et limites

Le PDF[NATLEX59989](https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/59989/FRA-59989.pdf) est une consolidation Légifrance générée le20août2021 : la page3201 porte elle aussi la lacune. Il n'est pas le fac-similé original et n'a pas été téléchargé. Le projet CNAM2013 n'est utilisé comme aucune annexe adoptée ni source de remplacement. L'édition UCANSS1983 repérée à la BnF est une autre édition ; elle n'est pas qualifiée de fac-similé JO.

Les recherches BnF/SUDOC, web exact, InternetArchive, DILA/FranceArchives et Ameli n'ont pas retrouvé de fac-similé primaire en ligne. GallicaSRU a renvoyé403 et la recherche publique Ameli a été interrompue côté serveur ; aucun contournement n'a été tenté. La conclusion est une absence de résultat dans les voies inspectées, pas une absence mondiale de numérisation.

Les notices complètes, requêtes publiques, états de collection, empreintes des fichiers et paquet de versions sont conservés dans ce dossier. Aucun message n'a été envoyé, aucun achat commandé, aucun corpus, compagnon actif, batch, politique, quota, processus ou coordinateur modifié. Les six rédacteurs restent hors de ce sous-travail.

## Livrables

- `summary.json` : faits établis, références, limites et prochaines vérifications.
- `catalogue-evidence-selected.json` et noticesXML/UNIMARC originales : preuve de catalogue, cotes et divergences conservées.
- `version-chain-source-packet.json` : quatre articles et documentsARTICLE complets, empreintes exactes du snapshot.
- `ophthalmology-text-comparison.json` : comparaison limitée et reproductible des textes1985/2006.
- `JO1982-p75.png`, `JO1982-p76.png`, textes correspondants : rendu local des pages du PDF déjà acquis.
- `search-log.json`, journaux de récupération, `primary-web-observations.json` : périmètre réel des recherches.
- `artifact-manifest.json` : empreintesSHA256 des pièces du dossier.
"""
    # Display typography only; preserve catalogue fields and identifiers verbatim.
    for before, after in {
        "numéro4010": "numéro 4010", "PPN035910356": "PPN 035910356",
        "SUDOC035910348": "SUDOC 035910348", "février1983": "février 1983",
        "décembre1984": "décembre 1984", "édition1984": "édition 1984",
        "30p.": "30 p.", "21cm": "21 cm", "30cm": "30 cm",
        "RCR751052119": "RCR 751052119", "225v indique3010": "225v indique 3010",
        "contre4010": "contre 4010", "et30 cm": "et 30 cm",
        "couvrent1982-1983": "couvrent 1982-1983", "salleD": "salle D",
        "ISSN0242-6773": "ISSN 0242-6773", "état1994": "état 1994",
        "papier1983": "papier 1983", "fin1982": "fin 1982", "début1983": "début 1983",
        "PDF1982": "PDF 1982", "pages75–76": "pages 75–76",
        "imprimées3975–3976": "imprimées 3975–3976", "décrets46-2959": "décrets 46-2959",
        "et73-598": "et 73-598", "articles1 et2": "articles 1 et 2",
        "l'article3": "l'article 3", "au1erjanvier1983": "au 1er janvier 1983",
        "note(1)": "note (1)", "p.3975": "p. 3975", "téléchargement1982": "téléchargement 1982",
        "recherches indexées(code_id,id)": "recherches indexées (code_id, id)",
        "annexeI": "annexe I", "couvre21décembre1985–6février2006": "couvre le 21 décembre 1985–6 février 2006",
        "le6février2006": "le 6 février 2006", "depuis1982": "depuis 1982",
        "décret93-74": "décret 93-74", "art.1": "art. 1", "chapitre16": "chapitre 16",
        "décret2006-111": "décret 2006-111", "1VII1°": "1, VII, 1°",
        "articlesR434-34 àR434-38": "articles R434-34 à R434-38",
        "l'ancienR434-35": "l'ancien R434-35", "le5février2006": "le 5 février 2006",
        "le6février": "le 6 février", "l'annexe1982–1983": "l'annexe 1982–1983",
        "codification1985": "codification 1985", "NATLEX59989": "NATLEX 59989",
        "le20août2021": "le 20 août 2021", "page3201": "page 3201",
        "CNAM2013": "CNAM 2013", "UCANSS1983": "UCANSS 1983",
        "InternetArchive": "Internet Archive", "GallicaSRU": "Gallica SRU",
        "renvoyé403": "renvoyé 403", "textes1985/2006": "textes 1985/2006",
        "empreintesSHA256": "empreintes SHA256", "noticesXML/UNIMARC": "notices XML/UNIMARC",
        "documentsARTICLE": "documents ARTICLE",
    }.items():
        report = report.replace(before, after)
    (HERE / "REPORT.md").write_text(report)
    manifest = {"at_utc": now, "root": str(HERE), "files": [
        {"name": f.name, "sha256": sha(f), "bytes": f.stat().st_size}
        for f in sorted(HERE.iterdir()) if f.is_file() and f.name != "artifact-manifest.json"
    ]}
    save("artifact-manifest.json", manifest)
    print(json.dumps({"status": summary["status"], "missing_graphic_resolved": False,
                      "files": len(manifest["files"]), "report": str(HERE / "REPORT.md")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
