# Dossier FUT-FISC : versions futures déjà publiées du CGI et de ses annexes face aux propositions de réforme

Red-team juridique indépendante, troisième passe. Instantané 20261026T230545Z ; date de référence du corpus : 18 octobre 2026. Rédaction : 26 octobre 2026. Ce rapport est une revue assistée par IA : il ne vaut pas validation par un juriste. La seconde passe continue en production, donc ses conclusions sont provisoires : plusieurs versions courantes sont encore « pending ».

Ce dossier documente, article par article et pour le CGI et ses annexes, l'objection transversale **RT-XCUT-01**. Le projet réécrit la rédaction en vigueur au 18 octobre 2026, alors que des rédactions futures sont déjà publiées.

## 1. Synthèse

- Périmètre : 178 entrées, soit 168 couples (130 `rewrite_draft`, 38 `retained_unchanged`) et 10 nouveaux numéros futurs. Elles se répartissent ainsi : CGI 172 entrées (163 couples et 9 nouveaux numéros), annexe II 5 entrées (4 couples et le nouveau numéro 310 HC), annexe III 1 couple.
- Qualifications : `sans effet` 113, `conflit de rédaction` 29, `réforme écrasée` 29, `déjà traité` 7.
- Par statut de la version courante : nouveau numéro / réforme écrasée : 4; nouveau numéro / sans effet : 6; retained_unchanged / sans effet : 38; rewrite_draft / conflit de rédaction : 29; rewrite_draft / déjà traité : 7; rewrite_draft / réforme écrasée : 25; rewrite_draft / sans effet : 69.
- Objections : 33 (P0 confirmé : 2, P1 confirmé : 17, P1 à confirmer : 5, P2 confirmé : 9).
- Lecture intégrale (proposition, motif, notes et version future) : 142 entrées sur 178. Le détail de chaque entrée figure dans le champ `read_scope` ; voir le § 7.

Constats les plus importants :

1. **Textes opératoires fondés sur une abrogation inexistante (RT-FUTFISC-23, P0 ; RT-FUTFISC-24, P1).** La seconde passe a lu l'état LEGI `ABROGE_DIFF` d'une version remplacée comme l'abrogation de l'article. Certaines propositions l'ont inscrit dans le texte normatif. Le V proposé de 150 VM déclare l'article réformé inapplicable « au-delà de sa date d'abrogation déjà prévue au 1er janvier 2027 ». 1840 P, l'annexe III 406 A 15, 87 A et l'annexe II 276 contiennent des clauses du même type.
2. **287, régime déclaratif de TVA (RT-FUTFISC-04, P0).** La proposition, rédigée sur la base 2026, rétablirait le régime simplifié annuel de 302 septies A, abrogé au 1er janvier 2027, et effacerait le régime trimestriel de la LF 2025.
3. **Prélèvements et formalités que des versions futures réédictent après la date probable de la réforme.** Sont concernés : la CSI étendue au livre foncier de Mayotte en 2029 (RT-FUTFISC-17), les barèmes CVAE et la TA-CVAE 2028-2029 (RT-FUTFISC-13), le droit fixe de procédure, la présomption de revenu, le délit de réitération, le droit de licence des débitants et la majoration de 1804 C en 2029 (RT-FUTFISC-18 à 22), l'amende de 5 % de 1788 A en 2030 (RT-FUTFISC-10). S'y ajoutent des charges que la recodification 2027 sort de l'article réformé : agrément de détaxe et sanctions transférés vers le nouvel article 1788 F et le CIBS (RT-FUTFISC-12), certificat de caisse et e-reporting (RT-FUTFISC-08, 09). Enfin, un nouveau numéro, 1496 ter, crée en 2029 une déclaration annuelle des loyers non examinée par le projet (RT-FUTFISC-26).

## 2. Méthode

- Lecture par `tools/cite.py` de toutes les versions des 161 numéros du paquet (exports dans `evidence/cited/20261026T230545Z/`), avec en complément des exports ciblés : 262-0 bis, 1418, 1729 C, 879, 273, 284, 302 septies A, 1586 quinquies, 1635 bis AD, 1649 quater F et G, entre autres. Pour chaque entrée, un fichier de travail dérivé à l'identique de l'instantané (même fonction `plain()`) réunit la proposition, le motif, les notes, la version future entière, la version courante, la NOTA, les liens modificateurs nouveaux et un diff mot à mot entre version courante et version future.
- Les 130 couples `rewrite_draft` ont été traités par date d'effet (2027-01, 2027-08, 2028-01, 2029-01, 2030-01, 2030-07, 2031-01, borne 2222-02-22), en sept lots regroupés par mécanisme. Six lots ont été confiés à des branches de l'agent, le lot B2, les retained_unchanged et les nouveaux numéros à l'agent principal. Les qualifications ont ensuite été harmonisées par l'agent principal.
- Grille : Δf désigne ce que change la version future et Δp ce que change la proposition.
  - `sans effet` : Δf ne touche pas ce que change la proposition. Le champ `rebase` vaut « report mécanique » si la proposition reproduit un passage que Δf modifie normativement, « aucun » sinon.
  - `réforme écrasée` : à sa date d'effet, la version future rétablit, maintient ou réédicte ce que le projet supprime.
  - `conflit de rédaction` : une fusion est nécessaire.
  - `déjà traité` : la proposition ou ses notes identifient la version future et la traitent correctement.
- **Règle d'harmonisation pour 2027.** Au 26 octobre 2026, la loi de réforme ne peut réalistement entrer en vigueur avant le 1er janvier 2027. Sa rédaction intégrale, ou son abrogation, emporte donc la version 2027 de l'article lui-même. Une version 2027 ne vaut `réforme écrasée` que si la charge survit hors de l'article réformé, dans le CIBS ou sous un nouveau numéro. Six couples, d'abord qualifiés `réforme écrasée` par les lots, ont été requalifiés : 1586 ter, 1804 C, 1788 A (2027), 1740 D, 1786 et 287. Le motif le signale. Pour 2027, le risque principal est inverse : la proposition, rédigée sur la base 2026, efface la coordination ou la faveur de 2027. Pour 2028-2031, la version future, publiée avant la réforme mais applicable après elle, peut l'écraser si l'instruction modificative est une réécriture. Une loi de finances 2027 entrant en vigueur le 1er janvier 2027 créerait une concurrence le même jour : ce point est réservé.
- Les bornes 2222-02-22 et 2999-01-01 ne sont pas traitées comme des dates normatives. Pour 39 quinquies G, la borne 2222-02-22 recouvre une date fixée par décret après décision de la Commission. Pour 87 A, 88 et 1736, 2030-01-01 est un plafond (« au plus tard »). Pour 81, 2029-01-01 est aussi un plafond.
- **Sources primaires.** La consultation de Légifrance pour l'ordonnance 2025-1247 (JORFTEXT000053091516), tentée le 26 octobre 2026, a été refusée (HTTP 403). Aucun contournement n'a été tenté. La nature des instructions modificatives (substitution ponctuelle ou réécriture) reste donc une réserve documentaire générale. Le CIBS et le CSP ne figurent pas dans le corpus.

## 3. Couverture : qualifications par date d'effet

| Date d'effet | sans effet | réforme écrasée | conflit de rédaction | déjà traité |
|---|---|---|---|---|
| 2027-01 | 86 | 4 | 19 | 5 |
| 2027-08 | 3 | 0 | 1 | 0 |
| 2028-01 | 0 | 2 | 0 | 1 |
| 2029-01 | 12 | 18 | 3 | 1 |
| 2030-01 | 5 | 4 | 5 | 0 |
| 2030-07 | 1 | 1 | 1 | 0 |
| 2031-01 | 2 | 0 | 0 | 0 |
| 2222-02 | 4 | 0 | 0 | 0 |

Les notes ou motifs lisent à tort `ABROGE_DIFF` comme une abrogation dans 64 entrées (champ `notes_misread_abroge_diff`). Le détail par entrée figure dans `reports/p1-work/FUT-FISC-classification.jsonl` : finding_id, qualification, objection, motif, lecture.

## 4. Constats (objections)

Chaque objection est détaillée dans `reports/dossiers/FUT-FISC.json` : articles avec empreintes, passages exacts, références, conséquences, corrections, éléments à préserver, incertitudes. Résumé :

| Id | Priorité | Statut | Nature | Objet |
|---|---|---|---|---|
| RT-FUTFISC-01 | P1 | confirmé | coordination manquante | Base de rédaction périmée : report des recodifications (TVA→CIBS 2027, CPP 2029, contributions douanières 2029) |
| RT-FUTFISC-02 | P1 | confirmé | risque juridique | 1741 : champ du délit de fraude figé sur 2026 (TVA hors champ après 2027), renvoi CPP 775 mort en 2029 |
| RT-FUTFISC-03 | P1 | à confirmer | coordination manquante | 220 Z septies : neutralisation des quotas visant un renvoi remplacé par L. 231-66 CIBS ; renvoi 284 II bis mort |
| RT-FUTFISC-04 | P0 | confirmé | incohérence du projet | 287 : régime déclaratif TVA de la LF 2025 effacé, régime simplifié abrogé réintroduit |
| RT-FUTFISC-05 | P1 | à confirmer | coordination manquante | 256 C : assujetti unique, dépôt mensuel 2027 et reprise CIBS, allègements du projet sans support |
| RT-FUTFISC-06 | P1 | à confirmer | coordination manquante | 99 : seuil de la faculté d'enregistrement d'après relevé bancaire transféré dans 302 septies A bis |
| RT-FUTFISC-07 | P2 | confirmé | simple alerte | Taxes abrogées par le projet que la version 2027 réécrit : pas d'écrasement, mais formulation et clause anti-renaissance au CIBS |
| RT-FUTFISC-08 | P1 | confirmé | coordination manquante | 1770 duodecies : certificat de caisse et amende de 7 500 € transférés à L. 216-40 CIBS |
| RT-FUTFISC-09 | P1 | confirmé | coordination manquante | 1788 D / 1788 E : e-reporting transféré à L. 216-47 et L. 216-48 CIBS ; montants réduits 2027 à appliquer ; renvois officiels erronés |
| RT-FUTFISC-10 | P1 | confirmé | risque juridique | 1788 A (2030-07) : réédiction de l'amende de 5 % et des registres, amende nouvelle de 2 c |
| RT-FUTFISC-11 | P1 | à confirmer | risque juridique | 289 bis (2030-07) : livraisons intra-UE dans le champ ; option papier du projet et droit de l'Union |
| RT-FUTFISC-12 | P1 | confirmé | coordination manquante | 1788 F (nouveau, 2027) : agrément de détaxe et sanctions que le projet supprime dans 262-0 bis |
| RT-FUTFISC-13 | P1 | à confirmer | risque juridique | CVAE et TA-CVAE : barèmes et taux 2027-2029 publiés, non neutralisés |
| RT-FUTFISC-14 | P1 | confirmé | coordination manquante | Plafonnement CFE : définitions 1586 quinquies et sexies abrogées en 2030 ; réécriture 1647 B sexies et 1647 B sexies A |
| RT-FUTFISC-15 | P2 | confirmé | simple alerte | CVAE : la mesure n'est qu'une accélération de la suppression légale de 2030 ; fusion des rédactions de 2030 |
| RT-FUTFISC-16 | P2 | confirmé | conflit de source | 1649 quater E et H : obligations des CGA/AGA ressuscitées en 2030 par la consolidation |
| RT-FUTFISC-17 | P1 | confirmé | coordination manquante | CSI : réédiction et extension au livre foncier de Mayotte au 1er janvier 2029 (880 à 881 M) |
| RT-FUTFISC-18 | P1 | confirmé | coordination manquante | 1018 A et 1100 : droit fixe de procédure pénale réédicté en 2029 |
| RT-FUTFISC-19 | P1 | confirmé | coordination manquante | 1649 quater-0 B bis : présomption de revenu réédictée en 2029 |
| RT-FUTFISC-20 | P1 | confirmé | coordination manquante | 1789 : délit de réitération réédicté en 2029 |
| RT-FUTFISC-21 | P1 | confirmé | coordination manquante | 568 : droit de licence des débitants de tabac réédicté en 2029 |
| RT-FUTFISC-22 | P1 | confirmé | coordination manquante | 1804 C : majoration de 0,2 % maintenue par les réécritures 2027 et 2029 |
| RT-FUTFISC-23 | P0 | confirmé | incohérence du projet | 150 VM : la proposition se déclare inapplicable après le 1er janvier 2027 |
| RT-FUTFISC-24 | P1 | confirmé | incohérence du projet | 1840 P, 406 A 15, 87 A, 1382-0 : clauses fondées sur une abrogation ou une extinction inexistante |
| RT-FUTFISC-25 | P1 | confirmé | risque juridique | Annexe II 276 (et 279, 280, 286 F) : agrément tabacs du décret 2026-612 au 1er août 2027 |
| RT-FUTFISC-26 | P1 | confirmé | coordination manquante | 1496 ter (nouveau, 2029) : déclaration annuelle des loyers non examinée ; amende maintenue par 1729 C |
| RT-FUTFISC-27 | P1 | confirmé | coordination manquante | Faveurs créées par versions futures à reporter (81 f, 39 quinquies G, lissage 1518 A quinquies A, 1788 A 2030, 200) |
| RT-FUTFISC-28 | P2 | confirmé | coordination manquante | Faveurs temporaires qui s'éteignent (JEII à impact 2029, Mayotte 2031) : rédiger en deux temps |
| RT-FUTFISC-29 | P2 | confirmé | incohérence du projet | 238 bis et 1729 B : déclaration des dons déjà abrogée par la loi 2026-403 |
| RT-FUTFISC-30 | P2 | confirmé | coordination manquante | 1518 A sexies : réduction et transmission contre actualisation et lissage 2027 |
| RT-FUTFISC-31 | P2 | confirmé | incohérence du projet | 302 bis ZL : transition renvoyant à des modalités abrogées en 2027 |
| RT-FUTFISC-32 | P2 | confirmé | conflit de source | Anomalies de source LEGI : versions de durée nulle, NOTA discordantes, bases anciennes, renvois morts, coquilles |
| RT-FUTFISC-33 | P2 | confirmé | anomalie d'inventaire | Inventaire : seconde passe sans versions futures ; ABROGE_DIFF lu comme abrogation ; nouveaux numéros non inventoriés |

### RT-FUTFISC-01 — Base de rédaction périmée : report des recodifications (TVA→CIBS 2027, CPP 2029, contributions douanières 2029)

*P1, confirmé, coordination manquante.* Effet certain à date connue (1er janvier 2027 pour la TVA, 1er janvier 2029 pour le CPP et les contributions douanières) : la réforme ne pouvant entrer en vigueur avant ces dates, toute proposition « ainsi rédigée » sur la base 2026 réintroduirait des renvois vers des articles abrogés ou effacerait la coordination publiée. Effet limité par article, mais très étendu.

Le projet réécrit les rédactions en vigueur au 18 octobre 2026. Or les ordonnances 2025-1247 et 2026-671 recodifient la TVA dans le livre II du CIBS au 1er janvier 2027 : renvois aux articles 256 à 298 du CGI remplacés, « taxes sur le chiffre d'affaires » remplacées par « taxes sur les biens et services », déclaration « sur l'annexe à la déclaration mentionnée au 1 de l'article 287 » remplacée par une constatation « dans les conditions prévues à l'article L. 161-1 », recouvrement par L. 180-1. L'ordonnance 2025-1091 recodifie le CPP au 1er janvier 2029 (« tribunal délictuel », renvois renumérotés). L'ordonnance 2026-671 substitue « contributions douanières » à « contributions indirectes » au 1er janvier 2029. Dans la plupart des couples, ces modifications ne touchent pas ce que la proposition change (qualification `sans effet`), mais la proposition reproduit à l'identique le passage modifié. La rédaction applicable à compter de la réforme doit donc être « proposition + modification future » (report mécanique). Sinon, une loi « ainsi rédigée » adoptée après la date d'effet ramènerait des renvois vers des articles abrogés au 1er janvier 2027 (256 A, 273, 278 sexies, 279, 293 B, 302 septies A) ou en sursis (257, 261, 271, 297 A, 279 bis). Cela peut affecter le champ de faveurs : abattement des artistes de 93, exonérations de 1042, 1115, 809 et 1594-0 G, crédit 200 quater. Dans quelques couples, la proposition a reformulé le passage et une fusion rédactionnelle est nécessaire : 80 (choix entre renvoi figé à l'ancien 261 et renvoi vivant à L. 213-82), 1509 (V visant « la cession mentionnée au I de l'article 257 »), 1609 sexvicies (franchise de 293 B ; contrôle de l'ANFA exposé à l'abrogation différée), 119 ter, 200 quater, 200 quater A, 207. La nature exacte des instructions modificatives (substitution ponctuelle ou nouvelle rédaction) n'a pas pu être vérifiée au JORF. Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Rebaser chaque proposition concernée sur la rédaction future publiée : reporter mot pour mot les passages modifiés par la version future que la proposition reproduit, sans autre changement (citations dans le fichier de classification). Pour les passages reformulés (80, 1509, 1609 sexvicies, 119 ter, 200 quater, 200 quater A, 207), adopter la rédaction fusionnée des fiches de lot. Dans la loi de réforme, viser l'article « dans sa rédaction en vigueur à la date de publication de la présente loi ».

**À préserver.** Faveurs dont le champ dépend des renvois (93, 31 f, 1042, 1115, 809, 1594-0 G, 200, 200 quater) ; Dates normatives des versions futures, à distinguer des bornes 2222-02-22 et 2999-01-01.

**Articles.** cgi 1042, cgi 1115, cgi 119 ter, cgi 1382-0, cgi 1383-0 B, cgi 1384 A, cgi 1384-0 A, cgi 1388-0, cgi 1391 E, cgi 1460, cgi 1468 bis, cgi 1509, cgi 1518 A quinquies, cgi 1594 F quinquies, cgi 1594-0 G, cgi 1609 sexvicies, cgi 1613 ter, cgi 1635 quater D, cgi 1635 quater I, cgi 1649 bis B, cgi 1656, cgi 1656 quater, cgi 1671, cgi 1698 D, cgi 1727, cgi 1737, cgi 1740 B, cgi 1744, cgi 1746, cgi 1750, cgi 1751, cgi 1751 A, cgi 1754, cgi 1756, cgi 1791-0, cgi 1920, cgi 1929 quater, cgi 1965 FA, cgi 199 novovicies, cgi 199 septvicies, cgi 200 quater, cgi 200 quater A, cgi 207, cgi 231 A, cgi 231 bis L, cgi 256-00, cgi 273, cgi 299 septies, cgi 302 bis P, cgi 302 bis S, cgi 302 bis U, cgi 302 bis WA, cgi 302 bis WB, cgi 302 bis WC, cgi 302 septies A bis, cgi 31, cgi 363, cgi 39, cgi 723, cgi 730 …

### RT-FUTFISC-02 — 1741 : champ du délit de fraude figé sur 2026 (TVA hors champ après 2027), renvoi CPP 775 mort en 2029

*P1, confirmé, risque juridique.* La proposition reproduit l'ancien champ du délit de fraude fiscale (« impôts visés dans la présente codification »). Adoptée telle quelle après le 1er janvier 2027, elle sortirait du délit général les impositions recodifiées au CIBS, TVA comprise. C'est une protection essentielle contre la fraude.

Le projet ne change que la peine complémentaire. Mais l'article étant réécrit en entier, la proposition fige le champ de 2026 et le renvoi à l'article 775 du CPP. La recodification de la TVA au CIBS fait sortir celle-ci des « impôts visés dans la présente codification » ; la version 2027 corrige précisément ce point. Les notes relèvent seulement que la version assignée prend fin au 2027-01-01. La NOTA de la version 2027 cite une « ordonnance n° 2026-1247 du 17 décembre 2026 » : c'est vraisemblablement une coquille pour 2025-1247 (anomalie de source).

**Correction minimale.** Rebaser la proposition : premier alinéa selon la version 2027 et renvoi au casier selon la version 2029, ou renvoi neutre au « bulletin n° 2 du casier judiciaire ». Voir la rédaction proposée.

**À préserver.** Peines principales et aggravées, coopération, poursuites L. 229 à L. 231 LPF ; Protection des crédits conventionnels.

