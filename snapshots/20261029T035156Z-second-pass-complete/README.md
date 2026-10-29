# Seconde passe complète — instantané vérifié

Les **30 314 secondes passes sont terminées**. Le rapprochement final des sept articles a fait l’objet d’une nouvelle relecture native **GPT-6.1 Sol High**, avec tous les contrôles ordinaires. La vérification de clôture a lié les 30 314 identités à 2 894 lots natifs réellement acceptés, leurs sessions, réponses, reçus, archives et valeurs enregistrées. Le suivi dédié à cette seconde passe a été supprimé.

Le projet juridique global reste **inachevé** : les trois réserves documentaires, les qualifications de cohérence et de références et la revue finale de troisième passe restent ouvertes. Les douze candidats CSS ne sont pas intégrés ; readiness=false. Aucun juriste n’a validé ces travaux. Les contrôles de seconde passe ne constituent pas une garantie de conformité juridique ou de zéro contradiction.

## Contenu et vérification

- `second-pass-acceptance.json` et `second-pass-acceptance.md` : preuve datée de clôture et limites. Les travaux ultérieurs de références et de réserves restent distincts.
- `snapshot.json` : manifeste des fichiers ajoutés/remplacés, fichiers réutilisés, exclusions, fichiers différés, sauvegarde cohérente et état local des sites au point de capture.
- `payload.tar.gz.partNNN` : superposition vérifiée, découpée sous la limite GitHub ; leurs empreintes individuelles et celle du flux complet figurent au manifeste.
- Les lots numériques courants, le registre, l’inventaire de seconde passe, les scripts courants et les notes de contradictions sont aussi consultables directement sous `legal-rewrite/`.

La base active a été sauvegardée avec l’API SQLite, puis rapprochée des cinq champs de chacun des **30 314 articles** dans les **1 449 lots propriétaires**, sous les verrous ordinaires. Les cinq sites ont été reconstruits et vérifiés localement avant capture. Cette publication GitHub ne déclenche aucun déploiement.

Des assemblages préliminaires ont été interrompus avant d’entamer la réserve d’espace disque. Leurs parties sont conservées localement. La capture centrale cohérente déjà vérifiée a été réutilisée ; les copies supplémentaires de bases historiques non indispensables à la restitution de la seconde passe sont explicitement différées. Leurs originaux locaux et les archives déjà publiées sont préservés.

## Restauration

Cet instantané prolonge `snapshots/2026-10-28-user-request`, publié au commit `0703487dcbee110f60eb9b6356d0208bc2066235`. Il ne remplace aucun historique Git.

Préparer un **nouveau checkout séparé** au commit initial `cac48419271390c9d4f47917ffee30c1bd7f9c2a`, disposer des deux dossiers d’instantanés et de leurs parties, puis lancer avec Python 3.11 ou ultérieur :

```sh
python3 /chemin/vers/cet-instantane/restore-snapshot.py --destination /chemin/vers/checkout-initial
```

L’outil restaure d’abord la superposition précédente, vérifie tous les fichiers réutilisés, les parties et les membres de la nouvelle archive, puis applique celle-ci. Si la superposition précédente est déjà restaurée, ajouter `--base-already-restored`. Prévoir plusieurs dizaines de Go pour la base historique restaurée et les données décompressées. Ne jamais restaurer sur les originaux de rédaction. Aucune suppression de fichier n’est inférée de l’absence d’un chemin.

Les sources synchronisées restent intouchables. Conversations, transcriptions natives, secrets, fichiers d’environnement, caches, verrous et comptes locaux sont exclus. `jobs-before-policy.tar.gz` reste exclu et préservé localement. Les exclusions et fichiers différés sont documentés sans prétendre qu’ils ont été publiés ou vérifiés juridiquement.

## Réserves et troisième passe

Lire `legal-rewrite/notes-contradictions/INDEX.md` et `legal-rewrite/GUIDE-TROISIEME-PASSE.md`, puis confronter chaque dossier à la version effectivement restaurée. Le corpus de référence est figé au **18 octobre 2026**. Les trois réserves documentaires sont D351-9 (60/62 ans), la figure de l’annexe I CSS R434-32(7), et les CERFA 30-0812/30-0813 de l’article 15 de l’annexe IV CGI.

Les alertes automatiques et certificats historiques ne sont pas autant de contradictions confirmées. Conserver les avantages, droits acquis et réformes décidées. Les propositions de troisième passe restent séparées. **Aucune issue GitHub ouverte n’est modifiée ou fermée par cette publication.**
