# Réparation ciblée et reprise supervisée — 23 octobre 2026

## Modification appliquée

Seul run_exhaustive.py a été remplacé, du baseline 1c66699… au candidat
e950a288939012b1915f180a7cc80987b5e79452e08eab7b9a4cd4a4f7a3a0db.
Le candidat avait passé 105 tests isolés. Son ajout de classification des
diagnostics natifs terminaux retire le faux signal provenant de « quota » dans
le texte juridique ; les refus d'accès explicites et les trois tentatives
bornées restent actifs. Aucun validateur, politique, source, article, limite
ou modèle global n'a été changé par l'installation.

## Exclusion et réconciliation fraîches

3122 et ses descendants étaient réellement absents, avec un reçu exit=0,
STOP=true dû au faux classement, postérieur au dernier constat vivant lié au
lstart converti. Les cinq publications existantes avaient abouti. Aucune
nouvelle publication, aucun signal ni lancement de coordinateur par ce contrôle.

La réconciliation a été rejouée sous verrous superviseur, coordinateur,
rédacteur et réservations manuelles, après la fin des travaux actifs. Aucun de
ces verrous n'a été tenu pendant leur attente. Les 30 317 identités des neuf
recueils et les dispositions des 795 absences ont été relues en SQLite ro.
Les 1 413 lots possédant 29 518 lignes concordent avec les sept champs en base,
les sources/NOTA/versions conservées et le registre. Les quatre propositions
canoniques sans propriétaire de lot et les quatre hors inventaire courant
restent sous leurs gardes historiques exactes, sans ajout à la couverture.

700 intentions durables correspondent à 15 473 lignes actuelles et à leurs
reçus ; aucune intention partiellement enregistrée ou ambiguë n'a été admise.
Les 493 archives ont été contrôlées, avec 2 766 lignes courantes de révision
ayant leurs avant-images. Quatorze marqueurs prior_proposal_sha256=null sont
des premières rédactions avec absence antérieure capturée, et non des secondes
passes indépendantes. Quatre lignes ont seulement eu leurs métadonnées de
renvois remplacées par une opération historique documentée : source, réponse,
capture, approbation, helper, reçu et empreintes exactes des fichiers propriétaires
ont été confrontés. Cette classification préserve les contrôles et ne crée
aucune nouvelle approbation juridique.

Le premier essai d'extension de ce contrôle avait refusé ces cas historiques
par manque de correspondance exacte dans la seule archive radical-review.
La vérification a ensuite été complétée par les captures de première rédaction
et le reçu de recertification sous empreintes ; aucune ligne canonique et
aucune garde du pipeline n'a été modifiée pour résoudre ce refus.

La file immuable de 3122 est entièrement partitionnée : 89 nouveaux lots =
85 terminaux et quatre non admis ; 505 lots de relecture = 12 terminaux et 493
non admis. Leurs identités et sources assignées concordent, zéro lot inconnu.
L'ancien zéro de queue ne constitue donc pas une preuve d'achèvement.

## Relance et attestations

L'intention d'installation, le baseline et les octets possédés de la pause ont
été conservés avant le remplacement atomique. Le hash installé et tous les
autres pins ont été relus. Seule notre pause a été retirée, sous comparaison
exacte des octets et du propriétaire. La supervision existante a lancé 39614,
puis l'a adopté seul. Les six places new et une place review demeurent.

La file reconstruite contient exactement les 792 identités accessibles : les
696 de travaux non acceptés et les 96 non tentées. Les 5 054 anciennes
relectures sont dans la nouvelle file, dont les 58 des travaux non acceptés.
Les réponses natives distinctes Astra/Moyen ont été retrouvées pour six
rédacteurs et un relecteur. Les nouvelles acceptations doivent être vérifiées
séparément ; la simple admission et un en-tête ne prouvent pas une acceptation.

## Travail restant

L'inventaire des renvois reste explicitement ouvert : 3 470 certificats périmés
et 1 092 absents dans le périmètre du catalogue courant, 606 courants. Ce ne sont
pas 4 562 erreurs juridiques établies, ni les signalements P1 de l'audit global.
Aucun de ces travaux n'a été transformé en validation fraîche.

La réallocation future a été rebasée hors ligne sur le correctif, avec 35 tests
ciblés et 74 régressions réussis. Le paquet d'origine reste scellé et intact,
son ancien baseline désormais incompatible n'est pas forcé. Aucun des six
modules n'est installé et le transfert reste NOT_READY_FOR_ACTIVATION.
Les cinq blocages du contrôleur ne sont pas déclarés levés.

Le stockage reste sous le seuil d'un nouvel audit volumineux ; aucune capture
de base n'a été réalisée et l'audit validé 222551Z reste intact. Aucune mesure
de gain ni clôture à 100 % n'est déduite de cette réparation technique.
