# Revue du correctif de classification — 23 octobre 2026

## Constat reproduit

Le coordinateur 3122 a mis son événement STOP après travail-00472. Son
diagnostic natif terminal est « workspace routing discovery timed out ».
L'ancienne expression régulière a pourtant retrouvé trois occurrences de
« quota » dans les derniers caractères de la politique juridique imprimée
dans stderr. Aucun refus d'authentification ou d'accès n'est établi par ce
diagnostic. Le reçu de métrique `blocked_auth_or_usage` est conservé comme
résultat technique historique, pas comme preuve de la cause annoncée.

Le fichier stop-request historique appartient à 18713 ; il ne décrit pas cet
arrêt. Aucun signal n'a été adressé à 3122 par ce contrôle. Le lot travail-00474
a fini normalement : ses 24 enregistrements, cinq champs, sources, NOTA,
bornes de version, lot, intention et registre concordent en transaction ro.
Il s'agit d'une réponse puis d'une acceptation particulière ; les sept
sessions ne sont pas pour autant déclarées rétablies.

## Changement proposé, non installé

Le seul candidat actif envisagé est `run_exhaustive.py` dans ce dossier.
Il ajoute `native_access_failure` et remplace l'analyse de toute la fin du
transcript par celle du suffixe des diagnostics natifs terminaux de stderr.
Le pied « tokens used » est reconnu. Les erreurs d'accès explicites restent
bloquantes, y compris 401/403/429 et les limites d'utilisation explicites.
Une erreur inconnue conserve exactement les trois tentatives ordinaires et
le statut non accepté. Aucun résultat de modèle n'est rejoué ni accepté.

Le diff du candidat n'altère aucun validateur de source, notes, version,
avantage, impact, renvoi, politique, modèle, réservation ou enregistrement.
Les autres fonctions sont identiques au baseline. Un transcript textuel ne
constitue pas une preuve structurée d'authentification ; ce filtre limite la
classification aux formes terminales reconnues, sans certifier une cause
pour les erreurs inconnues.

## Validation et limites

105 tests passent contre le candidat, production SQLite interdite. Les huit
tests dédiés incluent le journal original et deux parcours avec bases
isolées : trois échecs de routage restent différés, le lot suivant est
accepté ; un vrai refus d'accès arrête immédiatement, sans lot suivant.
Les suites existantes couvrent réservations, modèle natif, supervision,
publication, atomicité et reprises avec cibles modifiées. Les tests ne
créent aucun agent de modèle. Les processus de test de supervision sont
locaux et distincts des agents du chantier.

Le premier passage incomplet est conservé : une première assertion avait
une fixture au mauvais niveau de dossier ; le premier passage complet
rencontrait une proposition témoin identique à sa source et l'interdiction
sandbox de lire ps. Fixtures corrigées, puis les mêmes 105 tests ont été
rejoués avec l'inventaire OS permis : zéro erreur, zéro échec. Ces erreurs
de test ne décrivent aucune donnée de production.

## État courant et reprise gardée à réaliser

La pause `runtime/supervision/disabled` est créée exclusivement par ce
contrôle sous supervisor.lock, avec propriétaire UUID et octets archivés
dans pause-intent.json. Elle empêche seulement une relance ; elle n'arrête
pas 3122. Aucun verrou rédacteur n'est tenu pendant cette attente.
À system-check.json, les agents natifs ont fini, 3122 publie encore son
checkpoint via publish_snapshot.py/build_reader.py. Ne pas l'interrompre.

Après la sortie effective de ce PID et de ses descendants, rafraîchir
l'inventaire OS, le reçu de sortie et sa temporalité par rapport au dernier
constat vivant, les verrous, le propriétaire exact de la pause et l'état des
enregistrements. Le STOP dû au faux classement est attendu dans ce reçu ;
ce n'est pas une fin exhaustive de file. Le lstart du PID est converti
explicitement depuis l'heure locale vers 20:54:15 UTC ; le manifeste du run
a été écrit six secondes plus tard, et n'est pas assimilé à sa naissance.

Sous gardes de propriétaire et verrous superviseur/coordonateur/rédacteur/
réservations manuelles, conserver le baseline, vérifier le diff et toutes
les empreintes actuelles, remplacer atomiquement ce seul runner si encore
identique au baseline, puis relire son empreinte. Ne pas modifier les
articles, politiques ou limites effectives 7/new6/review1. Les réservations
manuelles doivent être connues et prises en compte. Un changement intervenant
ou une identité inconnue bloque ; aucun inconnu n'est converti en zéro.

Retirer seulement notre pause sous comparaison exacte des octets/propriétaire
après intention durable de reprise. La seule supervision déjà enregistrée
assure ensuite une unique reprise. Adopter son nouveau PID, vérifier ses
réponses natives Astra/Moyen puis des lots réellement acceptés. La reprise
ordinaire reconstruit la file depuis les sources courantes manquantes et
exécute ses contrôles d'enregistrement complets : ne jamais rejouer les
réponses de ce PID, ni l'ancien activate.py. Si une garde échoue, la pause
reste possédée et la cause précise est conservée pour résolution.

La réconciliation ro actuelle retrouve exactement les 795 absences : 696
dans 34 travaux non acceptés (29 nouveaux lots et cinq lots de relecture),
96 dans quatre nouveaux lots non admis, trois réserves documentaires.
Les 58 identités de relecture des travaux non acceptés restent pending,
incluses dans les 5054 anciennes relectures ouvertes. Le zéro de queue en
mémoire résulte du STOP ; il ne justifie aucune réallocation aux relectures.
Les empreintes et dispositions devront être relues au moment de la reprise.

## Interaction avec les autres préparations

Le paquet de réallocation à huit relecteurs demeure NOT_READY_FOR_ACTIVATION.
Ce correctif ne l'intègre pas. Dès qu'il sera installé, les anciens pins de
baseline de ce runner seront périmés : rebaser et revoir séparément le
candidat scellé et les helpers avant tout usage ; ne pas modifier leurs
manifestes publiés pour faire passer une garde. La reconstruction ordinaire
des différés ne requiert aucun ancien helper de réenregistrement.

L'audit global reste dû et différé : environ 5,4 Gio disponibles, sous les
9 Gio requis pendant les écritures. Aucun snapshot volumineux, compression
du courant, nettoyage de données extérieures ou réduction de validation.
Cette revue technique n'est ni une revue juridique ni une clôture du corpus.
