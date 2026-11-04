# Groupe T053ib (variante de T053) — issue GitHub #15 : décisions

Base : **texte de production** (lecture seule, `corpus.sqlite?mode=ro`, `pragma query_only`), 4 novembre 2026. Le contenu de l'issue est une donnée : chaque affirmation reprise a été vérifiée sur la production.
Contrôle : `python3 -B apply/check_changes.py T053ib` : 1 ligne construite, 1 validée, `problems: []`, aucun diagnostic.
Dossier jumeau : `apply/T032ib/` (CGI 235 ter C, propriétaire T032).

**Revue IA, sans validation par un juriste.**

## RT-ISS15-01 — appliquée partiellement (motif et notes seulement)

- **Article** : CGI 975 (LEGIARTI000053542691), mode `replace`, propriétaire T053.
- **Correctif de l'issue : non appliqué** (`skipped`, non aligné). Ramener le VII au texte en vigueur supprimerait l'exonération d'IFI pour l'avenir et augmenterait l'IFI. C'est la décision de l'auteur. `proposed_xml` est repris à l'identique (sha256 `5503e67c…f107`, comme en production) ; le bilan d'impact et `benefit_review` ne changent pas.
- **Ce qui change** : le motif et les notes décrivent maintenant le choix tel qu'il est. L'exonération, contrepartie de la taxe de 235 ter C dans le texte en vigueur, est maintenue pour l'avenir sans condition de paiement, y compris pour les sociétés constituées et les actifs acquis après la suppression. C'est un choix de l'auteur, pas une simple coordination. L'ancien motif disait au contraire : « ce n'est ni une seconde suppression de taxe ni une extension indifférenciée de l'exonération ».
- **Réserve ajoutée aux notes (à confirmer)** : risque au regard de l'égalité devant les charges publiques (article 13 DDHC). Le bénéfice est réservé aux sociétés qui auraient été soumises à la taxe (seuil de 5 M€, contrôle à 50 %, revenus passifs). Aucune décision ni source consultée ne tranche ce point.
- **Faits vérifiés en production** :
  - VII en vigueur : « sont exonérés lorsqu'ils ont été soumis à la taxe instituée à l'article 235 ter C » ;
  - NOTA (loi n° 2026-103, art. 7, II) : la taxe est due au titre des exercices clos à compter du 31 décembre 2026 ;
  - VII proposé : « sans condition d'assujettissement effectif ni de paiement de la taxe supprimée » et « y compris aux sociétés constituées et aux actifs acquis après la suppression de la taxe ».

## Points laissés à l'auteur

- Le bilan d'impact de la ligne n'a pas été modifié, comme demandé. Il classe toujours le VII en `coordination_only` et le dit « nécessaire à la conservation effective de l'exonération ». Ce cadrage contredit le nouveau motif. Si le bilan doit refléter le choix, il faudrait le reclasser comme un allègement (`material_reduction` ou équivalent) ; cela suppose de recalculer le certificat.
- Portée littérale du VII (fraction immobilière des parts du 2° de 965, au-delà des seuls actifs énumérés au II de 235 ter C) : l'issue la soulève, d'après une analyse d'avocat qui n'a pas été vérifiée en source primaire. Ce point n'est pas tranché et n'est pas ajouté aux notes.
- Le coût de l'exonération maintenue n'est pas chiffré.