**Articles.** cgi 1741

### RT-FUTFISC-03 — 220 Z septies : neutralisation des quotas visant un renvoi remplacé par L. 231-66 CIBS ; renvoi 284 II bis mort

*P1, à confirmer, coordination manquante.* La neutralisation des conditions de mixité ou de quotas voulue par le projet pour la créance d'IS des logements intermédiaires est accrochée à un renvoi que la version 2027 supprime. Effet probable : la condition supprimée pourrait subsister par la définition CIBS.

Les deux rédactions réécrivent le III. La proposition retire le 4° de 279-0 bis A, condition de mixité ou de quotas liée à la suppression des quotas SRU, et garde l'exception de location sans TVA. La version 2027 remplace tout le renvoi par la notion de logement locatif intermédiaire « au sens de l'article L. 231-66 » du CIBS, dont le contenu est hors corpus. Si cette définition reprend la condition de mixité, elle continuera de s'appliquer malgré la proposition. L'exception de location en exonération de TVA disparaît aussi du texte 2027 sans que l'on sache si L. 231-66 la reprend. La version 2027 de 220 Z septies, issue de l'ordonnance 2026-671, garde au IV un renvoi au II bis de l'article 284, abrogé au 1er janvier 2027 sans successeur, et à 279-0 bis A, alors que le III renvoie déjà au CIBS. Le CIBS fournit ailleurs le relais (1384-0 A 2027 : « le complément de taxe sur la valeur ajoutée devient exigible conformément à l'article L. 231-100 »). La proposition reproduit le même renvoi.

**Correction minimale.** Fusionner le III sur la base 2027 en ajoutant une neutralisation autonome des conditions supprimées par la loi sur les quotas, appréciée sur la définition CIBS, et rebaser le IV sur L. 231-100 CIBS (voir C3-04). Rédaction de passage dans C3-redactions.md.

**À préserver.** Vingt ans réduits des années d'exonération totale ; Remboursement immédiat des exonérés et PME ; Créances, cessions et nantissements antérieurs.

**Articles.** cgi 220 Z septies, cgi 279-0 bis A, cgi 284

### RT-FUTFISC-04 — 287 : régime déclaratif TVA de la LF 2025 effacé, régime simplifié abrogé réintroduit

*P0, confirmé, incohérence du projet.* Effet grave et certain dès l'entrée en vigueur si le texte est adopté tel quel : la réforme ne peut entrer en vigueur avant le 1er janvier 2027, et la proposition rétablirait alors un régime simplifié annuel renvoyant à l'article 302 septies A, abrogé à cette date. Elle effacerait aussi le régime trimestriel de la LF 2025. Il en résulte deux régimes déclaratifs incompatibles et l'impossibilité d'appliquer les renvois.

La version du 1er janvier 2027 remplace le régime simplifié annuel (déclaration annuelle et acomptes semestriels) par une déclaration trimestrielle sous 1 000 000 € / 1 100 000 €, supprime le 3 ter et le seuil de 4 000 €, mais garde l'autorisation du délai supplémentaire. La proposition, rédigée sur la version 2025, réécrit les mêmes 2 et 3. Elle supprime l'autorisation, ce qui est compatible avec l'objectif. Mais elle maintient le régime annuel du 302 septies A (abrogé au 1er janvier 2027), le 3 bis (15 000 €), le 3 ter et le seuil de 4 000 €. Une loi « ainsi rédigé » postérieure ferait revivre un régime abrogé, avec des renvois morts, et effacerait le régime trimestriel de la LF 2025. Si l'on se fie à la date d'effet de la LF 2025, la version 2027 rétablit à l'inverse l'autorisation que le projet supprime. La NOTA courante ajoute que 287 est abrogé par l'ordonnance 2025-1247 et maintenu seulement jusqu'à sa reprise réglementaire (L. 161-1 et L. 172-3 CIBS), hors corpus.

**Correction minimale.** Rebaser la proposition de 287 sur la version LEGIARTI000051190827. Ne garder que les gains qui subsistent : délai supplémentaire au choix, sans autorisation, pour les déposants mensuels, et transition. Supprimer les alinéas du régime simplifié annuel devenus sans objet, ou les réserver aux seuls exercices en cours au 31 décembre 2026 selon le VI de l'article 38 de la LF 2025. Porter la même règle dans la reprise réglementaire CIBS (L. 161-1, L. 172-3), hors corpus. Rédaction complète dans C3-redactions.md.

**À préserver.** Régime trimestriel de la LF 2025 et option mensuelle ; Exercices décalés en cours au 31 décembre 2026 (VI de l'article 38 LF 2025) ; Remboursements intermédiaires de crédits sur immobilisations (242-0 C, 242 septies J annexe II), à coordonner ; Délai de soixante jours en cas de cession, dont la version 2027 vise encore les entreprises « placées sous le régime simplifié ».

**Articles.** cgi 287, cgi 302 septies A

### RT-FUTFISC-05 — 256 C : assujetti unique, dépôt mensuel 2027 et reprise CIBS, allègements du projet sans support

*P1, à confirmer, coordination manquante.* La version 2027 impose le dépôt mensuel à l'assujetti unique, à l'opposé de l'allègement proposé. Les autres allègements (fin de l'engagement de trois ans, du 31 octobre et de la liste du 10 janvier) visent un article que la NOTA donne pour abrogé en 2027 au profit du CIBS : effet probable de perte de la réforme.

Δf et Δp portent sur la même phrase avec des effets opposés : la version 2027 rend le dépôt mensuel, la proposition veut ouvrir toutes les modalités de 287, y compris le trimestre. Or le « 2 de l'article 287 » de 2027 n'est plus celui que vise la proposition (seuil de 4 000 € supprimé, trimestre selon le chiffre d'affaires au 3). Le régime de l'assujetti unique passe en outre au CIBS (L. 234-2 visé par 231 A 2027 ; reprises L. 224-5, L. 161-1, L. 171-1, L. 224-10, L. 224-23 citées par la NOTA). Les suppressions du projet (engagement minimal, échéances, liste annuelle) resteraient dans un article CGI abrogé ou résiduel si elles n'y sont pas portées.

**Correction minimale.** Réécrire la phrase du 2 du III sur la base 2027 : « L'assujetti unique dépose ses déclarations de chiffre d'affaires selon les modalités prévues aux 2 à 3 bis de l'article 287 », supprimer « souscrite mensuellement » au 6, et rédiger la même modification et les suppressions du III dans les articles CIBS de reprise (hors corpus, à identifier) au lieu du seul CGI 256 C.

**À préserver.** Options, adhésions et dates d'effet acquises (IV proposé) ; Crédits antérieurs remboursables (6 du III) ; Indépendance des autres impôts (7 du III).

**Articles.** cgi 231 A, cgi 256 C

### RT-FUTFISC-06 — 99 : seuil de la faculté d'enregistrement d'après relevé bancaire transféré dans 302 septies A bis

*P1, à confirmer, coordination manquante.* Faveur en jeu : la faculté des petits exploitants BNC d'enregistrer à la date du relevé bancaire dépend d'un seuil que la LF 2025 art. 38 ramène au CGI au 1er janvier 2027 ; la proposition conserve l'ancien renvoi au CIBS. L'effet est probable si la proposition est adoptée telle quelle après 2027.

La LF 2025 transfère dans le c du III de l'article 302 septies A bis les seuils du régime simplifié, auparavant fixés par L. 162-4 du CIBS. La proposition de 99 reprend tel quel le renvoi au 2° de L. 162-4. Le contenu de L. 162-4 après le 1er janvier 2027 n'est pas dans le corpus : si le seuil n'y figure plus, la faculté favorable perd son critère d'accès.

**Correction minimale.** Remplacer le renvoi par « le seuil mentionné au troisième alinéa du c du III de l'article 302 septies A bis du présent code », en gardant la saisie périodique proposée. Voir C4-redactions.md, § 3.

**À préserver.** Saisie périodique et support commun introduits par la proposition ; Faculté de la date bancaire.

**Articles.** cgi 302 septies A bis, cgi 99

### RT-FUTFISC-07 — Taxes abrogées par le projet que la version 2027 réécrit : pas d'écrasement, mais formulation et clause anti-renaissance au CIBS

*P2, confirmé, simple alerte.* Pas d'effet normatif si la réforme entre en vigueur après le 1er janvier 2027, ce qui est l'hypothèse réaliste. Il reste un risque limité de concurrence le même jour (LFI 2027) et de renaissance au CIBS, plus un bilan des mesures à corriger.

Pour ces dix articles, le projet supprime la taxe ou son article de procédure et la version 2027 la maintient (seules constatation et recouvrement passent par L. 161-1 et L. 180-1 du CIBS). La loi de réforme sera adoptée après le 1er janvier 2027 : l'abrogation vise l'article dans sa rédaction alors en vigueur, et les clauses « années antérieures » couvrent la rédaction 2027 pour les faits générateurs passés. Ce n'est donc pas une réforme écrasée. Deux réserves : (1) si la réforme était portée par une loi entrant en vigueur le 1er janvier 2027 (LFI 2027), les deux textes prendraient effet le même jour et il faudrait viser expressément la rédaction issue de l'ordonnance ; (2) pour 1609 sexvicies, 1609 tertricies et 1613 quater, la version 2027 s'arrête au 2222-02-22 et porte un lien « ABROGATION » de l'article 17 de l'ordonnance 2025-1247. Une abrogation différée, probablement liée à une reprise dans le CIBS, est donc annoncée : une taxe supprimée au CGI pourrait renaître au CIBS hors des cinq codes. Dans ces cinq couples, la version 2027 ne fait que réécrire la procédure ou le renvoi TVA d'une charge que la proposition supprime en entier. Une abrogation ou une réécriture intégrale adoptée après le 1er janvier 2027 vise l'article tel qu'il est alors rédigé : la version 2027 disparaît avec lui, et aucun renvoi n'est à reporter. Le risque d'écrasement n'existerait que si la réforme entrait en vigueur avant le 1er janvier 2027, ce qui n'est pas réaliste au 26 octobre 2026. Les notes de WF, ZA, ZL et ZM lisent ABROGE_DIFF comme une abrogation au 1er janvier 2027. Or ces taxes subsistent en 2027 : le gain de la suppression est réel et doit figurer dans le bilan, au lieu d'être présenté comme « déjà acquis » ou incertain. L'état ABROGE_DIFF de la version courante signale un remplacement de rédaction, non une abrogation : 1740 D continue au 1er janvier 2027, renvois mis à jour (L. 217-8 CIBS, L. 80 PA LPF, L. 211-150 et L. 215-22 CIBS). La proposition d'abrogation reste donc nécessaire après 2027. Une abrogation par numéro adoptée après cette date atteindrait la rédaction 2027 ; la transition (« les publications en cours sont retirées sans délai ») doit couvrir les publications fondées sur cette rédaction. La version 2027 maintient intégralement la présomption, avec la seule mise à jour terminologique. Une abrogation par numéro postérieure à 2027 l'atteindrait ; mais la phrase interprétative de la proposition et sa transition visent les « taxes » au sens de 2026 et ne mentionnent pas la rédaction issue de l'ordonnance. Synthèse de l'agent principal : la même analyse vaut pour les taxes abrogées du lot C3 (231, 231 quater, 235 ter X, XB, ZD, ZD bis, ZE bis, 302 bis MB), pour 1804 C au 1er janvier 2027 (le risque réel est la réécriture de 2029, RT-FUTFISC-22) et pour 1740 D et 1786, où les notes ou la transition doivent viser la rédaction 2027. Pour ces versions 2027, il n'y a pas d'écrasement : la loi de réforme, nécessairement postérieure, emporte l'article tel qu'il est alors rédigé. Deux exceptions subsistent : une entrée en vigueur le même jour (LFI 2027) et la reprise de la charge au CIBS.

**Correction minimale.** Dans le véhicule législatif : rédiger les abrogations « L'article X du code général des impôts, dans sa rédaction en vigueur à la date de publication de la présente loi, est abrogé » et ajouter une clause : « Aucune disposition du code des impositions sur les biens et services ne peut instituer, pour les années ou opérations auxquelles s'appliquent les abrogations prévues par la présente loi, une imposition ayant le même fait générateur et la même assiette. » Pour 1740 D et 1786 : corriger les notes (l'article continue au 1er janvier 2027 ; la suppression a un effet propre) et étendre la transition aux décisions prises sur la rédaction 2027.

**À préserver.** Créances, restitutions, prescriptions et recours des années antérieures, y compris sous la rédaction 2027 ; Affectations des produits anciens (CNM, sociétés de courses, MSA, communes).

**Articles.** cgi 1519 A, cgi 1519 B, cgi 1582, cgi 1590, cgi 1609 duotricies, cgi 1609 sexdecies C, cgi 1609 sexvicies, cgi 1609 tertricies, cgi 1609 untricies, cgi 1613 quater, cgi 1740 D, cgi 1786, cgi 231, cgi 231 quater, cgi 235 ter X, cgi 235 ter XB, cgi 235 ter ZD, cgi 235 ter ZD bis, cgi 235 ter ZE bis, cgi 302 bis MB, cgi 302 bis WD, cgi 302 bis WF, cgi 302 bis ZA, cgi 302 bis ZM, cgi 828

### RT-FUTFISC-08 — 1770 duodecies : certificat de caisse et amende de 7 500 € transférés à L. 216-40 CIBS

*P1, confirmé, coordination manquante.* Effet certain à une date connue (1er janvier 2027, avant toute entrée en vigueur réaliste de la réforme) : l'amende que le projet supprime est réédictée sur une obligation transférée au CIBS, que le projet ne touche pas.

La proposition rattache la suppression de l'amende au certificat du 3° bis du I de 286 CGI, lui-même supprimé dans la proposition de 286. Or, au 1er janvier 2027, l'obligation de certificat est rattachée à L. 216-40 CIBS (hors des cinq codes) et 1770 duodecies est réécrit sur ce fondement. Une abrogation par numéro adoptée après 2027 atteindrait l'article dans sa rédaction 2027, mais l'obligation de certificat subsisterait dans le CIBS et pourrait être sanctionnée par une autre voie ou rétablie ; le motif « coordination de la suppression des certificats … dans le 3° bis du I de 286 » perd son support. La NOTA de la version 2027 annonce en outre « le 1er septembre 2026 », discordante avec le début LEGI.

**Correction minimale.** Viser dans la loi de réforme l'abrogation de 1770 duodecies « dans toutes ses rédactions, y compris celle issue de l'ordonnance n° 2026-671 » et neutraliser, par une disposition de coordination hors des cinq codes, l'obligation de certificat de L. 216-40 CIBS (sans en inventer le contenu), en conservant les exigences d'inaltérabilité et de conservation.

**À préserver.** Conditions d'inaltérabilité, sécurisation, conservation et archivage avec leurs dispenses ; Sanctions autonomes de fraude (1770 undecies) ; Application de la loi répressive plus douce aux manquements non définitivement sanctionnés.

**Articles.** cgi 1770 duodecies, cgi 286

### RT-FUTFISC-09 — 1788 D / 1788 E : e-reporting transféré à L. 216-47 et L. 216-48 CIBS ; montants réduits 2027 à appliquer ; renvois officiels erronés

*P1, confirmé, coordination manquante.* Les amendes de transmission (e-reporting) sont réédictées au 1er janvier 2027 sur les obligations L. 216-47/L. 216-48 CIBS, alors que la proposition ne supprime que 290 et 290 A CGI ; effet certain et prochain.

La proposition est une coordination de l'abrogation proposée de 290 et 290 A. Dans la version 2027, les obligations de transmission sont celles de L. 216-47 et L. 216-48 CIBS ; 290 et 290 A restent en ABROGE_DIFF jusqu'à une date non fixée. Supprimer 290/290 A CGI ne supprime donc pas les transmissions CIBS ; les sanctions 2027 restent applicables à ces obligations. La version 2027 réduit en outre les amendes (500 € → 250 € ; plafond 100 000 € → 45 000 € pour les opérateurs) : c'est une faveur pour les manquements anciens, que la transition de la proposition (renvoi au V « dans sa rédaction antérieure ») ne capte pas. Dans la rédaction 2027, 1788 D ne comporte plus de IV et son III est une dispense ; l'amende des plateformes est au II. 1788 E 2027 renvoie donc à des subdivisions inexistantes ou étrangères. La proposition de 1788 E (base 2026) abroge le 1° et garde ces renvois dans sa transition pour les retraits anciens.

**Correction minimale.** Abroger 1788 D dans toutes ses rédactions, étendre la clause de non-sanction aux obligations de L. 216-47 et L. 216-48 CIBS (coordination hors des cinq codes à nommer), et prévoir que les manquements antérieurs bénéficient des montants réduits de la version 2027 lorsqu'ils sont plus doux.

**À préserver.** Montants réduits et dispense de première infraction de la version 2027 ; Décisions définitives, restitutions, prescriptions et recours.

**Articles.** cgi 1788 D, cgi 1788 E, cgi 290, cgi 290 A

### RT-FUTFISC-10 — 1788 A (2030-07) : réédiction de l'amende de 5 % et des registres, amende nouvelle de 2 c

*P1, confirmé, risque juridique.* Effet probable et défavorable au redevable : la version du 1er juillet 2030, publiée avant la réforme mais applicable après elle, réédicte l'amende de 5 % et les registres que le projet supprime, et ajoute une amende nouvelle.

Le projet supprime l'amende de 5 % de la TVA déductible omise et remplace les registres par les pièces ordinaires de 277 A. La version 2027 (ord. 2026-671 art. 2) réécrit ces passages en termes CIBS. La réforme, postérieure, l'emportera sur cette version : c'est un conflit de rédaction, avec renvois morts à 289 B, 277 A et 287 dans la proposition. Mais une seconde version, publiée par l'ordonnance 2025-1247 (art. 20) et applicable au 1er juillet 2030, donc probablement après la réforme, réédicte l'amende de 5 % et les registres de L. 216-49. Elle crée aussi une amende de 15 € pour manquement à l'obligation d'information de L. 216-12 CIBS, et abroge en revanche les amendes des états récapitulatifs (1 a, 2 a). Pour 1737, la version 2030-07 conserve aussi la répétition trimestrielle de l'amende de 1 000 € que le projet supprime ; le passage n'est pas modifié par la version future, mais la question se pose si l'instruction est une réécriture. Les notes renvoient à une « reprise CIBS à coordonner séparément ». Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Dans la loi de réforme : « Les dispositions du II de l'article 20 de l'ordonnance n° 2025-1247 du 17 décembre 2025, en tant qu'elles modifient les 1, 2 et 4 de l'article 1788 A du code général des impositions, ne s'appliquent pas ; l'article 1788 A, dans sa rédaction issue de la présente loi, est applicable à compter du 1er juillet 2030 sous réserve de l'abrogation des a des 1 et 2. » Rebaser la proposition sur les renvois CIBS (L. 216-46, L. 216-45, L. 161-1) et garder l'abrogation des amendes des états récapitulatifs. Même clause pour le IV bis de 1737.

**À préserver.** Abrogation des amendes des états récapitulatifs (2030) ; Amendes antifraude des 1 à 3 et garanties du 5.

**Articles.** cgi 1788 A

### RT-FUTFISC-11 — 289 bis (2030-07) : livraisons intra-UE dans le champ ; option papier du projet et droit de l'Union

*P1, à confirmer, risque juridique.* Risque européen probable à date connue (1er juillet 2030) : fusionner la proposition (facture électronique facultative) avec la version 2030, qui fait entrer les livraisons intra-UE dans le champ, contredirait l'obligation européenne de facturation électronique de ces opérations.

La version de 289 bis applicable au 1er juillet 2030 retire du V l'exclusion des livraisons intracommunautaires, qui entrent alors dans le champ de la facturation électronique obligatoire. La proposition rend le support électronique et la plateforme facultatifs (I) et reproduit l'ancien V. Le report mécanique du V étendrait l'option papier aux livraisons intra-UE, alors que le régime européen « TVA à l'ère numérique » prévoit, sauf erreur à vérifier, la facture électronique obligatoire pour ces opérations à partir de juillet 2030. Les notes signalent la directive 2025/516 comme « point de confrontation européenne non vérifié ». Anomalie de source : la version courante porte une fin au 2222-02-22, alors que la version future débute le 2030-07-01, et la NOTA courante annonce une abrogation partielle au 1er janvier 2027 avec maintien jusqu'à reprise réglementaire (L. 215-39 et L. 216-44 CIBS). Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Dans la proposition, conserver jusqu'au 30 juin 2030 l'exclusion du 1° du I de l'article 262 ter et prévoir qu'à compter du 1er juillet 2030 l'option de support du I ne s'applique pas aux opérations pour lesquelles le droit de l'Union impose la facture électronique. Coordonner avec L. 215-39 et L. 216-44 CIBS (hors corpus).

**À préserver.** Annuaire, portabilité, services minimaux d'un an, exclusions IV et V ; Caractère facultatif de la plateforme dans le champ domestique, dans la mesure permise par le droit de l'Union.

**Articles.** cgi 289 bis

### RT-FUTFISC-12 — 1788 F (nouveau, 2027) : agrément de détaxe et sanctions que le projet supprime dans 262-0 bis

*P1, confirmé, coordination manquante.* Effet certain au 1er janvier 2027 : l'agrément d'opérateur de détaxe, sa caducité et l'amende de 300 000 € que le projet supprime dans 262-0 bis survivent dans un nouveau numéro, 1788 F, et dans le CIBS (L. 215-40), hors de l'article réformé.

1788 F est un numéro futur hors inventaire. Il institue au 1er janvier 2027 le régime de sanctions de l'agrément des intermédiaires de détaxe, défini au 1° de L. 215-40 du CIBS : caducité en cas de cession du fonds ou de prise de contrôle, amende jusqu'à 300 000 € et interdiction de trois ans pour qui agit sans agrément, amende jusqu'à 300 000 € pour manquement aux obligations de L. 215-40. La proposition de 262-0 bis supprime précisément l'agrément, sa caducité et « la sanction de son absence ». Mais l'article 262-0 bis est lui-même abrogé au 1er janvier 2027, hormis un maintien provisoire, et son contenu est transféré au CIBS et à 1788 F. Une réforme adoptée après cette date et limitée à 262-0 bis laisserait intacts l'agrément CIBS et les sanctions de 1788 F. Les notes de 262-0 bis anticipent la reprise CIBS sans identifier 1788 F : partiellement anticipé. Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Réécrire 1788 F dans la loi de réforme : ne garder que la sanction des obligations techniques maintenues, et déclarer qu'aucune caducité ni amende ne peut résulter de la seule absence d'agrément. Abroger le 1° de L. 215-40 du CIBS en tant qu'il soumet à agrément ces intermédiaires (coordination hors des cinq codes). Transition : loi plus douce pour les sanctions non définitives. Rédaction complète dans le rapport (R-OWN-1).

**À préserver.** Obligations techniques de transmission, gestion des risques, preuve de l'exportation ; Certifications d'interconnexion déjà délivrées ; Sanctions douanières de fraude (III bis).

**Articles.** cgi 1788 F, cgi 262-0 bis

### RT-FUTFISC-13 — CVAE et TA-CVAE : barèmes et taux 2027-2029 publiés, non neutralisés

*P1, à confirmer, risque juridique.* Les substitutions 2027-2029 du régime de la CVAE et de sa taxe additionnelle sont déjà publiées et prennent effet à date certaine. Pour toute année que le projet supprime, elles réédictent un barème, un taux ou des règles de recouvrement. Les propositions ne les neutralisent pas, alors que cvae_removal l'exige. L'effet juridique dépend de la nature des instructions et de la date de la réforme : probable, pas certain.

Le projet supprime la CVAE et la TA-CVAE pour les années commençant après l'entrée de la loi (années « supprimées »), et règle les années antérieures selon leur droit propre. Trois séries de versions déjà publiées portent sur les années 2027 à 2029 : 1586 ter (2027-2030), qui maintient l'assujettissement et réécrit le 3 du II ; 1586 quater (2028, 2029), qui réédicte un barème complet et un dégrèvement ; 1600 (2028, 2029), qui porte le taux de la TA-CVAE à 13,84 % puis 27,68 %. Pour une année que le projet supprime, ces versions maintiennent en le modifiant l'élément même que la proposition supprime : c'est une réforme écrasée au sens de la grille. Deux lectures sont possibles. 1) Les instructions sont des substitutions ponctuelles (taux, mots). Elles deviennent sans objet sur un article réécrit en clause d'abrogation : le risque est alors surtout un risque de consolidation et de sécurité juridique. 2) Les instructions remplacent un alinéa ou un article. Elles rétablissent le barème ou le taux à leur date d'effet, si la réforme est entrée en vigueur avant. L'adage lex posterior joue pour la loi de réforme seulement si elle vise expressément ces dispositions différées. Les notes de 1586 quater visent la seule abrogation de 2030 ; celles de 1600 ne citent que 9,23 % ; celles de 1586 ter ne citent aucune version future.

**Correction minimale.** Ajouter à la loi de réforme une disposition transitoire expresse (rédaction complète en A-redactions.md, n° 1). Les dispositions publiées et non encore entrées en vigueur qui modifient les articles 1586 ter, 1586 quater et 1600, ainsi que les articles liés (1586 quinquies à nonies, 1649 quater B quater, 1679 septies, 1681 septies, 1731), ne s'appliquent pas aux impositions des années supprimées, et elles restent applicables aux années antérieures. Dans la proposition de 1586 quater, remplacer « Le dégrèvement de 188 euros prévu au II dans la rédaction applicable aux années antérieures » par « Les dégrèvements prévus au II dans la rédaction applicable à chacune des années antérieures ».

**À préserver.** Barèmes réduits et dégrèvements 2028 (125 €) et 2029 (63 €) pour les années antérieures à la suppression ; Taux de TA-CVAE légalement applicables aux années antérieures (9,23 %, 13,84 %, 27,68 %) et affectation CCI France ; Exonérations, dégrèvements, restitutions et recours des années anciennes ; Baisses programmées du plafonnement CFE (1,531/1,438/1,344/1,25 %).

**Articles.** cgi 1586 quater, cgi 1586 ter, cgi 1600

### RT-FUTFISC-14 — Plafonnement CFE : définitions 1586 quinquies et sexies abrogées en 2030 ; réécriture 1647 B sexies et 1647 B sexies A

*P1, confirmé, coordination manquante.* Le 1er janvier 2030 est une date certaine. À cette date, l'abrogation déjà publiée de 1586 quinquies et 1586 sexies et la réécriture de 1647 B sexies privent les renvois du projet de leur objet. Elles retirent aussi des éléments favorables du plafonnement CFE que cvae_removal ordonne de conserver. Effet probable sur un avantage général des entreprises.

Le projet conserve 1586 quinquies et 1586 sexies comme définitions autonomes de la période et de la valeur ajoutée du plafonnement CFE, conformément à cvae_removal. Ses propositions de 1647 B sexies, 1447 et 238 bis HW y renvoient. Or la loi en vigueur abroge ces deux articles au 1er janvier 2030 (ABROGE_DIFF sans successeur pour 1586 quinquies ; lien ABROGE pour 1586 sexies). Une abrogation différée vise le numéro d'article, quel que soit son contenu à cette date : elle atteindra les définitions réécrites par le projet, sauf neutralisation expresse. Au même moment, 1647 B sexies est réécrit pour renvoyer à 1647 B sexies A et à un I bis de périodes. Comparée au projet, cette réécriture : a) supprime le plafond de la valeur ajoutée à 80 % ou 85 % du chiffre d'affaires (7 du I de 1586 sexies), favorable au redevable puisqu'il abaisse la VA et donc le plafond de 1,25 % ; b) omet la règle de création d'entreprise (3 du I de 1586 quinquies) ; c) retire de la cotisation majorée la TASA d'Île-de-France (1599 quater D) et la taxe spéciale GPSO (1609 İ), toujours en vigueur, avec une phrase lacunaire ; d) ajoute en revanche l'exclusion favorable de la VA de navigation (1647 B sexies A 7° et annexe II 310 HC). Le projet perd donc d (et 310 HC devient sans objet) s'il garde 1586 sexies, et perd a à c si la version 2030 l'emporte. Pour 238 bis HW, le renvoi figé du projet préserve les « plafonds », que la version 2030 supprime.

