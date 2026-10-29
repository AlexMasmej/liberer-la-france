# J14 : quatrième balayage (S9a, S9x), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` (exports dans `evidence/cited/production-20261029/`). Le paquet `audit/sweeps/packet-J14.json` compte 53 articles de l'annexe III du CGI et 53 pistes : 47 S9a et 6 S9x. Aucun article n'a de `previous_owner`, et `apply/assignment.json` les attribue tous à J14 : je n'ai créé aucun dossier de variante.

Méthode : pour chaque piste, j'ai lu l'article d'annexe en entier (source, proposition, motif, notes). J'ai lu aussi les `removed_provisions` de la loi visée et sa proposition. Quand l'annexe renvoie à un alinéa ou à un numéro de la loi, j'ai vérifié ce renvoi dans la proposition. J'ai lu aussi CGI 119 ter (dont la version `VIGUEUR_DIFF` de 2027), 119 quater et 221 bis. Pour les grandes cibles (31, 167 bis, 244 quater X et Y, 219, 39), j'ai lu les subdivisions visées, pas le texte ligne à ligne.

Contrôle : `python3 -B apply/check_changes.py J14` donne 4 lignes construites et 4 validées, et `problems` est vide. Le diagnostic `explicit_normative_reduction` reprend seulement les `removed_provisions` existants, qui ne changent pas. Rien n'a été écrit en production. Cette revue est faite par une IA et ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9a | S9x | Total |
|---|---|---|---|
| G | 3 | 1 | 4 |
| m | 0 | 0 | 0 |
| déjà réglé | 5 | 6 | 11 |
| faux positif | 37 | 1 | 38 |

Il y a 4 corrections (mode `replace`). `requests` et `skipped` sont vides.

## Corrections appliquées

**SWEEP-J14-46QFB : 46 quater-0 FB (LEGIARTI000035302070), S9a → 182 B bis, G (F1+F3+F5).**
- **Défaut.** La déclaration vise encore « l'engagement prévu [...] au deuxième alinéa du 1 de l'article 119 quater et au 2 de l'article 182 B bis » et le représentant (h). Or 119 quater proposé (LEGIARTI000006302662) et 182 B bis proposé (LEGIARTI000039382322) suppriment, pour les paiements postérieurs à la réforme, la durée minimale, l'engagement et le représentant, et interdisent au décret de les rétablir.
- **Changement.** Les renvois à 119 quater et 182 B bis sont limités aux engagements des paiements antérieurs. Un alinéa constate que la déclaration n'est pas due pour les intérêts et redevances payés après la réforme. L'engagement des dividendes (c du 2 de 119 ter, maintenu y compris dans sa version 2027) et ses huit rubriques ne changent pas.
- **Mise à jour du dossier.** Les notes erronées sont rectifiées : selon elles, l'engagement et la responsabilité « demeurent » pour les trois articles. J'ai ajouté un effet `coordination` (measure_id `interets-associes-fin-duree-minimale`) et mis à jour `benefit_review`.

**SWEEP-J14-313BQT : 313 BQ ter (LEGIARTI000036947661), S9a → 982, G (F1+F5).**
- **Défaut.** Le texte dit : « Le redevable renseigne les annexes prévues à l'article 982 ». Or 982 proposé (LEGIARTI000036385055) dispose : « Aucune annexe détaillant ou évaluant séparément chacun de ces actifs n'est jointe ». Il ajoute que le décret « ne peut rétablir une annexe annuelle ou un relevé périodique des actifs ».
- **Changement.** Les rubriques sont portées sur la déclaration annuelle de l'article 170, « sans y joindre d'annexe et sans détailler ni évaluer séparément chacun des actifs ». La transition reprend celle de 982 : elle couvre les années antérieures et exclut tout rattrapage d'annexe. Le 2° reste abrogé. La dispense de ressaisie est maintenue.
- **Mise à jour du dossier.** La note qui attribuait à 982 « les annexes des actifs de 965 » est rectifiée. J'ai ajouté un effet `coordination` (measure_id `ifi-annexes-annuelles-suppression`).
- **Point laissé à l'auteur.** Les 3° à 5° restent des rubriques globales par catégorie. Les supprimer au profit des seules valeurs brute et nette de 982 serait un allègement supplémentaire, que le projet n'a pas décidé.

