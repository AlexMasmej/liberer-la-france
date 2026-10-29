# Y18x — décisions (variante de Y18, demande SWEEP-J13-41VBIS)

Texte lu en production (`CITE_PRODUCTION=1 python3 -I tools/cite.py`), en lecture seule. Revue IA, sans validation par un juriste.

## SWEEP-J13-41VBIS — Annexe III, article 39 (LEGIARTI000053218832, LEGITEXT000006069574), 2°, k) : **appliquée**

- **Qualification :** coordination manquante, défaut G (F1+F5). 163 bis G proposé (LEGIARTI000053543883) dispose que le régime « s'applique quelle que soit la durée de l'activité ou du mandat du bénéficiaire ». Il supprime ainsi la majoration de 30 % pour les faits générateurs postérieurs à la réforme des bons attribués depuis le 1er janvier 2026. Ses notes demandent que les déclarations réglementaires « cessent de demander les seules durées devenues inutiles ». Le k) faisait encore déclarer la durée d'activité pour tous les bons.
- **Vérification du texte demandé :** le passage remplacé figure une seule fois, à l'identique, dans la proposition en production. Le critère retenu garde la donnée pour les bons attribués avant 2026 et pour les bons exercés avant la réforme. Il ne la retire donc jamais là où la majoration peut encore jouer : un bon exercé après la réforme est forcément cédé après elle. Il reprend le critère que J13 applique au f du 2° de 41 V bis.
- **Ce qui change :** seul le k) du 2° change. La durée d'activité n'est plus déclarée pour les bons attribués depuis le 1er janvier 2026 et exercés après la réforme. Les date, nombre, prix et fraction de source française restent déclarés. Aucune donnée n'est ajoutée et le reste de la proposition est inchangé.
- **Ligne de lot :** j'ai ajouté une entrée à `removed_provisions` et un effet `coordination` (mesure `bspce-mention-anciennete-etat-individuel`, la même que J13 sur 41 V bis), dont les deux citations sont exactes. J'ai complété l'évaluation (`assessment`), ainsi que le motif et les notes, avec la phrase de troisième passe.
- **Contrôle :** `python3 -B apply/check_changes.py Y18x` → `problems` vide. Diagnostics : `explicit_normative_reduction` (voulu) et `references_changed` (L136-2, L6322-37, L6331-2, L6331-9, R123-221). Ce dernier existait déjà dans la proposition et ne vient pas de cette correction.
- **Pour l'auteur :**
  - le bloc `reference_coherence` de la ligne porte l'empreinte de l'ancienne proposition, et le coordinateur devra le recalculer ;
  - la correction ne dépend pas de l'application de la correction J13 sur 41 V bis, mais les deux doivent aller ensemble ;
  - la transition dépend de 163 bis G : la date de fait générateur y est la cession, ici l'exercice, et ce critère est plus prudent.