**Correction minimale.** Réécrire 1647 B sexies en une rédaction unique applicable aux années supprimées (texte complet en A-redactions.md, n° 2). Cette rédaction renvoie à 1586 sexies jusqu'en 2029 et à 1647 B sexies A à compter de 2030 ; elle reprend expressément le plafond de 80/85 % du CA, la règle de création, la liste complète de la majoration (dont 1599 quater D et 1609 İ) et les taux programmés. Elle s'accompagne de la neutralisation de la réécriture de 2030 et de la coordination de 1447 (renvoi au « 1 du I de l'article 1647 B sexies A » à compter de 2030) et de 238 bis HW (renvoi figé maintenu, ou bien 1647 B sexies A plus le plafond).

**À préserver.** Plafonnement CFE à 1,25 % de la VA à compter de 2030 et taux décroissants antérieurs ; Plafond de VA à 80/85 % du CA ; Exclusion de la VA de navigation non liée à la France (1647 B sexies A 7°, 310 HC) à compter de 2030 ; Inclusion de 1599 quater D et 1609 İ dans la cotisation plafonnée ; Exonération CFE des micro-entrepreneurs (1447 IV proposé) ; Agréments et contrats 238 bis HV/HW acquis.

**Articles.** a2 310 HC, cgi 1447, cgi 1586 quinquies, cgi 1586 sexies, cgi 1647 B sexies, cgi 1647 B sexies A, cgi 238 bis HW

### RT-FUTFISC-15 — CVAE : la mesure n'est qu'une accélération de la suppression légale de 2030 ; fusion des rédactions de 2030

*P2, confirmé, simple alerte.* La loi en vigueur abroge déjà la CVAE et ses accessoires au 1er janvier 2030 et en réduit les taux en 2028 et 2029. Présenter la mesure du projet comme une suppression nouvelle et durable surestime son effet. C'est une alerte de mesure (substantive_outcomes), sans effet normatif direct ; les rédactions de 2030 qui convergent restent à fusionner.

Dans le droit déjà publié, la CVAE disparaît pour les impositions 2030 (1586 ter, 1586 quinquies à nonies, 1679 septies, 1600 III, 1649 quater B quater IV, 1681 septies 3, 1731 3) ; ses taux maximaux tombent à 0,19 % en 2028 et 0,09 % en 2029. Le gain propre du projet se limite donc aux années comprises entre l'année qui suit l'entrée en vigueur de la réforme et 2029, sur des taux déjà réduits. Les coordinations de 1600, 1649 quater B quater, 1681 septies et 1731 rejoignent les abrogations de 2030 : ce ne sont pas des allègements supplémentaires. Les rédactions doivent être fusionnées pour qu'une seule version s'applique.

**Correction minimale.** Dans le bilan de mesure : « accélération de la suppression légale de la CVAE et de la TA-CVAE programmée au 1er janvier 2030, pour les impositions de [première année supprimée] à 2029 ». Compter une seule mesure, ne pas compter les coordinations comme des baisses, et fusionner les rédactions convergentes de 2030 (abrogation pure ou maintien des clauses transitoires).

**À préserver.** Règles transitoires des années anciennes.

**Articles.** cgi 1586 ter, cgi 1600, cgi 1649 quater B quater, cgi 1681 septies, cgi 1731

### RT-FUTFISC-16 — 1649 quater E et H : obligations des CGA/AGA ressuscitées en 2030 par la consolidation

*P2, confirmé, conflit de source.* Les versions 2030 font réapparaître en consolidation des obligations de contrôle et de télétransmission des CGA et AGA, abrogées depuis 2025. Leur effet juridique est douteux, car modifier un article abrogé est en principe sans objet. L'affichage d'un texte « en vigueur » et l'insécurité qui en résulte sont, eux, certains.

La LF 2023 avait prévu, pour les impositions 2030 (après plusieurs reports), de retirer de 1649 quater E et H les mots relatifs à la CVAE. La LF 2025 a ensuite abrogé tout le régime des CGA et AGA. LEGI a pourtant conservé la version différée de 2030, qui fait renaître ces deux articles avec des obligations : examens de cohérence, de concordance et de vraisemblance, compte rendu au SIE, télétransmission, mandat. Ces textes renvoient à 1649 quater F et G, eux aussi abrogés. Le projet ne contient aucune proposition sur ces numéros, puisqu'ils sont absents de l'inventaire. Les orientations interdisent toute formalité de remplacement.

**Correction minimale.** Insérer dans la loi de réforme : « Les articles 1649 quater C à 1649 quater M du code général des impositions demeurent abrogés. Les dispositions du J du XXVII de l'article 55 de la loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023 en tant qu'elles modifient les articles 1649 quater E et 1649 quater H sont sans objet. » Le premier terme serait « code général des impôts » ; voir la rédaction exacte en A-redactions.md, n° 3.

**À préserver.** Droits et obligations nés pendant la période d'agrément antérieure à 2025, régis par les textes alors applicables.

**Articles.** cgi 1649 quater E, cgi 1649 quater H

### RT-FUTFISC-17 — CSI : réédiction et extension au livre foncier de Mayotte au 1er janvier 2029 (880 à 881 M)

*P1, confirmé, coordination manquante.* Effet probable et grave à date connue (1er janvier 2029). Si la réforme entre en vigueur avant cette date, la loi de finances pour 2026 réédicte des perceptions autonomes de CSI (881 B, 881 C) et en crée de nouvelles à Mayotte, contre la suppression générale décidée. Ce n'est pas P0 : l'effet dépend de la date de la réforme et de la nature, non vérifiée, de l'instruction modificative.

Le projet supprime la CSI pour toutes les réquisitions nouvelles : 879 réécrit, et 880 à 881 M abrogés ou réservés aux demandes antérieures. Il conserve l'exonération mahoraise de 881 O jusqu'à son terme, le 31 décembre 2028, en précisant qu'elle ne renaît pas. Or l'article 102 de la LF 2026 a déjà publié, pour le 1er janvier 2029, des rédactions de 880, 881 A, B, C, I, J, K et M qui organisent précisément la perception de la CSI sur le livre foncier de Mayotte à la fin de l'exonération. Elles étendent les tarifs aux inscriptions et à l'immatriculation (881 K II) et créent quatre faits générateurs nouveaux au 881 C (18° à 21°) ainsi qu'un nouveau cas au 881 B. 881 B et 881 C sont des dispositions de perception autonomes (« Il est perçu une contribution fixe… ») : elles ne dépendent pas de 879. Aucune proposition, aucun motif ni aucune note de 880 à 881 M ne mentionne ces versions. Seule la note de 881 O affirme, sans base textuelle, l'absence de renaissance.

**Correction minimale.** Ajouter à la loi de réforme une disposition de coordination : « Les dispositions du I de l'article 102 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 qui modifient les articles 880, 881 A, 881 B, 881 C, 881 I, 881 J, 881 K et 881 M du code général des impôts sont abrogées. » Préciser dans 879 que la suppression couvre aussi les formalités du livre foncier de Mayotte et l'immatriculation, sans condition de date de l'acte. Mentionner la version 2029 dans le motif des huit propositions.

**À préserver.** Exonération mahoraise de 881 O pour les demandes antérieures au 1er janvier 2029 ; Régime ancien des demandes antérieures à la réforme (créances, restitutions, recours) ; Formalités civiles du livre foncier de Mayotte, rang et opposabilité, qui ne sont pas des taxes.

**Articles.** cgi 879, cgi 880, cgi 881 A, cgi 881 B, cgi 881 C, cgi 881 I, cgi 881 J, cgi 881 K, cgi 881 M, cgi 881 O

### RT-FUTFISC-18 — 1018 A et 1100 : droit fixe de procédure pénale réédicté en 2029

*P1, confirmé, coordination manquante.* Renaissance probable, au 1er janvier 2029, d'un prélèvement que le projet abroge (droit fixe de procédure pénale) si la réforme entre en vigueur avant cette date. L'effet est certain à cette date si l'instruction de l'ordonnance est une réécriture.

Le projet abroge le droit fixe de procédure et sa liquidation en débet. L'ordonnance 2025-1091, qui recodifie le CPP, a publié pour le 1er janvier 2029 une rédaction entière de 1018 A (barème, majoration de non-comparution, supplément toxicologique) et de 1100, avec un vocabulaire et des renvois nouveaux. Les notes voient le risque de renaissance mais lisent l'état ABROGE_DIFF comme une abrogation, et la proposition ne neutralise pas l'ordonnance.

**Correction minimale.** Ajouter à la loi de réforme : « Les dispositions de l'ordonnance n° 2025-1091 du 19 novembre 2025 qui modifient les articles 1018 A et 1100 du code général des impôts sont abrogées. » Conserver l'abrogation prospective proposée et adapter le vocabulaire (« action pénale », « tribunal délictuel ») si la réforme entre en vigueur après 2029.

**À préserver.** Décisions antérieures, avec exemptions, dispenses de majoration, solidarités et restitutions ; Amendes et frais ayant un fondement autonome.

**Articles.** cgi 1018 A, cgi 1100

### RT-FUTFISC-19 — 1649 quater-0 B bis : présomption de revenu réédictée en 2029

*P1, confirmé, coordination manquante.* La présomption de revenu imposable égal à la valeur vénale des biens, que le projet supprime, est réédictée en entier au 1er janvier 2029 : effet probable sur l'assiette de l'IR.

La proposition supprime pour l'avenir la présomption spéciale de revenu. La version 2029 la réédicte en entier en ne changeant que les renvois au CPP. Le motif et les notes ne mentionnent pas 2029 : ils commentent seulement la NOTA de 2025.

**Correction minimale.** Neutraliser la disposition qui crée la version 2029 (« les dispositions […] qui modifient l'article 1649 quater-0 B bis du code général des impôts sont abrogées »), après avoir identifié le texte modificateur, et mentionner la version 2029 dans le motif.

**À préserver.** Années antérieures, avec preuve contraire, exclusions et voies de recours ; Incriminations et pouvoirs de contrôle autonomes.

**Articles.** cgi 1649 quater-0 B bis

### RT-FUTFISC-20 — 1789 : délit de réitération réédicté en 2029

*P1, confirmé, coordination manquante.* Un délit puni de six mois d'emprisonnement, abrogé par le projet, est réédicté au 1er janvier 2029. Contradiction probable en matière pénale, où la légalité des délits exige un texte certain.

Les notes lisent à tort une abrogation en 2029. L'article est en réalité remplacé : l'incrimination est maintenue et seule l'appellation du tribunal change. Faute de neutralisation, deux textes successifs se contredisent sur l'existence du délit.

**Correction minimale.** Abroger la disposition de l'ordonnance 2025-1091 qui modifie l'article 1789 (ou déclarer cette modification sans objet) et corriger les notes : remplacement, pas abrogation.

**À préserver.** Sanctions fiscales des articles 1729, 1729 B et 1734 ; Délit de fraude de l'article 1741.

**Articles.** cgi 1789

### RT-FUTFISC-21 — 568 : droit de licence des débitants de tabac réédicté en 2029

*P1, confirmé, coordination manquante.* Le droit de licence des débitants de tabac, que le projet abroge, est réédicté en entier au 1er janvier 2029 par l'ordonnance 2026-671 : renaissance probable d'un prélèvement.

La version courante n'est pas abrogée au 1er janvier 2029 : elle est remplacée par une rédaction entière (« rédaction issue du 1° du même II »), donc vraisemblablement une réécriture. Les notes l'ont lue comme une abrogation.

**Correction minimale.** Ajouter : « Le 1° du II de l'article 14 de l'ordonnance n° 2026-671 du 27 juillet 2026, en tant qu'il porte sur l'article 568 du code général des impôts, est abrogé. » Rectifier les notes.

**À préserver.** Mises à la consommation antérieures ; Accises, agréments et règles sanitaires distincts.

**Articles.** cgi 568

### RT-FUTFISC-22 — 1804 C : majoration de 0,2 % maintenue par les réécritures 2027 et 2029

*P1, confirmé, coordination manquante.* Une majoration de 0,2 % abrogée par le projet est maintenue par deux réécritures successives (2027, 2029). Le risque réel porte sur 2029 si la réforme intervient entre les deux dates.

Les notes lisent l'état ABROGE_DIFF comme une abrogation au 1er janvier 2027. En réalité, deux réécritures se succèdent (2027 puis 2029) et maintiennent la majoration. Une abrogation votée après 2027 vaut pour la version 2027, mais la réécriture de 2029 peut ensuite la réédicter.

**Correction minimale.** Abroger la disposition de l'article 16 de l'ordonnance 2026-671 (et celle de l'article 11 de l'ordonnance 2025-1247 si la réforme est antérieure à 2027) qui modifie l'article 1804 C ; corriger les notes.

**À préserver.** Obligation de télérèglement de 1698 D ; Sanctions définitives et restitutions.

**Articles.** cgi 1804 C

### RT-FUTFISC-23 — 150 VM : la proposition se déclare inapplicable après le 1er janvier 2027

*P0, confirmé, incohérence du projet.* Effet grave et certain dès l'entrée en vigueur si le texte est adopté tel quel : la loi de réforme est nécessairement postérieure au 1er janvier 2027, et le V proposé déclare que l'article réformé ne s'applique pas au-delà de cette date. L'article réformé serait donc inapplicable dès son entrée en vigueur.

L'état ABROGE_DIFF de la version courante traduit son remplacement le 1er janvier 2027 par une rédaction issue de l'ordonnance 2025-1247, non l'abrogation de l'article 150 VM. La proposition prend cet état pour une abrogation et inscrit dans le texte normatif que l'article réformé ne s'applique pas au-delà du 1er janvier 2027. Adoptée nécessairement après cette date, la loi de réforme introduirait un article qui proclame sa propre inapplicabilité. Le texte maintient en outre les modalités déclaratives des a à c (annexe à la déclaration 287, régime 302 septies A), qui disparaissent le 1er janvier 2027 au profit de L. 161-1 du CIBS.

**Correction minimale.** Supprimer la dernière phrase du V proposé ; rebaser le I 1° (second alinéa), le III 1° et le IV sur la rédaction 2027 (constatation selon L. 161-1 CIBS ; recouvrement et réclamations selon le livre II du CGI et le LPF applicables aux taxes sur les biens et services) ; conserver la suppression de la déclaration des exportations sans cession (I 2° et III 2°). Rédaction complète dans C1-redactions.md.

**À préserver.** Option de l'article 150 VL ; Déclaration des cessions et délais (635, un mois) ; Faits générateurs antérieurs, y compris ceux régis par la rédaction 2027, avec restitutions, prescriptions et recours.

**Articles.** cgi 150 VM

### RT-FUTFISC-24 — 1840 P, 406 A 15, 87 A, 1382-0 : clauses fondées sur une abrogation ou une extinction inexistante

*P1, confirmé, incohérence du projet.* Deux propositions écrivent, dans leur texte même, qu'une abrogation de l'article est prévue en 2029, ce qui est inexact. Pour 1840 P, la réforme se borne ainsi elle-même à 2029 et cède devant une version qui rétablit l'emprisonnement supprimé. Effet probable et pénal.

L'état ABROGE_DIFF d'une version suivie d'une version VIGUEUR_DIFF signifie un remplacement de rédaction, pas une abrogation de l'article. Ces deux propositions intègrent pourtant l'abrogation supposée dans leur texte opératoire. Pour 1840 P, la phrase limite la rédaction réformée à 2029 ; la version alors applicable contient l'emprisonnement d'un mois que le projet supprime. Pour 406 A 15, la version 2029 rétablit le préalable administratif que le projet retire. La même lecture erronée figure dans les notes de 1018 A, 1100, 1789, 1804 C et 568 (comptées dans leurs propres objections). Même défaut dans 87 A : la proposition écrit « sans modifier les échéances des 1° et 2° ni reporter l'extinction du présent article prévue au 1er janvier 2030 ». La NOTA de la version future fixe pourtant une entrée « à une date fixée par décret, et au plus tard le 1er janvier 2030 » d'une nouvelle rédaction du 2° : il n'y a pas d'extinction. Dans 1382-0, la phrase « Le présent V n'a pas pour effet de prolonger la période légale d'application du présent article » est ambiguë pour la même raison (C1-06). Le cas plus grave de 150 VM fait l'objet de RT-FUTFISC-23.

**Correction minimale.** Supprimer les deux phrases fondées sur une abrogation inexistante. Rebaser les propositions sur les rédactions 2029 (« tribunal délictuel ») et neutraliser, pour 1840 P et 406 A 15, les modifications de l'ordonnance 2025-1091 contraires aux choix du projet. Pour 87 A, supprimer « ni reporter l'extinction du présent article prévue au 1er janvier 2030 » et rebaser le 2° sur la version future. Pour 1382-0, supprimer la dernière phrase du V.

**À préserver.** Amende de 3 750 € doublée en récidive (1840 P) ; Saisine directe par l'intéressé et faculté de demande de l'administration (406 A 15).

**Articles.** a3 406 A 15, cgi 1382-0, cgi 1840 P, cgi 87 A

### RT-FUTFISC-25 — Annexe II 276 (et 279, 280, 286 F) : agrément tabacs du décret 2026-612 au 1er août 2027

*P1, confirmé, risque juridique.* Effet certain au 1er août 2027, date d'entrée en vigueur du décret 2026-612 (antérieure à toute réforme réaliste des annexes). Si la proposition est publiée après, elle substitue à l'agrément exigé par la loi (CSP L. 3512-14-7) un régime de numéro d'identification périmé qui se déclare lui-même inapplicable depuis le 1er août 2027 : l'agrément n'aurait plus de conditions de délivrance réglementaires, et un décret contraire à la loi serait illégal.

L'état ABROGE_DIFF de la version courante signifie qu'elle est remplacée le 1er août 2027 par une rédaction déjà publiée, pas que l'article est abrogé. La proposition et ses notes en déduisent à tort une extinction : elles réécrivent un régime appelé à disparaître et programment sa fin. La version future met en œuvre un agrément voulu par la loi (CSP) et retire déjà la caution, qui était la coupe recherchée par le projet. En revanche, elle crée des charges nouvelles : renouvellement tous les un ou trois ans, information dans un délai de quinze jours, compte bancaire dédié, contrôle du casier judiciaire, dossier fixé par arrêté. Une partie de ces charges découle de la loi (CSP) et du droit de l'Union sur la traçabilité ; ni le CSP ni le règlement ne figurent dans le corpus. Les retained_unchanged 279, 280 et 286 F de l'annexe II basculent au 1er août 2027 vers « l'agrément mentionné aux I et II de l'article 276 ». La version future de 286 F rend 276 et 279 applicables dans les collectivités régies par l'article 73 de la Constitution aux fournisseurs « soumis à agrément », ce qui réduit la dérogation outre-mer existante. Cette extension découle du CSP (L. 3512-14-2, hors corpus). Les notes de 279 et 280 parlent d'« abrogation différée au 1er août 2027 », lecture erronée.

**Correction minimale.** Retirer la proposition de 276 fondée sur le numéro d'identification et la phrase « cesse de s'appliquer […] 1er août 2027 ». Rédiger la réforme sur la version 2027-08-01 : conserver l'agrément CSP et ses conditions d'origine légale ou européenne, interdire expressément toute caution ou garantie financière de remplacement, et garder de la proposition la seule libération des cautions anciennes, limitées aux dettes antérieures. Voir C4-redactions.md, § 1.

**À préserver.** Suppression de la caution du précompte, acquise par le décret 2026-612 et voulue par le projet ; Présomption d'agrément de six mois pour les titulaires d'un numéro d'identification (NOTA du décret) ; Exclusions territoriales de 286 F (Saint-Barthélemy, Saint-Martin, Saint-Pierre-et-Miquelon) et délai d'écoulement de trois mois de 279 ; Dettes, restitutions et recours antérieurs.

**Articles.** a2 276, a2 279, a2 280, a2 286 F

### RT-FUTFISC-26 — 1496 ter (nouveau, 2029) : déclaration annuelle des loyers non examinée ; amende maintenue par 1729 C

*P1, confirmé, coordination manquante.* Effet certain à date connue (1er janvier 2029) : une déclaration annuelle obligatoire nouvelle pèse sur tous les propriétaires bailleurs, contre l'orientation de suppression des formalités. Le projet en garde même l'amende.

1496 ter est un numéro futur non inventorié. Au 1er janvier 2029, il crée pour la révision des valeurs locatives d'habitation une déclaration annuelle des bailleurs, à déposer avant le 1er juillet : informations sur les biens et loyer au 1er janvier, par voie électronique. Le projet allège au même moment la déclaration annuelle d'occupation de 1418 : il en retire le type de location et les dates d'occupation. Il maintient pourtant, dans 1729 C, l'amende de 150 € pour défaut de la déclaration de 1496 ter. Aucune note ne traite cette formalité nouvelle. Les orientations demandent de supprimer les déclarations sans utilité démontrée, sans formalité de remplacement, et de réemployer les données déjà disponibles. Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Décider expressément. Option A, conforme aux orientations : abroger 1496 ter, retirer le renvoi de 1729 C, prévoir que la révision s'appuie sur les données déjà détenues, sans déclaration de remplacement. Option B, si une fonction essentielle est démontrée : fusionner l'information sur le loyer dans la déclaration unique de 1418, avec la même échéance et la même dispense en l'absence de changement. Rédactions dans le rapport (R-OWN-2).

**À préserver.** Exonérations et abattements de taxe foncière ; Déclaration d'occupation allégée de 1418 ; Déclarations foncières de 1406.

**Articles.** cgi 1418, cgi 1496 ter, cgi 1729 C

### RT-FUTFISC-27 — Faveurs créées par versions futures à reporter (81 f, 39 quinquies G, lissage 1518 A quinquies A, 1788 A 2030, 200)

*P1, confirmé, coordination manquante.* Perte probable de faveurs déjà publiées si la réforme adopte une rédaction intégrale sur la base 2026 après leur date d'effet. C'est le cas certain de 81 (au plus tard le 1er janvier 2029), contraire à l'orientation de conservation des faveurs.

Plusieurs versions futures créent ou étendent une faveur dans un passage que la proposition reproduit sur la base 2026. 81 : exonération de l'allocation de réparation des mineurs réunionnais (4° f), entrée en vigueur par décret au plus tard le 1er janvier 2029. 39 quinquies G : provision en franchise pour les risques d'émeutes, la borne LEGI 2222-02-22 étant ici une date d'effet subordonnée à une décision européenne. 1518 A quinquies A : lissage sur 2027-2031 de l'actualisation des valeurs locatives professionnelles. 1788 A : abrogation en 2030 des amendes des états récapitulatifs. 1788 D : amendes réduites en 2027 (250 € au lieu de 500 € ; voir RT-FUTFISC-09). 1647 B sexies A : exclusion de la valeur ajoutée de navigation (voir RT-FUTFISC-14). 200 : le rattachement du taux de 75 % à une liste autonome peut réduire le champ si le CIBS couvre davantage (C2-08, à confirmer). Une loi « ainsi rédigée » adoptée après la date d'effet sans ces ajouts les supprimerait. Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Reporter dans chaque proposition le passage favorable de la version future (81 4° f ; 39 quinquies G « risques liés aux émeutes », sous la même condition d'entrée en vigueur ; 1788 A 2030 1 a et 2 a abrogés). Pour 200, viser à la fois l'ancienne liste et les articles L. 213-96 3°, L. 213-98 et L. 213-100 du CIBS (rédaction C2-08).

**À préserver.** Faveurs listées ; Conditions d'entrée en vigueur propres (décret, décision de la Commission).

**Articles.** cgi 1518 A quinquies A, cgi 200, cgi 39 quinquies G, cgi 81

### RT-FUTFISC-28 — Faveurs temporaires qui s'éteignent (JEII à impact 2029, Mayotte 2031) : rédiger en deux temps

*P2, confirmé, coordination manquante.* Effet limité : faveurs déjà temporaires dans la source. Le projet doit seulement dire s'il accepte leur fin programmée, sans prorogation inventée.

Deux faveurs temporaires de la source s'éteignent par des versions futures publiées. La qualification jeune entreprise d'innovation à impact et sa réduction d'IR à 40 % sont abrogées en 2029 (44 sexies-0 A d ; 199 terdecies-0 A ter I 3° et III A 2°). Les extensions mahoraises sont retirées en 2031 (44 quaterdecies : activités et taux de 100 % ; 1388 quinquies : abattement de 100 %). Les propositions maintiennent ces passages sans terme, voire les reformulent (44 sexies-0 A d). Leurs motifs les déclarent « intégraux », mais les notes excluent toute prorogation. Si l'instruction future est ponctuelle, la faveur s'éteint comme prévu. Si la réforme est adoptée avant et réécrit l'article, la faveur pourrait être prorogée sans décision. Si l'instruction était une réécriture, elle pourrait aussi rétablir les conditions supprimées par le projet : indicateurs de performance de 44 sexies-0 A c, option irrévocable de 44 quaterdecies VII, déclaration annuelle de 1388 quinquies VI. Ce constat documente, pour le paquet FUT-FISC, l'objection transversale RT-XCUT-01.

**Correction minimale.** Rédiger chaque proposition en deux temps : rédaction jusqu'au 31 décembre 2028 (respectivement 2030), puis rédaction sans la faveur temporaire mais avec les allègements du projet. Conserver la clause de survie des droits acquis (199 terdecies-0 A ter). Toute prorogation relève d'une décision expresse de l'auteur.

**À préserver.** Droits acquis sur souscriptions et exercices éligibles ; Suppression des indicateurs de performance (44 sexies-0 A c) et de la déclaration annuelle (1388 quinquies).

**Articles.** cgi 1388 quinquies, cgi 199 terdecies-0 A ter, cgi 44 quaterdecies, cgi 44 sexies-0 A

### RT-FUTFISC-29 — 238 bis et 1729 B : déclaration des dons déjà abrogée par la loi 2026-403

*P2, confirmé, incohérence du projet.* Risque d'interprétation a contrario limité à la période entre le 1er janvier 2027 et la réforme ; aucune perte de faveur certaine.

La loi 2026-403 abroge le 6 au 1er janvier 2027. La proposition supprime la même déclaration, mais à compter de la loi de réforme. Adoptée après 2027, sa formule peut se lire comme maintenant la déclaration pour les échéances comprises entre le 1er janvier 2027 et la réforme, ce qui réintroduit implicitement une obligation déjà supprimée. La loi 2026-403 supprime au 1er janvier 2027 la déclaration des dons de plus de 10 000 € (238 bis, 6) et sa majoration d'amende. La proposition de 1729 B, rédigée sur la base 2026, reproduit la majoration ; les notes de 238 bis demandaient déjà de limiter ce renvoi aux obligations historiques.

**Correction minimale.** Remplacer le 6 proposé par « 6. (Abrogé). » et déplacer la clause d'absence de sanction dans le 9, en visant les obligations supprimées « par la loi n° 2026-403 du 26 mai 2026 ou par la présente loi ». Coordonner 1729 B, que la version 2027 a déjà purgé du renvoi à 238 bis.

**À préserver.** Preuve sur demande du 5 bis ; Absence de déclaration de remplacement.

**Articles.** cgi 1729 B, cgi 238 bis

### RT-FUTFISC-30 — 1518 A sexies : réduction et transmission contre actualisation et lissage 2027

*P2, confirmé, coordination manquante.* Conflit de rédaction limité à un régime transitoire de réduction de valeur locative ; l'effet favorable du projet peut être réduit pour les réductions en cours en 2027.

La LF 2026 met fin, à l'actualisation 2027, aux réductions en cours au 31 décembre 2026 et les remplace par le lissage de 1518 A quinquies A. La proposition, rédigée sur la base 2026, conserve l'ancien III (recalcul après le 3 de 1518 A quinquies, abrogé en 2027) et ajoute la transmission du reliquat. Une loi de réforme « ainsi rédigée » adoptée après le 1er janvier 2027 rétablirait l'ancien III et entrerait en conflit avec 1518 A quinquies A (double atténuation ou renvoi mort).

**Correction minimale.** Remplacer le III proposé par le III de la version 2027, maintenir la règle du changement d'exploitant pour les réductions encore en cours (changements de méthode postérieurs ou réductions non éteintes), et préciser l'articulation avec 1518 A quinquies A. Rédaction complète dans C1-redactions.md.

**À préserver.** Barème 85/70/55/40/25/10 % ; Lissage 2027-2031 de 1518 A quinquies A ; Années antérieures.

**Articles.** cgi 1518 A quinquies A, cgi 1518 A sexies

### RT-FUTFISC-31 — 302 bis ZL : transition renvoyant à des modalités abrogées en 2027

*P2, confirmé, incohérence du projet.* Effet limité aux prélèvements devenus exigibles entre le 1er janvier 2027 et la suppression ; le texte de transition les soumettrait à des modalités déclaratives que la loi a déjà remplacées. Il en résulte une incertitude de procédure, sans perte de droits démontrée.

La proposition maintient, pour les créances anciennes, les trois modes de dépôt sur la déclaration 287. Depuis le 1er janvier 2027, la loi déjà publiée soumet ces prélèvements à la constatation de L. 161-1 du CIBS. La réforme ne pouvant entrer en vigueur avant cette date, les exigibilités de 2027 jusqu'à la réforme seraient renvoyées à des modalités abrogées. La dernière phrase contredit la précédente. Les notes croient l'article abrogé en 2027 et en tirent qu'il n'y a pas de gain à compter. C'est inexact : la version 2027 maintient la procédure, et le gain dépend des articles d'assiette ZG, ZH, ZI et ZO.

**Correction minimale.** Remplacer la liste des modalités par un renvoi aux règles « applicables à la date de leur exigibilité » : annexe 287 pour les exigibilités antérieures au 1er janvier 2027, L. 161-1 du CIBS ensuite. Supprimer la phrase contradictoire. Voir C4-redactions.md, § 2.

**À préserver.** Régularisations, restitutions, prescriptions, garanties et recours des prélèvements anciens ; Absence de déclaration à néant.

**Articles.** cgi 302 bis ZL

### RT-FUTFISC-32 — Anomalies de source LEGI : versions de durée nulle, NOTA discordantes, bases anciennes, renvois morts, coquilles

*P2, confirmé, conflit de source.* Anomalies documentaires LEGI sans effet normatif démontré, mais qui brouillent l'identification du texte applicable au 1er janvier 2027.

Trois numéros (1609 tertricies, 1613 quater, 1613 ter) ont deux versions qui commencent le 2027-01-01, dont une de durée nulle issue de l'ordonnance 2025-1247 art. 10 ; l'autre, issue de la LF 2025 art. 38, porte un lien « ABROGATION » de l'art. 17 de la même ordonnance et finit au 2222-02-22. Onze versions futures gardent la NOTA d'origine (« 1er septembre 2026 ») alors que LEGI les fait débuter au 2027-01-01 conformément à l'art. 17 de l'ord. 2026-671. La NOTA de la version courante de 1613 ter annonce une entrée au 1er janvier 2027 pour une version en vigueur depuis le 1er juillet 2026. 1) La version 1600 de 2027 retire l'EPCI de Corse de la répartition, mais les versions 2028, 2029 et 2030, issues de la LF 2025 art. 62, le rétablissent : soit la consolidation LEGI a omis la modification de 2027 dans les versions suivantes, soit la LF 2025 a réécrit la phrase. 2) Plusieurs NOTA annoncent une date d'application différente de la borne de début de version (1er septembre 2026, 2027, 2030). La date d'application à retenir est celle du texte JORF, pas la borne LEGI. 3) La version 2030 de 1681 septies renvoie à 1635 bis AD, abrogé depuis 2021. 4) La version 2030 de 1647 B sexies contient une phrase lacunaire. Une red-team ne peut pas trancher sans le JORF ; aucune de ces anomalies ne doit être recopiée dans une rédaction fusionnée. La version 2027 remplace « code des impositions sur les biens et services » par « code des impositions des biens et services », dénomination inexistante. La proposition garde la dénomination exacte ; la fusion du 5° bis (L. 213-104 CIBS) doit être faite sans reprendre cette coquille. (1) 235 ter X : deux versions futures commencent le même jour. L'une, issue de l'ordonnance, a une durée nulle et met en place la constatation par L. 161-1 CIBS. L'autre, issue de la LF 2025, maintient la déclaration sur annexe 287 et court jusqu'à la borne technique 2222-02-22. On ne sait pas quel mode déclaratif s'applique en 2027. (2) 235 ter ZE bis : la NOTA annonce l'abrogation en 2029 et le taux s'arrête à 2028, mais la version 2027 n'a pas de fin normative. (3) 256 C et 287 : la NOTA les dit abrogés au 1er janvier 2027 par l'ordonnance, avec maintien jusqu'à reprise réglementaire, alors que la LF 2025 les réécrit au même jour, avec une version LEGI sans terme. Les bornes 2222-02-22 et 2999-01-01 ne sont pas des dates normatives. Constats propres de l'agent principal. Les NOTA des versions 2027 de 1464 A, 1515, 1651, 1651 F, 1651 H et 1651 M annoncent une entrée « le 1er septembre 2026 », alors que la version LEGI débute le 2027-01-01 ; ces NOTA n'ont pas été mises à jour après l'ordonnance 2026-671, art. 17. La NOTA de 1635 quinquies (2029) cite une « ordonnance n° 2026-674 » alors que le lien vise l'ordonnance 2026-671. La version 2030 de 1736 (LEGIARTI000047006062, créée en 2021) est construite sur une base ancienne : elle ne contient plus le 6 (amende DAC7), ni les XIV et XV, et répète au XI le texte du XIII ; l'instruction de la LF 2022 art. 132 ne porte en réalité que sur le III. La version courante de 289 bis finit au 2222-02-22 alors que la version suivante débute le 2030-07-01. Les « articles réservés » 1419 à 1446 et 1481 à 1493 bis débutent au 2222-02-22 (borne technique, sans effet). La NOTA de la version 2027 de 1741 cite une « ordonnance n° 2026-1247 du 17 décembre 2026 » (B1-07). Aucune de ces anomalies ne doit être recopiée dans une rédaction fusionnée.

