# Y08 : troisième balayage (S9, S10), Code du travail, décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-Y08.json`, soit 53 articles et 65 pistes (53 S9, 12 S10). Preuves : `evidence/cited/production-20261029/`.

Contrôle : `python3 -B apply/check_changes.py Y08` donne 3 lignes construites, 3 validées et `problems` vide. Les diagnostics sont voulus : réductions déclarées, renvois ajoutés à L6323-17-2 et D6323-9-2 (et, pour R6323-10, les renvois R6323-10-1/2 déjà présents dans le brouillon).

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 1, corrigée (3 articles) |
| déjà réglé | 29 |
| faux positif | 35 |

Comme prévu, les pistes mécaniques S9 sont surtout des faux positifs : « dépôt » qui désigne la Caisse des dépôts, une formalité qui reste légale (DPAE, DOETH, attestation de suivi, agrément de base des SPST), une réduction de la loi sans rapport avec ce que dit le décret. Restent les décrets déjà coordonnés par la seconde passe ou par les balayages précédents. Les dérogations S10 visent presque toutes une règle encore présente.

## Défaut confirmé et corrigé

**SWEEP3-Y08-01** : piste S10/F5 de R6323-14 vers R6323-10, avec un défaut F1 à la racine. Qualification G, corrigé.

- **Le défaut.** L6323-17-2 proposé (LEGIARTI000047452262, reporté sur les versions de 2027 et 2028) supprime l'ancienneté générale d'accès au projet de transition professionnelle : « n'est subordonné à aucune ancienneté minimale en qualité de salarié ». Il interdit aussi aux règlements de « subordonner le congé ou la prise en charge à une ancienneté générale minimale ». R6323-14 proposé l'applique, mais les règlements qui suivent la contredisaient encore :
  - R6323-10 IV laissait l'employeur refuser le congé pour « non-respect ... des conditions d'ancienneté prévues au paragraphe 1 » ;
  - D6323-9 commençait encore par « Pour bénéficier d'un projet de transition professionnelle, le salarié justifie de l'ancienneté suivante : 1° Au moins vingt-quatre mois » ;
  - R6323-9-1 avait le même chapeau pour les intermittents et les intérimaires.
- **R6323-10** (LEGIARTI000041393503, `replace`).
  - Le IV ne permet plus de refuser le congé pour un défaut d'ancienneté générale.
  - Il garde le motif de refus que permettait déjà le paragraphe 1, réduit à la condition spéciale d'activité exposée. Ce motif ne vaut que pour un projet présenté au fonds d'usure : L6323-17-2 maintient cette condition.
  - La transition est celle de R6323-14 : demandes présentées ou en cours d'examen, sans nouveau dépôt. Les décisions définitives ne sont pas rouvertes.
- **D6323-9** (LEGIARTI000045369571, `replace`).
  - Le chapeau du I ne fait plus de l'ancienneté une condition d'accès. Les vingt-quatre mois et leurs dispenses (maladie, accident) restent la durée de référence des dispositions qui y renvoient, au premier rang la durée d'activité dans un métier exposé (D6323-9-2 1°).
  - La transition est ajoutée. Le motif et la note sont corrigés : la note disait l'ancienneté « habilitée », ce que la proposition de L6323-17-2 ne permet plus.
  - Dans `substantive_impact`, seul `scope_limitations` est mis à jour : il affirmait que « le minimum général » demeurait.
- **R6323-9-1** (LEGIARTI000040340619, `replace`). Les chapeaux des I et II deviennent « Pour l'application des dispositions qui renvoient au présent article ». Un alinéa de coordination et la transition sont ajoutés. Les seuils de métier et les 1 600 heures de branche sont conservés.
- **Ce qui est préservé.**
  - Les dispenses, la condition spéciale du fonds d'usure et sa dispense handicap.
  - Les régimes particuliers qui se réfèrent à ces seuils, laissés intacts : R6323-11-2, R6323-18-2-1, R6323-18-3-1 et D6323-18-3 II. Pour D6323-18-3 II, la dispense légale vaut pour tous les salariés.
  - Les décisions favorables et les recours.
  - Aucune formalité ni condition nouvelle. La suppression de l'ancienneté est celle de L6323-17-2 : elle n'est pas comptée une seconde fois.
