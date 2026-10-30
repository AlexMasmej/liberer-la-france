# X10 : renvois à des articles abrogés laissés par X8 et X9 (+ quatre pistes de régression)

Texte lu en production le 30 octobre 2026, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py …`, base et lots ouverts en lecture). X8, Z05, Z07, X9 et B02x sont déjà appliqués dans l'état lu.

Validation : `python3 -B apply/check_changes.py` donne `problems` vide pour X10 (2 lignes), Z07w (1) et W07w (1). Les diagnostics sont voulus : `explicit_normative_reduction` sur les abrogations déclarées, `length_change` ×4,0 sur 164 F septvicies (alinéa de transition), et `references_changed` sur R753-2 (R315-16, R371-9 et R371-10 ajoutés par les nouvelles bornes et la phrase de prise d'effet).

## 1. Annexe IV, 164 F septvicies (LEGIARTI000006301050, sans propriétaire) : appliquée dans X10 (`replace`, `full_repeal`)

- **Défaut.** La proposition faisait encore porter par les associations « l'obligation d'affichage définie au 1° de l'article 164 F quinvicies et la mention prévue au 1° de l'article 164 F sexvicies » à la connaissance des adhérents, et l'association « s'assure de leur exécution effective ». Or ces deux articles sont abrogés (Z07 et X9), de même que 164 F quatervicies, 164 F octovicies et 371 Y de l'annexe II (X8). L'article n'avait plus d'autre fonction.
- **Ce qui change.** L'article est abrogé pour l'avenir : plus d'information des adhérents, plus de contrôle par l'association, plus de compte rendu écrit, et rien ne les remplace. La transition est la même que pour les articles voisins : avantages de l'adhésion conservés, obligations autonomes maintenues, situations antérieures régies par les anciennes règles sous réserve de la loi répressive plus douce.
- **Bilan.** Il est classé `material_reduction`, mais aucune réduction n'est comptée deux fois. La suppression du compte rendu écrit était déjà comptée (`associations-agreees-fin-attestation-affichage`, mesure inchangée). L'information et le contrôle sont rattachés comme `coordination` à `associations-agreees-publicite-adhesion-supprimee`.

## 2. Réserve morte du « 3° de l'article 371 Y » : appliquée

- **164 F quatervicies (LEGIARTI000006301047, sans propriétaire), dans X10.**
  - Ce qui est retiré : « ni l'acceptation des moyens de paiement prévue au 3° de l'article 371 Y de l'annexe II ». La phrase devient : « Elle ne supprime pas les avantages fiscaux légalement attachés à l'adhésion… ».
  - Ce qui change aussi, pour supprimer les mentions devenues fausses : le motif, `benefit_review`, `repeal_scope`, ainsi que `scope_limitations`, `new_burdens_review` et l'effet `after` du bilan.
  - Les notes de revue sont complétées.
  - Le reste du corps est inchangé, y compris la phrase qui neutralise quinvicies, sexvicies et le 4° de 371 Y.
- **164 F quinvicies (LEGIARTI000006301048, groupe Z07), dans la variante `apply/Z07w/`.**
  - Ce qui est retiré : « ni l'acceptation des moyens de paiement prévue au 3° de l'article 371 Y de l'annexe II au code général des impôts ». La phrase devient : « Cette abrogation ne modifie pas les avantages attachés à l'adhésion… ».
  - Le motif, `repeal_scope` et le bilan sont alignés ; les notes rendues fausses sont rectifiées.
- **Pourquoi aucune faveur n'est retirée.** L'obligation d'accepter le chèque ou la carte reposait seulement sur le 3° de 371 Y. X8 l'a abrogé en entier, avec sa propre transition, parce que son fondement (CGI 1649 quater F et G) est abrogé depuis le 16 février 2025.

## 3. CCH L181-13, 5° (LEGIARTI000046120795) : déjà réglé, aucune modification

- **Ce que dit la production.** La proposition porte déjà « 5° Abrogé. Aucune suspension ou aucun retrait de l'agrément spécifique auparavant prévu à l'article L. 122-12 ne peut faire obstacle, pour l'avenir, à l'établissement d'attestations… ». Le contradictoire est limité aux « 1° à 4° », et les effets futurs des anciens retraits sont neutralisés.
- **L122-12 proposé (LEGIARTI000046123669).** Il supprime bien l'agrément : « L'établissement de ces attestations n'est subordonné à aucun agrément spécifique au titre du présent article… ». Les deux textes sont donc cohérents.
- **Origine de la remarque de Z05.** Elle portait sur le texte source : l'instantané du 29 octobre et la production ont la même proposition.
- **Version 2028.** Le corpus n'a aucune version 2028 de L181-13, ni de version future de L122-12.

## 4. Pistes de régression ajoutées par le coordinateur

| Article (LEGIARTI) | Renvoi | Qualification | Suite |
|---|---|---|---|
| CSS R753-2 (…53335775, groupe W07, maintenu) | « R. 371-8 à R. 371-11 » | **G**, F3 : la liste d'extension territoriale (collectivités de L751-1) rend encore applicables R371-10 et R371-11, abrogés par X8 (E152). Ce n'est ni une date ni une neutralisation. | **Corrigé** dans la variante `apply/W07w/` (`replace`, l'article passe de maintenu à réécrit, `coordination_only`). |
| CCH R165-2 (…43819313, groupe J07) | R165-16 | faux positif : simple neutralisation datée, « À compter de l'abrogation de l'article R. 165-16, aucun document de suivi de l'agenda n'incombe… » | Aucune. |
| CCH R165-18 (…43819359, groupe J07) | R165-16 | faux positif : la mention sert seulement à interdire de demander « l'établissement ou la transmission des documents de suivi supprimés à l'article R. 165-16 ». | Aucune. |
| CCH R165-19 (…43819361, groupe W12) | R165-16 | faux positif : la mention sert seulement à interdire mise en demeure et sanction fondées sur l'absence « des documents de suivi supprimés à l'article R. 165-16 ». | Aucune. |

**Correction de R753-2 en détail.**
- La plage « R. 371-8 à R. 371-11 » devient « R. 371-8, R. 371-9 ».
- Hors piste, la même liste vise « R. 315-1 à R. 315-17 ». Or R315-17 (LEGIARTI000037258478, rapport annuel sur les accords préalables) est abrogé par le projet. La plage devient « R. 315-1 à R. 315-16 ». C'est le même défaut dans le même article ; le corriger évite de toucher l'article une seconde fois.
- Une phrase finale fixe la prise d'effet : le retrait vaut « à la date de leur abrogation ».
- Rien d'autre ne change. Les doubles virgules et les graphies de la source (« R. 361-3à », « R. 376-1et ») sont conservées, sans réécriture de style.
- Aucune autre cible abrogée n'a été trouvée dans les plages R31x à R37x et R742 de la liste.

## Points laissés à l'auteur

- **R165-19.** Le premier alinéa garde un déclencheur de mise en demeure « lorsque les documents de suivi sont manifestement erronés ». Il ne vise pas R165-16 et peut encore servir pour les documents transmis avant l'abrogation : il n'a pas été modifié. À revoir si l'auteur veut le limiter aux documents antérieurs.
- **R753-2.** La vérification de renvoi relative à R371-8, dans la ligne de lot, mentionne encore « La plage R371-8 à R371-11 ». La date de fin de L751-1 (1er janvier 2028) reste non traitée.
- **164 F quatervicies.** Il neutralise encore expressément quinvicies, sexvicies et le 4° de 371 Y, tous abrogés. C'est une neutralisation, sans effet, laissée intacte comme le demandait la mission.

Revue IA, sans validation par un juriste.
