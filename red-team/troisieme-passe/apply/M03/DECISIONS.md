# M03 : décisions (cinquième balayage)

J'ai lu le texte en production avec `CITE_PRODUCTION=1 python3 -I tools/cite.py`, et la base en `mode=ro`. Rien n'a été écrit en production. Revue IA, sans validation par un juriste.

## Ce que contient le paquet

Le paquet compte 22 articles et 26 pistes, toutes dans le code de la construction et de l'habitation. Deux articles n'ont pas de `previous_owner` : R313-20-3 et R311-29. Ils appartiennent à M03 et ne demandent aucune correction, donc `apply/M03/changes.json` est vide (deux entrées `skipped` « déjà réglé »).

Les quatre corrections G portent sur des articles d'autres groupes. Elles sont dans deux variantes, validées toutes les deux (`problems` vide) :
- `apply/W11mc/` : R315-69, R318-27 et D331-104 ;
- `apply/Y10mc/` : R365-1.

## Une ligne par piste

| Piste | Article | Groupe | Qualification | Correction |
|---|---|---|---|---|
| S17 (S12/F4) vers L651-3 | L651-9, LEGIARTI000006825960 | J06 | m (F10, notes seulement) | Non |
| S17 (S8/F3) vers L315-32 | R315-69, LEGIARTI000006897038 | W11 | **G** (F3) | Oui, W11mc (SWEEP-M03-R315-69) |
| S17 (S8/F3) vers L315-26 | R315-69 | W11 | **G** (F3) | Oui, même correction |
| S17 (S8/F3) vers L315-19 | R315-69 | W11 | **G** (F3), même défaut | Oui, même correction |
| S17 (S8/F3) vers L315-25 | R315-72, LEGIARTI000006897041 | W11 | **G** (F3) | Oui, par la clause de sous-section de R315-69 |
| S17 (S8/F3) vers L315-21 | R315-73, LEGIARTI000006897042 | W11 | **G** (F3) | Oui, par la clause de R315-69 |
| S17 (S8/F3) vers L315-21 | R315-75, LEGIARTI000006897045 | W11 | **G** (F3) | Oui, par la clause de R315-69 |
| S17 (S8/F3) vers R318-3 | R318-27, LEGIARTI000006897137 | W11 | **G** (F3) | Oui, W11mc (SWEEP-M03-R318-27) |
| S17 (S9) vers L365-3 | R441-9-1, LEGIARTI000021617546 | Y09 | m (F5 rédactionnel) | Non |
| S17 (S7/F3) vers L411-8-1 | L411-8, LEGIARTI000028808988 | W11 | m (redondance, F10) | Non |
| S16/F3 vers L322-1 | R313-20-3, LEGIARTI000028809604 | **M03** | faux positif (CASF) | Non |
| S17 (S4/F4) | R824-11, LEGIARTI000038878851 | B02 | déjà réglé (RT-FUTTL-11) | Non |
| S17 (S4/F4) | R824-9, LEGIARTI000038878857 | B02 | déjà réglé (RT-FUTTL-11) | Non |
| S16/F3 vers L311-9 | R311-29, LEGIARTI000039042667 | **M03** | déjà réglé (ancrage historique) | Non |
| S17 (S8/F3) vers R353-165-4 | D331-104, LEGIARTI000039048258 | W11 | **G** (F3) | Oui, W11mc (SWEEP-M03-D331-104) |
| S17 (S8/F3) vers R381-5 | R365-1, LEGIARTI000039048439 | Y10 | **G** (F3) | Oui, Y10mc (SWEEP-M03-R365-1) |
| S17 (S10/F5) vers L126-35-4 | L126-35-2, LEGIARTI000043966759 | Y11 | m (F5 sans effet) | Non |
| S17 (S1) vers L443-14 | Annexe I à R423-86, LEGIARTI000045646952 | Y11 | m | Non |
| S17 (S1) vers L443-14 | Annexe II à R423-86, LEGIARTI000045646995 | Y11 | m | Non |
| S16/F3 vers L322-1 | R321-12, LEGIARTI000048685289 | Y12 | faux positif (CASF) | Non |
| S16/F3 vers L351-8 | R861-5, LEGIARTI000050811209 | W12 | faux positif (CSS) | Non |
| S17 (S12/F4) vers R824-1 | Annexe I à D353-90, LEGIARTI000051283462 | Y12 | m (mot « abrogation ») | Non |
| S17 (S12/F4) vers R824-4 | Annexe I à D353-90 | Y12 | m | Non |
| S17 (S12/F4) vers R824-4 | Annexe II à D353-90, LEGIARTI000053356309 | Y12 | m | Non |
| S17 (S12/F4) vers R824-4 | Annexe 1 au III de R353-159, LEGIARTI000053561433 | Y12 | m | Non |
| S17 (S12/F4) vers R824-7 | Annexe 1 au III de R353-159 | Y12 | m | Non |

