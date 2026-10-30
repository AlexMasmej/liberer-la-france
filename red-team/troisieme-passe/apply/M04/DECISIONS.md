# M04 : décisions (cinquième balayage)

J'ai lu le texte en production avec `CITE_PRODUCTION=1 python3 -I tools/cite.py`, et la base en `mode=ro`, sans rien écrire. Revue IA, sans validation par un juriste.

Les cinq articles du paquet ont un `previous_owner` (W13 pour trois d'entre eux, Y14 pour deux). Aucune correction ne porte donc sur M04 lui-même : `apply/M04/changes.json` est vide. Les corrections et les qualifications figurent dans les variantes `apply/W13md/` et `apply/Y14md/`.

| Piste | Article (code de l'urbanisme) | Qualification | Correction |
|---|---|---|---|
| S17 (S7/F3) vers L143-46 | L143-44, LEGIARTI000031211123 (W13) | **G** (F3, renvoi décalé) | Oui, dans W13md (SWEEP-M04-L143-44) |
| S17 (S8/F3) vers R141-3 | R173-1, LEGIARTI000031720345 (W13) | m (défaut de la source) | Non : arbitrage laissé à l'auteur |
| S16/F3 vers L332-1 | R462-7, LEGIARTI000043840954 (W13) | faux positif | Non |
| S16/F3 vers L124-1 | R421-23-2, LEGIARTI000049357558 (Y14) | faux positif | Non |
| S17 (S10/F5) vers L153-6 | L153-2, LEGIARTI000052866271 (Y14) | m (redondance) | Non : règle des défauts m |

## Détail

- **L143-44, appliquée (W13md).** La proposition dispose : « Aucun procès-verbal de cet examen n'est à établir [...], par dérogation au dernier alinéa de l'article L. 143-46 ». Or le dernier alinéa de L143-46 proposé (LEGIARTI000031211127) est désormais sa clause de transition, qui conserve « Les procès-verbaux déjà régulièrement versés au dossier d'enquête ». C'est l'avant-dernier alinéa qui écarte déjà le procès-verbal. Le renvoi vise donc le mauvais alinéa. W13 l'avait jugé m. Avec le critère de l'audit, je le requalifie G : un juriste le remarquerait, et la phrase peut se lire comme une dérogation à la conservation des pièces déjà versées.
  - **Ce que j'ai changé :** j'ai retiré le seul membre « par dérogation au dernier alinéa de l'article L. 143-46 ». Le reste du corps est inchangé, tout comme le motif, les `removed_provisions` et le bilan d'impact, dont les citations restent exactes. Dans les notes, j'ai rectifié la phrase sur cette dérogation (L143-46 est déjà coordonné) et ajouté la phrase de troisième passe.
  - **Effet :** aucun changement de fond. Il n'y a ni formalité de remplacement, ni changement de la transition.
- **R173-1, non corrigée.** La plage « R. 141-3 à R. 141-11 » est en partie morte dans la source officielle : R141-3 à R141-5 sont abrogés depuis le 1er avril 2021, et R141-6 à R141-11 ont changé d'objet. Le défaut reste m pour trois raisons :
  - la formule « tout ou partie » n'impose rien ;
  - elle ne vise que les schémas de secteur hérités d'avant 2014 (L173-1) ;
  - elle n'a aucun effet opératoire.
  Choisir les éléments actuels du SCoT à viser relève de l'auteur.
- **R462-7 : faux positif.** « L. 332-1 du même code » désigne le code de l'environnement.
- **R421-23-2 : faux positif.** « L. 124-1 et L. 313-1 du même code » désigne le code forestier.
- **L153-2, non corrigée (m).** La dérogation « au troisième alinéa du I de l'article L. 153-6 » vise un alinéa existant, dont l'objet est le bon. Cet alinéa renvoie lui-même à L153-2. La dérogation est redondante, mais concordante, sans effet.

## Contrôle

J'ai lancé `python3 -B apply/check_changes.py` sur les trois dossiers. `problems` est vide pour M04, W13md et Y14md.

Pour W13md, les diagnostics sont `explicit_normative_reduction`, `length_change` et `references_changed`. Ils sont tous antérieurs à la correction et mesurés par rapport à la source.
