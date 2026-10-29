# J15 : quatrième balayage (S9a, S9x), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro`. Les exports sont dans `evidence/cited/production-20261029/`. Le paquet `audit/sweeps/packet-J15.json` compte 53 articles (45 de l'annexe III, 8 de l'annexe IV) et 53 pistes : 45 S9a et 8 S9x, toutes adossées à une loi du CGI réduite (`normative_reduction`).

Méthode : pour chaque piste, j'ai lu les `removed_provisions` de la loi visée, puis sa proposition entière (ou ses passages pertinents pour les très longs articles 31, 156, 219, 244 quater B/U/W/Y). J'ai ensuite lu l'article d'application en entier (source et proposition, ou source maintenue). La question posée était chaque fois la même : le texte d'application organise-t-il encore ce qui a été retiré, ou le vise-t-il seulement pour un régime ancien ou une fonction utile ? J'ai aussi vérifié que les renvois ordinaux (alinéa, 1°, lettre) visent encore la bonne subdivision dans la loi proposée.

Contrôle : `python3 -B apply/check_changes.py J15` donne 3 lignes construites et validées, et `problems` est vide. Les diagnostics `explicit_normative_reduction` reprennent les `removed_provisions` déjà présents. Le `length_change` de l'annexe IV 35 (ratio 2,66) vient pour l'essentiel de la proposition existante. Variante B06 : `apply/B06jo/` est vide (la piste de 49 septies ZZB bis est un faux positif) ; elle est validée avec `problems` vide.

Rien n'a été écrit en production. Revue IA : ce n'est pas une validation par un juriste.

## Bilan

| Qualification | S9a | S9x | Total |
|---|---|---|---|
| G | 2 | 1 | 3 |
| m | 1 | 0 | 1 |
| déjà réglé | 1 | 2 | 3 |
| faux positif | 41 | 5 | 46 |

Il y a 3 corrections (mode `replace`), 1 demande à un autre groupe (Y15) et rien d'écarté.

## Corrections appliquées

**SWEEP-J15-313BQquater : annexe III 313 BQ quater (LEGIARTI000049642369), piste S9a → CGI 982, G (F1+F3).**
- **Défaut.** Le IV fixait les délais de communication « lui permettant de déclarer les informations requises sur les annexes prévues à l'article 982 », alors que 982 proposé (LEGIARTI000036385055) dispose « Aucune annexe détaillant ou évaluant séparément chacun de ces actifs n'est jointe à cette déclaration » et interdit au décret de « rétablir une annexe annuelle ».
- **Correction.** Le IV vise désormais la déclaration « de la valeur brute et de la valeur nette taxable de ses actifs sur la déclaration prévue au 1 du I de l'article 982 ». Les I à III (communications sur demande, utiles au calcul de la valeur nette taxable), le VI et le réemploi sont inchangés.
- **Déjà vu ?** Défaut signalé en remarque de lien dans `audit/V04.json` (T154, CGI 965), sans objection ni correction.

**SWEEP-J15-46quater0RH : annexe III 46 quater-0 RH (LEGIARTI000049642472), piste S9x → CGI 219, G (F1+F5).**
- **Défaut.** L'article organisait sans borne « L'état prévu au dernier alinéa du a septies du I de l'article 219 », y compris « Pour les exercices soumis à l'impôt sur les sociétés à la distribution ». Or 219 proposé (LEGIARTI000053542939, VI 3) prévoit que, « Pour les exercices relevant du V, les états distincts [...] au dernier alinéa du a septies du I ne sont plus joints à la déclaration de résultat », sans état de remplacement ni sanction propre à leur absence.
- **Correction.** Un dernier alinéa réserve l'état aux exercices qui ne relèvent pas du régime de distribution. Pour les autres, les éléments sont établis à partir des écritures existantes et du suivi de l'article 209, sans état ni attestation de remplacement. La loi répressive plus douce reste réservée. La dispense des lignes inchangées et la phrase de coordination IS existantes sont conservées mot pour mot, car elles portent des `proposed_quote`. La note fausse (« Le a septies du I de 219 conserve dans le corpus un état annuel ») est rectifiée.
- **Point pour l'auteur.** La suppression est comptée à 219 et n'est pas comptée une seconde fois.

**SWEEP-J15-a4-35 : annexe IV 35 (LEGIARTI000006300363), piste S9a → CGI 286, G (F1+F3).**
- **Défaut.** L'article imposait encore « les déclarations prévues aux 1° et 2° du I de l'article 286 » à chaque modification substantielle, alors que 286 proposé (LEGIARTI000054337091) porte « 2° Abrogé ; » (questionnaire professionnel sur imprimé). Son IV couvre aussi les demandes fondées sur ce seul texte.
- **Correction.** Le renvoi vise désormais la seule déclaration du 1°. Une phrase précise qu'aucun renseignement professionnel n'est exigé sur le fondement du 2° abrogé, pour les déclarations à souscrire à compter de la loi qui l'abroge. La transmission entre services et les dispenses légales sont inchangées.