- **Points pour l'auteur.**
  1. **Articles hors paquet.** Les trois articles sont hors paquet, mais aucun groupe n'en est propriétaire (`assignment.json`), ce que le contrôleur accepte. Le coordinateur doit vérifier qu'aucun autre groupe ne les modifie en parallèle.
  2. **Motif de refus maintenu.** Faut-il garder le refus patronal fondé sur l'activité exposée, que la commission contrôle déjà (R6323-14) ? Je l'ai gardé par prudence, car ce motif était déjà ouvert par la source.
  3. **Intermittents après leur dernier contrat.** R6323-11-2 réserve la demande déposée après la fin du dernier contrat aux intermittents qui remplissent une condition d'ancienneté. Je n'y ai pas touché : supprimer cette condition étendrait une faveur que le projet n'a pas décidée.
  4. **Notes périmées (m).** Les notes de R6323-14, D6323-20-4 et D6323-9-2 disent encore « coordinations hors lot restent ouvertes ». Celles de L6323-17-2 disent la version suivante « non présente dans le corpus », alors qu'elle y figure avec une proposition. Ces quatre articles ne sont pas modifiés ici.
  5. **Renvoi sans objet (m).** R6323-11-1 proposé déroge encore « à la condition d'accord préalable prévue à l'article R. 6323-11 », alors que R6323-11 proposé ne contient plus cette condition. Le renvoi est sans effet ; l'article n'est pas modifié.

## Pistes une à une

