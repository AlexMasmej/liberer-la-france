# DOM-SUCC — Revue de fond : suppression des droits de succession

Troisième passe, red-team juridique indépendante. Instantané `20261026T230545Z`, corpus au 18 octobre 2026. Rapport du 26 octobre 2026.
Cette revue est faite par une IA. Elle **ne vaut pas validation par un juriste**. Ses conclusions sont provisoires, car la seconde passe se poursuit en production.

## 1. Orientation et résultat obtenu

### Orientation (citations exactes, `policy-coordinations.json`, clé `successions`)

- « Décision ferme de l'auteur : supprimer les droits français sur toutes les transmissions à titre gratuit par décès, sans plafond, condition de parenté, de résidence, de nationalité ou de montant. Cela inclut héritages, legs, transmissions au décès via trust et les prélèvements de substitution sur les capitaux d'assurance-vie ou les plans retraite dénoués par décès. Aucun droit de succession requalifié en contribution ne doit subsister. »
- « La décision porte sur les décès à compter de l'entrée en vigueur de la loi proposée. Aucun rappel ne peut être établi pour ces nouveaux décès. Le recouvrement, les restitutions, contentieux et prescriptions sur les décès antérieurs sont préservés ; pas de remboursement rétroactif général décidé. »
- « Supprimer les déclarations, garanties, certificats de paiement et obligations d'information uniquement justifiés par la perception de cet impôt [...] Ne pas bloquer le versement d'une assurance ou d'une banque [...] Maintenir les formalités civiles utiles [...] »
- « Ne pas confondre succession et donation entre vifs : l'auteur n'a pas décidé ici de supprimer les droits sur les donations. Préserver leur assiette, barème, fait générateur et obligations utiles, et les régimes d'autres impôts (revenus, plus-values, IFI) qui ont une finalité distincte. Supprimer en revanche les conditions de conservation ou obligations de pacte devenues exclusivement inutiles [...] »
- « Coordonner l'assurance-vie 757 B/990 I, les trusts 792-0 bis, les règles internationales et l'imputation des impôts étrangers : pas de crédit remboursable sans impôt français [...] »

Le site (`site-summaries.json`) présente la mesure ainsi : « Zéro droit de succession [...] Supprimer aussi les prélèvements équivalents sur l'assurance-vie dénouée au décès et les transmissions au décès par trust. Retirer les déclarations et certificats fiscaux devenus inutiles. Les donations entre vifs et les formalités civiles de succession restent distinctes. » Les mesures connexes lues sont `fixed_act_charges_targeted_removal`, `registration_minimum_removal`, `contribution_securite_immobiliere_removal`, `cuts_and_reliefs_2026_10_19` et `substantive_outcomes_2026_10_19`. Le document de lot `batches/successions/controle-coordinations-fiscalite.md` a été lu en entier.

### Résultat obtenu

**La réforme atteint, pour l'essentiel, son objectif dans le CGI, ses annexes et le CSS.** Le résultat est le suivant :

- **Fait générateur et assiette.** Le II de 750 ter supprime tout droit de mutation à titre gratuit à raison d'un décès. 757 B, 990 I, 990 I bis (CDC) et la composante décès de 792-0 bis sont neutralisés. Le barème (777) et les abattements (779) sont réservés aux donations. Les présomptions (751 à 754 A), le passif (767 à 775 sexies) et le rappel au décès (784, 776 ter) sont abrogés pour les nouveaux décès.
- **Formalités.** Sont supprimés, sans remplacement, pour les nouveaux décès : la déclaration (800), les délais (641, 641 bis, 642), les listes et certificats des dépositaires et assureurs (806, 805, 808 ; annexe II 292 A, 292 B, 306-0 F ; annexe III 280 à 280 B), l'enregistrement des testaments (636), le paiement préalable aux formalités (1701), la solidarité (1709, 1710), les intérêts, majorations et amendes (1727, 1728, 1729 B), les affirmations pénales (1837) et le paiement fractionné ou différé (annexe III 396 à 404 GC).
- **Distinctions préservées.** Les donations conservent leur barème, leurs abattements, le rappel de quinze ans et les régimes Dutreil (787 B/C, 790), forestier et monuments historiques. Les dons manuels (757, 635 A), le droit de partage (746 à 748), la TPF à 0,60 % des donations (791) et l'IFI (973 autonomisé, 968 bis, 970) sont maintenus, ainsi que le prélèvement annuel sur les trusts (990 J). L'imputation de l'impôt étranger est bornée aux donations (784 A). Les règles civiles restent hors champ.
- **Autres impôts.** La valeur d'acquisition des biens hérités est fixée de manière autonome à la valeur au décès (150-0 D, 150 VB, 150 VH bis, 167 bis, annexe II 74-0 E ter). La réunion de l'usufruit est neutralisée (1133, avec la réserve de 1020). La décharge d'impôt sur le revenu des victimes (1691 ter) et l'exonération des dons aux victimes (796 bis) sont autonomisées.
- **Transition.** Les décès antérieurs restent soumis au droit applicable, sans remboursement général. Pour les crédits de paiement, la transition suit les règles temporelles propres (annexe III 397, 404 A, 404 B, 404 GA).

**Trois défauts empêchent de dire que l'objectif est atteint « sans contournement ni effet involontaire » :**

