# Groupe A3 — décisions de la troisième passe (versions futures du CGI : CVAE, plafonnement CFE, CSI, recodifications, faveurs)

Revue IA : rien de ceci ne vaut validation par un juriste. Lecture par `tools/cite.py` sur l'instantané 20261029T034912Z (sources, NOTA, propositions, motifs, notes et lignes propriétaires lus en entier pour chaque article modifié). Contrôle : `python3 -B apply/check_changes.py A3` → 59 changements construits et validés, 1 demande, 2 `skipped`, `problems` vide. Aucune écriture hors de `apply/A3/`, aucune écriture en production.

**Méthode commune.** Les corrections formulées « dans la loi de réforme » ont toutes reçu un équivalent codifié : une proposition en mode `new` sur chaque version future (VIGUEUR_DIFF) qui réédicte ce que le projet supprime, ou qui efface une faveur qu'il conserve, et une coordination de la version courante. Rien n'est placé sous `uncodified` : les textes non codifiés des dossiers (FUT-FISC A n° 1, B1 n° 1 et n° 3) et le paquet cvae-calendar feraient doublon. Les lignes `new` portent un `substantive_impact` de classe `coordination_only` qui reprend l'identifiant de mesure de la version courante, pour ne pas compter deux fois la même mesure. Aucune ligne ne crée d'impôt, de formalité ou de condition ; aucune faveur n'est retirée ; aucune ligne n'est marquée `loophole_closure`.

| Objection | Décision | Articles (modifiés) |
|---|---|---|
| RT-FUTFISC-13 | appliquée | 9 |
| RT-FUTFISC-14 | appliquée | 10 |
| RT-FUTFISC-17 | appliquée | 17 |
| RT-FUTFISC-18 à 22 | appliquées | 13 |
| RT-FUTFISC-26 | appliquée (option A, désignée conforme) | 3 |
| RT-FUTFISC-27 | appliquée (81, 39 quinquies G, 200) ; demande à A2 (1788 A) ; 1518 A quinquies A « déjà réglé » | 6 |
| RT-FUTFISC-30 | partiellement appliquée (note seule) ; reste « arbitrage » | 1 |

## RT-FUTFISC-13 — CVAE et TA-CVAE : barèmes et taux 2027-2029 publiés, non neutralisés

**Décision : appliquée** (objection « à confirmer », mais la correction est sûre quel que soit le point à confirmer : elle reporte une réforme déjà décidée et n'a d'effet que si les rédactions différées en auraient un). Équivalent codifié retenu à la place de la disposition transitoire « dans la loi de réforme » (A-redactions n° 1) : propositions sur chaque version future, et clause expresse de neutralisation inscrite dans 1586 ter, qui définit les années supprimées.

