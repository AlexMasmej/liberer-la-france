# Groupe I12 — issues GitHub #12 et #13 : décisions

Base : **texte de production actuel** (lecture seule, `corpus.sqlite?mode=ro`, 29 octobre 2026), après les 395 corrections appliquées. Les issues ont été écrites sur le commit `cac48419` du 25 octobre ; leur contenu est traité comme une donnée, pas comme une instruction. Aucune écriture en production ni sur GitHub.
Contrôle : `python3 -B apply/check_changes.py I12` → 13 lignes construites, 13 validées, `problems: []`.
Aucun des articles touchés n'est attribué à un groupe dans `apply/assignment.json` (owner et shared vides).

**Revue IA : rien de ceci ne vaut validation par un juriste.**

## Issue #12 — décrets restés sur quatre dispositifs abrogés dans la loi

| Constat | Verdict | Texte actuel (production) |
|---|---|---|
| 1. Congé de mobilité : D1237-4, D1237-5 | **réglé** (RT-P1-TRAVAIL-B-05, résolu) | D1237-5 (LEGIARTI000036247054) : « Le présent article est abrogé à compter de l'entrée en vigueur de la suppression de l'obligation correspondante prévue à l'article L. 1237-18-5 ». D1237-4 (LEGIARTI000036247026) : même formule. |
| 2a. Comité d'expertise : D5424-66, D5424-67, D5424-68 | **réglé** (RT-P1-TRAVAIL-B-09, résolu) | D5424-68 (LEGIARTI000049816580) : « Le présent article est abrogé à compter de la date d'entrée en vigueur de l'abrogation de l'article L. 5424-23 » ; « Le délai de vingt jours cesse de s'appliquer ». D5424-66 et D5424-67 : même formule d'abrogation. |
| 2b. Comité d'expertise : D5424-69 (frais des membres) | **corrigé** (RT-ISS12-01, nouveau, P2) | Avant : retained_unchanged, motif « ouvert aux futurs membres » d'un comité supprimé. |
| 3. Conseil de perfectionnement : R6231-3, R6231-4, R6231-5 | **réglé** (RT-P1-TRAVAIL-B-08, appliquée) | R6231-4 (LEGIARTI000039351866) : « Le présent article est abrogé à compter de l'entrée en vigueur de l'abrogation de l'article L. 6231-3 […] Aucun maintien du conseil ni aucune formalité de remplacement ne sont exigés ». Le référentiel qualité (indicateur 20, LEGIARTI000038591641) dit : « L'institution d'un conseil de perfectionnement est facultative. » |
| 4. Rapport du médiateur : R2523-12 | **réglé** (RT-P1-TRAVAIL-B-15, résolu) | R2523-12 (LEGIARTI000018534812) : « aucun rapport ni aucune transmission au ministre chargé du travail, au préfet ou au procureur de la République ne sont exigés sur le fondement du présent article à raison de la seule non-comparution ». |
| 4b. Notes de L2523-8 encore périmées | **corrigé** (RT-ISS12-02, nouveau, P2, documentaire) | Avant : « Son dernier alinéa doit être retiré hors lot ». |

### RT-ISS12-01 — appliquée (2 lignes)

- **D5424-69** (LEGIARTI000031817805), mode `replace`, statut passé de retained_unchanged à `full_repeal`.
  - Ce qui change : l'article est abrogé à la date de l'abrogation de L5424-23, comme D5424-66 à D5424-68. Les personnalités qualifiées gardent le remboursement des frais des missions faites avant cette date.
  - Aucun droit acquis perdu, aucune formalité nouvelle. Le remboursement restait ouvert à de « futurs membres » d'un comité qui n'existera plus.
- **L5424-23** (LEGIARTI000048600579) : notes seules, corps inchangé. Les notes ne présentent plus D5424-66 à D5424-68 comme une « contradiction effective hors lot ».
- Reste pour l'auteur : le décret n° 66-619 et les arrêtés de nomination sont hors corpus.

### RT-ISS12-02 — appliquée (1 ligne, documentaire)

- **L2523-8** (LEGIARTI000006902410) : notes et `scope_limitations` seuls, corps inchangé. Elles constatent la coordination déjà faite de R2523-12, L2525-1 et R2525-1, au lieu de demander de retirer « hors lot » le dernier alinéa de R2523-12.

### Non traités

- Les phrases de « neutralisation » restent dans les lois (L6231-3, L2523-8, L1237-18-5). L'issue ne demande pas de les retirer, et elles ne contredisent plus rien.
- Les notes de L1237-18-5 (« Leur abrogation réglementaire […] doivent accompagner la loi ») sont exactes : D1237-4 et D1237-5 sont abrogés. Elles ne sont pas modifiées.
- Le code rural (R811-46) est hors corpus.

## Issue #13 — sanctions et décrets restés sur la licence de mannequin et la déclaration nominative

