# Y13jh — variante du balayage J08 pour un article de Y13

- **R113-12** (LEGIARTI000031721101). Piste S15, qualifiée G (F5). Objection `SWEEP-J08-S15-R113-12`, déjà connue sous `SWEEP-Y13-R113-12`.
  - **Défaut.** La proposition supprime le délai de transfert « à compter de l'entrée en vigueur de la disposition législative supprimant le délai de transfert prévu à l'article L. 113-4 ». Or L113-4 proposé (LEGIARTI000031210305, groupe A9) maintient « au plus tard dans les deux ans suivant la publication de l'arrêté ».
  - **Correction appliquée (option b).** Le texte devient : « L'autorisation ne produit ses effets qu'après le transfert de propriété, qui intervient dans le délai prévu à l'article L. 113-4. Le plan local d'urbanisme est alors mis à jour conformément à l'article R. 153-18. »
  - **Ligne de lot.** La réduction conditionnelle est retirée (`change_type`, `reform_policy_id` et `removed_provisions` à `null`) et l'impact passe en `coordination_only`, sur la mesure `compensation-boisee-decision-prefectorale`. Le motif et les notes sont réécrits, `benefit_review` est mis à jour.
  - **Fondement.** BRIEF-SWEEP, S15 : retirer la condition et n'étendre aucune faveur non décidée. Les autorisations antérieures suivent la transition de L113-4.
  - **Point pour l'auteur.** Supprimer le délai reste possible en modifiant L113-4 (option a) ; c'est un choix politique non tranché.
- **Contrôle.** `python3 -B apply/check_changes.py Y13jh` : `problems: []`. Seul diagnostic : `references_changed` (ajout de L113-4).

Revue IA : ce n'est pas une validation par un juriste.