- **Articles touchés (9)** :
  - 1586 ter LEGIARTI000048847020 (replace) : dernier alinéa nouveau, qui rend sans application aux années supprimées les rédactions différées déjà publiées (1586 ter 2027, 1586 quater 2028-2029, 1600 2027-2029) et les maintient pour les années antérieures, sans toucher aux abrogations de 2030 ni aux taux décroissants du plafonnement ; phrase sur les définitions coordonnée avec RT-FUTFISC-14 ; note corrigée (ABROGE_DIFF = remplacement par la version 2027, pas abrogation).
  - 1586 ter LEGIARTI000053188762, version 2027 (new) : même texte, plus la substitution expresse de la rédaction de l'ordonnance n° 2025-1247 pour les années supprimées (renvoi L. 180-1 CIBS conservé pour les années antérieures).
  - 1586 quater LEGIARTI000048860944 (replace) : « Le dégrèvement de 188 euros… » remplacé par « Les dégrèvements prévus au II dans la rédaction applicable à chacune des années antérieures… » ; barèmes 2028 et 2029 écartés pour les années supprimées.
  - 1586 quater LEGIARTI000051242682 (2028) et LEGIARTI000051249022 (2029) (new) : abrogation pour les années supprimées ; barème réduit et dégrèvement de 125 € / 63 € conservés si l'année précède la suppression.
  - 1600 LEGIARTI000053562172 (replace) : le IV écarte pour les années supprimées les rédactions 2027 à 2029 ; leurs taux (9,23 %, 13,84 %, 27,68 %) restent dus pour les seules années antérieures ; note corrigée.
  - 1600 LEGIARTI000049534935 (2027), LEGIARTI000051242816 (2028), LEGIARTI000051249045 (2029) (new) : texte du projet (seule composante CFE, douze exonérations, demi-base artisans, 1,12 %, réserve de 1600 A) reporté, avec la rédaction et le taux propres à l'année si elle n'est pas supprimée. La version 2027 garde sa propre rédaction du I (sans l'établissement public de Corse).
- **Ce qui change en une phrase** : aucun barème, taux ou dégrèvement de CVAE ou de taxe additionnelle publié pour 2027-2029 ne peut renaître pour une année que le projet supprime, et les baisses programmées restent acquises pour les années antérieures.
- **Non codifié** : rien sous `uncodified`. La disposition transitoire A-redactions n° 1 et le paquet `coordinations/cvae-calendar` (statut « proposal_not_adopted ») feraient doublon avec les textes codifiés ; DOM-CVAE demande un véhicule unique.
- **Points laissés à l'auteur** :
  - activer ou non le paquet cvae-calendar ; s'il l'est, son XXVIII C (4e alinéa), qui laisse jouer la réécriture 2030 de 1647 B sexies, devra être aligné sur la rédaction retenue ici (voir DOM-CVAE C-02) ;
  - instructions JORF des lois de finances 2023 (art. 55), 2024 (art. 79), 2025 (art. 62) et de l'ordonnance 2025-1247 non lues ;
  - version 2030 de 1600 (LEGIARTI000051248679), hors du périmètre attribué : elle abroge le III comme le projet, mais ne reprend pas la réserve de l'article 1600 A ajoutée au II 1 ; coordination à décider (l'exonération de 1600 A reste autonome).

## RT-FUTFISC-14 — Plafonnement CFE : définitions abrogées en 2030, réécriture de 1647 B sexies

**Décision : appliquée** (codifiée, rédaction A-redactions n° 2 complétée). Elle supprime une contradiction et conserve des faveurs que cvae_removal ordonne de garder.

