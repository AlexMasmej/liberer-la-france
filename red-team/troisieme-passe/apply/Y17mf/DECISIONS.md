# Y17mf : variante du balayage M06 pour un article du groupe Y17

J'ai lu la production en lecture seule le 29 octobre 2026. Le détail des pistes est dans `apply/M06/DECISIONS.md` et `audit/sweeps/M06.json`.

## Correction

**49 septies ZH** (annexe III, LEGIARTI000032362648) : G F3, base légale éteinte.

Les trois articles dont il fixe la déclaration sont en état ABROGE depuis le 21 février 2026 :
- 199 ter L (LEGIARTI000006303156) ;
- 220 N (LEGIARTI000006303563) ;
- 244 quater M (LEGIARTI000051217460).

Un premier alinéa est ajouté. Il limite l'article aux réductions et crédits qui restent légalement ouverts au titre de ces articles dans leur rédaction antérieure. Il n'ouvre aucun crédit et ne crée aucune déclaration pour l'avenir. La déclaration simplifiée déjà décidée est conservée pour ces créances.

J'ai aussi mis à jour :
- le motif ;
- le `benefit_review` ;
- la note qui disait ces trois articles « absents du corpus ».

## Point pour l'auteur

La portée des créances encore ouvertes dépend des dispositions transitoires de la loi n° 2026-103. Cette loi est hors corpus et je ne l'ai pas lue au JORF.

## Contrôle

`python3 -B apply/check_changes.py Y17mf` donne 1 ligne construite et validée, et `problems` est vide.

Revue IA : rien de ceci ne vaut validation par un juriste.
