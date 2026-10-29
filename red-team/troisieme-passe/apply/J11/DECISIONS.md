# J11 : quatrième balayage (S9a, S9x), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` (exports dans `evidence/cited/production-20261029/`) et SQLite en `mode=ro`. Le paquet `audit/sweeps/packet-J11.json` compte 53 articles des annexes II et III du CGI et 53 pistes : 41 S9a et 12 S9x.

Méthode : pour chaque piste, j'ai lu l'article d'application en entier (source, proposition, motif, notes), puis les `removed_provisions` et la proposition de la loi visée. J'ai lu en entier les propositions de CGI 41, 93 quater, 151 nonies, 151 octies, 289 bis, 289 A, 1504 et 795 A. Pour CGI 39, j'ai vérifié le rang des alinéas visés au 5° du 1, au 1° bis, au 1° quater et au 9. Pour les autres cibles, j'ai lu les passages visés. Question posée à chaque fois : l'article d'application organise-t-il encore ce que la loi retire, ou vise-t-il seulement une règle conservée ou l'ancien régime ? J'ai aussi cherché dans les quatre annexes les autres textes qui appliquent CGI 41 IV, 151 nonies et 93 quater. Il n'y en a pas d'autre, hormis l'annexe II 74-0 E ter, qui vise 151 nonies pour les valeurs du patrimoine professionnel, sans état.

Contrôle : `python3 -B apply/check_changes.py J11` construit et valide 3 lignes, et `problems` est vide. Seul diagnostic : `explicit_normative_reduction`, voulu. Il n'y a aucun changement de longueur hors bornes ni aucun renvoi modifié.

Rien n'a été écrit en production. Cette revue est faite par une IA et ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9a | S9x | Total |
|---|---|---|---|
| G | 3 | 0 | 3 |
| m | 0 | 0 | 0 |
| déjà réglé | 7 | 3 | 10 |
| faux positif | 31 | 9 | 40 |

Il y a 3 corrections. `requests` et `skipped` sont vides.

Deux articles avaient un `previous_owner` : 242 nonies E de l'annexe II (B03) et 41 Y de l'annexe III (A8). Leurs pistes sont « déjà réglé », sans correction. Je n'ai donc créé aucun dossier de variante (`apply/B03jk/`, `apply/A8jk/`), puisqu'il n'y avait rien à y valider.

## Corrections appliquées

### SWEEP-J11-A3-10H-0bis : annexe III 10 H-0 bis (LEGIARTI000006297629), piste S9a/F1+F5 sur CGI 41, G, appliquée (mode `replace`, `full_repeal`)

- **Défaut.** La proposition disait : « Les états dont la production est prévue aux b, c et d du IV de l'article 41 du code général des impôts peuvent être établis sur tout support […] Ces états mentionnent notamment […] ». Or CGI 41 (LEGIARTI000020033991) proposé supprime les trois états (« b. Aucun état distinct […] », « c. Aucun état de suivi […] », « d. Aucun état spécial […] »). Son V interdit au décret de les rétablir et applique la suppression aux échéances futures, « y compris pour les reports en cours ». Les notes affirmaient aussi, à tort, qu'il faudrait modifier 41 IV b à d.
- **Changement.** L'article est abrogé pour les états dont l'échéance intervient après la réforme, y compris pour les reports en cours, sans état ni document de remplacement. Les échéances antérieures gardent la rédaction antérieure et la liberté de support déjà décidée. Aucun état déjà produit n'est à refaire. Les droits, recours et la loi répressive plus douce sont préservés.
- **Dossier.** Le motif, les notes (correction F10), `removed_provisions`, `repeal_scope` et `substantive_impact` sont mis à jour. L'effet nouveau est une `coordination` sous la `measure_id` de CGI 41, sans double compte.
- **Alignement.** La correction rend effective une suppression déjà décidée par la loi proposée. Elle ne crée aucune formalité.

### SWEEP-J11-A3-41novovicies : annexe III 41 novovicies (LEGIARTI000006297912), piste S9a/F1+F5 sur CGI 93 quater, G, appliquée (mode `replace`, `normative_reduction`)