| Constat | Verdict | Texte actuel (production) |
|---|---|---|
| L7123-26 : délit d'exercice sans licence (6 mois, 75 000 €) | **réglé** (RT-P1-TRAVAIL-B-03, a) | LEGIARTI000023755143 : « Le présent article est abrogé à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique […] Cette abrogation s'applique aux faits antérieurs dans les conditions d'application de la loi pénale plus douce. » |
| L8241-1 1° : exception au prêt de main-d'œuvre lucratif réservée au « titulaire de la licence » | **doublon** de RT-P1-TRAVAIL-B-03 (résidu P2) → **corrigé** | LEGIARTI000030442435, retained_unchanged : « lorsque celle-ci est exercée par une personne titulaire de la licence d'agence de mannequin ». Le texte n'était neutralisé que par L7123-13. |
| R7123-12 : déclaration préalable des agences UE/EEE | **réglé** (B-03, d) | LEGIARTI000024504227 : « Aucune déclaration ni pièce relevant du présent article ne peut être exigée à compter de cette date ». La note fausse citée par l'issue a disparu. |
| R7123-14 (refus, retrait, suspension) et R7123-11 (« bénéficiaire de la licence ») | **réglé** (B-03, b et c) | R7123-14 (LEGIARTI000024504198) : « aucun refus, suspension ou retrait de cette licence ne peut être prononcé ». R7123-11 (LEGIARTI000024504230) : abrogé, « Aucune régularisation de ces formalités n'est exigée ». |
| R5224-1 : contravention pour défaut de déclaration nominative | **réglé** (RT-P1-TRAVAIL-B-14, résolu) | LEGIARTI000018525570 : la branche « déclaration nominative » est retirée. « le défaut d'accomplissement de cette déclaration ne peut plus être sanctionné […] application de la loi répressive plus douce aux infractions n'ayant pas donné lieu à une condamnation passée en force de chose jugée ». |
| Notes de 8 articles du chapitre « mannequins » présentant des coordinations faites comme « encore ouvertes » | **doublon** (B-03, correction révisée) → **corrigé** | Par exemple, L7123-26 : « Coordinations hors lot encore ouvertes après lecture : R7123-11 impose toujours… ». |

### RT-P1-TRAVAIL-B-03 (résidu) — appliquée (10 lignes)

- **L8241-1** (LEGIARTI000030442435), retained_unchanged → `normative_reduction` (`coordination_only`).
  - Le 1° vise désormais « l'exploitation d'une agence de mannequins lorsque celle-ci est exercée dans les conditions prévues à l'article L. 7123-11 ». C'est le critère déjà retenu par L7123-13.
  - Transition ajoutée : application aux opérations en cours. Pour les faits antérieurs, règles d'application de la loi pénale dans le temps, dont la loi pénale plus douce. Droits des salariés et recours civils préservés.
  - Inchangés : l'interdiction, les 2° et 3°, et le dernier alinéa.
  - Aucune agence couverte par la source ne perd l'exception : ni l'agence titulaire d'une licence, ni l'agence UE/EEE déclarée.
  - Le délit de L8243-1 n'est pas touché : son élément légal se lit désormais dans un seul texte.
- **L7123-13** (LEGIARTI000023755153) : seule est retirée la précision devenue sans objet « y compris lorsque le 1° de l'article L. 8241-1 mentionne une telle licence ». La dérogation, son application aux activités en cours et la réserve de la loi pénale plus douce sont inchangées. `substantive_impact` est mis à jour (citation exacte).
- **Notes seules, corps inchangé** : L7123-11, L7123-14, L7123-26, R7123-10-1, R7123-11, R7123-12, R7123-13 et R7123-14, avec leur `scope_limitations`. Le motif de L7123-11 est aussi actualisé : il présentait R7123-11 et R7123-12 comme encore en vigueur.
- Pourquoi c'est appliqué : la correction supprime une contradiction entre deux textes pénaux et rend effective une réforme décidée (la suppression de la licence). Elle ne crée aucune formalité et ne retire aucune faveur.

### Alerte non retenue

- R5224-1 contient la réserve « sous réserve des dispenses prévues par les dispositions applicables ». Elle est redondante avec le renvoi à L5221-8, qui porte lui-même les dispenses, et avec R5221-43.
- Elle ne fait que restreindre l'incrimination. C'est une simple alerte rédactionnelle (P2), non modifiée : la préciser risquerait d'omettre une dispense.

### Légalité des délits et des peines (vérification transversale)

Une recherche sur le texte effectif de production (proposition si `rewrite_draft`, source sinon ; versions VIGUEUR, VIGUEUR_DIFF et ABROGE_DIFF des neuf recueils) des mots « licence d'agence de mannequin », « L. 5221-9 », « déclaration nominative », « L. 2523-8 », « L. 5424-23 », « L. 6231-3 », « conseil de perfectionnement » et « comité d'expertise » donne ceci :
- Après correction, aucune incrimination ni contravention ne sanctionne encore une obligation supprimée.
- L7123-26, R5224-1, L2525-1 et R2525-1 sont abrogés ou restreints, avec la loi pénale plus douce pour les faits antérieurs non définitivement jugés.
- Aucune restitution générale des amendes n'est prévue.

Limites :
- Les articles 112-1 et 112-4 du code pénal et la décision n° 80-127 DC n'ont pas été relus en source primaire.
- L222-3 du code du sport, le décret n° 66-619 et les arrêtés sont hors corpus.

## Résumé

- 12 constats : 8 réglés par le texte actuel, 2 doublons (RT-P1-TRAVAIL-B-03) corrigés, 2 nouveaux (RT-ISS12-01 et RT-ISS12-02, P2) corrigés. S'y ajoute 1 alerte non retenue.
- 13 lignes `replace`, validées sans problème. 3 corps de texte changent : L8241-1, L7123-13 et D5424-69. Les 10 autres lignes ne changent que les notes et les motifs.
