# Lot social — édition 001 figée

24 articles actuels du Code de la sécurité sociale appartiennent à l’export courant de 7 427 entrées, dans le périmètre global des 30 317 entrées. Les corps et notes représentent 29 129 caractères. Ils ont été capturés dans une transaction SQLite `mode=ro BEGIN`, avec documents DILA complets et empreintes du document, du corps, des notes et des avant-images. Aucun des 24 n’avait de proposition à la capture ou au dernier contrôle.

Le paquet contient **quatre allègements**, **une coordination** et **dix-neuf maintiens intégraux justifiés**. Les maintiens ont `proposed_xml: null` : leur texte source sera reproduit en entier, sans prétendre à une réécriture ou à une économie.

| Article | Effet matériel proposé |
| --- | --- |
| L242-14 | Retirer la notification autonome des attributions d’actions et le paiement de toutes les cotisations attaché à son seul défaut, sans retirer les conditions de fond de l’exclusion. |
| R133-44 | Retirer le second avis obligatoire sous huit jours par le mandataire aux clients que l’organisme notifie déjà. Garder fraude, contradictoire, recours et restitution des pièces sous un mois. |
| R242-3 | Retirer le modèle ministériel et les transmissions répétées de données de plafond légalement disponibles. Garder les informations réellement manquantes, les échéances résiduelles, les personnes ayant travaillé, le prorata, les restitutions et le règlement des désaccords. |
| D242-2-2 | Retirer la copie imposée du document salarié et les doubles envois lorsque l’employeur a effectivement reçu les deux montants utiles. Garder les deux échéances au choix et la contribution libératoire favorable. |
| R133-13 | Coordonner l’événement de fin d’emploi avec le contrat unique ; la fin d’une mission ne rompt pas le contrat. Toutes les autres divisions sont conservées, dont les événements de santé et le certificat purement technique. Aucune seconde mesure d’allègement comptée. |

Le candidat R243-29 a été écarté de la réécriture : son information « au moins une fois par an » n’imposait pas un relevé annuel distinct. Des décomptes mensuels complets peuvent déjà satisfaire cette obligation. Lui attribuer une coupe aurait été un surcompte ; il est conservé intégralement. R133-14-2 est également conservé : la loi impose encore la correction au déclarant, et le délai contradictoire ne doit pas être effacé par une simple réécriture réglementaire.

L242-1-4 reste intégral : contribution de 20 % au-delà de la franchise annuelle de 15 % du SMIC mensuel, jusqu’à 1,5 SMIC mensuel par an, cotisations ordinaires au-dessus, exceptions intragroupe et fraude. Aucune abrogation d’un autre régime de contribution à 20 % n’est importée. Les exonérations, alternatives de plafond, remboursements et situations futures éligibles sont préservés. Le maintien de L242-10 n’affirme pas qu’une extension de l’abattement à l’intérim soit impossible ; aucune extension non instruite ou droit à retraite fictivement constant n’est inventé ici.

## Preuves et limites

- `source.json` et `answer.json` sont figés ; les sources, notes, avant-images et politiques restent à vérifier sous le verrou d’inscription.
- `dependencies.json` capture 45 textes cibles complets, notes et propositions. Le rapport de garde ne prétend pas certifier toute leur chaîne de renvois ni le droit extérieur aux cinq codes.
- `validation.json` constate la validation locale des 24 lignes et l’absence de dérive des 69 vues au contrôle du 20 octobre 2026 à 07:03:38 UTC. Aucune dérive des deux politiques ; aucun chevauchement avec une source graphique réservée.
- Un ancien artefact de job `securite-sociale-00045` contient sept sources du lot et un `result.json`. Cela ne démontre pas un travail actif ni une inscription : aucune de ces sept propositions n’est dans la base au contrôle. Le parent a réservé les 24 et signalé que CLI3 relit le Travail ; vérifier l’allocation juste avant inscription.
- Les ouvertures web des trois sources centrales sur Légifrance ont retourné 403. Aucun contournement : les preuves reposent sur les documents primaires DILA locaux, avec empreinte du document XML vérifiée. Pas de confrontation visuelle au Journal officiel revendiquée.
- Les certificats d’impact attestent des citations exactes et des empreintes. Ils ne sont ni un audit indépendant des effets ni une validation de juriste. La contrelecture indépendante du parent et de l’agent fiscal reste nécessaire.
- Aucun impôt nouveau, aucune obligation d’inscription ni déclaration de remplacement. Aucun chiffrage d’économie nationale ; effet net global inconnu. Les quatre clés de mesure servent à dédupliquer les seuls effets décrits.
- Aucun enregistrement, aucune modification de base, politique, module actif, lot actif ou site ; aucune publication.

## Empreintes des fichiers figés

- source.json : `677ac463515ab8a0c7fef9d1549f3ef0aa4b3cb1102a257d69cfa5107c79d74b`
- answer.json : `2ab169896f9d32a9f251f3526e19c251b5dd4809b1f98755eda2d59655a1439f`
- dependencies.json : `11d9722a1f09ba410af52242e9be810d452af8138e9eb5e5fccaeabc57541f63`
