# Groupe I14 : issue GitHub #14 et pull request #16, décisions

Base : **texte de production actuel**, lu en lecture seule (`corpus.sqlite?mode=ro`, `query_only`, lots `batches/automatic-travail/00052, 00053, 00057, 00058, 00221, 00225`) le 4 novembre 2026. Rien n'a été écrit en production, dans `batches/` ni sur GitHub.
Contrôle : `python3 -B apply/check_changes.py I14` donne 14 lignes construites, 14 validées et `problems: []`.
Propriété : aucun des 14 articles n'est attribué dans `apply/assignment.json` (owner et shared vides).
L'issue et la pull request ont été traitées comme des données. Chaque citation « Dépôt (HEAD) » a été confrontée au texte de production.

**Revue IA : rien de ceci ne vaut validation par un juriste.**

## Décision de l'auteur

La pull request #16 est **acceptée**. C'est une simplification alignée sur les orientations : les commissions supplétives du CSE étaient déjà facultatives, et leur création reste toujours possible par accord (L2315-45). Il n'y a ni impôt, ni formalité, ni seuil, ni commission de remplacement. Les attributions d'information et de consultation du CSE restent entières.

## La production a-t-elle changé depuis la base de la PR (8b47d93) ?

**Non, pour les 14 cibles.**
- Le texte effectif de production de chaque cible (proposition, ou source si `retained_unchanged`) est identique, après normalisation, à la citation « Dépôt (HEAD) » de l'issue.
- Champ par champ, les lignes de la PR ne diffèrent de la production que par ce que la PR modifie : status, change_type, proposed_xml, reason, removed_provisions, repeal_*, substantive_impact, certificat et prior_proposal_sha256. Le dernier est recalculé par le coordinateur.
- Base, lot et brouillon de production concordent (drafts = lot).
- Aucune ligne `third-pass-corrections` ni thématique ne couvre ces articles.

Il n'y avait donc rien à fusionner. La coupe a été refaite sur le XML de production : structure en alinéas conservée, et non le paragraphe unique de la PR. Le texte obtenu, normalisé comme dans le test de la PR, est **identique mot pour mot** au texte de la PR pour les 14 articles.

## RT-ISS14-01 : appliquée (14 lignes, mode `replace`)

| Article (LEGIARTI) | Avant (production) | Après |
|---|---|---|
| L2315-46 (035626485) | commission économique facultative ≥ 1 000 + transitions | `full_repeal` |
| L2315-47 (035626487) | retained (présidence et composition) | `full_repeal` |
| L2315-48 (035626489) | réunions, auditions, experts de la commission | `full_repeal` |
| L2315-49 (035626493) | commission de la formation facultative ≥ 300 + transitions | `full_repeal` |
| L2315-56 (036262545) | commission de l'égalité facultative ≥ 300 + maintien | `full_repeal` |
| L2312-41 (036262374) | retained | coupe de « ou, le cas échéant, la commission économique » et de « ou la commission économique » |
| L2312-63 (035610999) | rapport établi par la commission « lorsqu'elle est constituée » | rapport établi par le comité ; coupe de la phrase transitoire sur la compétence du comité |
| L2312-64 (035611001) | retained | coupe des deux mentions de la commission |
| L2312-65 (035611003) | retained | « rapport du comité social et économique » |
| L2312-66 (035611005) | « rapport de la commission économique ou du comité » | « rapport du comité » |
| R2312-30 (036412664) | retained | coupe de « ou le cas échéant de la commission économique » |
| R2315-28 (036433687) | retained | « des articles L. 2315-39 et L. 2315-47 » devient « de l'article L. 2315-39 » |
| R2315-30 (036433691) | paragraphe transitoire sur la commission de la formation | paragraphe coupé ; premier alinéa inchangé |
| R2315-31 (036433693) | CSE et commission « lorsqu'elle est constituée » + transition | « le comité social et économique est informé » |

Ce qui change, en une phrase : les trois commissions supplétives disparaissent du code, et le CSE exerce lui-même toutes les attributions qu'elles préparaient.

