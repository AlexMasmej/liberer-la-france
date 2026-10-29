# Project context and methods — French legal rewriting

**Public handoff and supporting context for the planned arXiv preprint.**

This document explains how the AI-assisted French legal rewriting project was carried out. It is a retrospective account of the documented second-pass workflow, prepared on 29 October 2026, rather than the preprint manuscript itself. It separates recorded results from legal conclusions and unknowns.

This public edition omits machine-specific paths, account and hosting identifiers, private operational records, and commands for restarting the original agents. The complete internal handoff remains a separate local working document. Public repository paths below identify available code or documentation; the presence of a script is not an instruction to execute it against production.

## 1. Edition and scope

The second-pass reference edition is commit [`b6e5e4468d0f97b9d93b89c8ac6caa5f8617c6ab`](https://github.com/AlexMasmej/liberer-la-france/commit/b6e5e4468d0f97b9d93b89c8ac6caa5f8617c6ab) and the [completed second-pass snapshot](snapshots/20261029T035156Z-second-pass-complete/README.md). Read its restoration instructions and manifests before comparing results.

The repository has subsequently received third-pass corrections. For example, commit [`1df0d018143b33e12655294c1e9be33655c6b162`](https://github.com/AlexMasmej/liberer-la-france/commit/1df0d018143b33e12655294c1e9be33655c6b162) was observed when preparing this publication. Its existence does not retroactively change the second-pass reference edition, and this document does not independently audit those later corrections. Statements about completion and outstanding work below describe the second-pass edition, unless explicitly stated otherwise.

The project covers five complete codes and the four annexes of the French General Tax Code: nine technical collections, not the whole body of French law. The source corpus is frozen at **18 October 2026**.

| Collection | Source entries | Proposed rewritten texts | Motivated retentions | First-pass documentary holds |
|---|---:|---:|---:|---:|
| Labour Code | 11,593 | 4,296 | 7,297 | 0 |
| General Tax Code | 2,375 | 1,387 | 988 | 0 |
| Social Security Code | 7,427 | 3,178 | 4,247 | 2 |
| Urban Planning Code | 2,459 | 1,530 | 929 | 0 |
| Construction and Housing Code | 4,126 | 2,205 | 1,921 | 0 |
| Tax Code annex I | 71 | 42 | 29 | 0 |
| Tax Code annex II | 674 | 388 | 286 | 0 |
| Tax Code annex III | 1,115 | 799 | 316 | 0 |
| Tax Code annex IV | 477 | 290 | 186 | 1 |
| **Total** | **30,317** | **14,115** | **16,199** | **3** |

The completed second pass covers **30,314 article identities**. The final recorded verification linked them to **2,894 distinct accepted native jobs and sessions**, and checked the ordinary validation state across **1,449 active batch-owner files**. The three documentary holds are separate first-pass items, not successful second-pass reviews.

These counts distinguish source coverage, actual rewriting, motivated retention and AI review. They do not demonstrate zero contradictions, exhaustive external-source coverage, or validation by a lawyer. The project recorded **zero lawyer-reviewed articles** at this milestone. The dedicated second-pass monitoring was stopped after completion and delivery.

## 2. Intent and editorial decisions

The initial short website summaries were not treated as complete rewrites of the codes. The scope expanded to full legislative and regulatory texts, annexes, tables, application notes, version boundaries and relevant transitions.

The documented editorial direction changed on 19 October 2026: substantive reductions in taxes, duplicative formalities and administrative constraints were prioritised over stylistic paraphrase. A useful provision could be retained with a specific explanation; copying a source or changing synonyms was not counted as a substantive simplification.

On 23 October, the second pass was directed primarily at **contradictions and inconsistencies**: within an article, between articles, and across the nine collections. Additional cuts were secondary to coherent implementation of the reforms already chosen.

The detailed reference files are `legal-rewrite/policy-coordinations.json`, `legal-rewrite/site-summaries.json` and `legal-rewrite/fiscal-net-method.json`. They separate policy choices from the official source law. Central instructions included:

- Preserve acquired rights, autonomous protections, exemptions and favourable exceptions, including future eligible cases where intended.
- Preserve the full official source even when the proposal repeals an obligation.
- Do not invent tax rates, promulgation dates, funding, national savings, legal equivalences or missing normative figures.
- Do not let a subordinate regulation, form or cross-reference silently reintroduce a burden removed by the proposal; equally, do not assume a regulation can abolish a statutory obligation.
- Keep identifiers and subdivisions stable where other provisions depend on them. An article number alone is not a reliable identity across codes or historical versions.
- Distinguish an intended policy benefit, an optimisation requiring political arbitration, an unintended textual gap, already-prohibited fraud, and an unverified hypothesis.

Examples of documented choices include a single indefinite-term employment contract for new employment, distribution-triggered ordinary corporate income tax, abolition of future inheritance-related taxes within the defined scope, preservation of favourable TASCOM and coastal exceptions, and a gradual pension transition combining solidarity with individualised collective capitalisation. The policies contain detailed conditions and transitions; these examples are not a substitute for reading those texts or an endorsement of their legal compatibility.

## 3. Official sources and version control

The source ingestion used the DILA LEGI stock archive `Freemium_legi_global_20250713-140000.tar.gz` plus **466 updates** through the corpus date. Historical and current versions were kept separately from proposed texts.

Official entry points:

- [LEGI dataset and documentation on data.gouv.fr](https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides).
- [DILA LEGI archive directory](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) and [Légifrance DTD documentation](https://echanges.dila.gouv.fr/OPENDATA/DTD_LEGIFRANCE/).
- [Labour Code](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/), [General Tax Code](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/), [Social Security Code](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073189/), [Urban Planning Code](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074075/), [Construction and Housing Code](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074096/).
- Tax Code annexes [I](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069568/), [II](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069569/), [III](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069574/), [IV](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069576/).

A current web page does not automatically reproduce the frozen version. The primary working identity is `(code_id, source_id)`, with source hashes and validity boundaries. Source bodies, NOTA application notes, historical lineage and article structures are relevant to interpretation. Sources from outside the nine collections must be identified and verified separately rather than assumed to be covered.

## 4. Technical architecture

The main implementation is Python, SQLite, XML and JSON, with static HTML publication. The websites are views of the shared drafting project rather than five independent legal databases.

```text
Official archives and verified documentary complements
    → versioned source ingestion and structured inventories
    → complete sources + policies + target texts assigned to a model job
    → complete proposed articles and reasons in answer.json
    → native execution evidence and ordinary content/consistency checks
    → archived previous version and guarded registration
    → comparative reader, downloadable codes and website summaries
    → a separately manifested, restorable public snapshot
```

Key repository components:

| Component | Purpose |
|---|---|
| `legal-rewrite/ingest.py`, `archive-manifest.json`, `corpus.json` | Archive provenance, XML ingestion and dated exports |
| `legal-rewrite/run_exhaustive.py` | Job orchestration, prompt assembly, response validation and retries |
| `legal-rewrite/review_prior.py` | Second-pass before-images, historical archives and guarded replacement |
| `legal-rewrite/register_batches.py` | Ordinary batch validation and canonical registration |
| `legal-rewrite/worker_execution.py` | Expected execution policy and checks of observed native session evidence |
| `legal-rewrite/reference_coherence.py`, `reference_queue.py` | Whole target texts, reference guards and review requirements |
| `legal-rewrite/substantive_impact.py` | Classification and passage-based justification of substantive effects |
| `legal-rewrite/source_assets.py` | Verified normative media and documentary companions |
| `legal-rewrite/batches/`, `registered-batches.json`, `revisions/` | Current owners, registration links and archived revisions |
| `legal-rewrite/build_reader.py`, `build_downloads.py`, `build_compact_sites.py` | Comparative reader, archives and public summaries |
| `legal-rewrite/check_downloads.py`, `publish_snapshot.py` | Publication checks and serialised generation/deployment |

The SQLite model separates official archives, articles, full XML documents, draft sources and proposed drafts. The five canonical draft fields are `source_sha256`, `status`, `proposed_xml`, `reason` and `review_notes`. SQL NULL, an empty string and an actual text value are distinct. Original XML bytes must not be replaced with an approximate string when verifying evidence.

The databases are too large for ordinary GitHub file limits. Read the snapshot-specific restoration instructions: consistent SQLite backups, split archives, checksums and differential overlays are used. A standalone file copied from a database during writes is not necessarily a coherent snapshot. The public export is selected material, not every private journal or operational proof from the originating workspace.

## 5. Models and prompt design

The documented policy at the close of the second pass used:

| Role | Model | Reasoning effort |
|---|---|---|
| Initial drafting | `gpt-6-astra` | `medium` |
| Earlier second-pass reviews | `gpt-6-astra` | `medium` |
| Later second-pass reviews, after explicit user request | `gpt-6.1-sol` | `high` |

The later switch was requested for cost reasons. The project did not establish a controlled comparison proving equivalent quality, speed or total cost. Exact realised costs per article and a causal performance gain are unknown.

Exact prompt sources are in the code: `run_exhaustive.py::INSTRUCTIONS`, the second-pass additions in `_run_job`, `substantive_impact.py::PROMPT`, and `reference_coherence.py::PROMPT`. Per-job copies of source texts and policies preserve what was actually assigned where retained in the export. Do not assume the latest prompt was used in every historical job.

The prompts required the model to read each assigned source, NOTA, previous proposal and relevant counterpart text in full, including long annexes and tables. They requested complete normative articles, not deltas, instructions to amend, or summaries. Where no correction was justified, a motivated retention was allowed.

For the second pass, the model was asked to classify interactions as an effective contradiction, necessary coordination, compatible transition, difference of scope, or unverifiable point. Unresolved dependencies outside the assigned batch had to be stated rather than silently treated as solved.

`answer.json` contains exactly one object per assigned source with identifiers, a source hash, article number, proposed XML, reason, review notes and status. Explicit repeal and partial normative reduction have additional justification metadata. The final short model message reports the output filename and article count; it is not the legal deliverable itself.

The original workers were instructed not to spawn additional agents. Broader research and external review sometimes involved separate specialised agents. That does not establish identical independence, model usage or coverage for every task.

## 6. Acceptance and preservation controls

A requested model name, a response file or a process returning zero is **not an accepted article**.

The pipeline checks observed native execution information against the expected model/effort, provider, session identity and working context. This is local execution evidence, not cryptographic provider attestation. Migrating to a different provider would require an explicitly reviewed evidence adapter rather than simply removing those checks.

Acceptance also requires:

1. Exact assigned source identity, source content and version boundaries.
2. Complete response coverage, allowed markup and checks for omitted normative material.
3. Preservation or explicitly justified alteration of figures, tables, conditions, exceptions and favourable provisions.
4. Comparison with whole current reference targets and policy guards.
5. Exact equality of the captured five-field database before-image and the complete active owner row before replacement.
6. A durable archive of the old proposal, followed by ordinary registration and final review bookkeeping.

Previous versions are preserved even when a proposal changes. An old refusal cannot be relabelled as accepted after a later success. Historical absence of an owner is documented as a historical fact, not invented into a new before-image.

The final coverage check operated on the complete set of article identities and actual accepted job evidence, rather than summing counters from successive agent runs. Technical acceptance still does not establish global legal coherence or lawyer review.

## 7. Problems and corrective work

The documented workflow encountered several important failure modes:

- **Usage/authentication refusals:** nominal credits or a clean coordinator exit did not prove that a model had accepted or completed a job. Repeated failures were preserved rather than hidden by indefinite retries.
- **Changed before-images:** several reviews refused to replace drafts because current owners/database values differed from the old proposal supplied to the review. Stable differences could not all be dismissed as temporary publication races. The initial actor and cause were not conclusively established.
- **Seven remaining articles:** the user explicitly authorised comparison of all historical/current versions. New reviews used genuine current before-images while preserving the older versions and refusals. Six bodies were retained after comparison; R6332-15 received a further coordination correction. These were accepted through the ordinary checks.
- **Registration rollback:** a later protection restores staged owner/registry changes after registration failure only when the database is demonstrably still equal to its before-image. It does not turn a failed validation into success or overwrite a committed change without reconciliation.
- **Low disk space:** some evidence copies were incomplete. Partial captures were retained and labelled; an incomplete proof directory was not promoted into an accepted observation. No normative source or sealed history was discarded merely to make a check pass.
- **Unstable observations:** a whole-file guard failing during ongoing publication is a refused capture, not automatically a failure of the legal drafting engine. Guards were not widened to manufacture agreement.
- **Measurement pitfalls:** an old observation field shadowed a metric variable and could not be used for throughput. Throughput required the actual whole metric stream and matching job packets. Partial windows and changing mixtures of work could not establish a causal speed gain.
- **Publication/export failures:** bounded retries, checksum verification and preserved base trees were used. Temporary export or partial-checkout problems were not treated as permission to delete unrelated history.

The final seven were R6341-15, R6332-95, R6332-23, R6333-3, R6332-15, R6332-17 and R6332-19 of the Labour Code. Their resolution closed the second-pass workflow; it did not close every dependency mentioned in their review notes.

## 8. Open questions at the second-pass milestone

Three first-pass documentary holds remained:

- Social Security Code D351-9: a consolidation discrepancy concerning L(A), 60 versus 62 years.
- Social Security Code annex I to R434-32 (7): a missing normative ophthalmological figure.
- Tax Code annex IV article 15: missing original CERFA models 30-0812 and 30-0813.

Twelve proposed Social Security Code coordinations were not integrated: R123-1, R123-1-1, D224-7, R152-8, D224-8, R153-2, R151-1, R151-3, R612-7, R216-2, R281-4 and R213-5. A prepared candidate or passing synthetic test was not treated as activation; their recorded readiness remained false.

Other documented review topics included alcohol/excise declarations and cross-code equivalences, AAH and hospital-fee transitions, tax-programme historical transitions, apprenticeship/CPF coordination, future source versions and statutory/regulatory interactions. See `legal-rewrite/notes-contradictions/INDEX.md` and `legal-rewrite/GUIDE-TROISIEME-PASSE.md`, read with their dates. A previously corrected body can still have an unresolved external-source qualification.

A structural reference audit after the second pass recorded **94,059 points to examine**, including **1,412 priority-1 flags on 792 articles**. These are not 94,059 confirmed legal contradictions: they include historical references, ambiguities, subdivisions, transitions and differences needing semantic interpretation. Graph cycles alone are not legal errors.

The independent red-team work associated with [PR #1](https://github.com/AlexMasmej/liberer-la-france/pull/1) initially examined intermediate editions. Its findings must be compared with the final snapshot and later corrections, not imported indiscriminately. The public repository may contain later decisions not reflected in this retrospective.

## 9. Published outputs

The five thematic sites are:

- [Libérer l'embauche](https://libererlembauche.com/).
- [Libérer le revenu](https://www.libererlerevenu.com/).
- [Libérer l'entreprise](https://www.libererlentreprise.com/).
- [Libérer le logement](https://www.libererlelogement.com/).
- [Libérer la retraite](https://www.libererlaretraite.com/).

The shared [comparative reader](https://www.libererlaretraite.com/corpus/) and [downloads catalogue](https://www.libererlaretraite.com/telechargements/) are hosted on the retirement site. The downloads include one archive per code, all four tax annexes with the Tax Code, and a combined archive. The website summaries are not a substitute for the complete texts and data.

At second-pass delivery, the five homepages, central catalogue, manifest and six complete code archives were checked against local publication bytes, sizes and hashes. This was a dated verification, not a permanent uptime or content guarantee. Later deployments must be assessed separately.

The public sites identify the project as an independent supporters' initiative, not an official project of Nouvelle Énergie or David Lisnard. Political inspiration and support links do not imply institutional approval of the proposed texts.

## 10. Using this material for the preprint

This document can support the methods, provenance and limitations sections of the planned arXiv preprint. It should not be cited as evidence that an independent human audit or controlled model experiment occurred where none is documented.

For a research account:

1. Name the exact code/data edition, corpus date and commit used for each result.
2. Separate source coverage, rewritten text, motivated retention, model review, technical acceptance, structural flags and legal validation.
3. State prompt and model changes over time rather than assigning one model to the whole project.
4. Describe before-image preservation, refusal handling and the final identity-based verification, including failures and incomplete observations.
5. Attribute external review findings, identify the edition they examined, and distinguish reproduction from merely reading a report.
6. Report coverage gaps, unresolved sources, political choices and legal uncertainty. Do not turn an intended reduction in taxation into an accidental exploit by definition.
7. Treat costs, performance comparisons, model independence and national fiscal effects as unknown unless separately supported by suitable measurements.

The exact cause of every quota failure, the origin of every intermediate inconsistency, realised per-article costs, an exhaustive list of remaining legal contradictions, and overall compatibility with superior law were not established by this handoff. The texts remain reform proposals rather than the law in force. Neither a second nor a third AI pass is, by itself, legal certification.
