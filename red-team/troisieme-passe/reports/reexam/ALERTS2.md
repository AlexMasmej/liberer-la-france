# Réexamen ALERTS2 : alertes P1 perdues par le défaut du triage

Instantané ancien : `20261026T230545Z` (exports `evidence/cited/20261026T230545Z/`). Instantané courant : `20261027T044303Z` (lu par `tools/cite.py`, exports `evidence/cited/20261027T044303Z/`). Seconde passe arrêtée (`blocked`) : une proposition peut encore changer. Revue IA : elle ne vaut pas validation par un juriste.

## Synthèse

Le paquet compte 46 alertes P1 vivantes. L'outil de triage du coordinateur les avait classées à tort « reference_gone » : il ne reconnaissait pas les numéros suffixés (« 1406BIS » pour « 1406 bis »). 15 alertes n'avaient jamais été qualifiées (`index` 0 à 14). 31 l'avaient été sur l'ancien instantané, mais leurs textes ont changé depuis (`index` 15 à 45). Le paquet ne contient aucune objection du registre (`objections` : vide).

| Classification | Alertes | Objection |
|---|---|---|
| alerte écartée | 45 | — |
| coordination manquante | 1 | RT-P1-CGI-B-07 (existante, reformulée par le groupe CGI) |

Il y a aussi une **nouvelle objection, RT-RXALERTS2-01** (P2, coordination manquante, à confirmer). Elle ne vient d'aucune alerte : je l'ai trouvée en lisant 232 en entier, le renvoyeur de deux alertes.

Ce qui en ressort :