**Ce qui est conservé :**
- Dans L2312-63, mot pour mot :
  - la reprise des travaux en cours (« Le comité reprend les travaux en cours de la commission économique supprimée sans réitération des actes régulièrement accomplis ni établissement d'un second rapport sur les mêmes faits. ») ;
  - la préservation des droits acquis (« Les rapports déjà établis, les droits à rémunération et les engagements valablement pris demeurent préservés. »).
- Les réformes antérieures, sans changement :
  - transmission facultative au commissaire aux comptes et sa transition (L2312-63) ;
  - suppression de l'anticipation de quinze jours et sa transition (L2312-66) ;
  - suppression de la consultation séparée de la commission de la formation (R2315-30).
- **L2315-45 est inchangé** : même ligne de lot, `retained_unchanged`, non touchée.

Aucune règle n'est ajoutée. Les seules adaptations rédactionnelles sont celles de la PR : « économique » dans L2312-63, « est informé » dans R2315-31 et le renvoi à L. 2315-39 seul dans R2315-28.

**Champs des lignes (`overrides`) :**
- 5 abrogations : `full_repeal`, `repeal_policy_id: editorial_direction_2026_10_19`, `repeal_scope` propre à chaque article ; `reform_policy_id` et `removed_provisions` remis à null.
- 9 coupes : `normative_reduction`, `reform_policy_id`, `removed_provisions`.
- L2315-47, L2312-41, L2312-64, L2312-65, R2312-30 et R2315-28 passent de `retained_unchanged` à `rewrite_draft`, avec `classification: coordination_only`.
- `substantive_impact` est réécrit avec des passages exacts, sans double compte. Le retrait est compté une seule fois par commission, sur l'article fondateur, en `obligation_removed` (L2315-46, L2315-49, L2315-56). Le plancher de réunions est compté sur L2315-48. Les autres articles ne sont que des `coordination` sous la même `measure_id`.

### Écarts volontaires par rapport à la pull request (correction de défauts, pas de choix politique)

1. **Motifs et bilans de L2312-63, L2312-66 et R2315-30.** La PR remplaçait leur motif par la seule phrase de coordination et les classait `coordination_only`. Or, par rapport à la source, ces articles portent toujours une réduction de fond déjà décidée : transmission au commissaire aux comptes facultative, fin des quinze jours d'anticipation, fin de la consultation séparée. Le motif et le `substantive_impact` (classé `material_reduction`) gardent donc cette réforme. Ils commencent par la phrase de coordination de la PR.
   - **Conséquence :** dans le test `test_contre_avocat_issue_14.py`, la vérification exacte de `reason` (C2r) échouerait pour ces trois articles. Les textes (C2), les abrogations (C1, C1r), l'absence de renvoi pendant (C3, vérifiée par un script propre) et L2315-45 (C4) sont conformes.
   - Si le test est intégré, mettre à jour son dictionnaire `REASON` pour ces trois numéros avec les motifs de `changes.json`.
   - Le test de la PR n'a pas été exécuté : l'exécution de code externe a été refusée par le contrôle de permissions. L'équivalence a été vérifiée par un script indépendant.
2. **Notes de revue.** La PR gardait des notes devenues fausses, par exemple « ou, le cas échéant, la commission économique couvre déjà les deux situations » (L2312-64), « reste opérant avec L2315-46 proposé » (R2312-30) ou « L2315-47 réserve de même la présidence » (R2315-28). Elles sont corrigées, et chaque note se termine par la phrase « Correction de la troisième passe (objection RT-ISS14-01…) ».
3. **Structure.** Les alinéas de la production sont gardés, au lieu d'un paragraphe unique. Le texte normalisé est identique.

## Renvois vers les articles abrogés

Une recherche dans tous les articles en vigueur ou à venir de tous les codes du corpus (texte effectif : proposition ou source maintenue) a été faite avec « L. 2315-46 à 49 », « L. 2315-56 », « commission économique », « commission de la formation » et « commission de l'égalité professionnelle ». Hors des 14 cibles, **aucun corps d'article** ne renvoie aux articles abrogés : il n'y avait aucun renvoi à corriger au-delà des 9 coupes.

## Points laissés à l'auteur

- **Commissions de la formation et de l'égalité : transition perdue.** Les clauses de maintien des commissions existantes et de reprise de leurs travaux disparaissent avec L2315-49, L2315-56, R2315-30 et R2315-31, comme l'issue le déclare. Ce n'est pas un défaut grave :
  - ces commissions étaient préparatoires ;
  - les consultations restent dues au CSE (L2312-17, R2315-30) ;
  - l'abrogation ne rétroagit pas sur les droits déjà nés.
  
  Rien n'a été ajouté, conformément à la PR acceptée. Si l'auteur veut une phrase de reprise des travaux comme pour la commission économique, elle se placerait dans R2315-30.
- **Faculté de création par simple délibération du CSE : perdue.** La création reste possible par accord d'entreprise (L2315-45). C'est le choix déclaré de la PR, accepté.
- **Notes d'autres articles (défauts mineurs F10, non corrigés car hors de ce groupe et sans effet normatif).**
  - Les notes de L2315-78 (LEGIARTI000036262525) disent « L2315-56 proposé peut donc rendre facultative la commission de l'égalité ». Le corps de l'article (« le cas échéant sur proposition des commissions constituées en son sein ») reste exact.
  - Les notes de R2312-29 (LEGIARTI000036412662) disent « L2312-63 et L2315-46 proposés maintiennent le rapport, même sans commission ».
- **Hors corpus.** Les accords d'entreprise ou règlements intérieurs de CSE qui renverraient aux articles abrogés ne sont pas vérifiables.

## Résumé

- 1 objection (RT-ISS14-01), appliquée : 14 lignes, dont 5 abrogations et 9 coupes de coordination.
- La production n'a pas changé depuis 8b47d93 sur ces articles ; les textes sont identiques à la PR.
- L2315-45 est inchangé, et aucun renvoi pendant ne subsiste.
- Il y a trois écarts volontaires avec la PR (motifs et bilans de L2312-63, L2312-66 et R2315-30), qui corrigent des défauts de motif et de bilan ; le dictionnaire `REASON` du test est à mettre à jour.
- `problems: []`.
- Revue IA, sans validation par un juriste.