## Corrections appliquées

- **R315-69 (épargne-construction), dans W11mc.**
  - **Défaut :** l'article est maintenu tel quel, mais ses renvois structurants visent « les articles L. 315-19 à L. 315-32 » et « l'article L. 315-26 ». Ces articles ont été abrogés le 19 mai 2011 par l'article 180 de la loi n° 2011-525, sans successeur. Les notes les disaient à tort absents du corpus.
  - **Requalification :** W11 l'avait jugé m. Avec le critère de l'audit 5 (renvois morts structurants, comme A932-4-1), c'est un G.
  - **Ce que j'ai changé :** j'ai ajouté un dernier alinéa. Il rattache les références de la sous-section à leur rédaction antérieure à l'abrogation et aux seuls comptes ouverts jusqu'au 4 février 1959, sans remettre ces articles en vigueur et sans modifier les droits attachés aux comptes. Les trois alinéas de la source sont inchangés. Le statut passe de `retained_unchanged` à `rewrite_draft`, avec un bilan `coordination_only`.
  - **Effet sur les autres articles :** la clause vaut pour toute la « Sous-section 2 : Epargne-construction ». Elle règle donc aussi R315-72 4° (L315-25), R315-73 1° et R315-75 (L315-21), sans toucher à ces articles.
- **R318-27 (avances outre-mer), dans W11mc.**
  - **Défaut :** l'article n'adapte que R. 318-3, abrogé le 6 août 2010 par le décret n° 2010-912, sans successeur. Il est donc entièrement inopérant, alors que le motif le dit nécessaire.
  - **Ce que j'ai changé :** l'article est rattaché à la rédaction antérieure de R. 318-3, pour les seules « avances remboursables auxquelles cet article demeure applicable ». Une phrase précise qu'il n'impose aucune condition aux autres avances. Les normes et les deux exceptions sont conservées. Bilan `coordination_only`.
- **D331-104, dans W11mc.**
  - **Défaut :** le contrat de location annexé doit préciser la composition du loyer « selon les postes de dépense définis à l'article R. 353-165-4 ». Cet article a été abrogé le 2 avril 2011 (décret n° 2011-356), sans successeur, et le renvoi vise des conventions futures.
  - **Ce que j'ai changé :** seul le renvoi est supprimé (« qui précise le montant du loyer et sa composition. »). Le motif, les notes et le bilan d'impact sont rectifiés, avec un effet `coordination` ajouté. La réduction antérieure (lettre des financeurs) est inchangée.
- **R365-1, f du 1°, dans Y10mc.**
  - **Défaut :** l'activité agréée renvoie à « l'article R. 381-5 ». Cet article a été transféré à D381-5 en 2019, puis abrogé le 28 septembre 2022 (décret n° 2022-1257, art. 3).
  - **Ce que j'ai changé :** le renvoi vise D. 381-5 « dans sa rédaction antérieure à son abrogation ». La condition n'est pas supprimée, car cela élargirait l'agrément, et l'activité n'est pas retirée. Notes et bilan rectifiés.

Aucune de ces corrections ne crée de formalité, de sanction, de condition ou de prélèvement. Aucune ne retire un droit ou une faveur.

## Pistes non corrigées

- **Défauts m :** notes erronées, dérogations redondantes, mot « abrogation » inexact dans les annexes de D353-90 et de R353-159, et dispenses de L443-14 devenues sans objet. Ils ne sont pas corrigés, parce que les articles ne sont pas modifiés par ailleurs.
- **Faux positifs S16 :** « du même code » désigne le CASF pour R313-20-3 et R321-12, et le CSS pour R861-5.

## Points laissés à l'auteur

- Abroger la sous-section épargne-construction (R315-69 et suivants) et R318-27, s'il est établi qu'aucun compte ni aucune avance ne subsiste. Les pièces ne permettent pas de l'établir : les accords CDC et les dispositions transitoires du décret n° 2010-912 manquent.
- Les notes erronées (F10) de R315-72, R315-73, R315-75, L651-9, L411-8 et R311-29 ne sont pas rectifiées.
- R365-1 3° a : le décalage du « onzième alinéa de l'article L. 422-2 » préexiste dans la source (m, relevé par Y10).
- L126-35-2 : la mention « l'attestation de cette transmission demeurent régies par l'article L. 126-35-10 » est lisible mais maladroite, puisque L126-35-10 ne l'exige plus.

## Résumé

- **26 pistes :** 9 G, 11 m, 3 faux positifs et 3 déjà réglées.
- **4 articles corrigés :** ils couvrent les 9 G, dans deux variantes (W11mc, Y10mc).
- **0 correction sur M03** et aucune `request`.

Revue IA, sans validation par un juriste.
