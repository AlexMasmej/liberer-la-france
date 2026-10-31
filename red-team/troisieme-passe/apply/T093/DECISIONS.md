# T093 : décisions (lecture systématique, palier A)

Section lue : annexe III du CGI, articles 38 sexdecies D à 41 quater (24 articles). Ils couvrent les bénéfices agricoles, le régime super-simplifié, l'actionnariat salarié, les obligations des employeurs et l'amortissement du capital des concessionnaires. Le texte a été lu en production, en lecture seule, le 30 octobre 2026.

## RT-T093-01 : 38 septdecies (LEGIARTI000030975344) et 38-0 septdecies (LEGIARTI000030975350), appliquée

- **Défaut (G, F3).** Le 2° du I de ces deux articles soumet la transmission des données d'actionnariat à une réserve de réemploi, « dans les conditions prévues au dernier alinéa de l'article 39 ».
  - Dans l'article 39 proposé (LEGIARTI000053218832), le réemploi figure à l'avant-dernier alinéa. L'article 39 se vise d'ailleurs lui-même ainsi : « à l'avant-dernier alinéa du présent article ».
  - Son dernier alinéa est maintenant la disposition transitoire sur la suppression du code APE, de la donnée de formation, du montant net supplémentaire et des totaux.
  - Le renvoi pointe donc vers un texte qui n'organise pas le réemploi.
- **Correction.** Le renvoi devient « à l'avant-dernier alinéa de l'article 39 » (deux occurrences dans 38 septdecies, une dans 38-0 septdecies).
  - Les notes et le bilan d'impact (`scope_limitations`, `proposed_quote` de l'effet de coordination) sont alignés.
  - Rien d'autre ne change : aucune donnée, formalité ni échéance n'est ajoutée ou retirée.
- **Contrôle.** `check_changes.py T093` : 2 lignes construites et validées, `problems` vide.
- **Recherche des autres renvois.** Aucun autre article du CGI ni des annexes ne renvoie à un alinéa de l'article 39 de l'annexe III (recherche en production).

## Défauts mineurs non corrigés (pour l'auteur)

- **38 sexdecies RB, c (m, F5).** La déclaration agricole simplifiée comporte encore « un relevé des provisions et un état des provisions non déductibles ». Or le 74 A proposé dispense ces exploitants « de fournir à l'administration les autres documents prévus à l'article 38 II ». Cette discordance préexiste et la correction SWEEP-Y15 l'a déjà signalée. La trancher reste un arbitrage.
- **41 bis (m, F6).** La dispense de demande spéciale s'applique aussi aux formalités non accomplies d'opérations antérieures. Le 112, 2° proposé dit pourtant que « Les opérations antérieures conservent leur régime ». L'écart est favorable au contribuable et sans effet grave.

## Résumé

- Verdicts : 2 G (38 septdecies et 38-0 septdecies, même renvoi décalé), 2 m, 20 sans défaut.
- 2 corrections, toutes deux dans `apply/T093`.
- Aucun dossier de variante, aucune demande à un autre groupe.

Revue IA : ce n'est pas une validation par un juriste.