- **Articles touchés (10)** :
  - 1647 B sexies LEGIARTI000048860555 (replace) et ses versions futures LEGIARTI000051248428 (2028), LEGIARTI000051248495 (2029), LEGIARTI000048860644 (2030) (new, même texte) : rédaction fusionnée. Période de référence autonome (I bis, avec la règle de création d'entreprise) ; valeur ajoutée de 1586 sexies jusqu'en 2029 puis de 1647 B sexies A (navigation, 310 HC) ; plafond de 80/85 % et report des plus-values de l'année de création repris pour 2030 ; liste complète de la cotisation majorée (1599 quater D et 1609 İ conservés) ; taux 1,531/1,438/1,344/1,25 % ; VII ancré sur la date de la loi (et non sur 1586 ter, abrogé en 2030) ; VIII écartant les rédactions différées sauf leurs taux. `substantive_impact` mis à jour (effet relief_preserved ajouté).
  - 1586 quinquies LEGIARTI000023380915 (replace) : le I 1 ne vise plus le plafonnement, dont la période est au I bis de 1647 B sexies ; le III le rappelle ; note corrigée.
  - 1586 sexies LEGIARTI000043048297 (replace, notes seules) et LEGIARTI000054591243, version 2029 (new) : les deux alinéas du projet sont reportés sur la version 2029 (« contributions douanières »), avec la bascule 2030 du plafonnement.
  - 1447 LEGIARTI000053544997 (replace, notes seules) et LEGIARTI000046875608, version 2030 (new) : la version 2030 ne contient pas l'exonération CFE des micro-entrepreneurs (IV du projet) ; elle est reportée, avec le renvoi de 2030 au chiffre d'affaires de 1647 B sexies A (subdivision corrigée en « 1° du I »). Sans ce report, la faveur aurait disparu au 1er janvier 2030.
  - 238 bis HW LEGIARTI000046875615, version 2030 (new) : renvoi figé du projet aux définitions de 1586 ter à 1586 sexies, plafonds compris, reporté sur la version 2030 et complété pour une loi postérieure au 31 décembre 2029.
- **Non modifiés** : 1647 B sexies A (LEGIARTI000048847068) et annexe II 310 HC (LEGIARTI000047814988), qui s'appliquent tels que publiés par renvoi du b du I de 1647 B sexies ; 238 bis HW courant (LEGIARTI000047303743), dont le renvoi figé suffit tant que la loi précède 2030.
- **Ce qui change en une phrase** : à compter de 2030, le plafonnement de CFE ne dépend plus d'articles abrogés et cumule les éléments favorables de la version 2030 et ceux que le projet conservait.
- **Points laissés à l'auteur** :
  - instructions JORF de l'article 55 de la loi n° 2022-1726 (Q, G bis, I à İ) non lues ;
  - 1647 B sexies A ne reprend pas la mention de 1586 sexies relative à la décision 2009-599 DC : portée non examinée ;
  - renvois de CSS L137-33 à 1586 sexies après 2030 : RT-FUTCSS-04 (groupe A4) ;
  - incompatibilité avec le paquet cvae-calendar s'il est activé (voir RT-FUTFISC-13).

## RT-FUTFISC-17 — CSI : réédiction et extension au livre foncier de Mayotte au 1er janvier 2029

**Décision : appliquée** (équivalent codifié de la correction « dans la loi de réforme »). Elle rend effective une réforme déjà décidée : la suppression générale de la CSI, avec l'orientation `contribution_securite_immobiliere_removal` (« avantage Mayotte 881 O et anciens droits maintenus, sans renaissance CSI à son terme »). Elle empêche qu'une version future la rétablisse.

**Articles touchés (17)**
- CGI 879, LEGIARTI000022335681 (replace). Le I étend expressément la suppression au livre foncier de Mayotte : requêtes en immatriculation, inscriptions et inscriptions rectificatives, régularisations avec inscription provisoire, demandes en justice, oppositions, quelle que soit la date de l'acte. Il réserve les rédactions 2029 de 880 à 881 M (issues de la LF 2026, art. 102, I) aux seules demandes antérieures à la suppression. Le II ajoute que 881 O s'applique jusqu'à son terme aux demandes antérieures, et que la fin de 881 O, le 31 décembre 2028, ne rend aucune contribution exigible. Le reste de la proposition est inchangé : droits anciens, exonérations, pas de restitution générale, formalités civiles. La phrase des motifs, des notes et du `substantive_impact.scope_limitations` qui lisait les fins de version 2029 comme un simple « texte successeur à coordonner » est rectifiée. La citation `proposed_quote` est conservée telle quelle.
- CGI 880, 881 A, 881 B, 881 C, 881 I, 881 J, 881 K, 881 M, versions courantes (replace) : LEGIARTI000022335675, 022335747, 022335745, 038834363, 044073360, 044861032, 022335727, 022335723. Les propositions sont inchangées. Le motif et les notes sont rectifiés. La fin de version au 1er janvier 2029 n'est pas une abrogation : chaque motif nomme la version 2029 et décrit ce qu'elle réédicte ou étend. Pour 881 I, la mention d'un « texte opérant cette abrogation future » est supprimée.
- CGI 880, 881 A, 881 B, 881 C, 881 I, 881 J, 881 K, 881 M, versions 2029 (new) : LEGIARTI000053545692, 053545694, 053545699, 053545706, 053545720, 053545723, 053545726, 053545728. Chacune reçoit une proposition qui reporte la suppression avec la même formule que la version précédente. Les champs `change_type` full_repeal et `substantive_impact` coordination_only portent le `measure_id` contribution-securite-immobiliere-suppression, pour ne pas compter deux fois la même mesure.
  - La proposition vise expressément les cas mahorais nouveaux : 881 B (régularisation), 881 C 18° à 21°, 881 K II (immatriculation).
  - La rédaction de la LF 2026 est sans effet pour les demandes couvertes par la suppression. Elle ne s'applique qu'aux demandes présentées entre le 1er janvier 2029 et la suppression, s'il y en a.
  - Les demandes antérieures à 2029 restent régies par la rédaction antérieure et par 881 O.
  - Pour 880 et 881 A, les deux alinéas de la rédaction 2029 sont reproduits pour ces seules demandes intermédiaires, comme dans la version précédente.
- 881 O, LEGIARTI000053629981 : non modifié (retained_unchanged maintenu). Sa note « ne renaît pas après 2028 » a désormais une base textuelle dans le II de 879. Aucune réécriture n'est nécessaire.

**Ce qui change en une phrase.** Les rédactions 2029 de la LF 2026 ne peuvent plus faire renaître ni étendre la CSI au livre foncier de Mayotte après la réforme. Les droits anciens et l'exonération mahoraise jusqu'au 31 décembre 2028 sont conservés.

**Disposition non codifiée.** Elle n'est pas reprise sous `uncodified`. La phrase « Les dispositions du I de l'article 102 de la loi n° 2026-103 […] qui modifient les articles 880 […] 881 M sont abrogées » (B1 n° 1, I) devient inutile : les versions 2029 portent elles-mêmes la suppression, et 879 réserve leur rédaction aux demandes antérieures. Les ajouter créerait un second véhicule concurrent pour la même neutralisation.

**Points laissés à l'auteur.**
- Le texte JORF de l'article 102 de la LF 2026 n'a pas été lu. La nature de l'instruction (réécriture ou insertions) est déduite de la NOTA et de la comparaison des versions.
- Si la réforme entre en vigueur après le 1er janvier 2029, la CSI mahoraise est due entre cette date et la réforme. C'est le droit applicable à ces demandes, et le délai n'est pas chiffré.
- Le préambule de 879 (« abrogé pour les réquisitions et demandes présentées à compter de […] ») relève de RT-RXFISC-01, hors de cette part.
- Les décrets 55-22 et 55-1350 sont hors corpus.



## RT-FUTFISC-18 : droit fixe de procédure (1018 A, 1100)

- **Décision.** Appliquée : elle rend effective une suppression déjà décidée.
- **Articles touchés.**
  - 1018 A LEGIARTI000051877580 (`replace`) et LEGIARTI000052846070, version 2029 (`new`) ;
  - 1100 LEGIARTI000006305892 (`replace`) et LEGIARTI000052848556, version 2029 (`new`).
- **Ce qui change.** La rédaction du 1er janvier 2029, issue de l'ordonnance n° 2025-1091, réédictait le barème, la majoration de non-comparution, le supplément toxicologique et le débet. Elle est désormais couverte par l'abrogation prospective : aucun droit fixe ne renaît pour les décisions postérieures à la réforme.
- **Conservé.** Les décisions antérieures, avec leurs exemptions, dispenses, solidarités, restitutions et recours, ainsi que les amendes et frais qui ont un fondement autonome.
- **Laissé à l'auteur.** Le texte JORF de l'ordonnance, le CPP recodifié et le code de justice militaire L269-1 n'ont pas été lus.

## RT-FUTFISC-19 : présomption de revenu (1649 quater-0 B bis)

- **Décision.** Appliquée.
- **Articles touchés.** LEGIARTI000048638140 (`replace`) et LEGIARTI000053903698, version 2029 (`new`).
- **Ce qui change.** La rédaction de 2029, qui réédicte la présomption avec les renvois au CPP recodifié, ne s'applique au plus qu'aux années antérieures à la suppression.
- **Laissé à l'auteur.** Le texte qui modifie la version 2029 n'est pas identifié : la version n'a ni lien modificateur ni NOTA propre. Il est désigné par sa date et par son objet, sans subdivision inventée.

## RT-FUTFISC-20 : délit de réitération (1789)

- **Décision.** Appliquée.
- **Articles touchés.** LEGIARTI000024041681 (`replace`) et LEGIARTI000052845684, version 2029 (`new`).
- **Ce qui change.**
  - J'ai retiré la clause « ne reportent pas l'abrogation du présent article prévue au 1er janvier 2029 », qui reposait sur une abrogation inexistante. La phrase « ne rétablissent aucune disposition déjà abrogée » est gardée.
  - L'abrogation s'étend à la rédaction 2029, qui maintenait le délit devant le « tribunal délictuel ».
  - La loi pénale plus douce et la cessation d'exécution sont conservées.
- **Laissé à l'auteur.** La nature de l'instruction de l'ordonnance n'est pas vérifiée. Le renvoi entrant de 1753 reste à coordonner, hors de cette part.

## RT-FUTFISC-21 : droit de licence des débitants de tabac (568)

- **Décision.** Appliquée.
- **Articles touchés.** LEGIARTI000054591219 (`replace`) et LEGIARTI000054591800, version 2029 (`new`).
- **Ce qui change.** La rédaction issue du 1° du II de l'article 14 de l'ordonnance n° 2026-671 (recouvrement « contributions douanières ») ne fait pas renaître le droit ni la déclaration mensuelle des fournisseurs.
- **Laissé à l'auteur.** L'annexe IV 56 AJ et le CSP sont à coordonner, hors de cette part. La subdivision de l'ordonnance est déduite de la NOTA.

## RT-FUTFISC-22 : majoration de 0,2 % (1804 C)

- **Décision.** Appliquée.
- **Articles touchés.**
  - LEGIARTI000006313913 (`replace`) ;
  - LEGIARTI000053189053, version 2027, ordonnance n° 2025-1247 (`new`) ;
  - LEGIARTI000054591303, version 2029 (`new`).
- **Ce qui change.** Les rédactions de 2027 et de 2029 maintenaient la majoration. L'abrogation les couvre désormais, sans toucher à l'obligation de télérèglement de 1698 D.
- **Laissé à l'auteur.** La version 2029 n'a pas de NOTA. Son texte modificateur n'est pas établi (vraisemblablement l'ordonnance n° 2026-671, article 16, non vérifié), et il n'est donc pas cité dans le texte normatif.

