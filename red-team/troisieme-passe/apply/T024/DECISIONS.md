# T024 — lecture systématique, palier A (CGI 209 à 212 : détermination du bénéfice imposable à l'IS)

J'ai lu les 15 articles du paquet en production (lecture seule), le 30 octobre 2026. Bilan : 2 G, 3 m et 10 sans défaut. Le détail par article est dans `audit/tier-a/T024.json`. Aucun article du paquet n'a de version future publiée.

## TA-T024-01 : 210 A, reprise de la réserve spéciale de 209 quater — **appliquée** (`apply/T024/`, 210 A LEGIARTI000046196219)

- **Défaut** (F1, F5) : le a du 3 oblige toujours la société absorbante à reprendre « la réserve spéciale où la société absorbée a porté les plus-values à long terme soumises antérieurement au taux réduit ». Or 209 quater, tel que proposé, abroge cette réserve : « Aucune inscription, reprise ou reconstitution de la réserve spéciale des plus-values qu'il prévoit n'est exigée ».
  - Le bilan d'impact de 209 quater le reconnaissait : « 210 A reste à nettoyer expressément ».
  - 208 septies III et 223 D ont fait cette coordination pour leur propre champ. 210 A, qui est le texte général des fusions, ne l'a pas faite.
- **Correction** :
  - au a du 3, la branche « réserve spéciale » est retirée pour les fusions réalisées à compter de l'abrogation de 209 quater. Les sommes encore inscrites suivent le régime de cette abrogation, c'est-à-dire le compte protégé du 1 du XI de 209, sans double inscription ;
  - la reprise des provisions différées et celle de la réserve de fluctuation des cours (sixième alinéa du 5° du 1 de 39) restent inchangées ;
  - au 7, une phrase de transition est ajoutée : les impositions déjà exigibles sur des prélèvements antérieurs ne sont pas remises en cause ;
  - le motif, les notes, `removed_provisions` et `substantive_impact` sont mis à jour. L'effet est de type `coordination` et porte la mesure de 209 quater, pour ne pas la compter deux fois.
- **Ce qui ne change pas** : aucune formalité, condition ou sanction n'est ajoutée. Le texte reprend la formulation de 208 septies III.
- **Contrôle** : `check_changes.py T024`, `problems` vide. Le diagnostic `explicit_normative_reduction` est voulu.

## TA-T024-02 : 211 ter et annexe III 41 A — **demande** à T095

- **Défaut** (F1, F5) : 211 ter, tel que proposé, ouvre pour l'IS la déduction de 39 quinquies « quelle que soit la nature de leur activité ». Pourtant, 41 A, le texte d'application, réserve toujours la déduction aux entreprises industrielles et commerciales, aux professions non commerciales et aux exploitants agricoles au réel. La réforme n'a donc pas d'effet pour les autres redevables de l'IS. Les notes de 211 ter le reconnaissaient : « coordination réglementaire hors lot toujours nécessaire ».
- **Demande à T095** (propriétaire de 41 A), avec le texte complet :
  - un alinéa est inséré après le premier. Pour l'IS et pour les versements effectués à compter de l'abrogation de 211 ter, il ouvre la déduction à toute autre personne passible de l'IS ;
  - les conditions de 41 B restent les mêmes : affectation au logement, perte définitive des fonds, aucun avantage pour les dirigeants. La collecte reste réservée aux organismes habilités ;
  - il n'y a ni option, ni déclaration, ni habilitation nouvelle, et l'impôt sur le revenu n'est pas concerné.
- Cette correction rend effective une réforme déjà décidée (211 ter). Elle n'étend aucune faveur au-delà de ce qu'il prévoit. 211 ter n'est pas modifié.

## Défauts m non corrigés (articles non modifiés)

- **209-0 A** : la dernière phrase du 5 ter de 38 (T004) vise encore le « 1° de l'article 209-0 A ». Ce renvoi est neutralisé par le dernier alinéa de 209-0 A proposé.
- **209 B** : 1763 A est maintenu sans proposition. Il sanctionne la mise en demeure de produire « la déclaration prévue au IV de l'article 209 B », alors que la déclaration du II de l'annexe II 102 Z est devenue facultative. La déclaration obligatoire du I subsiste, donc la sanction garde un objet.
- **210 B** : 39 duodecies, 6 (T004) vise encore « l'engagement de conservation de trois ans prévu au a du 3 de l'article 210 B », supprimé pour l'avenir. La règle garde un objet transitoire pour les engagements anciens.

## Dossiers et articles

- Dossier créé : `apply/T024/`, avec une correction (210 A) et une demande (41 A, T095).
- Aucun dossier de variante : les articles 209 (B07), 209-0 A (B05) et 209 B (A7) n'appellent aucune correction G.

Revue IA, sans validation par un juriste.
