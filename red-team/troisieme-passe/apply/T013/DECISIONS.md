# T013 — lecture systématique, palier A (CGI 150 U à 151 septies A : plus-values immobilières, taxe sur les objets précieux, plus-values professionnelles)

J'ai lu les 15 articles du paquet en production (lecture seule), le 30 octobre 2026. Bilan : 2 G, 2 m et 11 sans défaut. Le détail par article est dans `audit/tier-a/T013.json`.

## TA-T013-01 : 150 VG, renvoi figé à 150 VM — **appliquée** (`apply/T013/`, 150 VG LEGIARTI000027978330)

- **Défaut** (F4, F3) : le 3° du I renvoyait aux délais de 150 VM « dans sa rédaction en vigueur avant le 1er janvier 2027 », parce que le projet croyait que 150 VM était abrogé à cette date. En réalité, 150 VM est remplacé (RT-FUTFISC-23 : version LEGIARTI000053154469, ordonnance n° 2025-1247). Après 2027, la déclaration de plus-value serait donc restée liée aux anciens calendriers des a à c (annexe à la déclaration de l'article 287), que l'ordonnance a remplacés.
- **Correction** :
  - le renvoi d'origine, « dans les délais prévus au 1° du I de l'article 150 VM », est rétabli ;
  - au IV, la phrase qui présentait comme maintenus les refus pour défaut de paiement de 150 VH, supprimés par la proposition de 150 VH, renvoie maintenant simplement à 150 VH ;
  - le motif, les notes et l'étude d'impact (`assessment`, `scope_limitations`, effet 2 `after`) sont rectifiés.
- **Ce qui ne change pas** : aucun délai, aucune formalité et aucune sanction n'est créé. Les deux réductions (modèle facultatif, fin du veto documentaire) sont inchangées.
- **Contrôle** : `check_changes.py T013`, `problems` vide.

## TA-T013-02 : 150 VH bis et annexe III 41 duovicies J et K — **demandes** (T095)

- **Défaut** (F1, F5) : 150 VH bis proposé supprime l'annexe qui détaille chaque cession de crypto-actifs et toute déclaration des cessions exonérées. Il interdit aussi au décret de les rétablir, même par l'intermédiaire des personnes interposées. Pourtant :
  - 41 duovicies J proposé organise toujours cette annexe cession par cession et la déclaration des cessions exonérées (III). Son motif affirme même que la loi exige encore ces données ;
  - 41 duovicies K fait reprendre ce détail par la personne interposée.
- **Demandes à T095**, propriétaire de J et K, avec le texte complet :
  - **J** : le montant global est porté sur la déclaration 170, sans annexe par cession ni déclaration des cessions exonérées. La quote-part reçue d'une personne interposée est retenue. Les justificatifs restent fournis sur demande, dans le délai de trente jours de la source. Transition alignée sur le VII de 150 VH bis.
  - **K** : la personne interposée déclare, sur support libre, le résultat global et sa répartition entre associés, sans détail de chaque cession.
  - Aucun registre ni document de remplacement.
- 150 VH bis n'est pas modifié. Il n'y a donc pas de dossier de variante B10.

## Défauts m non corrigés (articles non modifiés)

- **150 VH** : les notes affirment que 150 VG garde les refus pour absence de déclaration ou de mentions. La proposition de 150 VG les supprime.
- **150 VK** : « sous leur responsabilité » ne renvoie plus qu'au seul vendeur (reliquat grammatical).
- **Hors paquet** : l'annexe II 74 S sexies (maintenue) mentionne encore l'exportation et la valeur en douane. C'est sans effet, puisqu'aucune déclaration n'est due pour une exportation nouvelle.
- **Tension à signaler à l'auteur** : l'annexe II 74 SJ subordonne encore l'enregistrement aux mentions de prix. 150 VG supprime le veto, mais seulement pour ses propres mentions. Je n'ai pas fait de correction : c'est un choix assumé du lot 74 SJ.

## Points pour l'auteur

Aucun arbitrage politique n'est ouvert. Les faveurs déjà décidées par le projet sont conservées sans extension :
- 151 ter : plafond de soixante jours supprimé ;
- 151 sexies et 151 septies : cinq ans supprimés ;
- 150 U et 150 VE : remploi, gabarit et quota SRU supprimés.

Revue IA, sans validation par un juriste.
