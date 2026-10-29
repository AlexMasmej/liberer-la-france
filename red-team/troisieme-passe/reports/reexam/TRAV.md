# Réexamen TRAV : instantané 20261026T230545Z vers 20261027T044303Z

Revue IA, provisoire. Elle ne vaut pas validation par un juriste. La seconde passe est arrêtée (statut `blocked`) ; les articles encore `pending` peuvent changer à sa reprise.

## Synthèse

Le paquet compte 15 objections, issues des dossiers P1-TRAVAIL-A, P1-TRAVAIL-B, P1-NEW et DOM-SUCC. RT-P1-TRAVAIL-B-13 est une instance fusionnée de A-11 et elle est traitée avec elle.

| Verdict | Nombre | Objections |
|---|---|---|
| maintenue | 7 | B-04 (P1), DOMSUCC-03, DOMSUCC-06, A-08, A-13, B-10, B-15 (P2) |
| reformulée | 4 | DOMSUCC-01 (P1), A-03 (P1 → **P2**), B-12, B-19 (P2) |
| résolue | 4 | DOMSUCC-02, DOMSUCC-07, NEW-02, A-11 (avec B-13) |
| obsolète | 0 | — |

Changement de priorité : seule A-03 change, de P1 à P2. Après réexamen, il reste 2 objections P1 dans ce groupe : DOMSUCC-01 et B-04.

Nouveaux constats : 3, tous en P2.
- **RT-RXTRAV-01** : CSS R133-14 IV 2° et 3°. Si le décret entre en vigueur avant les abrogations législatives de L1221-16, L1221-18 et L1251-46, la DSN cesse de satisfaire ces trois formalités pendant l'intervalle. Statut : à confirmer.
- **RT-RXTRAV-02** : R3134-4 reste maintenu. Il organise toujours une décision préfectorale et une consultation que L3134-14 proposé supprime. Ce défaut existait déjà avant le nouvel instantané, mais il ne figurait pas au registre.
- **RT-RXTRAV-03** : la note de L3134-16 dit que la CSA est maintenue par L3133-7, alors que ce texte la supprime désormais.

Les 9 alertes P1 liées ont été requalifiées. 8 sont écartées : le renvoi est maintenant transitoire, neutralisé ou retiré. 1 reste une coordination manquante : L4641-2-1 renvoie toujours à L4622-9-3.

## Points principaux

1. **DOMSUCC-01 (reformulée, P1)**. Le défaut subsiste dans 750 ter II, 792-0 bis II 2, 792 bis, 757 B et 990 I. Il s'aggrave dans 784 C. Le texte remplace « droit de mutation par décès » par « aucun droit de mutation à titre gratuit ». Son motif annonce vouloir « empêche[r] de rétablir le prélèvement sous la qualification de donation ». Une libéralité graduelle consentie par un donateur vivant échappe donc à tout droit au décès du premier donataire. C'est contraire à successions[4] : l'auteur n'a pas supprimé les droits de donation. La correction doit désormais viser 784 C lui-même ; le texte est dans TRAV.json. Le volet assurance-vie (souscripteur distinct de l'assuré) est affaibli par successions[0], qui vise expressément les capitaux d'assurance-vie dénoués par décès. Ce volet est à trancher par l'auteur.
2. **A-03 (reformulée, P1 → P2)**. L3142-29 est réécrit : son renvoi à L3142-114 est retiré, et le report combiné est interdit aussi pour le sabbatique (option B). L3142-32 4° est corrigé. Il ne reste que D3142-21, inchangé et toujours en `pending`. Il renvoie à un alinéa de L3142-29 qui ne prévoit plus de report, et à D3142-75, abrogé. La correction proposée est son abrogation, avec transition. L'option B a été choisie par la seconde passe : l'auteur doit la confirmer.
3. **B-04 (maintenue, P1)**. Seules les notes ont changé. Elles reconnaissent désormais la « contradiction effective hors lot ». R3132-16 et R3132-17 restent inchangés et gardent le circuit préfectoral.
4. **Objections résolues** :
   - **DOMSUCC-02** : 754 A exclut désormais tout droit « à titre gratuit ou à titre onéreux » sur l'accroissement.
   - **DOMSUCC-07** : 754 B rétablit les I et II de la source et ne contient plus de présomption générale hors décès.
   - **NEW-02** : R184-8 neutralise la contravention déclarative et garde la 3e classe, la 5e classe et la récidive.
   - **A-11 et B-13** : L3134-16 et L3422-1 sont bornés à la rédaction antérieure.

   Pour chacune, j'ai vérifié qu'aucune faveur n'est perdue, qu'aucune formalité n'est créée et qu'aucun renvoi n'est cassé.
5. **Point connexe, non recompté**. L3133-7 2° supprime désormais la CSA, en alignement sur CSS L137-40 proposé. La contradiction de RT-P1-CSS-A-04 est donc levée dans le sens de la suppression. Ce point relève du groupe CSS.

## Contrat unique

Les propositions de L1234-1, L1234-3, L1234-9, L1237-1, R1234-1, R1234-2, R1234-4 et L1221-19 sont identiques dans les deux instantanés, avec les mêmes empreintes. Leur texte respecte l'invariant :
- préavis de 15 jours calendaires de chaque côté ;
- aucune indemnité ordinaire avant un an, seuil apprécié à la fin effective du contrat, préavis inclus ;
- ensuite 0,20 mois par année totale, au prorata des mois complets, plafonné à 6 mois ;
- indemnité due seulement quand l'employeur rompt.

Les nouvelles propositions du périmètre qui touchent la rupture ne modifient pas l'invariant : R133-14 II 2°, V 3° h et dernier alinéa, L3133-7, L3422-1, et les notes de L3142-28, L3142-113 et L3132-20.

## Méthode et couverture réelle

Pour chaque objection, j'ai relu l'objection complète dans `reports/register.json`. J'ai lu en entier l'ancienne version (export `20261026T230545Z`) et la nouvelle (`cite.py`, export `20261027T044303Z`) de chaque article de l'objection, modifié ou non : source, proposition, motif et notes. J'ai comparé les empreintes des deux manifestes.

Articles lus :
- 73 versions d'articles distinctes dans les objections. La version future de R3324-22 (LEGIARTI000052845711) est hors inventaire.
- Lus en plus :
  - contrat unique : L1234-1, L1234-3, L1234-9, L1237-1, R1234-1 ;
  - travail L1221-16, L1221-18 et R3134-4 ;
  - CSS L137-40 ;
  - orientations `policy-coordinations.json` : travail, successions et recherche CSA ;
  - entrée SOLIDARITE de `dedupe.json`.

Non examiné :
- textes hors corpus : code civil (art. 1048 à 1061), code monétaire et financier, CASF, BOFiP, arrêtés préfectoraux et arrêtés DSN ;
- D3142-68, D3142-76 et la cohérence d'ensemble des neuf recueils.

Aucune source extérieure n'a été consultée. Aucun fichier de production, de l'instantané ou d'un autre agent n'a été modifié. Les seules écritures sont `reports/reexam/TRAV.json`, le présent fichier et les exports de `cite.py`.
