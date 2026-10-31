# T126 : lecture systématique, palier A (annexe IV, contributions indirectes : comptabilité matières, alambics, consignation, acheteur-revendeur, capsules, exonérations, destinataire enregistré)

23 articles lus en production : 3 G, 2 m, 18 zéro.

## Corrections appliquées dans T126

- **TIERA-T126-50-00B (annexe IV 50-00 B, F1/F5) : appliquée.**
  - 286 H de l'annexe II proposé permet le regroupement des locaux « Sans information préalable particulière du service ». Le II de 50-00 B exigeait pourtant de désigner au service les chais ou locaux du site, et le III faisait dépendre le rattachement de cette désignation.
  - Seule la désignation du siège est conservée : elle a un fondement propre (VI de 286 I et b du 2° du II de 286 J). Les chais ou locaux n'ont plus à être désignés. Le III ne demande plus ni demande ni désignation préalable.
  - Ce qui ne change pas : la justification sur place (286 H), les désignations antérieures (toujours valables) et la transition.
  - Les notes périmées (« après information ») sont corrigées. L'impact est déclaré comme une coordination de la mesure de 286 H, sans double compte.
  - Ce point répond aussi à la note « à clarifier par T126 » du groupe T084.
- **TIERA-T084-285A (annexe IV 50-0 B, F1/F5) : appliquée, sur demande de T084.**
  - 285 A proposé rend le formulaire facultatif. Le I de 50-0 B admet désormais le papier libre.
  - Les mentions a à g sont inchangées, sauf le f : la décision d'octroi ne figure sur le formulaire que lorsque celui-ci est utilisé.
  - Aucune mention nouvelle n'est exigée. La transition existante couvre les demandes en cours.

## Variante M07tev

- **TIERA-T084-286M (annexe IV 50-00 G, F1/F5) : appliquée dans `apply/M07tev/`.** Cette demande de T084 était adressée à M07 ; l'article est dans le paquet T126.
  - Le 4° du II est aligné sur 286 M proposé : remboursement sur demande dès le replacement en suspension, sans attente de trois mois. Règle anti-cumul conservée.
  - Défauts m corrigés au passage :
    - les visas de l'article 302 D, abrogé le 29 mars 2024, sont retirés ;
    - le renvoi de catégorie à l'article 438 vise sa rédaction au 31 décembre 2021, comme dans 286 J.
  - Le motif, le `benefit_review` et le bilan d'impact (effet de coordination) sont mis à jour.

## Défauts m non corrigés (articles non modifiés)

- **50-00 C** : renvois de source morts (302 M ter, 403) et en abrogation différée (338). Réserve de concordance avec le CIBS, déjà qualifiée m par M07.
- **50-0 F** : la réserve écartant « le délai d'apurement de douze mois suivant le visa prévu à l'article 54-0 AB » est sans objet. 54-0 AB proposé ne prévoit plus ni visa ni délai.

## Points pour l'auteur

- **Annexe II 289, 8°** : compétence pour l'autorisation des alambics, « prévue par l'article 306 du code général des impôts et l'article 50 C de l'annexe IV ». Le 306 a été abrogé le 1er juillet 2025 ; les 50 A à 50 E sont abrogés par le projet. La clause finale de 289 neutralise le renvoi. La variante B09tdg (T085) l'a laissé à l'auteur, faute de pouvoir vérifier une reprise dans le CIBS (hors corpus). Aucune demande nouvelle.
- **Le 26° de 289** (rattachement hors limites de 50-00 B) est déjà abrogé pour l'avenir dans B09tdg. Il est cohérent avec la correction de 50-00 B.
- **Renvois anciens du chapitre** (302 D, 302 M, 302 M ter, 302 P, 338, 403, 1698 C) : leur concordance avec le CIBS reste hors corpus.

## Contrôle

`python3 -B apply/check_changes.py T126` et `python3 -B apply/check_changes.py M07tev` donnent `problems: []`.

Revue IA : ce n'est pas une validation par un juriste.
