# Proposition d’intégration hors ligne — CCH

**Prête à examiner, non activée. Aucun des quatre articles n’est déclaré traité.** Les deux vrais verrous ont été exécutés sur les copies épinglées, sans substituer de faux validateurs et sans désactiver les contrôles d’impact, d’avantages, de sources ou de renvois.

## Contenu et résultats

- `baseline-manifest.json` épingle les sources de code et les petits fichiers de configuration requis par leurs imports. `baseline/` contient ces copies inchangées. Aucun corpus exporté ni fichier SQLite live n’a été copié.
- `candidate/` contient le même environnement, avec exactement trois fichiers de production proposés : `run_exhaustive.py`, `register_batches.py`, `template_fields.py`. Les trois fichiers `.patch` rendent les modifications explicites. **Ne jamais déployer le dossier candidate entier** : les autres fichiers sont des dépendances de test et `test-batches/` contient intentionnellement des cas invalides.
- `deployment-manifest.proposed.json` contient les SHA avant/après des seuls fichiers à envisager pour la bascule. Au moment de cette préparation, aucun des fichiers actifs épinglés ne différait de la baseline.
- `test_real_gates.py baseline` : 6 résultats conformes. Les deux lots échouent dans chacun des deux vrais verrous, exactement pour les champs officiels ; les deux audits de renvois passent.
- `test_real_gates.py candidate` : **149 résultats conformes**. Les quatre propositions entières passent individuellement et en lots dans `run_exhaustive.validate_answer` puis `register_batches.validate_batches`. `reference_coherence.accept_checks` passe pour les deux lots avec le vrai catalogue copié et les snapshots conservés.
- Les tests négatifs passent par ces fonctions réelles : marqueurs nouveaux, entités HTML, source/notes modifiées, hash invalide, HTML interdit, impact invalide, absence d’analyse d’avantage là où requise, valeur de capital inventée, champs supprimés ou dupliqués, nom/siège/délai inventés, clause de capital déplacée, titres de clauses supprimés. Tous sont rejetés.

Les appels à `validate_batches` utilisent uniquement un SQLite **en mémoire**, contenant les quatre sources et documents minimaux, aucune ligne de draft existante. Il n’y a aucun appel à `register`, `_register`, `open_db` sur une base live, aucun commit persistant, aucune publication et aucun lancement d’agent. Les imports, contrôles et calculs de certificats sont les fonctions réelles. Les fichiers JSON des résultats donnent les erreurs observées de chaque cas.

## Fonction commune proposée

La seule exception s’applique aux cinq intervalles `[…]` des versions sources exactes de LEGIARTI000045646952 et LEGIARTI000045646995. Le registre est une constante embarquée, non une déclaration acceptée depuis le rédacteur. Il épingle identité, `source_sha256`, SHA du XML brut, SHA des notes, clause 5 complète et positions exactes des champs. Les deux empreintes source ont des objets différents et sont conservées séparément.

La clause 5 doit être intégralement inchangée ; ses bornes doivent être uniques. La séquence complète des titres de clauses doit être identique à la source : une clause 5 déplacée n’est plus admise. Les autres blancs de dénomination, siège et, pour l’annexe II, « préavis de mois » sont explicitement ancrés et ne peuvent être supprimés ni remplis. Tout autre marqueur restant est refusé par le motif le plus strict déjà employé par l’enregistrement. Le coordinateur adopte ainsi aussi le refus existant des variantes avec espaces et de `<placeholder>` ; aucune forme déjà interdite par l’enregistrement ne devient libre.

Aucun texte proposé n’est nettoyé ni modifié. Seuls les intervalles prouvés sont exclus de la recherche lexicale, après ces validations positives. Une valeur de capital inventée ne peut donc plus contourner le problème en supprimant les crochets. La fonction ne produit aucun statut de traitement.

Tous les autres contrôles restent textuellement inchangés dans les deux fichiers : version/identité, raisons et notes, avantage, impact et citations exactes, intégrité HTML, graphiques, tableaux, copie source, longueur, statut, détection de doublons et protections contre écrasement. Le raccordement n’ajoute aucun appel DB.

## Revue des quatre propositions entières

`text-integrity-audit.json` compare les dernières propositions avec les sources et avec les fichiers live des deux anciens lots : ils étaient inchangés depuis la copie du diagnostic. Les 16, 11, 13 et 15 clauses respectives (avec variantes 8A/8B et sous-clauses 6.1–6.3 quand applicables) restent en ordre ; les notes incorporées restent présentes. Les différences intégrales figurent dans `../articles/*/changes.diff` et ont été relues avec les sources.

