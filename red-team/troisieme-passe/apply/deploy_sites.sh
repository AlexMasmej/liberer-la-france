#!/bin/sh
# Rebuild and redeploy the five libererlafrance sites with the project's own publication tool.
# Authorized by the author for every future redeploy (29 October 2026).
cd /Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc || exit 1
exec python3 -B legal-rewrite/publish_snapshot.py --deploy
