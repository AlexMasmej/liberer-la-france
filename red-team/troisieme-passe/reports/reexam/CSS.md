# Réexamen CSS : instantané 20261026T230545Z → 20261027T044303Z

Groupe : CSS. Paquet : `reports/reexam/packet-CSS.json`, soit 15 objections issues des dossiers P1-CSS-A, P1-CSS-B et FUT-CSS, et 14 alertes P1 liées. Détail et traces : `reports/reexam/CSS.json`.

Revue par IA, en lecture seule. Elle ne vaut pas validation par un juriste. Les conclusions restent provisoires : la seconde passe est bloquée, et non terminée (15 597 articles relus sur 30 314).

## Méthode

- Chaque objection a été relue en entier dans `reports/register.json`.
- Pour chaque article modifié, j'ai lu en entier l'ancienne version (exports `evidence/cited/20261026T230545Z/`) et la nouvelle (`tools/cite.py`, exports `evidence/cited/20261027T044303Z/`) : source, NOTA, proposition, motif et notes.
- Pour tous les autres articles cités par les objections, j'ai comparé les empreintes des deux manifestes (`manifests/*.json`) et lu les textes courants concernés, y compris les versions différées hors inventaire.
- Lectures complémentaires, faites pour vérifier un effet nouveau ou lever une incertitude : L145-6-2, R165-1, R162-33-1, L641-1, L766-11, R532-8, L162-17-1 et L752-3.
- Aucun script de production n'a été lancé. Aucune source extérieure n'a été consultée.

## Verdicts

| Objection | Verdict | Priorité | Ce qui change |
|---|---|---|---|
| RT-FUTCSS-17 (L861-5) | maintenue | P1 | Seul le 6e alinéa change, en mieux : les échéanciers respectés valent paiement. Le texte reste rédigé sur la version ABROGE_DIFF, sans le renouvellement automatique des présumés éligibles (2° à 5° de L861-2) ni le ciblage du 3e alinéa (version 2023). |
| RT-P1-CSS-A-01 (R137-2) | résolue | – | La représentation n'est plus exigée ; la responsabilité est limitée aux opérations antérieures, conformément à L138-22 proposé. |
| RT-P1-CSS-A-04 (L3133-7) | résolue | – | Le 2° supprime désormais la CSA, avec la même transition que L137-40. Réserve mineure : la règle est énoncée en double. |
| RT-P1-CSS-A-14 (R123-48) | résolue | – | La réserve de l'agrément R123-4 est retirée ; le renvoi est historique et neutralisé. |
| RT-P1-CSS-B-02 (L162-1-7-1) | reformulée | P1 → P2 | R161-45 est corrigé et neutralise les mentions pour les soins nouveaux. Restent R163-2 IV (avec une note erronée) et huit décrets inchangés, plus R165-1, lu cette fois, qui porte la même mention fondée sur « L. 162-19-1 », absent du corpus. |
| RT-FUTCSS-21 (R160-5 2027) | reformulée | P2 | Portée élargie : la version du 1er janvier 2027 relève neuf fourchettes, pas seulement le 3° bis. R160-5 est clos par la seconde passe sans décision sur cette version. |
| RT-FUTCSS-36 (versions 2018/2012) | maintenue | P2 (à confirmer) | R145-10 coordonné avec L145-6-2. Le conflit avec les versions VIGUEUR_DIFF de 2018 et 2012 n'est pas traité. |
| RT-P1-CSS-A-03 (R138-19, L138-20) | reformulée | P2 | R138-19 est borné. Restent L138-20 et deux notes contradictoires. |
| RT-P1-CSS-A-06 (R137-6, D311-2) | reformulée | P2 | R137-6 est abrogé pour l'avenir. Reste D311-2 (CSA). |
| RT-P1-CSS-A-11 (L133-4-10, L752-3) | reformulée | P2 | R133-9-4 et R155-4 sont bornés au stock. Reste R752-6. Voir aussi RT-RXCSS-02. |
| RT-P1-CSS-A-16 (L931-25) | résolue | – | La plage pénale est limitée à L932-49 et L932-50, avec une transition pénale plus douce. |
| RT-P1-CSS-A-17 (R162-30-1, R931-1-3) | reformulée | P2 | R162-30-1 est corrigé. Reste R931-1-3 b). |
| RT-P1-CSS-B-01 (forfait L174-4) | reformulée | P2 | L871-1 et L911-7 sont bornés. Restent sept textes maintenus et D325-1, dont R821-8 I a) (AAH). |
| RT-P1-CSS-B-07 (L931-26, L272-2) | reformulée | P2 | L922-8 est corrigé ; L641-1 et L766-11 neutralisent déjà le renvoi. Reste L612-2. |
| RT-P1-CSS-B-11 (notes) | reformulée | P2 | R133-9 est corrigé. Restent les notes de L138-20 (point commun avec A-03), de R543-6 et de R163-2. |

**Bilan :** 2 maintenues, 9 reformulées, 4 résolues, 0 obsolète. Un seul changement de priorité : RT-P1-CSS-B-02 passe de P1 à P2. Les 14 alertes liées sont toutes requalifiées en « alerte écartée » : leur renvoi est désormais borné, transitoire ou neutralisé, et chacun a été lu en entier.

## Défauts nouveaux

- **RT-RXCSS-01 (P2, coordination manquante).** R160-5 corrige le renvoi du 12° vers R162-33-1, mais seulement sur la version qui expire le 1er janvier 2027. La version qui lui succède, hors inventaire, garde le renvoi fautif au « 3° […] urgences gynécologiques ». Correction : reporter la coordination sur LEGIARTI000054739003. C'est un cas particulier de RT-FUTCSS-38, distinct de RT-FUTCSS-21.
- **RT-RXCSS-02 (P2, incohérence du projet).** R133-9-4 et R155-4 réécrits reconduisent, pour les prélèvements anciens, deux compétences incompatibles pour le même arrêté de L133-4-10 : budget et sécurité sociale d'un côté, budget seul de l'autre. Correction : que R155-4 renvoie à R133-9-4.

## Effets nouveaux examinés et non retenus

- **L911-7 III.** « ni une dispense de rémunération entre deux affectations » devient « ne modifie pas les règles légales ou conventionnelles de rémunération ». La phrase retirée n'existait que dans le brouillon, et aucune orientation ne l'impose. Point à surveiller avec le dossier du contrat unique.
- **R137-6.** Le renvoi aux procédures R243-29/30 et au code rural est remplacé par « les règles applicables à ces versements ». Ce n'est pas une perte de garantie.
- **Notes périmées sans effet.** La note de R123-4 réclame encore le retrait de la réserve de R123-48, qui est fait. La note de R155-4 dit encore « son arrêté demeure ».

## Couverture réelle et limites

- **Lu en entier :** les 15 objections ; les 22 articles modifiés du paquet, dans leurs deux versions ; les autres articles des objections, par empreinte, avec lecture des textes courants utiles. Cela fait environ 60 versions d'articles, dont les versions différées hors inventaire de L861-5, L861-3, R160-5, R145-10 et R146-8.
- **Non lus en entier :** L932-49 et L932-50 (leur portée est reprise des notes de L931-25) ; les arrêtés d'application ; le JORF (décrets d'août 2026, décret n° 2025-1286, décret n° 2018-79) ; le CASF et le code rural.
- **Plusieurs articles du reliquat sont encore en attente de seconde passe :** D311-2, R752-6, R931-1-3, R163-2, R165-1, D325-1, R821-8 et R871-2. Ils peuvent encore changer.
