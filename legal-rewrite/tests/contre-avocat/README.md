# Tests d'acceptation « contre-avocat » (Code du travail)

Chaque script vérifie qu'une issue est résolue dans les lots `legal-rewrite/batches/automatic-travail`
et `legal-rewrite/batches/travail`, comparés au texte en vigueur de la base LEGI `corpus.sqlite`.
Code de sortie **0 = issue résolue** ; 1 = au moins un critère échoue (chaque critère est affiché PASS/FAIL).

| Script | Issue | Ce qu'il vérifie |
|---|---|---|
| `travail_02.py` | #2 | Préavis de licenciement (L1234-1, L1234-8, L2253-3, L2254-1) : retour à un préavis lié à l'ancienneté, compatible avec la Charte sociale européenne et la convention OIT C158, cités dans `reference_checks`. |
| `travail_04.py` | #3 | Dispositions transitoires : aucune clause temporelle/transitoire introduite dans les propositions, transitoires d'origine regroupées dans `legal-rewrite/transition/loi-contrat-unique.json`, pas de « loi portant… » introduite, abrogations totales (`full_repeal`) sans texte de remplacement. |
| `t04_patterns.py` | #3 | Module partagé de `travail_04.py` (motifs, normalisation). |
| `make_t04_fixture.py` | #3 | Régénère la référence figée `travail_04_baseline_sentences.json` (+ `_ids.json`) requise par `travail_04.py`. |
| `common.py` | — | Chargement des lots et de la base. |

## Lancer

Depuis la racine du dépôt :

```sh
# 1. Reconstituer la base (ignorée par git) si besoin
cat legal-rewrite/corpus.sqlite.gz.part* | gunzip > legal-rewrite/corpus.sqlite
# ou pointer vers une copie existante : export CONTRE_AVOCAT_CORPUS=/chemin/vers/corpus.sqlite

# 2. Référence figée de travail_04 : à générer UNE fois sur le snapshot de référence cac48419
git worktree add /tmp/ref cac48419271390c9d4f47917ffee30c1bd7f9c2a
#   (copier ce dossier dans /tmp/ref/legal-rewrite/tests/contre-avocat s'il n'y est pas)
python3 /tmp/ref/legal-rewrite/tests/contre-avocat/make_t04_fixture.py   # attendu : « 3030 5813 »
cp /tmp/ref/legal-rewrite/tests/contre-avocat/travail_04_baseline_*.json legal-rewrite/tests/contre-avocat/

# 3. Tests
python3 legal-rewrite/tests/contre-avocat/travail_02.py
python3 legal-rewrite/tests/contre-avocat/travail_04.py
```

Au snapshot cac48419 (LEGI_20261018), les deux tests échouent (0/6 et 0/5), ce qui est attendu.