**Correction minimale.** Réserve documentaire : viser dans la réforme « la rédaction en vigueur à la date de publication de la présente loi » ; signaler les NOTA discordantes à la DILA, sans corriger silencieusement.

**À préserver.** Dates normatives du 1er janvier 2027 (à distinguer de la borne 2222-02-22).

**Articles.** cgi 1383-0 B, cgi 1419 à 1446, cgi 1460, cgi 1464 A, cgi 1481 à 1493 bis, cgi 1509, cgi 1515, cgi 1519 A, cgi 1519 B, cgi 1586 quater, cgi 1586 ter, cgi 1594 F quinquies, cgi 1594-0 G, cgi 1600, cgi 1609 duotricies, cgi 1609 sexdecies C, cgi 1609 tertricies, cgi 1613 quater, cgi 1613 ter, cgi 1622, cgi 1635 quinquies, cgi 1647, cgi 1647 B sexies, cgi 1647 B sexies A, cgi 1649 quater B quater, cgi 1649 quater H, cgi 1651, cgi 1651 F, cgi 1651 H, cgi 1651 M, cgi 1681 septies, cgi 1736, cgi 207, cgi 235 ter X, cgi 235 ter ZE bis, cgi 256 C, cgi 287, cgi 289 bis

### RT-FUTFISC-33 — Inventaire : seconde passe sans versions futures ; ABROGE_DIFF lu comme abrogation ; nouveaux numéros non inventoriés