## Demande à un autre groupe

- **Y15, annexe II 254 (LEGIARTI000050811261, maintenu)** : le a) impose encore de « fournir tous renseignements relatifs à son activité professionnelle conformément aux 1° et 2° du I de l'article 286 ». Le texte exact demandé figure dans `changes.json` (`requests`) : « a) De déposer une déclaration d'existence conformément au 1° du I de l'article 286 du code général des impôts ; ».

## Points pour l'auteur

- L'annexe IV 37 (LEGIARTI000006300365) parle encore de « livre spécial » prescrit par le 3° du I de 286, alors que 286 proposé ne prescrit plus qu'un « document comptable chronologique ». C'est un défaut de terminologie (m), non corrigé parce que l'article n'est pas modifié par ailleurs.
- L'annexe II 242 octies (J09) dispense encore « des déclarations prévues aux 1° et 2° du I de l'article 286 ». C'est une dispense, donc sans effet contraignant, mais elle renvoie à un 2° abrogé.
- L'annexe III 313 BQ ter (J14) renvoie aussi aux « annexes prévues à l'article 982 ». Elle figure dans le paquet de J14, qui a une correction en cours sur cet article ; je n'ai pas fait de demande.
- 286 et 289 sont en `ABROGE_DIFF`, avec reprise dans le CIBS annoncée par l'ordonnance n° 2025-1247. Les corrections portent sur le texte maintenu jusqu'à cette reprise, sans en anticiper le contenu.

## Une ligne par piste

