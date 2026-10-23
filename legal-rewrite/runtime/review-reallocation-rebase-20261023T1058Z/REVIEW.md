# Rebase du paquet de réallocation, sans installation

Le baseline du runner contient désormais le correctif des faux signaux de quota, installé séparément après la sortie de 3122. Le paquet scellé f8cbed… reste intact ; son ancien baseline ne correspond plus au code actif et ne doit pas être forcé.

Ce nouveau dossier reprend les six modules candidats, avec le même correctif de classification incorporé dans le runner candidat. Les autres cinq modules sont identiques au candidat d'origine. Le baseline est recopié depuis les fichiers actifs vérifiés. Les fonctions de validation et d'enregistrement, et native_access_failure, sont identiques entre le nouveau baseline et le candidat.

35 tests ciblés passent (27 de réallocation et huit de classification), ainsi que 74 régressions. Les bases de production sont interdites ; aucun modèle n'est invoqué. Les fixtures ne certifient aucune cohérence juridique de production.

État : NON PRÊT POUR ACTIVATION. Aucun des six modules n'est installé. Le contrôleur d'origine conserve son refus inconditionnel avant collecte ou mutation. Les composants de gardes 0835Z et la réconciliation courante employée pour la réparation ciblée sont des travaux réutilisables, mais leur généralisation et leur raccordement au contrôleur de transfert, la revalidation après interruption et les attestations tardives restent à achever, revoir et tester. Aucun des cinq blocages du contrôleur n'est déclaré levé par ce rebase.

La nouvelle file ordinaire doit terminer les 792 premières passes accessibles, y compris les différés. Aucune admission de relecture supplémentaire, aucune bascule pendant les lots actifs. Les sources documentaires retenues et la convergence des renvois restent ouvertes.
