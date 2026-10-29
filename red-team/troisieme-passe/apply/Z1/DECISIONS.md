# Z1 — demandes restées en suspens après le troisième balayage (articles sans groupe)

Textes lus en production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite `mode=ro`), le 29 octobre 2026, après application de Y15, Y17 et Y18. Contrôle : `python3 -B apply/check_changes.py Z1` construit 3 lignes et en valide 3. `problems` est vide. Les diagnostics sont les réductions déclarées.

## Appliquées (3, mode `replace`, articles sans groupe dans `assignment.json`)

- **SWEEP-Y15-A2-242-septies-A**, annexe II 242 septies A (LEGIARTI000049826453). Défaut confirmé (F5). 287 proposé (LEGIARTI000048826856) dit qu'« aucun acompte semestriel du régime simplifié dont l'échéance intervient à compter de l'entrée en vigueur de la présente loi n'est exigé ». Pourtant le 2 de 242 septies A fait encore déterminer les « acomptes ultérieurement exigibles », et sa transition maintient la modulation et la suspension.
  - Ce qui change : un alinéa final écarte, pour ces exercices, les acomptes et toute déclaration de modulation ou de suspension. La taxe est payée avec la déclaration annuelle. Le relevé du 3 peut être déposé sans acompte pour demander le remboursement sur immobilisations. La transition vise désormais « les acomptes restant exigibles ».
  - Conservés : le tableau et la règle de substitution.
  - Écart avec la demande : « la loi qui les supprime » devient « la loi portant la présente réforme », qui est la formule de l'article.
  - Une note devenue fausse est corrigée : le renvoi de 242-0 C III a déjà été corrigé par Y15.
  - Effet `coordination` ajouté sous la mesure `tva-simplifie-suppression-acomptes` de 287.
- **SWEEP-Y17-85B**, annexe III 85 B (LEGIARTI000023099623). Défaut confirmé (F1). La proposition maintenait « Tout changement [...] est soumis à autorisation » et une décision modificative prise « conformément à l'article 85 A ». Or 85 A est abrogé, 85 ne prévoit plus de demande, et 277 A I 2° proposé dit : « ne requiert ni autorisation préalable ni déclaration d'ouverture ».
  - Ce qui change : abrogation complète (`full_repeal`), selon le texte de la demande. Les demandes en cours deviennent sans objet et les décisions modificatives antérieures sont conservées.
  - Restent applicables : les conditions de fond, la mise à jour de l'identification fiscale, l'agrément des locaux pour risque particulier et les autorisations douanières autonomes.
  - Bilan d'impact : `coordination_only`, sous la mesure de 277 A.
- **SWEEP-Y17-41TA**, annexe III 41 tervicies A (LEGIARTI000038950368). Défaut confirmé (F1). Le troisième alinéa exigeait l'indication du représentant fiscal et son engagement. Or le V proposé de 167 bis dit : « La désignation d'un représentant établi en France n'est pas exigée » (son X interdit de la rétablir).
  - Ce qui change : la mention du représentant devient facultative, et il n'y a plus ni désignation ni engagement. La transition renvoie au XI de 167 bis : elle s'applique aux sursis en cours et les mandats sont conservés.
  - Conservés : le délai de dépôt allégé et les garanties.
  - Le motif et les notes sont corrigés : ils disaient encore le représentant obligatoire.
  - Effet `coordination` ajouté sous `exit-tax-representant-obligatoire-suppression`.

## Non traitées ici (déjà satisfaites en production)

- **SWEEP-Y15-A4-50-0-A-bis** (annexe IV 50-0 A bis, LEGIARTI000042147351, groupe Y18). Déjà corrigé par Y18 (SWEEP3-Y18-02). Le I dit désormais : « Aucune demande d'agrément, aucune décision d'admission, aucune attribution préalable d'un numéro d'agrément [...] n'est exigée ». Les numéros d'agrément sont donnés « le cas échéant » pour les agréments antérieurs, et les demandes en cours deviennent sans objet. Aucune ligne Y18b.
- **SWEEP3-Y18-02** (annexe II 289, 68°, LEGIARTI000054363092, groupe Y15). Déjà traité par Y15 (SWEEP-Y15-A2-289). Le 68° est « Abrogé à compter de l'entrée en vigueur de la loi supprimant l'agrément du représentant fiscal [...] ». C'est plus net que le bornage demandé, et la demande disait elle-même « ignorer » ce cas. Aucune ligne Y15b.

## Points laissés à l'auteur

- 85 B : la ligne de lot garde les anciens champs `removed_provisions` et `reform_policy_id`, comme 85 A. Ils sont sans effet sous `full_repeal`.
- 242 septies A : le formulaire 3514 et les textes CIBS d'application restent à coordonner hors corpus.

Revue IA : rien de ceci ne vaut validation par un juriste.