1. **RT-DOMSUCC-01 (P1).** L'exonération est définie par l'événement (un décès) et non par l'auteur de la transmission (le défunt). Une personne vivante peut donc faire passer une donation, que l'orientation maintient, par le décès d'un tiers : assurance sur la tête d'un tiers, libéralité graduelle ou résiduelle dont l'auteur est vivant, trust ou fiducie au décès d'un bénéficiaire.
2. **RT-DOMSUCC-02 (P1, à confirmer).** L'abrogation de 754 A (tontine) supprime la qualification « réputés transmis à titre gratuit ». Le survivant est alors exposé au droit de vente (droit de mutation à titre onéreux), qu'aucune clause de suppression ne neutralise. Ce serait un impôt nouveau au décès.
3. **Hors corpus.** Le résultat n'est pas démontré dans le LPF, le code des assurances, le CMF, l'ordonnance 96-50 ni dans les conventions (RT-DOMSUCC-08). Les autres constats sont des alertes P2.

Le chiffrage de la perte de recettes n'est ni fait ni présumé compensé. C'est conforme à l'orientation, qui le renvoie à une étape ultérieure.

## 2. Méthode

1. Les deux briefs, l'orientation (`policy-coordinations.json`, `site-summaries.json`), le README de l'instantané et le document de contrôle du lot ont été lus.
2. Périmètre : les 140 lignes de `batches/successions/` (001 et 200 à 208). On y a ajouté une recherche dans `articles.content_xml` et `drafts.proposed_xml` (versions dont `valid_until` est postérieure au 18 octobre 2026) sur « mutation par décès », « déclaration de succession », « droits de succession », « décès de l'assuré », « 990 I », « 757 B », « valeur retenue pour la détermination des droits de mutation », « testament » et les numéros des articles abrogés.
3. Chaque pièce citée a été lue avec `tools/cite.py`, toutes versions comprises (preuves dans `evidence/cited/20261026T230545Z/`). Pour la lecture, un affichage limité aux versions courantes et futures, avec source, NOTA, proposition, motif et notes, a été produit par un script en lecture seule (`mode=ro`, `query_only`). Aucun script de production n'a été lancé.
4. Doublons : chaque objection a été confrontée à `reports/register.json` (312 objections) et aux dossiers existants, par numéros d'article et par texte.
5. Sources externes consultées le 26 octobre 2026 : AN QE n° 26893 (15e législature) et QE n° 60434 (13e législature, via résultat de recherche), rapport du 122e Congrès des notaires (2026, « La tontine »). Le BOFiP n'a pas pu être relu sur les points visés : c'est une réserve.

## 3. Objections existantes confirmées, précisées ou contredites

| Objection | Objet | Constat sur l'instantané |
|---|---|---|
| RT-P1-CGI-C-05 (P1) | 750 ter renvoie à la « chaîne de participations au sens de l'article 990 D », alors que 990 D est abrogé | **Confirmée** : la proposition de 750 ter (sha `306663e1…`) n'a pas changé et conserve le renvoi non figé. À corriger en même temps que RT-DOMSUCC-01. |
| RT-FUTFISC-01 (P1) | Versions 2027 sans proposition pour 1727, 1754 et 790 H | **Confirmée et précisée** : 1727 (LEGIARTI000053188950) et 1754 (LEGIARTI000053189001) sont VIGUEUR_DIFF au 1er janvier 2027, sans proposition ni inventaire. Le VI de 1727 (aucun intérêt sur les droits supprimés) et le 4 de 1754 (solidarité du faux créancier bornée aux anciens décès) disparaîtraient si la loi visait la rédaction 2026. Pas de nouvelle objection. |
| RT-FUTFISC-29 et RT-P1-CGI-B-08 (P2) | 1729 B, versions 2027 et absence de borne | **Confirmées** ; le nouveau 5 propre aux successions est concerné de la même façon. |
| RT-INTEG-03 et RT-FUTFISC-15 (P2) | 1649 quater B quater et 1681 septies, versions 2027 et 2030 | **Confirmées** : les alinéas « 990 I pour les seuls décès antérieurs » n'existent que dans la version ABROGE_DIFF. Effet limité, car 990 I subsiste pour les décès antérieurs. |
| RT-CSS12-04 (P2) | « La loi » non identifiée dans un texte réglementaire | Même schéma dans le domaine, traité comme constat propre et distinct (RT-DOMSUCC-06), sans double compte. |

Aucune objection existante n'est contredite.

## 4. Constats

Le détail complet (passages, empreintes, références) figure dans `DOM-SUCC.json`.