18 unités de lignes contenant des champs authentiques ont été recensées. Toutes sont reproduites intégralement sauf la phrase de retrait de l’annexe II : sa modalité de notification est réécrite conformément au projet déjà présent, mais son blanc « préavis de mois » et le droit au retrait/remboursement restent conservés. Les cinq champs de capital, les noms laissés vides, sièges, compétences à renseigner et options de gouvernance restent des champs du modèle. Aucune valeur ni durée n’a été inventée. Les champs n’ont pas été supprimés dans les dernières réponses pour esquiver le contrôle. Les logs intermédiaires ne constituent pas des instantanés séparés complets de chaque réponse historique ; ce constat vise expressément les versions finales scellées.

La conservation des clauses favorables est détaillée dans `../DIAGNOSTIC.md` : dérogations de cession, exonération de L443-14, facultés de détention du capital, garanties de rachat et agrément tacite, vote, dividendes, réserves, droits de retrait, dispense de dépôt/publication et notes de facultativité. Les changements du projet concernent les obligations énumérées dans ses métadonnées et transitions ; aucune clause n’a été remplacée par une ellipse.

**Aucun correctif textuel n’est proposé.** Cela sépare explicitement la correction de validation d’une réécriture du contenu. Les réserves sur les anciennes versions de renvois, sur la faculté de détention à 50 %, et sur les notifications hors corpus restent inscrites dans les notes ; la réparation du faux positif ne les résout pas.

## Limites et conditions bloquant une activation immédiate

1. Le coordinateur 75807 et ses huit agents doivent continuer. Ce dossier n’autorise aucun arrêt, signal, changement de slots ni modification à chaud. L’absence d’agents actifs et de transaction doit être établie au point sûr prévu par le coordinateur avant toute bascule. Le seul fait d’attendre un délai ne suffit pas.
2. Les contrôles de fraîcheur `check_guards` contre les documents/drafts canoniques réels, les politiques courantes, les éventuels drafts existants et le verrou d’écriture ne sont **pas** certifiés par la base de test minimale. Ils doivent être refaits au point sûr. Aucun test d’enregistrement live n’a été réalisé.
3. La suite démontre les deux validations complètes de ces entrées et le refus des mutations testées, pas une preuve universelle d’absence d’omissions sémantiques. Un texte abrégé sans marqueur et conservant artificiellement tous les titres exige toujours la revue de fond et les contrôles existants ; aucune regex ne la remplace.
4. Limite préexistante conservée : `validate_batches` accepte l’absence de `substantive_impact` lorsque `required=False`, alors que le coordinateur l’exige ici ; un impact fourni mais invalide est rejeté par les deux. L’enregistrement ne porte pas non plus l’exigence textuelle `benefit_review` du coordinateur. La bascule ne doit donc jamais remplacer le parcours complet par le seul enregistrement.
5. Le traitement des deux modèles certifiés est volontairement strict : un futur changement légitime de la clause 5 ou une abrogation intégrale exige une nouvelle revue de cette preuve. Pas d’extension automatique à d’autres modèles ni de contournement par changement de source.
6. La syntaxe des titres est comparée conservativement aux sources de ces deux articles. Une simple refonte de balisage peut produire un refus supplémentaire ; ce refus doit être examiné, pas assoupli silencieusement.

## Plan de bascule au prochain point sûr

1. Attendre la fin naturelle des lots actifs et vérifier le point sûr via le mécanisme existant du coordinateur ; ne pas déclencher une seconde boucle. Maintenir les huit capacités et politiques telles quelles.
2. Comparer les SHA actifs aux `before_sha256`, vérifier que `template_fields.py` n’existe pas déjà, et vérifier les empreintes des sources, notes, réponses, politiques et snapshots. Toute divergence suspend la bascule et impose rebase/revue ; ne jamais écraser une modification récente.
3. Relancer les deux commandes de test ci-dessus depuis le dossier isolé. Faire relire les trois patches, la preuve des cinq champs et l’absence de correction textuelle.
4. Appliquer ensemble les trois fichiers **seulement** à un point où aucun interpréteur actif n’emploie l’ancienne version ; utiliser le mécanisme de reprise existant, sans double coordinateur. Un Python déjà lancé garde des modules importés en mémoire : remplacer les fichiers ne suffit pas à changer sa validation.
5. Rejouer pour les deux lots le parcours normal : `validate_answer`, `accept_checks` sur snapshot frais, gardes de source/politique/renvois/draft puis contrôle d’enregistrement. Revalider les avantages et impacts, sans modifier de notes pour leur faire dire qu’une référence absente a été vérifiée.
6. N’enregistrer et ne compter que les résultats effectivement acceptés par ce parcours normal. Conserver la preuve originale, les SHA de bascule et résultats. Au moindre échec, laisser le lot en attente ; aucune fabrication de résultat de succès ni retrait de champs.
7. Retour arrière du code uniquement au même point sûr, avec comparaison des SHA après ; ne pas supprimer de brouillon ou annuler une transaction déjà effectuée pour revenir artificiellement à l’état du test.

État final de cette préparation : fichiers actifs et lots intacts ; aucun compteur modifié ; dossier d’intégration d’environ 2,7 Mo ; aucune activation.
