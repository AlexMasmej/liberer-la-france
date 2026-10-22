Ce script conserve le dossier d’échec original. Sans option, il vérifie seulement ; `--apply` est réservé au point sûr géré par le superviseur, après la fin normale de l’ancien coordinateur et avant de remplacer le code actif.

Le verrou du coordinateur est pris sans attente. S’il est occupé, le script sort avec le code 3, sans import actif, sans verrou de rédaction ni écriture active. Une garde modifiée entraîne le code 2 et une réserve, sans régénérer les justifications ou les instantanés. Les deux manifestes de preuves restent distincts ; le manifeste initial est immuable.

Après douze validations, les empreintes des sources/notes/XML entiers, des propositions précédentes, des propriétaires de lots, des politiques et des quatre renvois figés doivent correspondre. Les six références supplémentaires lues pendant l’examen doivent également rester identiques. La seule modification du dossier différé est `/2/substantive_impact/classification`, de `financing_transfer` à `mixed` ; les effets et obligations ajoutées sont conservés.

En mode application, une intention locale lie les preuves originales et l’archive attendue. Le seul commit est `review_prior.commit(validated, original_sources, reference_snapshot=original_snapshot)`, sans verrou de rédaction extérieur à cet appel. Le script ne modifie aucune source canonique et ne fait aucun appel de processus.

Une reprise après commit exige les douze lignes DB finales exactes, l’intention et l’archive exactes. Elle ne rappelle pas le commit. Elle peut rapprocher seulement les miroirs de lots et de registre reconnus comme anciens ou nouveaux, et terminer les statuts du manifeste de revue en préservant les autres lignes. Un état DB partiel, un lot inconnu, une garde périmée ou une résolution contradictoire provoque un refus. Une interruption avant commit ayant déjà changé les lots reste réservée à un examen explicite.

La preuve `integration-complete.json` précède l’ajout atomique à `failed-job-resolutions.json`. Ce dernier est relu et fusionné sous le verrou de rédaction existant, sans perdre d’autres entrées. Une seconde exécution vérifie les preuves et n’ajoute pas de doublon. Le dossier d’échec original est revérifié intégralement.

Cette préparation ne réalise aucune intégration. Le dry-run exécuté pendant l’activité du coordinateur doit refuser son verrou ; il ne prouve pas encore l’acceptation des gardes au futur point sûr. Les douze validations exécutées précédemment sont conservées dans le manifeste initial.
