# Audit indépendant Travail — édition 001

Quatre propositions correctives entières sont prêtes dans `answer.json`. Elles ne sont ni enregistrées ni publiées. Aucun fichier de politique, moteur, lot actif ou source canonique n’a été modifié par cet audit.

## Corrections proposées

| Article | Constat | Correction entière proposée |
| --- | --- | --- |
| R1221-41 | La proposition intégrée exige encore une mise en demeure « conformément à L1221-5-1 », alors que la seconde passe législative permet la saisine directe. | Retirer ce préalable et tout délai d’attente associé ; maintenir les échéances de remise, la demande amiable facultative et la réserve des décisions définitives. Aligner la transition sur les actions nouvelles et instances en cours de L1221-5-1. |
| R1221-34 | Le 7° annonce une interdiction de renouvellement du « contrat nouveau », au lieu de l’essai. | Viser expressément le non-renouvellement de la période d’essai. Maintenir les 14 rubriques et leurs numéros ; rétablir le renvoi de rémunération L3221-3 et expliciter au 10° le préavis, son calcul et les dispenses. Aucun écrit supplémentaire. |
| L1226-4 | « Quinze jours à compter de la notification » ne reprend pas le décompte au lendemain expressément retenu dans L1234-3. | Clarifier le même point de départ et la fin du quinzième jour, même non travaillé. Conserver la reprise du salaire après un mois, le préavis non exécuté non indemnisé dans ce cas spécial, le seuil à la fin effective et les contrats antérieurs. |
| L1226-14 | Même ambiguïté de décompte dans l’inaptitude professionnelle. | Renvoyer au décompte de L1234-3 sans changer le préavis payé, le salaire spécial de L1226-16, l’absence de seuil pour l’indemnité spéciale, le doublement et les transitions. |

Les deux premiers sont des défauts rédactionnels constatés. Les deux derniers sécurisent une ambiguïté de coordination ; l’audit n’affirme pas qu’un juge aurait déjà donné à ces propositions une interprétation contraire. Les articles complets gardent leurs autres dispositions, notamment les contreparties favorables et les droits antérieurs. Les raisons, réserves et revues d’avantages propres à chaque article figurent dans `answer.json`.

## Capture et gardes

La première capture en lecture seule du 20 octobre 2026 à 00:02 UTC porte sur 407 propositions déjà intégrées parmi 517 identités Travail ciblées :218 articles des paquets de la réforme et 299 candidats prioritaires. Les 230 articles du volet initial comprennent aussi 12 articles hors Code du travail ; ces 12 ne sont pas réaudités ici.

Les sources officielles intégrales, notes d’application et avant-images sont conservées dans `audit-source.snapshot.json`. `source.json` contient les quatre articles correctifs avec leur proposition antérieure entière, son empreinte et le lien à la source officielle. Les captures complémentaires de cibles sont dans `reference-targets.snapshot.json` et `dependency-sources.snapshot.json`.

`verify.py` ouvre SQLite avec `mode=ro` et une transaction de lecture. Il vérifie ensemble les quatre articles et 27 dépendances : corps source et empreinte officielle, notes d’application exactes, absence ou présence du draft et totalité de ses cinq champs (source, statut, proposition, raison, réserves). Une proposition apparue sur une cible jusque-là non réécrite invalide également la capture. La politique active est comparée à l’empreinte capturée. Le script n’écrit que `validation.json` dans ce dossier.

La dernière vérification avant remise a passé les contrôles de schéma et d’article entier et trouvé zéro garde en échec. Six tests hors réseau couvrent une proposition concurrente, un changement de sens sans changement de corps, des notes officielles modifiées, l’apparition d’une proposition sur une dépendance, une source modifiée et une avant-image corrompue. Ces contrôles ne constituent aucune validation juridique.

Avant inscription, le parent doit **rejouer la comparaison sous le verrou partagé du registre**, à partir des mêmes `source.json`, `answer.json` et dépendances. Un résultat antérieur de `validation.json` ne dispense pas de ce contrôle. Toute modification d’une cible ou d’un correctif concurrent doit bloquer l’inscription jusqu’à comparaison humaine et nouvelle capture. L’audit n’a appelé aucun registre, aucun modèle et aucun service externe.

