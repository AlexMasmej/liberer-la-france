# M07 : cinquième balayage (S1c, S2c, S8c, S17), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` (exports dans `evidence/cited/production-20261029/`) et SQLite en `mode=ro`. Les lignes de lot de production ont été lues sans modification. Le paquet `audit/sweeps/packet-M07.json` compte 46 articles et 64 pistes : 30 S1c, 27 S8c, 3 S2c et 5 S17. Elles portent sur l'annexe III, l'annexe IV et le CGI.

**Méthode.** Pour chaque piste, j'ai lu l'article entier : source, proposition ou source maintenue, motif et notes. J'ai lu ensuite chaque article visé, avec toutes ses versions et la proposition de la version en vigueur, et le texte qui l'abroge quand il figure dans le XML LEGI.

**Critère pour S8c.** Il faut distinguer deux situations :
- **Base vraiment éteinte.** L'article cesse d'organiser le régime pour l'avenir.
- **Article recodifié au CIBS** (ordonnances n° 2021-1843 et n° 2023-1210), qui est hors corpus. Neutraliser le renvoi pourrait retirer une compétence ou une faveur reprise par le CIBS. Ces pistes sont qualifiées `m` (réserve documentaire), sans correction ni cible inventée.

**Contrôle.**
- `python3 -B apply/check_changes.py M07` : 2 lignes construites et validées, `problems` vide, aucun diagnostic.
- Variantes `apply/J15mg/`, `apply/Y18mg/`, `apply/B10mg/`, `apply/A7mg/`, `apply/J16mg/`, `apply/B05mg/` et `apply/A8mg/` : toutes vides, car aucun G sur les articles de ces groupes. Chacune est validée, avec `problems` vide.

Rien n'a été écrit en production. Revue IA : ce n'est pas une validation par un juriste.

## Bilan

| Qualification | S1c | S2c | S8c | S17 | Total |
|---|---|---|---|---|---|
| G | 4 | 0 | 1 | 0 | 5 |
| m | 2 | 0 | 14 | 5 | 21 |
| déjà réglé | 18 | 1 | 1 | 0 | 20 |
| faux positif | 8 | 2 | 8 | 0 | 18 |

Il y a 2 corrections, une `replace` et une `new`. Les 5 G se ramènent à 2 défauts. Il n'y a aucune demande à un autre groupe. Deux pistes `m` sont notées `skipped` (« hors corpus »).

## Corrections

**SWEEP-M07-350quater : annexe III 350 quater (LEGIARTI000051821306), piste S8c → CGI 1562, G (F3+F7).**
- **Défaut.**
  - Le projet lit « 1° Aux articles 306, 321, 412, 450, 454, au 1 de l'article 1562 et à l'article 1565 septies ».
  - La source porte « 1562 (1) ». Ce « (1) » est l'appel de la note LEGI de 2015 (LEGIARTI000030695690) : « la référence [1562] devient sans objet, modification effectuée en conséquence de la loi n° 2014-1654 du 29 décembre 2014 ».
  - L'article 1562 est abrogé depuis le 1er janvier 2015 (LEGIARTI000006306322).
  - Le projet a donc créé un renvoi à une subdivision « 1 » d'un article mort.
- **Correction.**
  - Le 1° du I devient : « 1° Aux articles 306, 321, 412, 450, 454 et 1565 septies du code général des impôts ; ».
  - Le reste est inchangé, y compris le II 3°, qui porte le `proposed_quote` du bilan d'impact.
  - La note fausse « CGI 306, 321, … manquent comme sources du corpus fourni » est rectifiée : la note donne désormais leurs dates et textes d'abrogation, et la concordance CIBS reste ouverte.
- **Déjà vu ?** Non (registre et audits sans mention).

**SWEEP-M07-344-0B-doublon : annexe III 344-0 B, version LEGIARTI000053189893 (VIGUEUR_DIFF), pistes S1c → 1586 octies, 235 ter X, 1599 quater C, 300 bis, G (F4+F1).**
- **Défaut.**
  - LEGI publie deux versions de 344-0 B : LEGIARTI000053189893 (VIGUEUR_DIFF) et LEGIARTI000053732969 (VIGUEUR, proposition de Y18).
  - Les deux ont les mêmes bornes (31 mars 2026 → 2999), une source identique mot pour mot et la même note (ordonnance n° 2025-1247).
  - La version VIGUEUR_DIFF est hors inventaire et n'a pas de proposition. Elle maintient donc sans borne les déclarations de CVAE (6°), de taxe sur les excédents de provisions (8°), de taxe sur les surfaces de stationnement (15°) et de TIRUERT (21°), que la proposition de la version en vigueur limite aux périodes résiduelles.
