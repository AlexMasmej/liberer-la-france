# J12 : quatrième balayage (S9a, S9x), annexe III du CGI, décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro`. Les exports sont dans `evidence/cited/production-20261029/`.

Le paquet `audit/sweeps/packet-J12.json` compte 53 articles de l'annexe III et 53 pistes : 48 S9a et 5 S9x. Aucun article n'a de `previous_owner` : je n'ai donc créé aucun dossier de variante.

**Méthode.** Pour chaque piste, j'ai lu :
- les `removed_provisions` de la loi visée et sa proposition entière ;
- ses versions `VIGUEUR_DIFF` éventuelles ;
- l'article d'application en entier (source, proposition, motif, notes).

La question posée à chaque fois : le texte d'application organise-t-il encore ce que la loi a retiré, ou ne le vise-t-il que pour l'ancien régime ?

**Contrôle.** `python3 -B apply/check_changes.py J12` donne 4 lignes construites et validées, et `problems` est vide. Les diagnostics sont attendus :
- `explicit_normative_reduction` sur FD, 314 et 313-0 BR ;
- `length_change` sur YX (ratio 6,07, déjà élevé avant ma correction), 314 et 313-0 BR.

Rien n'a été écrit en production. Cette revue est faite par une IA et ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9a | S9x | Total |
|---|---|---|---|
| G | 4 | 0 | 4 |
| m | 2 | 0 | 2 |
| déjà réglé | 6 | 1 | 7 |
| faux positif | 36 | 4 | 40 |

J'ai fait 4 corrections (mode `replace`) et 1 demande à un autre groupe (J14). Rien n'est écarté (`skipped` vide).

## Corrections appliquées

**SWEEP-J12-46quater0FD : 46 quater-0 FD (LEGIARTI000006298202), G (F1/F5), appliquée.**
- **Défaut.** L'article est maintenu à l'identique. Il décompte « le délai de deux ans prévu au c du 2 de l'article 119 ter et au deuxième alinéa du 1 de l'article 119 quater [...] pendant lequel les titres doivent être conservés », et l'étend à 182 B bis. Or 119 quater et 182 B bis proposés suppriment ce délai pour les paiements futurs : « Pour les intérêts payés à compter de l'entrée en vigueur de la présente loi, aucune durée minimale de détention ni aucun engagement de conservation de cette participation n'est exigé ».
- **Changement.** Le décompte depuis l'inscription en compte est conservé mot pour mot pour les dividendes de 119 ter, qui gardent leurs deux ans. Pour 119 quater et 182 B bis, il ne vaut plus que pour les intérêts et redevances payés avant la réforme. Pour les paiements futurs, plus aucun délai n'est décompté.
- **Mise à jour du dossier.** Le statut passe à `rewrite_draft`, avec `normative_reduction` et un bilan d'impact `coordination_only`. Les notes fausses (« deux ans et alternative de l'engagement maintenus ») sont corrigées.
- **Alignement.** Il s'agit d'une coordination avec une réforme déjà décidée. Aucune formalité n'est ajoutée.

**SWEEP-J12-46quater0YX : 46 quater-0 YX (LEGIARTI000006298277), G (F5), appliquée.**
- **Défaut.** Le texte retenait encore « selon les règles applicables à la société la veille de son entrée dans ce régime ». Or 220 nonies proposé a remplacé cette référence par une référence objective : les règles « en vigueur la veille de l'entrée en vigueur du régime d'imposition à la distribution, appliquées aux caractéristiques de cette société et de l'exercice considéré ». Il l'étend expressément aux sociétés créées après cette date, et ses notes demandent cette coordination.
- **Changement.** YX reprend mot pour mot la référence de la loi. Le reste est inchangé.
- **Mise à jour du dossier.** `reference_coherence.referrer_sha256` est mis à l'empreinte de la nouvelle proposition. La cible et les analyses sont inchangées. **Coordinateur : vérifier que ce certificat est accepté par `check_guards`, ou le régénérer.**
- **Alignement.** L'avantage n'est pas étendu : il suit la loi.

**SWEEP-J12-314 : 314 (LEGIARTI000006299319), G (F1/F5), appliquée.**
- **Défaut.** Le texte organisait « La demande d'exonération [...] prévue au II de l'article 1384 » « sans recommencement du délai prévu au II ». Or ce II proposé dispose : « L'exonération s'applique sans demande spéciale dans les quatre mois de l'ouverture des travaux ». Les notes de 1384 signalaient elles-mêmes cette contradiction.
- **Changement.**
  - La demande devient la demande facultative du II.
  - Aucune demande n'est exigée dans les quatre mois.
  - La transition renvoie à celle de 1384, pour ne pas étendre l'exonération dans le temps.
  - Les acquis sont conservés : dépôt en mairie ou au service des impôts, intégration à un dossier existant, pas de second envoi des données déjà détenues.
