# J01 : quatrième balayage (S9x, S12, S15), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-J01.json`, soit 60 articles du CSS et 63 pistes (47 S9x, 14 S12, 2 S15). Contrôle : `python3 -B apply/check_changes.py J01` donne 11 lignes construites, 11 validées et `problems` vide. Seul diagnostic : R165-76 est une réduction déclarée, et ses renvois changent (R. 165-1 retiré, avec l'exception à l'obligation supprimée ; L. 165-1-3 ajouté). Ces deux effets sont voulus.

Rien n'a été écrit en production. Revue faite par une IA, sans validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 11, toutes corrigées (10 F4 sur L434-16, 1 F1+F5 sur R165-76) |
| m | 0 piste (une observation annexe, R133-42, non corrigée) |
| déjà réglé | 36 |
| faux positif | 16 |

Corrections : 11 lignes en mode `replace`. Six articles reviennent à la source maintenue (`retained_unchanged`) ; cinq gardent une proposition corrigée. Aucune demande à un autre groupe, rien d'écarté (`skipped` vide).

Articles avec `previous_owner` : R752-1 (W01), R133-42 (Y01), L922-8 (B09) et D162-30 (Y01). Les quatre sont des faux positifs. Aucune correction n'est nécessaire, donc aucun dossier de variante (`W01ja`, `Y01ja`, `B09ja`) n'a été créé.

## Défauts confirmés et corrigés

### Famille S12 sur L434-16 (10 articles, F4), objection `SWEEP-J01-S12-L434-16`

