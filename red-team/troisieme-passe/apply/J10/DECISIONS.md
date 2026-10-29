# Groupe J10 — décisions (quatrième balayage)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py …` et sqlite en `mode=ro`, `query_only`). Paquet : `audit/sweeps/packet-J10.json`, 53 articles de l'annexe II du CGI et 53 pistes (44 S9a, 9 S9x). Pour chaque piste, j'ai lu le texte d'application en entier (proposition, ou source s'il est maintenu, avec motif et notes), la ligne `removed_provisions` du lot de la loi visée et la proposition entière de cette loi. J'ai aussi lu 150 VI, 150 VL et 150 VM proposés, et les voisins 74 S bis, 74 S sexies et 74 S septies, ce dernier corrigé par X4 (AUDIT-K011). Les citations de `audit/sweeps/J10.json` ont été contrôlées mot pour mot, par script, contre la production. Les pièces sont exportées sous `evidence/cited/production-20261029/`.

## Bilan

- 53 pistes : 41 faux positifs, 7 déjà réglées, 1 défaut mineur (m, F10) et 4 défauts grossiers (G, F1+F5).
- 4 corrections dans `apply/J10/changes.json`, toutes en mode `replace` sur des articles de J10. Pas de `requests` ni de `skipped`. `python3 -B apply/check_changes.py J10` renvoie `problems: []`. Les diagnostics sont attendus : `explicit_normative_reduction` sur 171 AT, 74 S ter et 74 S quater, et `length_change` sur 60 B (2,79) et 171 AT (3,9), qui viennent des clauses de transition déjà présentes.
- Articles avec `previous_owner` : 57 (B06) est déjà réglé, 371 D (A8) est un faux positif. Ni l'un ni l'autre n'appelle de correction : je n'ai donc créé aucun dossier de variante (`B06jj`, `A8jj`).

## Corrections (défauts G)