*P2, confirmé, anomalie d'inventaire.* Défaut de méthode de la seconde passe, visible dans au moins 10 notes du lot ; effet normatif direct seulement pour 150 VM (C1-01), sinon risque de mauvais bilan et de clauses superflues.

La seconde passe n'a pas disposé des versions futures déjà publiées et a lu l'état ABROGE_DIFF comme une extinction. Cela a produit des clauses de « continuité après 2027 » sans objet (119 ter 5, 125-00 A), une clause d'extinction réelle (150 VM), une phrase ambiguë (1382-0 V) et une sous-évaluation des suppressions (1622 : la déclaration supprimée subsiste dans la version 2027). La seconde passe n'a pas eu accès aux versions futures. Elle a lu l'état ABROGE_DIFF comme une possible fin des taxes en 2027 et a minoré la suppression : la taxe bureaux PACA, la taxe sur les excédents de provisions et la taxe de 8 % sur les rachats continuent en 2027. Leur suppression est donc une baisse réelle, à compter dans le bilan. Pour 299 septies, les notes affirment à tort que 302 septies A n'est pas aboli ; le régime simplifié de TVA disparaît en 2027. Synthèse de l'agent principal : sur les 178 entrées, les notes ou motifs de nombreuses propositions (fichier de classification, champ notes_misread_abroge_diff) lisent l'état ABROGE_DIFF d'une version remplacée comme une abrogation ou une « extinction ». Exemples : « Source annoncée abrogée au 1er janvier 2027 » (302 septies A bis), « La disposition de recodification ou de remplacement n'est pas fournie dans ce lot » (1744, 1756, 1746, 1751 A), « Abrogation différée au 1er août 2027 » (annexe II 279). La seconde passe n'a donc pas disposé des versions futures, comme XCUT l'établissait. Les dix nouveaux numéros futurs du paquet (1496 ter, 1788 F, 1647 B sexies A, 1649 quater E et H, 1518 A quinquies A, 256-00, annexe II 310 HC, 1419 à 1446, 1481 à 1493 bis) ne sont pas inventoriés ; deux portent une charge nouvelle ou rétablie contraire aux orientations (RT-FUTFISC-12 et 26) et deux autres font renaître des obligations (RT-FUTFISC-16).

**Correction minimale.** Pour chaque proposition dont la source porte ABROGE_DIFF avec successeur, remplacer les mentions d'abrogation ou d'extinction au 1er janvier 2027 par une référence à la rédaction applicable à compter de cette date ; supprimer la phrase finale du V de 1382-0 ; compter la suppression de 1622 comme effective. Ajouter à l'inventaire de seconde passe les versions VIGUEUR_DIFF et les nouveaux numéros futurs, et rattacher à chaque proposition l'identifiant de la version qui lui succède.

**À préserver.** Les clauses de maintien des avantages après 2027, qui sont inoffensives.

**Articles.** cgi 1042, cgi 119 ter, cgi 125-00 A, cgi 1382-0, cgi 150 VM, cgi 1509, cgi 1582, cgi 1609 sexdecies C, cgi 1609 sexvicies, cgi 1613 quater, cgi 1622, cgi 231, cgi 231 A, cgi 231 bis L, cgi 231 quater, cgi 235 ter X, cgi 235 ter XB, cgi 299 septies

## 5. Propositions de correction (rédactions complètes)

Les rédactions ci-dessous sont présentées séparément des constats. Elles ont été produites par l'agent principal (R-OWN) et par les lots. Les identifiants de lot cités (A-01, B1-07, C1-01, etc.) correspondent aux objections définitives suivantes : A-01 → RT-FUTFISC-13; A-02 → RT-FUTFISC-14; A-03 → RT-FUTFISC-32; A-04 → RT-FUTFISC-16; A-05 → RT-FUTFISC-15; B1-01 → RT-FUTFISC-17; B1-02 → RT-FUTFISC-18; B1-03 → RT-FUTFISC-19; B1-04 → RT-FUTFISC-20; B1-05 → RT-FUTFISC-21; B1-06 → RT-FUTFISC-22; B1-07 → RT-FUTFISC-02; B1-08 → RT-FUTFISC-24; C1-01 → RT-FUTFISC-23; C1-02 → RT-FUTFISC-30; C1-04 → RT-FUTFISC-07; C1-06 → RT-FUTFISC-33; C1-07 → RT-FUTFISC-32; C2-01 → RT-FUTFISC-08; C2-02 → RT-FUTFISC-09; C2-03 → RT-FUTFISC-07; C2-04 → RT-FUTFISC-07; C2-05 → RT-FUTFISC-09; C2-06 → RT-FUTFISC-29; C2-07 → RT-FUTFISC-32; C3-01 → RT-FUTFISC-04; C3-02 → RT-FUTFISC-05; C3-03 → RT-FUTFISC-03; C3-04 → RT-FUTFISC-03; C3-05 → RT-FUTFISC-29; C3-06 → RT-FUTFISC-32; C3-07 → RT-FUTFISC-33; C4-01 → RT-FUTFISC-25; C4-02 → RT-FUTFISC-31; C4-03 → RT-FUTFISC-07; C4-05 → RT-FUTFISC-06; agent principal → RT-FUTFISC-01. Les mécanismes « RT-FUTFISC-xx » cités à l'intérieur des rédactions de lot sont des codes provisoires de travail, non les identifiants définitifs. Les rédactions ne sont pas validées par un juriste. Les subdivisions des lois différées doivent être vérifiées au JORF avant tout dépôt.


### Rédactions — Agent principal

##### R-OWN-1 — CGI 1788 F (nouveau numéro au 1er janvier 2027) et 262-0 bis : agrément de l'opérateur de détaxe

Pièces lues : 1788 F LEGIARTI000054561288 (VIGUEUR_DIFF 2027-01-01, ord. 2026-671 art. 7), 262-0 bis LEGIARTI000053562169 (source, NOTA, proposition, motif et notes en entier).

Constat : le projet de 262-0 bis supprime l'agrément d'opérateur de détaxe, sa caducité en cas de cession ou de prise de contrôle et l'amende sanctionnant son absence (III B et C, « (Abrogé) »). Mais la NOTA de 262-0 bis prévoit son abrogation au 1er janvier 2027, avec maintien provisoire des I (2e alinéa et suivants) et II « jusqu'à leur reprise par les mesures réglementaires mentionnées au 4° de l'article L. 213-15 et article L. 215-40 du code des impositions sur les biens et services ». Le nouvel article 1788 F, au 1er janvier 2027, reprend la caducité (III) et l'amende de 300 000 € pour l'exercice sans agrément, avec interdiction de trois ans (IV), en visant « l'agrément … mentionné au 1° de l'article L. 215-40 » du CIBS. La réforme, qui ne peut guère entrer en vigueur avant 2027, viserait un article 262-0 bis déjà largement abrogé. L'agrément et ses sanctions survivraient dans le CIBS et dans 1788 F.

Rédaction proposée (loi de réforme, article de coordination) :

« I. – L'article 1788 F du code général des impôts est ainsi rédigé :

"Art. 1788 F. – I. – Le non-respect par un intermédiaire intervenant dans la production ou la transmission de la preuve de l'exportation, pour l'application de l'exonération prévue au 2° de l'article L. 213-12 du code des impositions sur les biens et services, des obligations techniques de transmission, de gestion des risques, de formation de son personnel et de justification de l'exportation qui lui incombent est constaté par l'administration. Il entraîne, après un délai de trente jours laissé à l'intéressé pour présenter ses observations, l'application d'une amende dont le montant ne peut excéder 300 000 €.

II. – L'autorité administrative prononce la sanction prévue au I après application de la procédure prévue aux articles L. 122-1 et L. 122-2 du code des relations entre le public et l'administration.

III. – L'exercice de l'activité mentionnée au I n'est subordonné à aucun agrément. Aucune caducité, aucune amende et aucune interdiction de solliciter un agrément ne peuvent être prononcées au seul motif de l'absence d'agrément, de la cession du fonds de commerce ou de la prise de contrôle de l'intermédiaire."

II. – Le 1° de l'article L. 215-40 du code des impositions sur les biens et services, en tant qu'il soumet à agrément les intermédiaires mentionnés au I de l'article 1788 F du code général des impôts, est abrogé. [Coordination hors des cinq codes : le texte de L. 215-40 n'est pas dans le corpus. Elle est à vérifier avant rédaction définitive.]

III. – Le I s'applique aux manquements commis à compter de l'entrée en vigueur de la présente loi. Les sanctions non définitives prononcées sur le fondement des anciens III B et C de l'article 262-0 bis, ou des III et IV de l'article 1788 F dans leur rédaction antérieure, bénéficient de la loi répressive plus douce. Les décisions définitives, les restitutions, les prescriptions et les recours restent régis par les règles antérieures. Les certifications techniques d'interconnexion déjà délivrées restent valables. »

Dépendances : la proposition de 262-0 bis (V) et les annexes II 202 E à 202 O, III 75 A et IV 50 sexies L doivent suivre la même logique. La réforme ne peut supprimer l'agrément en ne réécrivant que 262-0 bis.

##### R-OWN-2 — CGI 1496 ter (nouveau numéro au 1er janvier 2029) : déclaration annuelle des loyers

Pièces lues : 1496 ter LEGIARTI000041403640 (VIGUEUR_DIFF 2029-01-01, NOTA : reports successifs 2024 → 2026 → 2029), 1418 LEGIARTI000053546060 (source et proposition), 1729 C LEGIARTI000042913666 (proposition).

Constat : le projet allège la déclaration d'occupation de 1418. Il en retire le type de location, les dates d'occupation et le motif de vacance. Or 1496 ter crée en 2029, pour les propriétaires bailleurs, une seconde déclaration annuelle avant le 1er juillet portant sur « les informations relatives à ces biens et au montant du loyer au 1er janvier ». Cette déclaration n'est pas inventoriée. Le projet maintient même l'amende de 150 € qui la sanctionne (1729 C proposé).

Option A, conforme à l'orientation de suppression des formalités sans remplacement :

« I. – L'article 1496 ter du code général des impôts est abrogé. Les mots : ", à l'article 1496 ter" sont supprimés de l'article 1729 C du même code.

II. – Les informations nécessaires à la révision des valeurs locatives des locaux d'habitation sont établies à partir des données dont l'administration dispose déjà légalement. Aucune déclaration, aucun relevé ni aucune attestation de remplacement ne peut être exigé des propriétaires à ce titre.

III. – Le I s'applique dès son entrée en vigueur, y compris pour les déclarations qui n'avaient pas encore été souscrites. Les déclarations déjà déposées ne sont pas renouvelées. »

Option B, si une fonction essentielle de la révision est démontrée : fusionner l'information sur le loyer dans la déclaration unique de 1418 (même échéance du 1er juillet, même dispense en l'absence de changement), sans seconde déclaration. Cette option va contre l'allègement de 1418 proposé et suppose une décision expresse de l'auteur.

Incertitudes : le dispositif de révision (loi 2019-1479, art. 146) est hors des cinq codes et n'est pas réécrit. Le coût budgétaire et la faisabilité d'une révision sans déclaration ne sont pas établis.


### Rédactions — Lot C1

### Lot C1 : rédactions fusionnées proposées

Ces rédactions sont applicables à compter de l'entrée en vigueur de la loi de réforme, nécessairement postérieure au 1er janvier 2027. Elles partent de la rédaction en vigueur à cette date, qui est la version VIGUEUR_DIFF de l'instantané 20261026T230545Z, et reprennent les choix de fond du projet. Les renvois au CIBS reproduisent ceux de la version future ; leur contenu n'est pas vérifié, car le CIBS est hors corpus. Il s'agit d'une revue IA, qui ne remplace pas une validation par un juriste.

---

#### 1. CGI art. 150 VM (objection C1-01)

Base : LEGIARTI000053154469 (2027-01-01), à laquelle s'ajoute la réforme de LEGIARTI000030752146 : plus de déclaration ni de paiement pour les exportations sans cession. La clause d'extinction au 1er janvier 2027 est supprimée.

> I. – Une déclaration, conforme à un modèle établi par l'administration, retrace, selon le cas, les éléments servant à la liquidation de la taxe ou l'option prévue à l'article 150 VL. Elle est déposée :
>
> 1° Pour les cessions réalisées avec la participation d'un intermédiaire domicilié fiscalement en France ou, en l'absence d'intermédiaire, lorsque l'acquéreur est un assujetti à la taxe sur la valeur ajoutée établi en France, par cet intermédiaire ou cet acquéreur, au service des impôts chargé du recouvrement dont il dépend ou, lorsqu'il s'agit d'un officier ministériel, au service des impôts chargé du recouvrement compétent pour l'enregistrement de l'acte lorsqu'il doit être présenté à cette formalité, dans le délai prévu par l'article 635.
>
> Toutefois, lorsqu'il est assujetti à la taxe sur la valeur ajoutée, l'intermédiaire, l'acquéreur ou l'officier ministériel constate la taxe dans les conditions prévues à l'article L. 161-1 du code des impositions sur les biens et services ;
>
> 2° Pour les cessions dans un pays tiers de biens exportés temporairement, par l'exportateur à la recette des douanes compétente pour cette exportation, lors de l'accomplissement des formalités douanières ;
>
> 3° Pour les autres cessions, par le vendeur au service des impôts chargé du recouvrement dont il relève dans un délai d'un mois à compter de la cession.
>
> II. – La taxe est acquittée lors du dépôt de la déclaration.
>
> III. – Le recouvrement de la taxe s'opère :
>
> 1° Pour les cessions réalisées avec la participation d'un intermédiaire ou, en l'absence d'intermédiaire, lorsque l'acquéreur est un assujetti à la taxe sur la valeur ajoutée établi en France, dans les conditions prévues par les dispositions du livre II du présent code et du livre des procédures fiscales qui sont applicables aux taxes sur les biens et services ;
>
> 2° Pour les cessions dans un pays tiers de biens exportés temporairement, selon les dispositions prévues par la législation douanière en vigueur ;
>
> 3° Pour les autres cessions, selon les règles, garanties et sanctions prévues au titre IV du livre des procédures fiscales pour les impôts recouvrés par les comptables publics compétents.
>
> IV. – Les réclamations sont présentées, instruites et jugées dans les conditions prévues par les dispositions du livre II du présent code et du livre des procédures fiscales qui sont applicables aux taxes sur les biens et services si la taxe est recouvrée par les comptables de la direction générale des finances publiques et dans les conditions prévues par les dispositions du code des douanes qui sont applicables aux droits de douane si la taxe est recouvrée par les receveurs des douanes.
>
> V. – Les dispositions du présent article issues de la loi n° … du … s'appliquent aux exportations et cessions réalisées à compter de son entrée en vigueur. Les faits générateurs antérieurs demeurent régis par les dispositions qui leur étaient applicables, y compris celles issues de l'ordonnance n° 2025-1247 du 17 décembre 2025, avec leurs exonérations, options, obligations, imputations, restitutions, prescriptions et recours, même lorsque leur échéance est ultérieure. Aucun remboursement général des taxes légalement dues n'est institué, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives. Les exportations réalisées sans cession à compter de cette entrée en vigueur ne donnent lieu à aucune déclaration ni à aucun paiement au titre du présent article, y compris pour exercer l'option prévue à l'article 150 VL. Les formalités douanières et patrimoniales ayant un objet distinct demeurent applicables.

Justification : la phrase « ne proroge pas l'application du présent article au-delà de sa date d'abrogation déjà prévue au 1er janvier 2027 » repose sur une abrogation qui n'existe pas. Elle rendrait l'article réformé inapplicable dès son entrée en vigueur. Les a à c renvoyaient à l'article 302 septies A, abrogé sans successeur au 2027-01-01.
Dépendances : 150 VI, et 150 VG I 3° proposé ; article L. 161-1 du CIBS (hors corpus).

---

#### 2. CGI art. 1518 A sexies (objection C1-02)

Base : LEGIARTI000053589487 (2027-01-01), à laquelle s'ajoute la réforme de LEGIARTI000053545912 : le reliquat de réduction est transmis lors du seul changement d'exploitant.