- **Les 15 alertes jamais qualifiées.** Leurs propositions sont identiques dans les deux instantanés (empreintes du manifeste). Seule l'erreur de triage les avait sorties des paquets. Toutes sont écartées : renvois neutralisants exprès (238 bis HM, 223, 289 bis, 990 F), plages de numéros ou notes documentaires (238 bis HM, 223 L), renvois figés (238 bis HW), bascules identiques (234 quaterdecies, 232), ou zonage rendu autonome (L441-2-8 et L631-7 du CCH).
- **289 bis.** Les contextes cités par l'audit pour 289 bis (« Par dérogation à l'article 289 E et au 1° du I de l'article 290 A » ; « Les obligations ayant un fondement autonome dans [...] le II de l'article 290 A demeurent applicables ») ne figurent plus dans le texte. Il dispose désormais : « Les articles 289 E, 290 et 290 A ne peuvent fonder aucune obligation de transmission [...] y compris pour les transmissions restant à effectuer ». La contradiction signalée par les notes de 289 E et 290 A est donc réglée côté 289 bis. Les objections RT-P1-CGI-A-01, A-02, A-03 et B-02 visent d'autres textes (annexes II et IV, 1737, CIBS) et ne sont pas touchées.
- **Les 31 alertes déjà qualifiées.** Les changements vont tous dans le sens d'une coordination. Quatre textes qui étaient retenus inchangés sont maintenant réécrits et bornés : 990 G, 1635 quinquies, 1507 et 1636 B octies. Les accessoires de 1647 (III bis, VIII, IX, XIX), 1599 bis, 1379-0 bis (XI), 302 decies, 881 L, 990 F et 299 septies (III, IV, VI) sont désormais bornés aux recettes ou opérations antérieures. La « coordination formelle recommandée » pour 299 septies a été faite.
- **Le seul changement de classement : 9152cc01… (1640 → 1407 ter).** Il passait d'« écartée » à « coordination manquante ». La réécriture de 1640 n'a borné que la taxe de 1530. Le II 1° b maintient toujours les délibérations prises sur 1406 bis et 1407 ter. Le registre traite déjà le cas 1640 → 1406 bis comme une coordination manquante (RT-P1-CGI-B-07, et RT-RXCGI-02 pour l'artefact du triage). Par cohérence, l'alerte est rattachée à B-07 sans nouvelle objection. L'effet reste limité, car 1407 ter neutralise ces délibérations (« Les délibérations antérieures ne peuvent fonder de nouvelles impositions »).

## Méthode

1. J'ai exporté par `cite.py`, sur le nouvel instantané, les 55 versions visées par le paquet (renvoyeurs et cibles, par identifiant LEGIARTI). Pour RT-RXALERTS2-01, j'y ai ajouté quatre textes du CCH qui renvoient à 232 : L422-2, L422-3, R302-14 et R642-1.
2. J'ai lu en entier, sur le nouvel instantané, la proposition, le motif et les notes de chaque renvoyeur et de chaque cible. Pour un article retenu inchangé, c'est la source qui est lue. Pour les trois textes longs (223 L, 1379-0 bis, 1647), toute la proposition a été lue, pas seulement le passage cité.
3. J'ai comparé chaque article à l'export ancien quand il existait (statut et empreintes de proposition, de motif et de notes). J'ai fait un diff phrase par phrase pour les renvoyeurs dont la proposition a changé : 299 septies, 1640, 302 decies, 881 L, 990 F, 1599 bis, 1647 B sexies, 1601, 1379-0 bis et 1647. Pour les articles sans export ancien, j'ai comparé les empreintes des manifestes.
4. J'ai qualifié chaque alerte selon `BRIEF-P1.md` : le renvoi vise-t-il la bonne cible, et pose-t-il aujourd'hui un problème réel ?
5. Avant toute nouvelle objection, j'ai vérifié les doublons dans `reports/register.json`, dans les `new_findings` des autres groupes et dans `merges.json`. Les objections existantes qui touchent des articles du paquet par un autre effet ne sont pas requalifiées ici : RT-P1-CGI-B-01, B-07, C-03, C-08, C-09, A-01 à A-03, B-02, A-08, B-03, B-10, RT-FUTFISC-01, 07, 14, 17, 32, 33, RT-DOMCVAE-01 à 05 et RT-RXCGI-01 et 02. Aucune objection ne traite la survie de 232 après le 1er janvier 2027 : une recherche de « 232 » dans le registre, les dossiers et les réexamens ne renvoie rien.

## Périmètre réellement lu (nouvel instantané)

Chaque article est donné avec son identifiant LEGIARTI et l'empreinte de sa proposition dans `ALERTS2.json` (`articles_read`).

- **CGI, renvoyeurs** :
  - 238 bis HM, 234 quaterdecies, 223, 232, 238 bis HW, 223 L, 289 bis (LEGIARTI000053546660) ;
  - 990 G, 1635 quinquies, 1599 bis, 1647 B sexies (LEGIARTI000048860555), 1601, 1507, 1636 B octies ;
  - 881 L, 1640, 990 F, 1379-0 bis, 302 decies, 1647, 299 septies.
- **CGI, cibles** :
  - 238 bis HL, 238 bis HJ, 234 nonies, 54 quater, 1406 bis, 1407 bis, 1586 ter (LEGIARTI000048847020), 223 U, 289 E, 290 A ;
  - 990 D, 1519 A, 1519 B, 1519 HB, 1599 quater A, 1599 quater B, 1599 quater D, 1601-0 A, 1607 ter, 1609 B, 1609 H ;
  - 1518 F, 1407 ter, 881 M, 223 quinquies A, 1613 quater, 1635 bis AE, AF et AG, 299 quinquies.
- **Annexe III, cibles** : 46 quindecies A, 46 quindecies F.
- **CCH** :
  - L441-2-8 et L631-7 (renvoyeurs), lus en entier ;
  - L422-2, L422-3, R302-14 et R642-1, en lecture ciblée (passages visant 232, motif, notes), pour RT-RXALERTS2-01.
- Versions de 232, 1406 bis, 1407 bis et 1407 ter énumérées par requête SQL en lecture seule (état et bornes).

## Constats

### RT-RXALERTS2-01 : 232 est réécrit comme un article qui survit, alors que la loi en vigueur l'abroge au 1er janvier 2027 sans successeur (P2, coordination manquante, à confirmer)

- **Source.** 232 (LEGIARTI000046872468) est ABROGE_DIFF, valable du 2023-01-01 au 2027-01-01. Le corpus ne contient aucune version ultérieure. D'après les NOTA de 1406 bis et 1407 ter, la loi n° 2026-103 (art. 108) transfère la taxe sur les logements vacants vers 1406 bis à compter des impositions de 2027.
- **Proposition.** Elle fait du I une définition de zonage qui « conserve un objet autonome pour les exonérations, aides, dérogations et autres dispositions qui s'y réfèrent, y compris pour les situations futures éligibles ». Elle maintient aussi les V et VI « pour leurs seuls usages autonomes malgré la disparition ou la recodification de la taxe ». Le motif le reconnaît : « La seule disparition de 232, déjà programmée au 1er janvier 2027, ne suffirait pas ». Le corps, lui, ne règle pas l'articulation avec cette abrogation.
- **Effet.** Une loi de réforme adoptée après le 1er janvier 2027, hypothèse réaliste retenue par RT-FUTFISC-07, ne peut pas modifier un article déjà abrogé. Elle devrait le rétablir expressément. Sinon, les clauses de survie n'ont aucun support.
- **Utilité faible.** Les renvois à 232 qui restent après 2027 sont :
  - L422-2 et L422-3 du CCH, pour une expérimentation de 2014 bornée aux opérations engagées pendant sa durée ;
  - R642-1, qui renvoie à la liste figée du décret n° 2013-392 ;
  - 1407 bis, lui-même éteint en 2027.
- **Risque si l'article est rétabli.** Cela créerait une troisième base de zonage pour les mêmes communes, à côté de la liste de 1406 bis figée par L441-2-8 et du décret autonome de L631-7 (voir RT-P1-CGI-B-01).
- **Aucune perte de faveur.** 1406 bis proposé supprime à lui seul la taxe et le relais, à la même bascule, et précise qu'il ne remet pas en vigueur « les dispositions antérieures de l'article 232 ».
- **À confirmer.** L'article 108 de la loi n° 2026-103 n'est pas disponible en entier. Il peut coordonner des renvois à 232 qui ne sont pas visibles ici.

### 9152cc01… : 1640 → 1407 ter, coordination manquante couverte par RT-P1-CGI-B-07

- **Texte actuel.** Le II 1° b de 1640 maintient, pour l'année où la création d'une commune nouvelle prend effet, les délibérations prises en application de « 1406 bis, 1407, 1407 ter ». La phrase « Les dispositions issues de l'article 108 de la loi n° 2026-103 du 19 février 2026 demeurent applicables à compter des impositions établies au titre de 2027 » n'est toujours pas bornée.
- **Ce qui a changé.** Seule la réserve relative à 1530 a été retouchée.
- **Neutralisation par la cible.** 1407 ter proposé prive ces délibérations d'effet pour les années supprimées.
- **Rattachement.** C'est le même mécanisme que celui que B-07 relève pour 1406 bis.

### Alertes écartées (45)

Le motif de chaque alerte figure dans `ALERTS2.json`, avec le classement et le motif précédents pour les 31 déjà qualifiées.

- **SOFICA (238 bis HM → 238 bis HL, HJ ; annexe III 46 quindecies A, F).** La plage « HE à HL » et la note « (1) Annexe III, art. 46 quindecies A à 46 quindecies F » sont documentaires. HM neutralise expressément l'indemnité de HJ, la reprise de HL, l'agrément du capital et les attestations des œuvres pour les faits nouveaux.
- **Renvois neutralisants.**
  - 223 → 54 quater : « Le présent renvoi ne rétablit [...] ni le relevé détaillé supprimé par l'article 54 quater » ;
  - 990 F → 223 quinquies A ;
  - 289 bis → 289 E et 290 A (trois alertes) ;
  - 1599 bis → 1599 quater A, 1599 quater B et 1519 HB (six alertes).
- **Bascules identiques ou bornages ajoutés.**
  - 234 quaterdecies → 234 nonies ; 232 → 1406 bis et 1407 bis ;
  - 1601 → 1601-0 A ; 1647 B sexies → 1601-0 A (« qui demeurent dues ») ;
  - 1647 → 1635 bis AE, AF, AG et 1519 B ; 881 L → 881 M (deux alertes) ;
  - 1379-0 bis → 1519 A ; 302 decies → 1613 quater ; 299 septies → 299 quinquies (trois alertes).
- **Textes passés de « retenu inchangé » à « réécrit ».**
  - 990 G → 990 D : non-déductibilité limitée aux taxes anciennes ;
  - 1635 quinquies → 1519 B : exception bornée, exemption maintenue ;
  - 1507 → 1518 F : réserve retirée avec la même transition ;
  - 1636 B octies → 1607 ter et 1407 ter (trois alertes) : répartition des TSE bornée. Les minorations par le produit de 1407 ter de l'année précédente portent sur un produit réellement perçu et deviennent nulles ensuite.
- **Plafonnement de CFE (1647 B sexies → 1599 quater D, 1607 ter, 1609 B, 1609 H).** La majoration par les TSE est nulle pour les années supprimées. Les cibles réservent les seuls montants légalement dus et interdisent toute reconstitution fictive. L'abrogation en 2030 des définitions de 1586 quinquies et sexies relève de RT-FUTFISC-14.
- **Renvois figés ou de plage.** 238 bis HW → 1586 ter (« dans leur rédaction applicable à la veille ») ; 223 L → 223 U (plage « 223 A à 223 U », 223 U n'étant qu'une habilitation réglementaire).
- **Zonage de 1406 bis (CCH L441-2-8 et L631-7).** Les deux textes rendent leur zonage autonome, et c'est précisément la correction que demande RT-P1-CGI-B-01. Cette objection reste ouverte pour L433-2 et L302-1. Les deux méthodes diffèrent : L441-2-8 garde « les critères [...] et les listes établies », L631-7 crée un décret autonome et maintient la liste en attendant. Cette différence n'a pas d'effet démontré.

## Propositions de correction (séparées des constats)

1. **RT-RXALERTS2-01 (232).**
   - Ne pas réécrire 232. Remplacer sa proposition par la seule mention que l'article reste abrogé au 1er janvier 2027 par la loi n° 2026-103, sans rédaction nouvelle.
   - Par sécurité, ajouter dans la loi de réforme une disposition non codifiée : « Les renvois à l'article 232 du code général des impôts qui servent à délimiter un territoire désignent, après l'abrogation de cet article, la liste de communes établie pour son application dans sa dernière rédaction. Cette règle ne maintient ni ne rétablit aucune imposition. »
   - Justification : 1406 bis proposé supprime déjà seul la taxe et son relais à la même bascule, et le régime des années antérieures reste celui de la loi en vigueur.
   - Autre option : si l'auteur veut une base de zonage vivante, la placer dans un article qui survit (sur le modèle du premier alinéa de L631-7), ou écrire « L'article 232 est rétabli dans la rédaction suivante » en se limitant au I et en alignant L441-2-8, L631-7, L433-2 et L302-1 sur une liste unique.
   - Dépendances : RT-P1-CGI-B-01 ; lecture de l'article 108 de la loi n° 2026-103.
2. **RT-P1-CGI-B-07, correction révisée (1) par le groupe CGI.** Étendre la borne aux délibérations prises sur 1407 ter, par exemple : « Le maintien des délibérations prises en application des articles 1406 bis et 1407 ter ne vaut que pour les impositions établies au titre des années antérieures à leur abrogation. » Aucune faveur n'est en jeu : seuls des maintiens de délibérations fiscales sont concernés.

## À préserver

Il faut conserver :

- la suppression de la taxe sur la vacance (232, relais de 1406 bis et majorations) et de la majoration de 1407 ter pour toutes les années suivant la réforme ;
- le régime des années antérieures et les recours ;
- la liste du décret n° 2013-392 (R642-1) et la continuité de liste de L631-7 et L441-2-8 ;
- l'absence de toute formalité de remplacement.

## Incertitudes et éléments non examinés

- L'article 108 de la loi n° 2026-103 et le décret de liste de 1406 bis ne sont pas disponibles en entier.
- La recherche des renvois à 232 est limitée aux neuf recueils locaux (versions en vigueur ou futures après le 18 octobre 2026) et à une recherche par expression régulière. Elle peut manquer des formulations inhabituelles.
- Je n'ai pas relu en entier L422-2, L422-3, R302-14 et R642-1, seulement leurs passages pertinents, leur motif et leurs notes.
- Je n'ai pas revérifié les objections existantes citées (B-01, B-07, FUTFISC-14, FUTFISC-17, etc.) au-delà de leur trace de réexamen.
- Aucune consultation externe (Légifrance, etc.) n'a été faite.

## Couverture

46 alertes sur 46 qualifiées, toutes après lecture entière du renvoyeur et de la cible sur le nouvel instantané (`read_in_full: true`). Aucune n'est classée `non examiné`.
