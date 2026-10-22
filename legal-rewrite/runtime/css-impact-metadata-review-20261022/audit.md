# Lot CSS L111-1 à LO111-3-6 : correctif de métadonnée uniquement

**L’échec est reproductible et se résout par une seule modification documentaire : L111-2-1 doit être classé `mixed`, puisque son bilan déclare déjà un transfert de financement et une complexité nouvelle.** Aucun changement de proposition, de raison, de notes de revue, d’effet, de citation, de référence, de source ou de garde n’est nécessaire pour lever ce défaut. La validation mécanique du candidat passe pour les douze articles ; aucune intégration n’a été effectuée.

Lot original : `runtime/exhaustive/jobs/review-securite-sociale-LEGIARTI000042223830-00001-resume-2uu0letr`. Son fichier de dernier échec indique l’essai3 et l’erreur « A financing transfer alone is not a tax or contribution cut ». Le validateur reproduit cette erreur sur le seul L111-2-1 du lot inchangé.

## Cause exacte et différence minimale

Dans `substantive_impact.py`, `ADDITIONS` comprend `complexity_added`. La branche de validation de `financing_transfer` refuse une liste contenant une coupe ou un ajout ; `mixed` exige au contraire un effet concret de coupe ou d’ajout. Ici la liste contient déjà, sous une même measure_id :

- `financing_transfer` : affectation d’une fraction de cotisations existantes à la capitalisation ; aucun taux ni montant total de prélèvement réduit n’est démontré.
- `complexity_added` : compte obligatoire, financement préalable, règles de droits et de gouvernance, gestion, contrôle et liquidation ; coûts administratifs inconnus.

La seule feuille modifiée est `/2/substantive_impact/classification` : `financing_transfer` → `mixed`. L111-2-1 n’a pas de `classification` parallèle au premier niveau ; aucun champ n’est ajouté. Le remplacement est effectué directement dans les octets du fichier, sans reformatage du reste. `file-byte-patch-proof.json` donne la position exacte et prouve l’identité du préfixe et du suffixe ; `exact-metadata-diff.json` confirme l’unique feuille modifiée.

`answer.metadata-only.json` est le candidat brut minimal. `answer.validated.json` contient en plus les certificats produits normalement par les validateurs existants. Ceux-ci sont des contrôles de passages et d’empreintes, sans approbation juridique indépendante. Les champs normatifs et analyses déjà rédigées y restent inchangés.

## Lecture et comparaisons des douze articles

Les douze sources entières, leurs notes, les douze previous_drafts entiers et leurs motifs/notes ainsi que les douze réponses du lot ont été lus. Les quatre cibles fournies dans `reference-targets.json` ont été lues en entier avec leurs notes et leur proposition : L1234-1, L1221-2, L1234-9 et L241-3. Les cinq projets de `policy.json` et les sections applicables travail, retraite, direction éditoriale, avantages préservés, suppressions/allègements et résultats substantiels de `coordination.json` ont été examinés. L’ensemble des fichiers de politique et de coordination reste conservé sans changement.

| Article | Statut de la réponse différée | Texte effectif identique dans le candidat | Classification finale |
|---|---|---|---|
| L111-1 | Maintien intégral | Oui | retained_necessary |
| L111-2 | Maintien intégral | Oui | retained_necessary |
| L111-2-1 | Proposition existante | Oui | **mixed** |
| L111-2-2 | Maintien intégral | Oui | retained_necessary |
| L111-2-3 | Proposition existante | Oui | coordination_only |
| LO111-3 | Maintien intégral | Oui | retained_necessary |
| LO111-3-1 | Maintien intégral | Oui | retained_necessary |
| LO111-3-2 | Maintien intégral | Oui | retained_necessary |
| LO111-3-3 | Proposition existante | Oui | mixed |
| LO111-3-4 | Proposition existante | Oui | coordination_only |
| LO111-3-5 | Maintien intégral | Oui | retained_necessary |
| LO111-3-6 | Maintien intégral | Oui | retained_necessary |

Pour un maintien, le texte effectif est la source entière, `proposed_xml` restant null. Les empreintes UTF-8 effectives avant/après, empreintes de propositions antérieures actives, gardes de source et comparaisons de tous les champs protégés sont dans `twelve-article-byte-comparison.json`. Les douze `reason`, `review_notes`, `reference_checks`, listes d’effets et mesures de transition sont inchangés. Une différence préexistante de sérialisation `<br>`/`<br/>` entre le champ de brouillon auxiliaire de L111-2 et son `previous_draft` a été lue et préservée ; le contrôle utilise bien le before-image `previous_draft`, qui correspond à la base et au lot actif. Les copies sources, notes et previous_drafts sont identiques à celles du lot original.

Cette identité concerne le correctif **par rapport à la réponse différée**. Une éventuelle intégration enregistrerait aussi les changements déjà proposés par ce lot par rapport aux brouillons actifs antérieurs, notamment huit maintiens et les réformes des quatre autres articles. Le dossier ne présente pas cette révision antérieure comme une simple modification de métadonnée du corpus actif.

