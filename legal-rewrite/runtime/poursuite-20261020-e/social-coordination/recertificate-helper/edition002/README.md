Édition 002 : seule la référence C est remplacée par le dernier gel enregistré certificate-refresh/refreshed003/answer.json et son SHA exact. Les constantes de chemin sont ajustées à ce sous-dossier. Aucun élargissement des champs modifiables ; aucun mode capture ou stage exécuté. Le helper et le manifeste précédents restent immuables.

Helper borné aux cinq certificats R243-17, R243-18, R243-19, R243-59 et R243-59-6-A. Aucun appel de modèle, aucune publication, aucun enregistrement ni écriture DB. Le helper n’a pas été lancé en mode capture ou stage par son auteur.

La commande `capture` lit le vrai DB en `mode=ro`, transaction BEGIN, après le signal d’enregistrement E52. Elle impose l’égalité des sources, notes et XML DILA bruts aux preuves figées ; les corps, motifs et autres métadonnées des lignes canoniques doivent correspondre aux paquets approuvés. R243-59 doit réellement contenir le corps E entier attendu. Les cinq propriétaires de batch sont identifiés et leurs lignes comparées au DB. Le snapshot natif comprend les textes cibles entiers et leurs notes. Toute autre cible changée, autre que R243-59, bloque.

Les checks L243-7-6 ajoutés manuellement aux anciens snapshots mais absents des exigences natives sont exposés séparément comme retraits optionnels. Aucun autre retrait n’est permis. La preuve et les analyses législatives des nouveaux audits E restent immuables. Il ne s’agit pas de retirer cette dépendance juridique des audits.

Exemples à exécuter uniquement par root après inspection du script :

```sh
python3 legal-rewrite/runtime/poursuite-20261020-e/social-coordination/recertificate-helper/edition002/prepare_recertificates.py capture --out legal-rewrite/runtime/poursuite-20261020-e/social-coordination/recertification/capture001
```

La capture produit `capture.json`, `source.json`, `before-answer.json`, `reference-targets.json`, `db-records.json`, `batch-owners.json` et `approval.template.json`. Le dernier fichier porte `approved: false`. Root doit lire les vraies vues, rédiger trois analyses spécifiques de R243-59 (R243-17/-18/-59-6-A), approuver les retraits optionnels par identité et enregistrer un JSON d’approbation distinct. Champs : `version: 1`, `approved: true`, `approved_by: "root"`, `approved_at`, `capture_sha256`, `approved_optional_check_removals` et `analyses` (objets `key`, `target_key`, `assessment`, au moins 80 caractères chacun).

```sh
python3 legal-rewrite/runtime/poursuite-20261020-e/social-coordination/recertificate-helper/edition002/prepare_recertificates.py stage --capture legal-rewrite/runtime/poursuite-20261020-e/social-coordination/recertification/capture001 --approval /chemin/approbation-root.json --out legal-rewrite/runtime/poursuite-20261020-e/social-coordination/recertification/staging001
```

Le staging vérifie les empreintes de tous les fichiers de capture, l’approbation liée au SHA exact, les cinq états DB/notes/rawXML et toutes les lignes de batch ainsi que les cibles. Il reprend les analyses non modifiées, remplace les trois analyses autorisées et retire les seuls checks optionnels approuvés. `validate_answer`, `accept_checks` et `certificate_current` natifs doivent passer. Toute différence hors `reference_checks` et `reference_coherence`, même un certificat d’impact recalculé différent, bloque.

La sortie est un nouveau paquet `source.json`/`answer.json`/`reference-targets.json` et un reçu `staging.json`, compatible avec la préparation `register_pack.py`. Aucun commit n’est effectué. Juste avant inscription, root doit encore comparer sous le verrou d’écriture les gardes complètes de capture (dont rawXML, état/motifs et ligne de batch), en plus des gardes propres et de références déjà contrôlées par `register_pack`. Un changement entre staging et inscription reste bloquant. Ce helper ne prétend pas rendre ces étapes atomiques entre deux commandes.

Distinction après inscription : la fonction existante `review_prior.commit` peut ajouter ou actualiser `policy_review_id` et `prior_proposal_sha256`. Le reçu de staging annonce ces deux champs de provenance séparément ; ils restent strictement inchangés pendant le staging lui-même. Après inscription, root doit les comparer explicitement. Aucune égalité byte de tous les champs d’une ligne de batch après commit n’est promise : corps, impacts, raisons, notes et tous les autres champs hors références/provenance doivent cependant rester identiques.

Vérifications de l’auteur : compilation statique et sept tests sur les seules fonctions pures sélectionnées par AST (approbation, empreinte, retrait explicite, analyses, invariance des autres champs). Aucune importation/exécution du helper complet ni accès DB par ces tests. La vraie recapture et le staging attendent l’inspection et les commandes root.
