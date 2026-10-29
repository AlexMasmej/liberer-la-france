# Réexamen ALERTS : alertes P1 écartées dont les textes ont changé

Instantané ancien : `20261026T230545Z` (exports `evidence/cited/20261026T230545Z/`). Instantané courant : `20261027T044303Z` (lu par `tools/cite.py`, exports `evidence/cited/20261027T044303Z/`). Seconde passe arrêtée (`blocked`) : les propositions dont l'inventaire est `pending` peuvent encore changer. Revue IA : elle ne vaut pas validation par un juriste.

## Synthèse

Le paquet compte 80 alertes, toutes classées « alerte écartée » sur l'ancien instantané. Il ne contient aucune objection du registre (`objections` : vide).

| Classification nouvelle | Alertes | Objection |
|---|---|---|
| alerte écartée | 77 | — |
| incohérence du projet | 2 | RT-RXALERTS-01 (nouvelle, P2, à confirmer) |
| coordination manquante | 1 | RT-RXALERTS-02 (nouvelle, P2, confirmé) |

Les deux nouvelles objections viennent du même mouvement. La seconde passe a amélioré la transition d'une cible : couverture SGA acquise, absence de refus de formalité pour le stock. Le texte qui y renvoie, resté inchangé, n'a pas suivi. Il est désormais plus sévère que la cible pour le stock ancien.

Pour les 77 autres alertes, les changements des cibles vont dans le même sens et confortent le classement « écartée ». La plupart des cibles ajoutent une clause : le maintien du régime des années ou cessions antérieures « ne fait pas obstacle » aux allègements de formalités prévus par les annexes. Plusieurs cibles ajoutent aussi une coordination explicite avec les textes qui y renvoient : 1599 quater D et TSE pour 220 Z septies, 1586 ter pour 1586 quinquies et sexies, 796-0 bis et ter pour 990 I bis, 302 bis ZN pour 344 GD, 1519 G pour 1649 A quater et 328 P. Trois textes qui renvoient ont été bornés : 900 B, 1382-0 IV et 792-0 bis.

Le drapeau `target_proposal_changed` du paquet compare l'état courant à l'audit, pas à l'ancien instantané. Entre les deux instantanés, quatre cibles n'ont changé que dans leurs motifs ou notes, sans changement de proposition : 641, 636, 893 et 1530. Leurs alertes restent écartées.

## Méthode

1. J'ai exporté par `cite.py` les 84 articles du paquet (textes qui renvoient et cibles), plus L453-1 et L453-3 du CCH pour le contexte.
2. Pour chaque article, j'ai comparé l'export ancien et l'export nouveau : statut, empreintes de proposition, de motif et de notes. J'ai produit un diff par phrase.
3. J'ai lu en entier, sur le nouvel instantané, la proposition (ou la source, si l'article est `retained_unchanged`), le motif et les notes de chaque texte qui renvoie et de chaque cible.
4. J'ai qualifié chaque alerte selon `BRIEF-P1.md`. La question posée est la même : le renvoi vers une disposition abrogée par le projet pose-t-il désormais un problème réel ?
5. J'ai vérifié les doublons dans `reports/register.json` : aucune objection existante sur R662-1 ou R261-24-1, ni sur 317 B ou le refus de formalité de 1529. Plusieurs objections touchent des articles du paquet sur d'autres effets (RT-P1-CGI-C-01, C-02, C-05, C-09, B-05, B-06, RT-DOMCVAE-02, RT-FUTFISC-01, 13, 14, RT-DOMSRU-01, RT-DOMSUCC-01, 02, 06). Elles figurent dans `packets.json` et sont réexaminées par d'autres groupes. Je ne les requalifie pas.

## Périmètre réellement lu (nouvel instantané, comparé à l'export ancien)

- **Annexe II** : 311 A, 311 B, 311 C, 317 A, 317 B.
- **Annexe III** : 255, 313 BG bis, 328 K, 328 M, 328 O, 328 P, 331 K bis, 331 K ter, 344 GD, 344 quindecies.
- **Annexe IV** : 121 K ter, 155-0 bis, 155-0 ter, 155-00 ter (ces trois derniers retenus inchangés).
- **CGI** :
  - IFER : 1519, 1519 D, E, F, G, H, HA, 1599 quater A, A bis, B.
  - TSE et taxe additionnelle francilienne : 1599 quater D, 1607 bis, 1607 ter, 1609 B, C, D, G, H.
  - Taxes sur les terrains devenus constructibles : 1529, 1605 nonies.
  - CVAE : 1586 ter, quinquies, sexies.
  - 990 D, 990 FA, 990 I bis, 796-0 bis, 796-0 ter.
  - 641, 636, 662, 719, 722 bis, 724, 792-0 bis, 893, 900 B, 916 A.
  - 1135 bis, 1840 G ter, 1382-0, 1396, 1530, 1601, 1601-0 A.
  - 302 bis MB, 302 bis ZN, 1693 bis, 1681 septies, 1656 quater, 1964, 220 Z septies.
