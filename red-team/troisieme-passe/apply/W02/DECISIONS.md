# W02 : décisions du balayage (troisième passe)

Tous les textes ont été lus en production, en lecture seule : `CITE_PRODUCTION=1 python3 -I tools/cite.py` et sqlite en `mode=ro`. Les exports sont sous `evidence/cited/production-20261029/`. Rien n'a été écrit en production. Le contrôle `python3 -B apply/check_changes.py W02` donne 8 changements construits, 8 validés et `problems: []`.

Cette revue est faite par une IA ; elle ne vaut pas validation par un juriste.

## Bilan

- **Volume** : 54 articles (tous du CSS) et 81 pistes.
- **Qualification** : 24 faux positifs, 15 déjà réglés, 33 défauts mineurs (m) et 9 pistes G. Les 9 pistes G recouvrent 8 défauts distincts, car D711-7 porte deux pistes (S8 et AUDIT) pour le même défaut.
- **Corrections** : 7 défauts G corrigés, soit 8 changements dans `changes.json` (6 `replace`, 1 `replace` sur des notes seulement, 1 `new`). Un défaut G n'est pas corrigé : D821-8, qui demande un arbitrage.
- **Demande** : 1 demande au groupe W06, pour R174-2-4.
- **Écarts** : 6 entrées `skipped`, pour arbitrage ou pièce hors corpus.
- **Diagnostics du validateur** : tous voulus.
  - Changements de longueur hérités : D711-7 et R931-1-28.
  - Renvois retirés : D241-26 et R931-3-23.
  - Renvoi ajouté : L162-27.
  - Renvois R244-4 et R244-6 : déjà présents dans la proposition de L244-1, reportés sur sa version de 2029.

## Corrections appliquées (défauts G)

| Objection | Article (version) | Correction |
|---|---|---|
| SWEEP-W02-01 | D711-7 (LEGIARTI000030067305) | Retrait du renvoi « et D. 241-26 ». D241-26 est abrogé depuis le 1er janvier 2018 ; sa dernière version, LEGIARTI000030067280, portait sur l'effectif de la déduction forfaitaire de D241-24. La note qui le disait « absent du corpus » est rectifiée. Aucun droit n'est retiré. La correction est celle que suggérait l'audit. |
| SWEEP-W02-02 | R114-18 (LEGIARTI000031828742) | L'exception à l'avis préalable reprend les termes de L162-1-20, maintenu : « des faits relevant du IV de l'article L. 114-17-1 ». Sont retirées la condition de « fraude établie [...] dans les cas définis par voie réglementaire » et la phrase « La seule suspicion d'une fraude ne dispense pas ». Par décret, elles rétablissaient un avis que la loi écarte, et elles vidaient l'exception de son effet. L'avis de quinze jours, le conseil, le document signé conjointement, le secret médical et la transition limitée au renvoi VII→IV sont conservés. Aucune formalité nouvelle. |
| SWEEP-W02-03 | R174-2-1 (LEGIARTI000030057250, maintenu, désormais `rewrite_draft`) | Les trois renvois « L. 174-2-1 » deviennent « L. 162-27 ». La loi n° 2025-1403, article 72, a transféré L174-2-1 à L162-27 au 1er janvier 2026 (LEGIARTI000048702756, état TRANSFERE, avec un lien de concordance). Une phrase de continuité couvre les factures émises sous l'ancien numéro. Fond inchangé. |
| SWEEP-W02-04 | R931-1-28 (LEGIARTI000030575584) | Retrait de la mention isolée « R. 931-3-23, ». Le décret n° 2015-513, article 14, a transféré cet article à R931-3-21 (LEGIARTI000006754838), qui figure déjà dans la plage « R. 931-3-21 à R. 931-3-22-4 ». Les notes sont rectifiées. Aucun effet de fond. |
| SWEEP-W02-05 | L162-5-4 (LEGIARTI000031928685) | La transition présentait l'exemption de « la majoration hospitalière » comme ouverte aux consultations futures. Or le troisième alinéa de L162-26 proposé dispose « Aucune majoration ne peut être appliquée ». Cette exemption vaut désormais pour les seules consultations et actes antérieurs ; l'exemption relative aux dépassements (18° de L162-5) reste ouverte aux installations futures. Le `benefit_review` est mis à jour. |
| SWEEP-W02-06 | L161-36-5 (LEGIARTI000033714741, maintenu, désormais `rewrite_draft`) | « dernier alinéa » devient « troisième alinéa ». L161-15-4 proposé ajoute en effet un quatrième et dernier alinéa transitoire ; la dispense CFE se trouve au troisième, dans la source comme dans la proposition. |
| SWEEP-W02-07 | L244-1 : version LEGIARTI000052846151 (`new`) et version LEGIARTI000029961352 (`replace`, notes seulement) | La version publiée au 1er janvier 2029 (ordonnance n° 2025-1091 : « tribunal contraventionnel ») n'avait pas de proposition. Elle reçoit le second alinéa de coordination, qui empêche de poursuivre les manquements dépénalisés par l'abrogation de R244-4 à R244-6. Ce seul alinéa est reporté ; sans lui, il aurait disparu en 2029. Sur la version courante, la note « texte successeur non fourni » est corrigée ; le corps et le motif sont inchangés. |