## Gardes et contrôles exécutés

`before-images.current.json` conserve, pour chaque article, la ligne canonique complète, le XML ARTICLE, les notes, la ligne de brouillon actuelle, la ligne entière du lot actif propriétaire, leurs empreintes et la concordance avec les gardes originales. Capture en connexion SQLite `mode=ro`, `query_only=ON`, transaction de lecture, sous le verrou d’écriture existant pour assurer la cohérence lot/base. Le temps consigné inclut l’attente éventuelle de ce verrou ; aucune durée distincte de détention n’est revendiquée. Aucun slot de rédacteur n’est réservé.

| Contrôle existant ou preuve | Résultat |
|---|---|
| `validate_answer` sur la réponse originale | Erreur attendue sur L111-2-1 |
| `substantive_impact.validate` sur l’original | 11 passent, L111-2-1 reproduit l’erreur |
| `substantive_impact.validate` sur le candidat | **12/12** |
| `validate_answer` sur le candidat | **12/12**, douze certificats d’impact |
| Sources entières, notes, SHA et numéros | **12/12**, identiques aux gardes originales |
| Tuple de brouillon antérieur et SHA de proposition | **12/12**, identiques aux gardes originales |
| Empreinte de la ligne entière du lot actif | **12/12**, identique aux gardes originales |
| `reference_coherence.accept_checks` | Réussite, quatre cibles requises pour L111-2-1 |
| `reference_coherence.check_guards` | Réussite sur les cibles et politiques courantes |
| `validate_batches` sur le dossier isolé | **12 articles réellement inspectés**, un fichier |
| Politique figée du lot vs politique active | Identité |
| Nouvelle vérification fraîche des douze gardes | Réussite, `fresh-guards.json` |
| Fichiers du lot original | Tous inchangés |

La preuve exécutée figure dans `validation-execution.json`, les sorties `validation.stdout.txt`/`validation.stderr.txt` et `validation.json`. Le programme de validation impose que le contrôleur de lot ait réellement inspecté12lignes ; un répertoire vide ne pourrait produire une réussite. Les empreintes des modules et politiques utilisés sont dans `active-code-policy-hashes.json`.

Les diagnostics d’intégrité non bloquants restent visibles : nouveau renvoi L241-3 déjà couvert par les quatre cibles ; longueur9,47fois supérieure pour L111-2-3, qui conserve l’habilitation et reprend les garanties de preuve ; réduction normative explicite avec contreparties documentaires de LO111-3-3. Aucun de ces diagnostics n’est masqué ni transformé en approbation juridique.

## Avantages, nouvelles charges et limites

Les douze `benefit_check_required` valent false et restent inchangés : aucun `benefit_review` artificiel n’est ajouté. La non-régression de ce correctif est démontrée par l’identité des douze textes effectifs. Les cinq paragraphes santé du I et les deux paragraphes autonomie du III de L111-2-1 reproduisent exactement les paragraphes officiels. Les droits antérieurs de retraite, la réduction explicite des seuls droits futurs sur la fraction transférée, les objectifs de solidarité et le financement préalable sont conservés ; aucun gain fiscal n’est attribué au transfert.

L111-2-1 conserve son effet `complexity_added` et son analyse des traitements/coûts nouveaux. LO111-3-3 conserve les deux effets `obligation_removed` et `obligation_added` : la dispense facultative de reproduction doit être rapprochée de l’identification de chaque donnée et de la fourniture des documents. L111-2-3 reste `coordination_only`, sans nouveau gain supposé au titre de droits CRPA existants, avec coûts d’adaptation non chiffrés. Aucun solde net global n’est présumé.

Les versions et notes historiques sont préservées, notamment la borne1erjanvier2028 de L111-2 et les dates2022/2023. Six renvois locaux supplémentaires cités dans les analyses existantes ont été relus depuis la capture : LO111-4-1, LO111-10-2, R111-2, R111-3, R114-10 et R114-10-1. Ils confirment respectivement l’annexe des compensations au4°, les quinze jours francs de l’avis organique et les garanties de preuve/contrôle distinctes. Ils restent des pièces de revue supplémentaires, sans extension silencieuse des quatre gardes de référence exigées par le lot. Les dispositions CSP et CRPA extérieures seulement identifiées ne sont pas présentées comme intégralement certifiées par ce contrôle.

## Absence d’intégration

`review_prior.commit`, `register`, `_register` et tout outil de publication n’ont pas été appelés. Le catalogue, les politiques, les sources synchronisées, les notices actives, les lots actifs, la base et les limites des six rédacteurs ne sont pas modifiés. Aucun coordinateur n’est relancé. Le lot original reste une preuve intacte. Le plan futur est décrit dans `integration-plan.md` et doit conserver les gardes existantes, avec arrêt si elles ont changé.
