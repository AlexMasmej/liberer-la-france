# Dossier INUT : déclaration de profession et numéro IN/UT (alcools exonérés)

Red-team juridique indépendante, troisième passe. Rapport établi le 26 octobre 2026 sur l'instantané `snapshots/20261026T230545Z` (corpus arrêté au 18 octobre 2026). Toutes les conclusions sont provisoires : la seconde passe continue en production, et celle de CGI 302 D bis est encore `pending`. Ce travail est une revue faite par une IA. Il ne vaut pas validation par un juriste.

Préfixe des objections : `RT-INUT-xx`. Le fichier `INUT.json` reprend ces objections sous forme structurée.

---

## 1. Périmètre réellement lu

Tout a été lu par `tools/cite.py` : source entière, NOTA, bornes, état, proposition, motif, notes de revue et lot propriétaire. Les copies sont dans `evidence/cited/20261026T230545Z/`.

| Code | Article | Versions lues (LEGIARTI, bornes, état) | Statut du projet |
|---|---|---|---|
| CGI | 302 D bis | 006304984 (2001-09-01→2010-01-01) ; 021664227 (2010→2012-03-16) ; 025516267 (2012→2014-12-30) ; 030061575 (2014→2018) ; 031816856 (2018→2020) ; 041535137 (2020→2021) ; **041472187 (2021-01-01→2222-02-22, ABROGE_DIFF)** ; 043140563 (MODIFIE_MORT_NE, 2023-01-01, III « (Abrogé) ») ; 041535168 (MODIFIE_MORT_NE, 2026-01-01) | rewrite_draft, seconde passe **pending** |
| Annexe III | 111-0 E | **006298854 (2005-07-06→2999, VIGUEUR)** | rewrite_draft |
| Annexe III | 111-0 F | 006298855 (2005-07-06→2006-01-01) ; **006298856 (2006-01-01→2999)** | rewrite_draft |
| Annexe IV | 50-0 G | 006300441 (2005-07-06→2006-01-01) ; **006300442 (2006→2999)** | **retained_unchanged** (proposed_xml NULL) |
| Annexe IV | 50-0 H | **006300443 (2005-07-06→2999)** | rewrite_draft |
| Annexe II | 289 | 23 versions, de 006294741 (1998) à **054363092 (2026-07-01→2999)** | rewrite_draft |

La version courante de 289, sa proposition, son motif et ses notes ont été lus en entier. Pour les 22 versions historiques, j'ai fait une lecture différentielle ciblée : apparition du 15° dans la version 006294747 du 12 mai 2006, constance du 2° et des 15°/18°. Je n'ai pas relu ligne à ligne les quelque 60 rubriques de chaque version antérieure, car elles sont sans lien avec ce dossier.

**Recherche dans la base**, en lecture seule, sur les sources et les propositions courantes au 18 octobre 2026, avec les motifs suivants : « déclaration (préalable) de profession », IN/UT, « numéro UT/IN », « utilisateur(s) d'alcool », « intermédiaire mentionné/défini », 111-0 E/F, 50-0 H, « alcool dénaturé », « en franchise », 302 D bis. Tous les résultats pertinents ont été lus en entier par `cite.py` :

- annexe III 111-0 G (006298857) et 111-0 H (006298858) ;
- annexe IV 50-0 I (006300444), 130 (006300919) et 54-0 H (006300709) ;
- annexe I 181 (006293591) ;
- CGI 458 (041472229, ABROGE_DIFF) et 508 (006309958, ABROGE_DIFF).

Les autres résultats ont été écartés après lecture de leur passage : homonymies sur « intermédiaire » (logement intermédiaire, sociétés intermédiaires, guichet IOSS) et sur « en franchise » sans lien avec l'alcool.

Les articles 165, 185 et 186 de l'annexe I relèvent du dossier A1DOSSIER. Je les ai seulement repérés, sans les instruire. 111-0 H 2° et 50-0 I II relèvent du dossier MENS.

