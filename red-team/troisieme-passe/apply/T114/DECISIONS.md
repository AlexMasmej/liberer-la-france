# T114 — décisions (lecture systématique, palier A, annexe III du CGI 328 G bis à 344 undecies)

Lecture en production (lecture seule), 30 articles. Décompte : 1 G, 4 m, 25 « 0 ».

## TA-T114-328Q — annexe III 328 Q (LEGIARTI000046538972) : appliquée

- **Défaut (G, F3/F4, conflit de source non coordonné)** : 328 Q applique le 2° du I de 1635 quater D, qui exonère de taxe d'aménagement les logements « dès lors qu'elles sont financées dans des conditions définies par décret ». La version de 1635 quater D en vigueur au 1er janvier 2027 (LEGIARTI000054567181, ordonnance n° 2025-1247 modifiée par l'ordonnance n° 2026-671) renvoie désormais aux articles L. 231-62 et suivants du CIBS et ne parle plus de décret. Faute de coordination, 328 Q imposerait à partir de 2027 une condition de financement que la loi ne prévoit plus.
- **Correction** (mode `replace`) : le corps actuel est repris sans changement. Un dernier alinéa limite 328 Q aux constructions qui relèvent de la rédaction antérieure du 2°. Pour la rédaction de 2027, l'exonération suit les seules conditions légales. Les droits acquis, les impositions établies et les recours sont conservés. Le motif, les notes et `substantive_impact.assessment` sont complétés.
- **Alignement** : il s'agit d'une coordination avec le droit publié. La correction ne crée aucune formalité ni condition et ne retire aucun avantage.
- **Points laissés à l'auteur** : les articles L. 231-62 et suivants du CIBS sont hors corpus. Deux cas restent possibles :
  - si ces articles reprennent la condition de financement (PLAI), la correction est neutre ;
  - sinon, l'élargissement de l'exonération découle de l'ordonnance, pas du projet.

  Pour garder le ciblage par le financement, il faudrait une proposition sur la version 2027 de 1635 quater D. Ce serait un choix politique, qui n'est pas fait ici.
- **Voisins à vérifier** : les articles 318 E à I de l'annexe II et 344 N de l'annexe III citent d'autres numéros (1°, 5°, 6°, 7°) ou l'article entier de 1635 quater D. Ils ne sont pas touchés par cette rédaction du 2°.
- Contrôle : `python3 -B apply/check_changes.py T114` donne `problems` vide. Un seul diagnostic, `length_change` (4,37), est voulu.

## Défauts m non corrigés (notes seulement, F10, articles non modifiés)

- **328 N** : les notes disent que 1649 A ter « conserve actuellement « déclare chaque année » ». Or la proposition de 1649 A ter supprime déjà cette déclaration et l'amende du V de 1736 pour les années supprimées.
- **328 P** : les notes disent « leurs projets ne comportent pas encore cette extinction ». Or la proposition de 1649 A quater l'organise (objection close RT-P1-CGI-C-02).
- **336 bis, 336 ter** : les notes disent que le successeur de 1622 n'est « pas fourni ». Or la version 2027 (LEGIARTI000053188857) est au corpus avec sa proposition, et 344-0 B 11° est coordonné.

## Requests

Aucune. Aucun dossier de variante n'est créé : les articles dont `previous_owner` vaut B03, J14, J15, Y16 ou Y17 sont tous qualifiés « 0 » ou « m ».

Revue IA : ce n'est pas une validation par un juriste.
