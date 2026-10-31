# B10tap — variante de la lecture systématique T016 (CGI 170, article du groupe B10)

Lecture faite sur la production, en lecture seule, le 30 octobre 2026. Revue IA : elle ne vaut pas validation par un juriste.

## TA-T016-02 — CGI 170, 1, troisième alinéa : mention annuelle des reports maintenus (appliquée)

- **Décision :** appliquée. La correction rend effective une réforme que le projet a déjà décidée.
- **Article touché :** CGI 170, LEGIARTI000053543803 (propriétaire B10, mode `replace`).
- **Défaut (G, F1 + F2) :** le troisième alinéa du 1 exige « Dans tous les cas » que la déclaration mentionne « le montant des plus-values en report d'imposition en application de l'article 150-0 B ter » et « le montant des fractions de gain net en report d'imposition en application du C du IV de l'article 163 bis H ». Le manquement est puni par l'amende de 5 % de l'article 1760 (LEGIARTI000006314337), qui vise cet alinéa.
  - Le IV proposé de 150-0 B ter (LEGIARTI000053542872) dispose : « Aucune mention annuelle, confirmation ou état réitérant des informations inchangées n'est exigé en l'absence d'un tel événement ».
  - Le 3 du C du IV proposé de 163 bis H (LEGIARTI000053543789) dispose : « Le maintien du report sans modification du montant déjà déclaré ne donne lieu à aucune mention annuelle répétée dans la déclaration prévue à l'article 170 ».
  - La formalité supprimée survivait donc dans 170, avec sa sanction. Les notes de 167 bis relevaient déjà cette coordination, sans qu'elle soit faite.
- **Ce qui change :** une phrase est ajoutée à la fin du même alinéa. Elle écarte la mention pour les années où ces deux dispenses s'appliquent, avec leurs transitions (VII de 150-0 B ter, V de 163 bis H). L'alinéa reste le troisième du 1 : le renvoi de 1760 n'est pas décalé.
- **Ce qui ne change pas :** les mentions des reports non maintenus, de 150 U et du revenu fiscal de référence, la déclaration des opérations, des modifications et des fins de report, ainsi que le reste de l'article.
- **Ligne du lot :** le motif et les notes sont complétés. Deux effets `coordination` sont ajoutés à `substantive_impact`, sous les `measure_id` des réductions de 150-0 B ter et de 163 bis H. Ils ne sont pas comptés une seconde fois. La classification `coordination_only` est inchangée.
- **Aucune** formalité, condition ni sanction nouvelle.
- **Point laissé à l'auteur :** aucun.

Validation : `python3 -B apply/check_changes.py B10tap` donne `problems` vide et aucun diagnostic.