> I. – En cas de changement de méthode de détermination de la valeur locative d'un bâtiment ou terrain industriel en application des articles 1499-00 A ou 1500, la variation de la valeur locative qui en résulte fait l'objet d'une réduction dans les conditions prévues au II du présent article.
>
> Cette réduction s'applique également à la variation de la valeur locative résultant d'un changement d'affectation au sens de l'article 1406 pour les locaux mentionnés au premier alinéa du présent I nouvellement affectés à un usage professionnel ou réciproquement.
>
> II. – A. – La réduction prévue au I s'applique lorsque la variation de valeur locative excède 30 % de la valeur locative calculée avant la prise en compte du changement prévu au même I et, le cas échéant, après l'application de l'avant-dernier alinéa de l'article 1467 et de l'article 1518 A quinquies.
>
> La réduction est égale à 85 % du montant de la variation de valeur locative la première année où le changement est pris en compte, à 70 % la deuxième année, à 55 % la troisième année, à 40 % la quatrième année, à 25 % la cinquième année et à 10 % la sixième année.
>
> Le seul changement d'exploitant ne met pas fin à la réduction prévue au premier alinéa du présent A ; le nouvel exploitant en bénéficie pour les années restant à courir, sans recommencement de la période de six ans. Lorsque le bâtiment ou terrain est concerné par l'application du I de l'article 1406, la réduction de valeur locative cesse de s'appliquer pour les impositions établies au titre de l'année qui suit la réalisation de ce changement.
>
> B. – Lorsqu'un rôle particulier est établi en application de l'article 1508, la réduction de la variation de valeur locative prévue au A du présent II s'applique à compter de la première année au titre de laquelle les bases rectifiées sont prises en compte dans les rôles généraux.
>
> III. – Le cas échéant, pour les locaux qui bénéficient au 31 décembre 2026 du présent article, la réduction cesse de s'appliquer lorsque la valeur locative est actualisée en application du A du III de l'article 1518 ter. Ces locaux relèvent alors, le cas échéant, de l'article 1518 A quinquies A.
>
> IV. – La règle de maintien de la réduction en cas de changement d'exploitant s'applique aux impositions établies au titre des années commençant à compter du 1er janvier suivant l'entrée en vigueur de la loi n° … du …, pour les réductions qui n'ont pas cessé en application du III, y compris si le changement d'exploitant est antérieur, pour la seule durée restant à courir. Elle ne rouvre ni une période de six ans expirée ni une réduction éteinte en application du III. Les impositions des années antérieures, leurs dégrèvements, restitutions et recours restent régis par les dispositions qui leur étaient applicables.

Justification : l'ancien III renvoyait au 3 des I et III de 1518 A quinquies, abrogé en 2027. Le reprendre ferait coexister la réduction et le lissage de 1518 A quinquies A, soit un double avantage que personne n'a décidé. L'avantage propre au projet (transmission du reliquat) est conservé pour toutes les réductions encore en cours.
Option alternative : voir C1-02, other_options.

---

#### 3. CGI art. 1509 (objection C1-03)

Base : LEGIARTI000053188717 (2027-01-01), à laquelle s'ajoutent les deux suppressions de LEGIARTI000027517709.

> I. – La valeur locative des propriétés non bâties établie en raison du revenu de ces propriétés résulte des tarifs fixés par nature de culture et de propriété, conformément aux règles tracées par l'instruction ministérielle du 31 décembre 1908.
>
> II. – Pour le calcul de la valeur locative, les pépinières exploitées sur terrains non aménagés doivent être comprises dans la catégorie des " terres " à la classe correspondant aux caractéristiques du terrain.
>
> III. – La valeur locative prise en compte pour le calcul de la taxe foncière afférente aux bois, aux landes et aux étangs ainsi qu'aux terres utilisées principalement pour la chasse et n'appartenant pas à une commune ou un groupement de communes, inclut celle du droit de chasse effectivement perçu sur ces propriétés à moins :
>
> - que ce droit n'ait été apporté à une association communale ou intercommunale de chasse agréée ;
>
> - ou que la propriété n'ait été classée en réserve naturelle ou en réserve de chasse agréée.
>
> IV. – À compter de l'entrée en vigueur de la loi n° … du …, les terres incultes ou manifestement sous-exploitées ne sont plus inscrites dans la catégorie des meilleures terres labourables sur le seul fondement de leur inscription à l'état prévu à l'article L. 125-5 du code rural et de la pêche maritime. Aucune somme complémentaire ne naît sur ce fondement à compter de cette date. Les sommes légalement dues avant cette date restent régies par les dispositions antérieures, y compris les conditions de mise en recouvrement dans le délai de trois ans, les remboursements en cas d'annulation de l'arrêté préfectoral ou d'absence de mise en exploitation dans le délai d'un an, l'exclusion des fonds en nature de bois et les voies de recours.
>
> V. – Pour les cessions intervenant à compter de la même date, la cession d'un terrain autre que ceux classés dans la catégorie fiscale des terrains à bâtir, soumise à la taxe sur la valeur ajoutée en application des dispositions du livre II du code des impositions sur les biens et services, n'entraîne plus l'imposition à la taxe foncière sur les propriétés non bâties en tant que terrain à bâtir au titre de l'année de la cession et des deux années précédentes. La taxe foncière de droit commun demeure applicable. Les cessions antérieures restent soumises au V du présent article dans sa rédaction applicable à la date de la cession, y compris l'imputation de la taxe déjà acquittée, les droits à restitution, les prescriptions et les recours.

Justification : le critère de la suppression est rédigé dans les termes de la version 2027, et non plus par renvoi au I de l'article 257, dont l'abrogation est programmée. La transition vise la rédaction en vigueur à la date de chaque cession, qui couvre aussi la rédaction 2027.


### Rédactions — Lot C3

### Lot C3 — rédactions proposées (FUT-FISC)

Ces textes sont des propositions de red-team. Ils n'ont pas été validés par un juriste. Ils fusionnent la version future publiée (instantané 20261026T230545Z) avec les choix du projet, sans taux ni formalité nouveaux. Le contenu du CIBS (L. 161-1, L. 172-3, L. 231-66, L. 231-100, L. 234-2…) est hors corpus : les renvois y sont repris tels que les versions LEGI 2027 les écrivent, sans en inventer le contenu.

#### 1. CGI article 287 (objection C3-01) — rédaction entière, base LEGIARTI000051190827 (LF 2025 art. 38, en vigueur au 1er janvier 2027)

Seul changement de fond par rapport à la version 2027 : le délai supplémentaire d'un mois devient un choix sans autorisation, comme le voulait la proposition (sha 88599d44…). Le régime simplifié annuel et ses acomptes, déjà supprimés par la LF 2025, ne sont pas rétablis. La transition reprend le 8 proposé, en tenant compte de la date d'effet de la LF 2025.

> 1. Tout redevable de la taxe sur la valeur ajoutée identifié conformément aux dispositions combinées des articles 286 ter et 286 ter A est tenu de remettre au service des impôts dont il dépend et dans le délai fixé par arrêté une déclaration conforme au modèle prescrit par l'administration.
>
> 2. La déclaration prévue au 1 comprend, d'une part, le montant total des opérations réalisées, d'autre part, le détail des opérations taxables. Elle est déposée chaque mois ou, lorsque les conditions prévues au 3 sont remplies, chaque trimestre civil.
>
> Les redevables qui déposent mensuellement la déclaration peuvent, à leur choix et sans demande, déclaration d'option ni autorisation préalable, disposer d'un délai supplémentaire d'un mois dans les conditions fixées par arrêté du ministre chargé de l'économie. Cet arrêté ne peut subordonner ce choix à un accord de l'administration ni à une formalité distincte. Les obligations de versement prévues à l'article 1693 s'appliquent aux redevables qui exercent ce choix.
>
> 3. Les redevables déposent la déclaration prévue au 1 chaque trimestre civil lorsqu'ils n'ont pas réalisé un chiffre d'affaires majoré des acquisitions taxables supérieur à :
>
> a) 1 000 000 € pendant l'année civile précédente ;
>
> b) 1 100 000 € pendant l'année en cours.
>
> Le chiffre d'affaires majoré des acquisitions taxables qui sert de référence pour l'application des seuils prévus aux a et b est le chiffre d'affaires déterminé dans les conditions prévues à l'article 293 D, majoré du montant, hors taxe sur la valeur ajoutée, des opérations pour lesquelles le déclarant est redevable en application des 2 à 2 decies de l'article 283, du 2 de l'article 293 A, du 2 du II de l'article 277 A ou du 4° du 1 de l'article 298.
>
> En cas de dépassement du seuil mentionné au b du présent 3 en cours d'année, les redevables déposent mensuellement leur déclaration à compter du premier jour du mois au cours duquel ce dépassement est intervenu. La première déclaration mensuelle déposée par le redevable récapitule les opérations qu'il a effectuées depuis le premier jour du trimestre civil en cours.
>
> Les seuils prévus aux a et b sont indexés sur l'inflation, avec une évolution tous les trois ans dans les conditions prévues au chapitre II du titre III du livre Ier du code des impositions sur les biens et services. Les valeurs révisées sont arrondies au millier d'euros.
>
> 3 bis. Les redevables qui remplissent les conditions mentionnées au 3 pour déposer la déclaration mentionnée au 1 par trimestre peuvent opter pour un dépôt mensuel. L'option prend effet le premier jour du mois du trimestre civil suivant celui au cours duquel elle est exercée ou au premier jour d'un trimestre civil ultérieur précisé par le déclarant.
>
> L'option s'applique pour une période au moins égale à quatre trimestres civils. Au terme de cette période, la révocation prend effet le premier jour du trimestre civil suivant celui au cours duquel elle a été exprimée ou le premier jour d'un trimestre civil ultérieur précisé par le déclarant.
>
> Le redevable exerce l'option et la révocation auprès du service des impôts dont il dépend.
>
> 3 ter. (Abrogé).
>
> 4. En cas de cession ou de cessation d'une activité professionnelle, les redevables sont tenus de souscrire dans les trente jours la déclaration prévue au 1. Toutefois, ce délai est porté à soixante jours pour les entreprises placées sous le régime simplifié d'imposition.
>
> 5. [inchangé : a à c de la version LEGIARTI000051190827, reproduits intégralement]
>
> 6. [inchangé : a à c de la version LEGIARTI000051190827, reproduits intégralement]
>
> 7. Pour chacun de ses membres constitués en secteur d'activité, l'assujetti unique communique les informations figurant sur la déclaration mentionnée au 1 ainsi que des informations sur les opérations réalisées à destination des autres membres, selon des modalités fixées par arrêté du ministre chargé du budget.
>
> 8. Le choix du délai supplémentaire prévu au 2 est ouvert aux déclarations dont l'échéance n'est pas expirée à la date d'entrée en vigueur de la présente loi, y compris pour les redevables déjà en activité ; les délais supplémentaires déjà accordés sont conservés. Les déclarations, acomptes et liquidations afférents aux périodes antérieures au 1er janvier 2027, ainsi qu'aux exercices en cours à cette date mentionnés au second alinéa du VI de l'article 38 de la loi n° 2025-127 du 14 février 2025 de finances pour 2025, demeurent régis par les règles qui leur sont applicables. Toutefois, aucun acompte du régime simplifié dont l'échéance intervient à compter de l'entrée en vigueur de la présente loi n'est exigé : les sommes déjà versées sont imputées une seule fois sur la taxe due et leur excédent est remboursé selon les règles applicables aux crédits de taxe, sans déclaration de modulation. Ces dispositions ne réduisent ni la taxe définitivement due ni les droits à déduction, exonération, restitution ou recours.
>
> Les présentes dispositions ne rétablissent aucune disposition abrogée par la loi n° 2025-127 du 14 février 2025 ou par l'ordonnance n° 2025-1247 du 17 décembre 2025. Elles s'appliquent, dans les mêmes termes, aux mesures prises pour l'application des articles L. 161-1 et L. 172-3 du code des impositions sur les biens et services qui reprennent le présent article.

Justification : le régime trimestriel de la LF 2025 vaut déjà suppression des acomptes semestriels. Le seul apport du projet qui subsiste est le délai supplémentaire sans autorisation. Le 4 conserve la mention « régime simplifié » de la version 2027, qui est un défaut de source : le délai de soixante jours pourrait être réservé aux redevables trimestriels du 3, mais c'est un choix de fond (extension de faveur) à faire valider.

Dépendances : 1693 (terme « autorisés ») ; annexe II 242-0 C III, 242 sexies, 242 septies A et 242 septies J ; annexe III 383 ter ; annexe IV 39 ; 256 C (C3-02) ; 299 septies (C3-08) ; reprises CIBS L. 161-1 et L. 172-3 (hors corpus). Réserve : l'articulation avec l'abrogation de 287 par l'ordonnance 2025-1247, avec maintien jusqu'à reprise, n'est pas vérifiée sur le JORF (C3-06).

#### 2. CGI article 238 bis, 6 (objection C3-05) — passage

Remplacer le 6 proposé par :

> 6. (Abrogé).

Et compléter le 9 proposé, après sa première phrase :

> Aucune déclaration prévue à l'ancien 6 du présent article n'est due pour les transmissions dont l'échéance intervient à compter du 1er janvier 2027. Aucune sanction ne peut être prononcée pour le défaut d'une telle transmission, et aucune déclaration, liste de bénéficiaires ou transmission de remplacement n'est instituée. Les éléments nécessaires au calcul de la réduction dans la déclaration de droit commun et la preuve prévue au 5 bis demeurent.

Justification : rédaction alignée sur la loi n° 2026-403 (art. 6, entrée en vigueur au 1er janvier 2027), sans l'a contrario de la formule « à compter de l'entrée en vigueur de la présente loi ». Dépendance : 1729 B (version 2027 déjà purgée du renvoi à 238 bis).

#### 3. CGI article 220 Z septies, III et IV (objections C3-03 et C3-04) — passages, base LEGIARTI000054567230

> III.-Le bénéfice du I du présent article est accordé aux personnes morales mentionnées au même I qui sont propriétaires ou titulaires de l'usufruit de logements locatifs intermédiaires au sens de l'article L. 231-66 du code des impositions sur les biens et services. Pour l'application du présent article, aucune condition de mixité du programme ou de proportion communale de logements sociaux supprimée par la loi supprimant les quotas communaux obligatoires de logements sociaux ne peut être opposée à la naissance ou au maintien de la créance, y compris pour les logements acquis ou construits antérieurement, et la condition de location en exonération de la taxe sur la valeur ajoutée n'est pas exigée.
>
> IV.-Le I du présent article s'applique pendant une durée de vingt ans à compter de la première mise en recouvrement de la taxe foncière sur les propriétés bâties pour les logements mentionnés au III.
>
> La durée de vingt ans est réduite à due concurrence du nombre d'années d'exonération totale de la taxe foncière sur les propriétés bâties dont peuvent bénéficier les logements.
>
> Le I cesse de s'appliquer à compter de l'exercice suivant celui au cours duquel le complément de taxe sur la valeur ajoutée devient exigible conformément à l'article L. 231-100 du code des impositions sur les biens et services, sans que la méconnaissance d'une condition mentionnée à la deuxième phrase du III puisse entraîner cette exigibilité au regard du présent article.

