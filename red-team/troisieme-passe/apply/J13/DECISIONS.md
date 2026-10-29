# J13 : quatrième balayage (S9x, S9a), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro`. Les exports sont dans `evidence/cited/production-20261029/` : les 53 articles de l'annexe III du paquet et leurs 34 cibles du CGI. Le paquet `audit/sweeps/packet-J13.json` compte 53 articles de l'annexe III et 53 pistes : 8 S9x et 45 S9a.

Méthode : pour chaque piste, j'ai lu l'article d'annexe en entier (source, proposition ou maintien, motif, notes, ligne de lot). J'ai lu les `removed_provisions` et la proposition de la loi visée, en entier ou dans les passages en cause pour les longs articles (39, 219, 31, 158, 277 A, 289). J'ai ensuite vérifié si le texte d'application organise encore ce qui a été retiré, ou s'il le vise seulement pour l'ancien régime.

Contrôle : `python3 -B apply/check_changes.py J13` donne 1 ligne construite et validée, et `problems` est vide. Le seul diagnostic est `explicit_normative_reduction` : il liste les deux `removed_provisions`, dont celle que j'ai ajoutée. C'est voulu.

Rien n'a été écrit en production. Cette revue est faite par une IA et ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9x | S9a | Total |
|---|---|---|---|
| G | 0 | 1 | 1 |
| m | 0 | 1 | 1 |
| déjà réglé | 6 | 5 | 11 |
| faux positif | 2 | 38 | 40 |

Il y a une correction, sur 41 V bis, et une demande au groupe Y18. Rien n'est écarté (`skipped` vide).

41 X (LEGIARTI000027799345) appartient à A8 (`previous_owner`). Sa piste est un faux positif. Je n'ai donc créé aucun dossier `apply/A8jm/`, puisqu'il n'y avait rien à y valider.

## Correction appliquée

**SWEEP-J13-41VBIS : annexe III 41 V bis (LEGIARTI000030975293), piste S9a vers 163 bis G, G (F1), appliquée (mode `replace`).**
- **Défaut.** 163 bis G proposé (LEGIARTI000053543883) supprime la majoration de 30 % pour moins de trois ans d'activité. Il dit : « Le régime prévu au premier alinéa s'applique quelle que soit la durée de l'activité ou du mandat du bénéficiaire ». Cela vaut pour les bons attribués depuis le 1er janvier 2026 et pour les faits générateurs postérieurs à la réforme. Ses notes ajoutent que les déclarations réglementaires doivent cesser de demander « les seules durées devenues inutiles ».
- **Ce que l'annexe garde.** Le f de l'état individuel exige encore, pour tous les bons, « la date depuis laquelle le bénéficiaire exerce son activité dans la société ou, s'il n'y exerce plus son activité, la date de son départ et son ancienneté ». Cette mention ne servait qu'à la majoration supprimée.
- **Changement.** Le f ne vaut plus que pour les bons attribués avant le 1er janvier 2026 et pour ceux exercés avant l'entrée en vigueur de la réforme, dont la cession peut encore relever de la majoration. Pour les autres bons, une phrase dit que la mention n'est pas exigée.
- **Transition.** Elle s'applique aux états délivrés après l'entrée en vigueur. Les états déjà délivrés ne sont pas refaits et aucune information de remplacement n'est demandée.
- **Ce qui ne change pas.** Les a à e, l'attestation de conformité, les 2° et 3° et la dispense de conservation déjà acquise restent tels quels.
- **Mise à jour du dossier.** Le motif et les notes sont complétés, avec la phrase de troisième passe. La phrase des notes « a à f [...] restent entières », devenue fausse, est corrigée (F10). J'ai ajouté une entrée à `removed_provisions` et un effet à `substantive_impact`, avec des citations exactes de la source et de la nouvelle proposition. L'outil recalcule le certificat.
- **Alignement.** La correction enlève une contrainte. Elle ne crée aucune formalité, conserve le régime ancien et ne fait aucun choix politique nouveau.

## Demande à un autre groupe

**Y18, annexe III article 39 (LEGIARTI000053218832), 2°, k.** Le k impose de déclarer « la durée d'exercice de l'activité du bénéficiaire dans la société » pour les BSPCE. C'est le même défaut. La demande, à texte exact dans `requests`, limite cette donnée aux bons attribués avant 2026 ou exercés avant la réforme.

## Défaut `m`, non corrigé

**322 G (LEGIARTI000026348001), piste S9a vers 1465 (F5, à confirmer).**
- **Piste.** Le dépôt annuel retiré de 1465 n'est pas repris par 322 G. La piste elle-même est donc sans objet.
- **Contradiction.** 322 G proposé ouvre une voie fondée sur les seuls emplois : « le respect d'une voie fondée sur les emplois dispense du montant minimal national d'investissement ». Or 1465 proposé (LEGIARTI000048846734, sans groupe) ne prévoit que des conditions « tenant compte notamment soit du volume des investissements et du nombre des emplois créés, soit du seul volume des investissements ». Les notes de 322 G le reconnaissent.
- **Portée limitée.** Sans agrément, l'exonération porte seulement sur l'augmentation des bases issue des immobilisations nouvelles, et le mot « notamment » laisse une marge.
- **Point pour l'auteur.** Si l'auteur veut conserver la voie « emplois », il faut compléter le deuxième alinéa de 1465. Il s'agit d'une extension de faveur que l'auteur doit décider. J12 traite 322 I et 322 L sur la même cible.

## Pistes déjà réglées (11)

- 46 quater-0 ZZ bis B (208 C) ;
- 255, 256 et 253 (860) ;
- 49 septies WB (244 quater E) ;
- 46 quater-0 ZJ (219) ;
- 96 I (289) ;
- 346 A (1650 A) ;
- 344 G nonies (990 I bis) ;
- 46 quater-0 ZM et ZE (223 A).

Le détail et les citations sont dans `audit/sweeps/J13.json`.

F10 non corrigé : les notes de 46 quater-0 ZM disent encore que « Le 2 de 46 quater-0 ZD encore annuel dans le corpus doit être coordonné ». Or 46 quater-0 ZD proposé (Y17) ne demande plus de liste annuelle.

## Faux positifs (40)

Dans tous ces cas, le texte d'application n'organise pas ce que la loi a retiré. Il a une fonction propre : méthode de calcul, définition, ordre d'imputation, composition ou quorum de commission, état de suivi utile, condition de fond.
- **Avec mots partagés (S9x).** 46 AG quaterdecies et 46 AG quindecies : les « mentions de 289 » et le « taux du 3° du 1 de 39 » visent des règles maintenues.
- **Autres (S9a) :**
  - ZY sexies ;
  - 315 sexdecies et 322 R ;
  - 2 E, 41 DA, 85 K, 85 J et 85 G ;
  - ZZF, ZZI, 73 I, 75, 350 A ;
  - 346 B, 346, 345, 49 quinquies ;
  - 41 duovicies-0 H, 96 I bis, 96 G ;
  - 41 X, 41 sexdecies J et H ;
  - 111-0 C, 2 quindecies C ;
  - 49 septies P, T, YT et YQ ;
  - ZZO, ZZM, ZZL, ZF, ZY duodecies ;
  - 39-0 A ;
  - 38 sexdecies OD, OB et O.

## Limites

- **Réserve documentaire.** Les arrêtés et modèles d'application (formulaires d'état BSPCE, 2042-C-PRO, arrêtés douaniers) sont hors corpus.
- **Non vérifié.** La concordance avec le CIBS au 1er janvier 2027 (277 A, 289, 262).

Revue IA : rien de ceci ne vaut validation par un juriste.
