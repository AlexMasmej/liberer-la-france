# TR2 : points 2 à 5 (carte de couverture) et point 7 de la transmission

Instantané : `20261029T034912Z`. Lecture seule. `cite.py` a été lancé sur tous les articles cités ; les preuves sont dans `evidence/cited/20261029T034912Z/`. Détail et empreintes : `TR2.json` (clés `coverage`, `points`, `new_objections`). Les objections du registre sont seulement citées : leur réexamen relève des autres groupes (paquets `reexam-final` F01, F02, F04 et F05). Une revue IA ne vaut pas validation par un juriste.

**Lecture de production signalée.** La liste des 18 certificats ne figure ni dans l'instantané ni dans les preuves scellées. Je l'ai donc lue en lecture seule dans `runtime/heartbeat-check-20261025T0653Z/` : `current-reference-dispositions.json` (8d8a5ec7…), `target-change-explanations.json` (a8ad7095…) et `REPORT.md` (679140ee…). J'ai aussi lu les compteurs de trois fichiers `reconciliation-final.json`. Rien n'a été écrit ni exécuté en production.

## A. Carte de couverture

**2a (D351-9).** Couvert par RT-D351-01 (divergence 60/62) et RT-D351-02 (formule non jointe) ; voir aussi RT-D351-03 et RT-DOC-03. Le texte final est inchangé : LEGIARTI000030400105 n'a pas de proposition. On y lit « A est l'âge de référence fixé à soixante-deux ans » mais « L (A) est l'effectif à l'âge de soixante ans ». Qualification : pièce manquante, sur un conflit de source déjà qualifié.

**2b (annexe I R434-32 (7)).** Couvert par RT-DOC-01. RT-INV-03 (où a été fusionnée RT-FUTCSS-01) et RT-XCUT-01 (où a été fusionnée RT-INTEG-03) portent sur le successeur de R434-32, une autre question. LEGIARTI000028675462 reste documentary_hold, sans figure. Pièce manquante.

**2c (annexe IV art. 15).** Couvert par RT-DOC-02. LEGIARTI000019493914 : « (non reproduits-Cerfa n° 30-0812 et n° 30-0813) ». Pièce manquante.

**3 (douze coordinations CSS).** Constat factuel important : aucun des douze candidats parentaux du 25/10 n'est intégré tel quel. Mais au 29/10, les douze articles portent tous une proposition native completed, d'empreinte différente du candidat (par exemple D224-7 3c414c9f…, D224-8 5abb9152…, R612-7, R216-2, R281-4 et R213-5, qui sont passés de retained_unchanged à rewrite_draft). La mention « non intégrées, readiness=false » vise les candidats, pas l'état final des articles : il faut juger les propositions finales. Chaque réserve a ses objections :
- agréments, budgets et tutelle : RT-CSS12-01 à -06, -08 à -11, RT-UNION-03, RT-UNION-04, RT-TUT-04 ;
- D224-8 / D227-5 / L228-1 : RT-INST-01 à -04 et RT-TUT-01. RT-INST-03, faux positif, établit que le V de L228-1 n'impose pas lui-même l'avis ;
- L216-3 / L281-6 : RT-UNION-01 (sélecteur V), RT-UNION-02, -06, -07, RT-CSS12-11, RT-DOC-04 ;
- D227-6 / L224-10 : RT-TUT-01, -02, -03, -05, -06, -07, RT-UNION-07, RT-CSS12-08.

Seul aspect couvert partiellement : l'annexe 14 UGECAM. Elle n'apparaît que comme incertitude dans RT-UNION-02 et, de façon générique, dans RT-DOC-04. Aucun texte du corpus ne contient « UGECAM » ni « annexe 14 » (requête en lecture seule). L281-6 proposé maintient pourtant « les dispositions obligatoires et facultatives des modèles ». Qualification : pièce manquante, sans nouvelle objection.

**4a–4d.** Les textes sont inchangés depuis le registre ; seules les notes de 302 D bis ont changé. Tous les aspects sont couverts :
- 4a : RT-A1-01 à -04 et -06, RT-INUT-04 (où a été fusionnée RT-A1-05) ;
- 4b : RT-INUT-01 à -08 et RT-A1-02. Le motif de 50-0 G, qui suppose encore le numéro, relève de RT-INUT-02 ; la distinction avec les identifiants d'accise, de RT-INUT-08 et RT-INUT-06 ;
- 4c : RT-MENS-01, -02, -05 et RT-INUT-04 (où a été fusionnée RT-MENS-04) ;
- 4d : RT-CIBS-01 à -05.

Aucun aspect n'est sans objection.

**5a (AAH).** Le noyau est résolu dans le texte final :
- R821-8 (9cfaba2a…, désormais rewrite_draft/completed) : « Elle s'applique également aux hospitalisations et hébergements commençant après cette suppression, sans exiger le paiement d'un forfait ni une attestation de paiement. » ;
- L821-6 et L174-4 portent la même fiction.

L821-6 n'est visé par aucune objection. **Prémisse supersédée signalée** : RT-P1-CSS-B-01 décrit R821-8 « retained_unchanged ; inventaire=pending » et propose précisément la réécriture désormais faite. Ses autres volets ont aussi changé et sont dans le paquet F04. Aucun verdict n'est rendu ici. La concordance CASF L312-1 (R821-8 II) n'est couverte par aucune objection : pièce manquante, car le CASF est absent du corpus et le renvoi vient de la source. Une tentative Légifrance du 28/10 a échoué (mauvais identifiant) et n'a pas été renouvelée. Les notes finales de L174-4, L821-6 et R821-8 décrivent encore la coordination comme à faire : RT-TR2-01.