- **Mise à jour du dossier.** Le motif et les notes sont corrigés (l'ancien texte disait : « retirer la demande ou les quatre mois nécessiterait une réforme de 1384 II »). Le bilan d'impact reçoit un effet de coordination.

**SWEEP-J12-313-0BR : 313-0 BR (LEGIARTI000018658153), G (F1/F5), appliquée.**
- **Défaut.** L'article est maintenu à l'identique : « doit être déposée avant le 16 mai de chaque année ». Or le d du 3° de 990 E proposé dispose : « En l'absence de modification à déclarer, l'exonération demeure applicable sans déclaration ni confirmation annuelle ». Et 990 D proposé rend ces obligations non exigibles pour les années sans taxe.
- **Changement.** L'échéance avant le 16 mai vaut pour les seules déclarations encore dues, « selon la périodicité et les dispenses » des d et e. Elle ne s'applique pas aux années sans taxe. Les obligations échues gardent leur régime.
- **Mise à jour du dossier.** Le statut passe à `rewrite_draft`, avec `normative_reduction` et un bilan d'impact `coordination_only`. La note dépassée « Une réforme de l'annualité doit viser 990 E et 990 F eux-mêmes » est corrigée.

## Demande à un autre groupe

**J14, 46 quater-0 FB (LEGIARTI000035302070).** Cet article organise encore la déclaration de l'engagement prévu « au deuxième alinéa du 1 de l'article 119 quater et au 2 de l'article 182 B bis », et la désignation du représentant. Ces deux articles proposés suppriment l'engagement et le représentant pour les paiements futurs. J'ai rédigé un alinéa exact sous `requests`, qui limite ces renvois aux paiements antérieurs. La piste FB figure dans le paquet J14.

## Défauts `m`, non corrigés (articles non modifiés)

- **406 A 13 (LEGIARTI000006299773), F4/F10.**
  - Le texte dit : « Le présent article ne constitue pas un fondement autonome de placement sous séquestre après l’abrogation de l’article 1751 ».
  - Les notes disent : « texte de destination manquant ».
  - Or 1751 a une version VIGUEUR_DIFF au 1er janvier 2029 (LEGIARTI000052845689), qui a sa proposition.
  - L'effet est sans portée, car la condition n'arrive pas. Correction possible : supprimer cette phrase.
- **41-0 A bis A (LEGIARTI000019613253), F10.** Les notes disent : « L'annualité législative de l'état n'est pas supprimée par ce règlement ». Or 151 octies B proposé, au V, dispose : « Pour les années suivantes, cet état n'est joint que si ces renseignements ont changé ». Le texte de l'article est conforme.

## Déjà réglé (7)

- 49 E : coordonné avec 242 ter.
- 49 septies WH : relevé limité aux reprises effectives du III.
- 315 octies : délais de 1395 sans fenêtre.
- 366 M : exclusion de l'IS de distribution.
- 383 ter : renvoi direct à 1684.
- 404 C : gratuité de 809 pour les opérations nouvelles.
- 281 J : engagements non requis pour les décès futurs.

## Faux positifs (40)

Une citation par piste figure dans `audit/sweeps/J12.json`. Les cas typiques :
- **ordre d'imputation ou année civile de calcul d'un crédit**, sans rapport avec l'agrément, la convention ou le dépôt retiré : YR, YU, YY, YZ, YZC, YA, YB, YP, YR (244 quater J), ZZA, ZZC, 49 septies J ;
- **renvoi à une subdivision intacte** de la loi réduite : ZC, 46 quindecies I, 49 octies B et C, 49 V, 49 Y, 324 W ;
- **décret qui garde une fonction utile** : 111-0 G (comptabilité matières, que 302 D bis déclare maintenue) ;
- **article d'un autre code de même numéro** : 169-0 A vise CGI 403, alors que la cible de la piste est l'article 403 de l'annexe III.

## Constats connexes, hors paquet, non corrigés

- **46 AGG bis (LEGIARTI000051762600), F10.** Les notes disent encore « après délai légal d'un an », alors que 199 decies E proposé supprime ce délai. Le texte ne le reprend pas. Défaut `m`, sans propriétaire dans `assignment.json`.
- **1684 proposé (LEGIARTI000033812284), F7.** La formule « dans les conditions suivantes : a) La condition d'avis fiscal distinct de cession est supprimée ; b) [...] est supprimée » est maladroite, mais son effet est clair. Défaut `m`.
- **CCH D319-11, à vérifier.** Les notes de 244 quater U signalent que D319-11 garde la convention avec l'Etat pour octroyer les avances. Ce point est hors paquet et je ne l'ai pas vérifié.

## Points pour l'auteur

- **YX.** Le certificat `reference_coherence` doit être revérifié par l'outil gardé.
- **46 quater-0 FB.** La correction dépend de l'acceptation de la demande par J14. Sans elle, FB et FD restent incohérents pour les intérêts et redevances.
- **Pièces hors corpus.** Aucune n'a été inventée : directives 2003/49/CE et 2011/96/UE, arrêté de l'article 990 F, formulaires.

Revue IA : rien de ceci ne vaut validation par un juriste.