## Demande à un autre groupe

- **W06, R174-2-4 (LEGIARTI000050942470)** : remplacer « l'article L. 174-2-1 » par « l'article L. 162-27 » au premier alinéa, et rectifier la note « L174-2-1 absent du corpus actif ». C'est la même coordination que SWEEP-W02-03.

## Défauts non corrigés (points pour l'auteur)

1. **D821-8 (G, non corrigé : arbitrage et pièce manquante).**
   - Constat : la liste des titres ouvrant l'AAH renvoie aux 1° à 6° et 11° de D115-1. Le décret n° 2017-736 a abrogé D115-1 (dernière version LEGIARTI000031202714).
   - Option 1 : un renvoi figé à la rédaction de 2015. Mais cette liste ignore les titres créés depuis, comme la carte pluriannuelle.
   - Option 2 : la liste de l'arrêté pris pour R111-3. Mais cet arrêté est hors corpus, et R111-3 ne vise pas L821-1.
   - Le choix peut restreindre ou étendre l'accès à l'AAH ; il revient à l'auteur.
2. **Fonds de solidarité vieillesse dissous (m).**
   - Constat : L135-1 à L135-5 sont abrogés au 1er janvier 2026 par la loi n° 2025-199, article 24 (LEGIARTI000037290440).
   - Pourtant, R135-2, réécrit par le projet pour la nomination du conseil, et R135-14 organisent encore cet établissement. Les notes disent à tort L135-1 « non disponible ».
   - À décider : faut-il abroger la section réglementaire du FSV (environ R135-1 à R135-15) en réservant les opérations de dévolution ? Les dispositions transitoires de l'article 24 sont hors corpus, et cette section dépasse le paquet.
3. **Annexes prudentielles orphelines (m).**
   - Annexes concernées : LEGIARTI000027894005, LEGIARTI000027894041, LEGIARTI000027894158, LEGIARTI000027894208, LEGIARTI000027894211, LEGIARTI000027894223 et LEGIARTI000027898913.
   - Constat : elles sont données VIGUEUR, alors que leurs articles de rattachement (A931-11-9, A931-11-11, A931-11-15, A931-11-17, A931-11-21, A941-1-1) et presque toutes les cibles qu'elles citent sont ABROGE au 1er janvier 2016.
   - Les successeurs relèvent du code des assurances ou du règlement ANC 2015-11, hors corpus.
   - D'autres annexes de la même famille, hors paquet, sont probablement dans le même cas : à A931-11-16, A931-11-19, A931-11-20, A931-11-22 et les annexes (1) et (2) à A931-11-11. Je ne les ai pas lues en entier.
   - À décider : une vérification sur Légifrance, puis éventuellement une abrogation de toilettage.
