# R2 — demandes de correction du palier A (paquet requests-R2.json)

Texte lu en production, en lecture seule, le 30 octobre 2026. Rien n'a été écrit en production.

Le paquet compte 12 demandes : 6 appliquées, 0 fusionnée et 6 non appliquées. Les 6 demandes non appliquées étaient déjà réglées par le propriétaire de l'article.

Tous les dossiers créés sont validés par `check_changes.py` (`problems` vide) : `R2`, `T017rb`, `Y17rb`, `Y15rb` et `A1rb`. Les dossiers des propriétaires (T095, T082, T125, T126) n'ont pas été modifiés.

## Appliquées

| Demande | Article | Dossier | Ce qui change |
|---|---|---|---|
| TA-T015-01 (T015) | CGI 182 A ter (LEGIARTI000051217999) | `T017rb` | Le III 1 renvoyait au taux du « deuxième alinéa » de 163 bis G, alinéa qui ne fixe plus de taux. Il vise désormais le taux du premier alinéa. Pour les seuls avantages que la transition de 163 bis G laisse sous l'ancienne rédaction, il vise l'ancien taux du second alinéa (30 %). |
| TA-T045-02 (T045) | Annexe III 281 P (LEGIARTI000048806797) | `Y17rb` | Le dépôt n'est plus réservé au service du domicile d'une partie : il peut se faire « auprès de tout service des impôts, dans les conditions de l'article 654 », comme pour 281 E et 281 N. Le motif est corrigé et `removed_provisions` complété. |
| TA-T056-01 (T056) | Annexe II 310 G (LEGIARTI000006295726) | `Y15rb` | Un alinéa facultatif organise le don volontaire des héritiers et légataires que 1131 proposé leur ouvre : offre sans délai, II à IV applicables, aucun droit exigible en cas de refus. |
| TA-T100-01 (T100) | CGI 208 ter (LEGIARTI000027518093, maintenu, sans propriétaire) | `R2` | Le a reçoit l'extension aux livrets supplémentaires que l'annexe III 46 quater-0 B proposé appliquait sans base légale, avec la même transition. L'article passe en `rewrite_draft`, `coordination_only`, avec la même `measure_id` que l'annexe. |
| TA-T110-01 (T110) | Annexe IV 71 (LEGIARTI000006301497, maintenu, sans propriétaire) | `R2` | L'article est abrogé (`full_repeal`), en coordination avec l'abrogation de l'annexe III 301 : il n'autorisait plus que le timbrage pour le timbre de dimension, supprimé depuis 2006. |
| TA-T117-03 (T117) | CGI 1671, version du 1er janvier 2027 (LEGIARTI000053188936) | `A1rb` (`new`) | « faire accréditer » devient « désigner », sans accréditation préalable. Les accréditations et les demandes en cours valent désignation. Le reste de la version 2027, dont le 5 qui renvoie au CIBS L. 180-1, est repris sans changement. |

### Écarts par rapport au texte demandé

- **310 G.** L'offre se dépose auprès de tout service des impôts, et non au service du dernier domicile du défunt. Cela évite toute restriction de lieu, en cohérence avec 654 proposé.
- **71.**
  - Le renvoi « 72 à 75 » devient « 72 à 74 », car l'article 75 n'a plus de version en vigueur (PERIME depuis 1997).
  - Une phrase neutralise le c de 164 M (groupe T131). Ce c exige une « mention particulière à l'usage autorisé et défini à l'article 71 ».
- **1671 (2027).** La coquille « dépôt ;les » est corrigée.

## Non appliquées (déjà réglées)

- **TA-T012-01, annexe III 41 quatervicies A.** La demande est déjà intégrée par T095 (TA-T095-02), avec un `proposed_xml` identique.
- **TA-T024-02, annexe III 41 A.** T095 (TA-T095-03) l'a déjà intégrée, dans une rédaction plus juste : « toute autre **entreprise** » passible de l'IS, comme le dit 211 ter proposé. La rédaction demandée, « toute autre personne », étendrait la déduction au-delà de la loi.
- **TA-T041-02, annexe II 242 nonies C.** L'abrogation est appliquée par T082 (TIERA-T082-01), avec un texte identique.
- **TA-T041-03, annexe IV 50 sexies E.** La demande est appliquée par T125, à l'identique.
- **TIERA-T081-03, annexe IV 50 sexies L.** L'abrogation est appliquée par T125, avec un texte identique et la note sur 202 G corrigée.
- **TIERA-T084-285A, annexe IV 50-0 B.** La demande est appliquée par T126, qui a aussi adapté le f.

## Points laissés à l'auteur

- **1671.** La version en vigueur (LEGIARTI000041471931) relève de la demande du paquet R1. Les deux versions doivent être modifiées ensemble ; sinon, 357 H bis reste contraire à la loi jusqu'au 31 décembre 2026.
- **71.** Le traitement d'ensemble du chapitre des machines à timbrer reste un arbitrage, déjà signalé par T129 (TA-T129-02). Il porte sur 72 à 74, 164 L et suivants, et 405 B de l'annexe III. Les notes de 72 (« 71 et annexe III 301 conservent la faculté ») deviendront inexactes après les abrogations.
- **208 ter.** Si l'auteur ne retient pas l'extension aux livrets supplémentaires, il faut revenir à la source de 46 quater-0 B. La ligne garde un `reference_coherence` calculé sur l'ancien état maintenu, que le coordinateur devra recalculer.

Revue IA, sans validation par un juriste.