| ID | Prio. | Nature | Statut | Résumé |
|---|---|---|---|---|
| RT-DOMSUCC-01 | P1 | incohérence du projet | confirmé | Exonération attachée au décès d'un tiers et non au défunt auteur : contournement des droits de donation maintenus (750 ter II, 757 B, 990 I, 792-0 bis II 2, 792 bis, 784 C). |
| RT-DOMSUCC-02 | P1 | incohérence du projet | à confirmer | Abrogation de 754 A : l'accroissement tontinier retombe dans le droit de vente, non neutralisé (750 ter II, 662 et 677 ne visent que les droits gratuits ou « par décès »). |
| RT-DOMSUCC-03 | P2 | risque juridique | à confirmer | Les droits de donation deviennent largement optionnels : perte du principal point de révélation des dons manuels (784, 800) et incitation à attendre le décès ; égalité devant l'impôt à motiver. |
| RT-DOMSUCC-04 | P2 | simple alerte | confirmé | La valeur d'acquisition au décès est bien coordonnée, mais elle est surévaluable sans coût ; la charge de la preuve n'est pas fixée ; les termes varient. |
| RT-DOMSUCC-05 | P2 | coordination manquante | à confirmer | La suppression de la CSG au décès (L136-7 VII, PEA compris) dépasse l'orientation : à documenter comme mesure distincte ; CRDS (ordonnance 96-50, article 16) non coordonnée. |
| RT-DOMSUCC-06 | P2 | incohérence du projet | confirmé | Six désignations différentes de la loi et plusieurs critères temporels. Absence et déclaration judiciaire de décès non réglées. Transition de 1722 bis figée, contraire à 397 de l'annexe III corrigé. |
| RT-DOMSUCC-07 | P2 | risque juridique | à confirmer | 754 B II : une présomption successorale devient une présomption générale contre les dirigeants. |
| RT-DOMSUCC-08 | P2 | réserve documentaire | confirmé | LPF, code des assurances, code de la mutualité, CMF, code civil, ordonnance 96-50 et conventions : résultat non démontré hors corpus. |

### 4.1 RT-DOMSUCC-01 — Le « décès d'un tiers » comme voie de contournement

Le II de 750 ter dispose : « Aucun droit de mutation à titre gratuit n'est dû en France à raison d'un décès ». L'exonération couvre les « sommes [...] dues par un assureur [...] à raison du décès d'un assuré ». Le critère retenu est donc l'événement, non l'auteur de la libéralité. Quatre situations en découlent :

- **Assurance sur la tête d'un tiers.** Un souscripteur vivant paie les primes d'un contrat sur la tête d'un assuré âgé. Au décès de l'assuré, le bénéficiaire reçoit un capital exonéré. La doctrine y voit aujourd'hui une donation indirecte possible (rép. min., QE n° 60434).
- **Trust.** Le 792-0 bis II 2 proposé exonère les attributions « à raison du décès du constituant ou d'un bénéficiaire ». Or, dans la source (II 1), une transmission du vivant du constituant est une donation.
- **Fiducie.** Le 792 bis proposé exonère de même les transferts au décès d'un bénéficiaire, alors que la source taxe toute transmission libérale à 60 %.
- **Libéralités graduelles et résiduelles.** Le 784 C proposé exonère la transmission au second gratifié au décès du premier, même si l'auteur est vivant. La source taxait d'après le lien entre l'auteur et le second gratifié.

Exemple : un donateur fait une donation graduelle à son conjoint (abattement de 80 724 €, barème du tableau II), à charge de transmettre à un neveu. Le neveu recevra au décès du conjoint sans aucun droit, alors qu'une donation directe aurait supporté 55 % après 7 967 € d'abattement.

### 4.2 RT-DOMSUCC-02 — Tontine

Le second alinéa de la source de 754 A prouve qu'en dehors de cet article, la tontine relève d'un autre régime : celui des droits de mutation à titre onéreux, selon le rapport du Congrès des notaires de 2026. Le projet abroge l'article en entier. 750 ter II ne neutralise que les droits à titre gratuit, 662 4° les droits « par décès », 677 « l'imposition [...] de succession ». Le droit de vente sur la part du prémourant n'est neutralisé par aucun de ces textes. Le projet a pourtant repris la définition de la clause pour l'IFI (968 bis).

### 4.3 Autres constats (P2)

Voir le tableau et le fichier JSON. Points saillants :

- **RT-DOMSUCC-05.** Le VII de L136-7 supprime la CSG due « du seul fait du décès, du dénouement d'un contrat ou d'un plan par ce décès ». Il touche donc aussi le PEA. Ces prélèvements portent sur des revenus, ce ne sont pas des droits de succession requalifiés.
- **RT-DOMSUCC-06.** Les variantes relevées sont : « la présente loi » (y compris dans les annexes réglementaires), « la loi supprimant les droits de mutation par décès », « la loi portant suppression des droits de succession », « la loi supprimant les droits français de mutation à titre gratuit par décès et le prélèvement prévu à l'article 990 I », « la loi portant la présente réforme », « la loi ».

## 5. Mécanique d'ensemble — éléments vérifiés sans objection

