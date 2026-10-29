# Y13 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-Y13.json`, soit 45 articles du code de l'urbanisme et 48 pistes (41 S9, 7 S10). Pour chaque piste S9, la ligne `removed_provisions` de la loi visée a été lue dans son lot de production. Contrôle : `python3 -B apply/check_changes.py Y13` construit 1 ligne et en valide 1, avec `problems` vide. Les diagnostics sont voulus : la réduction est déclarée en `full_repeal`, et le rapport de longueur (4,66) s'explique par une source très courte, deux phrases, face à un corps qui doit porter l'abrogation et sa transition.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9 | S10 | Total |
|---|---|---|---|
| G | 2 | 0 | 2 (1 corrigé, 1 laissé à l'arbitrage) |
| m | 0 | 0 | 0 |
| déjà réglé | 20 | 0 | 20 |
| faux positif | 19 | 7 | 26 |

Corrections : 1 ligne en mode `replace` (R121-33). Aucune demande à un autre groupe. Un défaut est écarté (`skipped`) comme relevant d'un arbitrage : R113-12.

## Défaut confirmé et corrigé

- **R121-33** (LEGIARTI000031720948), piste S9 vers L121-39. Qualification G (F1), corrigé.
  - **Défaut.** L121-39 proposé (LEGIARTI000031210528) rend la dérogation éolienne directe : les ouvrages « peuvent être implantés en dehors des espaces proches du rivage, sans autorisation particulière ni avis préalable au titre de cette dérogation ». Ses `removed_provisions` portent « Autorisation spéciale de l'État et avis préalable de la commission ». Pourtant, R121-33 proposé disposait encore : « Le préfet de région accorde l'autorisation prévue à l'article L. 121-39 après avis de la commission départementale de la nature, des paysages et des sites ». Le décret organisait donc une autorisation et un avis que la loi supprime. La note de L121-39 signalait déjà « R. 121-33 reste à coordonner hors lot ».
  - **Correction.** L'article est abrogé à la date de la loi, en reprenant la transition de L121-39. Les demandes en cours ne sont plus instruites sur ce seul fondement, sans nouveau dépôt. Les autorisations antérieures, leurs prescriptions et les recours sont conservés. Les refus définitifs ne sont pas rouverts. Aucune pièce ni consultation de remplacement n'est créée. Jusqu'à la loi, la suppression des trois avis ministériels décidée par le brouillon est conservée mot pour mot, avec le silence favorable de la commission au bout de deux mois. Les interdictions de fond de L121-39 et les procédures autonomes demeurent.
  - **Ligne de lot.** `change_type: full_repeal`, avec `repeal_scope` et `benefit_review` mis à jour. `substantive_impact` est en `material_reduction`. Il garde l'effet `obligation_removed` des avis ministériels et ajoute une `coordination` sous la `measure_id` de L121-39 (`littoral-eolien-outre-mer-derogation-directe`), pour ne pas compter la mesure deux fois.
  - **Note corrigée.** La note affirmait que « l'avis de la commission, exigé par la loi, est conservé ». C'est faux depuis L121-39 proposé, et la note est corrigée.
  - **Renvois.** Aucun autre article en vigueur du corpus ne renvoie à R121-33 ou à l'autorisation de L121-39. Les recherches « L. 121-39 » et « R. 121-33 » sur les sources et les propositions ne renvoient que R121-33 lui-même.

## Défaut confirmé non corrigé (arbitrage)

- **R113-12** (LEGIARTI000031721101), piste S9 vers L113-4. La piste elle-même est déjà réglée : aucune autorisation supprimée n'est rétablie. Elle révèle en revanche une contradiction entre propositions, G (F5).
  - **R113-12 proposé** supprime le délai de deux ans du transfert de propriété (« Le transfert de propriété n'est soumis à aucun délai de caducité »). Il le fait « à compter de l'entrée en vigueur de la disposition législative supprimant le délai de transfert prévu à l'article L. 113-4 ».
  - **L113-4 proposé** (LEGIARTI000031210305, groupe A9) maintient au contraire ce délai au niveau législatif : « qui intervient au plus tard dans les deux ans suivant la publication de l'arrêté ». Son motif le justifie : il « évite de laisser indéfiniment disponible une autorisation compensatoire non exécutée ».
  - **Effet aujourd'hui.** La loi proposée régit le délai, et la clause réglementaire reste suspendue à une loi que le projet ne contient pas. Le texte est incohérent, sans effet immédiat.
  - **Pourquoi rien n'est appliqué.** Choisir entre supprimer le délai ou le maintenir est une décision de fond que les orientations ne tranchent pas : coupe d'une contrainte, ou garde-fou de la compensation boisée. La troisième passe l'avait déjà signalé comme point non examiné (`apply/A9/DECISIONS.md`, `reports/dossiers/P1-NEW.md`).
  - **Option a, supprimer le délai** (demande au groupe A9). Dans le cinquième alinéa de L113-4, retirer « , qui intervient au plus tard dans les deux ans suivant la publication de l'arrêté ». Remplacer la dernière phrase par : « Le transfert de propriété n'est soumis à aucun délai de caducité ; cette règle s'applique aux autorisations dont le délai de transfert n'est pas expiré à l'entrée en vigueur de la loi et ne fait pas revivre une autorisation devenue caduque. » R113-12 reste alors tel quel.
  - **Option b, maintenir le délai** (Y13). Ramener R113-12 à : « L'autorisation ne produit ses effets qu'après le transfert de propriété, qui intervient dans le délai prévu à l'article L. 113-4. Le plan local d'urbanisme est alors mis à jour conformément à l'article R. 153-18. » Supprimer aussi la réduction conditionnelle de sa ligne de lot.

## Pistes S9 : faux positifs (19)

- **L410-1 (13 pistes).** La loi ne retire que la cristallisation fiscale opposable aux allègements ultérieurs. Le certificat lui-même demeure.
  - A410-3, A410-5, R*410-1, R*410-2, R*410-6, R*410-7, R*410-10 (piste L111-11), R*410-13 et R*410-17-1 règlent le contenu, l'instruction, les exemplaires ou la prorogation du certificat.
  - R*410-12 et R*410-18 renvoient au « quatrième alinéa de l'article L. 410-1 ». C'est toujours l'alinéa de la garantie de dix-huit mois, et le renvoi est exact.
  - R*322-26, R*322-27 et R*322-28-1 disent déjà que le certificat n'est pas une condition de recevabilité.
- **R213-24 (L213-1).** La « déclaration » visée est la déclaration d'achèvement, et non la déclaration préalable de la location-accession. Le c de L213-1 n'a pas bougé.
- **D213-13-4 (L213-2).** La DIA ordinaire et la visite sont conservées par la loi.
- **R*423-36 (L425-8).** L'autorisation cinématographique reste préalable au permis. Seule la suspension pendant les recours est retirée.
- **R472-14 (L462-1).** La demande de mise en exploitation tient lieu de déclaration d'achèvement. Elle n'ajoute aucune formalité.
- **R153-10 (L123-2).** Le renvoi vise L123-2 du code de l'environnement, homonyme d'un autre code.

## Pistes S9 : déjà réglé (20)

- **L424-7** : A424-14, R*424-11, R*424-12 et R452-1. La prise d'effet a lieu à la notification, et la transmission ne la retarde plus.
- **L425-6** : R*423-45. Plus de prolongation pour attendre l'autorisation de défrichement.
- **L462-1** : A462-1. La déclaration volontaire n'est assortie d'aucune obligation de remplacement.
- **L473-3** : R472-19. Commission et majoration supprimées.
- **L442-3** : R*442-9, R*442-21 et R*442-2. Dispense de déclaration, sans formalité de remplacement.
- **L163-7** : R163-5. Plus d'approbation préfectorale.
- **L151-11** : R151-35. Plus d'identification graphique préalable.
- **L132-12 et L132-13** : R132-7 (deux pistes). La procédure d'agrément ne s'applique pas aux consultations dispensées.
- **L121-24** : R121-6. Plus de délai minimal distinct ni de seconde mise à disposition.
- **L113-24** : R113-29. Plus d'accord préalable du département.
- **L113-4** : R113-8, R113-9, R113-10 et R113-13. Arrêté préfectoral, sans décret ni accord communal.

## Pistes S10 : faux positifs (7)

- A424-11 et R*442-13 (vers R*442-17) : la défaillance du lotisseur est toujours définie par R*442-17 proposé.
- L322-3 (vers L322-2) : les objets 1°, 2°, 3°, 5° et 6° existent toujours. Le 4° est abrogé dès la source.
- R*421-26 (vers L421-3 et R*421-27) : même date d'effet que la suppression du permis de démolir communal.
- R*322-17 (vers L322-6-1) : même date que l'abrogation de L322-6-1. R*322-8, du groupe W13, est déjà coordonné.
- R132-7 (vers L132-13) : la dispense d'agrément figure toujours dans L132-12 et L132-13.

## Points laissés à l'auteur

- **R113-12 et L113-4** : choisir entre l'option a, qui supprime le délai de deux ans, et l'option b, qui le maintient. Les deux sont rédigées ci-dessus.
- **R121-33** : l'abrogation suppose que le décret et la loi modifiant L121-39 entrent en vigueur ensemble ou dans cet ordre. La période intermédiaire, sans avis ministériels, est conservée telle que la seconde passe l'avait décidée.