| Article (piste) | Cible | Qualification | Correction |
|---|---|---|---|
| D3345-1 (S9) | L3312-5 | déjà réglé : documents de négociation sans PV distinct | non |
| D3345-1 (S9) | L3323-4 | déjà réglé : dépôt de participation facultatif réservé | non |
| R5122-10 (S9) | L5122-1 | déjà réglé : engagements limités aux autorisations antérieures (m F10 : la note dit R5122-9 non coordonné, alors qu'il l'est) | non |
| R3333-6 (S9) | L3332-27 | déjà réglé : dépôt volontaire | non |
| R3332-4 (S9) | L3332-9 | déjà réglé | non |
| R3332-4 (S9) | L3332-27 | déjà réglé | non |
| R3332-4 (S9) | L3332-6-1 | déjà réglé | non |
| R3332-4 (S9) | L3333-7-1 | déjà réglé (m : garantie dès la signature pour le PEE, dès le dépôt volontaire pour le PEI, déjà signalé) | non |
| D5212-8 (S9) | L5212-1 | faux positif : employeurs assujettis seulement | non |
| D5212-8 (S9) | L5212-8 | déjà réglé : « accord » sans « agréé » | non |
| R6241-28-1 (S9) | L6131-4 | faux positif : Caisse des dépôts ; approbation de la convention de reversement non visée | non |
| R6241-28-2 (S9) | L6131-4 | faux positif | non |
| R6241-28-3 (S9) | L6131-4 | faux positif : autre convention | non |
| R6241-21 (S9) | L6241-5 | faux positif : listes régionales, et non la liste nationale du 13° | non |
| D7231-1 (S9) | L7233-2 | faux positif : déclaration « à titre facultatif » | non |
| D6241-25-1 (S9) | L6131-4 | faux positif | non |
| D6323-20-4 (S9) | L6323-17-2 | déjà réglé : pas d'autorisation de réalisation distincte | non |
| R1221-37 (S10) | R1221-36 | faux positif : délais de R1221-35, deuxième alinéa, toujours présents | non |
| R1221-41 (S9) | L1221-5-1 | déjà réglé : plus de mise en demeure | non |
| L5311-10 (S10) | L6123-3 | faux positif : réserve du cinquième alinéa maintenue | non |
| L5422-16 (S10) | L5424-20 | faux positif : périodes antérieures seulement | non |
| R6411-1 (S9) | L6111-3 | faux positif : centres VAE maintenus | non |
| R1251-3-1 (S9) | L1251-33-1 | déjà réglé : plus de signalement à France Travail | non |
| R6223-10 (S9) | L6131-1 | déjà réglé : CSA pour les années anciennes | non |
| R4623-44 (S9) | L4624-1 | faux positif : seul le modèle d'attestation devient facultatif | non |
| R6323-14 (S9) | L6323-17-2 | déjà réglé | non |
| **R6323-14 (S10)** | **R6323-10** | **G (F5+F1)** : ancienneté générale encore exigée par R6323-10 IV, D6323-9 et R6323-9-1 | **oui (3 articles)** |
| R6323-14 (S10) | R6323-11 | faux positif : dépôt avant l'accord de congé prévu | non |
| R8294-2 (S9) | L8291-1 | déjà réglé (m F10 : notes périmées sur R8294-7 et R8295-x) | non |
| R5311-9 (S9) | L5311-9 | déjà réglé : publication sans approbation | non |
| R6123-3-2 (S10) | L6121-4 | faux positif : exception L6122-2 alignée | non |
| R5132-11 (S10) | R5311-26 | faux positif : 2° réservé | non |
| R7122-16 (S9) | L1221-10 | faux positif : DPAE maintenue | non |
| R5422-5 (S9) | L1221-10 | faux positif | non |
| R2312-9 (S9) | L5212-5 | faux positif : déclaration maintenue | non |
| R2312-9 (S9) | L3121-48 | faux positif : simple définition | non |
| R2312-8 (S9) | L5212-5 | faux positif | non |
| R2312-8 (S9) | L2312-26 | faux positif : aucun visa ; retraits non rétablis | non |
| L1252-15 (S10) | L1237-1 | faux positif : dispense de préavis cohérente | non |
| R6523-23 (S9) | L6123-3 | faux positif : autre avis | non |
| R6523-19 (S9) | L6123-3 | faux positif | non |
| R3332-21-6 (S9) | L3332-17-1 | déjà réglé : plein droit, sans rapport | non |
| R4451-86 (S9) | L4622-6-1 | faux positif : agrément de base maintenu | non |
| R5312-42 (S9) | L1251-33-1 | déjà réglé | non |
| D6235-9 (S10) | D6224-1 | faux positif : règle dérogée toujours présente | non |
| R4745-3 (S9) | L4624-1 | déjà réglé : non-utilisation du modèle non sanctionnée | non |
| R5412-2 (S10) | L5412-1 | faux positif | non |
| R6351-17 (S9) | L6352-11 | déjà réglé | non |
| R6351-16 (S9) | L6352-11 | déjà réglé | non |
| R6351-14 (S9) | L6351-2 | déjà réglé : la déclaration d'activité demeure | non |
| R6351-14 (S9) | L6352-11 | déjà réglé | non |
| D4644-6 (S9) | L4644-1 | déjà réglé : plus de dossier d'enregistrement | non |
| R5221-22 (S9) | L5221-5 | faux positif | non |
| R6333-3 (S9) | L6323-4 | faux positif | non |
| R6333-3 (S10) | L6323-4 | faux positif (m : critère « inscription » dans L6323-4, « souscription ou inscription » dans L6323-7, sans effet pratique) | non |
| D6123-37 (S9) | L6131-1 | déjà réglé | non |
| D6123-37 (S9) | L6242-1 | déjà réglé | non |
| L1234-8 (S10) | L3142-88 | faux positif : deux mandats, renvoi exact | non |
| R6324-2 (S9) | L6324-9 | déjà réglé | non |
| R5212-19-1 (S9) | L5212-8 | déjà réglé : report sans autorisation | non |
| R5212-19 (S9) | L5212-8 | déjà réglé | non |
| D6323-8 (S9) | L6323-4 | faux positif | non |
| D6123-2-3 (S9) | L6111-3 | faux positif : autre rapport ; bilan national déjà abrogé | non |
| R5411-6 (S9) | L5411-2 | faux positif : signalement des changements maintenu | non |
| R4624-45-4 (S9) | L4624-1 | faux positif | non |

Contrôles complémentaires hors paquet, lus parce qu'une note les disait non coordonnés : R5122-9, R8294-7, R8295-1, R8295-2, R8295-3, R8295-3-1, R6352-22, R6352-23, R6351-9, D4644-7, D4644-8, D4644-9, R4623-39, R4644-2 et R5411-7. Tous sont désormais coordonnés ; seules leurs notes de renvoi sont périmées.

Toutes les pistes du paquet ont été traitées.