**SWEEP-J14-38Q : 38 quindecies (LEGIARTI000038668632), S9x → 54 septies, G (F1+F5).**
- **Défaut.** Le texte organise encore « L'état dont la production est prévue au I de l'article 54 septies » (« Il est souscrit tant qu'il existe [...] ») et l'état du deuxième alinéa de 221 bis. Or 54 septies proposé (LEGIARTI000044989165) dispose : « Aucun état n'est joint à la déclaration de résultat [...] sans rétablir le dépôt d'un état ni un support distinct ». 221 bis proposé (LEGIARTI000037987801) dit de même. Les notes de 54 septies demandaient déjà de coordonner 38 quindecies.
- **Changement.** Les I, II et IV décrivent désormais les renseignements conservés en comptabilité, sans dépôt, sans modèle ni support distinct. Leur contenu est inchangé (1° à 3°, trois valeurs du IV). La transition reprend celle de 54 septies III et de 221 bis : elle couvre les échéances expirées et réserve la loi répressive plus douce.
- **Mise à jour du dossier.** Les notes erronées sont rectifiées : « le registre du II demeure distinct ». J'ai ajouté deux effets `coordination` (`plus-values-suppression-etat-annuel` et `suivi-plus-values-sans-etat-distinct`).
- **Point laissé à l'auteur.** La sanction de 1763 relative à l'état de 54 septies, hors paquet, doit suivre cette suppression. Je ne l'ai pas vérifiée.

**SWEEP-J14-410BA : 41-0 bis A (LEGIARTI000043663499), S9a → 93 A, G (F1+F5+F10).**
- **Défaut.** L'article est maintenu avec la demande sur papier libre « avant le 1er février ». Or 93 A proposé (LEGIARTI000048847605) permet d'opter « notamment dans la déclaration visée à l'article 97, jusqu'à l'expiration du délai de dépôt de cette déclaration ». Les notes de 93 A demandent d'adapter les textes réglementaires. Le motif de 41-0 bis A est faux : « Le délai du 1er février est fixé par le I de 93 A lui-même ».
- **Changement.** L'article passe de maintenu à coordonné : `status` devient `rewrite_draft` et `classification` devient `coordination_only`, avec un effet `coordination` (`bnc-options-delai-declaration`). Le délai et les voies d'option sont ceux de 93 A, la demande libre restant une simple faculté. Les règles du commencement d'activité et de la renonciation sont conservées. La transition est celle de 93 A.

## Pistes une par une

| Article | LEGIARTI | Famille | Loi visée | Qualification | Correction |
|---|---|---|---|---|---|
| 38 sexdecies GB | LEGIARTI000033289604 | S9a/F1+F5 | 151 octies | faux positif | aucune correction |
| 49 septies S | LEGIARTI000034597902 | S9a/F1+F5 | 244 quater C | faux positif | aucune correction |
| 10 K | LEGIARTI000034597954 | S9a/F1+F5 | 42 septies | faux positif | aucune correction |
| 2 vicies | LEGIARTI000034597961 | S9a/F1+F5 | 31 | faux positif | aucune correction |
| 382-0 C septies | LEGIARTI000034729430 | S9a/F1+F5 | 1724 quinquies | déjà réglé | aucune correction |
| 382-0 C octies | LEGIARTI000034729432 | S9a/F1+F5 | 1681 ter | faux positif | aucune correction |
| 39 B | LEGIARTI000034737239 | S9a/F1+F5 | 87 | faux positif | aucune correction |
| 357 E | LEGIARTI000034757415 | S9a/F1+F5 | 1663 C | faux positif | aucune correction |
| 46 quater-0 FB | LEGIARTI000035302070 | S9a/F1+F5 | 182 B bis | G | corrigé (SWEEP-J14-46QFB) |
| 313 BQ ter | LEGIARTI000036947661 | S9a/F1+F5 | 982 | G | corrigé (SWEEP-J14-313BQT) |
| 313 BO | LEGIARTI000036960667 | S9a/F1+F5 | 978 | faux positif | aucune correction |
| 49 F | LEGIARTI000037100796 | S9x/F1+F5 | 242 ter | déjà réglé | aucune correction |
| 49 D | LEGIARTI000037100804 | S9a/F1+F5 | 242 ter | déjà réglé | aucune correction |
| 49 septies ZZW | LEGIARTI000038631470 | S9a/F1+F5 | 244 quater X | faux positif | aucune correction |
| 46 quater-0 ZH | LEGIARTI000038650642 | S9x/F1+F5 | 219 | déjà réglé | aucune correction |
| 46 quater-0 ZG | LEGIARTI000038650653 | S9a/F1+F5 | 223 R | faux positif | aucune correction |
| 38 quindecies | LEGIARTI000038668632 | S9x/F1+F5 | 54 septies | G | corrigé (SWEEP-J14-38Q) |
| 41 tervicies A | LEGIARTI000038950368 | S9x/F1+F5 | 167 bis | déjà réglé | aucune correction |
| 41 tervicies B | LEGIARTI000038950370 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies C | LEGIARTI000038950372 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies D | LEGIARTI000038950374 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies F | LEGIARTI000038950378 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies I | LEGIARTI000038950384 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies J | LEGIARTI000038950386 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies K | LEGIARTI000038950388 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 41 tervicies L | LEGIARTI000038950390 | S9a/F1+F5 | 167 bis | faux positif | aucune correction |
| 71 | LEGIARTI000041838654 | S9a/F1+F5 | 208 | faux positif | aucune correction |
| 406 A 12 | LEGIARTI000042160740 | S9x/F1+F5 | 1751 | déjà réglé | aucune correction |
| 41 sexdecies C | LEGIARTI000042161123 | S9a/F1+F5 | 158 | faux positif | aucune correction |
| 350 quindecies | LEGIARTI000042987126 | S9a/F1+F5 | 1960 | déjà réglé | aucune correction |
| 344 C | LEGIARTI000043164894 | S9x/F1+F5 | 1649 AA | déjà réglé | aucune correction |
| 46 quater-0 ZZ bis E | LEGIARTI000043166044 | S9a/F1+F5 | 210 F | faux positif | aucune correction |
| 46 quater-0 ZY septdecies | LEGIARTI000043537008 | S9a/F1+F5 | 220 T | faux positif | aucune correction |
| 49 septies XC | LEGIARTI000043663479 | S9a/F1+F5 | 238 bis | faux positif | aucune correction |
| 41-0 bis A | LEGIARTI000043663499 | S9a/F1+F5 | 93 A | G | corrigé (SWEEP-J14-410BA) |
| 49 septies F | LEGIARTI000043682643 | S9a/F1+F5 | 244 quater B | faux positif | aucune correction |
| 281 ter | LEGIARTI000043855509 | S9a/F1+F5 | 795 A | déjà réglé | aucune correction |
| 281 bis | LEGIARTI000043855518 | S9a/F1+F5 | 795 A | déjà réglé | aucune correction |
| 41 ZZ quinquies | LEGIARTI000043894661 | S9a/F1+F5 | 242 ter | faux positif | aucune correction |
| 38 sexies | LEGIARTI000045195248 | S9a/F1+F5 | 39 | faux positif | aucune correction |
| 49 K | LEGIARTI000045515606 | S9a/F1+F5 | 44 octies A | faux positif | aucune correction |
| 49 septies ZZY | LEGIARTI000045758300 | S9a/F1+F5 | 244 quater Y | faux positif | aucune correction |
| 49 septies ZZY bis | LEGIARTI000045758302 | S9a/F1+F5 | 244 quater Y | faux positif | aucune correction |
| 49 septies ZZY ter | LEGIARTI000045758304 | S9a/F1+F5 | 244 quater Y | faux positif | aucune correction |
| 49 septies ZZU | LEGIARTI000045759822 | S9a/F1+F5 | 244 quater X | faux positif | aucune correction |
| 49 septies ZZT | LEGIARTI000045759826 | S9x/F1+F5 | 244 quater X | faux positif | aucune correction |
| 49 P | LEGIARTI000045766159 | S9x/F1+F5 | 44 octies A | déjà réglé | aucune correction |
| 2 duodecies | LEGIARTI000045766417 | S9a/F1+F5 | 31 | faux positif | aucune correction |
| 330 | LEGIARTI000046078832 | S9a/F1+F5 | 1600 | faux positif | aucune correction |
| 85 H | LEGIARTI000046157913 | S9a/F1+F5 | 277 A | faux positif | aucune correction |
| 85 F | LEGIARTI000046157921 | S9a/F1+F5 | 277 A | faux positif | aucune correction |
| 85 D | LEGIARTI000046157943 | S9a/F1+F5 | 277 A | faux positif | aucune correction |
| 46 quater-0 YW quater | LEGIARTI000046552234 | S9a/F1+F5 | 220 Q bis | faux positif | aucune correction |

Les citations exactes de chaque piste sont dans `audit/sweeps/J14.json`.

## Résumé

Sur 53 pistes, 4 sont des défauts G, 11 sont déjà réglées et 38 sont des faux positifs. J'ai fait 4 corrections, validées sans problème. Points laissés à l'auteur :
- les rubriques par catégorie de 313 BQ ter ;
- la sanction de 1763 pour l'état supprimé de 54 septies, hors paquet.

Revue IA, sans validation par un juriste.
