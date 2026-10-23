# Guarded recovery preflight — 2026-10-22 16:16–16:18 UTC

Recommendation: prioritize the registration optimizer and graceful coordinator handoff. CCH helper code can be grouped after combining/retesting its two gate changes with the optimizer; neither frozen CCH replay nor CSS's obsolete twelve-row apply is ready. No active code, policy, source, DB, process, reservation or resolution was modified. Evidence: `checks.json`; repeatable targeted read-only script: `check.py`. These are technical annotations, not legal validation.

## CCH

Exactly three original drafts remain absent: LEGIARTI000039049511 (annexe R422-37), LEGIARTI000032660331 (annexe R423-85), LEGIARTI000045646952 (annexe I R423-86), all from construction-habitation-00194. All four source bodies/hashes/numbers and official notes match the frozen evidence. LEGIARTI000045646995 (annexe II R423-86, job 00195) now has a different rewrite_draft, proposal SHA 5f3b0755692a643bb671d9e82529a66aa1599e3f0a8e8c51bfa1184e85768d41: preserve it, do not replay the original fourth answer.

Both old snapshots fail `check_guards` on L1221-2 / LEGIARTI000019071087. Both frozen answers still fail active `validate_answer` with Incomplete placeholder. Thus source guards pass but reference guards do not; no current recovery acceptance is established.

The active run_exhaustive.py and register_batches.py exactly match CCH's deployment-manifest before hashes, and template_fields.py is absent. CCH's old candidate is therefore a valid code base for a combined patch, but **do not deploy its complete register_batches.py over the optimizer**. Merge only compatible changes, preserve full validation and strict shared template helper in both gates; retain exact certified source/notes/clause/positions and arbitrary-value rejection. Preserve current orchestration/concurrency changes when assembling runner. Rerun original two-gate positive/negative fixture suite against the combined code in an isolated directory, not only the original candidate.

Next safe integration: establish coordinator drain/no old interpreters, verify combined before/after hashes, install combined code atomically as planned. Separately reassess changed reference target and build fresh reviewed snapshot/checks for remaining three proposals; do not silently refresh notes/certificates. Run validate_answer, accept_checks, current DB source/draft/reference/policy guards and registration gate under normal locks. Full owner uniqueness and any source DOCUMENT guard must be checked at that safe point. Only count accepted rows. Keep fourth existing draft intact.

## CSS

All twelve review-manifest entries are now `completed`: the old review recovery is superseded as a twelve-row unit. Eleven of twelve original DB draft beforeimages changed. L111-2-1 alone retains its original DB tuple; however its whole known-owner batch row changed and remains classified financing_transfer. Therefore the old metadata-only candidate has **not** been integrated exactly, and all twelve candidate DB tuples differ from current DB. Do not treat manifest completion as proof the old candidate was applied.

All twelve sources and notes still match. The old candidate's twelve rows pass current validate_answer; original policy fingerprint is current. This is validation of frozen inputs, not permission to overwrite current drafts. All captured known-owner row hashes have drifted. Only known captured owner files were read; no whole-corpus owner scan was done.

Required references: L1221-2 guard drifted; L1234-1, L1234-9 and L241-3 remain exact. Supplemental LO111-4-1 remains exactly at the explicitly reassessed retained_unchanged state. Supplemental LO111-10-2 has now drifted beyond both the original and reassessed guards; other four supplementals remain exact. All supplemental source/notes checks pass.

CSS old engine pin differs only for runner; validate_answer AST still equals reassessment baseline. Optimizer/CCH deployment will introduce additional intentional engine drift and needs explicit revalidation, not hash substitutions.

Next safe integration: keep old apply helper held and original evidence immutable. Since all twelve manifest items are completed, inspect the current L111-2-1 owner/certificate and determine whether a new narrowly scoped metadata correction is still substantively appropriate; preserve later reviewed proposals. Any new correction must be explicitly rebased/reviewed against current full row, sources, effects and burdens, current L1221-2 and LO111-10-2, then use normal guarded commit. The only originally approved metadata delta was `/2/substantive_impact/classification`: financing_transfer → mixed in the old twelve-answer candidate; it does not authorize replaying or transforming later draft content. Resolve old failure ledger only after sufficient current evidence, not from completion flags alone.

## Priority/conflicts

1. Preserve PID75807's valid in-flight review commit and finish optimizer validation; do not wait on stale recovery material.
2. Optional combined CCH code deployment at safe handoff after combined fixture tests; conflict is register_batches.py shared with optimizer and runner shared with admission change. No ready live article replay yet.
3. Defer CCH three-row replay until reference reassessment; preserve fourth draft.
4. Defer CSS: original twelve-row integration obsolete, current metadata question requires a fresh narrow review. No arbitrary values, legal-validation claims, reserve-resolution claims or recovered counters.

No new full DB copy or full corpus scan; read-only SQLite transaction for targeted checks. Checks are a point-in-time preflight and must be repeated at the actual integration point.