Les I, II, V et VI restent ceux de la proposition, VI compris (modèle facultatif, pas de déclaration d'ensemble dédiée). Le dernier alinéa proposé, qui vise le « 4° du I de l'article 279-0 bis A », est remplacé par la deuxième phrase du III ci-dessus. Les créances, restitutions et recours des exercices antérieurs restent régis par leurs règles.

Justification : la version 2027 ne renvoie plus à 279-0 bis A mais à la définition CIBS, et garde un renvoi à 284 II bis, abrogé au 1er janvier 2027. Réserve : le contenu de L. 231-66 et L. 231-100 n'est pas lu. Si la condition de mixité y figure, la neutralisation doit aussi être écrite dans le CIBS.


### Rédactions — Lot C2

### Lot C2 — rédactions complètes proposées (FUT-FISC)

Ces rédactions partent des propositions courantes de l'instantané 20261026T230545Z et des versions VIGUEUR_DIFF du 1er janvier 2027. Elles ne présument pas le contenu du CIBS. Les articles du CIBS cités sont ceux que vise la version 2027 publiée. Aucune n'a été validée par un juriste.

#### 1. CGI 1770 duodecies (C2-01). Proposition LEGIARTI000053546759, version 2027 LEGIARTI000054567638

**Article 1770 duodecies.** (Abrogé.)

**Disposition de coordination de la loi de réforme :**

I. L'article 1770 duodecies du code général des impôts est abrogé. L'abrogation porte sur l'article dans toutes ses rédactions, y compris celle qui résulte de l'article 2 de l'ordonnance n° 2026-671 du 27 juillet 2026 et qui est applicable à compter du 1er janvier 2027.

II. À compter de l'entrée en vigueur de la présente loi, aucune amende ne peut être prononcée pour le défaut de production du certificat ou de l'attestation relatifs aux logiciels ou systèmes de caisse, que cette obligation résulte du 3° bis du I de l'article 286 du code général des impôts ou de l'article L. 216-40 du code des impositions sur les biens et services. La réitération et le délai de mise en conformité de soixante jours attachés à cette amende sont supprimés.

III. Les conditions d'inaltérabilité, de sécurisation, de conservation et d'archivage des données restent applicables aux personnes qui y sont assujetties, avec leurs dispenses légales. Les contrôles et les sanctions des manœuvres frauduleuses fondés sur des dispositions distinctes, notamment l'article 1770 undecies, restent applicables. Aucun certificat, attestation, agrément ou déclaration n'est exigé en remplacement.

IV. Le II s'applique aux manquements commis à compter de l'entrée en vigueur de la présente loi. Il s'applique aussi aux manquements antérieurs qui n'ont pas donné lieu à une sanction devenue définitive. Les décisions définitives, les droits en principal, les restitutions, les prescriptions et les recours restent régis par les règles qui leur sont applicables.

*Dépendances :*
- la proposition de 286 3° bis ;
- une coordination à nommer hors des cinq codes, si l'obligation de certificat de L. 216-40 CIBS doit elle-même disparaître ;
- L. 80 O du LPF.

#### 2. CGI 1788 D (C2-02). Proposition LEGIARTI000053546693, version 2027 LEGIARTI000054567750

**Article 1788 D.** (Abrogé.)

**Disposition de coordination de la loi de réforme :**

I. L'article 1788 D du code général des impôts est abrogé dans toutes ses rédactions, y compris celle qui résulte de l'article 2 de l'ordonnance n° 2026-671 du 27 juillet 2026.

II. À compter de l'entrée en vigueur de la présente loi, aucune amende ne peut être prononcée pour le non-respect d'une obligation de transmission que la présente loi supprime. Cela vaut que l'obligation résulte des articles 290 et 290 A du code général des impôts ou des articles L. 216-47 et L. 216-48 du code des impositions sur les biens et services.

III. Les manquements antérieurs à l'entrée en vigueur de la présente loi qui n'ont pas donné lieu à une sanction devenue définitive bénéficient de la règle la plus douce. Ils ne peuvent être sanctionnés au-delà de 250 € par transmission pour l'assujetti et de 750 € par transmission pour la plateforme ou l'opérateur. Les totaux restent plafonnés à 15 000 € et 45 000 € par année civile et par obligation. La dispense de première infraction réparée spontanément, ou dans les trente jours suivant une première demande de l'administration, demeure applicable.

IV. Les décisions définitives, les droits à restitution, les prescriptions et les recours restent régis par leurs règles propres. Les déclarations fiscales distinctes et leurs garanties ne sont pas modifiées.

*Réserve :* la suppression des transmissions L. 216-47 et L. 216-48 doit être rédigée dans le CIBS, hors des cinq codes. Sa conformité au cadre européen de TVA n'est pas présumée. Si cette suppression n'est pas décidée, seul le III (règle plus douce) reste pertinent et la version 2027 doit être acceptée.

#### 3. CGI 1788 E, rédaction fusionnée (C2-05). Proposition LEGIARTI000053546696, version 2027 LEGIARTI000054567685

I. Le numéro d'immatriculation délivré en application de l'article L. 215-39 du code des impositions sur les biens et services peut être retiré :

1° (Abrogé) ;

2° Lorsque l'administration a constaté le non-respect par une plateforme agréée des conditions auxquelles est subordonnée la délivrance du numéro d'immatriculation prévu à l'article L. 215-39 du code des impositions sur les biens et services, ou des obligations de transmission d'informations prévues en application de l'article L. 216-36 du même code, et que cette plateforme, mise en demeure par l'administration de se conformer à ses obligations dans un délai de trois mois, ne lui a pas communiqué dans ce délai tout élément de preuve établissant qu'elle s'y est conformée ou qu'elle a pris les mesures nécessaires pour assurer sa mise en conformité dans un délai raisonnable ;

3° Lorsque l'administration a constaté le non-respect par la plateforme agréée de ses obligations relatives :
- à l'actualisation, dans l'annuaire central prévu au III de l'article 289 bis, des informations nécessaires à l'adressage des factures à recevoir ;
- au changement de plateforme agréée de réception des factures ;
- aux services minimaux que l'ancienne plateforme agréée doit fournir en cas de changement ;

et que cette plateforme, mise en demeure par l'administration de se conformer à ses obligations dans un délai de quinze jours ouvrés, ne lui a pas communiqué dans ce délai tout élément de preuve établissant qu'elle s'y est conformée ou qu'elle a pris les mesures nécessaires pour assurer sa mise en conformité dans un délai raisonnable.

II. Le retrait prononcé en application du I prend effet à l'expiration d'un délai de trois mois à compter de sa notification à la plateforme agréée.

Pour les retraits prononcés avant l'entrée en vigueur de la présente loi sur le fondement du 1° du I dans sa rédaction antérieure, l'exclusion des amendes reste applicable dans les conditions antérieures. Sont concernées les amendes prévues au IV de l'article 1737 et à l'article 1788 D, dans leurs rédactions applicables à la date des sanctions.

L'administration informe les clients de la plateforme agréée du retrait de son numéro d'immatriculation dans un délai d'un mois à compter de la notification de la décision de retrait. Aucune seconde information des mêmes clients n'est imposée à la plateforme.

III. La plateforme agréée dont le numéro d'immatriculation a été retiré peut déposer une nouvelle demande d'immatriculation dans les conditions prévues à l'article L. 215-39 du code des impositions sur les biens et services, sans délai minimal d'attente. Ce dépôt ne suspend pas le retrait et ne dispense pas du respect des conditions de délivrance.

IV. Ces dispositions s'appliquent aux décisions et informations qui restent à intervenir à l'entrée en vigueur de la présente loi.

Après cette date, aucun retrait ne peut être fondé :
- sur les sanctions ou manquements relatifs aux transmissions supprimées des articles 289 E, 290 et 290 A du présent code et des articles L. 216-47 et L. 216-48 du code des impositions sur les biens et services ;
- sur le défaut d'un renouvellement périodique supprimé.

L'information déjà donnée aux clients n'est pas renouvelée. La suppression du délai du III bénéficie aussi aux plateformes dont le retrait a été prononcé avant cette date, sans annuler ce retrait ni rétablir leur numéro. Les garanties, les droits des clients et les recours restent applicables, sous réserve des règles d'application de la loi répressive plus douce.

*Justification :* cette rédaction conserve toutes les coupes de la proposition :
- le 1° est abrogé ;
- la double information des clients est supprimée ;
- le délai de six mois avant nouvelle demande est supprimé.

Elle reprend aussi les renvois CIBS de la version 2027 et neutralise le renvoi erroné de cette version aux « III et IV de l'article 1788 D ».

*Dépendance :* la version future de 289 bis au 1er juillet 2030 (lot B2) peut déplacer l'annuaire central.


### Rédactions — Lot C4

### Lot C4 : rédactions fusionnées proposées

Ces rédactions sont des propositions de red-team, non validées par un juriste. Elles portent sur le texte applicable à compter de l'entrée en vigueur de la réforme, réputée postérieure aux dates d'effet des versions futures (1er janvier 2027 et 1er août 2027). Les articles du CIBS et du CSP cités ne figurent pas dans le corpus : leur contenu n'est pas vérifié.

#### 1. Annexe II, article 276 (objection C4-01, RT-FUTFISC-15)

Base de rédaction : version future LEGIARTI000054411891 (décret n° 2026-612, au 1er août 2027), et non la version courante LEGIARTI000006295637. La proposition courante (numéro d'identification et phrase « cesse de s'appliquer à la date de son abrogation prévue le 1er août 2027 ») est retirée.

> Article 276
>
> I. – La délivrance par l'administration des douanes de l'agrément préalable à l'exercice des activités de fourniture de tabacs manufacturés prévu par l'article L. 3512-14-7 du code de la santé publique est subordonnée à l'ensemble des conditions suivantes :
>
> 1° Etre immatriculé au registre national des entreprises ou, le cas échéant, pour les ressortissants d'un autre Etat partie à l'accord sur l'Espace économique européen, à un registre équivalent ;
>
> 2° Disposer des moyens matériels et humains nécessaires au respect des règles de suivi et de gestion de l'accise prévues par l'article L. 311-39 du code des impositions sur les biens et services, des formalités douanières ainsi que des exigences de traçabilité et de sécurité prévues par le règlement d'exécution (UE) 2018/574 de la Commission du 15 décembre 2017 et par les articles L. 3512-23 à L. 3512-25 du code de la santé publique ;
>
> 3° Ne pas faire l'objet d'une procédure d'insolvabilité prévue par le livre VI du code de commerce ou, le cas échéant, d'une procédure équivalente dans l'Etat d'immatriculation ;
>
> 4° N'avoir pas manqué de manière grave ou répétée aux obligations de paiement de l'accise ou du droit de consommation, des droits de douane et du droit de licence et aux règles et exigences mentionnées au 2° ;
>
> 5° N'avoir, ni aucun de ses dirigeants, lorsqu'il s'agit d'une personne morale, fait l'objet d'aucune condamnation ou sanction mentionnée au bulletin n° 2 du casier judiciaire pour méconnaissance de dispositions du code des douanes, du code général des impôts, du code des impositions sur les biens et services en lien avec l'exercice des activités de fournisseur de tabac ou pour des faits de blanchiment, de trafic de stupéfiants, de corruption ou trafic d'influence, et n'avoir pas fait, au cours des trois années qui précèdent, l'objet des sanctions prévues aux articles L. 651-2, L. 653-2 et L. 653-8 du code de commerce, ni d'une mesure d'interdiction en cours d'exécution prévue au même article L. 653-8 ;
>
> 6° Détenir un compte bancaire dans un établissement de crédit établi en France ou dans un autre Etat partie à l'Espace économique européen dédié à l'activité de fournisseur de tabac ;
>
> 7° En l'absence d'établissement doté de la personnalité morale sur le territoire national, y désigner un représentant habilité à satisfaire à la place du demandeur aux obligations qui lui incombent ;
>
> 8° Fournir l'adresse des établissements où sont détenus les tabacs.
>
> L'agrément est délivré par l'administration des douanes pour une durée d'un an lorsque l'immatriculation au registre national des entreprises ou son équivalent a été effectuée depuis moins de douze mois. Dans les autres cas, il est délivré pour une durée de trois ans.
>
> Le titulaire de l'agrément informe l'administration des douanes, dans un délai de quinze jours à compter de la survenance de l'évènement, de toute infraction ou condamnation mentionnée au 5° le concernant ou concernant ses représentants légaux, de tout changement dans son contrôle au sens de l'article L. 233-3 du code de commerce, de tout changement de ses représentants légaux ou de tout évènement susceptible de remettre en cause le respect des obligations prévues au présent article.
>
> II. – [Texte du II de la version LEGIARTI000054411891, sans changement : agrément de fabrication, deux conditions, information dans un délai de quinze jours, durée d'un an ou de cinq ans.]
>
> III. – Pour l'application des I et II, la composition des dossiers de demande est fixée par arrêté du ministre chargé des douanes. Elle ne peut comprendre aucune pièce que l'administration détient déjà ou peut obtenir d'un registre public, ni aucune caution, garantie financière ou sûreté.
>
> IV. – La liste des entreprises agréées est publiée sur le site internet de l'administration des douanes.
>
> V. – Aucune caution ni garantie financière garantissant le paiement du précompte sur remise n'est exigée pour la délivrance, le renouvellement ou le maintien de l'agrément. Les cautionnements constitués sur le fondement de la rédaction du présent article antérieure au décret n° 2026-612 du 7 juillet 2026 ne garantissent que les dettes nées avant le 1er août 2027 ; ils sont libérés après extinction de ces dettes et ne sont pas renouvelés. Les dettes légalement dues, les restitutions et les recours restent régis par leurs règles propres. Les garanties exigées pour les accises sur un fondement distinct ne sont pas modifiées.

Justification. L'agrément a une base légale (CSP L. 3512-14-7) et un objet de traçabilité qui relève en partie du droit de l'Union (règlement 2018/574) : un décret ne peut ni le supprimer ni le remplacer par un numéro d'identification. La coupe que voulait le projet, la caution, est déjà acquise et devient explicite au V. La seule charge supplémentaire retirée est la fourniture de pièces déjà détenues (III, deuxième phrase). Celle-ci ne doit pas être comptée comme un gain nouveau si elle ne fait que reprendre CRPA L. 113-12 (`coordination_only`).

Dépendances. Les articles 279, 280 et 286 F, en retained_unchanged, renvoient dans leur version 2027 à « l'agrément mentionné aux I et II de l'article 276 », et la présente rédaction les garde opérants. CSP L. 3512-14-7, L. 3512-23 et L. 3515-6-2 restent à lire. La présomption d'agrément de six mois, prévue par l'article 9 du décret 2026-612, n'est pas touchée.

Autre option, non retenue comme correction minimale : supprimer le terme de l'agrément ou allonger sa durée, et limiter l'obligation d'information aux changements de contrôle. Cela relève d'un choix de politique et suppose d'avoir vérifié le CSP.

#### 2. CGI, article 302 bis ZL : transition (objection C4-02, RT-FUTFISC-02)

Seul le troisième alinéa de la proposition LEGIARTI000041480036 change. Les autres alinéas restent tels que proposés.

> Pour les seuls prélèvements demeurant légalement dus sur des opérations antérieures selon les dispositions transitoires des articles 302 bis ZG, 302 bis ZH, 302 bis ZI et 302 bis ZO, les règles de rattachement aux comptes joueurs, d'exigibilité, de déclaration ou de constatation et de liquidation applicables à la date de leur exigibilité restent applicables : pour les prélèvements devenus exigibles avant le 1er janvier 2027, les modalités de dépôt prévues par le présent article dans sa rédaction antérieure à l'ordonnance n° 2025-1247 du 17 décembre 2025 ; pour ceux devenus exigibles à compter de cette date, la constatation dans les conditions prévues à l'article L. 161-1 du code des impositions sur les biens et services. Les régularisations, restitutions, prescriptions, garanties et recours correspondants restent ouverts. Le présent alinéa ne proroge ces règles qu'à l'égard de ces seuls prélèvements.

Justification. La phrase « Cette disposition ne remet pas en vigueur les textes dont l'abrogation est déjà prévue » est supprimée : elle repose sur une lecture erronée d'ABROGE_DIFF et contredit la phrase précédente. Aucune déclaration à néant n'est réintroduite.

#### 3. CGI, article 99 : renvoi de seuil (objection C4-05, RT-FUTFISC-07)

Seul le cinquième alinéa de la proposition LEGIARTI000053546818 change. Les quatre premiers alinéas proposés, saisie périodique et support commun, sont maintenus.

> Par exception au premier alinéa, les exploitants individuels dont le montant annuel de recettes n'excède pas le seuil mentionné au troisième alinéa du c du III de l'article 302 septies A bis du présent code, au cours de l'année civile ou de l'année civile précédente, peuvent procéder, au cours de l'année, à l'enregistrement de leurs recettes et dépenses professionnelles sur le livre-journal en retenant la date de l'opération figurant sur le relevé qui leur est adressé par un établissement de crédit, sous réserve d'enregistrer toutes leurs recettes et dépenses de l'année au plus tard le dernier jour de celle-ci. Pour l'appréciation des recettes d'années antérieures au 1er janvier 2027, le seuil est celui qui était alors applicable.

Justification. Ce texte reprend le Δf de la LF 2025 (art. 38) sans perte de la faveur. La dernière phrase évite qu'une modification du support du seuil ne ferme la faculté à un exploitant qui y avait droit. Elle doit être confrontée aux règles d'exercice décalé de la NOTA (LF 2025, art. 38, VI).


### Rédactions — Lot A

### Lot A (CVAE, CCI, plafonnement CFE) : rédactions proposées

Ce sont des propositions de red-team, pas une validation juridique. Les subdivisions des lois différées sont citées d'après les NOTA et les liens LEGI de l'instantané 20261026T230545Z ; elles doivent être vérifiées au JORF avant tout dépôt.

---

#### 1. Disposition transitoire de la loi de réforme : neutraliser le calendrier CVAE 2027-2029 pour les seules années supprimées (objection A-01)

**Article [X] de la loi de réforme (hors CGI)**

I. – Pour l'application du présent article, sont dites « années supprimées » les années d'imposition commençant à compter du 1er janvier de l'année suivant celle au cours de laquelle la présente loi entre en vigueur, et antérieures au 1er janvier 2030.

II. – Les dispositions publiées avant la présente loi dont l'entrée en vigueur ou l'application est différée ne sont pas applicables aux impositions dues au titre des années supprimées, en tant qu'elles modifient, rétablissent ou fixent pour ces années l'assujettissement, l'assiette, le barème, le dégrèvement, le taux, la déclaration, le paiement, le recouvrement ou les sanctions de la cotisation sur la valeur ajoutée des entreprises et de la taxe additionnelle à cette cotisation, aux articles 1586 ter, 1586 quater, 1586 quinquies, 1586 sexies, 1586 septies, 1586 octies, 1586 nonies, 1600, 1649 quater B quater, 1679 septies, 1681 septies et 1731 du code général des impôts. Sont notamment visés :

1° L'article 10 de l'ordonnance n° 2025-1247 du 17 décembre 2025, en tant qu'il modifie le 3 du II de l'article 1586 ter du code général des impôts ;

2° L'article 62 de la loi n° 2025-127 du 14 février 2025 de finances pour 2025, ainsi que les dispositions de l'article 79 de la loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024 et de l'article 55 de la loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023 dans leur rédaction qui en résulte, en tant qu'ils fixent les taux et le dégrèvement prévus aux I et II de l'article 1586 quater et le taux prévu au III de l'article 1600 du même code pour les impositions dues au titre de 2028 et de 2029.

III. – Les dispositions mentionnées au II restent applicables, dans leur rédaction et à leur date, aux impositions dues au titre des années antérieures aux années supprimées. Cela vaut notamment pour les taux et dégrèvements réduits de l'article 1586 quater et pour les taux de la taxe additionnelle de l'article 1600 dus au titre de ces années, ainsi que pour leurs exonérations, dégrèvements, restitutions, procédures, garanties, prescriptions et recours.

IV. – Le présent article ne fait pas obstacle à l'application, à compter des impositions établies au titre de 2030, des abrogations de la cotisation sur la valeur ajoutée des entreprises et de la taxe additionnelle à cette cotisation déjà prévues par la loi. Il ne s'oppose pas non plus à l'application des taux décroissants du plafonnement prévu à l'article 1647 B sexies du code général des impôts.

V. – Le présent article ne crée aucun prélèvement, aucune obligation déclarative ni aucune majoration d'une autre imposition.

**Correction corrélative de la proposition de 1586 quater (LEGIARTI000048860944), dernier alinéa :**

> Les dégrèvements prévus au II dans la rédaction applicable à chacune des années antérieures, ainsi que les autres dégrèvements légalement applicables à ces années, restent pris en compte. Aucun barème de CVAE n'est maintenu pour une année supprimée.

*Justification.* cvae_removal demande de « retirer les substitutions futures qui réintroduiraient un barème ou une CVAE ». Les propositions abrogent les articles sans viser les instructions déjà publiées. La clause ne touche que les années supprimées et conserve les baisses programmées pour les années antérieures. *Dépendances.* La date de la première année supprimée dépend de la date d'entrée en vigueur de la loi. Il faut une liste exacte des subdivisions JORF, qui n'a pas été lue.

---

#### 2. Article 1647 B sexies du CGI : rédaction fusionnée applicable aux années supprimées et à compter de 2030 (objection A-02)

**Article 1647 B sexies**

I. ― Sur demande du redevable effectuée dans le délai légal de réclamation prévu pour la cotisation foncière des entreprises, la cotisation foncière des entreprises de chaque entreprise est plafonnée en fonction de sa valeur ajoutée.

Cette valeur ajoutée est :

a) Pour les contribuables soumis à un régime d'imposition défini au 1 de l'article 50-0 ou à l'article 102 ter, égale à 80 % de la différence entre le montant des recettes et, le cas échéant, celui des achats réalisés au cours de l'année d'imposition ;

b) Pour les autres contribuables, celle définie à l'article 1586 sexies pour les impositions établies au titre des années antérieures à 2030, et celle définie à l'article 1647 B sexies A pour les impositions établies au titre de 2030 et des années suivantes.

Pour l'application du b, la valeur ajoutée ne peut excéder 80 % du chiffre d'affaires pour les contribuables dont le chiffre d'affaires est inférieur ou égal à 7,6 millions d'euros, et 85 % du chiffre d'affaires pour les contribuables dont le chiffre d'affaires est supérieur à 7,6 millions d'euros. Le chiffre d'affaires est déterminé selon la même définition et sur la même période que la valeur ajoutée.

La valeur ajoutée prise en compte est celle produite au cours de la période définie au I bis.

Le taux de plafonnement est fixé à 1,531 % de la valeur ajoutée pour les impositions établies au titre de 2026 et de 2027, à 1,438 % pour 2028, à 1,344 % pour 2029 et à 1,25 % à compter de 2030.

I bis. ― A. ― 1. Sous réserve des 2, 3 et 4 du présent A, la valeur ajoutée prise en compte est celle produite au cours de l'année au titre de laquelle l'imposition est établie ou au cours du dernier exercice de douze mois clos au cours de cette même année lorsque cet exercice ne coïncide pas avec l'année civile.

2. Si l'exercice clos au cours de l'année au titre de laquelle l'imposition est établie est d'une durée supérieure ou inférieure à douze mois, la valeur ajoutée prise en compte est celle produite au cours de cet exercice.

3. Si aucun exercice n'est clôturé au cours de l'année au titre de laquelle l'imposition est établie, la valeur ajoutée prise en compte est celle produite entre le premier jour suivant la fin de la période retenue pour le calcul du plafonnement de l'année précédente et le 31 décembre de l'année d'imposition. En cas de création d'entreprise au cours de l'année d'imposition, la période retenue correspond à celle comprise entre la date de création et le 31 décembre de l'année d'imposition.

4. Lorsque plusieurs exercices sont clôturés au cours d'une même année, la valeur ajoutée prise en compte est celle produite au cours des exercices clos, quelles que soient leurs durées respectives.

5. Dans les situations mentionnées aux 1 à 4 du présent A, il n'est pas tenu compte de la fraction d'exercice clos qui se rapporte à une période déjà retenue pour le calcul du plafonnement dû au titre d'une ou de plusieurs années précédant celle de l'imposition.

B. ― En l'absence de cession ou de cessation d'entreprise au cours de l'année d'imposition, le montant de la valeur ajoutée mentionnée au b du I et déterminée conformément aux 2 à 4 du A du présent I bis est corrigé pour correspondre à une année pleine.

II. ― Le plafonnement prévu au I s'applique sur la cotisation foncière des entreprises diminuée, le cas échéant, de l'ensemble des réductions et dégrèvements dont cette cotisation peut faire l'objet.

Il ne s'applique pas aux taxes visées aux articles 1600 à 1601-0 A ni aux prélèvements opérés par l'Etat sur ces taxes en application de l'article 1641. Il ne s'applique pas non plus à la cotisation minimum prévue à l'article 1647 D.

La cotisation foncière des entreprises s'entend de la somme des cotisations de chaque établissement établies au titre de l'année d'imposition. La cotisation de chaque établissement est majorée du montant de la taxe prévue à l'article 1530 bis et des taxes spéciales d'équipement additionnelles à la cotisation foncière des entreprises prévues aux articles 1599 quater D, 1607 bis, 1607 ter et 1609 B à 1609 H, ainsi que du montant de la taxe prévue à l'article 1609 İ, calculées dans les mêmes conditions.

III. ― Le dégrèvement s'impute sur la cotisation foncière des entreprises.

IV. ― Le dégrèvement ne peut avoir pour effet de ramener la cotisation foncière des entreprises à un montant inférieur à celui résultant de l'application de l'article 1647 D.

V. ― Le reversement des sommes indûment restituées est demandé selon les mêmes règles de procédure et sous les mêmes sanctions qu'en matière de cotisation foncière des entreprises. Les réclamations sont présentées, instruites et jugées selon les règles de procédure applicables en matière de cotisation foncière des entreprises.