- **Correction (mode `new`).**
  - La proposition actuelle de LEGIARTI000053732969 est reprise mot pour mot.
  - Le bilan `coordination_only` reprend les mêmes identifiants de mesure, pour éviter tout double compte.
  - Le motif et les notes expliquent le doublon.
- **Point pour l'auteur.** Version à inscrire à l'inventaire. Toute modification future de l'une des deux versions doit être reportée sur l'autre. C'est l'un des deux seuls doublons VIGUEUR/VIGUEUR_DIFF de même date du corpus ; l'autre est CGI 1649 bis C, hors paquet.

## Non corrigé (m, hors corpus)

- **Annexe IV 50 duodecies A (LEGIARTI000006301349) → CGI 297.**
  - L'article 297 (taux corses de TVA) est abrogé au 1er septembre 2026, et la disposition qui lui succède est hors corpus.
  - Abroger ou figer la liste retirerait le taux réduit des matériels agricoles, une faveur.
  - La note « 297 absent du fichier » est fausse (F10).
  - La réforme de l'« affectation permanente » reste à coordonner avec la disposition qui succède à 297.
- **Annexe III 350 quinquies 8° (LEGIARTI000054364269) → CGI 571.** L'article 571 est abrogé au 1er juillet 2025 (ordonnance n° 2023-1210) et recodifié hors corpus. Une neutralisation pourrait retirer une compétence reprise par le CIBS.
- **Autres renvois S8c recodifiés.** Ils sont qualifiés `m`, sans correction :
  - 350 quater : 306, 444, 570, 625 et 1565 septies ;
  - 50 septies : 402 bis et 520 A ;
  - 50-00 E : 407 ;
  - 50-00 C : 403 ;
  - 50-00 G : 438, 302 D et 302 M ter.

  Ce sont des renvois de compétence, de définition ou de faveur, que les notes signalent déjà comme concordance CIBS à établir.

## Une ligne par piste