- **Défaut.** Le II b exigeait encore, pour tout acte, « un extrait ou une copie de l'acte comportant la demande de report ». Les notes et le bilan le justifiaient par « 93 quater IV 3 subordonne légalement le report à cette mention dans l'acte ». Or 93 quater (LEGIARTI000049641561) proposé dispose au IV 3 : « Le bénéfice du report prévu au 1 n'est pas subordonné à une mention dans l'acte […] elle n'a pas à être répétée dans cet acte ». Son IV 4 interdit au décret de la rétablir, pour les actes établis après la réforme.
- **Changement.** Le b ne demande plus aucun extrait ni copie pour les actes établis après la réforme. La jonction est conservée pour les actes antérieurs, dont la mention reste une condition légale selon la transition de 93 quater. Le I, le a (note annexe supprimée), le III et la transition sont inchangés.
- **Dossier.** Le motif, les notes, `benefit_review`, `removed_provisions` et `substantive_impact` sont mis à jour : l'affirmation fausse est retirée et une `coordination` est ajoutée sous la `measure_id` de 93 quater.
- **Alignement.** Il s'agit d'une suppression de contradiction. Aucune faveur n'est étendue : la condition des actes anciens n'est pas touchée.

### SWEEP-J11-A3-41-0Ater : annexe III 41-0 A ter (LEGIARTI000006297925), piste S9a/F1+F5 sur CGI 151 nonies, G, appliquée (mode `replace`, `full_repeal`)

- **Défaut.** La proposition remplaçait les deux états par « un document unique joint à la déclaration de revenus ». Or 151 nonies (LEGIARTI000037099936) proposé les supprime (2 du II et VI). Son 3 du II dispose : « Aucun décret d'application ne peut imposer les états spécifiques supprimés au 2 et au VI ni un document de remplacement ».
- **Changement.** L'article est abrogé pour les obligations dont l'échéance intervient après la réforme, y compris pour les reports nés antérieurement. Les obligations échues gardent la rédaction antérieure, avec la fusion des supports et la liberté de modèle déjà décidées. Le texte suit le VII de 151 nonies.
- **Dossier.** Le motif, les notes et `substantive_impact` sont mis à jour : `coordination` sous la `measure_id` de 151 nonies, plus les deux effets antérieurs, restreints aux obligations échues. `removed_provisions` et `repeal_scope` sont aussi mis à jour.
- **Alignement.** La correction rend effective une suppression décidée et supprime une formalité de remplacement interdite par la loi proposée.

## Points pour l'auteur

- Les notes de CGI 151 nonies (LEGIARTI000037099936, hors J11) disent que 41-0 A ter est « hors du lot et n'est pas déclaré réécrit ». Elles sont dépassées : ce défaut F10 relève du propriétaire de 151 nonies.
- Je n'ai pas recherché les formulaires, modèles, arrêtés ni les sanctions du CGI ou du LPF éventuellement fondés sur les seuls états supprimés de 41 et de 151 nonies.
- Les deux abrogations laissent aux échéances antérieures « la rédaction antérieure » de l'article. Si l'auteur préfère éteindre aussi ces obligations échues, c'est un choix plus large que les transitions de CGI 41 V et de 151 nonies VII. Je ne l'ai pas fait.

## Qualification par piste

