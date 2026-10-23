# Nouvelle interruption des réponses natives

Constat du 23 octobre 2026 vers 01h23 UTC (22 octobre en heure locale utilisateur). Le coordinateur 3122 est toujours unique ; le LaunchAgent reste enregistré. La configuration effective reste six places de nouveaux articles et une de relecture, sur un plafond autorisé de huit. Aucun processus, code actif, politique, contrôle d’admission ou réglage global n’a été modifié pendant ce diagnostic.

Les sept journaux de sessions observées ne prouvent aucune réponse de modèle actuelle. Tous présentent désormais leur en-tête Astra/medium, mais attendent la réponse. Les logs répètent `workspace routing discovery timed out`, des échecs de transport et des reconnexions bornées. La dernière acceptation de la cohorte est horodatée au 22 octobre à 23h25m42 UTC. Une session lancée, une configuration correcte ou un socket ne prouvent pas une reprise.

Cette nouvelle interruption ne doit pas être présentée comme la panne historique déjà résolue. Sa cause au-delà des erreurs natives de routage/transport n’est pas établie. Aucun statut d’authentification ou de quota n’est déduit de ces délais, aucun reset n’est consommé et aucun nouvel appel authentifié ou modèle de test n’a été lancé. Le diagnostic n’essaie pas de contourner la découverte de routage ou une protection. La supervision et les tentatives bornées existantes restent en place, sans second coordinateur ni interruption de lot.

## Disposition des articles

`deferred-disposition.json` rapproche les 22 résultats différés de la cohorte 3122, leurs refus conservés, leurs sources entières, la file persistante et une transaction SQLite en lecture seule. Dix-neuf lots de première passe représentent 456 identités toujours absentes de la table des propositions. Trois lots de relecture représentent 36 anciennes propositions dont la relecture reste en attente. Aucun de ces refus n’est converti en acceptation. L’ancien correctif d’une espace dans la citation d’impact de R5315-5 reste préparé, non intégré.

Les 492 identités ont toutes des empreintes de source, textes, NOTA et bornes de version concordantes avec les sources capturées de leurs lots. Elles sont toutes présentes dans la file persistante initiale ; cela ne prouve ni leur réadmission dans la file en mémoire déjà consommée, ni leur acceptation. Avant toute reprise, relire les résolutions et les états actuels. La reprise sûre doit reconstruire les travaux réellement ouverts depuis les sources et propositions courantes, sous les contrôles ordinaires, ou utiliser une réparation coordonnée complètement gardée. Ne pas rejouer une ancienne réponse à l’aveugle.

Le dernier statut canonique relu compte 1 851 premières passes et 5 103 anciennes propositions en attente de relecture. Ces dernières ne constituent pas à elles seules le décompte de toutes les relectures requises pour la clôture exhaustive.

## Audit et suite

Le pointeur global validé reste l’audit `global-reference-audit-20261022T222551Z`. Les compteurs observés n’ont augmenté que de 156 traitements depuis sa baseline, sous le seuil de mille. Aucune nouvelle capture volumineuse n’est requise à ce contrôle ; l’audit final frais restera obligatoire avant clôture. Plus de 24 Gio sont disponibles à la capture, donc aucun blocage d’écriture dû au stockage n’est établi ici.

La réaffectation future aux relectures reste hors ligne dans `review-reallocation-preflight-20261022T223009Z`, revue et testée, sans contrôleur opérationnel prêt. La file nouvelle n’est pas vide. Aucun transfert n’est déclenché pendant cet incident ou pendant des lots actifs. La capacité de seconde passe reste à une admission ; les six places de nouveaux articles ne sont pas transférées. La période de panne doit être exclue de toute comparaison de débit.

Les originaux des échecs restent conservés ; les copies de logs, en-têtes natifs et sources de cette capture sont accompagnées d’empreintes. Aucun texte n’est déclaré achevé, aucune cohérence sémantique globale ou validation par juriste n’est déduite du contrôle technique. Le suivi reste actif jusqu’à la clôture vérifiée de tous les textes et annexes. Une résolution de cette panne ne sera annoncée qu’après de nouvelles réponses natives distinctes puis des lots effectivement acceptés.
