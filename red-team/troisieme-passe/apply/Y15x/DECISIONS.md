# Y15x — décisions (variante de Y15, demande SWEEP-J15-a4-35)

Texte lu en production (`CITE_PRODUCTION=1 python3 -I tools/cite.py`), en lecture seule. Revue IA, sans validation par un juriste.

## SWEEP-J15-a4-35 — Annexe II, article 254 (LEGIARTI000050811261, LEGITEXT000006069569) : **appliquée**

- **Qualification :** défaut confirmé G (F1+F3). 286 proposé (LEGIARTI000054337091) porte « 2° Abrogé ; », ce qui supprime le questionnaire professionnel sur imprimé sans formalité de remplacement. Son II 1-0 ne vise déjà plus que le 1° du I. L'article 254, maintenu à la source, obligeait encore le franchisé non établi en retard à « fournir tous renseignements relatifs à son activité professionnelle conformément aux 1° et 2° du I de l'article 286 ». C'est une formalité supprimée par la loi qui survit dans le décret.
- **Ce qui change :** le a) devient « a) De déposer une déclaration d'existence conformément au 1° du I de l'article 286 du code général des impôts ; ». Le chapeau, ses deux déclencheurs de retard, le b) et le c) restent ceux de la version officielle. Aucun renseignement de remplacement n'est créé. La transition des demandes fondées sur le seul 2° est déjà réglée par le IV de 286 proposé.
- **Ligne de lot :** l'article passe de `retained_unchanged` à `rewrite_draft`, avec la classification `coordination_only`, `change_type: normative_reduction`, `reform_policy_id: editorial_direction_2026_10_19` et une entrée `removed_provisions`. Le bilan d'impact compte un effet `coordination` (mesure `tva-questionnaire-professionnel-supprime`, déjà comptée à 286, donc aucune seconde réduction), dont les deux citations sont exactes. Le motif est réécrit en coordination. Les notes sont conservées, avec la phrase de troisième passe demandée en plus.
- **Vérifications :** 254 n'a pas d'autre version au corpus. La franchise de 293 B bis et les seuils favorables de trente jours et de deux trimestres sont intacts.
- **Contrôle :** `python3 -B apply/check_changes.py Y15x` → `problems` vide. Diagnostic `explicit_normative_reduction` (voulu).
- **Pour l'auteur :** 286 est en ABROGE_DIFF, maintenu jusqu'à sa reprise réglementaire CIBS (L. 215-26). La même coordination devra suivre lors de cette reprise, qui est hors corpus.
