# Recherche documentaire des lacunes graphiques — 20 octobre 2026

Résultat borné : aucune des neuf lacunes n’est levée par cette passe. Aucun article, formule ou modèle CERFA n’est inventé, aucune proposition n’est enregistrée et aucun registre de pièces jointes actif n’est modifié.

Les neuf corps sources, notes et documents ARTICLE DILA complets ont été capturés en lecture seule dans `source-snapshot.json`. Les neuf contrôles finaux confirment l’égalité des corps, empreintes source, XML ARTICLE et propositions avec cette capture. Les notes sont également protégées par le XML ARTICLE entier. Les 45 contrôles passent. L’inventaire distingue treize marqueurs de quatorze éléments, car le marqueur fiscal de l’article 15 désigne deux CERFA.

## Nouvelle pièce primaire récupérée et effectivement vérifiée

Le Bulletin officiel des impôts n° 39 du 30 mars 2012, instruction du 27 mars 2012, référence 4 A-6-12, a été téléchargé sur le site public officiel du ministère :

https://www11.minefi.gouv.fr/boi/boi2012/4fepub/textes/4a612/4a612.pdf

Le fichier complet de 49 pages est conservé avec sa provenance et son empreinte. L’annexe 3, à partir de la page imprimée 31, reproduit le décret n° 2010-1728. La page imprimée 32 (page 32 du PDF) a été rendue en PNG et lue visuellement : les deux emplacements mathématiques de l’article 49 septies ZZH comportent chacun la phrase de renvoi au JO n° 303 du 31 décembre 2010, texte 67. Le PDF ne contient donc pas les deux formules recherchées. Son tableau historique des primes 75/55/35 ne remplace pas non plus le tableau courant modifié en 2024.

Étendue honnête de lecture : titre, sommaire et annexe 3 ciblée, notamment page 32 intégralement ; pas de prétention à une revue juridique des 49 pages. Il s’agit d’une publication primaire de doctrine fiscale, avec reproduction d’un décret, et non du fac-similé authentifié du Journal officiel. La transcription textuelle complète du PDF est fournie pour permettre la recherche et ne vaut pas reconstitution des formules absentes.

La version HTML officielle de l’annexe 3, BOFiP-Archives identifiant 24759-AIDA / 30 mars 2012, renvoie également au JO aux deux endroits ; elle ne résout pas la lacune.

## Accès ordinaires et limites

L’ouverture HTTPS publique du décret 2010-1728 a renvoyé 403. Les deux liens de consultation PDF testés par l’outil web sont inaccessibles. L’ouverture normale dans Chrome du décret initial 2003-1376 a affiché une vérification de sécurité ; elle a été laissée intacte. Aucun CAPTCHA n’a été résolu, aucun cookie, jeton ou en-tête de contournement n’a été utilisé, aucun téléchargement CUA `downloadMedia` n’a été lancé.

Le lecteur web donne accès à la représentation HTML historique du décret 2003-1376. La formule mensuelle y est fragmentée et dupliquée par la représentation des fractions/sommes. Elle n’a pas été recomposée en norme actuelle. Les notations A/B, les bornes de somme et les modifications/rectificatifs doivent être confrontés aux fac-similés ; le terme trimestriel ne peut être déduit du terme mensuel. La circulaire RSI 2011/017 documente le déplacement des âges en 2010, pas un original graphique suffisant.

Les recherches ciblées n’ont pas retrouvé de reproduction primaire complète pour les deux CERFA historiques. La légende SUP de l’arrêté du 11 mai 1984 relative à R126-1 est distincte de la légende POS visée par A123-1/R123-18 : elle n’est pas utilisée comme substitut. Les versions du barème ophtalmologique de 2026 ou d’autres pays ne remplacent pas le cliché AT demandé. Les formules d’autres produits, notamment éco-PTZ ou reconstruction Mayotte, ne remplacent pas celles de 49 septies ZZH. La recherche de R254-5 déjà effectuée par le parent n’a pas été répétée.

`recovery-findings.json` donne pour chaque source la pièce exacte qui manque encore. Les anciennes recherches locales ont été lues en référence ; aucun résultat secondaire ou rapport d’experts ancien n’est requalifié en fac-similé réglementaire. Il reste notamment nécessaire de récupérer les JO exacts et rectificatifs concernés, ou une reproduction primaire complète démontrée identique.

## Sortie utilisable

- `source-snapshot.json` : les neuf sources officielles et notes entières, avec XML ARTICLE complet.
- `recovery-findings.json` : neuf réserves détaillées ; zéro transcription normative et zéro lacune déclarée levée.
- `boi-4a612-20120330.pdf`, provenance, texte intégral extrait et rendu de la page 32 : preuve primaire négative, vérifiable indépendamment.
- `access-attempts.json` et `legifrance-standard-attempt.json` : accès essayés, résultats et protection respectée.
- `fresh-guards.json` : 45 contrôles de stabilité en transaction RO, tous conformes à l’instant indiqué.
- `manifest.json` : empreintes de tous les fichiers de ce dossier.

La récupération demeure incomplète ; aucune intégration normative n’est proposée à ce stade. Aucun effet sur la publication C ni sur les travaux en cours.