**Preuves scellées lues :**
- `alcohol-denaturation-coherence-readonly-20261026T1305Z` : REPORT, CONTROL, qualification sémantique (sept constats), exigences restantes, comparaison officielle de 165/186 et liste des identités. Les gros fichiers d'entrée (copies intégrales des lignes de la base, environ 1 Mo) ont été inventoriés par identité, sans relecture redondante, puisque leur contenu est celui de l'instantané relu par `cite.py`.
- `alcohol-2005-scoped-readonly-20261026T1505Z` : REPORT, CONTROL, qualification 2005 et complément 50-0 G, exigences, revue de la copie, diff.
- `alcohol-2005-normative-followup-20261026T1501Z` : décret n° 2005-758 affiché en entier (255 lignes), reçus du sommaire du JO du 6 juillet 2005, échec d'accès à l'arrêté du 4 juillet 2005 (Cloudflare 403, non contourné), extrait de l'étude d'impact de 2018.
- Pistes complémentaires : `cibs-alcohol-public-followup-20261026T1707Z` (CIBS L313-6 à L313-18 affiché dans sa version du 18 mars 2026) et `cibs-2021-primary-pistes-followup-20261026T1808Z` (articles 40 et 41 de l'ordonnance 2021-1843, mention de l'abrogation de 302 D bis par son article 10).

**Sources publiques consultées le 26 octobre 2026 :**
- EUR-Lex, directive 92/83/CEE (CELEX 31992L0083 et version consolidée) et directive 2020/262 (CELEX 32020L0262) : **inaccessibles**. L'URL HTML a renvoyé HTTP 202 avec un corps vide (défi anti-robot). Rien n'a été contourné.
- Légifrance, article 38 de l'ordonnance 2021-1843 et PDF de l'étude d'impact de 2018 : HTTP 403.
- douane.gouv.fr, page « Le dispositif d'exonération de droit d'accise sur l'alcool » : accessible, sans date de mise à jour affichée. C'est une page administrative non normative, et sa date réelle peut être postérieure au 18 octobre 2026.
- assemblee-nationale.fr, amendement n° 534 au PLFR 2022 (n° 17), du 18 juillet 2022, retiré : accessible, texte extrait du PDF.

## 2. Méthode

1. J'ai lu en entier les versions et les propositions citées par `cite.py`, puis comparé chaque corps proposé à ceux des autres niveaux : loi (302 D bis), décret (annexes II et III), arrêté (annexe IV).
2. Pour chaque texte qui dépend du circuit, j'ai qualifié la référence de l'une de trois façons :
   - (a) maintien du numéro ou de la déclaration supprimés ;
   - (b) contradiction entre le corps et le motif ;
   - (c) identifiant d'accise autonome (numéro d'accise, entrepositaire agréé, destinataire enregistré, expéditeur ou destinataire certifié, numéro d'agrément), à ne pas confondre avec IN/UT.
3. J'ai confronté les conclusions scellées à l'instantané courant. Elles restent exactes : 50-0 H et 50-0 G sont inchangés depuis 13 h 05 et 15 h 05.
4. Pour l'ordre juridique supérieur (loi et CIBS, droit de l'Union), je ne conclus que sur des sources primaires réellement obtenues. Ce qui n'a pas été obtenu reste une réserve.
5. Points déjà écartés et non rouverts : l'exception spéciale des 3° de 111-0 G/H pour les corrections traçables face à 50-00 D, et la double comptabilisation des renvois 185/186 vers 165.

## 3. État du circuit dans le projet courant

