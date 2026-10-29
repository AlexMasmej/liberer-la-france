# Libérer la France

Sources des cinq sites et propositions indépendantes de simplification du droit français, portées par Alex Masmej avec ses agents IA.

Snapshot of the five websites and their shared legal drafting project, exported on 20 October 2026.

| Site | Published files |
| --- | --- |
| Libérer la retraite | `sites/liberer-la-retraite/dist/` |
| Libérer le logement | `sites/liberer-le-logement/dist/` |
| Libérer le revenu | `sites/liberer-le-revenu/dist/` |
| Libérer l’entreprise | `sites/liberer-lentreprise/dist/` |
| Nouveau droit du travail | `sites/nouveaudroitdutravail/dist/` |

Each `dist/` directory contains a static website, including its available assets and downloads. The retirement website also hosts the shared corpus reader and code downloads. Existing Vercel project bindings are retained under each site's `.vercel/` directory. Pushing this snapshot does not configure automatic deployment.

`legal-rewrite/` contains the drafting scripts, tests, batches, archived revisions, source attachments, and available research/validation state. See its README for provenance, editorial rules, rebuilding, and limitations. The legal rewrite is unfinished; these materials are not represented as lawyer-validated or a completed rewrite.

## Seconde passe complète

La [publication de la seconde passe](snapshots/20261029T035156Z-second-pass-complete/README.md) rassemble les 30 314 secondes passes terminées et vérifiées, la base active sauvegardée de façon cohérente et les textes finaux. Les sept derniers articles ont été rapprochés et relus avec GPT-6.1 Sol High. Le suivi dédié est arrêté.

Les lots courants et notes restent consultables sous `legal-rewrite/`. L’état complet se restaure selon le manifeste du nouvel instantané, qui prolonge le précédent sans effacer l’historique. Les trois réserves documentaires, les questions de cohérence et la troisième passe demeurent ouvertes ; ceci ne constitue pas une validation par juriste. Les issues ouvertes sont conservées.

## Methodological context for the planned arXiv preprint

[CODEX_HANDOFF.md](CODEX_HANDOFF.md) is a public, dated account of how this AI-assisted legal rewriting project was carried out: official-source provenance, editorial decisions, models and prompts, the agent pipeline, validation controls, revision history, problems encountered, published outputs, and unresolved questions. It provides supporting context for preparing the planned arXiv preprint and for understanding or continuing the research.

It describes the completed second-pass edition of 29 October 2026 UTC, with a [frozen snapshot](snapshots/20261029T035156Z-second-pass-complete/README.md); later third-pass corrections are separate. This public edition omits machine-specific paths and private operational records. It distinguishes documented results from unknowns and is neither the preprint manuscript nor a claim of legal certification or exhaustive human review.

## Restore the databases

The SQLite databases exceed GitHub's ordinary file limit. Consistent SQLite snapshots are compressed and split into parts below 50 MiB. Restore them with Python 3.11 or later:

```sh
python3 restore-databases.py
```

The restoration verifies SHA-256 checksums and refuses to replace existing databases. `database-parts.json` lists the files and checksums. After restoration, follow `legal-rewrite/README.md` to build or continue work.

## Export scope

The export includes the available files from `sites/` and `legal-rewrite/`. Credentials, environment files, Python caches, locks, database sidecars, detected secret-bearing files, and local memory-service account/operational records are omitted. `export-exclusions.json` records omitted paths. Unrelated video material and the read-only synced project folder are outside this website export.

## Previous interim snapshot — 28 October 2026

The [user-requested snapshot](snapshots/2026-10-28-user-request/README.md) records the latest captured websites and drafting archive as a verified differential overlay on commit `cac48419271390c9d4f47917ffee30c1bd7f9c2a`. Earlier files in this repository remain preserved; use the snapshot manifest to restore the captured current state.

This is an unfinished research and drafting snapshot: 30,314 entries addressed, 3 documentary entries pending and 2,548 second passes still awaiting review at capture. Remaining semantic coordination and final source/reference checks are not complete. The latest local website build passed its technical checks, but its deployment failed; this GitHub snapshot does not claim that build is live or lawyer-approved.