- **CSS** : L862-4-1, R862-13-1, R862-11-3, L241-2, L213-1.
- **CCH** : R261-24-1, R662-1, R302-16, R302-16-1, R302-17, R302-18, R302-19, R374-1, ainsi que L453-1 et L453-3 pour le contexte.

`ALERTS.json` (`articles_read`) donne, pour chacun, l'identifiant LEGIARTI de la version et l'empreinte de la proposition nouvelle. Les textes qui renvoient restent dans l'inventaire de seconde passe `pending` : R662-1, R374-1, 1656 quater, 1681 septies, 1693 bis, 1840 G ter, 1964, R862-11-3 et R862-13-1.

## Constats

### RT-RXALERTS-01 : R662-1 (Polynésie) exclut R261-24-1 plus largement que sa propre transition (P2, incohérence du projet, à confirmer)

Alertes 84e6ff8c… et 47b7ee06….

- **Avant.** R261-24-1 proposé retirait la justification par la garantie SGA pour tous les contrats conclus après la réforme. R662-1 l'excluait en Polynésie pour les « contrats nouveaux » : les deux textes concordaient.
- **Maintenant.** R261-24-1 maintient cette justification pour une opération déjà couverte, « y compris lorsque la vente est conclue après cette date ». Il s'aligne ainsi sur L453-1 proposé, qui interdit d'« exiger une garantie de remplacement ».
- **Divergence.** R662-1 (inchangé, `pending`) exclut toujours R261-24-1 pour tout contrat conclu après la suppression. Ses propres notes de cible le signalent : « étendre la réserve des opérations déjà garanties [...] dans l'exclusion territoriale de R. 662-1 proposée, actuellement fondées sur la seule date du contrat ».
- **Conséquence possible.** En Polynésie, la couverture acquise serait perdue pour les ventes postérieures, avec une garantie de remplacement imposée.
- **Effet pratique incertain.** L'applicabilité de R261-24-1 en Polynésie n'est pas établie : il a été créé en 2019, alors que la plage de R662-1 date de 2000 (spécialité législative). L'existence d'organismes HLM garantis par la SGA y est aussi douteuse.

### RT-RXALERTS-02 : 317 B (annexe II) garde, pour les cessions antérieures, un refus de formalité que 1529 exclut désormais (P2, coordination manquante, confirmé)

Alerte 756e35be….

- **Ajout dans 1529.** 1529 proposé comporte un nouvel alinéa : « Pour les dépôts et formalités présentés à compter de l'entrée en vigueur de la présente loi, y compris lorsqu'ils concernent une cession antérieure, l'absence de la déclaration ou des mentions exclusivement relatives à cette taxe [...] ne peuvent justifier un refus de dépôt, d'enregistrement ou de formalité fusionnée. »
- **317 B inchangé.** 317 B maintient pour les cessions antérieures « les dispositions alors applicables, y compris [...] obligations déclaratives ». Son I subordonne « l'accomplissement de la formalité » aux mentions.
- **Effet.** La loi l'emporte, mais le décret garde un motif de refus devenu inopérant. Il y a un risque de refus erronés pour le stock ancien.

### Alertes écartées

Les 77 motifs, un par finding_id, figurent dans `ALERTS.json`. Ils se répartissent en sept groupes.

- **Redevances des mines (311 A, B, C).** L'ajout dans 1519 (produits de l'année précédente, relevés nominatifs) reprend la règle déjà écrite dans les annexes.
- **Terrains devenus constructibles (317 A, 255, 331 K bis, 331 K ter).** 1605 nonies réserve désormais expressément les allègements de 331 K bis et K ter. 255 ne vise les mentions que « le cas échéant », sans refus. Un toilettage est possible, comme le demandent les notes de 1605 nonies.
- **Déclarations IFER (328 K, M, O, P ; 155-0 bis, 155-0 ter, 155-00 ter).** Les annexes sont abrogées à la même bascule et ne servent qu'aux années anciennes. Les cibles réservent ces allègements. Les définitions de l'annexe IV n'imposent aucune obligation ; leur motif de rétention, qui suppose l'IFER maintenue, est périmé, sans effet.
- **TSE et taxe additionnelle (1396, 220 Z septies, 1607 bis, 1656 quater).** Les cibles ajoutent qu'aucun montant fictif d'une taxe supprimée n'entre dans une créance ou un plafonnement, et que l'identité des organismes reste utile aux avantages distincts.
- **Successions (990 I bis, 662, 792-0 bis, 1840 G ter).** Les renvois restent bornés aux décès antérieurs ou sont neutralisants. 1135 bis réserve les allègements de 1840 G ter.
- **Autres textes fiscaux.**
  - 313 BG bis et 916 A, 1964 et 724, 1693 bis et 302 bis MB : renvois au seul stock ancien.
  - 121 K ter, 1681 septies et 990 FA vers 990 D : idem.
  - 344 GD et 302 bis ZN, 344 quindecies et 1586 ter, 1586 quinquies et sexies : idem.
  - 1382-0, désormais borné ; 1601-0 A et 1601 ; 722 bis et 719 ; 900 B, désormais réécrit.
