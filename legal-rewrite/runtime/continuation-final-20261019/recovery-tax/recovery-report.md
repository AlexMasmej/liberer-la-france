# Récupération fiscale — état au 19 octobre 2026

**Résultat : 0 article normativement achevé ; 4 pièces graphiques restent manquantes dans 2 articles.** Aucun enregistrement en base, lot, activation de pièce jointe ou publication. Les deux sources et leurs notes canoniques ont été lues intégralement ; aucun projet antérieur n’était enregistré lors du relevé.

## Pièces livrées

- `source.json` : corps canoniques entiers, notes, métadonnées de version, empreinte source brute et empreinte du corps ; les deux XML bruts sont aussi conservés individuellement.
- `companion-candidates.json` : deux fiches documentaires **incomplètes et non activables**, `proposed_xml: null`, marqueurs attendus, manque précis, preuves et réserves. Ce ne sont pas deux réécritures terminées.
- `answer.json` : tableau vide, car aucun candidat normatif complet n’a été établi.
- `validation.json` et `artifact-checksums.json` : contrôles et empreintes des fichiers locaux ; les journaux `*-attempts.json` conservent URL, résultat HTTP, taille et SHA des réponses reçues.
- Trois captures ont été inspectées visuellement : BOI2012 page32, BOFIP actuel page3 et première page de la copie JO différente.

## CGI annexe III — 49 septies ZZH — LEGIARTI000049362876

Deux formules sont absentes du corpus : (1) calcul du facteur β_t à partir de z_t ; (2) équation déterminant le taux annuel i qui annule la valeur actualisée nette du prêt de T mois. Les formules n’ont pas été déduites des phrases environnantes ou d’un autre régime.

Source initiale certaine : décret2010-1728 du30décembre2010, NOR **EFIE1033033D**, JORF0303 du31décembre2010 **texte67**, article1 :
https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023333871

Légifrance identifie un extrait authentifié de262Ko :
https://www.legifrance.gouv.fr/download/pdf?id=63svbPxxA_9vv0UbiiKxBb2WtDEED7w2wigHyhC4AJI%3D

Le JO intégral de18,1Mo est également identifié :
https://www.legifrance.gouv.fr/download/pdf?id=63svbPxxA_9vv0UbiiKxBU1tUE4pff_NWtPY0T-2KIM%3D

**Les deux téléchargements renvoient HTTP403**, y compris avec réseau autorisé. Les réponses HTML et leurs empreintes sont conservées. Aucun contournement de protection n’a été tenté. Le moteur web peut lire la version HTML du décret, mais les deux formules y sont aussi remplacées par un renvoi au JO.

Le BOI officiel4A-6-12, annexe3 p.32, a été vérifié visuellement : il comporte les mêmes deux renvois au JO à la place des formules. Le BOFIP actuel, BOI-BIC-RICI-10-140-20-10-20210310, téléchargé le19octobre2026, p.3, explique le tauxS et renvoie à49septiesZZH ; il ne donne pas ces formules.

Piste supplémentaire exactement rattachée au calcul : arrêté du25mai2011 NOR **DEVL1105391A**, JORFTEXT000024113794, JORF0129 du4juin2011 **texte10**, annexe2 de la convention État–SGFGAS. Son texte expose la mise en œuvre de49septiesZZH, mais les formules graphiques manquent également dans le HTML consultable. Le téléchargement direct de la page renvoie403. Le site `www2.sgfgas.fr` a renvoyé une erreur TLS de nom de serveur, conservée au journal.

Copies documentaires publiques recherchées :

- Le PDF téléchargé depuis `https://www.fichier-pdf.fr/2011/09/23/ptz-journal-officiel/ptz-journal-officiel.pdf` est le **décret2010-1704, NOR DEVL1025687D, texte20** du même JO, et non le texte67. Toutes ses pages extraites portent texte20 ; sa première page a été contrôlée visuellement. Il n’est donc pas une récupération des formules. Aucune authentification de signature JO n’est revendiquée.
- Les deux PDF Moneyvox retrouvés (`/r/arrete-20110525-ptz.pdf` et `/r/decret-2010-1704-ptz.pdf`) renvoient403. Leurs intitulés indexés visent respectivement texte9 et décret2010-1704, pas les textes manquants67/10.

**À préserver :** tableau canonique actuel p=75/55points de base, et NOTA d’application aux offres émises depuis le1eravril2024. Le tableau initial2010 en trois tranches n’est pas réintroduit. Le crédit d’impôt n’est ni supprimé ni diminué pour masquer le manque documentaire.

## CGI annexe IV — article15 — LEGIARTI000019493914

Les deux modèles entiers **CERFA30-0812 et30-0813** visés au1° manquent : cadres, rubriques, mentions et renvois, éventuels versos, rattachement exact de chaque numéro à son intitulé. Les rubriques décrites aux2° et4° ne prouvent pas à elles seules le contenu intégral des modèles.

Les archives officielles BOFIP4J1 et4J1342 du1ernovembre1995 sont téléchargées et conservées. Elles donnent le texte et les modalités des relevés, **aucune image de modèle entier**. Les anciennes versions LEGI consultées les omettent aussi.

La modification2008 est identifiée : arrêté15septembre2008, NOR **BCFL0818512A**, JORFTEXT000019491882, article1 LEGIARTI000019492164. Ce texte ne fournit pas la provenance initiale des deux modèles. La version la plus ancienne porte une anomalie de dates de consolidation ; elle n’a pas servi à reconstruire une période de validité.

**Piste secondaire à poursuivre, non probante à ce stade :**
https://www.dalloz.fr/documentation/Document?FromId=CODES_SECS_CGIM_TALPHA&id=CODE_CGIM_ANNE_4_ARTI_14

Le moteur indexe à cette URL deux tableaux intitulés « Modèle de relevé de coupons crédités en compte » et « Modèle de relevé de coupons encaissés au guichet ». Le HTML public effectivement téléchargé est une coquille JavaScript sans ces tableaux. Aucun PDF/fac-similé officiel, référence certaine des numéros CERFA, ni version n’a pu être contrôlé visuellement. Les mentions indexées d’avoir fiscal et d’identité du mari sont manifestement historiques et ne doivent pas être introduites comme droit actuel. L’outil navigateur in-app n’était pas disponible ; aucun accès payant ni protection n’a été contourné.

Aucune équivalence officielle avec2561/2078 ou un autre modèle moderne n’a été trouvée. Aucune substitution n’a été écrite. La future réécriture reste réservée jusqu’à la récupération exacte des modèles ou une décision normative distincte et traçable sur ces formalités ; une telle décision ne constituerait pas une récupération de la source graphique.

## Limite d’intégration

Ces fiches peuvent servir de dossier d’obstacles et de pistes. Elles ne doivent pas être placées parmi les pièces attestées complètes, ni faire augmenter le compteur des réécritures achevées. La récupération documentaire et l’authentification JO restent toutes deux **false** pour les deux articles.
