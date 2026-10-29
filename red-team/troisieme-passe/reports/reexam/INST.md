# Réexamen INST : instantané 20261026T230545Z → 20261027T044303Z

Groupe INST : 15 objections issues des dossiers CSS12, TUT, UNION, INV, XCUT et A1DOSSIER. Les verdicts détaillés, avec leurs citations exactes, figurent dans `INST.json`. Cette relecture a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Synthèse

| Verdict | Nombre | Objections |
|---|---|---|
| maintenue | 7 | RT-XCUT-01 (P1), RT-UNION-03 (P1), RT-A1-02, RT-A1-03 (à confirmer), RT-TUT-04, RT-INV-10, RT-TUT-08 (P2) |
| reformulée | 3 | RT-INV-01 (P0 → P2), RT-CSS12-01 (P1 → P2), RT-CSS12-03 (P2) |
| résolue | 5 | RT-CSS12-02, RT-CSS12-04, RT-CSS12-05, RT-CSS12-06, RT-INV-13 |
| obsolète | 0 | |

Changements de priorité : le seul P0 du groupe, RT-INV-01, descend à P2 ; RT-CSS12-01 passe de P1 à P2. Il reste deux P1 : RT-XCUT-01 et RT-UNION-03.

## Points principaux

- **RT-INV-01 (CGI 1609 quinvicies).** L'effet P0 est levé. La proposition ne réinstitue plus la contribution supplémentaire à l'apprentissage : elle commence par « Le présent article est abrogé. » et précise qu'elle « n'institue aucune contribution en sus de celle régie […] par l'article L. 6242-1 du code du travail ». Elle concorde avec L6242-1, qui est inchangé. Deux défauts subsistent, en P2 :
  - la version mort-née (LEGIARTI000042914206) reste comptée comme article courant ;
  - des règles de fond sur le contrat unique sont logées dans un article qui se déclare abrogé, en doublon de L6242-1 VIII.

  Correction : une mention documentaire non normative, et la sortie de la version de la couverture courante.
- **RT-XCUT-01 (versions futures).** Le recomptage sur le nouvel instantané donne **516 versions VIGUEUR_DIFF futures sans proposition, contre 516 avant** ; aucune n'a reçu de proposition. Il y a 408 successeurs et 108 nouveaux numéros. 43 successeurs prennent effet le 1er novembre 2026, alors que la seconde passe est arrêtée jusqu'au 2 novembre. Parmi les 384 versions courantes concernées, 85 ont changé, mais aucune ne traite sa version future.
- **Agréments CSS (CSS12-01 à 04).** R123-1-1 et R152-8 sont désormais abrogés à la date de la loi, et R123-1 est réécrit : il garde la désignation ministérielle utile à R123-54. RT-CSS12-02 et RT-CSS12-04 sont résolues. Il reste D224-7, encore « pending » :
  - il affirme « Les agréments prévus par les articles L. 123-1 et L. 123-2 demeurent applicables dans leur champ. » (RT-CSS12-01, P2) ;
  - il supprime l'avis du comité dès le décret, alors que la source de R123-1-1 fait courir l'agrément tacite à partir de cet avis jusqu'à la loi (RT-CSS12-03).
- **Tutelle.** R151-1 et R151-3 sont coordonnés (RT-CSS12-06 résolue) et R153-2 aussi (RT-CSS12-05 résolue). En revanche, R226-1 et R226-2 renvoient encore au « troisième alinéa de l'article R. 151-1 » pour la saisine nationale. Cet alinéa est désormais la clause qui supprime cette saisine : le renvoi est inversé (RT-TUT-04). R216-2 est inchangé (RT-UNION-03, P1).
- **RT-INV-13.** Les trois propositions CCH sont rattachées aux lots `radical-review-legacy/00011` et `00012`, enregistrées et relues en seconde passe : résolue.

## Nouveaux constats

- **RT-RXINST-01 (P2, réserve documentaire).** Les notes de L123-1, L123-2, L123-2-1, R123-1-1, R123-1 et R123-54 décrivent comme actuelles des contradictions déjà corrigées dans le même intervalle. Par exemple, « R. 123-1-1 conserve encore un agrément tacite dans sa proposition ». Les notes de R123-1-1 demandent même de retirer une désignation que R123-54 utilise. Correction : mettre à jour les notes seulement.
- **RT-RXINST-02 (P2, anomalie d'inventaire, cause de RT-XCUT-01, sans double compte).** Au moins 30 versions courantes, comptées « completed », ont des notes qui déclarent leur successeur « non fourni » ou « manquant ». Or chaque successeur figure au corpus en VIGUEUR_DIFF. La note de 1509 affirme même : « aucun successeur de 1509 disponible dans le corpus », alors que LEGIARTI000053188717 y figure. Les rédacteurs de seconde passe ne reçoivent donc pas les versions futures. Correction : joindre le XML des successeurs aux sources et requalifier les articles déjà terminés sans eux.

## Couverture réelle

- **Lus en entier, dans l'ancien export et dans le nouveau** (proposition, motif, notes) : CGI 1609 quinvicies ; CSS R123-1-1, R152-8, R123-1, R151-1, R151-3, R151-4, R153-2, R155-1, R151-2, R152-1, R152-2 ; CCH D304-1, D319-6, D319-7 ; CGI 302 J.
- **Lus en différentiel** : CGI 302 D bis (seules ses notes ont changé), CSS R123-54 et R123-56.
- **Relus dans le nouvel instantané** : travail L6242-1 ; CSS D224-7, L123-1, L123-2, L123-2-1, L153-6, R216-2, L216-3, R226-1, R226-2, R752-24, L151-1, D635-5 ; annexe I 165 ; CGI 508 (état et NOTA).
- **Contrôlés par empreinte seulement, inchangés** : L224-5-1, L224-5-2, L123-2-3, L153-2, R226-4, D632-7.
- **XCUT** : recomptage complet par SQL sur les 516 versions. Différentiel des 13 articles du paquet : complet pour L3332-17-1, L931-7-2, R145-10 et 1042 ; filtré sur les mentions temporelles pour les 9 autres. Les 408 couples (courant, futur) n'ont pas été lus.
- **Non examiné** : production (lecture seule, non consultée), textes hors corpus (code rural, CIBS, CASF), JORF des ordonnances 2021-797 et 2021-1843.

Toutes les conclusions sont provisoires : la seconde passe reprendra au plus tôt le 2 novembre 2026.