- **Assurance-vie.** 757 B et 990 I sont abrogés pour les décès. 990 I bis neutralise les sommes de la CDC dues pour un décès nouveau, même restituées plus tard. Le versement ne peut plus être bloqué (806 ; annexe II 292 A, 292 B, 306-0 F ; annexe III 344 G nonies), et la télédéclaration du prélèvement disparaît (1649 quater B quater, 1681 septies). L'échéance contractuelle hors décès reste soumise à 990 I bis. FICOVIE (1649 ter) est maintenu pour sa propre finalité.
- **Dutreil.** 787 B et 787 C : le pacte post mortem est retiré. Les engagements attachés à une donation antérieure survivent au décès du donataire. Les engagements des décès antérieurs relèvent du régime ancien. C'est cohérent avec les droits acquis.
- **Rappel fiscal.** 784 : le rappel de quinze ans et la consommation des abattements sont conservés pour les donations ; aucun rappel n'a lieu au décès.
- **Présents d'usage et dons manuels.** 757 et 635 A sont inchangés ou explicités ; les présents d'usage, d'origine jurisprudentielle, ne sont pas touchés.
- **Territorialité et conventions.** 750 ter I est réécrit pour les seules donations, sauf le renvoi à 990 D (RT-P1-CGI-C-05). 784 A interdit tout crédit sans impôt français. 789 (territoires d'outre-mer) est abrogé pour les décès. Les conventions ne sont pas vérifiées (RT-DOMSUCC-08). Aucun risque européen identifié : l'exonération est générale et ne dépend ni de la résidence ni de la situation des biens.
- **TPF et droits fixes.** 677 1° exclut les décès nouveaux. 1133 neutralise la réserve de 1020. L'enregistrement des testaments (636) est supprimé pour les nouveaux décès. 1071 (Croix-Rouge) est daté au décès. 791 (0,60 % pour les donations) est maintenu. Le droit de partage (746 à 748) est maintenu par choix explicite et documenté : son fait générateur est distinct. Ce n'est pas une objection, mais un point politique à signaler, puisqu'il devient le principal coût fiscal d'une succession en indivision.
- **IFI.** 973 fige les méthodes d'évaluation des droits de mutation par décès. 970 et 968 bis sont autonomisés. 982 renvoie à 204, qui est coordonné.
- **Plus-values.** Cinq textes sont coordonnés (RT-DOMSUCC-04, qui ne porte que sur la preuve).
- **Transition.** Chaque article réserve les décès antérieurs, sans remboursement général. 990 I : le versement ultérieur suit la date du décès. L'annexe III 397 a été corrigée pour les demandes de crédit postérieures.
- **Constitution.** Pas de rétroactivité. La différence de traitement entre décès antérieurs et postérieurs repose sur la date et est classiquement admise. Le point de l'asymétrie avec les donations est traité en RT-DOMSUCC-03 ; une incompétence négative serait possible si la date d'effet reste relative (RT-DOMSUCC-06).

## 6. Propositions de correction (séparées des constats)

### C1 — RT-DOMSUCC-01

**750 ter, II** : ajouter un quatrième alinéa :

> « Le présent II ne s'applique qu'aux biens, droits, sommes et valeurs dont le défunt est l'auteur de la transmission. Lorsqu'une transmission prend effet au décès d'une personne alors que son auteur est vivant à la date de ce décès, notamment lorsque les primes d'un contrat d'assurance ont été versées par un souscripteur autre que l'assuré et survivant à celui-ci, lorsque l'auteur d'une libéralité graduelle ou résiduelle survit au premier gratifié, ou lorsque le constituant d'un trust ou d'une fiducie survit au bénéficiaire dont le décès entraîne l'attribution, cette transmission constitue, lorsque l'intention libérale est établie, une donation entre vifs soumise au I, appréciée à la date de ce décès pour la valeur alors transmise. »

**Coordinations :**

- **792-0 bis, II 2, 1re phrase** : remplacer « à raison du décès du constituant ou d'un bénéficiaire » par « à raison du décès du constituant ».
- **792-0 bis, II 2** : ajouter « L'attribution consécutive au décès d'un bénéficiaire du vivant du constituant relève du 1 du présent II. »
- **792 bis, 3e alinéa** : remplacer « Le seul décès du constituant ou d'un bénéficiaire » par « Le seul décès du constituant ».
- **784 C, 2e alinéa** : rédiger ainsi :

> « Lorsque le premier légataire ou donataire décède à compter de l'entrée en vigueur de la présente loi et que l'auteur de la libéralité est lui-même décédé, la transmission au second gratifié ne supporte aucun droit de mutation par décès ni prélèvement de remplacement. Lorsque l'auteur de la libéralité est vivant au décès du premier gratifié, la transmission au second gratifié est soumise aux droits de donation d'après le lien de parenté entre l'auteur et le second gratifié, sur la valeur à cette date ; les droits acquittés par le premier gratifié sur les mêmes biens sont imputés. »

- **757 B, 2e alinéa** : ajouter « lorsque les primes ont été versées par l'assuré décédé ou dépendent de sa succession ».

Dépendances : RT-P1-CGI-C-05, à corriger dans la même rédaction de 750 ter ; 990 I.

### C2 — RT-DOMSUCC-02 : 754 A, rédaction complète proposée

> « Les biens recueillis en vertu d'une clause insérée dans un contrat d'acquisition en commun selon laquelle la part du ou des premiers décédés reviendra aux survivants, de telle sorte que le dernier vivant sera considéré comme seul propriétaire de la totalité des biens, sont, au point de vue fiscal, réputés transmis à titre gratuit par le prémourant à chacun des bénéficiaires de l'accroissement.
> Lorsque le prémourant décède à compter de l'entrée en vigueur de la présente loi, cette transmission est exonérée en application du II de l'article 750 ter. L'accroissement ne donne lieu à aucun droit de mutation à titre onéreux ni à aucune taxe proportionnelle de publicité foncière ; le seuil de 76 000 € et l'option prévus dans la rédaction antérieure ne s'appliquent pas à ces décès.
> Pour les décès antérieurs, les dispositions applicables à la date du décès, y compris l'exception relative à l'habitation principale et l'option pour les droits de mutation par décès, continuent de s'appliquer, sans droit général au remboursement. »

Dépendances : 968 bis, qui reste autonome ; 677 ; 662.

### C3 — RT-DOMSUCC-03

Pas de texte normatif. Ajouter à l'exposé des motifs et au chiffrage : objectif de l'asymétrie entre donation et décès ; effet sur les recettes de donation ; perte de la révélation des dons manuels. Aucune formalité de remplacement.

### C4 — RT-DOMSUCC-04

Ajouter dans 150-0 D (1 et 13), 150 VB I, 167 bis I 2, 150 VH bis et l'annexe II 74-0 E ter, après la mention de la valeur au décès :

> « Il appartient au cédant de justifier cette valeur. Lorsqu'une évaluation figure dans un inventaire, un acte de notoriété, une attestation notariée ou un autre acte civil établi à l'occasion du décès, elle est retenue sauf preuve contraire. »

Uniformiser l'expression « valeur vénale réelle ».

### C5 — RT-DOMSUCC-05

- Motiver et chiffrer à part le VII de L136-7, en tant que mesure de baisse de prélèvements distincte.
- Viser dans la loi l'article 16 de l'ordonnance n° 96-50 si la CRDS doit suivre.
- Décider expressément du cas du PEA.

### C6 — RT-DOMSUCC-06

Article non codifié de la loi de réforme :

> « I. – Les dispositions du code général des impôts, de ses annexes et du code de la sécurité sociale modifiées ou abrogées par la présente loi à raison des décès s'appliquent aux successions ouvertes par un décès survenu à compter du [date]. Pour l'application du présent I, la date du décès est, en cas de déclaration judiciaire de décès, celle fixée par le jugement et, en cas de jugement déclaratif d'absence, celle de sa transcription. II. – Les successions ouvertes par un décès antérieur restent régies par les dispositions applicables à la date du décès, sous réserve des règles temporelles propres aux demandes de crédit de paiement ; il n'est procédé à aucun remboursement général. »

Dans les articles codifiés, remplacer toutes les variantes par « à compter du [date] ». Dans **1722 bis**, remplacer « les dispositions applicables à la date du décès continuent de régir » par « les dispositions applicables à ces décès et aux demandes de crédit, selon leurs règles temporelles propres, y compris pour les demandes formées après cette entrée en vigueur, continuent de régir ». La date de transcription en matière d'absence est à confirmer dans le code civil, hors corpus.

### C7 — RT-DOMSUCC-07 : 754 B, II

> « II. – Pour les décès antérieurs à l'entrée en vigueur de la présente loi, la présomption de propriété prévue au II du présent article dans sa rédaction antérieure reste applicable aux droits de mutation par décès afférents à ces décès. Elle ne s'applique à aucun autre impôt. »

### C8 — RT-DOMSUCC-08

Récupérer les textes hors corpus, les relire, puis rédiger les coordinations, notamment la taxation d'office et la reprise propres aux successions non déclarées. Ne pas affirmer de résultat hors du corpus réécrit.

## 7. Incertitudes restantes et éléments non examinés

- BOFiP non relu : tontine, assurance sur la tête d'un tiers, dons manuels.
- Textes du code civil (1048 à 1061, 1002-1, 1078-1 et suivants, absence) non relus.
- Le LPF, le code des assurances, le code de la mutualité, le CMF, l'ordonnance 96-50, le décret n° 55-22 et les conventions bilatérales n'ont pas été lus.
- Les 19 articles de l'annexe II repris par `review_prior` (dans les lots automatiques) n'ont été lus qu'en partie : 292 A, 292 B, 306-0 F et 74-0 E ter en entier ; 293, 294 A, 294 B, 294 E, 294 bis, 294 ter, 294 quater, 306-0 F bis, 310 G, 369, 369 A, 384 A, 384-0 A bis, 384 A bis et 384 A ter seulement par la recherche plein texte ; l'annexe IV 121 Z quinquies n'a pas été relue.
- La seconde passe est `pending` pour 116 des 140 articles du lot : leurs propositions peuvent encore changer.
- Aucun chiffrage.

## 8. Couverture réelle

**Lus en entier (source, NOTA, proposition, motif et notes, versions courantes et futures) :**

- **CGI.** 641, 641 bis, 642, 644, 645, 750 ter, 751, 752, 753, 754, 754 A, 754 B, 755, 756 bis, 757, 757 A (motif), 757 B, 757 C, 763 bis, 776 A, 777, 778, 778 bis, 779, 782, 783, 784, 784 A, 784 B, 784 C, 776 ter, 786, 787 A, 787 B (proposition entière), 788, 788 bis, 789, 790, 790 B, 790 D, 790 E, 790 H (deux versions), 791, 791 ter, 792-0 bis, 792 bis, 795 B, 797 A, 800, 805, 806, 808, 968 bis, 973, 983, 990 I, 1133, 1701, 1709, 1710, 1715, 1716 A, 1716 bis, 1717, 1722 bis, 1722 ter, 1722 quater, 1965, 1965 A, 635 A, 636, 1071, 235 ter.
- **Annexe III.** 396, 397, 397 A, 400, 401, 404 A, 404 B, 404 GA, 404 GC, 350 quindecies.
- **Annexe II.** 292 A, 292 B, 306-0 F (propositions), 74-0 E ter.
- **CSS.** L136-7 (parties décès et PEA, motif, notes) et L136-1-2 (9° et III).

**Lus par extraits ciblés (clauses de décès, motifs et notes ; proposition partielle) :**

- 758, 759, 760, 761, 762 bis, 763, 776, 787 C, 793, 793 bis, 793 ter, 793 quater, 794, 795, 795-0 A, 795 A, 796 bis, 798, 799, 648, 662, 677, 851, 859, 881 L, 970, 990 I bis, 990 J, 1131, 1649 quater B quater, 1681 septies, 1727, 1728, 1729 B, 1754, 1837, 1840 G, 1691 ter.
- Annexe III : 280, 280 A, 280 B, 281 B, 281 O, 281 bis, 281 ter, 281 C, 281 H, 281 H bis, 281 I, 281 J, 281 M, 344 G nonies, 350 terdecies.
- Sources partielles de 150-0 D, 150 VB, 150 VH bis et 167 bis, propositions lues sur les passages de la valeur d'acquisition.

**Lus par empreinte (propositions identiques, texte type d'abrogation lu une fois ; sources non relues en entier) :**

- 764, 764 A, 764 bis, 766, 766 bis, 767 à 770, 773, 774, 774 bis, 775, 775 bis, 775 quater, 775 quinquies, 775 sexies (empreinte `33073712f1e5`).
- 796-0, 796-0 bis, 796-0 ter, 796-0 quater, 796-0 quinquies, 796, 797, 801, 802, 802 bis, 803, 807 (empreinte `dd9d4ca23191`).
- 1135 bis, 1238, 1826 (empreinte `0ecc39c79066`).

**Non lus :** 1840 F (lu seulement dans le listage du lot) ; 121 Z quinquies (annexe IV) ; les articles de l'annexe II cités ci-dessus, hors recherche plein texte ; 790 A, 790 A bis, 790 F, 790 G et 776 bis, 776 quater (lots automatiques, champ des donations) ; les articles de l'IFI autres que 968 bis, 970, 973, 982 et 983.

## 9. Périmètre : liste des articles du lot `successions` et statut de seconde passe

Lot successions : 140 articles ; seconde passe : {'pending': 116, 'completed': 24} ; types : {'rewrite': 60, 'full_repeal': 71, 'normative_reduction': 9}

| Code | Article | Version | Lot | Type | Seconde passe |
|---|---|---|---|---|---|
| cgi | 750 ter | LEGIARTI000024453202 | 001.json | rewrite | pending |
| cgi | 757 B | LEGIARTI000047288569 | 001.json | full_repeal | pending |
| cgi | 990 I | LEGIARTI000047288653 | 001.json | full_repeal | pending |
| cgi | 641 | LEGIARTI000006305176 | 001.json | full_repeal | pending |
| cgi | 800 | LEGIARTI000041471327 | 001.json | full_repeal | pending |
| cgi | 806 | LEGIARTI000042194226 | 001.json | full_repeal | pending |
| cgi | 751 | LEGIARTI000027517865 | 200.json | full_repeal | pending |
| cgi | 752 | LEGIARTI000027517860 | 200.json | full_repeal | pending |
| cgi | 753 | LEGIARTI000006305356 | 200.json | full_repeal | pending |
| cgi | 754 | LEGIARTI000006305357 | 200.json | full_repeal | pending |
| cgi | 754 A | LEGIARTI000021629563 | 200.json | full_repeal | pending |
| cgi | 754 B | LEGIARTI000022201691 | 200.json | rewrite | pending |
| cgi | 755 | LEGIARTI000054373367 | 200.json | rewrite | pending |
| cgi | 777 | LEGIARTI000030061736 | 200.json | rewrite | pending |
| cgi | 779 | LEGIARTI000026292566 | 200.json | rewrite | pending |
| cgi | 784 | LEGIARTI000033809289 | 200.json | rewrite | pending |
| cgi | 784 A | LEGIARTI000006305429 | 200.json | rewrite | pending |
| cgi | 784 C | LEGIARTI000006305431 | 200.json | rewrite | pending |
| cgi | 786 | LEGIARTI000054373359 | 201.json | rewrite | pending |
| cgi | 787 A | LEGIARTI000044375617 | 201.json | rewrite | pending |
| cgi | 787 B | LEGIARTI000053542700 | 201.json | rewrite | pending |
| cgi | 787 C | LEGIARTI000053542704 | 201.json | rewrite | pending |
| cgi | 788 | LEGIARTI000042194220 | 201.json | full_repeal | pending |
| cgi | 788 bis | LEGIARTI000006305439 | 201.json | full_repeal | pending |
| cgi | 789 | LEGIARTI000006305441 | 201.json | full_repeal | pending |
| cgi | 792-0 bis | LEGIARTI000054335294 | 201.json | normative_reduction | pending |
| cgi | 792 bis | LEGIARTI000006305462 | 201.json | rewrite | pending |
| cgi | 764 | LEGIARTI000045277005 | 202.json | full_repeal | pending |
| cgi | 764 A | LEGIARTI000006305384 | 202.json | full_repeal | pending |
| cgi | 764 bis | LEGIARTI000006305387 | 202.json | full_repeal | pending |
| cgi | 766 | LEGIARTI000006305390 | 202.json | full_repeal | pending |
| cgi | 766 bis | LEGIARTI000020194752 | 202.json | full_repeal | pending |
| cgi | 767 | LEGIARTI000006305391 | 202.json | full_repeal | pending |
| cgi | 768 | LEGIARTI000006305392 | 202.json | full_repeal | pending |
| cgi | 769 | LEGIARTI000006305393 | 202.json | full_repeal | pending |
| cgi | 770 | LEGIARTI000006305394 | 202.json | full_repeal | pending |
| cgi | 773 | LEGIARTI000027517853 | 202.json | full_repeal | pending |
| cgi | 774 | LEGIARTI000022328750 | 202.json | full_repeal | pending |
| cgi | 774 bis | LEGIARTI000048777677 | 202.json | full_repeal | pending |
| cgi | 775 | LEGIARTI000006305398 | 202.json | full_repeal | pending |
| cgi | 775 bis | LEGIARTI000006305405 | 202.json | full_repeal | pending |
| cgi | 775 quater | LEGIARTI000006305407 | 202.json | full_repeal | pending |
| cgi | 775 quinquies | LEGIARTI000018015397 | 202.json | full_repeal | pending |
| cgi | 775 sexies | LEGIARTI000028403238 | 202.json | full_repeal | pending |
| cgi | 758 | LEGIARTI000006310326 | 202.json | rewrite | pending |
| cgi | 759 | LEGIARTI000006305374 | 202.json | rewrite | pending |
| cgi | 760 | LEGIARTI000030110697 | 202.json | rewrite | pending |
| cgi | 761 | LEGIARTI000006305376 | 202.json | rewrite | pending |
| cgi | 762 bis | LEGIARTI000006305379 | 202.json | rewrite | pending |
| cgi | 763 | LEGIARTI000006305381 | 202.json | rewrite | pending |
| cgi | 776 | LEGIARTI000006310345 | 202.json | rewrite | pending |
| cgi | 776 ter | LEGIARTI000026292571 | 202.json | rewrite | pending |
| cgi | 793 | LEGIARTI000051149498 | 203.json | rewrite | pending |
| cgi | 793 bis | LEGIARTI000051216307 | 203.json | rewrite | pending |
| cgi | 793 ter | LEGIARTI000006305472 | 203.json | rewrite | pending |
| cgi | 793 quater | LEGIARTI000006305474 | 203.json | rewrite | pending |
| cgi | 794 | LEGIARTI000044982923 | 203.json | rewrite | pending |
| cgi | 795 | LEGIARTI000045293476 | 203.json | rewrite | pending |
| cgi | 795-0 A | LEGIARTI000030010994 | 203.json | rewrite | pending |
| cgi | 795 A | LEGIARTI000042654712 | 203.json | rewrite | pending |
| cgi | 796-0 | LEGIARTI000006305479 | 203.json | full_repeal | pending |
| cgi | 796-0 bis | LEGIARTI000006305480 | 203.json | full_repeal | pending |
| cgi | 796-0 ter | LEGIARTI000006305481 | 203.json | full_repeal | pending |
| cgi | 796-0 quater | LEGIARTI000017923876 | 203.json | full_repeal | pending |
| cgi | 796-0 quinquies | LEGIARTI000048777670 | 203.json | full_repeal | pending |
| cgi | 796 | LEGIARTI000044375614 | 203.json | full_repeal | pending |
| cgi | 797 | LEGIARTI000028417042 | 203.json | full_repeal | pending |
| cgi | 801 | LEGIARTI000006305499 | 203.json | full_repeal | pending |
| cgi | 802 | LEGIARTI000006310440 | 203.json | full_repeal | pending |
| cgi | 802 bis | LEGIARTI000053546893 | 203.json | full_repeal | pending |
| cgi | 803 | LEGIARTI000022174492 | 203.json | full_repeal | pending |
| cgi | 805 | LEGIARTI000022174494 | 203.json | full_repeal | pending |
| cgi | 807 | LEGIARTI000036362930 | 203.json | full_repeal | pending |
| cgi | 808 | LEGIARTI000022174500 | 203.json | full_repeal | pending |
| cgi | 796 bis | LEGIARTI000033805204 | 203.json | rewrite | pending |
| cgi | 798 | LEGIARTI000006305490 | 203.json | rewrite | pending |
| cgi | 799 | LEGIARTI000006305492 | 203.json | rewrite | pending |
| cgi | 641 bis | LEGIARTI000028417046 | 204.json | full_repeal | pending |
| cgi | 642 | LEGIARTI000027978362 | 204.json | full_repeal | pending |
| cgi | 644 | LEGIARTI000044981649 | 204.json | full_repeal | pending |
| cgi | 645 | LEGIARTI000006305180 | 204.json | full_repeal | pending |
| cgi | 1135 bis | LEGIARTI000051149532 | 204.json | full_repeal | pending |
| cgi | 1238 | LEGIARTI000049117453 | 204.json | full_repeal | pending |
| cgi | 1709 | LEGIARTI000020034005 | 204.json | full_repeal | pending |
| cgi | 1710 | LEGIARTI000006313654 | 204.json | full_repeal | pending |
| cgi | 1715 | LEGIARTI000006313658 | 204.json | full_repeal | pending |
| cgi | 1716 A | LEGIARTI000006312803 | 204.json | full_repeal | pending |
| cgi | 1722 bis | LEGIARTI000006313662 | 204.json | full_repeal | pending |
| cgi | 1722 ter | LEGIARTI000006313663 | 204.json | full_repeal | pending |
| cgi | 1722 quater | LEGIARTI000022201877 | 204.json | full_repeal | completed |
| cgi | 1826 | LEGIARTI000006313963 | 204.json | full_repeal | pending |
| cgi | 648 | LEGIARTI000006305185 | 204.json | rewrite | pending |
| cgi | 662 | LEGIARTI000041466161 | 204.json | rewrite | pending |
| cgi | 859 | LEGIARTI000022174358 | 204.json | rewrite | pending |
| cgi | 881 L | LEGIARTI000053545671 | 204.json | rewrite | pending |
| cgi | 973 | LEGIARTI000048806768 | 204.json | rewrite | pending |
| cgi | 990 I bis | LEGIARTI000031781404 | 204.json | rewrite | pending |
| cgi | 990 J | LEGIARTI000036428777 | 204.json | rewrite | pending |
| cgi | 1131 | LEGIARTI000006305929 | 204.json | rewrite | pending |
| cgi | 1649 quater B quater | LEGIARTI000051764508 | 204.json | normative_reduction | pending |
| cgi | 1681 septies | LEGIARTI000051764486 | 204.json | normative_reduction | pending |
| cgi | 1701 | LEGIARTI000006313642 | 204.json | rewrite | pending |
| cgi | 1716 bis | LEGIARTI000036428719 | 204.json | rewrite | pending |
| cgi | 1754 | LEGIARTI000053881346 | 204.json | rewrite | pending |
| cgi | 1965 | LEGIARTI000006314077 | 204.json | rewrite | pending |
| cgi | 1965 A | LEGIARTI000006313406 | 204.json | rewrite | pending |
| a3 | 280 | LEGIARTI000006299245 | 205.json | full_repeal | completed |
| a3 | 280 A | LEGIARTI000025624869 | 205.json | full_repeal | completed |
| a3 | 280 B | LEGIARTI000027799315 | 205.json | full_repeal | completed |
| a3 | 281 B | LEGIARTI000006299255 | 205.json | full_repeal | completed |
| a3 | 281 O | LEGIARTI000048839993 | 205.json | full_repeal | completed |
| a3 | 397 | LEGIARTI000048852299 | 205.json | full_repeal | completed |
| a3 | 404 A | LEGIARTI000048852254 | 205.json | full_repeal | completed |
| a3 | 404 B | LEGIARTI000048852245 | 205.json | full_repeal | completed |
| a3 | 404 GA | LEGIARTI000048852235 | 205.json | full_repeal | completed |
| a3 | 281 bis | LEGIARTI000043855518 | 205.json | normative_reduction | completed |
| a3 | 281 ter | LEGIARTI000043855509 | 205.json | normative_reduction | completed |
| a3 | 281 C | LEGIARTI000006299256 | 205.json | full_repeal | completed |
| a3 | 281 H | LEGIARTI000025887020 | 205.json | normative_reduction | completed |
| a3 | 281 H bis | LEGIARTI000027527832 | 205.json | full_repeal | completed |
| a3 | 281 I | LEGIARTI000025887017 | 205.json | full_repeal | completed |
| a3 | 281 J | LEGIARTI000018617987 | 205.json | normative_reduction | completed |
| a3 | 281 M | LEGIARTI000030493222 | 205.json | normative_reduction | completed |
| a3 | 344 G nonies | LEGIARTI000031116715 | 205.json | normative_reduction | completed |
| a3 | 350 terdecies | LEGIARTI000047623583 | 205.json | rewrite | completed |
| a3 | 396 | LEGIARTI000022343738 | 205.json | rewrite | completed |
| a3 | 397 A | LEGIARTI000006299725 | 205.json | rewrite | completed |
| a3 | 401 | LEGIARTI000048852279 | 205.json | rewrite | completed |
| a3 | 404 GC | LEGIARTI000048852230 | 205.json | rewrite | completed |
| cgi | 970 | LEGIARTI000036385015 | 206.json | rewrite | pending |
| cgi | 677 | LEGIARTI000019264747 | 206.json | rewrite | pending |
| cgi | 1840 F | LEGIARTI000006313198 | 206.json | full_repeal | pending |
| cgi | 851 | LEGIARTI000006305536 | 206.json | rewrite | pending |
| cgi | 635 A | LEGIARTI000025842147 | 206.json | rewrite | pending |
| cgi | 1691 ter | LEGIARTI000046201218 | 207.json | rewrite | pending |
| cgi | 1727 | LEGIARTI000051213330 | 207.json | rewrite | pending |
| cgi | 1728 | LEGIARTI000053546784 | 207.json | rewrite | pending |
| cgi | 1840 G | LEGIARTI000028448157 | 207.json | rewrite | pending |
| cgi | 1729 B | LEGIARTI000043982240 | 208.json | rewrite | pending |
| cgi | 1837 | LEGIARTI000029041636 | 208.json | rewrite | pending |

Articles hors lot examinés (propriétaire, statut) : 757, 757 C, 763 bis, 776 A, 778, 778 bis, 782, 784 B, 790, 790 B, 790 D, 790 E, 790 H, 791, 791 ter, 795 B, 797 A et 1717 (automatic-impots, retained_unchanged, pending) ; 783 (automatic-impots, pending) ; 150-0 D, 150 VB, 150 VH bis et 167 bis (automatic-impots, completed) ; 968 bis (pending) ; 636, 1071 et 1133 (pending) ; 235 ter, L136-7 et L136-1-2 (completed) ; annexe II 74-0 E ter, 292 A, 292 B et 306-0 F (completed). Versions futures sans proposition (not_in_inventory) : 1727 et 1754 (2027), 1729 B (2027), 1649 quater B quater (2027, 2030), 1681 septies (2030) et 790 H (2027).
