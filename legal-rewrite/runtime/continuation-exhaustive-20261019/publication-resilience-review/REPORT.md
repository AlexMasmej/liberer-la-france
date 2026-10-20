# Publication resilience — separate proposal

No canonical module was changed. Both patches apply cleanly to the frozen module hashes recorded in `validation.json`. No network call or deployment was made.

## Behavior

`publish_snapshot.py.patch` preserves local corpus/build/download checks and destination validation as fatal failures (exit 1). For deployment only, each site gets at most **three total attempts**, each capped at **900 seconds**, with 2- and 4-second waits between transient network failures. Other deployment errors are not retried. The report is written before validation and after each deployment attempt, and remaining sites are attempted after one fails. Raw CLI output stays in private log files; it is not copied into the report or terminal output.

Exit 0 means the requested operation succeeded; exit 20 means local checks passed but at least one deployment remains unconfirmed. A local-only build never claims five deployments succeeded. `last-published.json` advances only when all five Vercel commands report success; a partial failure preserves the previous successful report. A timeout may have created a remote deployment, but it remains honestly unconfirmed here.

`run_exhaustive.py.patch` accepts only the explicit deployment-only exit 20 plus a consistent report, records `runtime/exhaustive/publication-state.json`, and preserves `publication_pending` in subsequent status updates. Article work continues. A successful later deployment clears pending; a local-only export does not. Local validation failures retain the blocking path. Both periodic and final publication checkpoints use this helper.

## Verification

13 new isolated regression tests pass, including timeout-then-success, the actual 900-second subprocess argument, persistent deployment failure, authentication failure without retry, local validation failure, destination mismatch, durable pending status, and pending clearance. All 142 existing discovered tests also pass with the proposed modules loaded. All publication/model calls in these tests are simulated. Detailed counts and SHA-256 guards are in `validation.json` and `existing-regressions.json`.

## Boundaries

Publication remains sequential and can wait for each bounded attempt. Subsequent publication retries occur at the coordinator’s normal publication checkpoints; no additional scheduler is introduced. A zero Vercel CLI exit confirms the deployment operation, not independent public HTTP verification. No source, policy, database, active draft, or reference-coherence logic is changed.
