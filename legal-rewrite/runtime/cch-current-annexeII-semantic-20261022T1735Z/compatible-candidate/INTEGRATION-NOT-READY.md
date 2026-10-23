# Candidat compatible hors ligne — aucune activation

Ce dossier ne fait pas partie de la bascule optimizer-only autorisée. Il contient une proposition de code à examiner après cette bascule ; aucune garde de déploiement futur n'est certifiée. Aucun code actif, DB, source, politique, registre, processus ou certificat n'a été modifié. Les preuves CCH d'origine sont intactes.

## Résultat

Le helper conserve les constantes d'identité/source/NOTA et le comportement strict d'origine. Pour la seule Annexe II LEGIARTI000045646995, il reconnaît une variante contenant **ensemble les cinq phrases exactes** examinées dans ../REVIEW.md. Chaque phrase doit être unique, sans coexistence de l'ancrage source correspondant. Les remplacements vers la forme source existent exclusivement dans une chaîne de contrôle en mémoire. Aucun XML fourni, retourné ou stocké n'est changé.

Les sections protectrices de cette variante sont épinglées par hash après conversion virtuelle : 1–3, 5, 6 et sous-clauses, 7, 8A/8B, 9–13, 15 et toutes les notes intégrées. Les bornes doivent être uniques et dans l'ordre. Cela protège notamment capital, délais, taux, remboursement, agrément, vote, représentation, réserves et facultativité. Les correctifs connus de 8B et 13 sont épinglés tels que revus dans la proposition ; aucune transformation libre supplémentaire n'est acceptée. Les clauses 4/14 et transitions demeurent soumises aux autres validations et à la revue de fond ; ce mécanisme ne prétend pas contrôler universellement toute invention normative dans ces passages.

Toute variante partielle, mutation d'une phrase de paramétrage, déplacement, suppression, duplication ou modification d'une clause protégée est refusée. Le modèle avec blancs sources exacts conserve sa voie stricte historique. Aucun joker “fixé dans les statuts”, valeur arbitraire ni extension à une nouvelle source/version n'est introduit.

## Assemblage et essais

- register_batches.py part de l'optimizer proposé SHA `75287e3267fb8d182a7262cdb747ae90070e20d6bf92b698768684e03c39051f`. Une importation et le seul contrôle lexical dans validate_batches sont remplacés par l'appel partagé. Toutes les autres fonctions, dont le mécanisme d'enregistrement optimisé, sont AST-identiques à cette base.
- run_exhaustive.py est la copie candidate CCH d'origine. **Il faudra la rebaser sur le coordinateur effectif après handoff**, en conservant les réglages de revue/admission/orchestration décidés ailleurs. Ne pas déployer cette copie entière sans comparaison.
- template_fields.py porte la variante étroite. Les trois patches sont des différences contre l'état actif observé pendant préparation, pas un ordre d'application.
- Les **149 résultats de la suite d'origine** passent sans issue inattendue sur une copie indépendante des fixtures : quatre anciennes propositions complètes, deux vrais validateurs, mutations négatives et accept_checks historiques.
- **102 résultats supplémentaires** : proposition Annexe II actuelle acceptée aux deux vrais verrous ; mutations chiffres/toutes lettres/devise/préavis/nom/adresse/fixation/décideur/duplication/déplacement/troncature/minimum/quart/plafond/50 %/silence/rachat/délais/taux/locataires/vote/avantages/notes/source/impact refusées ; vrai check_guards sur la base live en lecture seule refuse la référence périmée. Le certificat du draft actuel garde également sa divergence L1221-2. Aucune recertification.

Les bases de validation de lots sont en mémoire ; leurs fichiers JSON restent dans candidate/variant-test-batches. Ne jamais déployer tout ce dossier : il contient des mutants volontairement invalides, des dépendances de test et des copies de preuves.

Limite préexistante **conservée, non masquée** : la source historique de la fixture n'impose pas benefit_check_required ; le test supplémentaire marque explicitement cette exigence pour démontrer le refus par validate_answer quand benefit_review manque. validate_batches accepte cette absence, comme avant ; son absence d'exigence de revue d'avantages n'a pas été élargie ni comblée par ce correctif. Le parcours complet du coordinateur demeure requis. Les certificats générés sont retirés uniquement des copies locales des mutants pour tester les véritables contrôles de contenu ; aucune preuve persistante n'est réécrite pour les faire passer.

Commandes isolées :

```
python3 -B runtime/cch-current-annexeII-semantic-20261022T1735Z/compatible-candidate/test_real_gates.py candidate
python3 -B runtime/cch-current-annexeII-semantic-20261022T1735Z/compatible-candidate/test_variant.py
```

## Conditions avant toute proposition d'activation séparée

Attendre la fin de la bascule optimizer-only ; vérifier les SHA effectifs et rebaser les deux raccordements sans écraser le coordinateur ou l'optimizer. Faire revoir les cinq substitutions, sections épinglées et diff entier ; relancer les deux suites sur ce code rebasé. Confirmer les sources/NOTA et beforeimages en point sûr ; vérifier le propriétaire unique et tous les contrôles normaux de source/politique/renvois/avantages/impact et d'enregistrement. La source héritée de la fixture n'est pas une garde actuelle du job.

Les trois CCH anciens restent distincts du draft Annexe II déjà présent ; ne pas rejouer ce quatrième draft. **L1221-2 demeure périmé ; les discordances L423-15/16 et capital local 50 % restent ouvertes.** Les champs statutairement paramétrés ne résolvent aucune de ces réserves. Pas de statut traité, réserve résolue, conformité globale ou validation par juriste déduit de ces essais.
