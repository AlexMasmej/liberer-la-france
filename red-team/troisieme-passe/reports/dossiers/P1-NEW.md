# Dossier P1-NEW : abrogations apparues depuis l'audit du 25 octobre

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z`, corpus daté du 18 octobre 2026.
Ce rapport est une revue par IA, sans valeur de validation par un juriste. Ses conclusions sont provisoires : la seconde passe continue en production, et les propositions peuvent encore changer.

## 1. Périmètre réellement lu

### 1.1 Les 26 cibles (`reports/repeal-delta-since-audit-20261026T230545Z.json`, clé `new`)

Chaque cible a été lue en entier avec `tools/cite.py` : source, NOTA, bornes, proposition, motif, notes, lot et statut d'inventaire. Toutes ont un brouillon `rewrite_draft`, sont en VIGUEUR depuis la date indiquée jusqu'au 2999-01-01, et ont un inventaire `completed`.

| Code | Numéro | LEGIARTI | Renvois entrants réels après vérification |
|---|---|---|---|
| travail | L2141-7-1 | 036773159 | 3 plages L. 2141-5 à L. 2141-8 (écartées) ; CASF L344-2-6 (réserve, RT-04) |
| css | L434-21 | 006743079 | aucun |
| urba | R153-7 | 031720475 | aucun (4 homonymes CSS) |
| urba | R151-32 | 031720581 | aucun |
| urba | R142-3 | 031720715 | aucun courant (homonymes CCH, CSS ; liens LEGI historiques) |
| urba | R142-2 | 031720717 | aucun courant (homonymes CCH, CSS ; liens LEGI historiques) |
| urba | R123-15 | 031720822 | aucun (homonymes du code de l'environnement) |
| urba | R123-14 | 031720824 | aucun (homonymes environnement et CSS) |
| urba | R113-14 | 031721095 | aucun (homonymes CCH et code des assurances) |
| urba | R113-7 | 031721111 | **R113-8 (RT-01)** ; homonymes CCH et CRPA |
| urba | R113-6 | 031721113 | aucun |
| urba | R300-20 | 031764533 | aucun |
| urba | L520-4 | 031816516 | 39 renvois du chapitre L520/R520/A520 et CGI 302 septies B : 38 écartés, **L520-11 (RT-03)** |
| urba | R324-5 | 038366834 | aucun courant (R324-6 abrogé en 2011) |
| urba | R111-57 | 049387952 | R111-58 (renvoi supprimé, écarté) |
| urba | R111-24 | 054613385 | aucun courant (CCH R662-1 homonyme ; R150-1 historique) |
| cch | R126-1 | 043818553 | aucun |
| cch | R126-4 | 043818559 | **R184-8 (RT-02)** |
| cch | R126-24 | 043818615 | arrêté du 22 décembre 2021 (neutralisé, écarté) |
| cch | R126-23 | 043934809 | aucun |
| cch | R125-22 | 048521621 | aucun |
| cch | R125-23 | 048521625 | aucun |
| cch | R125-25 | 048521641 | aucun |
| cch | R125-27 | 048521659 | aucun |
| cch | R*125-28 | 048521666 | R125-29 (abrogé à la même date, écarté) |
| cch | R125-29 | 048521670 | R*125-28 (abrogé à la même date, écarté) |

### 1.2 Référents lus en entier

Textes lus en entier : la proposition pour un `rewrite_draft`, la source pour un `retained_unchanged`.

- Travail : L2134-2, L2146-2, L8113-5 (toutes versions).
- Urbanisme : R113-8, L113-4, R113-13. R113-4, R113-5, R113-9, R113-10, R113-11 et R113-12 ont été lus pour les dépendances. Également : R111-58 ; L520-1, L520-2, L520-3, L520-5 à L520-23 (dont L520-13-1, L520-20) ; R520-3, R520-9 à R520-18, R520-15-1 ; A520-1, A520-2, A520-4, A520-5, A520-6 ; versions courantes de R142-1 (LEGIARTI000043529837) et L142-1 (LEGIARTI000042017863) ; anciennes versions de R142-1, R142-4-1, R611-5, L142-1, R324-6, R150-1 et L520-13-1.
- CCH : R184-8, L126-6, L183-18.
- CGI : 302 septies B (version courante LEGIARTI000045917140).
- Homonymes : seul le contexte de citation a été lu, ce qui suffit à exclure l'identité de code (voir le motif de chaque ligne).

Les exports `cite.py` sont dans `evidence/cited/20261026T230545Z/`.

## 2. Méthode et limites

Script en lecture seule (`mode=ro`, `pragma query_only=1`) sur `corpus.sqlite`.

1. **Univers des textes** : les 30 314 lignes de `drafts`, avec la proposition si `rewrite_draft` et la source `articles.content_xml` si `retained_unchanged`. S'y ajoutent les articles VIGUEUR et VIGUEUR_DIFF sans brouillon (531), lus sur leur source. Les neuf recueils sont tous couverts, y compris CGI et annexes, ce qui permet de capter les renvois d'autres codes qui nomment le code cible.
2. **Citation préfixée exacte** : jeton `[LRDA]\s*\*?\s*\.?\s*\*?\s*<numéro>`, non suivi de `-` ou d'un chiffre. Le suffixe est donc exact (par exemple, L. 2141-7 ne capte pas L. 2141-7-1), et les formes « R*. 125-28 », « R.* », « R. » sont admises.
3. **Plages** « X à Y » de même préfixe, encadrant numériquement la cible (comparaison par tuple), par exemple L. 2141-5 à L. 2141-8 pour L. 2141-7-1.
4. **Numéro nu sans préfixe** : aucune occurrence pertinente.
5. **Attribution de code** : j'ai lu à la main chaque contexte (« du présent code », « du code de l'environnement », « du code des assurances », « du code de la sécurité sociale », etc.) et j'ai exclu les homonymes : 33 lignes `faux positif`, conservées pour la traçabilité.
6. **Liens canoniques LEGI** (table `documents`), pour toutes les versions de la cible (même code, même numéro) :
   - dans le XML de la cible, `LIEN sens="cible" typelien="CITATION"` désigne une citation entrante ;
   - dans le XML d'un autre article, `LIEN sens="source"` portant l'identifiant d'une version de la cible désigne aussi une citation entrante.

   Les liens `sens="cible"` relevés dans le XML des autres articles sont des citations **sortantes** de la cible ; ils ont été écartés. Les liens CONCORDANCE, CONCORDE et TXT_ASSOCIE (anciennes numérotations) ne sont pas des citations et n'ont pas été retenus. J'ai ensuite rapporté chaque lien historique à la version courante du même numéro pour vérifier si le renvoi y subsiste.
7. **Contrôle croisé** : une recherche brute par sous-chaîne sur les numéros des cibles a confirmé les résultats ; aucun renvoi manqué.

**Limites :**
- Les renvois implicites ne sont pas captés : « le délai prévu à l'article précédent », « la commission mentionnée ci-dessus », ou une simple reprise de l'objet. Exemples relevés dans les notes : CCH L721-1 4° et R721-1 imposent la même indication de dépenses d'énergie que R126-23 sans le citer, et CCH R125-24/26/30/31, R122-25 et R125-16-1 maintiennent l'agrément sans citer R125-22 à R125-29. Ces points relèvent de la coordination de fond des cibles et ne sont pas des renvois ; ils ne sont pas traités ici.
- Les textes hors des neuf recueils (CASF, arrêtés, décrets non codifiés, code forestier, code de l'environnement) ne sont connus que par leurs liens LEGI.
- Légifrance a répondu HTTP 403 le 2026-10-26. Je ne l'ai pas contourné.
- Les plages de plus de deux bornes ou d'écriture atypique (« et suivants ») ne sont pas développées : aucun « et suivants » ne visait une cible.

## 3. Constats

### RT-P1-NEW-01 (P1, incohérence du projet, confirmé) : R113-8 s'appuie encore sur R113-7 abrogé

- R. 113-7 proposé abroge la transmission du dossier au ministre, « y compris pour les demandes en cours ».
- L. 113-4 proposé prévoit une autorisation « accordée par arrêté du représentant de l'État dans le département », « sans décret individuel, sans transmission du dossier aux ministres pour décision », et un refus implicite de deux mois « à compter de la réception d'une demande complète ».
- R. 113-9, R. 113-10, R. 113-11 et R. 113-13 proposés sont déjà alignés sur ce dispositif.
- R. 113-8 réécrit dispose au contraire : « est accordée par décret, au vu du dossier transmis par le préfet en application de l'article R. 113-7 », avec un délai qui court « à compter de l'envoi du dossier par le préfet ».

Conséquence : deux autorités (décret ou arrêté) et deux points de départ du refus implicite coexistent dans le projet. Il en résulte un risque de délais de recours mal calculés et de contentieux de compétence. Les notes de R113-7 et de L113-4 annonçaient cette coordination hors lot ; elle n'est pas faite.

### RT-P1-NEW-02 (P2, coordination manquante, confirmé) : R184-8 sanctionne une déclaration abrogée

Le deuxième alinéa de CCH R184-8 (`retained_unchanged`, seconde passe `pending`) punit d'une contravention de quatrième classe le défaut de déclaration « dans les conditions prévues à l'article R. 126-4 ». Or R126-4 est abrogé, L126-6 III proposé supprime la déclaration et L183-18 proposé exclut toute sanction de ce défaut. Les notes de R184-8 sont antérieures à cette abrogation.

L'effet est limité : il n'y a plus d'élément légal, et L183-18 neutralise la sanction. Le texte maintenu reste néanmoins incohérent.

### RT-P1-NEW-03 (P2, incohérence du projet, confirmé) : L520-4, pivot transitoire, s'ouvre sur une formule d'abrogation

Les 38 autres renvois entrants vers L520-4 sont écartés : ils viennent d'articles eux-mêmes abrogés et ne visent le III, ou L520-4 « dans sa rédaction antérieure », que pour les faits générateurs antérieurs.

Le défaut est propre à la cible. Elle se déclare « abrogé[e] pour les faits générateurs intervenant à compter de » la date de la réforme, alors que son I (suppression de la taxe) et son IV (dispense de formalités) ne régissent que ces faits-là. L520-11 proposé invoque pourtant « la dispense du IV du même article ».

Aucune perte de droit n'est démontrée : L520-1 proposé porte la suppression et la dispense, et le III reste applicable aux faits anciens. La formule fragilise toutefois la lecture du III dont dépendent 21 articles législatifs.

### RT-P1-NEW-04 (P2, réserve documentaire, à confirmer) : CASF L344-2-6 cite L2141-7-1

Le XML LEGI de L2141-7-1 porte un lien CITATION entrant depuis CASF L344-2-6 (LEGIARTI000048586843, en vigueur différée). Ce texte est hors corpus et n'a pas été lu. La portée de l'abrogation sur ce renvoi externe n'est pas vérifiée.

### Alertes écartées notables (sans objection)

- **L2141-7-1** : les plages « L. 2141-5 à L. 2141-8 » (L2134-2, L2146-2, L8113-5) restent valides. L'article intercalaire disparaît, mais les bornes et l'objet de la plage demeurent. La plage pénale de L2146-2 est limitée aux dispositions « relatives à la discrimination syndicale ».
- **R126-24** : l'arrêté du 22 décembre 2021 est neutralisé par la clause de la cible (« ou de ses textes d'application »). Son abrogation formelle reste souhaitable mais n'est pas nécessaire en droit.
- **R111-57** : R111-58 a déjà retiré le renvoi.
- **R*125-28 / R125-29** : renvois croisés entre deux articles abrogés à la même date.
- **Faux positifs** (homonymes) : CSS R153-7, R142-2, R123-14 ; CCH R142-2/3, R113-7, R113-14, R111-24 ; code de l'environnement R123-7 à R123-23 ; code des assurances R113-14 ; CRPA R113-7.

## 4. Propositions de correction (séparées des constats)

### 4.1 RT-01 : nouvelle rédaction de C. urb. R113-8 (urba|LEGIARTI000031721109)

> L'autorisation de construire prévue au 2° de l'article L. 113-3 est accordée par arrêté du représentant de l'État dans le département, dans les conditions prévues à l'article L. 113-4. Aucun décret, aucune transmission du dossier aux ministres et aucun rapport ministériel ne sont exigés.
>
> Le silence gardé par le représentant de l'État dans le département pendant deux mois à compter de la réception de la demande complète vaut refus, dans les conditions prévues à l'article L. 113-4.
>
> La présente rédaction s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux demandes en cours dans les conditions transitoires de l'article L. 113-4. Lorsqu'un délai de deux mois avait commencé à courir à la suite de l'envoi du dossier par le préfet au ministre chargé de l'urbanisme, son terme initial est conservé, sans interruption ni recommencement. Les dossiers déjà transmis et les rapports déjà établis restent utilisables sans nouveau dépôt. Les décrets déjà intervenus et les refus devenus définitifs conservent leurs effets et leurs voies de recours.

- **Justification** : aligner le texte sur L113-4 proposé ; la transition reprend celle de L113-4.
- **Dépendances** : entrée en vigueur simultanée avec L113-4 et R113-7 ; R113-13 renvoie déjà à L113-4.
- **Option** : abroger R113-8 (aucun renvoi courant vers l'article d'urbanisme).
- **Préservé** : le refus implicite (pas de titre de défrichement tacite), le terme déjà engagé, les décrets antérieurs ; aucune formalité de remplacement.

### 4.2 RT-02 : nouvelle rédaction de CCH R184-8 (cch|LEGIARTI000043819581)

> Est puni de l'amende prévue pour les contraventions de la troisième classe le fait de ne pas souscrire la déclaration de la présence de termites prévue à l'article L. 126-4.
>
> Est puni de l'amende prévue pour les contraventions de la cinquième classe le fait de ne pas avoir procédé, en cas de démolition de bâtiment situé dans une zone délimitée par arrêté préfectoral, aux opérations d'incinération ou de traitement avant transport des bois ou matériaux contaminés par les termites, exigées au III de l'article L. 126-6.
>
> La récidive de la contravention prévue à l'alinéa précédent est punie conformément à l'article 132-11 du code pénal.
>
> La contravention de la quatrième classe sanctionnant le défaut de déclaration en mairie des opérations d'incinération ou de traitement avant transport, prévue par le présent article dans sa rédaction antérieure, est supprimée à compter de l'entrée en vigueur de la suppression de cette déclaration au III de l'article L. 126-6. Elle ne peut plus être prononcée pour des faits antérieurs non définitivement jugés, conformément aux règles d'application dans le temps de la loi pénale plus douce.

- **Justification** : coordination avec R126-4, L126-6 et L183-18 proposés.
- **Préservé** : les sanctions du défaut de déclaration de présence, du défaut de traitement et de la récidive.

### 4.3 RT-03 : première phrase de C. urb. L520-4 (urba|LEGIARTI000031816516)

Remplacer « Le présent article est abrogé pour les faits générateurs intervenant à compter de la date d'entrée en vigueur de la loi supprimant la taxe […], selon les dispositions suivantes. » par :

> La suppression de la taxe sur la création de bureaux, de locaux commerciaux et de locaux de stockage en Ile-de-France, à compter de la date d'entrée en vigueur de la loi qui la prévoit, est régie par les dispositions suivantes.

- Le I, le II, le III et le IV restent inchangés. L'article devient une disposition transitoire en vigueur, ce qui fait aussi disparaître l'alerte mécanique sur ses 39 renvois entrants.
- **Option** : supprimer le I et le IV (redondants avec L520-1) et faire renvoyer L520-11 à « la dispense prévue à l'article L. 520-1 ».
- **Préservé** : l'intégralité du III (exonérations, plafonnement de 30 %, imputations, remboursements, rescrits, prescriptions, recours, règles plus favorables de L520-20), sans aucune imposition de remplacement.

### 4.4 RT-04 : CASF L344-2-6

Lire le texte. S'il vise L2141-7-1, ajouter à la loi de réforme : « À l'article L. 344-2-6 du code de l'action sociale et des familles, la référence à l'article L. 2141-7-1 du code du travail est supprimée. » Aucune formalité de remplacement ; les droits syndicaux autonomes des travailleurs d'ESAT sont réservés.

## 5. Incertitudes et éléments non examinés

- Toutes les conclusions portent sur l'instantané. R184-8 est encore `pending`, et R113-8 pourra être corrigé en production.
- Textes externes non lus : CASF L344-2-6, arrêté du 22 décembre 2021 (CCH R126-24), décret 2015-1783 art. 12, décret 81-534 art. 5, loi 76-394 art. 28 (`read_in_full=false` dans la classification). Code forestier et code de l'environnement non lus.
- Coordinations de fond des cibles signalées par leurs propres notes, mais sans renvoi numéroté, non examinées : CCH L721-1 et R721-1 (indication de dépenses d'énergie, liée à R126-23) ; R125-24/26/30/31, R122-25 et R125-16-1 (agrément L122-12) ; conflit L113-4 / R113-12 sur le délai de cession ; R151-2 5° (L151-41) ; commerce L752-4 et cinéma L212-7/8 (R142-2/3) ; arrêtés locaux de classement (R126-1).
- Les renvois implicites, non numérotés, ne sont pas couverts par la méthode.
- Aucune cible ni aucun référent ne figure dans la liste des dossiers ouverts de l'addendum : rien n'est classé « couvert par dossier ».

## 6. Livrables

- `reports/dossiers/P1-NEW.json` : 4 objections.
- `reports/p1-work/P1-NEW-classification.jsonl` : 98 lignes (cible > référent), réparties en 61 alertes écartées, 33 faux positifs, 2 incohérences du projet, 1 coordination manquante et 1 réserve documentaire.