## RT-FUTFISC-26 — 1496 ter : déclaration annuelle des loyers (2029)

**Appliquée (option A).** L'option A est retenue parce que l'objection la désigne elle-même comme « conforme aux orientations » : suppression des formalités sans remplacement.

- **Articles touchés :**
  - CGI 1496 ter LEGIARTI000041403640 (mode new, `full_repeal`) ;
  - CGI 1729 C LEGIARTI000042913666 (replace) ;
  - CGI 1418 LEGIARTI000053546060 (replace, notes seules).
- **Ce qui change :**
  - La déclaration annuelle des loyers des bailleurs, qui devait entrer en vigueur en 2029, est abrogée avant toute application.
  - La révision des valeurs locatives repose sur les données déjà légalement détenues, sans accès nouveau ni déclaration de remplacement.
  - 1729 C ne vise plus 1496 ter. Ses notes erronées (« 1496 ter absent du corpus ») sont rectifiées.
  - 1418 n'est pas étendu au loyer.
- **Laissé à l'auteur :**
  - la faisabilité et le coût d'une révision sans déclaration (loi 2019-1479, art. 146, hors corpus) ;
  - l'option B (fusion du loyer dans la déclaration de 1418), non retenue ;
  - le VI de l'article 146, encore visé par 1729 C et non vérifié.