| Article (LEGIARTI) | Piste → cible | Qualification | Correction |
|---|---|---|---|
| a3 46 AGG bis (051762600) | S8c → 199 decies | faux positif : « 199 decies Edu » = 199 decies E, en vigueur ; 6e et 7e phrases toujours exactes | non |
| a3 350 quater (051821306) | S1c → 568 | déjà réglé (II 3° neutralise le droit de licence) | non |
| a3 350 quater | S8c → 1562 | **G** F3+F7 (« au 1 de l'article 1562 » créé par le projet) | **oui** |
| a3 350 quater | S8c → 306, 1565 septies, 444, 570, 625 | m F3 (recodification, réserve documentaire) ; note rectifiée | non |
| a3 406 terdecies (052589631) | S1c → 234 nonies, 568 | faux positif (comptable seulement ; « dans les seuls champs et périodes demeurant imposables », V) | non |
| a3 406 terdecies | S1c → 235 ter ZD, 1586 ter | déjà réglé (bornes expresses) | non |
| a3 344 quindecies (053173178, J15) | S1c → 1586 ter | déjà réglé (b sans effet pour les années supprimées) | J15mg vide |
| a3 344-0 B (053189893, doublon) | S1c → 1586 octies, 235 ter X, 1599 quater C, 300 bis | **G** F4+F1 (version sans proposition) | **oui** (new) |
| a3 46 AI quinquies-0 B (053527526) | S1c → 199 | faux positif (199 terdecies-0 A bis) | non |
| a3 46 AI quinquies (053534626) | S1c → 199 | faux positif (199 terdecies-0 A) | non |
| a3 344-0 B (053732969, Y18) | S17 → 990 F | m F5 maintenu (clause finale « désigne seulement le service destinataire ») | Y18mg vide |
| a3 350 quinquies (054364269) | S8c → 571 | m F3+F10 (recodification ; skipped hors corpus) | non |
| a4 37 (006300365, J15) | S17 → 286 | m F5 maintenu (terminologie « livre spécial ») | J15mg vide |
| a4 41 ter (006300371, Y18) | S17 → 286 quater | m F5 maintenu (« registre spécial », contenu seulement) | Y18mg vide |
| a4 50, 50 bis, 49 (006300401, 006300402, 043592523, B10) | S1c → 276 | déjà réglé (RT-P1-CGI-A-07) | B10mg vide |
| a4 56 AB (006300607) | S8c → 575 | déjà réglé (renvoi retiré) | non |
| a4 50 duodecies A (006301349) | S8c → 297 | m F3+F10 (faveur ; skipped hors corpus) | non |
| a4 50 septies (020786757) | S8c → 402 bis, 520 A | m F3 (définition de franchise, recodification) | non |
| a4 155-0 bis (025089740) | S1c → 1599 quater A | faux positif (définitions utiles aux années antérieures) | non |
| a4 155-0 ter, 155-00 ter (026203815, 026203819) | S1c → 1599 quater A bis | m F10 (fond sain ; notes muettes sur l'abrogation) | non |
| a4 50 sexies B (026203838, A7) | S1c → 290 quater | déjà réglé (V, RT-P1-CGI-C-06) | A7mg vide |
| a4 50-00 E (032694360) | S8c → 407 | m F3 (faculté de support, recodification) | non |
| a4 50-00 C (032694368) | S8c → 403 | m F3 (rubrique rhums DOM, recodification) | non |
| a4 190, 191, 192, 192 bis (049639947, 041438607, 041438609, 041455751 ; J16/Y18) | S1c → 293 A ter | déjà réglé (283 bis seul ; clause 293 A ter) | J16mg, Y18mg vides |
| a4 18 bis (041963475, J16) | S17 → 200 quater | m F10 maintenu (notes seules) | J16mg vide |
| a4 50 duodecies A bis (045866114, Y18) | S1c → 300 bis | déjà réglé (numéro recyclé figé et exclu) | Y18mg vide |
| a4 50-00 G (051821545) | S8c → 438, 302 D, 302 M ter | m F3 (accises recodifiées) | non |
| a4 216 (053356214) | S1c → 1912 | faux positif (frais nés d'actes antérieurs) | non |
| a4 155 bis A (053702677) | S1c → 1641 | faux positif (barème 2025, 1641 abrogé pour l'avenir) | non |
| a4 121 sexies, 56 AJ (054359512, 054359557 ; B05) | S1c → 1519, 568 | déjà réglé (RT-P1-CGI-B-05, B-04) | B05mg vide |
| a4 41 septies A (054606058, J16) | S1c → 289 E | faux positif (date de suppression seulement) | J16mg vide |
| a4 41 septies A | S17 → 289 | m F5 maintenu (point d'audit d'une plateforme facultative) | J16mg vide |
| a4 41 septies G (054606169) | S1c → 290 A, 289 E | déjà réglé (renvoi figé ; aucune transmission) | non |
| a4 41 septies K (054606200, A8) | S1c → 290 | déjà réglé (RT-P1-ANNEXES-01) | A8mg vide |
| cgi 238 bis B, 1057 (006303975, 006305828) | S8c → 9 | faux positif (loi de 1954, ordonnance de 1945) | non |
| cgi 332, 524 (006305011, 006309990) | S8c → 315, 535 | faux positif (articles ABROGE_DIFF hors inventaire) | non |
| cgi 1078 (006305860) | S8c → 84 | faux positif (loi du 31 mars 1903) | non |
| cgi 150 A bis (006307388) | S8c → 160 | faux positif (régime de report historique) | non |
| cgi 1761 (006313055) | S2c → 244 bis A, 150 VI | faux positif (amende assise sur les droits éludés) | non |
| cgi 1788 B (006313865) | S2c → 286 quater | déjà réglé (amende alignée, loi plus douce) | non |
| cgi 298 sexdecies B (018035961) | S8c → 348 | faux positif (articles de la directive 2006/112) | non |

## Requalification S17

Aucune des 5 pistes S17 ne devient G :
- 344-0 B 10° et 41 ter n'imposent rien au-delà de la loi : une clause générale ou la loi visée prévaut.
- 37 ne pose qu'un problème de terminologie.
- 41 septies A ne fixe qu'un point d'audit pour une plateforme facultative.
- 18 bis n'a que des notes fausses (F10).

## Résumé

64 pistes : 5 G (2 défauts), 21 m, 20 déjà réglés, 18 faux positifs. 2 corrections : 350 quater en `replace`, le doublon 344-0 B en `new`. 7 dossiers de variante vides et validés : J15mg, Y18mg, B10mg, A7mg, J16mg, B05mg, A8mg. Pour l'auteur : la concordance CIBS des annexes d'accises et de 297 (Corse), et l'inscription du doublon 344-0 B à l'inventaire. Revue IA, sans validation par un juriste.
