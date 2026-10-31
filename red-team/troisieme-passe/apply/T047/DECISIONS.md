# T047 — lecture systématique, palier A (CGI 732 ter à 763 : meubles, baux, partages, champ et assiette des droits de mutation à titre gratuit)

J'ai lu les 30 articles du paquet en production (lecture seule), le 30 octobre 2026, avec leurs renvois entrants dans le CGI et les annexes I à IV. Aucune version future publiée n'existe pour ces articles, et aucun article d'annexe ne les cite. Bilan : 1 G, 2 m et 27 sans défaut. Le détail est dans `audit/tier-a/T047.json`.

| Objection | Décision | Articles | Changement |
|---|---|---|---|
| TA-T047-01 (suite de RT-DOMSUCC-01) | Appliquée, `loophole_closure`, dans le dossier de variante `apply/B10tbu/` (750 ter appartient à B10) | CGI 750 ter | Le II réserve les droits de donation que 784 C, 792 bis et 792-0 bis maintiennent lorsque l'auteur de la libéralité est vivant au décès d'un tiers. |
| RT-DOMSUCC-01, volet c (assurance-vie) | Non appliquée (arbitrage) | 750 ter II, deuxième alinéa ; 757 B | L'orientation « successions » inclut les capitaux décès ; A7 et A7c ont laissé ce point à l'auteur. |

## Défauts mineurs non corrigés

- **746** : 635 proposé (hors paquet) garde l'enregistrement dans le mois des actes de partage (1, 7°), alors que 746 interdit toute formalité « exclusivement destinée à liquider » le droit supprimé. La frontière entre ces deux textes reste à préciser. Les notes du projet le signalent déjà.
- **757 B** : volet assurance-vie de RT-DOMSUCC-01 (arbitrage, voir ci-dessus).
- **750 ter** : désignation « la présente loi » et gel des procédures « à la date du décès » au III, alors que 758 à 763 visent les « règles temporelles propres ». C'est RT-DOMSUCC-06 (P2), déjà connu ; la même formule de survie figure dans 751 à 754 A.

Aucune demande n'est adressée à d'autres groupes. Contrôle : `python3 -B apply/check_changes.py T047` et `python3 -B apply/check_changes.py B10tbu` renvoient tous deux `problems` vide.

Revue IA : rien de ceci ne vaut validation par un juriste.