1. **60 B (LEGIARTI000022179500) — appliquée.** L'objet est SWEEP-J10-S9a-60B, en coordination avec 163 quinquies C (LEGIARTI000041464278). La loi proposée exonère les produits « sans obligation de réinvestissement dans la société ni de placement sur un compte bloqué ». Elle interdit à tout règlement de rétablir ce réinvestissement. Le I, 2° du décret imposait pourtant encore d'informer la société « des modalités qu'il retient pour le réinvestissement ». Ce qui change : le 2° est abrogé à son emplacement, l'exemple « instructions de réinvestissement » est retiré de la dispense, et une transition immédiate est alignée sur le IV de 163 quinquies C. Les notes inexactes sont rectifiées. Il n'y a aucune formalité de remplacement. Le classement reste `coordination_only` : l'effet est ajouté avec le `measure_id` de la loi (`capital-risque-fin-remploi-distributions`) et n'est pas compté deux fois.
2. **171 AT (LEGIARTI000027799302) — appliquée.** L'objet est SWEEP-J10-S9a-171AT, avec le même défaut pour les FCPR et FPCI au regard de 163 quinquies B (LEGIARTI000027795200), II, 2°, et V. Ce qui change : l'information sur les modalités de réinvestissement est supprimée, avec une transition immédiate. Le motif, les notes et le `benefit_review`, qui tenaient le réinvestissement pour maintenu, sont rectifiés. Une ligne s'ajoute à `removed_provisions`, avec un effet `coordination` (même `measure_id`). La citation `proposed_quote` de l'effet existant est mise à jour, puisque « engagements et modalités » devient « engagements ».
3. **74 S ter (LEGIARTI000029101329) — appliquée.** L'objet est SWEEP-J10-S9a-74Ster, au regard de 150 VI III (LEGIARTI000043140066) et de 150 VJ 5° (LEGIARTI000028429032). Pour une exportation sans cession, la loi proposée exclut « paiement, … déclaration, option ou justification ». Le décret exigeait pourtant encore de tout exportateur la justification de son domicile et un document d'origine du bien, lors des formalités douanières. Ce qui change : le dispositif est borné aux exportations réalisées avant l'entrée en vigueur du III de 150 VI, et aucune justification n'est demandée pour les suivantes. La rédaction suit celle de 74 S septies (X4, AUDIT-K011). Les lettres a à d et la liberté de preuve restent intactes pour les exportations anciennes.
4. **74 S quater (LEGIARTI000029101326) — appliquée.** L'objet est SWEEP-J10-S9a-74Squater. Ce qui change : la mention de l'exportateur et la production des justificatifs en douane (« En cas d'exportation, ils sont produits auprès du service des douanes ») sont bornées aux exportations antérieures. La décharge de l'intermédiaire ou de l'acquéreur pour les cessions et la preuve libre ne changent pas.

Ces corrections ne recréent aucune formalité, aucun impôt ni aucune sanction. Elles n'étendent aucune faveur. Les droits et les régimes des opérations antérieures sont conservés.

## Points laissés à l'auteur

- Les blocs `reference_checks` et `reference_coherence` de 60 B et de 171 AT gardent, dans leur texte d'évaluation, l'ancienne lecture du réinvestissement (« choix du mode de réinvestissement », « réinvestissement immédiat avec indisponibilité »). Je ne les ai pas modifiés : ils sont scellés par des empreintes et le changement de `proposed_xml` impose de toute façon leur recertification par l'outil du coordinateur.
- 310 N (LEGIARTI000029919486), défaut m (F10) : les notes disent la coordination de 1501 « non effectuée ici », alors que 1501 proposé retire la majoration. Je ne l'ai pas corrigé, faute de modifier l'article par ailleurs (BRIEF-SWEEP, point 4).
- 74 S sexies (Y15) : la rubrique b, « en cas d'exportation », et la valeur en douane restent dans le texte maintenu. Y15 l'a jugé faux positif, au motif que 150 VM I 2° garde les cessions de biens exportés temporairement. Je ne demande rien, mais une lecture coordonnée avec 74 S ter, 74 S quater et 74 S septies serait utile.

## Une ligne par piste

| # | Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|---|
| 1 | 371 bis I (LEGIARTI000022006313) | S9a/F1+F5 | cgi 158 (LEGIARTI000054373673) | déjà réglé | non |
| 2 | 242-0 P (LEGIARTI000022146964) | S9a/F1+F5 | cgi 262 (LEGIARTI000033469152) | faux positif | non |
| 3 | 17 (LEGIARTI000022147119) | S9a/F1+F5 | cgi 39 bis A (LEGIARTI000051217524) | faux positif | non |
| 4 | 60 B (LEGIARTI000022179500) | S9a/F1+F5 | cgi 163 quinquies C (LEGIARTI000041464278) | G | oui |
| 5 | 201 quater (LEGIARTI000022816450) | S9a/F1+F5 | cgi 260 (LEGIARTI000025576729) | faux positif | non |
| 6 | 245 (LEGIARTI000022816542) | S9a/F1+F5 | cgi 270 (LEGIARTI000042910192) | faux positif | non |
| 7 | 201 quinquies (LEGIARTI000022816617) | S9x/F1+F5 | cgi 260 A (LEGIARTI000006304259) | déjà réglé | non |
| 8 | 310 G ter (LEGIARTI000024045380) | S9a/F1+F5 | cgi 1378 octies (LEGIARTI000049531775) | faux positif | non |
| 9 | 310 G quater (LEGIARTI000024045441) | S9x/F1+F5 | cgi 1378 octies (LEGIARTI000049531775) | faux positif | non |
| 10 | 310 G quinquies (LEGIARTI000024045456) | S9x/F1+F5 | cgi 1378 octies (LEGIARTI000049531775) | faux positif | non |
| 11 | 171 AU (LEGIARTI000024446675) | S9a/F1+F5 | cgi 163 quinquies B (LEGIARTI000027795200) | faux positif | non |
| 12 | 171 AV (LEGIARTI000024446687) | S9a/F1+F5 | cgi 163 quinquies B (LEGIARTI000027795200) | faux positif | non |
| 13 | 95 ZA (LEGIARTI000025077249) | S9x/F1+F5 | cgi 170 ter (LEGIARTI000024189377) | faux positif | non |
| 14 | 95 ZC (LEGIARTI000025077255) | S9a/F1+F5 | cgi 170 ter (LEGIARTI000024189377) | faux positif | non |
| 15 | 95 ZD (LEGIARTI000025077257) | S9x/F1+F5 | cgi 170 ter (LEGIARTI000024189377) | faux positif | non |
| 16 | 95 ZF (LEGIARTI000025077263) | S9a/F1+F5 | cgi 170 ter (LEGIARTI000024189377) | faux positif | non |
| 17 | 242-0 L (LEGIARTI000025393306) | S9a/F1+F5 | cgi 1693 ter (LEGIARTI000053189147) | faux positif | non |
| 18 | 57 (LEGIARTI000025622239) | S9a/F1+F5 | cgi 242 ter (LEGIARTI000047622843) | déjà réglé | non |
| 19 | 382 bis (LEGIARTI000025712501) | S9a/F1+F5 | cgi 1691 bis (LEGIARTI000051219480) | faux positif | non |
| 20 | 382 quinquies (LEGIARTI000025712508) | S9a/F1+F5 | cgi 1691 bis (LEGIARTI000051219480) | faux positif | non |
| 21 | 95 ZB (LEGIARTI000025886907) | S9a/F1+F5 | cgi 170 ter (LEGIARTI000024189377) | faux positif | non |
| 22 | 286 H (LEGIARTI000026407222) | S9a/F1+F5 | cgi 302 G (LEGIARTI000050085168) | faux positif | non |
| 23 | 242 nonies (LEGIARTI000027356472) | S9a/F1+F5 | cgi 289 (LEGIARTI000048827413) | faux positif | non |
| 24 | 310 HB quater (LEGIARTI000027518856) | S9a/F1+F5 | cgi 1465 (LEGIARTI000048846734) | faux positif | non |
| 25 | 286 N (LEGIARTI000027518861) | S9a/F1+F5 | cgi 302 G (LEGIARTI000050085168) | faux positif | non |
| 26 | 171 AT (LEGIARTI000027799302) | S9a/F1+F5 | cgi 163 quinquies B (LEGIARTI000027795200) | G | oui |
| 27 | 210 (LEGIARTI000028505608) | S9a/F1+F5 | cgi 298 (LEGIARTI000044873424) | faux positif | non |
| 28 | 74 S quinquies (LEGIARTI000029101323) | S9a/F1+F5 | cgi 150 VK (LEGIARTI000036428328) | faux positif | non |
| 29 | 74 S quater (LEGIARTI000029101326) | S9a/F1+F5 | cgi 150 VJ (LEGIARTI000028429032) | G | oui |
| 30 | 74 S ter (LEGIARTI000029101329) | S9a/F1+F5 | cgi 150 VJ (LEGIARTI000028429032) | G | oui |
| 31 | 310 N (LEGIARTI000029919486) | S9a/F1+F5 | cgi 1501 (LEGIARTI000036364459) | m | non |
| 32 | 242-0 O (LEGIARTI000030091379) | S9a/F1+F5 | cgi 262 (LEGIARTI000033469152) | faux positif | non |
| 33 | 370 C (LEGIARTI000030420804) | S9x/F1+F5 | cgi 1649 ter (LEGIARTI000028440192) | déjà réglé | non |
| 34 | 91 ter A (LEGIARTI000032702448) | S9a/F1+F5 | cgi 163 bis G (LEGIARTI000053543883) | faux positif | non |
| 35 | 286 K (LEGIARTI000032881394) | S9a/F1+F5 | cgi 302 G (LEGIARTI000050085168) | faux positif | non |
| 36 | 408 (LEGIARTI000033051360) | S9a/F1+F5 | cgi 1691 bis (LEGIARTI000051219480) | faux positif | non |
| 37 | 371 Y (LEGIARTI000033238525) | S9a/F1+F5 | cgi 99 (LEGIARTI000053546818) | faux positif | non |
| 38 | 371 QA (LEGIARTI000033238558) | S9a/F1+F5 | cgi 102 ter (LEGIARTI000054373747) | faux positif | non |
| 39 | 371 D (LEGIARTI000033238650) | S9a/F1+F5 | cgi 1750 (LEGIARTI000024041640) | faux positif | non |
| 40 | 371 bis L (LEGIARTI000033238711) | S9a/F1+F5 | cgi 158 (LEGIARTI000054373673) | déjà réglé | non |
| 41 | 371 bis A (LEGIARTI000033238768) | S9a/F1+F5 | cgi 158 (LEGIARTI000054373673) | faux positif | non |
| 42 | 371 E (LEGIARTI000033240703) | S9x/F1+F5 | cgi 39 (LEGIARTI000053542680) | faux positif | non |
| 43 | 371 Q (LEGIARTI000033240761) | S9x/F1+F5 | cgi 39 (LEGIARTI000053542680) | faux positif | non |
| 44 | 301 C (LEGIARTI000034588634) | S9x/F1+F5 | cgi 145 (LEGIARTI000051203497) | faux positif | non |
| 45 | 310-00 H ter (LEGIARTI000034597689) | S9a/F1+F5 | cgi 1395 B bis (LEGIARTI000053543368) | faux positif | non |
| 46 | 310-00 H bis (LEGIARTI000034597697) | S9a/F1+F5 | cgi 1395 B bis (LEGIARTI000053543368) | faux positif | non |
| 47 | 310-00 H (LEGIARTI000034597707) | S9a/F1+F5 | cgi 1395 B bis (LEGIARTI000053543368) | faux positif | non |
| 48 | 384 A (LEGIARTI000037273446) | S9a/F1+F5 | cgi 982 (LEGIARTI000036385055) | faux positif | non |
| 49 | 171 BL (LEGIARTI000038668435) | S9a/F1+F5 | cgi 242 septies (LEGIARTI000042912633) | faux positif | non |
| 50 | 46 (LEGIARTI000038668480) | S9a/F1+F5 | cgi 109 (LEGIARTI000006302651) | déjà réglé | non |
| 51 | 294 quater (LEGIARTI000038702053) | S9a/F1+F5 | cgi 787 C (LEGIARTI000053542704) | déjà réglé | non |
| 52 | 74-0 J (LEGIARTI000041589970) | S9a/F1+F5 | cgi 242 ter (LEGIARTI000047622843) | faux positif | non |
| 53 | 371 ter S (LEGIARTI000042160490) | S9a/F1+F5 | cgi 1504 (LEGIARTI000041471065) | faux positif | non |

Revue IA : rien de ceci ne vaut validation par un juriste.