- **Défaut.** Dix propositions ajoutaient un alinéa de relais « à compter de l'abrogation de l'article L. 434-16 » (ou « Après l'abrogation… »). Cet alinéa figeait le minimum à « la veille de cette abrogation », puis le revalorisait selon L161-25.
  - Or L434-16 n'est pas abrogé. Sa version LEGIARTI000031688385 (ABROGE_DIFF au 1er novembre 2026) est remplacée par LEGIARTI000051288487 (VIGUEUR_DIFF, loi n° 2025-199, art. 90).
  - Cette nouvelle version maintient « un minimum déterminé au 1er avril de chaque année d'après le coefficient mentionné à l'article L. 161-25 ». Les deux versions ont une proposition.
  - C'est le défaut déjà corrigé pour D412-97 (X3, AUDIT-S11N-04).
  - Pour R754-9, la clause figeait de plus L434-16 « dans [sa] rédaction applicable la veille de son abrogation ». Elle gardait ainsi le renvoi au « quatrième alinéa de l'article L. 434-2 », que la rédaction de 2026 remplace par le III.
- **Retour à la source maintenue** (`retained_unchanged`, `proposed_xml: null`, impact `retained_necessary`, sur le modèle de X3). Seul l'alinéa de relais avait été ajouté :
  - D412-85 (LEGIARTI000006736835) ;
  - D412-89 (LEGIARTI000006736970) ;
  - D412-99-2 (LEGIARTI000006736855) ;
  - D412-99-5 (LEGIARTI000006736858) ;
  - R413-3 (LEGIARTI000006750223) ;
  - R754-9 (LEGIARTI000006752632).
- **Alinéa retiré, reste de la proposition conservé :**
  - D412-92 (LEGIARTI000030067856) : la référence de trente-cinq heures et sa transition sont conservées. Le second effet d'impact (continuité) est retiré.
  - D412-103 (LEGIARTI000032542446) et D412-108 (LEGIARTI000033226188) : la précision « minimum mentionné au premier alinéa de l'article L. 434-16 » est conservée. La mention « dans son champ d'application temporel » est retirée : elle ne servait qu'au relais. L'effet d'impact décrit désormais la seule précision du renvoi (`atmp-base-annuelle-renvoi-minimum`).
  - L413-5 (LEGIARTI000025016224) : la réserve de transition sur L434-8 est conservée. L'effet est rattaché à la mesure `atmp-survivant-fin-duree-lien`.
- **Motifs et notes.** Les affirmations fausses sont rectifiées : abrogation « annoncée », successeur « absent » ou « non fourni », L434-2 postérieur « absent », citation d'une phrase du projet de L434-16 retirée depuis (RT-INV-03).
- **Contrôle.** Aucun autre brouillon de la production ne contient « abrogation de l'article L. 434-16 ».

### R165-76 (LEGIARTI000034618444), piste S9x vers L165-1-3 (F1+F5), objection `SWEEP-J01-S9x-R165-76`

- **Défaut.** Le II imposait encore au prestataire de transmettre « au moins une fois par mois » (ou « au moins une fois tous les trois mois ») les données d'utilisation et d'identification du patient au service du contrôle médical.
  - Cette obligation exécutait le quatrième alinéa source de L165-1-3 (« le distributeur au détail transmet à l'assurance maladie, avec l'accord du patient, les données permettant d'attester du respect des conditions d'utilisation »).
  - La proposition de L165-1-3 (LEGIARTI000051285324) supprime cet alinéa : les données « peuvent être télétransmises » au contrôle médical. Ses notes disent que la « transmission obligatoire à l'assurance maladie [...] disparaît ».
  - Les notes de R165-76 revendiquaient au contraire le maintien des périodicités.
- **Correction.**
  - Le premier alinéa du II devient une faculté : « peut transmettre », « Cette transmission n'est pas obligatoire et n'est soumise à aucune périodicité minimale. » L'exception tirée de l'arrêté de R. 165-1, devenue sans objet, disparaît.
  - La transition est ajoutée au dernier alinéa : transmissions restant à effectuer à compter de la nouvelle rédaction de L165-1-3, données déjà transmises préservées.
  - Lignes : `change_type: normative_reduction`, `removed_provisions` renseigné. Impact `coordination_only` sur la mesure `dispositifs-medicaux-remboursement-sans-observance` de L165-1-3.
- **Inchangé.** Consentement écrit, recueil, détermination du niveau d'utilisation et modulation fournisseur, transmission au prescripteur (utile à la réévaluation que la loi conserve), interdiction de géolocalisation et d'identification auprès du fabricant. Aucune sanction ne s'attachait au défaut de transmission.

## Points laissés à l'auteur

- **R165-76.** Le choix inverse, maintenir la transmission mensuelle pour vérifier la modulation tarifaire facturée par le prestataire, aurait une utilité de contrôle. Il contredit toutefois la note de L165-1-3 et l'absence de toute transmission obligatoire dans la loi proposée. À trancher si l'auteur veut garder ce contrôle par une base législative expresse.
- **R133-42** (Y01, non modifié). La suppression du bilan annuel, d'origine purement réglementaire, est datée par « l'entrée en vigueur de la loi supprimant cette obligation ». Or aucune loi ne vise ce bilan. C'est une rédaction maladroite (m), sans effet bloquant, puisque la première phrase (« Aucun bilan annuel distinct n'est exigé ») est inconditionnelle.
- **D412-103 / D412-108.** La précision au « minimum » du premier alinéa est un choix de la seconde passe, conservé. Il n'est pas réexaminé ici.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| D162-1-7 (LEGIARTI000006735431) | S9x/F1+F5 | L162-5-3 | déjà réglé | non |
| D412-85 (LEGIARTI000006736835) | S12/F4 | L434-16 | G (F4) | oui |
| D412-99-2 (LEGIARTI000006736855) | S12/F4 | L434-16 | G (F4) | oui |
| D412-99-5 (LEGIARTI000006736858) | S12/F4 | L434-16 | G (F4) | oui |
| D412-89 (LEGIARTI000006736970) | S12/F4 | L434-16 | G (F4) | oui |
| D461-20 (LEGIARTI000006737093) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| D634-14 (LEGIARTI000006738001) | S9x/F1+F5 | L353-1 | faux positif | non |
| D713-24 (LEGIARTI000006738448) | S9x/F1+F5 | L162-5-3 | faux positif | non |
| R174-18 (LEGIARTI000006747954) | S9x/F1+F5 | L174-18 | déjà réglé | non |
| R221-11 (LEGIARTI000006748678) | S9x/F1+F5 | L221-3-1 | déjà réglé | non |
| R242-6-2 (LEGIARTI000006748761) | S9x/F1+F5 | L241-5-1 | déjà réglé | non |
| R243-1-1 (LEGIARTI000006748781) | S9x/F1+F5 | L243-1-1 | déjà réglé | non |
| R353-2 (LEGIARTI000006749405) | S9x/F1+F5 | L353-1 | faux positif | non |
| R371-4 (LEGIARTI000006749475) | S9x/F1+F5 | L371-6 | déjà réglé | non |
| R382-98 (LEGIARTI000006749805) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| R412-1 (LEGIARTI000006750202) | S9x/F1+F5 | L412-4 | déjà réglé | non |
| R413-3 (LEGIARTI000006750223) | S12/F4 | L434-2 | faux positif | non |
| R413-3 (LEGIARTI000006750223) | S12/F4 | L434-16 | G (F4) | oui |
| R413-16 (LEGIARTI000006750237) | S9x/F1+F5 | L413-8 | déjà réglé | non |
| R433-17 (LEGIARTI000006750334) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| R443-1 (LEGIARTI000006750453) | S9x/F1+F5 | L443-1 | déjà réglé | non |
| R581-6 (LEGIARTI000006750783) | S9x/F1+F5 | L581-5 | déjà réglé | non |
| R531-3 (LEGIARTI000006750821) | S9x/F1+F5 | L531-4 | déjà réglé | non |
| R742-13 (LEGIARTI000006752534) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| R752-1 (LEGIARTI000006752557) | S12/F4 | L751-1 | faux positif | non |
| R754-9 (LEGIARTI000006752632) | S12/F4 | L434-16 | G (F4) | oui |
| R815-5 (LEGIARTI000006753542) | S9x/F1+F5 | L815-7 | déjà réglé | non |
| R815-18 (LEGIARTI000006753648) | S9x/F1+F5 | L815-7 | déjà réglé | non |
| R133-42 (LEGIARTI000018503702) | S15/F5 | — | faux positif | non |
| R353-12 (LEGIARTI000020791843) | S9x/F1+F5 | L353-6 | faux positif | non |
| R413-12 (LEGIARTI000022021379) | S9x/F1+F5 | L413-8 | déjà réglé | non |
| R173-15-1 (LEGIARTI000024082508) | S9x/F1+F5 | L351-4 | faux positif | non |
| L413-5 (LEGIARTI000025016224) | S12/F4 | L434-16 | G (F4) | oui |
| D376-1 (LEGIARTI000026510727) | S9x/F1+F5 | L376-1 | déjà réglé | non |
| R754-5 (LEGIARTI000029007611) | S9x/F1+F5 | L413-8 | déjà réglé | non |
| R815-10 (LEGIARTI000029007664) | S9x/F1+F5 | L815-7 | déjà réglé | non |
| R871-1 (LEGIARTI000029779013) | S9x/F1+F5 | L871-1 | faux positif | non |
| R531-4 (LEGIARTI000030055471) | S9x/F1+F5 | L531-4 | déjà réglé | non |
| D412-92 (LEGIARTI000030067856) | S12/F4 | L434-16 | G (F4) | oui |
| D643-4 (LEGIARTI000030100689) | S9x/F1+F5 | L643-2 | déjà réglé | non |
| L922-8 (LEGIARTI000030438909) | S12/F4 | L931-7-2 | faux positif | non |
| R932-5-6 (LEGIARTI000030586063) | S9x/F1+F5 | L932-41 | faux positif | non |
| R434-10 (LEGIARTI000030730333) | S9x/F1+F5 | L434-8 | déjà réglé | non |
| D861-2 (LEGIARTI000030819781) | S9x/F1+F5 | L861-3 | faux positif | non |
| R847-3 (LEGIARTI000031676262) | S9x/F1+F5 | L845-2 | déjà réglé | non |
| D160-12 (LEGIARTI000031806440) | S9x/F1+F5 | L160-13 | déjà réglé | non |
| D161-13-1 (LEGIARTI000031813522) | S9x/F1+F5 | L161-31 | déjà réglé | non |
| D161-13-1 (LEGIARTI000031813522) | S12/F4 | L162-16-4 | faux positif | non |
| R544-2 (LEGIARTI000031828207) | S9x/F1+F5 | L544-3 | déjà réglé | non |
| R454-4 (LEGIARTI000031828575) | S9x/F1+F5 | L454-2 | déjà réglé | non |
| R454-4 (LEGIARTI000031828575) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| R376-4 (LEGIARTI000031828587) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| D412-103 (LEGIARTI000032542446) | S12/F4 | L434-16 | G (F4) | oui |
| D412-108 (LEGIARTI000033226188) | S12/F4 | L434-16 | G (F4) | oui |
| R160-13 (LEGIARTI000033240399) | S9x/F1+F5 | L142-4 | déjà réglé | non |
| D162-12 (LEGIARTI000034459871) | S9x/F1+F5 | L162-30-2 | faux positif | non |
| R165-75 (LEGIARTI000034618407) | S9x/F1+F5 | L165-1-3 | déjà réglé | non |
| R165-77 (LEGIARTI000034618411) | S9x/F1+F5 | L165-1-3 | déjà réglé | non |
| R165-76 (LEGIARTI000034618444) | S9x/F1+F5 | L165-1-3 | G (F1+F5) | oui |
| R161-4-1 (LEGIARTI000034623298) | S9x/F1+F5 | L161-13-1 | déjà réglé | non |
| R114-35 (LEGIARTI000034669311) | S9x/F1+F5 | L114-19 | déjà réglé | non |
| D756-5 (LEGIARTI000034726710) | S9x/F1+F5 | L613-7 | faux positif | non |
| D162-30 (LEGIARTI000034731961) | S15/F5 | — | faux positif | non |
