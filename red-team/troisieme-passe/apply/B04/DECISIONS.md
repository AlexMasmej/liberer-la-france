# B04 : objections P2, décisions

J'ai lu la production en lecture seule le 29 octobre 2026 (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`). Les exports sont dans `evidence/cited/production-20261029/`. Le registre (`reports/register.json`) date d'un instantané ancien, et chaque objection a donc été confrontée au texte actuel.

Contrôle :
- `python3 -B apply/check_changes.py B04` : 14 lignes construites, 14 validées, `problems` vide.
- `python3 -B apply/check_changes.py B03b` : 1 ligne, `problems` vide.
- Diagnostics, tous voulus : changements de longueur et de renvois mesurés par rapport à la source officielle, et réductions déjà déclarées.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Décision | Objections |
|---|---|
| Appliquées | RT-P1-CSS-A-02, RT-P1-CSS-A-03, RT-P1-CSS-A-19, RT-TR1-02, RT-ISS8-01, RT-FUTFISC-16 |
| Appliquées en partie (le reste est déjà réglé) | RT-FUTFISC-07, RT-FUTFISC-28, RT-FUTFISC-29, RT-FUTFISC-15 (variante B03b) |
| Déjà réglées | RT-ISS2-01, RT-ISS6-01, RT-ISS9-01, RT-FUTFISC-31 |
| Non appliquées | RT-FUTFISC-32 (hors corpus), RT-RXALERTS2-01 (à confirmer, arbitrage) |

Volume :
- 14 changements dans `apply/B04/changes.json` : 11 en mode `replace` et 3 en mode `new`.
- 1 changement dans la variante `apply/B03b/` (1586 ter appartient à B03).
- 1 disposition non codifiée (`uncodified`).
- Aucune demande (`requests`), aucune fermeture de faille.

## Appliquées

**RT-P1-CSS-A-02 : CSS L138-7 (LEGIARTI000006740397).**
- Ce qui change : le recouvrement ne se fonde plus sur L. 138-22, que le projet abroge. Ce renvoi est limité aux obligations et responsabilités nées avant l'abrogation.
- Notes : celle qui disait « L138-22 conserve le représentant » est rectifiée.

**RT-P1-CSS-A-03 : CSS L138-20 (LEGIARTI000051287267) et R138-19 (LEGIARTI000042389712, notes seules).**
- Ce qui change : L138-20 reçoit un dernier alinéa. Les contributions de L. 245-1, L. 245-5-1 et L. 245-6 n'y sont plus recouvrées que pour leur stock, et aucune déclaration n'est due pour les charges ou années qui leur sont soustraites.
- Une entrée `removed_provisions` est ajoutée.
- Les notes contraires des deux articles sont rectifiées.

**RT-P1-CSS-A-19 : CSS L131-8 (LEGIARTI000053538201).**
- Ce qui change : le 3° ter ne répartit plus que la contribution casino due au titre des faits générateurs antérieurs à sa suppression, avec ses régularisations et restitutions.
- Non examiné ici : la coordination du 3° avec L. 136-8 I 3°.

**RT-TR1-02 : travail L6323-4 (LEGIARTI000054703482).**
- Ce qui change : le I, second alinéa, reprend le double critère déjà retenu par L6323-7, R6323 et R6333-3. La participation n'est pas due si la demande de souscription ou l'inscription est postérieure à la loi. L'ancien régime reste pour les formations où les deux événements sont antérieurs.
- `substantive_impact` (citation exacte) et `removed_provisions` sont mis à jour. La note qui préconisait l'alignement inverse est rectifiée.

**RT-ISS8-01 : travail L2353-27 (LEGIARTI000006902274), L2363-6 (LEGIARTI000033023049) et L2373-3 (LEGIARTI000047591165).**
- Ce qui change : L2353-27 écrit une fois, de façon autonome, la règle de l'ancien L2325-44. Elle comprend :
  - cinq jours au plus, dans les conditions de L. 2145-11 ;
  - un temps de formation rémunéré, non déduit des heures de délégation et imputé sur le congé de formation économique, sociale et environnementale et de formation syndicale ;
  - un financement par le comité ;
  - un renouvellement après quatre ans de mandat.