| Article | Piste → loi | Qualification | Correction |
|---|---|---|---|
| a3 49 septies ZZY quater (LEGIARTI000046724093) | S9a/F1+F5 → 244 quater Y | faux positif | — aucune correction |
| a3 344 G septdecies (LEGIARTI000046822080) | S9a/F1+F5 → 1649 ter E | faux positif | — aucune correction |
| a3 111 H sexdecies (LEGIARTI000047114057) | S9a/F1+F5 → 302 H ter | faux positif | — aucune correction |
| a3 328 R (LEGIARTI000047278834) | S9x/F1+F5 → 1635 quater A | faux positif | — aucune correction |
| a3 328 S (LEGIARTI000047278838) | S9a/F1+F5 → 1635 quater A | faux positif | — aucune correction |
| a3 328 W (LEGIARTI000047278848) | S9a/F1+F5 → 1635 quater N | faux positif | — aucune correction |
| a3 41 DO (LEGIARTI000047480561) | S9a/F1+F5 → 156 | faux positif | — aucune correction |
| a3 96 F ter (LEGIARTI000047559578) | S9a/F1+F5 → 289 | faux positif | — aucune correction |
| a3 96 F quater (LEGIARTI000047559583) | S9a/F1+F5 → 289 | faux positif | — aucune correction |
| a3 96 F bis (LEGIARTI000047560563) | S9a/F1+F5 → 289 | faux positif | — aucune correction |
| a3 96 F (LEGIARTI000047560572) | S9a/F1+F5 → 289 | faux positif | — aucune correction |
| a3 49 septies ZZY sexies (LEGIARTI000047623629) | S9a/F1+F5 → 244 quater Y | faux positif | — aucune correction |
| a3 49 septies ZZP (LEGIARTI000047697120) | S9a/F1+F5 → 244 quater W | faux positif | — aucune correction |
| a3 49 septies ZZE (LEGIARTI000049356877) | S9a/F1+F5 → 244 quater U | faux positif | — aucune correction |
| a3 49 septies ZZB bis (LEGIARTI000049356901) | S9a/F1+F5 → 244 quater U | faux positif | — aucune correction |
| a3 49 septies ZZB (LEGIARTI000049356913) | S9a/F1+F5 → 244 quater U | faux positif | — aucune correction |
| a3 46 quater-0 ZZ bis D (LEGIARTI000049634793) | S9a/F1+F5 → 210 F | déjà réglé | — aucune correction |
| a3 313 BQ quater (LEGIARTI000049642369) | S9a/F1+F5 → 982 | G | — correction SWEEP-J15-313BQquater |
| a3 46 quater-0 RH (LEGIARTI000049642472) | S9x/F1+F5 → 219 | G | — correction SWEEP-J15-46quater0RH |
| a3 46 ter A bis (LEGIARTI000049642479) | S9x/F1+F5 → 208 | déjà réglé | — aucune correction |
| a3 41-0 A bis B (LEGIARTI000049642523) | S9a/F1+F5 → 151 octies C | faux positif | — aucune correction |
| a3 384 D (LEGIARTI000049826480) | S9x/F1+F5 → 1693 ter | déjà réglé | — aucune correction |
| a3 49 septies ZZ bis (LEGIARTI000050175598) | S9a/F1+F5 → 244 quater T | faux positif | — aucune correction |
| a3 49 septies ZZ ter (LEGIARTI000050175600) | S9a/F1+F5 → 244 quater T | faux positif | — aucune correction |
| a3 49 septies ZZ quinquies (LEGIARTI000050175604) | S9a/F1+F5 → 244 quater T | faux positif | — aucune correction |
| a3 49 septies ZZ (LEGIARTI000050175847) | S9x/F1+F5 → 244 quater T | faux positif | — aucune correction |
| a3 49 septies ZY (LEGIARTI000050175853) | S9a/F1+F5 → 244 quater T | faux positif | — aucune correction |
| a3 41 JB (LEGIARTI000050735773) | S9a/F1+F5 → 242 ter | faux positif | — aucune correction |
| a3 46 quater-0 ZZD (LEGIARTI000051762516) | S9x/F1+F5 → 223 A | faux positif | — aucune correction |
| a3 46 quater-0 S (LEGIARTI000051762566) | S9x/F1+F5 → 219 | faux positif | — aucune correction |
| a3 46 AI bis B (LEGIARTI000051762578) | S9a/F1+F5 → 1763 C | faux positif | — aucune correction |
| a3 321 E (LEGIARTI000051762675) | S9a/F1+F5 → 1499 | faux positif | — aucune correction |
| a3 96 P (LEGIARTI000051762698) | S9a/F1+F5 → 289 A | faux positif | — aucune correction |
| a3 49 septies I (LEGIARTI000051916060) | S9a/F1+F5 → 244 quater B | faux positif | — aucune correction |
| a3 46 quindecies O (LEGIARTI000052040030) | S9a/F1+F5 → 238 bis | faux positif | — aucune correction |
| a3 46 quindecies M (LEGIARTI000052040037) | S9a/F1+F5 → 238 bis | faux positif | — aucune correction |
| a3 49 septies Y (LEGIARTI000052108392) | S9a/F1+F5 → 244 quater F | faux positif | — aucune correction |
| a3 41 duovicies-0 H bis (LEGIARTI000052205035) | S9a/F1+F5 → 150 U | faux positif | — aucune correction |
| a3 344 quindecies (LEGIARTI000053173178) | S9a/F1+F5 → 1635 sexies | faux positif | — aucune correction |
| a3 2 terdecies G (LEGIARTI000054364048) | S9a/F1+F5 → 31 | faux positif | — aucune correction |
| a3 2 terdecies C (LEGIARTI000054364106) | S9a/F1+F5 → 31 | faux positif | — aucune correction |
| a3 2 terdecies B (LEGIARTI000054364125) | S9a/F1+F5 → 31 | faux positif | — aucune correction |
| a3 2 terdecies A (LEGIARTI000054364136) | S9a/F1+F5 → 31 | faux positif | — aucune correction |
| a3 2 terdecies (LEGIARTI000054364145) | S9a/F1+F5 → 31 | faux positif | — aucune correction |
| a3 111-0 B (LEGIARTI000054364291) | S9a/F1+F5 → 302 G | faux positif | — aucune correction |
| a4 4 octies (LEGIARTI000006300218) | S9a/F1+F5 → 39 bis A | faux positif | — aucune correction |
| a4 23 bis (LEGIARTI000006300292) | S9x/F1+F5 → 208 | faux positif | — aucune correction |
| a4 23 H (LEGIARTI000006300305) | S9a/F1+F5 → 223 | faux positif | — aucune correction |
| a4 23 L bis (LEGIARTI000006300312) | S9a/F1+F5 → 238 bis J | faux positif | — aucune correction |
| a4 35 (LEGIARTI000006300363) | S9a/F1+F5 → 286 | G | — correction SWEEP-J15-a4-35 |
| a4 37 (LEGIARTI000006300365) | S9a/F1+F5 → 286 | m | — aucune correction |
| a4 30 (LEGIARTI000006301296) | S9a/F1+F5 → 279 | faux positif | — aucune correction |
| a4 188 B (LEGIARTI000006301959) | S9a/F1+F5 → 1678 bis | faux positif | — aucune correction |

Les citations exactes de chaque piste figurent dans `audit/sweeps/J15.json`.

Revue IA, sans validation par un juriste.