4. **Renvois morts hérités, sans successeur établi au corpus (m, non corrigés).**
   - A932-3-4 vise le II de A932-3-14, abrogé le 5 décembre 2020.
   - A932-4-1 vise R932-4-14 et A931-10-10.
   - R932-5-11 vise L932-43 et L932-48, abrogés ou déplacés en 2023 ; l'article paraît sans objet depuis le transfert aux IRPS.
   - L160-7 vise L766-1, abrogé en 2018. C'est une réserve favorable : elle est laissée telle quelle.
5. **Notes inexactes (F10, m).**
   - De nombreuses notes disent une cible « absente du corpus » alors qu'elle y figure, abrogée ou transférée : L643-6 dans D643-10 et D643-10-1, et les cibles des annexes A931.
   - Elles ne sont corrigées que sur les articles modifiés ici.
6. **Hors lot.** L161-15-4 (LEGIARTI000043498638) vise encore L766-2, abrogé le 27 décembre 2018. C'est un renvoi hérité, non corrigé.

## Une ligne par piste

**Faux positifs**
- D454-1 et L454-2 → L454-1, cinquième alinéa (2 + 2 pistes) : ce cinquième alinéa porte toujours l'obligation d'information.
- D281-2 et R151-3 → L151-1, troisième alinéa : c'est bien la suppression de la suspension financière.
- R522-3 → L522-2, dernier alinéa : toujours le complément différentiel.
- R174-2-1 → L174-2, premier alinéa : désignation de la caisse inchangée.
- A931-3-12 → A931-3-29, dernier alinéa : conservation des procès-verbaux.
- L471-1 → L441-5, premier alinéa : délivrance de la feuille.
- Renvois à un autre code de même numéro :
  - R145-32 → R623-1 et R623-7 ; R145-27 → R611-7 et R611-5 ; R145-25 → R611-5 (code de justice administrative) ;
  - R541-7 → L245-1 ; R861-5 → L262-2 (CASF) ;
  - L931-18 → L611-4 (code de commerce) ;
  - L931-15-1 → L542-1 (code monétaire et financier) ;
  - L931-9 → L143-1 et L310-2-1 ; L931-4 → L322-2 ; R931-12-6 → L326-12 (code des assurances) ;
  - L413-10 → L723-2 (code rural).

**Déjà réglés**
- R815-44 (L815-13), R138-10 (L245-1), R137-2 (L138-22), D162-29 (L162-1-7-1) ;
- L931-25 (L932-51), R931-1-3 (L912-2) ;
- D325-6, D325-1 et R821-8 (L174-4) ; D374-6 (L374-1) ; D380-5 (L380-2) ;
- D643-10 et D643-10-1 (L643-6, renvoi transitoire voulu) ;
- A931-3-13 et A931-3-14 (A931-3-11, « rédaction antérieure »).

**G corrigés** : D711-7 (D241-26 et AUDIT), R114-18 (AUDIT), R174-2-1 (L174-2-1), R931-1-28 (R931-3-23), L162-5-4 (L162-26), L161-36-5 (L161-15-4) et L244-1 (S5, successeur 2029).

**G non corrigé** : D821-8 (D115-1).

**m, non corrigés**
- Annexes A931 (25 pistes) ;
- A932-4-1 (2 pistes) et A932-3-4 ;
- R932-5-11 (2 pistes) ;
- R135-14 et R135-2 (L135-1) ;
- L160-7 (L766-1).

Le détail par piste, avec les citations et les identifiants LEGIARTI, figure dans `audit/sweeps/W02.json`.

## Limites

- Les annexes comptables de 50 000 à 60 000 caractères ont été lues par plages : contexte des renvois, motifs et notes. Elles n'ont pas été lues ligne à ligne.
- Le texte intégral des lois n° 2025-199 (article 24), n° 2025-1403 (article 72) et n° 2018-1214 n'est pas au corpus. Seuls leurs liens LEGI ont été exploités.
- Aucune source n'a été consultée sur Légifrance pendant cette passe.