## Couverture et limites

Les nombres exacts et les identités sont dans `coverage-summary.json` et `coverage.json`. **124 articles sources et leurs notes ont été lus intégralement ;113 avaient une proposition également lue intégralement.** Onze cibles de référence n’avaient pas encore de proposition. Une proposition lue, L1233-67, appartenait à un job actif : elle ne reçoit aucune conclusion et n’est pas corrigée par ce paquet.

Parmi les 407 propositions de la capture initiale, 105 ont reçu une relecture complète hors concurrence ; 302 restent sans conclusion de cet audit. Les autres lectures documentées comprennent des textes de référence supplémentaires.

Les douze réouvertures initiales ont été lues intégralement : L1221-1, L1221-5-1, L1222-15, L1223-5 à 9, L1225-1, L1225-6, L1225-34 et L1225-38. Aucun autre conflit certain n’y a été identifié dans les axes de cet audit. Cette conclusion locale ne certifie ni tous leurs effets juridiques ni la chaîne entière.

Les contrôles ont porté sur :

- Le noyau de l’essai, du préavis et du barème : quinze jours, seuil d’un an au terme effectif, ancienneté totale et prorata,0,20 mois par an, plafond de six mois et initiative employeur ; séparation des créances de salaire/congés, réparations et indemnités spéciales.
- Les inaptitudes et leurs renvois structurés : les 1° à 3° de L1226-12 existent dans la proposition ; le doublement de L1226-14 porte sur le montant plafonné avant doublement, avec salaire propre de L1226-16. Le seuil ordinaire ne supprime pas les minima spéciaux.
- L’intérim : L1251-58-4/5 écartent des faux positifs. L1251-28 et son ancien préavis d’un jour par semaine ne s’appliquent pas aux missions en CDI intérimaire/contrat unique ; les substitutions de « contrat de mission » en « lettre de mission » conservent l’emploi. Le deuxième alinéa de L1251-26 vise toujours les éléments essentiels repris par L1251-34. Les 1° à 5° de L1251-6 sont stables. Les garanties d’intermission restent dans L1251-58-2/3.
- L’apprentissage, la mobilité et les aides : phase pédagogique distincte de l’emploi ; signatures et médiation du mineur conservées ; anciens 45 jours et 5+7 jours réservés aux contrats antérieurs selon leurs notes ; dispenses favorables ouvertes aux situations futures. Les références à des articles non encore réécrits restent signalées comme telles.
- L’aménagement du temps de travail : L3121-41/44 gardent 35 heures moyennes et 1607 heures ; l’information de R1221-34 ne porte pas ces seuils à 40 heures.

La capture a exclu conservativement douze cibles déjà attribuées à une revue active. Les dossiers confirmés par le parent étaient `travail-00038`, `travail-00039` et `review-travail-LEGIARTI000006900996-00003` ; leurs sources sont aussi conservées par le coordinateur. Les lots actifs peuvent évoluer : la vérification de concurrence doit être refaite avant toute inscription. Aucun correctif de ce paquet ne leur est attribué à la dernière vérification.

Les 407 propositions capturées n’ont **pas** toutes été lues intégralement. Le repérage automatique des autres références n’est pas compté comme revue. Les textes hors Travail, les sources non encore réécrites, les évolutions ultérieures des workers et les renvois externes ne sont pas certifiés. Les textes légaux officiels restent la référence documentaire ; les propositions restent un travail d’auteur non adopté et non validé par un juriste.

## Vérification reproductible

```sh
python 3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/edition001/test_guards.py
python 3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/edition001/verify.py
```

`author.py` ne fait qu’écrire les quatre propositions entières dans ce dossier. Il ne faut pas le relancer pour écraser une modification ultérieure du parent ; les empreintes et la revue du correctif doivent précéder toute intégration.
