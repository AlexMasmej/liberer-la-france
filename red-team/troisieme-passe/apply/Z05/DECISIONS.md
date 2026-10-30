# Z05 : sixième balayage (S16b, S18, S19a, S19b), code de la construction et de l'habitation

Texte lu en production le 30 octobre 2026, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, base ouverte en `mode=ro`).

Le paquet compte 42 entrées, soit 41 articles et 44 pistes. Résultat :
- **1 G**, corrigé ;
- 25 pistes déjà réglées ;
- 18 faux positifs.

Deux remarques m (F10, notes inexactes) restent sur des articles non modifiés. Aucun dossier de variante n'a été créé : les quatre articles qui ont un `previous_owner` (L421-7, L831-1, L441-1 et L441-2-8) n'ont aucun défaut à corriger. Une request est adressée à B02.

## Correction appliquée

| Article (LEGIARTI) | Piste | Qualification | Décision |
|---|---|---|---|
| L181-11 (…46120784, maintenu) | S18 → L152-3 | **G** F2+F5 | **Corrigé** (mode `replace`, l'article passe de maintenu à réécrit). Voir le détail ci-dessous. |

Détail de la correction de L181-11 :
- **Le défaut.** Le projet abroge L152-3 (comptage de l'eau froide), « y compris pour les constructions en cours ». L181-11 citait encore L152-3 parmi les obligations dont le manquement donne lieu au rapport. Ce rapport ouvre la mise en demeure de L181-12 et les sanctions administratives de L181-13, dont une amende pouvant atteindre 100 000 €. La liste pénale de L183-4 avait déjà été coordonnée (W12), mais pas cette liste administrative.
- **Ce qui change.** « L. 152-3, » est retiré de la liste. Un alinéa final est ajouté : après l'abrogation, aucun rapport, aucune mise en demeure ni aucune mesure de L181-12 ou L181-13 ne peut se fonder sur la seule méconnaissance de cette obligation. Les manquements antérieurs restent régis par les règles anciennes, sous réserve de la loi répressive plus douce.
- **Ce qui reste.** La copie du rapport, le délai d'observations d'au moins un mois et la graphie « L 171-4 » sont inchangés.
- **Contrôle.** Le bilan `substantive_impact` est classé `coordination_only`. Le validateur ne signale aucun problème. Son diagnostic `references_changed` (L181-12 et L181-13 ajoutés) est voulu.

## Request

- **B02, L181-11, version de 2028 (LEGIARTI000047475243, `VIGUEUR_DIFF`, sans proposition).** Cette version conserve L. 152-3. La request demande la même coordination en mode `new` : retirer L. 152-3, garder L. 171-5 et ajouter l'alinéa de transition. Le texte complet est fourni dans `changes.json`. Le précédent est L183-4 2028 (W12).

## Pistes sans correction

| Article (LEGIARTI) | Piste | Qualification | Motif |
|---|---|---|---|
| L242-4 (…6824539) | S18 L213-2 | faux positif | Dispense transitoire de 1972, favorable. |
| L421-7 (…6825599, B08) | S18 L423-1 | déjà réglé | Le renvoi est limité aux dissolutions antérieures (RT-P1-CCH-12). |
| L442-10 (…6825760) | S18 L441-3 | déjà réglé | Le renvoi est borné aux périodes antérieures à la suppression du SLS. |
| R281-1 (…6896641) | S18 R211-6 | faux positif | Simple plage d'applicabilité territoriale. |
| R315-77 (…6897047) | S16b L315-20 | déjà réglé | R315-69 rattache déjà toute la sous-section aux articles L315-19 à L315-32 abrogés en 2011 (loi n° 2011-525, art. 180), dans leur rédaction antérieure, pour les seuls comptes ouverts avant 1959. **m F10** : les notes disent L315-20 « absent du corpus », ce qui est inexact. |
| R431-16 (…6899468) | S18 R431-14 | déjà réglé | R431-14 est retiré des causes d'exigibilité. Il n'est plus cité que pour neutraliser. |
| L423-1-2 (…37668094) | S18 L443-14 | faux positif | Exclusion favorable d'une notification abrogée, sans formalité. |
| L621-2 (…37669855) | S18 L621-5 et L621-6 | faux positif (2 pistes) | Clause d'interdiction de rétablissement. |
| L442-12 (…37669889) | S18 L441-4 | déjà réglé | Renvoi borné aux périodes anciennes. |
| L831-1 (…38814882, B08) | S18 L831-2 | déjà réglé | Réserves bornées aux mois antérieurs (RT-P1-CCH-10). |
| L823-1 (…38814920) | S18 L822-8 | faux positif | Le 2° vise désormais L822-5 à L822-7. L822-8 n'est cité que pour interdire le rétablissement. |
| L441-9 (…38833818) | S18 L441-8 | déjà réglé | La liquidation provisoire est réservée aux périodes anciennes. |
| D842-15, D842-6, D832-24, D832-10, D823-16 | S18 L823-7 | déjà réglé (5 pistes) | Le non-versement est borné aux mois antérieurs (AUDIT3-Q242). |
| R823-6 (…41419232) | S18 L823-7 | déjà réglé | Même coordination. |
| R824-17 (…38878837) | S19a R824-16 | faux positif | R824-17 prend fin au 1er janvier 2027, comme la version de R824-16 qu'il vise. Il ne coexiste jamais avec la version de 2027. |
| R481-8-2 (…38928774) | S18 R443-19 | déjà réglé | Le renvoi est retiré. Seule la transition le mentionne encore. |
| R212-18 (…39041938) | S18 R212-6 | déjà réglé | Application bornée à l'abrogation. |
| R432-2 (…39043118) | S18 R431-14 | déjà réglé | Le renvoi est retiré. La seule mention restante interdit le rétablissement. |
| R423-28 (…39043157) | S16b L421-14 | déjà réglé | Le texte dit déjà que le renvoi à L421-14, abrogé en 2015, « ne fonde aucune sanction nouvelle ». **m F10** : les notes disent le texte de L421-14 « manquant », alors qu'il est au corpus. |
| R431-9 (…39048806) | S18 R431-14 | déjà réglé | R431-14 est exclu de la plage. La seule mention restante interdit le rétablissement. |
| R423-89 (…39050141) | S18 D423-77 | faux positif | Clause d'interdiction, cohérente avec D423-77 abrogé. |
| L452-3 (…41466661) | S18 L452-4-1 | déjà réglé | Cotisations bornées aux années antérieures. |
| L443-15-2-3 et L443-15-2-2 | S18 L443-14 | déjà réglé (2 pistes) | Exclusion acquise pour les décisions antérieures. |
| L121-5, R171-31, L441-2-9, L122-14 | S18 | faux positif (4 pistes) | Clauses d'interdiction de rétablissement. |
| R126-14-1 (…43827676) | S18 R126-14 | faux positif | Renvoi de neutralisation (« n'est pas exigée »). |
| L441-2-3 (…45211734) | S18 L302-9-1 | déjà réglé | Le IX écarte toute imputation fondée sur un arrêté de carence. |
| D312-27 (…46589732) | S18 D312-19 | déjà réglé | Seules restent les contributions nées avant l'abrogation. |
| D862-7 et D861-8 | S18 D842-12 | déjà réglé (2 pistes) | Dispense bornée aux mois antérieurs, sans plancher rétabli. |
| L441-2-8 (…53546117, B04) | S18 L441-2-5 | faux positif | Clause d'interdiction. |
| L441-1 (…54354341, B08) | S18 L441-2-5 et L302-9-1-2 | faux positif (2 pistes) | Renvoi historique et clause d'interdiction. |
| R862-3 et R863-9, versions de 2027 | S19b | faux positif (2 pistes) | Voir le détail ci-dessous. |

Détail des pistes S19b (R862-3 et R863-9, versions de 2027) :
- Ces versions adaptent les versions de 2027 de R824-13 à R824-16, issues du décret n° 2026-84. Aucune de ces versions n'a de proposition.
- Les réécritures du projet portent sur les versions de 2019 de R824-13 et R824-16. Elles excluent toute prorogation au-delà du 1er janvier 2027.
- La commission de médiation de L441-2-3 II est maintenue par le projet.
- Aucune réforme n'est donc écrasée.

## Points pour l'auteur

- **Hors piste.** Le 5° de L181-13 (LEGIARTI000046120795, maintenu) vise encore « l'agrément des personnes ou organismes visés à l'article L. 122-12 ». Or le projet supprime cet agrément. Ce point n'a pas été corrigé : l'article est hors paquet.
- **Chapitre R824 après 2027.** Toutes les versions de 2027 du chapitre R824 sont sans proposition. Il n'a pas été vérifié ici si la refonte réglementaire de 2027 reprend les allègements que le projet avait apportés aux versions de 2019.

Revue IA, sans validation par un juriste.