| Texte | Proposition courante | Qualification |
|---|---|---|
| CGI 302 D bis III | Supprime la déclaration préalable de profession. Le numéro ne peut être exigé « sur le seul fondement du présent article ». | Base de la suppression. Rédaction perfectible (RT-INUT-04). |
| An. III 111-0 E | I 2°, 4° b et c, II 2° : plus de copie, plus de numéro, plus de déclaration de l'intermédiaire. I 3° : une extraction des données commerciales tient lieu de liste clients. | Cohérent avec 302 D bis III. Les « identifiants exigés sur un autre fondement » (I 4° b) sont légitimes. |
| An. III 111-0 F | I 1° et 2° : plus de déclaration, de numéro, de copie, ni d'avis de retrait. II : dossier technique tenu à disposition. | Cohérent. Transition sur les numéros existants à compléter (RT-INUT-07). |
| An. III 111-0 G/H | Renvoient aux « obligations fixées à l'article 111-0 F ». | F conserve des obligations (conservation, justification des quantités) : alerte écartée (RT-INUT-09). Le rapport mensuel relève de MENS. |
| **An. IV 50-0 H** | **Conserve la déclaration, les modèles I à III de l'arrêté de 2005, les pièces, le numéro IN/UT, la case administrative et les rubriques.** Seuls le second exemplaire et le cachet sont retirés. | **Incohérence du projet (RT-INUT-01).** Le « numéro d'accises » du 5° a 1 est un identifiant autonome légitime. |
| **An. IV 50-0 G** | **Inchangé : son b exige le numéro IN/UT.** Le motif présente la liste comme « distincte de la déclaration de profession », et les notes tiennent pour acquis le maintien de l'IN/UT dans 50-0 H. | **Incohérence du corps (suppose un numéro supprimé) et entre le corps et le motif (RT-INUT-02).** |
| An. II 289 15° | Compétence d'attribution et de retrait des numéros IN/UT maintenue. La clause finale lui refuse tout fondement autonome. | Coordination manquante à effet limité (RT-INUT-03). Le 2° (autorisation du procédé de dénaturation) et le 70° (expéditeur ou destinataire certifié) sont des compétences autonomes à conserver. |
| An. I 181 | Abrogation de la déclaration des locaux de commerce des alcools dénaturés par procédé général. | Cohérent avec 302 D bis III : alerte écartée (RT-INUT-09). |
| An. I 165 | Corps : « La déclaration prévue au III de l'article 302 D bis … demeure distincte ». | Relève de **A1DOSSIER** (constat scellé « 165-premise-profession ») : non doublé ici. |
| An. IV 50-0 I II c | Numéro UT dans la déclaration mensuelle vinaigre. | Relève de **MENS** : non doublé ici. |
| An. IV 130 ; 54-0 H | « Déclaration de profession » des marchands de billets et des fabricants de marques fiscales. | Circuits distincts : faux positif (RT-INUT-08). |
| CGI 458 ; 508 | Alcools totalement dénaturés affranchis des formalités de circulation ; lieu de dénaturation. ABROGE_DIFF, hors inventaire, sans proposition. | Pas de numéro IN/UT. La NOTA de 508 renseigne sur l'abrogation différée (RT-INUT-04). |

## 4. Constats

### RT-INUT-01 (P1, incohérence du projet, confirmé) : 50-0 H maintient la déclaration et le numéro IN/UT supprimés par la loi et le décret

**Ce que dit le texte.** La proposition de 50-0 H commence ainsi : « les opérateurs doivent établir une déclaration préalable de profession conforme au modèle de l'annexe I de l'arrêté du 4 juillet 2005 ». Son 3° prévoit : « La déclaration porte un numéro d'identification composé de sept caractères numériques précédés des lettres « IN » … ou des lettres « UT » ». Son motif ajoute : « la copie nécessaire aux fournisseurs demeure ».

**Ce qui le contredit.**
- 302 D bis III proposé : le bénéfice « ne [est] subordonné[] à aucune déclaration préalable de profession ».
- 111-0 E II 2° proposé : l'intermédiaire « n'est soumis à aucune déclaration préalable de profession ni à l'attribution d'un numéro d'identification ».
- 111-0 F I 1° proposé : aucune déclaration ni numéro.
- 111-0 F I 2° proposé : « aucune copie … n'est exigée ».

**Pourquoi c'est un problème.** L'annexe IV est un texte de niveau arrêté. Elle prétend appliquer « le 2° du II de l'article 111-0 E » et « le 1° du I de l'article 111-0 F », de niveau décret, alors que ces deux dispositions retirent désormais la formalité. Un arrêté d'application ne peut maintenir une obligation que le décret et la loi suppriment. Dans le projet, cela produit un texte illégal ou, au mieux, une source d'insécurité : formulaires et téléservice SOPRANO UT maintenus, refus d'exonération au guichet. La transition propre à 50-0 H (« sans renouvellement des dépôts déjà effectués ») suppose elle aussi la survie du circuit.

**Constat scellé confirmé.** Le constat « profession-50H » de 13 h 05 est intact dans l'instantané.

### RT-INUT-02 (P1, incohérence du projet, confirmé) : 50-0 G est conservé inchangé alors que son b suppose le numéro supprimé, et son motif contredit son corps

**Ce que dit le texte.** Le corps maintenu prévoit : « b. Le numéro d'identification porté sur la déclaration préalable de profession, numéro fixé … dans les conditions définies à l'article 50-0 H ». Le motif affirme : « La liste constitue une preuve de destination admissible, distincte de la déclaration de profession ». Les notes de revue ajoutent : « Le numéro IN/UT est conservé dans 50-0 H proposé ; le renvoi demeure cohérent ».