| Article | LEGIARTI | Piste | Cible | Qualification |
|---|---|---|---|---|
| a2 310 K | LEGIARTI000043663379 | S9a/F1+F5 | 1499 | faux positif |
| a2 294 C | LEGIARTI000043854120 | S9a/F1+F5 | 795 A | faux positif |
| a2 339 | LEGIARTI000045128741 | S9a/F1+F5 | 1504 | faux positif |
| a2 336 | LEGIARTI000045128752 | S9a/F1+F5 | 1504 | faux positif |
| a2 335 | LEGIARTI000045128756 | S9a/F1+F5 | 1498 bis | déjà réglé |
| a2 242 novodecies | LEGIARTI000045632751 | S9a/F1+F5 | 289 A | déjà réglé |
| a2 209 | LEGIARTI000046086713 | S9x/F1+F5 | 278 sexies | faux positif |
| a2 207 | LEGIARTI000046086720 | S9a/F1+F5 | 256 C | faux positif |
| a2 16 C | LEGIARTI000047658145 | S9a/F1+F5 | 39 quinquies G | déjà réglé |
| a2 16 B | LEGIARTI000047658153 | S9a/F1+F5 | 39 quinquies G | faux positif |
| a2 310-0 H | LEGIARTI000047785461 | S9x/F1+F5 | 1384 A | faux positif |
| a2 16 A | LEGIARTI000049684171 | S9a/F1+F5 | 39 quinquies G | faux positif |
| a2 206 | LEGIARTI000049904359 | S9x/F1+F5 | 256 C | faux positif |
| a2 253 | LEGIARTI000050811267 | S9a/F1+F5 | 293 D | faux positif |
| a2 242 nonies A | LEGIARTI000050811276 | S9x/F1+F5 | 289 | déjà réglé |
| a2 242 nonies E bis | LEGIARTI000054543964 | S9a/F1+F5 | 289 bis | faux positif |
| a2 242 nonies E ter | LEGIARTI000054543966 | S9x/F1+F5 | 289 bis | faux positif |
| a2 242 nonies B | LEGIARTI000054552495 | S9x/F1+F5 | 289 bis | déjà réglé |
| a2 242 nonies E | LEGIARTI000054552509 | S9a/F1+F5 | 290 B | déjà réglé |
| a2 242 nonies H | LEGIARTI000054552531 | S9x/F1+F5 | 289 bis | déjà réglé |
| a3 3 | LEGIARTI000006296502 | S9x/F1+F5 | 39 | faux positif |
| a3 10 undecies | LEGIARTI000006296507 | S9x/F1+F5 | 39 | faux positif |
| a3 38 sexdecies A | LEGIARTI000006296577 | S9a/F1+F5 | 69 | faux positif |
| a3 39 A | LEGIARTI000006296693 | S9a/F1+F5 | 158 | faux positif |
| a3 41 duodecies F | LEGIARTI000006296718 | S9a/F1+F5 | 1678 bis | faux positif |
| a3 41 F | LEGIARTI000006296729 | S9a/F1+F5 | 31 | faux positif |
| a3 49 octies | LEGIARTI000006296872 | S9a/F1+F5 | 39 | faux positif |
| a3 70 sexies | LEGIARTI000006296920 | S9a/F1+F5 | 260 B | faux positif |
| a3 73 B | LEGIARTI000006296926 | S9a/F1+F5 | 262 | faux positif |
| a3 73 C | LEGIARTI000006296928 | S9a/F1+F5 | 262 | faux positif |
| a3 73 D | LEGIARTI000006296930 | S9a/F1+F5 | 262 | faux positif |
| a3 73 E | LEGIARTI000006296932 | S9a/F1+F5 | 262 | faux positif |
| a3 2 novodecies | LEGIARTI000006297555 | S9x/F1+F5 | 31 | faux positif |
| a3 2 novodecies A | LEGIARTI000006297557 | S9a/F1+F5 | 31 | faux positif |
| a3 2 novodecies B | LEGIARTI000006297558 | S9a/F1+F5 | 31 bis | faux positif |
| a3 2 C bis | LEGIARTI000006297568 | S9a/F1+F5 | 38 sexies | déjà réglé |
| a3 2 D | LEGIARTI000006297572 | S9x/F1+F5 | 39 | faux positif |
| a3 10 sexies | LEGIARTI000006297594 | S9x/F1+F5 | 39 | faux positif |
| a3 10 H-0 bis | LEGIARTI000006297629 | S9a/F1+F5 | 41 | G |
| a3 41-0 bis B | LEGIARTI000006297773 | S9a/F1+F5 | 93 A | faux positif |
| a3 41 bis | LEGIARTI000006297779 | S9a/F1+F5 | 112 | déjà réglé |
| a3 41 quinquies | LEGIARTI000006297781 | S9a/F1+F5 | 112 | faux positif |
| a3 41 duodecies J | LEGIARTI000006297795 | S9a/F1+F5 | 125 D | faux positif |
| a3 41 duodecies O | LEGIARTI000006297802 | S9a/F1+F5 | 242 ter | faux positif |
| a3 41 sexdecies E | LEGIARTI000006297820 | S9a/F1+F5 | 158 | faux positif |
| a3 41 sexdecies I | LEGIARTI000006297829 | S9a/F1+F5 | 158 | faux positif |
| a3 41 sexdecies L | LEGIARTI000006297832 | S9a/F1+F5 | 125 D | faux positif |
| a3 41 novovicies | LEGIARTI000006297912 | S9a/F1+F5 | 93 quater | G |
| a3 41-0 A | LEGIARTI000006297922 | S9a/F1+F5 | 151 septies | faux positif |
| a3 41-0 A bis | LEGIARTI000006297924 | S9a/F1+F5 | 151 octies | faux positif |
| a3 41-0 A ter | LEGIARTI000006297925 | S9a/F1+F5 | 151 nonies | G |
| a3 41 W | LEGIARTI000006297983 | S9a/F1+F5 | 163 quinquies B | faux positif |
| a3 41 Y | LEGIARTI000006297987 | S9a/F1+F5 | 163 quinquies B | déjà réglé |

Citations exactes de chaque piste : `audit/sweeps/J11.json`.
