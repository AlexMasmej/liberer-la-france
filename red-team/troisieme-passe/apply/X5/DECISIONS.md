# X5 — décisions (demande SWEEP-J06-S12-R313-3)

Texte lu en production (`CITE_PRODUCTION=1 python3 -I tools/cite.py`), en lecture seule. Revue IA, sans validation par un juriste.

## SWEEP-J06-S12-R313-3 — CGI 235 bis (LEGIARTI000038586341, LEGITEXT000006069577) : **appliquée**

- **Qualification :** défaut confirmé G, famille F4 (S12). La proposition bornait les renvois à L. 313-4 et L. 313-6 du CCH à leur « champ temporel légal ». Elle ajoutait : « Le renvoi à ces deux derniers articles ne proroge ni ne rétablit leur application après leur abrogation. » Or ces deux articles sont maintenus au 1er janvier 2027 par LEGIARTI000053151481 (L. 313-4) et LEGIARTI000053151478 (L. 313-6), en VIGUEUR_DIFF, issus de l'article 49 de l'ordonnance n° 2025-1247 modifiée par l'ordonnance n° 2026-671. Ces versions reprennent la cotisation de 2 p. 100, le bordereau et les vérifications. Elles ne changent que les renvois au régime de recouvrement et de secret. Le motif s'appuyait sur une clause de L. 313-4 que RT-FUTTL-02 a déjà retirée.
- **Article sans propriétaire** dans `assignment.json` : traité dans ce dossier.
- **Ce qui change :** l'article revient à la version officielle (`retained_unchanged`, `proposed_xml` nul, classification `retained_necessary`, bilan d'impact sans effet). Son 1 retrouve le renvoi « L. 313-1, et L. 313-4 à L. 313-6 » ; le 2 agricole est inchangé.
- **Motif et notes :** le motif est réécrit (maintien de la source). Dans les notes, j'ai corrigé les affirmations devenues fausses (successeurs « non fournis », « coordination hors lot » pour L313-6, « suivre ces bornes » pour l'annexe II 162) et ajouté la phrase de troisième passe demandée. Le reste des notes, notamment 1655 septies et le régime rural hors corpus, est conservé.
- **Vérifications :** 235 bis n'a pas d'autre version future au corpus. L. 313-1 et L. 313-5 sont en vigueur et ont une proposition qui conserve la participation. Aucune cotisation, aucun taux et aucune formalité ne sont créés ni supprimés.
- **Contrôle :** `python3 -B apply/check_changes.py X5` → `problems` vide, aucun diagnostic.
- **Pour l'auteur :** cohérent avec la correction de R313-3 par J06 (même objection). Les deux doivent être appliquées ensemble.
