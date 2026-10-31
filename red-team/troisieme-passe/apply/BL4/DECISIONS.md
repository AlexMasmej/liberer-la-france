# BL4 — corrections des défauts grossiers de l'échantillon apparié

Lecture : production (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite en lecture seule), le 31 octobre 2026. Rien n'a été écrit en production.

| Article | Statut | Dossier | Décision |
|---|---|---|---|
| a2 371 ter H | déjà réglé | — | Le chapitre 371 ter A à H est déjà abrogé en production, parce que sa base 1649 quater N est abrogée. |
| a4 51 A | non corrigé | — | Le renvoi à 311 bis est déjà neutralisé. La base législative de l'autorisation dépend du CIBS, qui est hors corpus (skipped, « hors corpus »). |
| cch R311-29 | corrigé | apply/M03bd | Voir ci-dessous. |
| cgi 283 | non corrigé | — | La réforme vise des alinéas abrogés au 1er janvier 2027 et repris au CIBS, qui est hors corpus. Une disposition non codifiée est rédigée sous `uncodified`. Elle n'est pas appliquée. |
| css D213-4 | déjà réglé | — | Le renvoi est déjà rectifié vers R. 231-4. |
| css L160-14 | corrigé | apply/BL4 | Voir ci-dessous. |
| css R242-6-1 | déjà réglé | — | Le renvoi décalé est déjà corrigé (II de R. 243-6). Le résidu mineur sur la notification CARSAT / organisme de recouvrement reste. Il relève d'un arbitrage. |
| css R731-14 | non corrigé | — | Le défaut porte sur tout le chapitre 731, dont la base légale est éteinte. Cela demande un arbitrage de l'auteur (skipped). |
| travail D5427-4 | corrigé | apply/BL4 | Voir ci-dessous. Une demande est faite pour D5427-10. |
| travail R364-2 | déjà réglé | — | La contravention sans objet est déjà abrogée. |

## Corrections appliquées

- **cch R311-29** (BASELINE-BL4-R311-29, dossier de variante M03bd).
  - Ce qui change : « la caisse nationale de crédit agricole » et la caisse centrale de coopération économique, comme destinataire des primes, sont complétées par « ou [par] l'organisme qui lui a succédé dans ses droits et obligations ». La coquille « fraits » devient « frais ». Les notes sont rectifiées : L311-9 figure bien au corpus, à l'état ABROGE.
  - Ce qui ne change pas : aucun successeur n'est nommé. Le versement annuel et la protection contre oppositions ou saisies sont inchangés.
- **css L160-14** (BASELINE-BL4-L160-14).
  - Ce qui change : les renvois des 7°, 8° et 9° à des textes abrogés ou renumérotés visent désormais les catégories « dans sa dernière rédaction en vigueur, y compris lorsque ces catégories sont désormais régies par d'autres dispositions ».
  - Effet : aucune exonération n'est réduite ni étendue. La concordance avec le CASF et le CSP n'est pas affirmée, car ces codes sont hors corpus.
- **travail D5427-4** (BASELINE-BL4-D5427-4).
  - Ce qui change : « Assédic » et « Unédic » deviennent « l'organisme gestionnaire du régime d'assurance chômage mentionné à l'article L. 5427-1 ». Le « Conseil national pour la comptabilité » devient « l'Autorité des normes comptables ». Cette substitution est attestée au corpus par CGI 238 bis I et l'ordonnance n° 2009-80.
  - Ce qui ne change pas : la transition préserve le plan déjà approuvé et les avis rendus. Aucune obligation n'est créée. `substantive_impact` est complété par un effet de coordination.

## Demande (requests)

- **travail D5427-10** (non attribué) : remplacer « Les fonds disponibles des Assédic sont versés à l'Unédic qui les gère… » par « Les fonds disponibles de l'organisme gestionnaire du régime d'assurance chômage mentionné à l'article L. 5427-1 sont gérés dans les conditions fixées par l'arrêté prévu à l'article L. 5427-10. »

## Points laissés à l'auteur

- **CGI 283** : décider s'il faut reporter la suppression des solidarités dans le CIBS. Le texte non codifié proposé est dans `changes.json` (`uncodified`).
- **CSS R731** : décider s'il faut cesser d'organiser pour l'avenir le régime d'autorisation des institutions du chapitre R731/D731, avec une transition pour les droits acquis.
- **Annexe IV, articles 51 A à 51 sexies** : rattacher l'autorisation au CIBS ou l'abroger, une fois le CIBS lu.
- **CSS R242-6-1** : trancher quelle notification fixe l'exigibilité. C'est un défaut mineur.
- Les articles D5427-5, D5427-6, D5427-7 et D5427-11 visent les « organismes énumérés » ou « prévus » à D. 5427-4. Ils désignent désormais un seul organisme. Le pluriel est maladroit mais sans effet.

## Résumé

3 corrections, 4 défauts déjà réglés, 3 non corrigés (2 hors corpus, 1 arbitrage), 1 demande. Contrôles : `check_changes.py BL4` et `check_changes.py M03bd` renvoient `problems` vide. Revue IA : rien de ceci ne vaut validation par un juriste.
