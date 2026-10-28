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

## Restore the databases

The SQLite databases exceed GitHub's ordinary file limit. Consistent SQLite snapshots are compressed and split into parts below 50 MiB. Restore them with Python 3.11 or later:

```sh
python3 restore-databases.py
```

The restoration verifies SHA-256 checksums and refuses to replace existing databases. `database-parts.json` lists the files and checksums. After restoration, follow `legal-rewrite/README.md` to build or continue work.

## Export scope

The export includes the available files from `sites/` and `legal-rewrite/`. Credentials, environment files, Python caches, locks, database sidecars, detected secret-bearing files, and local memory-service account/operational records are omitted. `export-exclusions.json` records omitted paths. Unrelated video material and the read-only synced project folder are outside this website export.

## Latest interim snapshot — 28 October 2026

The [user-requested snapshot](snapshots/2026-10-28-user-request/README.md) records the latest captured websites and drafting archive as a verified differential overlay on commit `cac48419271390c9d4f47917ffee30c1bd7f9c2a`. Earlier files in this repository remain preserved; use the snapshot manifest to restore the captured current state.

This is an unfinished research and drafting snapshot: 30,314 entries addressed, 3 documentary entries pending and 2,548 second passes still awaiting review at capture. Remaining semantic coordination and final source/reference checks are not complete. The latest local website build passed its technical checks, but its deployment failed; this GitHub snapshot does not claim that build is live or lawyer-approved.
