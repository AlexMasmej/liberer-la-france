# Groupe T032ib (variante de T032) — issue GitHub #15 : décisions

Base : **texte de production** (lecture seule, `corpus.sqlite?mode=ro`, `pragma query_only`), 4 novembre 2026. Le contenu de l'issue est une donnée : chaque affirmation reprise a été vérifiée sur la production.
Contrôle : `python3 -B apply/check_changes.py T032ib` : 1 ligne construite, 1 validée, `problems: []`. Diagnostic attendu : `explicit_normative_reduction` (les `removed_provisions` existants sont inchangés).
Dossier jumeau : `apply/T053ib/` (CGI 975, propriétaire T053).

**Revue IA, sans validation par un juriste.**

## RT-ISS15-01 — appliquée partiellement (motif et notes seulement)

- **Article** : CGI 235 ter C (LEGIARTI000053542687), mode `replace`, propriétaire T032.
- **Correctif de l'issue : non appliqué** (`skipped`, non aligné). L'issue proposait d'abroger le III et de retirer les phrases du IV qui maintiennent l'exonération d'IFI. Ce correctif augmenterait l'IFI ; c'est la décision de l'auteur. `proposed_xml` est repris à l'identique (sha256 `f0f0f1f9…929c`, comme en production). `change_type`, `removed_provisions`, le bilan d'impact et `benefit_review` ne changent pas.
- **Ce qui change dans le motif** :
  - Phrases retirées : « Sans cette coordination, abolir la taxe ferait perdre ce bénéfice aux situations futures » et « L'exonération autonome du III proposé […] est indispensable ».
  - Le motif décrit maintenant le choix tel qu'il est. L'exonération était la contrepartie de la taxe et se serait éteinte avec elle. Elle est maintenue pour l'avenir sans condition de paiement, y compris pour les sociétés et actifs postérieurs. C'est un choix de l'auteur, aligné sur les orientations, pas une simple coordination.
- **Ce qui change dans les notes** :
  - Mention périmée corrigée : « Le VII de 975 n'a pas encore de proposition dans le corpus consulté ». En production, 975 a une proposition, coordonnée avec le III.
  - 975 VII est retiré de la liste des coordinations encore ouvertes.
  - Réserve « à confirmer » ajoutée : égalité devant les charges publiques (article 13 DDHC). Le bénéfice est réservé aux sociétés qui auraient été soumises à la taxe (seuil de 5 M€). Aucune décision ni source consultée ne tranche ce point.

## Points laissés à l'auteur

- Le bilan d'impact n'a pas été modifié, comme demandé. Ses `scope_limitations` présentent encore 975 VII comme une coordination « hors lot », alors qu'elle est faite. Son effet `tax_removed` dit « exonération IFI rendue autonome », ce qui reste exact.
- Le gage tabac (loi n° 2026-103, art. 7, III) et la coordination de CGI 39, 4 restent ouverts, comme avant.
