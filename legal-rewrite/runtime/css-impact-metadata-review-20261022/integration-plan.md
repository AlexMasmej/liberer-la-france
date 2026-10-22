# Plan d’intégration ultérieure — non exécuté

Ce dossier prépare une seule correction de classification dans la réponse différée ; il n’autorise pas une écriture active. Le point d’intégration reste `review_prior.commit`, avec les douze sources et `previous_draft` du lot original et le `reference-targets.json` original inchangé.

1. Attendre un point où le verrou de coordinateur existant `runtime/exhaustive/coordinator.lock` est disponible, ou confier l’opération à son propriétaire au point d’intégration prévu. Une procédure externe doit demander ce verrou sans attente et s’arrêter s’il est occupé. Ne pas arrêter ou relancer le coordinateur et ne pas réserver de slot pour obtenir ce point.
2. Vérifier les empreintes du dossier, l’identité des fichiers originaux, la politique avec `run_exhaustive.policy_is_current`, les douze différences textuelles nulles et l’unique feuille de métadonnée. Charger `answer.metadata-only.json`, `original-job/source.json` et `original-job/reference-targets.json` ; ne pas reconstruire ni rafraîchir les anciennes gardes pour faire passer l’opération.
3. Exécuter à nouveau `validate_answer` sur une copie du candidat, puis `reference_coherence.accept_checks`. Vérifier les gardes de référence courantes en lecture seule. Toute différence de cible, politique, source, note, brouillon ou ligne de lot appelle un arrêt et une nouvelle revue ; aucune garde n’est effacée ou ignorée.
4. Après autorisation d’intégration et sous le verrou de coordinateur, appeler exactement `review_prior.commit(rows, expected, reference_snapshot=reference_snapshot)`. Ne pas prendre au préalable `writer_lock`, qui n’est pas réentrant : `commit` le prend lui-même et le garde jusqu’au contrôle de propriétaire, aux comparaisons du tuple complet de brouillon et du SHA de ligne de lot, à l’archive durable, puis à l’enregistrement sous transaction existante. Le second passage du verrou pour le manifeste de revue reste celui du code actif.
5. Relire les douze lignes enregistrées, leurs propriétaires, les archives de révision et certificats ; comparer leurs propositions, raisons et notes au candidat validé et leurs sources/notes aux before-images. Faire produire le suivi de progression et le traitement du lot différé par le chemin du coordinateur, sans modifier le dossier original de l’échec.

L’appel central futur, après les contrôles ci-dessus, est :

```python
rows = run_exhaustive.validate_answer(copy.deepcopy(candidate), expected)
reference_coherence.accept_checks(rows, expected, reference_snapshot)
review_prior.commit(rows, expected, reference_snapshot=reference_snapshot)
```

La fonction archive les brouillons antérieurs avant de remplacer un lot ; elle contrôle le SHA de source et l’ensemble des cinq champs antérieurs (`source_sha256`, `status`, `proposed_xml`, `reason`, `review_notes`) ainsi que `proposed_sha256` et `batch_row_sha256`. Le candidat n’altère aucune de ces valeurs attendues. Un état courant modifié doit donc rester bloquant.

Les ajouts automatiques de certificats, `policy_review_id` et `prior_proposal_sha256` relèvent du chemin existant. La révision de douze réponses peut enregistrer les choix déjà présents dans le lot différé par rapport aux anciens brouillons ; l’unique modification nouvelle de ce correctif est la classification d’impact de L111-2-1. Aucune publication, déploiement, modification de politique ou nouvelle validation assouplie n’est incluse dans ce plan.