- **CSS et CCH.** Les renvois à L862-4-1 sont bornés aux années encore dues. R374-1 (exclusion mahoraise) est expressément voulu par les cibles SRU, qui demandent de le maintenir.

## Propositions de correction (présentées séparément)

**RT-RXALERTS-01, R662-1, dernier alinéa proposé.**

> L'exclusion de l'article R. 261-24-1 s'applique aux contrats conclus à compter de l'entrée en vigueur, en Polynésie française, de la suppression de la garantie de la société de garantie des organismes d'habitations à loyer modéré pour les opérations nouvelles, sauf lorsque le contrat porte sur une opération valablement couverte avant cette date par cette garantie ; l'article R. 261-24-1 demeure alors applicable dans les conditions transitoires qu'il prévoit et dans les limites de la couverture acquise. Les contrats et garanties valablement conclus auparavant et les droits qui en découlent sont conservés. Cette exclusion ne supprime ni les garanties générales applicables aux ventes d'immeubles à construire ni les adaptations territoriales prévues au présent article.

Au premier alinéa, remplacer « pour les contrats nouveaux mentionnés ci-dessous » par « pour les contrats mentionnés au dernier alinéa ».

- **Justification** : alignement sur R261-24-1 et L453-1 proposés ; préserve la couverture acquise, sans garantie de remplacement.
- **Dépendances** : applicabilité réelle en Polynésie (option alternative : retirer l'exclusion comme sans objet) ; critère de date du contrat dans L453-3 proposé, à vérifier.

**RT-RXALERTS-02, 317 B, troisième alinéa proposé.**

> Les cessions réalisées avant cette date demeurent régies par les dispositions alors applicables, y compris les exclusions de champ, exonérations, dispenses, obligations déclaratives, contrôles, garanties, restitutions, prescriptions et recours. Toutefois, pour les dépôts et formalités présentés à compter de l'entrée en vigueur de cette loi, y compris lorsqu'ils concernent une cession antérieure, l'absence des mentions prévues au I ou des justificatifs prévus aux II et III ne peut justifier un refus de dépôt, d'enregistrement ou de formalité fusionnée ; ces mentions et justificatifs restent dus dans la seule mesure où l'article 1529 du code général des impôts les maintient pour ces cessions. Aucun remboursement général des sommes légalement dues n'est institué. L'application de la loi répressive plus douce aux sanctions non définitives demeure réservée.

- **Justification** : reporter dans le décret la règle de procédure favorable ajoutée par la loi ; conserver dettes et exonérations du stock.
- **Dépendances** : 150 VG et 150 VH (coordination signalée par les notes de 1529, non relue ici) ; choix différent pour 1605 nonies, qui garde les mentions requises pour le stock.

## Observations utiles aux autres groupes (sans verdict de ma part)

- 1519 G ferme désormais expressément, pour les années supprimées, la déclaration de 1649 A quater, celle de 328 P et l'amende de 1736 VI. À confronter à RT-P1-CGI-C-02.
- 1519 ajoute : « Aucun relevé nominatif des ouvriers ou employés [...] n'est exigé ». Ses notes signalent que 121 sexies (annexe IV) conserve une collecte annuelle générale. À confronter à RT-P1-CGI-B-05.
- 990 D réserve les simplifications de 990 E, 990 F et 990 FA, et indique avoir corrigé la contradiction avec les brouillons de 990 E et 990 F. À confronter à RT-P1-CGI-C-09.
- 1586 ter maintient expressément les définitions de 1586 quinquies et 1586 sexies pour 1647 B sexies. À confronter à RT-FUTFISC-14 et RT-DOMCVAE-02 (leurs bornes LEGI de 2029 et 2030 ne sont pas traitées par cet ajout).
- Notes périmées sans effet normatif. 792-0 bis note que « 641 [n'est] pas réécrit », alors qu'il l'est. 220 Z septies note que 1599 quater D, 1607 bis et ter et 1609 B à H ne sont « pas réécrits », alors qu'ils sont abrogés à la même bascule.

## Incertitudes et éléments non examinés

- Aucune source primaire en ligne n'a été consultée : tout repose sur l'instantané.
- Les textes extérieurs aux neuf recueils n'ont pas été lus : loi 2010-597, décret 55-22, code des transports, CPCE, texte d'extension polynésien, etc.
- Les articles cités par les cibles hors du paquet n'ont pas été relus en entier : 150 VG, 150 VH, 1635-0 quinquies, 1649 A quater, 1736, 121 sexies, 990 E, 990 F, L261-10 à L261-11.
- Les textes qui renvoient restés `pending` peuvent encore être réécrits.
- Revue IA : elle ne vaut pas validation par un juriste.
