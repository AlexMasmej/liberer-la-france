# J02 : quatrième balayage (S9x, S12, S13, S15), code de la sécurité sociale

Texte lu en production, en lecture seule, le 2026-10-29 (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`). Paquet `audit/sweeps/packet-J02.json` : 60 articles et 64 pistes. Une piste a été ajoutée parce qu'un défaut a été relevé à la lecture (D162-25-1, famille S15).

## Décompte

- 65 pistes : 28 faux positifs, 35 déjà réglés, 2 défauts G et aucun m.
- 2 corrections dans `apply/J02/changes.json`, en mode `replace`. `python3 -B apply/check_changes.py J02` donne `problems: []`.
- Aucune requête vers un autre groupe. Les deux articles de la liste `previous_owner` sont des faux positifs : R133-44 (Y02) et L862-7 (W05). Il n'y a donc pas de variante `Y02jb` ni `W05jb`.

## Corrections

### SWEEP-J02-D162-25-1 : CSS D162-25-1 (LEGIARTI000043412723), appliquée (G, F5)

- **Défaut.** La transition faisait jouer le renouvellement de plein droit à partir de « l’entrée en vigueur de la disposition législative modifiant le I de l’article L. 162-1-7 pour permettre un renouvellement de plein droit de trois ans, dans une limite totale de six ans ». Le projet ne fait pas cette modification : L162-1-7 proposé (LEGIARTI000053283421) garde « trois ans renouvelable une fois, dans la limite de dix-huit mois ». La condition ne pouvait donc jamais se réaliser, et la réforme décidée (renouvellement sans décision distincte) restait sans date d'application.
- **Correction.** La condition est retirée. Le renouvellement de plein droit s'applique aux inscriptions en cours « à la date d’entrée en vigueur du décret portant la présente rédaction » et aux inscriptions ultérieures. Ont été mis à jour : le motif, les notes (y compris la phrase « ce lot ne la réalise pas », devenue sans objet) et `substantive_impact` (`after`, `conditions_and_transition`, `scope_limitations`).
- **Inchangé.** Les durées de trois et six ans de la source, les critères de l'acte innovant, les radiations pour raisons de santé publique, la hiérarchisation définitive subsidiaire et la protection des inscriptions et renouvellements acquis. Aucune durée n'est allongée.
- **Point pour l'auteur.** Il existe un conflit de source, antérieur au projet : depuis la version LEGIARTI000046812411 (31 décembre 2023), L162-1-7 I prévoit « dans la limite de dix-huit mois », alors que D162-25-1 garde trois ans de renouvellement et six ans au total. Deux options : aligner la loi sur six ans, ce qui étend une faveur et suppose une décision ; ou plafonner le décret à la limite légale. Aucune n'a été appliquée.

### SWEEP-J02-R861-16-2 : CSS R861-16-2 (LEGIARTI000044492530), appliquée (G, F1)

- **Défaut.** Au I 1°, le bulletin devait encore préciser « les circonstances dans lesquelles il peut être mis fin à la prise en charge prévue à l'article L. 861-3, en application des dispositions de l'article L. 861-11 ». Or L861-11 proposé (LEGIARTI000044628815) interdit toute suspension ou fermeture fondée sur le seul défaut de paiement. Les notes de l'article le disaient déjà : « Les supports doivent retirer ces anciens motifs pour les périodes nouvelles. »
- **Correction.** La mention est retirée. Une phrase de transition est ajoutée : les bulletins adressés après l'entrée en vigueur de la modification de L861-11 ne mentionnent plus de motif de fin fondé sur cet article, et les bulletins déjà adressés ne sont pas à refaire. La ligne reçoit une `removed_provisions` supplémentaire et un effet `obligation_removed` (`css-bulletin-mention-fin-droit-l861-11`).
- **Inchangé.** Le montant de la participation, les garanties, la durée du droit, le mandat de prélèvement sans frais, la dispense de renvoi au renouvellement et le recouvrement des participations dues. Aucune mention de remplacement n'est ajoutée.

## Qualification piste par piste

| # | Article | LEGIARTI | Piste | Cible | Qualification | Corrigé |
|---|---|---|---|---|---|---|
| 1 | L642-6 | LEGIARTI000036379509 | S12/F4 | L244-8-1 | faux positif | non |
| 2 | L641-1 | LEGIARTI000036391505 | S12/F4 | L355-2 | faux positif | non |
| 3 | D171-12 | LEGIARTI000036475158 | S9x/F1+F5 | L171-3 | déjà réglé | non |
| 4 | R217-9 | LEGIARTI000036914458 | S9x/F1+F5 | L217-3 | déjà réglé | non |
| 5 | R165-48-1 | LEGIARTI000037114513 | S9x/F1+F5 | L165-1 | faux positif | non |
| 6 | D755-7 | LEGIARTI000037251362 | S12/F4 | L751-1 | faux positif | non |
| 7 | R382-80 | LEGIARTI000037551909 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 8 | R142-1 | LEGIARTI000037595656 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 9 | R133-44 | LEGIARTI000037877089 | S15/F5 |  | faux positif | non |
| 10 | L861-10 | LEGIARTI000037950193 | S12/F4 | L861-3 | faux positif | non |
| 11 | R762-8 | LEGIARTI000038673066 | S9x/F1+F5 | L762-5 | déjà réglé | non |
| 12 | R762-11 | LEGIARTI000038673094 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 13 | D762-7 | LEGIARTI000038676525 | S9x/F1+F5 | L762-6-5 | déjà réglé | non |
| 14 | R861-30 | LEGIARTI000038677019 | S9x/F1+F5 | L861-11 | déjà réglé | non |
| 15 | R861-33 | LEGIARTI000038677025 | S9x/F1+F5 | L861-11 | faux positif | non |
| 16 | R861-35 | LEGIARTI000038677029 | S9x/F1+F5 | L861-11 | faux positif | non |
| 17 | D221-39 | LEGIARTI000038679901 | S9x/F1+F5 | L221-1-4 | déjà réglé | non |
| 18 | R632-1 | LEGIARTI000038787314 | S9x/F1+F5 | L632-1 | faux positif | non |
| 19 | R261-1 | LEGIARTI000038789836 | S9x/F1+F5 | L223-1 | déjà réglé | non |
| 20 | R243-12 | LEGIARTI000039222430 | S9x/F1+F5 | L133-5-4 | déjà réglé | non |
| 21 | R115-1 | LEGIARTI000039308773 | S9x/F1+F5 | L133-5 | faux positif | non |
| 22 | R413-10 | LEGIARTI000039342937 | S9x/F1+F5 | L413-8 | faux positif | non |
| 23 | R413-6 | LEGIARTI000039344520 | S9x/F1+F5 | L413-8 | déjà réglé | non |
| 24 | R160-2 | LEGIARTI000039344532 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 25 | R142-9 | LEGIARTI000041404184 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 26 | R142-13-2 | LEGIARTI000041404287 | S9x/F1+F5 | L242-7 | déjà réglé | non |
| 27 | D642-5-2 | LEGIARTI000041966458 | S9x/F1+F5 | L642-1 | déjà réglé | non |
| 28 | D632-1 | LEGIARTI000041966755 | S9x/F1+F5 | L632-1 | déjà réglé | non |
| 29 | D742-18 | LEGIARTI000041967272 | S13/F3 | L742-6 | déjà réglé | non |
| 30 | D169-4 | LEGIARTI000041968991 | S9x/F1+F5 | L169-13 | déjà réglé | non |
| 31 | D169-5 | LEGIARTI000041969214 | S9x/F1+F5 | L162-1-7 | faux positif | non |
| 32 | R847-2 | LEGIARTI000042247849 | S9x/F1+F5 | L845-2 | déjà réglé | non |
| 33 | R165-4-2 | LEGIARTI000042270883 | S9x/F1+F5 | L165-1 | faux positif | non |
| 34 | R165-4-2 | LEGIARTI000042270883 | S9x/F1+F5 | L165-4 | déjà réglé | non |
| 35 | R491-1 | LEGIARTI000042586762 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 36 | R491-2 | LEGIARTI000042586764 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 37 | L162-17-4 | LEGIARTI000042685804 | S12/F4 | L138-13 | faux positif | non |
| 38 | R163-31 | LEGIARTI000042803622 | S9x/F1+F5 | L162-17-8 | déjà réglé | non |
| 39 | D160-2 | LEGIARTI000042947082 | S9x/F1+F5 | L821-1 | faux positif | non |
| 40 | R815-61 | LEGIARTI000042964341 | S9x/F1+F5 | L815-7 | faux positif | non |
| 41 | R412-2 | LEGIARTI000043128366 | S9x/F1+F5 | L412-4 | faux positif | non |
| 42 | R162-33-25 | LEGIARTI000043186687 | S9x/F1+F5 | L162-22-8-2 | déjà réglé | non |
| 43 | R847-1-1 | LEGIARTI000043280745 | S9x/F1+F5 | L845-3 | faux positif | non |
| 44 | R847-1-1 | LEGIARTI000043280745 | S9x/F1+F5 | L845-2 | déjà réglé | non |
| 45 | R133-9-2 | LEGIARTI000043281678 | S9x/F1+F5 | L142-4 | déjà réglé | non |
| 46 | D162-25-1 | LEGIARTI000043412723 | S9x/F1+F5 | L162-1-7 | faux positif | non |
| 47 | R162-52 | LEGIARTI000043413482 | S9x/F1+F5 | L162-1-7 | déjà réglé | non |
| 48 | R162-52 | LEGIARTI000043413482 | S9x/F1+F5 | L165-1 | faux positif | non |
| 49 | D136-3 | LEGIARTI000043563661 | S9x/F1+F5 | L136-7 | faux positif | non |
| 50 | R165-44-5 | LEGIARTI000043759130 | S9x/F1+F5 | L165-1 | faux positif | non |
| 51 | R165-44-7 | LEGIARTI000043759141 | S9x/F1+F5 | L162-17-2-1 | déjà réglé | non |
| 52 | D162-15 | LEGIARTI000044102672 | S9x/F1+F5 | L162-30-2 | déjà réglé | non |
| 53 | D162-14 | LEGIARTI000044102681 | S9x/F1+F5 | L162-30-2 | déjà réglé | non |
| 54 | R861-16-2 | LEGIARTI000044492530 | S9x/F1+F5 | L861-11 | G | oui |
| 55 | D185-1 | LEGIARTI000044511723 | S9x/F1+F5 | L162-1-7 | faux positif | non |
| 56 | L862-7 | LEGIARTI000044628803 | S12/F4 | L861-3 | faux positif | non |
| 57 | R161-71 | LEGIARTI000044635646 | S9x/F1+F5 | L162-1-7 | faux positif | non |
| 58 | R161-71 | LEGIARTI000044635646 | S9x/F1+F5 | L165-1 | faux positif | non |
| 59 | R211-1-2 | LEGIARTI000044929742 | S9x/F1+F5 | L221-3-1 | déjà réglé | non |
| 60 | D612-2 | LEGIARTI000045133645 | S9x/F1+F5 | L635-4-1 | faux positif | non |
| 61 | R162-62 | LEGIARTI000045186840 | S9x/F1+F5 | L162-58 | déjà réglé | non |
| 62 | R162-60 | LEGIARTI000045186861 | S9x/F1+F5 | L162-58 | déjà réglé | non |
| 63 | R433-15 | LEGIARTI000045370964 | S9x/F1+F5 | L433-1 | déjà réglé | non |
| 64 | R761-2 | LEGIARTI000045417202 | S15/F5 |  | faux positif | non |
| 65 | D162-25-1 | LEGIARTI000043412723 | S15/F5 | L162-1-7 | G | oui |

Les citations exactes et leur justification figurent dans `audit/sweeps/J02.json` (champ `evidence`).

## Observations hors périmètre (non corrigées, pour l'auteur)

- L162-30-2 (LEGIARTI000041398036) est `ABROGE_DIFF` au 1er janvier 2027. Sa proposition affirme pourtant : « La faculté de conclure de nouveaux contrats ouvrant droit à intéressement demeure applicable au-delà du 1er janvier 2027. » D162-14 et D162-15 renvoient à cet article. Le corpus ne contient aucune version suivante de cet article. La phrase semble donc prolonger un article abrogé (famille F4, à confirmer, hors paquet). Garder ou non le contrat facultatif après 2027 est un choix qui revient à l'auteur.
- Les notes de L751-1 (LEGIARTI000031323778) disent « sans NOTA ni texte successeur joint ». Or le successeur LEGIARTI000054466946 (1er janvier 2028) est au corpus. C'est un défaut F10 (m), sur un article hors paquet.

Revue IA : ce n'est pas une validation par un juriste.