**Pourquoi c'est un problème.**
1. Le corps suppose un numéro que 302 D bis III et 111-0 E/F retirent.
2. Le motif décrit la liste comme distincte de la déclaration alors que la rubrique b en dépend entièrement.
3. La cohérence alléguée repose sur 50-0 H, qui est lui-même en contradiction (RT-INUT-01).
4. Le chapeau parle d'une « liste récapitulative », alors que 111-0 E I 3° proposé ne demande plus de liste séparée et admet une extraction des données commerciales.

Il s'agit de la même coordination que RT-INUT-01 : ce n'est pas un gain de formalité supplémentaire. L'objection est distincte seulement parce qu'un second corps doit changer. La rubrique a (identité, adresse, activité du destinataire) reste utile comme **preuve ordinaire de destination** et doit être conservée.

### RT-INUT-03 (P2, coordination manquante, confirmé) : 289 15° conserve la compétence d'attribution et de retrait des numéros IN/UT

Le 15° proposé est identique à la source : « Attribution et retrait du numéro d'identification des intermédiaires … et … des utilisateurs ». Il vise des dispositions (111-0 E II 2°, 111-0 F I 1°) qui n'attribuent plus de numéro.

L'effet est limité. Le dernier alinéa proposé dispose que les attributions « ne constituent pas un fondement autonome d'autorisation, d'agrément, de déclaration », et que les renvois abrogés ne valent que pour les opérations antérieures. Il reste néanmoins une rubrique trompeuse, qui conforte la lecture de 50-0 H.