VI. ― Les dégrèvements résultant de l'application du présent article sont ordonnancés dans les six mois suivant celui du dépôt de la demande.

VII. ― La présente rédaction s'applique aux impositions établies au titre des années supprimées en application du premier alinéa de l'article 1586 ter, puis à compter des impositions établies au titre de 2030. Pour les années antérieures, le plafonnement de la contribution économique territoriale et les dégrèvements correspondants restent régis par les dispositions applicables à ces années. La suppression de la cotisation sur la valeur ajoutée des entreprises n'autorise ni une hausse du taux de plafonnement ni la réduction d'un dégrèvement déjà acquis. Aucun montant de cette cotisation au titre d'une année supprimée ne peut être mis à la charge du redevable par l'application du présent article.

**Clause de la loi de réforme (coordination de la version 2030) :**

> Les dispositions de l'article 55 de la loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023, dans leur rédaction issue de l'article 79 de la loi n° 2023-1322 du 29 décembre 2023 et de l'article 62 de la loi n° 2025-127 du 14 février 2025, qui réécrivent l'article 1647 B sexies du code général des impôts à compter des impositions établies au titre de 2030, ne sont pas applicables. Cet article s'applique dans sa rédaction issue de la présente loi. L'article 1647 B sexies A du même code et l'article 310 HC de l'annexe II à ce code s'appliquent pour la détermination de la valeur ajoutée mentionnée au b du I de l'article 1647 B sexies à compter des impositions établies au titre de 2030.

**Coordinations corrélatives :**
- 1447 I, deuxième alinéa (proposition LEGIARTI000053544997) : « …ou un chiffre d'affaires, au sens du 1 du I de l'article 1586 sexies pour les impositions établies au titre des années antérieures à 2030 et au sens du 1° du I de l'article 1647 B sexies A à compter des impositions établies au titre de 2030, inférieur à 100 000 €. » Le IV (micro-entrepreneurs) est inchangé.
- 238 bis HW (proposition LEGIARTI000047303743) : le renvoi figé du projet peut être conservé. Il faut alors ajouter : « Les dispositions qui, à compter du 1er janvier 2030, substituent à ce renvoi celui du I bis de l'article 1647 B sexies et de l'article 1647 B sexies A ne s'appliquent pas aux agréments sollicités sur le fondement du présent article. »
- 1586 quinquies et 1586 sexies : aucune neutralisation de leur abrogation au 1er janvier 2030 n'est nécessaire avec cette rédaction. Leurs propositions restent la base des années supprimées antérieures à 2030.

*Justification.* Cette rédaction garde ce que la version 2030 apporte de favorable : 1,25 %, la VA de navigation (1647 B sexies A 7° et 310 HC) et des périodes autonomes. Elle garde aussi ce que la version 2030 retire et que le projet conserve : le plafond de VA à 80/85 % du CA, la règle de création et l'inclusion des taxes 1599 quater D et 1609 İ. Elle supprime les renvois à des articles abrogés en 2030 et ne crée aucune formalité : la demande dans le délai de réclamation existe déjà. *Dépendances.* La proposition 1586 ter définit les années supprimées. Les subdivisions JORF de la LF 2023 art. 55 doivent être vérifiées. 1647 B sexies A ne reprend pas la mention de 1586 sexies relative à la décision 2009-599 DC ; la portée de cet écart n'a pas été examinée.

---

#### 3. Clause sur les CGA et AGA (objection A-04)

> Les articles 1649 quater C à 1649 quater M du code général des impôts, abrogés par l'article 11 de la loi n° 2025-127 du 14 février 2025 de finances pour 2025, demeurent abrogés. Les dispositions de l'article 55 de la loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023 qui modifient, à compter des impositions établies au titre de 2030, les articles 1649 quater E et 1649 quater H du même code sont sans objet. Les obligations nées avant le 16 février 2025 restent régies par les dispositions qui leur étaient applicables.

*Justification.* Cette clause empêche la renaissance apparente, en 2030, d'obligations de contrôle, de compte rendu et de télétransmission supprimées en 2025. Elle ne crée aucune formalité.


### Rédactions — Lot B1

### Lot B1 — rédactions proposées (versions futures 2027-2029)

Revue IA, provisoire. Les textes modificateurs (LF 2026 art. 102, ordonnances 2025-1091, 2025-1247 et 2026-671) n'ont pas été lus au JORF. Leurs subdivisions sont donc désignées par leur objet et non par leur alinéa : à vérifier avant tout dépôt.

#### 1. CSI — neutraliser la version 2029 étendue au livre foncier de Mayotte (objection B1-01)

Ajouter à la loi de réforme, à côté de la suppression générale prévue à l'article 879 :

> **Article [coordination CSI].**
> I. – Les dispositions du I de l'article 102 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 qui modifient les articles 880, 881 A, 881 B, 881 C, 881 I, 881 J, 881 K et 881 M du code général des impôts sont abrogées. Les modifications de ces articles qui seraient entrées en vigueur avant la publication de la présente loi ne s'appliquent qu'aux réquisitions et demandes présentées avant l'entrée en vigueur de la suppression prévue à l'article 879 du même code.
> II. – La suppression de la contribution de sécurité immobilière prévue à l'article 879 du code général des impôts s'applique aux réquisitions de publier, d'inscrire, de mentionner ou d'immatriculer présentées au fichier immobilier comme au livre foncier de Mayotte, y compris aux requêtes en immatriculation des immeubles, aux inscriptions rectificatives et aux oppositions, quelle que soit la date de l'acte ou du droit concerné.
> III. – Les réquisitions et demandes présentées avant l'entrée en vigueur de cette suppression restent régies par les dispositions qui leur étaient applicables, y compris l'article 881 O pour les formalités mahoraises antérieures au 1er janvier 2029. Aucune contribution de sécurité immobilière ne devient exigible à Mayotte du seul fait de l'arrivée à son terme, le 31 décembre 2028, de l'article 881 O. Aucune restitution générale n'est instituée, et une même somme ne peut être imputée ou remboursée deux fois.

Justification : 881 B et 881 C, dans leur rédaction de 2029, perçoivent la contribution de façon autonome (« Il est perçu une contribution fixe… »). Sans ce I, ils renaîtraient au 1er janvier 2029 si la réforme entre en vigueur avant cette date. Le II applique la règle d'orientation « sans renaissance CSI à son terme ». Dépendances : proposition de 879 (hors lot B1), 881 N et 881 O conservés.

#### 2. CGI 1741 — rédaction fusionnée (objection B1-07)

Cette rédaction remplace la proposition ; elle est fondée sur la version 2027 (LEGIARTI000054566825) et neutre pour la renumérotation du CPP de 2029 :

> Sans préjudice des dispositions particulières relatées dans la présente codification, quiconque s'est frauduleusement soustrait ou a tenté de se soustraire frauduleusement à l'établissement ou au paiement total ou partiel des impositions prévues par le présent code et, lorsque les dispositions du présent livre leur sont applicables, de celles prévues par le code des impositions sur les biens et services, soit qu'il ait volontairement omis de faire sa déclaration dans les délais prescrits, soit qu'il ait volontairement dissimulé une part des sommes sujettes à l'impôt, soit qu'il ait organisé son insolvabilité ou mis obstacle par d'autres manoeuvres au recouvrement de l'impôt, soit en agissant de toute autre manière frauduleuse, est passible, indépendamment des sanctions fiscales applicables, d'un emprisonnement de cinq ans et d'une amende de 500 000 €, dont le montant peut être porté au double du produit tiré de l'infraction.
>
> Les peines sont portées à sept ans d'emprisonnement et à une amende de 3 000 000 €, dont le montant peut être porté au double du produit tiré de l'infraction, lorsque les faits ont été commis en bande organisée ou réalisés ou facilités au moyen :
>
> 1° Soit de comptes ouverts ou de contrats souscrits auprès d'organismes établis à l'étranger ;
>
> 2° Soit de l'interposition de personnes physiques ou morales ou de tout organisme, fiducie ou institution comparable établis à l'étranger ;
>
> 3° Soit de l'usage d'une fausse identité ou de faux documents, au sens de l'article 441-1 du code pénal, ou de toute autre falsification ;
>
> 4° Soit d'une domiciliation fiscale fictive ou artificielle à l'étranger ;
>
> 5° Soit d'un acte fictif ou artificiel ou de l'interposition d'une entité fictive ou artificielle.
>
> Toutefois, cette disposition n'est applicable, en cas de dissimulation, que si celle-ci excède le dixième de la somme imposable ou le chiffre de 153 €.
>
> Toute personne condamnée en application des dispositions du présent article peut être privée des droits civiques, civils et de famille, suivant les modalités prévues aux articles 131-26 et 131-26-1 du code pénal.
>
> Le prononcé des peines complémentaires d'interdiction des droits civiques, civils et de famille, mentionnés à l'article 131-26 du code pénal, est obligatoire à l'encontre de toute personne coupable du délit prévu aux deuxième à huitième alinéas du présent article, du recel de ce délit ou de son blanchiment. Toutefois, la juridiction peut, par une décision spécialement motivée, décider de ne pas prononcer lesdites peines complémentaires, en considération des circonstances de l'infraction et de la personnalité de son auteur. La condamnation à l'inéligibilité est mentionnée pendant toute sa durée au bulletin n° 2 du casier judiciaire. Ces interdictions ne peuvent excéder dix ans à l'encontre d'une personne exerçant une fonction de membre du Gouvernement ou un mandat électif public au moment des faits, et cinq ans pour toute autre personne.
>
> La peine complémentaire de privation du droit à l'octroi de réductions ou de crédits d'impôt sur le revenu ou d'impôt sur la fortune immobilière est supprimée. Les avantages fiscaux restent applicables dans les conditions propres à chacun d'eux.
>
> Les crédits d'impôt octroyés sur le fondement d'une convention internationale ayant pour objet l'élimination de la double imposition en matière d'impôts sur le revenu et sur la fortune demeurent applicables dans les conditions de cette convention.
>
> La juridiction ordonne l'affichage de la décision prononcée et la diffusion de celle-ci dans les conditions prévues aux articles 131-35 ou 131-39 du code pénal. Elle peut toutefois, par une décision spécialement motivée, décider de ne pas ordonner l'affichage de la décision prononcée et la diffusion de celle-ci, en considération des circonstances de l'infraction et de la personnalité de son auteur.
>
> La durée de la peine privative de liberté encourue par l'auteur ou le complice d'un des délits mentionnés au présent article est réduite des deux tiers si, ayant averti l'autorité administrative ou judiciaire, il a permis de faire cesser l'infraction ou d'identifier, le cas échéant, les autres auteurs ou complices.
>
> Les poursuites sont engagées dans les conditions prévues aux articles L. 229 à L. 231 du livre des procédures fiscales.
>
> La suppression de la peine complémentaire de privation du droit à l'octroi de réductions ou de crédits d'impôt s'applique dès l'entrée en vigueur de la loi portant la présente réforme, y compris aux faits antérieurs non définitivement jugés. Les décisions définitives demeurent soumises aux règles d'exécution et aux voies de recours qui leur sont applicables. La définition du champ des impositions mentionnée au premier alinéa n'a pas pour effet de restreindre les poursuites engagées sur le fondement d'une rédaction antérieure du présent article pour des faits commis sous son empire.

Justification : la rédaction reprend le champ CIBS de 2027 (sinon, après la recodification, la TVA sort du délit général) et supprime le numéro d'article du casier, que l'ordonnance 2025-1091 renumérote en 2029. Le décompte des « deuxième à huitième alinéas » est inchangé. Ajouter dans la loi de réforme : « Les modifications de l'article 1741 du code général des impôts prévues par l'ordonnance n° 2025-1091 du 19 novembre 2025 sont sans objet. » Dépendances : 1743 et 1744 (hors lot), même mécanisme.

#### 3. Prélèvements et délits abrogés que les ordonnances réécrivent en 2027-2029 (objections B1-02 à B1-06 et B1-08)

Une seule disposition de coordination dans la loi de réforme :

> **Article [coordination des recodifications].**
> I. – Sont abrogées, en tant qu'elles modifient ou réécrivent les articles du code général des impôts mentionnés ci-après, les dispositions suivantes :
> 1° Les articles 3 et 22 de l'ordonnance n° 2025-1091 du 19 novembre 2025, pour les articles 1018 A, 1100, 1649 quater-0 B bis et 1789 ;
> 2° L'article 14 de l'ordonnance n° 2026-671 du 27 juillet 2026, pour l'article 568 ;
> 3° L'article 16 de la même ordonnance et l'article 11 de l'ordonnance n° 2025-1247 du 17 décembre 2025, pour l'article 1804 C.
> II. – Le I ne remet pas en cause les rédactions qui s'appliquent aux décisions, faits générateurs, paiements et années antérieurs à l'entrée en vigueur des abrogations prévues par la présente loi, ni les créances, restitutions, prescriptions et recours afférents.
> III. – Pour l'article 1840 P du code général des impôts et l'article 406 A 15 de l'annexe III au même code, les mots « tribunal correctionnel » sont remplacés par les mots « tribunal délictuel » à compter du 1er janvier 2029. Les autres modifications de ces articles par l'ordonnance n° 2025-1091 du 19 novembre 2025 sont sans objet.

Texte de 1840 P corrigé (la phrase sur une « abrogation prévue le 1er janvier 2029 », qui n'existe pas, est supprimée) :

> 1. Ceux qui ont sciemment employé, vendu ou tenté de vendre des timbres mobiles ayant déjà servi, sont poursuivis devant le tribunal correctionnel et punis d'une amende de 3 750 €. En cas de récidive, l'amende est doublée.
>
> Les dispositions du présent article sont applicables dans tous les cas où un impôt, une taxe ou un droit quelconque recouvré par l'administration fiscale est acquitté au moyen de l'apposition de timbres mobiles.
>
> 2. Les dispositions du premier alinéa du 1 sont applicables à ceux qui, dans une intention frauduleuse, ont altéré, employé, vendu ou tenté de vendre des papiers timbrés ayant déjà servi.
>
> La peine d'emprisonnement d'un mois prévue antérieurement en cas de récidive est supprimée à compter de l'entrée en vigueur de la loi portant la présente réforme, avec application de la loi pénale plus douce dans son champ. Les infractions distinctes demeurent régies par leurs textes.

Pour 406 A 15, supprimer la dernière phrase de la proposition (« Les présentes dispositions ne reportent pas une abrogation différée… »).

Réserve : 406 A 15 appartient à l'annexe III, de niveau réglementaire. Son III relève donc d'un décret et non de la loi si la compétence est confirmée.

## 6. Contrôle des retained_unchanged et des nouveaux numéros

- **38 retained_unchanged.** Pour 13 d'entre eux, la version future, le motif, les notes et le diff ont été lus en entier : 1384-0 A, 1388-0, 1391 E, 1464 A, 1468 bis, 1515, 1518 A quinquies, 1635 quater D, annexe II 279, 286 F, 302 septies A bis, 1671, 1965 FA. Pour les 25 autres, seuls le diff intégral (extraits limités à 420 caractères par modification), le motif et les notes ont été lus ; leur version future n'a pas été relue d'un seul tenant (`read_in_full` = false).
- Aucune de ces versions futures ne crée un prélèvement contraire aux orientations. Trois points relèvent de l'alerte. L'agrément tabacs de l'annexe II (279, 280, 286 F), issu du CSP, s'étend aux collectivités de l'article 73 (RT-FUTFISC-25). La déclaration des rentes de 88 est fusionnée dans la déclaration de 87-0 A, ce qui est favorable. L'actualisation des valeurs locatives professionnelles (1518 A quinquies, 1468 bis, 1656, 1656 quater) n'est qu'une coordination.
- **10 nouveaux numéros, tous lus en entier.**
  - Créent une charge nouvelle : 1496 ter, déclaration des loyers (RT-FUTFISC-26), et 1788 F, sanctions de l'agrément de détaxe (RT-FUTFISC-12).
  - Ressuscitent des obligations abrogées : 1649 quater E et H, CGA/AGA (RT-FUTFISC-16).
  - Sont neutres ou favorables : 1647 B sexies A et annexe II 310 HC (définition de la valeur ajoutée et exclusion navigation, RT-FUTFISC-14), 1518 A quinquies A (lissage, RT-FUTFISC-27), 256-00 (renvoi au CIBS).
  - « Articles réservés » à la borne technique 2222-02-22, sans effet : 1419 à 1446 et 1481 à 1493 bis.

## 7. Incertitudes restantes et éléments non examinés

- **Lecture non intégrale (36 entrées).** cgi 1635 quater I (2027-01-01); cgi 1651 (2027-01-01); cgi 1651 F (2027-01-01); cgi 1651 H (2027-01-01); cgi 1651 M (2027-01-01); cgi 1656 (2027-01-01); cgi 1656 quater (2027-01-01); cgi 1698 D (2027-01-01); cgi 1740 B (2027-01-01); cgi 1744 (2027-01-01); cgi 1756 (2027-01-01); cgi 1920 (2027-01-01); cgi 199 novovicies (2027-01-01); cgi 199 septvicies (2027-01-01); cgi 200 (2027-01-01); cgi 200 quater (2027-01-01); cgi 200 quater A (2027-01-01); cgi 207 (2027-01-01); cgi 302 bis P (2027-01-01); cgi 302 bis S (2027-01-01); cgi 302 bis U (2027-01-01); cgi 31 (2027-01-01); cgi 39 (2027-01-01); cgi 790 H (2027-01-01); a2 280 (2027-08-01); cgi 1635 quinquies (2029-01-01); cgi 1649 bis B (2029-01-01); cgi 1746 (2029-01-01); cgi 1751 A (2029-01-01); cgi 1791-0 (2029-01-01); cgi 1920 (2029-01-01); cgi 363 (2029-01-01); cgi 81 (2029-01-01); cgi 1736 (2030-01-01); cgi 88 (2030-01-01); cgi 44 quaterdecies (2031-01-01). Il s'agit des 25 retained_unchanged et de grandes propositions (31, 39, 81, 199 novovicies, 199 septvicies, 200, 200 quater, 200 quater A, 207, 1736, 44 quaterdecies). Pour ces dernières, la proposition, le motif, les notes et le diff ont été lus, mais la version future n'a pas été relue d'un seul tenant ; pour 200 quater, le motif et les notes n'ont été lus que par recherche ciblée.
- Les instructions modificatives (JORF) n'ont pas été lues : LF 2023 art. 55, LF 2025 art. 38 et 62, LF 2026 art. 23, 102, 106, 123 et 171, ordonnances 2025-1247, 2025-1091 et 2026-671, décret 2026-612, lois 2025-797, 2026-403 et 2026-555. On ne peut donc pas trancher partout entre substitution ponctuelle et réécriture. Les qualifications `réforme écrasée` de 2028-2031 reposent sur le contenu publié de la version future (lecture XCUT) et deviennent sans objet si l'instruction est ponctuelle et vise des mots absents du texte réformé.
- Le CIBS (L. 161-1, L. 180-1, L. 215-39, L. 215-40, L. 216-x, L. 231-x, L. 233-x, L. 234-2) et le CSP sont hors corpus. Les coordinations correspondantes sont nommées, non rédigées.
- La date d'entrée en vigueur de la loi de réforme est inconnue. La règle d'harmonisation 2027 suppose qu'elle est postérieure au 1er janvier 2027.
- Non examinés dans ce paquet : les autres articles qui renvoient aux numéros réformés (par exemple 1743, au même champ que 1741 ; 302 bis ZG, ZH, ZI, ZO ; les décrets d'application), et les codes autres que le CGI et ses annexes, couverts par les paquets FUT-CSS et FUT-TRAV-LOG. Les abrogations différées sans successeur relèvent du dossier INV.
- Plusieurs versions courantes sont encore « pending » en seconde passe. Les propositions peuvent changer, et les conclusions sont à reconfronter à l'instantané suivant.

## 8. Livrables

- `reports/dossiers/FUT-FISC.md` (ce rapport) ; `reports/dossiers/FUT-FISC.json` (33 objections) ; `reports/p1-work/FUT-FISC-classification.jsonl` (178 lignes, une par couple ou nouveau numéro).
- Exports de preuve : `evidence/cited/20261026T230545Z/` (fichiers cités dans chaque objection, champ `evidence_files`).
