# Tiger team assessment

## Scope and verdict

This assessment reviews the original drafting pipeline, the red team’s third-pass reports and correction trail, the audit scripts and verdicts, the preprint, and `main` at commit [`5fbf43e5a5c3ba5e2ff671aa496478aa96eedcce`](https://github.com/AlexMasmej/liberer-la-france/commit/5fbf43e5a5c3ba5e2ff671aa496478aa96eedcce).

**The project is a valuable, unusually transparent research artifact, but it is not ready to become legislation.** The red team found real systemic defects and many corrections are verifiably present. Important legal defects nevertheless remain open, the red team has become a co-author rather than an independent evaluator, and the headline reliability statistic measures AI-judged textual coherence—not legal validity.

This was a sampled AI review, not an exhaustive re-read or validation by a lawyer.

## What holds up well

- **Provenance and version discipline.** Official sources are separated from proposals, with identifiers, hashes, before-images, archived revisions, and guarded replacement. These are substantial engineering controls.
- **The red team’s substantive work.** It correctly identified two structural blind spots: published future versions and subordinate texts preserving removed obligations. Its objections generally include exact versions, passages, reasoning, corrections, and uncertainties.
- **Corrections are real, not merely reported.** Direct checks confirmed that the corrected CGI 150 VM and 287 proposals are present in current `main`. Conversely, the unresolved corporate-interest objection remains verbatim in CGI 212 bis.
- **The statistical arithmetic is reproducible.** Samples 7 and 8 each contain 632 unique, disjoint articles. From the published 60 repaired and 9 introduced defects, the figures are:
  - 95 official-text defects versus 44 rewritten-text defects;
  - a **53.68% relative reduction**;
  - a 95% interval of approximately **40.4%–64.0%**;
  - McNemar exact \(p \approx 2.24\times10^{-10}\).
- **The preprint is candid about many limits**, including self-evaluation, model disagreement, missing case law, and zero lawyer-reviewed articles.

## Release-blocking legal issues

These deserve priority over further aggregate defect-rate improvements.

### 1. VAT reform effectiveness remains unresolved

The [systematic tax review](../red-team/troisieme-passe/audit/AUDIT-ET-BALAYAGES.md) leaves approximately nine cases where reforms are written into CGI subdivisions whose content moves to the CIBS on 1 January 2027. Without including the CIBS or using an effective non-codified legislative vehicle, those reforms can be ineffective.

### 2. CCH R318-7 remains in current `main`

The [current proposal](../legal-rewrite/batches/automatic-construction-habitation/00114.json) removes both the personal motive and maximum duration for renting a property financed by a first-time-buyer advance. The fresh audit’s concern is substantial: this appears to relax a statutory principal-residence condition by decree. Either the statute must expressly authorize the new policy or the relaxation must be reconsidered. Its registry hash confirms that the text has not changed since that audit.

### 3. CGI 1763 C still contains an indeterminate sanction base

The [current text](../legal-rewrite/batches/automatic-impots/00130.json) retains a 20% fine calculated by reference to reaching “50% or 100%” of quotas, although the relevant target no longer supplies those thresholds. Saying that they create no intermediate deadline does not repair the amount of the fine. This provision needs substantive redrafting, not another safeguarding clause.

### 4. Distribution-based corporate tax needs specialist EU-law review

CGI 212 bis currently says that corrections adjust tracked bases and, where relevant, distributions already made, without making retained profits immediately taxable. [ATAD Article 4(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016L1164) states that exceeding borrowing costs are deductible **in the tax period in which they are incurred only up to 30% of EBITDA**. This makes the red team’s objection serious and well grounded. It does **not**, by itself, prove a violation: compatibility of the complete distribution-based regime and available options still requires expert analysis. The red team’s “confirmed mechanism” should therefore not be read as “confirmed illegality.”

### 5. Financing decisions remain open, not merely technical

Payroll-tax compensation and the CNBF/ASV regimes still require explicit revenue, reserve, vehicle, and acquired-rights decisions. The red team correctly left some of these as uncertain or political arbitrations. Declaring protective language without identifying resources does not establish financial sustainability.

The last fresh audit deliberately left **16 defects uncorrected**. Two important examples above were directly confirmed in current `main`; the other findings were not independently requalified. A single current register should make every one of them visible with an owner and disposition.

## Assessment of the red team

The [original red-team report](../red-team/troisieme-passe/reports/RAPPORT.md) is strong as a risk-based review, but it was never exhaustive. Its 243 objections describe a historical snapshot, not the current state.

Two developments weaken its independence:

- **Reviewer became writer.** After applying more than a thousand corrections, the red team and its models are evaluating their own work. The preprint acknowledges this as partial self-evaluation.
- **The alignment rule is policy-specific.** Corrections favor fewer taxes and constraints and preserve chosen reforms. That is appropriate for implementation, but it is not neutral assessment of policy merits or superior-law compliance.

There is also no sufficiently clear **live residual-risk register**. The initial register, P0/P1 application table, P2 rounds, sweeps, and fresh audits are spread across many directories. Current status must be reconstructed rather than read.

## What the “54% fewer defects” result actually proves

The result is statistically coherent for the published AI verdicts. It should nevertheless be worded narrowly:

> In two frozen paired samples, the rewritten text had 54% fewer **AI-flagged gross coherence defects under this protocol**.

It does not establish that the rewritten law is 54% more correct, constitutional, enforceable, or ready for enactment because:

- no lawyer-established ground truth exists;
- the intervals cover sampling variation, not auditor misclassification;
- constitutional and EU-law risks are excluded or marked uncertain;
- case law is outside the review;
- minor clerical defects and reform-nullifying defects count equally;
- the two fresh audits used different models, with visibly different rewritten-text rates;
- sample 7 was subsequently corrected, while sample 8 remains the intact measurement. There is no single unchanged corpus state for which 3.5% is now a fresh measurement.

The comparison against official consolidated law is useful, but it measures editorial coherence—especially dead references and coordination—not the quality of the political choices.

## Original pipeline and reproducibility

The principal architectural defect is visible in the inputs:

- `legal-rewrite/run_exhaustive.py:190` loads the reader’s current-article JSON.
- `legal-rewrite/ingest.py::export_snapshot` selects versions valid at the reference date, excluding published successors from drafting assignments.

That explains how all 30,314 current identities could pass review while 516 future versions received no proposal. Future versions must become first-class nodes in the drafting and validation graph.

The guarded writer is also **not atomic across SQLite and the filesystem**. `register_batches.py:175` commits SQLite before replacing the registry at line 181, while `review_prior.commit` has already rewritten batch files. A crash or I/O failure can therefore leave database, batches, and registry inconsistent. The tests explicitly preserve a post-commit failure for later reconciliation; they do not demonstrate universal rollback. A write-ahead journal and startup reconciliation are needed.

Finally, exact reproduction needs better packaging:

- fresh-audit verdicts are dated 31 October despite 5–6 November samples and chronology;
- `evidence/cited/production-20261031/` is referenced but not published;
- `sample8.py` retains copied sample-7 documentation;
- the validator requires POSIX `fcntl`, and a full Windows checkout fails on filenames containing `R*`.

The reported 321 tests could not be independently run in this review: the focused test command stops at `ModuleNotFoundError: fcntl` on Windows. This is a portability limitation, not evidence that the upstream POSIX tests fail.

## Recommended next steps

1. **Freeze a release candidate** and publish one authoritative register: open, fixed, accepted-risk, political arbitration, out-of-corpus, and unverified—with commit and owner for each item.
2. **Resolve the release blockers first**: CIBS, R318-7, CGI 1763 C, the ATAD question, financing decisions, and every open fresh-audit defect.
3. **Run an independent fourth-pass evaluation** on a frozen text using practising lawyers and a separate model/vendor. Use a fresh, untouched holdout stratified by code, rewrite status, and severity; make no corrections until scoring is complete.
4. **Report inherited and introduced defects separately**, with severity-weighted results and per-code breakdowns. Preserve the current arithmetic and paired design.
5. **Strengthen reproducibility**: publish exact audit evidence and timestamps, version every measurement by commit, document supported platforms, and add crash-injection tests for cross-store recovery.
6. **Temper the preprint’s cost claims.** The €6–36 million scenarios count article-processing hours, not equivalent validated legal work. Remove the large multipliers from the abstract and key-result box, and include the cost of the human review still required.

No project files were modified during the review preceding this assessment.
