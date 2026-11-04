# Groupe I17 — issue GitHub #17 (L600-8 du code de l'urbanisme) : décisions

Base : **texte de production actuel** (lecture seule, `corpus.sqlite?mode=ro`, 4 novembre 2026). Décision de l'auteur : issue **acceptée**. Le contenu de l'issue est traité comme une donnée ; chaque affirmation reprise a été vérifiée sur la production.
Contrôle : `python3 -B apply/check_changes.py I17` → 1 ligne construite, 1 validée, `problems: []`, aucun diagnostic. Variante liée : `apply/T044ia/` (CGI 635, propriétaire T044), validée elle aussi.

**Revue IA : rien de ceci ne vaut validation par un juriste.**

## RT-ISS17-01 — appliquée

### L600-8 (LEGIARTI000037667978, sans propriétaire, lot `automatic-urbanisme/00051.json`), mode `replace`

- Ce qui change : le texte en vigueur est rétabli mot pour mot. Il exige l'enregistrement dans le mois et permet la répétition de la contrepartie pendant cinq ans. Seule correction : au quatrième alinéa, « prévue à l'alinéa précédent » devient « prévue au deuxième alinéa ».
- Métadonnées : `change_type`, `reform_policy_id` et `removed_provisions` sont mis à `null`. `substantive_impact` passe en `coordination_only`, sans effet. `reason`, `review_notes`, `benefit_review`, `assessment`, `scope_limitations` et `new_burdens_review` reprennent les textes de l'issue, après vérification. Une phrase sur l'origine du texte, une sur la différence de champ avec 635 et la phrase « Correction de la troisième passe » sont ajoutées.
- Vérifié sur la production :
  - la source citée par l'issue est exacte ;
  - le brouillon remplacé dispensait d'enregistrement les transactions nouvelles et retirait la répétition ;
  - le renvoi « à l'alinéa précédent » visait bien l'alinéa sur les associations, qui ne contient pas l'action en répétition ;
  - le XML LEGI confirme l'origine du texte : version de 2013 créée par l'ordonnance n° 2013-638, art. 3 (LEGIARTI000027728724) ; version en vigueur modifiée par la loi n° 2018-1021 (ELAN), art. 80 ;
  - la consigne « Ne pas supprimer au hasard une protection essentielle contre […] la fraude […] ou le recours au juge » figure bien dans `policy-coordinations.json` ;
  - le texte proposé compte 204 mots (`\w+`), comme l'annonce l'issue ;
  - aucun terme périmé (`dispens`, « réduction de fond », « transactions nouvelles », « répétition automatique », `fin-enregistrement`) ne reste dans l'entrée.
- Le rapport Labetoulle n'est pas au corpus. Il n'est pas cité dans le motif.
- Alignement : le texte rétabli garde une sanction contre les recours rémunérés contre les permis. Cette sanction protège le constructeur. Elle sert l'objectif de construire plus et d'éviter les recours abusifs. Elle ne crée aucun impôt, puisque 680 exonère ces transactions. Elle ne crée pas non plus de formalité qui n'existait pas dans la source.

### CGI 635 (LEGIARTI000042911346, propriétaire T044) → `apply/T044ia/`

- Le 9° du 1 retrouve sa rédaction source.
- Sont retirés : la ligne L600-8 de `removed_provisions`, l'effet `transactions-urbanisme-dispense-enregistrement` et les phrases sur la dispense dans `reason`, `assessment`, `scope_limitations` et `review_notes`.
- Les réductions du 5° du 1 et du 7° du 2, avec leurs effets et leurs transitions, sont inchangées. Le seul changement du corps est le 9° du 1 (vérifié par diff contre le lot de production).

## Autres propositions qui renvoient à la dispense

Recherche dans tous les brouillons de production (`proposed_xml`, `reason`, `review_notes`) des motifs « 600-8 », « 9° du 1 de l'article 635 », « 635, 1, 9 », « transactions-urbanisme », « désistement du recours », et des textes qui réunissent transaction, recours et permis. Seuls quatre articles en sortent : L600-8, CGI 635, CGI 680, et deux versions de CGI 31, qui sont des faux positifs (« frais […] de transaction » des fonds de placement immobilier). Aucune source en vigueur ne cite L600-8.

- **CGI 680** (LEGIARTI000027729145, lot `poursuite-20261020-c-reviewed/001.json`) : **aucune modification**. Sa proposition maintient « Les transactions mentionnées au 9° du 1 de l'article 635 […] demeurent exonérées de cette imposition fixe ». Ses notes disent que « 635, 1, 9° conserve « le désistement du recours pour excès de pouvoir […] » ». Elle devient cohérente avec le 9° rétabli.

## Points laissés à l'auteur

- Une différence de champ vient de la source : L600-8 vise aussi l'engagement de « ne pas introduire de recours », alors que 635, 1, 9° ne vise que le désistement. Elle est signalée dans les notes et n'est pas élargie.
- La proposition de 680 supprime le droit fixe de 125 € pour tous les actes innomés. Son exonération propre des transactions du 9° devient donc surabondante, sans être contradictoire. Elle n'est pas touchée.