À conserver : le 2° (autorisation du procédé spécial de dénaturation, I b de 302 D bis), le 5° (retrait d'agrément de l'entrepositaire agréé), le 67° (numéro d'accise substituable), le 70° (expéditeur ou destinataire certifié), les dispenses, décharges et remboursements.

### RT-INUT-04 (P1, risque juridique, à confirmer) : la base législative de la suppression est fragile, car 302 D bis est en abrogation différée et les exonérations figurent depuis 2022 au CIBS

**Faits établis par des sources primaires.**
- **LEGI, dans l'instantané** : 302 D bis (041472187) est à l'état `ABROGE_DIFF`, borne technique 2222-02-22, avec un lien `ABROGE` vers l'article 10 de l'ordonnance n° 2021-1843 (JORFTEXT000044590225) et des liens `CONCORDANCE` vers CIBS L313-7 à L313-14 et L314-9 à L314-12. Pour l'article 508, rattaché au même régime, la NOTA précise : « Conformément au 5° de l'article 38 de l'ordonnance n° 2021-1843 … l'abrogation des présentes dispositions prendra effet à compter de l'intervention du décret mentionné à l'article L. 311-39 du code des impositions sur les biens et services ». Pour 458, la NOTA renvoie à l'article 38 de l'ordonnance 2021-1843 et à l'article 41 de l'ordonnance 2023-1210.
- **LEGI, versions mort-nées de 302 D bis** : 043140563 (2023-01-01, NOTA « II de l'article 185 de la loi n° 2019-1479 ») affiche « III.-(Abrogé) ». La suppression du III a donc déjà été votée par le législateur, puis n'est jamais entrée en vigueur.
- **Légifrance, CIBS** (sous-section L313-6 à L313-18 affichée dans sa version du 18 mars 2026, reçu scellé de 17 h 07) : L313-7 et L313-8 exonèrent les alcools dénaturés « en vigueur depuis le 01/01/2022 ». L313-8 2° dispose : « dénaturé conformément à l'un des procédés autorisés, dans des conditions déterminées par décret ». Aucune déclaration de profession n'y figure.
- **Amendement AN n° 534** (PLFR 2022, 18 juillet 2022, retiré) : il qualifie 302 D bis d'« (abrogé) » et indique que l'article 185 de la LFI 2020 a été abrogé. Il proposait de réinsérer la déclaration dans un article L. 313-14-1 du CIBS.
- **douane.gouv.fr** (page non normative, consultée le 26 octobre 2026, non datée) : « le dispositif actuel de la DPP-UT sera maintenu au-delà du 1er janvier 2023 ». La page vise les exonérations des articles L. 313-7 à L. 313-14 du CIBS.

**Conséquences.**
1. Le jour où l'abrogation différée de 302 D bis prendra effet, le III proposé disparaîtra avec l'article. La garantie législative « aucune déclaration » sera alors perdue, et les textes d'application du CIBS (hors corpus) pourront rétablir une déclaration.
2. Dès aujourd'hui, le régime d'exonération effectivement appliqué par l'administration s'adosse au CIBS. Les annexes III et IV, qui sont prises « pour l'application » de 302 D bis, sont la seule vraie prise réglementaire du projet. D'où l'importance décisive de corriger 50-0 H.
3. La formule « ne peut être exigé sur le seul fondement du présent article » laisse ouverte une exigence fondée sur un autre texte.

**À confirmer.** Je n'ai pas obtenu le texte des articles 10 et 38 de l'ordonnance, ni celui du décret visé à L. 311-39, ni le CIBS figé au 18 octobre 2026. Le champ résiduel exact de 302 D bis reste donc une **réserve documentaire**. Ce n'est pas un conflit de source prouvé.

### RT-INUT-05 (P1, risque juridique, à confirmer) : la suppression du numéro ne doit pas faire disparaître la qualité d'« utilisateur » ni imposer le statut d'entrepositaire agréé

L'exposé de l'amendement AN n° 534 (source parlementaire primaire) le dit expressément : « la suppression de la déclaration préalable de profession entraîne celle du statut d'utilisateur d'alcool pratiqué par un très grand nombre d'opérateurs qui devraient, pour la plupart, passer sous un statut douanier d'entrepositaire agréé ». La page de la douane, non normative, précise de son côté que ces opérateurs « ne seront pas tenus d'adopter le statut d'Entrepositaire Agréé ». Elle mentionne aussi la circulation nationale sous « DSA "exo" », et l'envoi vers un autre État membre sous DAE ou DAES selon le statut du destinataire.

Dans le projet, 111-0 F proposé garde la définition de l'« utilisateur ». Mais aucun texte ne dit que cette qualité subsiste sans numéro et n'exige pas le statut d'entrepositaire. Si la qualité d'utilisateur était lue comme l'attribution du numéro UT, la réforme aboutirait à une charge plus lourde (agrément, caution, comptabilité d'entrepôt). Ce serait l'inverse de l'objectif poursuivi et la perte d'une faveur existante.

Le mécanisme exact de cette bascule n'est établi par aucun texte normatif obtenu, d'où le statut « à confirmer ». La priorité P1 tient à l'effet probable et lourd si le risque se réalise.

### RT-INUT-06 (P2, risque juridique (Union européenne), à confirmer) : le contrôle reste suffisant au regard de l'article 27 de la directive 92/83/CEE, sous réserve de lecture d'EUR-Lex

**Source obtenue.** L'étude d'impact du projet de loi de suppression des surtranspositions (2018, article 10) affirme, dans un extrait scellé : « Elle ne résulte pas de l'article 27 de la directive 92/83/CEE ». Elle retient l'option « supprimer l'obligation de dépôt ». L'article 27 laisse aux États membres le soin de fixer les conditions d'une application correcte des exonérations et de prévention de la fraude, de l'évasion et des abus. Je n'ai pas pu en vérifier la lettre sur EUR-Lex (accès bloqué). Cette paraphrase reste donc à vérifier.

**Garanties conservées dans les propositions.**
- Fournisseur entrepositaire agréé (111-0 E I 1°).
- Documents d'accompagnement ou économiques portant la mention « Produits exonérés » (I 4°).
- Identification des destinataires dans les données commerciales (I 3°, 50-0 G a).
- Marquage alimentaire indélébile (II 1°).
- Justification des besoins réels et des quantités par l'utilisateur (111-0 F II 2°) et dossier technique à disposition (II 1°).
- Stockage séparé chez le débitant (II 3°).
- Comptabilité matières au-delà de 100 L d'alcool ou 500 L de boissons (111-0 G) et pour le vinaigre (111-0 H).
- Conservation (L. 102 B LPF).
- Autorisation des procédés spéciaux (302 D bis I b, 289 2°) et procédés de dénaturation totale reconnus (règlement (CE) n° 3199/93, cité par CIBS L313-7).

**Lacune résiduelle.** Disparaît l'outil d'exclusion prospective : le retrait motivé du numéro en cas de manquement (111-0 F source). Le fournisseur perd aussi un moyen simple de vérifier l'éligibilité avant livraison. Cela peut le pousser à exiger des attestations privées, ce qui créerait de fait une formalité de remplacement.

**Conclusion provisoire.** Je ne vois pas d'incompatibilité apparente avec le droit de l'Union. Les identifiants européens autonomes (numéros d'accise, DAE, DSA/DAES, destinataires enregistrés, expéditeurs ou destinataires certifiés) ne sont pas touchés et doivent rester distincts. À confirmer par la lecture d'EUR-Lex (articles 27 de la directive 92/83/CEE et régime de 2020/262).

### RT-INUT-07 (P2, coordination manquante, confirmé) : la transition est hétérogène et incomplète

**Formules actuelles.**
- 302 D bis : « dès l'entrée en vigueur de la loi qui les prévoit … aux demandes en cours, sans nouveau dépôt ».
- 111-0 E et F : « à compter de l'entrée en vigueur de la réforme ».
- 50-0 H : « formalités accomplies à compter de l'entrée en vigueur de la réforme ».

**Points non traités.**
- (a) Le sort des **numéros déjà attribués**. Ils figurent sur les documents en circulation, les listes clients, la base SOPRANO UT et les licences « UTI » citées par la douane.
- (b) Les **décisions de refus ou de retrait** de numéro, prononcées ou en cours.
- (c) Les **déclarations en cours d'instruction**. Seul 302 D bis les traite.
- (d) Les **opérations antérieures** dépourvues de numéro : régularisations, rappels non prescrits.
- (e) Les **sanctions** liées au seul défaut de déclaration.
- (f) Les **modèles I à III de l'arrêté du 4 juillet 2005** (JORFTEXT000000632265), hors corpus et non obtenus.

Il faut une clause commune, sans supprimer les droits et exonérations antérieurs ni les échéances anciennes.

### RT-INUT-08 (faux positif) : identifiants et déclarations autonomes à ne pas confondre

Les éléments suivants ne relèvent pas du circuit IN/UT et ne doivent pas être supprimés par assimilation :
- le « numéro d'accises » de l'intermédiaire entrepositaire agréé (50-0 H 5° a 1) ;
- l'exigence d'entrepositaire agréé du fournisseur (111-0 E I 1°) ;
- les « identifiants exigés sur un autre fondement pour la circulation » (111-0 E I 4° b) ;
- les numéros d'agrément de 289 27° et 67° ;
- les expéditeurs et destinataires certifiés de 289 70° ;
- la déclaration de profession des marchands de billets (annexe IV 130, abrogée par son propre projet) ;
- la déclaration de profession du fabricant de marques fiscales (annexe IV 54-0 H, maintenue avec caution).

### RT-INUT-09 (alerte écartée) : textes voisins cohérents

- Annexe I 181 proposé abroge la déclaration des locaux de commerce des alcools dénaturés par procédé général. C'est cohérent avec 302 D bis III, qui supprime la déclaration pour « le commerce des alcools totalement dénaturés ».
- 111-0 G et 111-0 H renvoient « en plus des formalités et obligations fixées à l'article 111-0 F ». F proposé conserve des obligations réelles (conservation, justification, stockage séparé) et non le numéro : pas de renvoi vide.
- CGI 458 1° (affranchissement des formalités de circulation des alcools totalement dénaturés) est une faveur autonome à conserver.

## 5. Propositions de correction (présentées séparément)

Ces propositions forment un **paquet couplé** : C1 à C5 doivent être intégrés ensemble. C6 et C7 sont des coordinations hors corpus. Elles ne créent aucune formalité de remplacement.

### C1. Annexe IV 50-0 H : abrogation opératoire (corrige RT-INUT-01 et RT-INUT-07)

Texte complet proposé :

> Le présent article est abrogé à compter de l'entrée en vigueur de la réforme.
>
> À compter de cette date, aucune déclaration préalable de profession, aucune pièce jointe, aucun exemplaire ni aucun modèle établi selon les annexes I à III de l'arrêté du 4 juillet 2005 ne peut être exigé des intermédiaires mentionnés au 2° du II de l'article 111-0 E ni des utilisateurs mentionnés à l'article 111-0 F de l'annexe III au code général des impôts. Les déclarations en cours d'instruction deviennent sans objet, sans nouveau dépôt.
>
> Aucun numéro d'identification « IN » ou « UT » n'est plus attribué. Les numéros déjà attribués n'ont plus à être portés sur les documents d'accompagnement, documents économiques, listes ou déclarations ; leur mention éventuelle est sans effet. Leur absence, leur caducité ou leur retrait ne peut fonder un refus d'exonération pour les opérations réalisées à compter de cette date, sans préjudice du contrôle des conditions de fond.
>
> Le numéro d'accise attribué à l'entrepositaire agréé, les identifiants exigés pour la circulation des produits soumis à accise et les autorisations de procédés de dénaturation demeurent régis par leurs dispositions propres.
>
> Les opérations réalisées avant cette date demeurent régies, pour l'établissement des droits, par les dispositions qui leur étaient applicables, sous réserve de l'application de la loi répressive plus douce aux sanctions ayant le caractère de punition. Les pièces déjà soumises à conservation demeurent conservées dans les conditions de l'article L. 102 B du livre des procédures fiscales. Aucune attestation, déclaration ni registre de remplacement n'est institué.

Justification : aligne l'arrêté sur le décret (111-0 E/F) et la loi (302 D bis III) ; préserve les identifiants autonomes et les échéances anciennes. Dépendances : C2, C3 ; motif et notes de 50-0 H à réécrire.

### C2. Annexe IV 50-0 G : réécriture (corrige RT-INUT-02)

Texte complet proposé :

> Pour l'application du 3° du I de l'article 111-0 E de l'annexe III au code général des impôts, les données d'identification des destinataires tirées des documents commerciaux ou des enregistrements de vente du fournisseur comportent le nom ou la raison sociale, l'adresse et l'activité professionnelle des personnes définies au 2° du II de l'article 111-0 E et à l'article 111-0 F de la même annexe. Aucun numéro d'identification issu d'une déclaration préalable de profession n'y est exigé. Ces données n'ont pas à être reprises dans une liste distincte de ces documents ou enregistrements.
>
> Les listes établies avant l'entrée en vigueur de la réforme et comportant un tel numéro restent conservées dans les conditions de l'article L. 102 B du livre des procédures fiscales, sans avoir à être complétées ni corrigées.

Statut à changer : `retained_unchanged` devient `rewrite_draft`. Le motif doit dire que la rubrique a reste la preuve ordinaire de destination et que la rubrique b disparaît avec le circuit retiré. Il s'agit de la même mesure que C1 : pas de gain supplémentaire compté.

### C3. Annexe II 289 : 15° (corrige RT-INUT-03)

Remplacer le 15° par :

> 15° (Sans objet) ;

Tout le reste de la proposition est conservé, y compris le 2°, le 5°, le 67°, le 70° et le dernier alinéa. Les opérations antérieures restent couvertes par ce dernier alinéa : « Les références à des dispositions abrogées ne valent que pour les opérations antérieures ».

### C4. CGI 302 D bis III : resserrement (corrige RT-INUT-04, partiellement)

Remplacer le III proposé par :

> III. – Le bénéfice des exonérations prévues aux I et II et le commerce des alcools totalement dénaturés mentionnés au a du I ne sont subordonnés à aucune déclaration préalable de profession ni à l'attribution, à la détention ou à la mention d'un numéro d'identification délivré à la suite d'une telle déclaration. Les dispositions prises pour l'application du présent article ne peuvent rétablir ces formalités. Les procédés de dénaturation et les conditions d'utilisation prévus aux I et II demeurent applicables. Leur respect peut être établi, lors des contrôles légalement prévus, par les pièces ordinaires d'achat, de fabrication ou d'utilisation et les données légalement disponibles, sans attestation ni registre de remplacement. Les statuts, numéros d'accise et documents de circulation exigés sur un autre fondement demeurent régis par leurs dispositions propres.

Le IV et l'alinéa transitoire final proposés sont conservés sans changement. Dépendance : la seconde passe de 302 D bis est `pending`.

### C5. Annexe III 111-0 F : compléments (corrige RT-INUT-05 et RT-INUT-07)

Au I, après « … Les conditions de fond de l'article 302 D bis demeurent applicables. », insérer :

> La qualité d'utilisateur résulte de la seule réunion de ces conditions. Elle n'impose pas, à ce seul titre, le statut d'entrepositaire agréé pour la réception sur le territoire national de produits expédiés en exonération par un fournisseur mentionné à l'article 111-0 E, sous réserve des statuts et documents exigés pour la circulation entre États membres de l'Union européenne.

À la fin du dernier alinéa, ajouter :

> Les numéros d'identification déjà attribués cessent d'être exigés. Les décisions de refus ou de retrait de numéro, prononcées ou en cours, sont sans effet sur les opérations réalisées à compter de l'entrée en vigueur de la réforme, sans préjudice du contrôle des conditions de fond et des droits relatifs aux opérations antérieures.

Dépendance : la portée de la première phrase sur le statut d'entrepositaire dépend du régime de redevabilité du CIBS (C6). À défaut de base suffisante, elle doit être portée au niveau législatif.

### C6. Hors corpus : disposition législative autonome rattachée au CIBS (RT-INUT-04 et RT-INUT-05)

Article non codifié de la loi de réforme, ou article du CIBS dans la sous-section des exonérations :

> Le bénéfice des exonérations prévues aux articles L. 313-7 à L. 313-14 du code des impositions sur les biens et services n'est subordonné à aucune déclaration préalable de profession ni à l'attribution d'un numéro d'identification délivré à la suite d'une telle déclaration. Les dispositions réglementaires prises pour leur application ne peuvent rétablir ces formalités. Les personnes qui reçoivent des produits exonérés pour un usage mentionné à ces articles ne sont pas tenues, à ce seul titre, d'obtenir le statut d'entrepositaire agréé, sous réserve des statuts exigés par le droit de l'Union européenne pour la circulation entre États membres. Les conditions de fond, les procédés de dénaturation autorisés et les contrôles demeurent applicables.

Cette disposition garantit la suppression au-delà de la prise d'effet de l'abrogation différée de 302 D bis. Elle est à vérifier sur le CIBS figé au 18 octobre 2026 et sur le décret visé à L. 311-39.

### C7. Hors corpus : arrêté du 4 juillet 2005 (RT-INUT-07)

Abroger les annexes I à III (modèles de déclaration préalable de profession) à la même date. Réserve : l'arrêté n'a pas été obtenu (403), ni son contenu exact, ni l'existence d'une éventuelle autre annexe. Le formulaire mensuel vinaigre relève de MENS.

## 6. Ce qu'il faut préserver

- Les exonérations des I, II et IV de 302 D bis et leurs chiffres : NC 2209 ; 1,2 % vol. ; 8,5 L et 5 L d'alcool pur par 100 kg.
- La preuve ordinaire de destination (50-0 G a, 111-0 E I 3°).
- Les marquages alimentaires et la dispense « ECHANTILLON ».
- Le statut d'entrepositaire agréé du fournisseur et ses numéros d'accise.
- Les documents de circulation et les identifiants européens.
- Les autorisations spéciales de procédé (302 D bis I b, 289 2°, annexe I 165 à 186 selon A1DOSSIER).
- L'affranchissement des formalités de circulation de 458 1°.
- Les droits, exonérations et remboursements des opérations antérieures, les pièces sous conservation et les échéances anciennes.
- La loi répressive plus douce.
- Aucune formalité de remplacement.

## 7. Incertitudes et éléments non examinés

- Les textes d'EUR-Lex (92/83/CEE, en particulier l'article 27 et sa modification par la directive 2020/1151, et 2020/262) n'ont pas été obtenus. L'analyse européenne est provisoire.
- Les articles 10 et 38 de l'ordonnance 2021-1843, le décret visé à L. 311-39 et le CIBS figé au 18 octobre 2026 n'ont pas été obtenus. La version affichée du CIBS date du 18 mars 2026 et certains articles y sont bornés au 1er janvier 2027, ce qui est postérieur au gel.
- L'arrêté du 4 juillet 2005 et ses modèles, ainsi que le décret 2006-356 (article 3) et l'arrêté du 24 mars 2006, n'ont pas été obtenus.
- Je n'ai obtenu ni l'article 185 de la LFI 2020 ni l'article 55 de la LFR 2020 eux-mêmes : seule la version LEGI mort-née et l'exposé de l'amendement 534 en témoignent.
- Le régime de redevabilité du fournisseur en cas de détournement par le destinataire (risque de demande d'attestations privées) n'a pas été instruit. Il relève du CIBS.
- La page de la douane n'est pas datée et n'est pas normative.
- Je n'ai pas fait d'inventaire exhaustif des formulaires et téléservices (SOPRANO UT, licences « UTI »). La page de la douane mentionne aussi un « numéro de fournisseur (FA) ». Une recherche dans la base (sources et propositions) ne le trouve dans aucun texte du corpus : son fondement, sans doute administratif ou réglementaire hors corpus, n'est pas établi. Il ne doit pas être supprimé ni recréé par assimilation.
- Les historiques de 289 n'ont été lus que par différentiel.
- Annexe I 165, 185 et 186 : voir A1DOSSIER. Annexe III 111-0 H 2° et annexe IV 50-0 I II : voir MENS.
