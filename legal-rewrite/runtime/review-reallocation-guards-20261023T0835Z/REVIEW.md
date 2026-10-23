# Gardes préparées hors ligne, non intégrées

Ces fonctions n'ont aucun chemin de lancement, d'arrêt, d'installation,
d'enregistrement ou de modification de configuration. Le contrôleur précédent
reste inchangé et son backend de production refuse toujours toute activation
avant collecte. Les six modules candidats scellés ne sont pas modifiés.

## Apport vérifié

`terminal_new_queue` confronte la file complète du PID, son plan, les compteurs,
tous ses résultats new terminaux et les sources réellement assignées à chaque
lot. Il lit la disposition actuelle des identités en SQLite `mode=ro`, dans une
transaction. Les cas deferred absents sont retournés explicitement EN ATTENTE.
Un accepted/skipped doit correspondre à une entrée présente sous la bonne
empreinte de source. Un skip légitime du runner n'a pas de dossier de lot ; il
doit néanmoins avoir toutes ses identités enregistrées. Les relectures en cours
de validation dans le coordinateur ne sont pas déclarées inactives sur la seule
absence d'un processus modèle. L'ancien horodatage d'admission n'est jamais
réécrit ; il peut être ancien seulement si ce rapprochement complet réussit.
La stabilité des fichiers est revérifiée à la fin de la lecture. Les neuf
recueils sont exigés ; les champs inconnus, troncatures, doublons, booléens à la
place de nombres, changements de sources et incohérences bloquent.

`successful_exit` relit le run et le reçu effectifs et vérifie PID, début,
observation du processus encore vivant, fin, mtime du reçu et sortie naturelle
réussie. Un reçu historique, futur ou d'une autre génération ne suffit pas.

`native_launch_attestation` vérifie avant et après collecte l'ensemble explicite
des pins de code et de politiques ainsi que l'appartenance du catalogue de
compagnons. Il confronte le reçu de lancement à l'unique processus observé et
son run. Chaque processus modèle doit avoir son propre enregistrement de durée,
son dossier, son journal natif et une réponse réellement commencée en
gpt-6-astra/medium, avec session distincte. Le parseur natif épinglé est chargé
en mémoire, sans cache écrit. Cette attestation ne lance rien et ne prouve ni
la capacité simultanée maximale ni un gain de débit.

## Revue des refus et réparations

La première exécution des tests a révélé un problème de chemins de fixtures
macOS `/var` versus `/private/var`. Les racines temporaires sont désormais
résolues avant la construction des commandes et des URI SQLite. Le journal
initial est conservé. La revue a ensuite ajouté des refus concernant les
booléens, la substitution des identités dans une file, l'origine exacte des
sources des lots, la stabilité des preuves, l'appartenance du catalogue, les
symlinks, le dossier natif et la génération de processus. Les tests couvrent ces
régressions avec de vrais petits fichiers/DB isolés et le vrai parseur natif.

## Limites impératives avant toute utilisation opérationnelle

1. L'intégration à un collecteur OS frais et au contrôleur n'est pas faite. Les
   identités de processus reçues par ces fonctions doivent venir de la lecture
   native effective, et non d'un JSON fourni. Le prototype existant stocke un
   `lstart` textuel ; sa conversion temporelle, sa base UTC explicite et son
   rattachement au run doivent être implémentés et testés. Ne pas présumer que
   l'heure du run est exactement l'heure de création du processus.
2. Le rapprochement complet des propriétaires, batches/registry, intentions et
   complétions, documents/sources/NOTA/versions, avantages, impacts, cibles et
   dernières avant-images reste à implémenter. Le simple fait qu'une ligne
   existe dans drafts n'est jamais sa validation. Aucune garde de renvoi n'est
   rajeunie par ces fonctions ; les certificats périmés restent à reprendre.
3. La re-collecte réelle de ce rapprochement après interruption des phases
   RECONCILED/installée/configurée n'est pas implémentée. Les anciens reçus
   ne doivent pas être réutilisés comme autorisation permanente.
4. La reprise tardive du contrôleur doit être raccordée à l'attestation native,
   à la lecture fraîche et unique des processus et aux pins exacts de sa phase.
   Une session encore en démarrage exige une nouvelle observation bornée ;
   elle ne permet jamais de lancer un second coordinateur.
5. Le point sûr, le drainage naturel, les verrous, la pause propriétaire et les
   tests d'interruption de l'orchestration complète restent obligatoires.
   Aucun de ces prérequis n'est levé par la réussite des tests de composants.

Aucun appel à ces nouveaux collecteurs n'a été effectué sur la production.
Les tests n'ouvrent que des bases temporaires avec lecture ro instrumentée,
sans modèle, CLI natif, quota, snapshot ou verrou rédacteur de production.
Ces preuves ne sont ni une activation ni une validation juridique.
