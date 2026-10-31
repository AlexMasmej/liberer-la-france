# R5 — demandes de correction des groupes BL3 et BL4

Lecture en production (lecture seule). Neuf demandes, neuf appliquées dans `apply/R5/`. Aucun article n'avait de propriétaire dans `apply/assignment.json` ni de changement en attente dans les dossiers de `audit/baseline/fix-folders.json`. Contrôle : `python3 -B apply/check_changes.py R5` sans problème.

## CSS D161-6 à D161-12 (objection BASELINE-BL3-D161-13) : appliquée (abrogation)

- **Défaut vérifié :** ces articles organisent encore le Comité national paritaire de l'information médicale. Ce comité était créé par L. 161-30, abrogé depuis le 28 janvier 2016 (LEGIARTI000006740574, état ABROGE).
- **Ce qui change :** les sept articles sont abrogés pour l'avenir, en même temps que D161-13, dont l'abrogation est proposée par BL3 dans `apply/BL3`. Les mandats en cours prennent fin. Les avis et actes antérieurs sont conservés. Les procès-verbaux existants et le secret (D161-11) sont maintenus, ainsi que l'indemnisation des frais déjà exposés (D161-12). Rien ne remplace le comité.
- **Écart avec la demande :** dans D161-9, D161-10 et D161-11, la date n'avait pas d'antécédent dans l'alinéa. Pour la même raison, la première occurrence dans D161-12 est aussi modifiée. Dans ces quatre articles, « avant cette date » devient donc « avant la date mentionnée au premier alinéa ». Pour D161-6 et D161-10, les anciens champs de réduction (`reform_policy_id`, `removed_provisions`) sont neutralisés.
- **Dépendance :** ces articles doivent être appliqués avec D161-13 (BL3). Sans cela, D161-13 confierait des missions à un comité qui n'existerait plus.
- **Points pour l'auteur :**
  - D161-8 a été modifié par le décret n° 2025-906, ce qui montre que l'administration tenait encore le comité pour existant.
  - L'article 193 de la loi n° 2016-41 n'a pas été relu au JORF.

## CSS D757-14 (objection BASELINE-BL3-D756-3) : appliquée (coordination)

- **Ce qui change :** le renvoi mort à D. 812-4, abrogé en 2007, vise désormais sa dernière rédaction en vigueur, celle à laquelle renvoie le 2° de D. 756-3. Aucun droit ni montant ne change.
- **Notes :** les notes antérieures disaient D812-4 « absent du corpus ». Elles sont corrigées.
- **Point laissé ouvert :** la coordination de L751-1 au 1er janvier 2028.

## Code du travail D5427-10 (objection BASELINE-BL4-D5427-4) : appliquée (coordination)

- **Ce qui change :** « Les fonds disponibles des Assédic sont versés à l'Unédic » devient « Les fonds disponibles de l'organisme gestionnaire du régime d'assurance chômage mentionné à l'article L. 5427-1 sont gérés ». Ces fonds restent gérés selon l'arrêté de L. 5427-10. Aucune obligation nouvelle n'est créée.
- **Article lié :** le contrôle de D5427-6 garde son objet.

Revue IA, sans validation par un juriste.