**5b (244 quater X / ZZX / ZZX bis).** Aucune objection du registre ne porte sur ces trois articles. Lecture des textes finaux :
- conflit 1, résolu : ZZX (47b4f0a3…) dit « ce premier fait générateur ne peut, à lui seul, maintenir cette condition pour l'avenir », ce qui concorde avec le X ;
- conflit 2, résolu : ZZX bis II (c1b90653…) dit « ces exigences de performances propres à l'autre voie d'éligibilité et leur justification ne sont pas cumulativement requises », ce qui concorde avec le VIII 2 ;
- ZZT 6° c, qui renvoie à 46 AG terdecies A (« par leur nature, équivalent à de la reconstruction »), est inchangé depuis la source. La branche de confortation porte en pratique sur le gros œuvre, déjà visé par la définition. La note de 46 AG terdecies A conclut : « La définition présente ne ferme pas la catégorie autonome de confortation. » Qualification : non confirmé ;
- décision 2012/21/UE, décrets et formulaires : pièces manquantes.

Les notes de 244 quater X qualifient toujours les deux conflits de « Contradiction effective et coordination hors lot » : RT-TR2-02.

## B. Point 7

**Les 18 certificats.** Ce sont des certificats `reference_coherence` refusés le 25/10 dans le périmètre de 681 articles, parce qu'une cible avait changé :
- 16 en CSS : L224-10, L225-1-1, L224-5, L224-5-2, L241-3-1, L241-3-2, L241-5, L241-5-1, L241-10, L241-13, L241-14, L242-3, L242-6, L242-7, L241-19, L241-20 ;
- 2 en urbanisme : L322-3, L322-11.

Les identifiants et les cibles modifiées figurent dans le JSON. Sur l'instantané final, **les 18 restent périmés** : la proposition du référent et les politiques sont inchangées, mais au moins une cible a changé. Aucun n'a été renouvelé, alors que les référents sont completed.

**Échantillon reconfronté (15 des 18).** Je l'ai choisi par gravité : heures supplémentaires et réduction générale, capitalisation retraite, UCANSS, délaissement, renvois ordinaux AT-MP. Résultats :
- L241-13 et L241-19 avec L241-18 et L241-18-1 : assertions confirmées (moins ou au moins vingt salariés, 36e à 40e heure, sept forfaits, cumul du VI) ;
- L241-3-1 et L241-3-2 avec L241-3 : confirmées ;
- L224-10, L224-5 et L224-5-2 avec L224-5-1 : confirmées ;
- L242-3, -6 et -7 avec L242-5 : confirmées, l'ordre des alinéas est conservé ;
- L241-5-1, L241-10 et L241-5 : confirmées ;
- L322-3 et L322-11 avec L322-5 : la réserve du certificat (renvoi au « troisième alinéa » de L322-7) est **levée** par le texte final, qui renvoie au « quatrième alinéa ».

Aucune contradiction confirmée : ce sont des périmés par empreinte. Non relus : L225-1-1, L241-14 et L241-20.

**Au-delà des 18 (indication).** Je n'ai pas recompté l'audit GLOBAL. En reproduisant les seuls contrôles d'empreinte, 1 737 des 5 388 certificats des lots finaux ne correspondent plus ; la réconciliation de production du 27/10 en comptait 2 996. Les 18 ne sont donc qu'un sous-ensemble.

**Anciennes analyses L1242-2 et CVAE.**
- L1242-2 (gardes du 22/10) : 10 des 15 propositions ont changé. Échantillon L2412-2 : la prolongation future autonome subsiste. Un contenu nouveau, non examiné le 22/10, est apparu : la protection pendant le mandat et les six mois suivants, sous réserve de L2411-3. Je n'y vois aucune perte de protection. Aucune objection du registre ne vise ce groupe.
- CVAE (gardes du 23/10) : 8 des 18 propositions ont changé, dont 1586 ter et 1647 B sexies. Le domaine est couvert par RT-FUTFISC-13, -14, -15, -32 et RT-DOMCVAE-03, -05. RT-DOMCVAE-01 et -02 y sont fusionnées.

Ni l'une ni l'autre analyse ne peut être reprise.

## Nouvelles objections

- **RT-TR2-01** (P2, anomalie d'inventaire, confirmé). Les notes finales de L174-4, L821-6 et R821-8 présentent comme à faire la coordination AAH déjà intégrée.
- **RT-TR2-02** (P2, anomalie d'inventaire, confirmé). Les notes finales de 244 quater X présentent comme ouverts les deux conflits ZZX et ZZX bis déjà réglés.

Toutes deux sont de même nature que RT-RXCGI-01 : je propose de les y fusionner comme instances, sans compter un défaut distinct. La correction porte sur les notes seulement, aucun corps n'est modifié.

## Couverture réelle et limites

Lus en entier avec `cite.py` (sources, NOTA, propositions, motifs et notes des versions en vigueur) :
- D351-9, annexe I R434-32 (7), annexe IV art. 15 ;
- R821-8, L821-6, L174-4 ;
- 244 quater X (les passages pertinents, le reste parcouru), ZZX, ZZX bis, ZZT, 46 AG terdecies A ;
- les cibles de l'échantillon du point 7 et L2412-2.

Pour les points 3 et 4, je me suis limité à l'état des empreintes et à des extraits, sans relecture sémantique, puisque ces points sont réexaminés ailleurs. Non examinés : textes extérieurs (CASF, arrêtés de modèles, décision 2012/21/UE, CIBS) et les trois certificats restants.