## RT-FUTFISC-27 — Faveurs créées par des versions futures

**Appliquée pour 81, 39 quinquies G et 200.** Rien n'est à changer pour 1518 A quinquies A. 1788 A fait l'objet d'une demande au groupe A2.

- **81 :**
  - LEGIARTI000054703556 (replace) : le f du 4° (allocation de réparation des mineurs réunionnais, loi n° 2026-555) est ajouté sous sa condition d'entrée en vigueur : décret, au plus tard le 1er janvier 2029. Une phrase transitoire précise que la réforme n'en restreint pas le bénéfice. La note qui lisait ABROGE_DIFF comme une abrogation est corrigée.
  - LEGIARTI000054354206 (new, `normative_reduction`, `coordination_only`) : la réforme du projet (salaires étudiants, aide au transport, titres-restaurant) est reportée sur la version 2029, f inclus.
- **39 quinquies G :**
  - LEGIARTI000048805546 (replace) : un alinéa est ajouté à la fin du I. Il ouvre la provision aux risques liés aux émeutes, avec un délai de quinze ans, à la date fixée par le décret de la LF 2026, art. 171 III, après décision de la Commission. Placé en fin de I, il ne décale aucun renvoi existant.
  - LEGIARTI000053548420 (new) : la réforme (suppression des transmissions spéciales, coordination de l'IS à la distribution) est reportée sur la version future, avec les émeutes.
- **200 :**
  - LEGIARTI000053543932 (replace) et LEGIARTI000053154489 (new, même texte) : le taux de 75 % vise l'union de deux définitions. La première est la définition autonome des soins, reprise de 261, 4, 1°, désormais datée au 31 décembre 2026. La seconde reprend les renvois de la version 2027 au 3° de L. 213-96, à L. 213-98 et à L. 213-100 du CIBS.
  - L'union ne peut restreindre le champ. Aucun contenu du CIBS n'est reproduit ni présumé.
  - Cette rédaction couvre aussi le point de RT-INV-06 (groupe A6) sur le renvoi à 261.
- **1518 A quinquies A** (LEGIARTI000053534927) : nouvel article sans brouillon, qu'aucune proposition ne réécrit. Le lissage s'applique tel que publié. Rien n'est modifié (`skipped`, « déjà réglé »).
- **1788 A** (groupe A2) : demande de conserver « a. (Abrogé) » au 1 et au 2 dans la version du 1er juillet 2030 (LEGIARTI000053294012), et de ne pas rétablir ces amendes après le 30 juin 2030 par une rédaction fondée sur une base antérieure.
- **Laissé à l'auteur :**
  - la portée réelle des articles du CIBS (hors corpus) ;
  - les dates effectives des décrets (81 f et 39 quinquies G) ;
  - 1788 D et 1647 B sexies A, traités sous RT-FUTFISC-09 et RT-FUTFISC-14.

## RT-FUTFISC-30 — 1518 A sexies : réduction, actualisation et lissage 2027

**Partiellement appliquée (note seule).** Le reste n'est pas appliqué : c'est un arbitrage.

- **Article touché :** CGI 1518 A sexies LEGIARTI000053545912 (replace, proposition inchangée).
- **Ce qui change :**
  - La note affirmait à tort qu'aucun successeur n'était fourni. Elle signale désormais la version 2027 (LEGIARTI000053589487) et son III, ainsi que le lissage de 1518 A quinquies A.
  - Elle indique aussi que le III proposé (réductions en cours au 31 décembre 2020) n'a plus d'effet après 2026 : son renvoi à 1518 A quinquies ne vaut que pour les années anciennes.
- **Non appliqué :**
  - le remplacement du III par celui de 2027 ;
  - la suppression de « Les réductions en cours sont conservées pour leur durée restant à courir » ;
  - le choix entre limiter la transmissibilité aux réductions non éteintes en 2027 et exclure ces locaux du lissage.

  Le réexamen dit lui-même « Ce choix revient à l'auteur ». Chaque option retire une faveur écrite par le projet ou réduit le lissage légal. Pour la même raison, aucune proposition n'est créée sur la version 2027 : elle trancherait ce choix.
- **Laissé à l'auteur :** l'articulation entre le maintien des réductions en cours et le lissage 2027-2031, ce qui comprend le risque de double atténuation et le report de la réforme (transmission au nouvel exploitant) sur la version 2027.


Revue IA : rien de ceci ne vaut validation par un juriste.