- Écartés de la règle autonome : le seuil de cinquante salariés et la condition d'organisme agréé de l'ancien texte.
- L2363-6 et L2373-3 ne gardent, au troisième alinéa, que la prise en charge par leur propre comité. La numérotation des alinéas est conservée.
- Notes : celles qui disaient la dernière rédaction de L2325-44 absente du corpus sont rectifiées (elle y figure : LEGIARTI000033023366). Les motifs de L2363-6 et L2373-3, qui reposaient sur un renvoi supposé à L2315-63, sont aussi rectifiés.
- Points laissés à l'auteur : faut-il reprendre la condition d'organisme (option b de l'objection) ? Faut-il restreindre le droit aux titulaires élus pour la première fois (option c, déconseillée) ?

**RT-FUTFISC-16 : CGI 1649 quater E (LEGIARTI000046875411) et 1649 quater H (LEGIARTI000046875405), versions 2030, mode `new`.**
- Solution codifiée, préférée à la disposition non codifiée de l'objection.
- Ce qui change : ces versions différées sont déclarées abrogées et sans objet (`full_repeal`). Elles ne rétablissent aucune obligation des centres et associations de gestion agréés, dont le régime a été abrogé en 2025. Les droits et obligations de la période d'agrément sont conservés. Aucune formalité de remplacement n'est créée.
- Réserve : le JORF de l'article 55 de la loi de finances pour 2023 n'a pas été relu.

## Appliquées en partie

**RT-FUTFISC-07.**
- Déjà réglé : les versions 2027 portent leur proposition (balayages W14 et RT-FUTTL-02). Celle de 1740 D étend l'abrogation aux publications fondées sur la rédaction 2027.
- Appliqué (notes seules) : 1740 D, version expirante (LEGIARTI000044981533). La note « destination future non fournie » est rectifiée.
- Appliqué (`uncodified`) : une disposition non codifiée. Les abrogations visent la rédaction en vigueur à la publication, y compris celle issue de l'ordonnance n° 2025-1247. Aucune disposition du CIBS ne peut instituer une imposition de même fait générateur et de même assiette pour les années supprimées. Le stock et les affectations sont réservés.
- Point laissé à l'auteur : la portée de l'article 17 de l'ordonnance n° 2025-1247 (borne 2222-02-22) n'a pas été vérifiée au JORF.

**RT-FUTFISC-28.**
- Déjà réglé : 44 sexies-0 A en 2029, 44 quaterdecies et 1388 quinquies en 2031 (W14).
- Appliqué (mode `new`) : 199 terdecies-0 A ter, version 2029 (LEGIARTI000053570759). Le texte officiel est repris sans changement : 3° et taux de 40 % abrogés, sans prorogation. Le dernier alinéa du projet y est ajouté : allègements de 199 terdecies-0 A et survie des droits acquis jusqu'au 31 décembre 2028.
- Point laissé à l'auteur : toute prorogation des faveurs temporaires suppose une décision expresse.

**RT-FUTFISC-29.**
- Déjà réglé, sur le fond, par les versions 2027 :
  - 238 bis : « 6. (Abrogé). » ;
  - 1729 B : 238 bis retiré du 1.
- Appliqué (notes seules) : 1729 B (LEGIARTI000043982240) et 238 bis (LEGIARTI000054402913), versions expirantes. Les notes qui disaient le successeur absent du corpus sont rectifiées. Les corps sont inchangés.

**RT-FUTFISC-15 : variante `apply/B03b/` (1586 ter, LEGIARTI000048847020, propriétaire B03).**
- Ce qui change : le bilan de la mesure `suppression-cvae` est corrigé dans `substantive_impact.scope_limitations`, dans `conditions_and_transition` et dans les notes. Il s'agit d'une accélération de la suppression légale déjà programmée pour 2030 : le gain propre porte sur les années allant jusqu'à 2029, à des taux maximaux déjà réduits (0,19 % en 2028, 0,09 % en 2029). Une seule mesure est comptée, les coordinations ne sont pas des baisses, et aucun chiffrage n'est inventé.
- Corps et motif inchangés.
- Point pour le coordinateur : B03 n'avait pas modifié cet article à la date de ce travail. S'il le fait, il faudra fusionner.

## Déjà réglées (texte actuel cité dans `skipped`)

- **RT-ISS2-01** : L1234-1 porte déjà la lecture (a). Les ruptures notifiées après une conversion suivent les quinze jours, et l'ancienneté et les créances sont conservées.
- **RT-ISS6-01** : CSS L241-17 vise déjà « l'article L. 3123-22, pour les heures accomplies au-delà de la durée déterminée par l'avenant ». La note de L3123-8 est périmée ; elle n'est pas corrigée, car ce n'est pas l'objet de l'objection.
- **RT-ISS9-01** : la phrase de L1233-46 a été supprimée, et les notes de R1233-3-5 sont à jour.
- **RT-FUTFISC-31** : la version 2027 de 302 bis ZL renvoie aux règles de la date d'exigibilité (annexe 287, puis L. 161-1 du CIBS), sans la phrase contradictoire.

## Non appliquées

- **RT-FUTFISC-32** (hors corpus). C'est une réserve documentaire sur la consolidation LEGI : elle relève d'un signalement à la DILA. Aucune proposition ne recopie les anomalies. La visée de la rédaction en vigueur est couverte par la disposition non codifiée de RT-FUTFISC-07.
- **RT-RXALERTS2-01** (à confirmer, arbitrage). Si 232 n'est plus réécrit, le zonage « autonome » du I, sur lequel s'appuient d'autres propositions, disparaît. La correction de R642-1 dépend aussi du choix fait pour 232.
  - Choix laissé à l'auteur : abandonner la réécriture de 232, ou le rétablir expressément, en limitant ce rétablissement au I.
  - La disposition non codifiée facultative de lecture des renvois de zonage n'est pas proposée, parce qu'elle contredirait le maintien du I.

## Résumé

- 6 objections appliquées.
- 4 appliquées en partie, dont RT-FUTFISC-15 par la variante B03b.
- 4 déjà réglées.
- 2 non appliquées : RT-FUTFISC-32 (hors corpus) et RT-RXALERTS2-01 (arbitrage).

Aucune correction ne crée d'impôt, de formalité ou de condition nouvelle. Aucune ne supprime une faveur ou un droit acquis.

Revue IA, sans validation par un juriste.
