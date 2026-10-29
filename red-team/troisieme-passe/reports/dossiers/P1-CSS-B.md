# P1-CSS-B : renvois vers des abrogations proposées (Code de la sécurité sociale)

Red-team juridique indépendante, troisième passe. Rapport établi le 26 octobre 2026 sur l'instantané `snapshots/20261026T230545Z`, pour un corpus LEGI arrêté au **18 octobre 2026**. Paquet `reports/p1-work/P1-CSS-B.json` : 39 clusters et 107 alertes P1 de l'audit GLOBAL du 25 octobre (`global-reference-audit-20261025T2341Z`), toutes encore « live ».

Cette revue est faite par une IA. Elle **ne vaut pas validation par un juriste**. La seconde passe continue en production (11 052 articles relus, 19 262 restants) : les conclusions valent pour les empreintes citées et restent provisoires. Aucune écriture n'a été faite hors des trois livrables et des exports de `tools/cite.py`. Aucune source extérieure n'a été consultée en ligne : les références au code pénal, au code de la santé publique, aux décrets et ordonnances cités par les NOTA, et au droit de l'Union, sont identifiées mais **non lues**.

## 1. Résumé

| ID | Priorité | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-P1-CSS-B-02 | P1 | incohérence du projet | confirmé | L162-1-7-1 abrogé, mais dix décrets (dont R161-45 et R163-2 réécrits) subordonnent encore la prise en charge à la mention ou au document « conformément à l'article L. 162-1-7-1 » |
| RT-P1-CSS-B-04 | P1 | coordination manquante | confirmé | Droits de plaidoirie supprimés (L652-6), mais R652-26 à R652-35 sont maintenus avec des motifs contraires ; une version de R652-26 en vigueur en 2029, sans proposition, les réédicte |
| RT-P1-CSS-B-06 | P1 | risque juridique | confirmé | Ressources de la CNBF (tiers des charges du régime de base) et de l'ASV (cotisation d'ajustement) supprimées sans ressource de remplacement, alors que R652-36 et D645-5 limitent la garantie des prestations aux ressources affectées : risque pour les pensions et droits acquis |
| RT-P1-CSS-B-08 | P1 | incohérence du projet | confirmé | Suffixe générique supprimé (L162-17-1), mais R163-7 et R163-2 réécrits conservent l'obligation et la radiation sans avis |
| RT-P1-CSS-B-09 | P1 | incohérence du projet | confirmé | Condition d'examen prénatal pour la prime à la naissance supprimée (L533-1), mais D532-2 et D532-1 réécrits la maintiennent |
| RT-P1-CSS-B-01 | P2 | coordination manquante | confirmé | Forfait journalier (L174-4) : dix renvois non bornés aux journées anciennes, neutralisés seulement par la clause législative (dont la non-réduction de l'AAH) |
| RT-P1-CSS-B-03 | P2 | incohérence du projet | confirmé | R382-84 réécrit, R243-44 et R644-2 renvoient encore aux contraventions de R244-4 et R244-5 supprimées (à fusionner avec le paquet P1-CSS-A) |
| RT-P1-CSS-B-05 | P2 | incohérence du projet | confirmé | La faveur proposée à R652-31 (déduction des droits reversés en retard) ne vise que des années supprimées : elle est sans effet |
| RT-P1-CSS-B-07 | P2 | incohérence du projet | confirmé | L922-8 et L612-2 réécrits étendent encore L931-26 et L272-2 abrogés |
| RT-P1-CSS-B-10 | P2 | coordination manquante | confirmé | D545-8 5° exige encore les documents de D512-2 abrogé (séjour des enfants) pour l'allocation versée en cas de décès d'un enfant |
| RT-P1-CSS-B-11 | P2 | anomalie d'inventaire | confirmé | Notes de revue obsolètes (L138-20, R133-9, R543-6, R163-2, R652-26) décrivant comme maintenues des règles abrogées |

**Classification des 107 alertes** (`reports/p1-work/P1-CSS-B-classification.jsonl`, toutes lues en entier) : 67 alertes écartées, 1 faux positif, 19 coordinations manquantes, 12 incohérences du projet, 1 anomalie d'inventaire, 2 simples alertes, 5 couvertes par un autre dossier (2 UNION, 3 douze coordinations CSS). Aucune n'est « non examinée ».

## 2. Méthode

1. Pour chacun des 39 clusters, j'ai exporté par `tools/cite.py` la cible et chaque article qui y renvoie (version identifiée par LEGIARTI), puis je les ai lus en entier : source, NOTA, bornes, état, proposition, motif, notes de revue, lot propriétaire et statut d'inventaire. Les exports sont dans `evidence/cited/20261026T230545Z/`. Pour les clusters dont l'effet dépassait les articles qui renvoient, j'ai lu des compléments : R652-26 version 2029, R652-27, R652-28, R652-29, R652-32, R652-35, R652-36, L652-7, D645-5, D532-1 (toutes versions), L512-2.
2. J'ai vérifié que chaque numéro cité vise bien la cible : même code, même article. Les annexes III et IV et le CGI renvoient bien au CSS, et aucun homonyme n'a été trouvé. J'ai aussi vérifié que la cible est réellement abrogée. R931-3-16 ne l'est qu'en partie : c'est un faux positif de l'audit.
3. Règles de qualification appliquées de façon uniforme :
   - **écartée** : l'article qui renvoie est lui-même abrogé et coordonné ; ou le renvoi est borné aux périodes anciennes, ou neutralisé par une clause de la cible ou du texte qui renvoie ; ou l'application est auto-limitée (« l'année au titre de laquelle la contribution est due », « le cas échéant ») ; ou le renvoi porte sur une **plage** d'articles, qui applique alors l'article abrogé dans son état abrogé sans le rétablir ;
   - **coordination manquante** : un texte maintenu inchangé applique nominativement la règle abrogée comme vivante ;
   - **incohérence du projet** : une proposition réécrite s'appuie activement sur la règle abrogée ;
   - **priorité** : P2 lorsqu'une clause législative expresse prive d'effet le renvoi et que le défaut reste rédactionnel ; P1 lorsque la neutralisation est partielle ou absente et qu'un organisme appliquera probablement le texte réglementaire.
4. Une objection par effet juridique distinct, avec la liste de tous les articles concernés. Les doublons d'alertes (même article, plusieurs occurrences) sont classés individuellement mais ne forment qu'une objection.
5. Orientations confrontées : `policy-coordinations.json` (`retraite`, `cuts_and_reliefs_2026_10_19`, `editorial_direction_2026_10_19`, `substantive_outcomes_2026_10_19`, `dispositifs_medicaux`, `reporting_social`). Aucune correction proposée ne rétablit un prélèvement ou une formalité supprimés. Chacune conserve les faveurs et les règles applicables aux périodes anciennes.

## 3. Constats par cluster

Les numéros Cxx renvoient à l'ordre des clusters du paquet.

- **C00 L174-4 (forfait journalier)**, 12 alertes. L'abrogation porte sur les journées postérieures à l'entrée en vigueur. Elle comporte une clause générale de neutralisation des renvois, une fiction qui maintient l'AAH et une clause de conformité pour L871-1 et L911-7. L174-15-3, abrogé, et L162-31-1, dont la dérogation expérimentale est neutralisée, sont écartés. Les dix autres renvois → **RT-01** (P2).
- **C01 L162-1-7-1 (document du prescripteur)**, 11 alertes. D162-29 est déjà coordonné (écarté). Dix décrets → **RT-02** (P1).
- **C02 L138-19-8 (contribution « Z »)**, 6 alertes sur D138-3 et D138-4 : écartées. Ces textes sont auto-limités aux années pour lesquelles la contribution est due, et les années anciennes restent régies.
- **C03 L245-7 (cotisation sur les alcools à plus de 18 %)**, 5 alertes : écartées. 406 terdecies (annexe III) et 54-0 BV (annexe IV, « le cas échéant ») ne visent que les créances encore dues ; 238 bis GA, D245-14 et L245-9-1 sont abrogés avec la même frontière (exigibilité de l'accise).
- **C04 R244-5 (récidive contraventionnelle)**, 5 alertes. L244-4 et L244-1 proposés sont coordonnés (écartés). R382-84 réécrit, R243-44 et R644-2 → **RT-03** (P2).
- **C05 L245-5-1 (contribution sur la promotion des dispositifs médicaux)**, 5 alertes. R245-16-1/2 (abrogés), R138-19 et L241-2 sont écartés. L138-20 → **RT-11** (asymétrie avec la contribution Z et note inexacte, sans effet juridique).
- **C06 L862-4-1 (0,8 % sur les organismes complémentaires)**, 4 alertes : toutes coordonnées par des bornes annuelles, donc écartées.
- **C07 R613-10 et C16 R613-9 (taxation forfaitaire et pénalité des travailleurs indépendants)**, 5 alertes : écartées. 41 DG ter (annexe III) neutralise les renvois ; R243-19 garde une compétence résiduelle ; le renvoi de R133-9 est historique (sa note est obsolète, voir RT-11).
- **C08 L137-27 (contribution sur la publicité des jeux)**, 3 alertes : écartées. CGI 302 bis ZG, ZH et ZI sont eux-mêmes abrogés, et leur réserve vise une plage d'articles.
- **C09 L374-1 (remboursement patronal pour les étrangers)**, 3 alertes : D374-2, D374-6 et L243-2 coordonnés, écartées.
- **C10 R135-26 (tutelle du FRR)**, 3 alertes : écartées, renvoi limité à la transition.
- **C11 L245-5-3 et C19 L245-5-5**, 5 alertes sur R245-16-1/2, eux-mêmes abrogés avec une plage transitoire : écartées.
- **C12 L652-6 (droits de plaidoirie, CNBF)**, 3 alertes. L213-1 est écarté (exception de compétence). R652-26 → **RT-04** (P1) ; R652-31 → **RT-05** (P2). Le cluster révèle aussi **RT-06** (P1, financement du régime autonome).
- **C13 L645-3 (cotisation d'ajustement ASV)**, 3 alertes. L213-1, 2° et 3°, écartés (compétence de recouvrement pour les périodes anciennes). R147-15 réécrit : simple alerte (suspension d'une participation devenue sans objet, sans effet défavorable). Le cluster nourrit **RT-06**, D645-5 réécrit maintenant la limite de garantie.
- **C14 L137-10, C15 L137-14, C23 L137-13 (contributions sur les préretraites et l'actionnariat salarié)**, 8 alertes : écartées. L213-1 4° pose une clause générale (« n'autorise aucun recouvrement sur les versements ou faits générateurs qu'ils soustraient ») ; L241-3 1° est borné ; L131-8 5° affecte un produit résiduel, ce qui ne crée pas d'assiette.
- **C17 L281-4**, 2 alertes (R213-5, R281-4) : **couvertes par le dossier UNION** (RT-UNION-04).
- **C18 R532-8 (évaluation forfaitaire déclarée illégale, CE n° 420104)**, 2 alertes : écartées. Les renvois sont déjà ramenés à R532-3 à R532-7.
- **C20 L931-26 et C31 L272-2 (peines accessoires)**, 3 alertes. L941-3, renvoi par plage, est écarté. L922-8 et L612-2 réécrits → **RT-07** (P2).
- **C21 R152-8 et C27 L153-6**, 3 alertes (R123-1-1 à deux reprises, R153-2) : **couvertes par le dossier des douze coordinations CSS** de l'index (R123-1-1, R152-8 et R153-2 y figurent). Aucune objection en double.
- **C22 L162-1-9 (commission de l'imagerie)**, 2 alertes. L162-1-9-1 est coordonné (écarté). L162-5 26° : simple alerte (« dans le respect des dispositions des articles L. 162-1-9 … », renvoi inerte).
- **C24 L162-17-1 (suffixe générique)**, 2 alertes → **RT-08** (P1).
- **C25 L533-1 (prime à la naissance)**, 1 alerte → **RT-09** (P1), avec D532-1 réécrit (hors alerte).
- **C26 R815-46, C29 A931-3-3, C30 D848-3, C32 R862-11-5, C37 L382-9, C38 L162-30**, 6 alertes : écartées (coordinations, mainlevée d'office, clauses anti-rétablissement, pouvoirs résiduels).
- **C28 R931-3-16** : **faux positif**. La cible n'est abrogée qu'aux alinéas 1 à 3 (limites d'âge) et conserve la démission du président sous tutelle ; R931-1-28 est coordonné.
- **C33 R382-86 et C34 R815-40**, 2 alertes : écartées (D758-3 et R815-61 renvoient par plage).
- **C35 D512-2 (justificatifs de séjour des enfants)**, 1 alerte : D545-8 → **RT-10** (P2).
- **C36 L244-5**, 1 alerte : R644-2 renvoie par plage (L244-1 à L244-5), écartée. Son renvoi nominatif à R244-4 et R244-5 est traité en RT-03.

## 4. Objections

### RT-P1-CSS-B-02 (P1, incohérence du projet, confirmé) : mention et document de L162-1-7-1

L162-1-7-1 proposé (LEGIARTI000051287773 ; empreintes dans le JSON) abroge pour les soins nouveaux le document du prescripteur, sa transmission et les arrêtés. Il dispose : « L’absence de ce document … ne peut, à elle seule, faire obstacle à la prise en charge. » Le décret n° 2025-1286 avait décliné ce mécanisme dans neuf articles d'inscription, sous la forme d'une mention prévoyant une prise en charge « que si, conformément à l'article L. 162-1-7-1, le prescripteur indique sur l'ordonnance ou renseigne pour l'établissement du document prévu au III de l'article R. 161-45 des éléments… ». Ces neuf articles sont R162-34-13 V, R162-37-2 III, R162-38, R162-73 II, R162-116 II, R163-2 IV, R163-32 II, R163-51 et R165-93. Sept sont maintenus inchangés, avec des motifs de « contrôle ciblé ». R163-2 est réécrit et garde son IV. R161-45 est réécrit : il garde le 6° du I et améliore même le III (« le prescripteur choisit entre le téléservice dédié et le questionnaire… »). Le projet entretient donc le circuit qu'il abroge. La clause législative ne vise que le « document » et l'obstacle « à elle seule ». La mention sur l'ordonnance, condition de prise en charge posée par décret, n'est pas couverte. **Conséquence probable** : refus de remboursement fondés sur des décrets privés de base légale. **Correction minimale** : section 5.1.

### RT-P1-CSS-B-04 (P1, coordination manquante, confirmé) : chaîne réglementaire des droits de plaidoirie

L652-6 proposé : « Aucun droit de plaidoirie n'est dû pour les plaidoiries et représentations intervenant à compter de cette date », et aucune contribution équivalente pour les années nouvelles. Pourtant R652-26 (« Le droit de plaidoirie ne peut faire l'objet d'aucune dispense »), R652-27, R652-28 (13 euros), R652-29, R652-32 et R652-35 sont maintenus. Leurs motifs reposent sur une prémisse contraire : « Cette abolition n’est pas proposée dans ce lot » (R652-26) ; « Une suppression isolée du tarif laisserait une obligation légale sans calcul » (R652-28). L'instantané contient en outre **R652-26 version 2029** (LEGIARTI000052846149, VIGUEUR_DIFF au 1er janvier 2029, issue de l'ordonnance n° 2025-1091, hors inventaire, sans proposition), qui reprend l'exigibilité. **Conséquence probable** : perception de 13 euros par plaidoirie et appels de contribution équivalente malgré la loi. **Correction** : section 5.2. Le traitement des versions futures rejoint RT-XCUT-01.

### RT-P1-CSS-B-06 (P1, risque juridique, confirmé) : financement des droits à pension de deux régimes autonomes

Dans sa source, L652-6 affecte les droits de plaidoirie à la couverture du **tiers des charges** du régime de base de la CNBF. Le projet les supprime, et L652-7 proposé interdit de relever les cotisations en compensation (« Leur suppression ne relève ni le montant ni l'assiette des cotisations »). R652-36, maintenu, dispose : « Les prestations ne sont garanties que dans la limite des ressources affectées au compte correspondant. » Il prévoit aussi le remboursement des avances entre fonds par majoration de cotisation. Pour l'ASV, L645-3 proposé supprime la cotisation d'ajustement, tandis que D645-5 réécrit garde la limite de garantie aux ressources affectées. Les notes de L645-3 reconnaissent le « financement des engagements anciens non démontré ». La phrase « La présente abrogation ne constitue pas un fondement de réduction de ces pensions ou droits » interdit seulement que la suppression serve de motif. Elle ne crée ni ressource ni garantie. Une fois les réserves consommées, le seul mécanisme d'ajustement restant est la réduction des prestations, ou une majoration que la loi interdit. Cela contredit l'orientation « Pensions liquidées et droits déjà constitués protégés ». Le projet procède autrement ailleurs : pour la C3S (L137-30) et le transfert vers la capitalisation (L241-3 II), il subordonne la mesure à un financement voté. **Correction recommandée** (section 5.3) : même condition de financement et clause de garantie des droits, sans renoncer à la suppression ni créer de prélèvement de remplacement. P1 et non P0 : l'atteinte dépend des réserves et des décisions des organes, qui n'ont pas été examinées.

### RT-P1-CSS-B-08 (P1, incohérence du projet, confirmé) : suffixe des génériques

L162-17-1 proposé abroge l'exigence de dénomination avec suffixe générique, et l'inscription « ne peut être refusée » sur ce fondement. Le même lot de décrets (00134) réécrit pourtant R163-7 et R163-2 sans en tenir compte. R163-7 II 1° maintient la radiation **sans avis** d'un générique dont la dénomination de fantaisie « n'est pas complétée par le suffixe prévu par l'article L. 162-17-1 ». R163-2 II maintient la mention du suffixe dans l'arrêté et son ajout à l'étiquetage, à la notice, au RCP et à la publicité. La clause législative vise le refus d'inscription, pas la radiation. **Conséquence probable** : déremboursement possible de génériques et obligation d'étiquetage maintenue. **Correction** : section 5.4.

### RT-P1-CSS-B-09 (P1, incohérence du projet, confirmé) : examen prénatal et prime à la naissance

L533-1 proposé : « Les justificatifs de grossesse exigés pour l'attribution de la prime ne peuvent imposer la réalisation de cet examen. » D532-2 proposé se termine pourtant par : « Cette abrogation ne supprime ni les examens médicaux obligatoires ni la condition propre à la prime à la naissance prévue à l’article L. 533-1. » D532-1 proposé (dépôt unique) garde la déclaration de grossesse « attestée par un document médical constatant la passation du premier examen prénatal ». Les notes de L533-1 signalent elles-mêmes la contradiction, qui n'a pas été corrigée. **Correction** : section 5.5. Conserver le fondement documentaire de D545-8 6° pour l'allocation versée en cas de décès pendant la grossesse.

### RT-P1-CSS-B-01 (P2, coordination manquante, confirmé) : forfait journalier

La clause de L174-4 (« les renvois au forfait supprimé … ne permettent ni sa facturation ni son rétablissement ») et ses fictions (AAH, contrats responsables) rendent le droit futur correct. Mais D174-1, D325-6, R381-80, R381-83, R821-8 I a), R871-2 6° et L162-22-11-1 b) (maintenus), ainsi que L871-1 al. 3, L911-7 II 2° et D325-1 (réécrits), présentent encore le forfait comme dû. Les notes de la cible le reconnaissent : « Ces coordinations hors lot ne sont pas déclarées exécutées. » R821-8 I a) est le cas le plus sensible : sans la fiction législative, l'AAH serait réduite à 30 % après soixante jours d'hospitalisation. Il faut aussi faire valider par un juriste que les clauses durables portées par un article « abrogé » survivent bien à l'abrogation. **Correction** : section 5.6.

### RT-P1-CSS-B-03 (P2, incohérence du projet, confirmé) : contraventions de R244-4 et R244-5

R382-84 réécrit (modèles facultatifs) garde « sous les sanctions prévues aux articles R. 244-4 et R. 244-5 ». R243-44 et R644-2, maintenus, les rendent nominativement applicables. Le principe de légalité empêche toute peine sur ce fondement, mais le texte annonce des sanctions qui n'existent plus. **Doublon probable** avec le cluster R244-4 du paquet P1-CSS-A, qui porte sur les mêmes articles : à fusionner. Correction : section 5.7.

### RT-P1-CSS-B-05 (P2, incohérence du projet, confirmé) : faveur de R652-31 privée d'effet

R652-31 proposé lève la perte de déduction des droits reversés en retard, mais seulement « Pour les contributions dues au titre des années civiles commençant à compter de l'entrée en vigueur de la réforme ». Or ces années sont précisément celles où L652-6 supprime la contribution équivalente. L652-6 renvoie à ces allègements « selon leurs dates d'effet propres ». La faveur ne bénéficie donc à aucune créance. Correction : section 5.2, dernier point.

### RT-P1-CSS-B-07 (P2, incohérence du projet, confirmé) : extensions de peines accessoires abrogées

L922-8 réécrit étend toujours « L. 931-25, L. 931-26 et L. 931-27 » aux institutions de retraite complémentaire. L612-2 réécrit étend toujours « L. 272-2 » au Conseil de la protection sociale des travailleurs indépendants. Les notes des articles abrogés demandent ce retrait. L941-3, qui renvoie par plage, est écarté. Correction : section 5.7.

### RT-P1-CSS-B-10 (P2, coordination manquante, confirmé) : D545-8 et les justificatifs de séjour des enfants

L512-2 proposé interdit tout justificatif relatif à l'entrée et au séjour de l'enfant, et D512-2 est abrogé. D545-8 5°, maintenu, exige encore pour l'allocation forfaitaire versée en cas de décès d'un enfant « l'un des titres ou documents mentionnés aux articles D. 512-1 et D. 512-2 ». Le délai de versement de quinze jours ne court qu'après le recueil de l'ensemble des informations. Correction : section 5.8.

### RT-P1-CSS-B-11 (P2, anomalie d'inventaire, confirmé) : notes obsolètes

Exemples : L138-20 (« Maintien des cinq contributions autonomes », alors que L245-5-1 est abrogé), R133-9 (« R613-10 … n'est pas réécrit », alors qu'il est abrogé), R543-6 (« aucune proposition n'y est publiée » pour R532-8), R163-2 (L162-17-1 traité comme maintenu), R652-26. Ces notes ne valent pas vérification des propositions courantes. Pour L138-20, une réserve temporelle analogue à celle de la contribution Z est proposée (voir le JSON).

## 5. Propositions de correction (présentées séparément)

Les textes ci-dessous sont des passages complets proposés. Ils ne modifient que le point en cause et laissent intactes les autres réformes déjà proposées dans les mêmes articles. Aucun n'introduit de taux, de montant ou de formalité nouvelle.

### 5.1 L162-1-7-1 et ses décrets (RT-02)

**R161-45 proposé.** Remplacer le 6° du I par :
> 6° Abrogé.

Remplacer le III par :
> III. – Abrogé. Aucun document indiquant si la prescription respecte les indications ouvrant droit au remboursement ne peut être exigé pour les produits délivrés, actes, prestations et transports réalisés à compter de l'entrée en vigueur de la loi abrogeant l'article L. 162-1-7-1, y compris sur prescription antérieure. Les documents établis antérieurement restent soumis aux règles de confidentialité et de conservation qui leur sont applicables.

Conserver les autres modifications proposées (II, R161-48) et la clause transitoire finale.

**R162-34-13 V, R162-37-2 III, R162-38 (deuxième alinéa), R162-73 II (troisième alinéa), R162-116 II, R163-2 IV, R163-32 II, R163-51 et R165-93 (troisième alinéa).** Remplacer le passage relatif à la mention par :
> [V / III / …] – Abrogé. Les mentions prises sur le fondement de la rédaction antérieure du présent [alinéa / paragraphe] cessent de subordonner la prise en charge des produits délivrés, actes et prestations réalisés à compter de l'entrée en vigueur de la loi abrogeant l'article L. 162-1-7-1, y compris sur prescription antérieure. Les indications thérapeutiques et les conditions de prise en charge fixées par l'acte d'inscription ou de prise en charge demeurent applicables. Les soins antérieurs, les créances et les recours correspondants restent régis par les dispositions antérieures.

*Justification* : aligner les décrets sur l'abrogation législative, sans formalité de remplacement et sans ouvrir de remboursement hors indication. *Dépendances* : R165-1 (non lu), formulaires et téléservice ; entrée en vigueur conjointe avec la loi.

### 5.2 Chaîne réglementaire de la CNBF (RT-04, RT-05)

**R652-26** (version courante LEGIARTI000039348152 **et** version 2029 LEGIARTI000052846149) :
> Le présent article est abrogé pour les plaidoiries et représentations intervenant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi abrogeant l'article L. 652-6. Pour les plaidoiries et représentations antérieures, le droit de plaidoirie demeure exigible devant les juridictions administratives de droit commun et les juridictions de l'ordre judiciaire, dans les conditions et sous les exemptions prévues par la rédaction antérieure du présent article, notamment devant les conseils de prud'hommes, en matière de contraventions des quatre premières classes, de contentieux de la sécurité sociale ou électoral et pour l'aide juridictionnelle totale aux audiences à bref délai. Aucune exigibilité ni interdiction de dispense ne peut résulter du présent article pour les plaidoiries et représentations postérieures.

**R652-27, R652-28, R652-29** : ajouter en tête « Pour les plaidoiries et représentations antérieures au 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi abrogeant l'article L. 652-6, ». **R652-32** : ajouter en tête « Pour les contributions équivalentes dues au titre des années antérieures à leur suppression, ».

**R652-35, deuxième alinéa** :
> Le premier compte reçoit, outre l'intégralité du produit des droits de plaidoirie et des contributions équivalentes dus au titre des périodes antérieures à leur suppression, le montant des cotisations personnelles prévues à l'article L. 652-7.

**R652-31, dernier alinéa** (RT-05) :
> La déduction prévue au deuxième alinéa du II s'applique, quel que soit le délai de reversement, à toute contribution équivalente non définitivement liquidée à la date d'entrée en vigueur de la réforme, y compris au titre des années antérieures. Les droits reversés après le calcul donnent lieu à régularisation de la contribution de l'année concernée, dans les délais de réclamation applicables et sans double déduction. Les contributions définitivement liquidées et les recours correspondants demeurent régis par les dispositions qui leur étaient applicables.

*Justification* : rendre la suppression effective dans les textes d'exécution, conserver toutes les exemptions et plafonds pour le stock, et donner un effet réel à la faveur proposée. *Dépendances* : R652-30, R652-33, R652-34 (réécrits, non relus en entier ici) ; dossier XCUT pour les versions futures.

### 5.3 Financement des régimes autonomes (RT-06)

**L652-6 proposé** : ajouter un dernier alinéa :
> La suppression prévue aux deux premiers alinéas prend effet au 1er janvier de l'année suivant l'entrée en vigueur d'une loi de financement de la sécurité sociale qui identifie, pour le régime d'assurance vieillesse de base de la Caisse nationale des barreaux français, une ressource compensant la perte de recettes correspondante. Les pensions liquidées et les droits constitués au titre des périodes antérieures ne peuvent être réduits, ni les cotisations prévues à l'article L. 652-7 relevées, du fait de cette suppression ; la limitation de la garantie des prestations aux ressources affectées prévue par voie réglementaire ne leur est pas opposable à raison de cette suppression.

Dans ce cas, remplacer « à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant son abrogation » par « à compter de la date prévue au dernier alinéa » dans le premier alinéa, et coordonner L652-7 et les dates de 5.2.

**L645-3 proposé** : alinéa analogue pour les régimes de prestations complémentaires de vieillesse de L645-1, avec la participation des caisses d'assurance maladie de L162-14-1 5° inchangée.

**R652-36, quatrième alinéa, et D645-5 proposé** : ajouter :
> Cette limitation ne peut être opposée aux pensions liquidées et aux droits constitués à raison de la suppression des ressources prévues à l'article L. 652-6 [à l'article L. 645-3].

*Justification* : conserver la suppression et la non-hausse des cotisations, tout en appliquant aux droits acquis la règle que le projet retient déjà pour la C3S et pour la capitalisation. *Autre option* : compensation intégrale par l'État selon le principe de L131-7. *Dépendances* : LFSS, statuts de la CNBF, D645-1 et suivants, compensation démographique.

### 5.4 Suffixe générique (RT-08)

**R163-7 proposé, II 1°** :
> 1° Abrogé pour les décisions de radiation prises à compter de l'entrée en vigueur de la loi abrogeant l'article L. 162-17-1, y compris dans les procédures en cours. Aucune spécialité ne peut être radiée au seul motif que sa dénomination de fantaisie n'est pas complétée par un suffixe. Les radiations prononcées auparavant et les recours correspondants demeurent régis par les règles antérieures ;

**R163-2 proposé, II** :
> II. – Lorsqu'a été notifiée, conformément aux dispositions du code de la santé publique relatives à l'identification des spécialités génériques, la décision du directeur général de l'Agence nationale de sécurité du médicament et des produits de santé identifiant un médicament comme spécialité générique, l'arrêté d'inscription de ce médicament sur les listes prévues au premier alinéa de l'article L. 162-17 du présent code et à l'article L. 5123-2 du code de la santé publique mentionne sa dénomination. À compter de l'entrée en vigueur de la loi abrogeant l'article L. 162-17-1, aucun suffixe ne peut être exigé sur le fondement du présent article, ni dans l'arrêté d'inscription, ni dans l'étiquetage, la notice, le résumé des caractéristiques du produit ou la publicité, sans préjudice des obligations d'identification et d'étiquetage prévues par le code de la santé publique et le droit de l'Union. Les inscriptions et mentions antérieures demeurent valables.

*Dépendances* : arrêté fixant le suffixe ; code de la santé publique (non lu).

### 5.5 Prime à la naissance (RT-09)

**D532-2 proposé**, dernière phrase :
> Cette abrogation ne supprime pas les examens médicaux obligatoires prévus par le code de la santé publique. Conformément à l'article L. 533-1, le versement de la prime à la naissance ne peut être subordonné à la réalisation de ces examens.

**D532-1 proposé**, deuxième alinéa :
> La déclaration de grossesse est attestée par un document médical constatant la grossesse. Le document constatant la passation du premier examen prénatal, établi le cas échéant sur le formulaire homologué du ministre chargé de la sécurité sociale, en tient lieu ; tout autre document médical établissant le même fait est recevable. Pour l'attribution de la prime à la naissance, la réalisation de cet examen ne peut être exigée. Aucun examen ni certificat médical supplémentaire n'est exigé du seul fait du dépôt unique.

*Préserver* : dépôt unique opposable aux deux organismes, quatorze semaines, D545-8 6°.

### 5.6 Forfait journalier (RT-01)

**R821-8, I, a)** :
> a) Lorsque l'allocataire est astreint au paiement du forfait journalier prévu à l'article L. 174-4 ou, pour les journées postérieures à la suppression de ce forfait, lorsqu'il se trouve dans une situation dans laquelle il y aurait été astreint selon les règles en vigueur immédiatement avant celle-ci ;

**L871-1 al. 3, L911-7 II 2°, R871-2 6°, L162-22-11-1 b), D174-1, D325-1, D325-6, R381-80, R381-83** : ajouter après la mention du forfait « , pour les seules journées antérieures à sa suppression ». Exemple pour L911-7 : « 2° Le forfait journalier prévu à l'article L. 174-4, pour les seules journées antérieures à sa suppression ; ».

### 5.7 Renvois répressifs (RT-03, RT-07)

- R382-84, premier alinéa : supprimer « , sous les sanctions prévues aux articles R. 244-4 et R. 244-5, ».
- R243-44 : « Les dispositions des articles R. 155-4, R. 133-3 et R. 244-7 s'appliquent au recouvrement des cotisations mentionnées au premier alinéa de l'article L. 243-2. »
- R644-2 : retirer « R. 244-4 et R. 244-5 » ; ajouter « Ce renvoi ne rétablit aucune des contraventions ni des peines supprimées par l'abrogation des articles L. 244-5 et R. 244-4 à R. 244-6. »
- L922-8 : « Les dispositions des I à VI de l'article L. 931-7-2, et les dispositions des articles L. 931-14, L. 931-25 et L. 931-27 s'appliquent aux institutions de retraite complémentaire et à leurs fédérations. »
- L612-2, quatrième alinéa : retirer « L. 272-2, » ; coordonner aussi L641-1 et L766-11 (non lus).

### 5.8 D545-8 (RT-10)

> 5° Pour les étrangers non ressortissants d'un État membre de l'Union européenne, d'un autre État partie à l'accord sur l'Espace économique européen ou de la Confédération suisse, l'un des titres ou documents mentionnés à l'article D. 512-1 ; aucun document relatif à l'entrée ou au séjour de l'enfant n'est exigé pour les allocations dues à compter de l'entrée en vigueur de l'abrogation de l'article D. 512-2 ;

## 6. Simples alertes sans objection

- **R147-15 II 2°** (C13) : la suspension de « la participation … prévue … à l'article L. 645-3 » devient sans objet pour les périodes nouvelles. Retrait rédactionnel suggéré : « … telle que prévue au 5° du I de l'article L. 162-14-1 et, pour les périodes antérieures à sa suppression, à l'article L. 645-3 … ».
- **L162-5 26°** (C22) : « dans le respect des dispositions des articles L. 162-1-9 et L. 162-1-9-1 » ; retirer « L. 162-1-9 et ».
- Remarque de légistique non comptée : D162-29 proposé (« Le renvoi au délai de six mois … est supprimé ») est rédigé comme une instruction d'amendement dans un texte consolidé.

## 7. Incertitudes et éléments non examinés

- **Non lus** : code pénal (111-3, 112-1, 112-4), code de la santé publique (L2122-1, R5121-1 et suivants, L5123-2), décret n° 2025-1286, ordonnance n° 2025-1091, arrêtés (suffixe, audiences, modèles), CASF, code des pensions militaires, CIBS et directive 2001/83/CE. R165-1, R652-30, R652-33, R652-34, L641-1, L766-11, D512-1 et D645-1 et suivants n'ont pas été lus en entier.
- **Données financières** : réserves de la CNBF et de l'ASV, part réelle des recettes supprimées, effet de la compensation démographique. RT-06 repose sur la structure des textes, non sur un chiffrage.
- **Légistique** : le projet abroge souvent un article tout en y maintenant des clauses durables (garanties, fictions, neutralisations). La survie de ces clauses doit être validée par un juriste ; elle conditionne l'appréciation P2 de RT-01.
- **Provisoire** : la plupart des articles qui renvoient sont « pending » en seconde passe. Une proposition modifiée invalide la qualification correspondante, et les empreintes de référence figurent dans le JSON.
- **Doublons inter-paquets** : RT-03 recoupe le cluster R244-4 du paquet P1-CSS-A ; la version 2029 de R652-26 relève aussi de RT-XCUT-01. Les clusters C17, C21 et C27 sont laissés aux dossiers UNION et des douze coordinations.

## 8. Périmètre réellement lu (versions et empreintes, 12 premiers caractères)

Tous les articles ci-dessous ont été exportés et lus en entier par `tools/cite.py` (source, NOTA, proposition, motif et notes) ; les fichiers sont sous `evidence/cited/20261026T230545Z/`. Pour D532-1, toutes les versions historiques ont aussi été exportées.

| Rôle | Article | Version | Bornes (état) | Statut / inventaire | Source sha256 | Proposition sha256 |
|---|---|---|---|---|---|---|
| C00 cible | css L174-4 | LEGIARTI000053713364 | 2017-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | fdf455f6a2ec | 5878b4aa5260 |
| C00 renvoi | css D174-1 | LEGIARTI000006735547 | 1985-12-21 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 8cd820caf604 | — |
| C00 renvoi | css L174-15-3 | LEGIARTI000006741473 | 2006-12-22 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | d888415c6e5f | fca3867bd42a |
| C00 renvoi | css L911-7 | LEGIARTI000031686110 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 292fd263f6d6 | 9e5d98ec0300 |
| C00 renvoi | css D325-6 | LEGIARTI000031813511 | 2016-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 9cd5f18fa014 | — |
| C00 renvoi | css D325-1 | LEGIARTI000031813576 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | ed47f5055bf1 | 75707d7d57af |
| C00 renvoi | css R821-8 | LEGIARTI000031828843 | 2016-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 5c29c91cae39 | — |
| C00 renvoi | css R381-80 | LEGIARTI000034623318 | 2017-05-06 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 50871ef2d532 | — |
| C00 renvoi | css R381-83 | LEGIARTI000034623350 | 2017-05-06 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 8379405e4e6a | — |
| C00 renvoi | css L162-22-11-1 | LEGIARTI000048702188 | 2024-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / completed | fde9db3271bf | — |
| C00 renvoi | css L871-1 | LEGIARTI000051382496 | 2025-02-28 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | b7328c361a61 | 63a2c03dff13 |
| C00 renvoi | css R871-2 | LEGIARTI000052861614 | 2025-11-28 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 83ce9c3061b3 | — |
| C00 renvoi | css L162-31-1 | LEGIARTI000054715108 | 2026-08-20 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | cd1d73bb4f28 | 7fccf5934ea0 |
| C01 cible | css L162-1-7-1 | LEGIARTI000051287773 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 006a0f6b7f8b | 0981ca19335b |
| C01 renvoi | css D162-29 | LEGIARTI000030261705 | 2015-02-21 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 30d3e8cdd0c0 | 84aab4838442 |
| C01 renvoi | css R165-93 | LEGIARTI000053185269 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 8fa19aca8719 | — |
| C01 renvoi | css R163-51 | LEGIARTI000053185275 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 68879e20e433 | — |
| C01 renvoi | css R162-116 | LEGIARTI000053185289 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | b54dddaee1ff | — |
| C01 renvoi | css R162-73 | LEGIARTI000053185293 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | b2d2ed30930d | — |
| C01 renvoi | css R162-38 | LEGIARTI000053185301 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 2e68ca7867ab | — |
| C01 renvoi | css R162-37-2 | LEGIARTI000053185307 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 243b72d55d7f | — |
| C01 renvoi | css R162-34-13 | LEGIARTI000053185316 | 2026-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 5d9ee1818fcb | — |
| C01 renvoi | css R161-45 | LEGIARTI000053185324 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 16029ebe12b9 | 28b6f29780b9 |
| C01 renvoi | css R163-2 | LEGIARTI000053212995 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 63e04ea84e04 | 2d7f333942de |
| C01 renvoi | css R163-32 | LEGIARTI000054206153 | 2026-09-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | d56e8b57fbd2 | — |
| C02 cible | css L138-19-8 | LEGIARTI000053282743 | 2025-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 3b21791e13cd | b8e9b01b4539 |
| C02 renvoi | css D138-3 | LEGIARTI000043085614 | 2021-02-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | c92ee8a1c1af | — |
| C02 renvoi | css D138-4 | LEGIARTI000051257538 | 2025-02-28 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | b5ddeeaccdbf | — |
| C03 cible | css L245-7 | LEGIARTI000048834648 | 2023-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 02e852588a8e | c77f8b8d211e |
| C03 renvoi | a3 406 terdecies | LEGIARTI000052589631 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 4a3080451c7a | c47d15242be2 |
| C03 renvoi | a4 54-0 BV | LEGIARTI000006300731 | 2001-03-31 → 2999-01-01 (VIGUEUR) | retained_unchanged / completed | ecf431a36ac1 | — |
| C03 renvoi | cgi 238 bis GA | LEGIARTI000006309120 | 2006-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | c53ddabcceba | cf4669a723ef |
| C03 renvoi | css D245-14 | LEGIARTI000006735929 | 1985-12-21 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 0b201afabe44 | f4a9f34eb48a |
| C03 renvoi | css L245-9-1 | LEGIARTI000048795876 | 2023-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | c661b4780e25 | e3556db3e11d |
| C04 cible | css R244-5 | LEGIARTI000006749090 | 2000-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f94aaa0f5ddb | dec15ec2ca6e |
| C04 renvoi | css L244-4 | LEGIARTI000006742089 | 1989-07-12 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 0d9cf8b7a2cc | 80c36a8f7d19 |
| C04 renvoi | css L244-1 | LEGIARTI000029961352 | 2015-01-01 → 2029-01-01 (ABROGE_DIFF) | rewrite_draft / completed | 65aa257c3c56 | 47692bafbcd1 |
| C04 renvoi | css R382-84 | LEGIARTI000034623071 | 2017-05-06 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f0a0b56dfa87 | 12899aae5341 |
| C04 renvoi | css R243-44 | LEGIARTI000035656864 | 2017-09-28 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | ff73bfad1136 | — |
| C04 renvoi | css R644-2 | LEGIARTI000047265913 | 2023-03-05 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 2767214048ff | — |
| C05 cible | css L245-5-1 | LEGIARTI000037064538 | 2018-06-14 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 2555942229df | ee6872a064df |
| C05 renvoi | css R245-16-2 | LEGIARTI000019268747 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 2d07af9fa325 | 72f19875d48f |
| C05 renvoi | css R245-16-1 | LEGIARTI000019268750 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 48775e173e4b | 9ce119f31b09 |
| C05 renvoi | css R138-19 | LEGIARTI000042389712 | 2021-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 80c84d1ffdc9 | 8ff72d7a2ed8 |
| C05 renvoi | css L241-2 | LEGIARTI000046805562 | 2023-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 46b15148ce05 | 162d36fc6e65 |
| C05 renvoi | css L138-20 | LEGIARTI000051287267 | 2025-02-28 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 0e7c04d168b1 | b09c0e0362b8 |
| C06 cible | css L862-4-1 | LEGIARTI000037853668 | 2019-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 93a8c1a2ee4c | cc70034a7d72 |
| C06 renvoi | css R862-13-1 | LEGIARTI000038701715 | 2019-11-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f0168e305c8b | 07154e5ee2c0 |
| C06 renvoi | css R862-11-3 | LEGIARTI000039222837 | 2020-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 2f0f4fbd680c | 2c7cf5bbbe82 |
| C06 renvoi | css L241-2 | LEGIARTI000046805562 | 2023-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 46b15148ce05 | 162d36fc6e65 |
| C06 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C07 cible | css R613-10 | LEGIARTI000038786719 | 2019-07-08 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 28b6bdc18e0e | 215f6492ad62 |
| C07 renvoi | a3 41 DG ter | LEGIARTI000042161110 | 2020-07-25 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 18f486e51ba1 | a10bc26412a7 |
| C07 renvoi | css R133-9 | LEGIARTI000038790623 | 2019-07-08 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 00b6fc079313 | 9c23899c57f7 |
| C07 renvoi | css R243-19 | LEGIARTI000047480864 | 2023-04-23 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 6ad1b4436479 | 149a78f91770 |
| C08 cible | css L137-27 | LEGIARTI000053269267 | 2025-12-31 → 2027-01-01 (ABROGE_DIFF) | rewrite_draft / completed | 33f54df5eb29 | 2878285e73e3 |
| C08 renvoi | cgi 302 bis ZH | LEGIARTI000038589476 | 2020-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 75559df428a9 | 6ea70f38a1f7 |
| C08 renvoi | cgi 302 bis ZI | LEGIARTI000054373381 | 2026-07-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 2f25359d98e6 | 3b14789f3ba6 |
| C08 renvoi | cgi 302 bis ZG | LEGIARTI000054373392 | 2026-07-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | d88e6a594927 | 49460405986b |
| C09 cible | css L374-1 | LEGIARTI000046042840 | 2021-05-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 0a5409c49802 | 2289869c1a01 |
| C09 renvoi | css D374-2 | LEGIARTI000006736618 | 1985-12-21 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 7c655aa51902 | 5b9851e936eb |
| C09 renvoi | css D374-6 | LEGIARTI000031813542 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | e149453f322d | 3b94f8ed8af5 |
| C09 renvoi | css L243-2 | LEGIARTI000033713045 | 2017-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | cd704cb17779 | 162654853525 |
| C10 cible | css R135-26 | LEGIARTI000006747058 | 2005-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 5ffe07d50525 | e5def3df452f |
| C10 renvoi | css R135-20 | LEGIARTI000006747048 | 2002-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 08e5056b6ffd | e24dae3ad871 |
| C10 renvoi | css R135-24 | LEGIARTI000021311808 | 2009-11-23 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 1acb44bd8ffa | 53d672afae8a |
| C10 renvoi | css R135-22 | LEGIARTI000021311813 | 2009-11-23 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | eb18f5ba1565 | bfd8a9d52264 |
| C11 cible | css L245-5-3 | LEGIARTI000021535696 | 2009-12-28 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 8af3e398b0c6 | a47629931008 |
| C11 renvoi | css R245-16-2 | LEGIARTI000019268747 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 2d07af9fa325 | 72f19875d48f |
| C11 renvoi | css R245-16-1 | LEGIARTI000019268750 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 48775e173e4b | 9ce119f31b09 |
| C12 cible | css L652-6 | LEGIARTI000037063237 | 2018-06-14 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | c21bad466436 | ba75a173730a |
| C12 renvoi | css R652-31 | LEGIARTI000038770185 | 2019-07-08 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | ccb53dbe54c0 | 66ed50e72556 |
| C12 renvoi | css R652-26 | LEGIARTI000039348152 | 2020-01-01 → 2029-01-01 (ABROGE_DIFF) | retained_unchanged / pending | b9d602505a91 | — |
| C12 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C13 cible | css L645-3 | LEGIARTI000037062633 | 2018-06-14 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 0f570f0c65d3 | 26c7940c0252 |
| C13 renvoi | css R147-15 | LEGIARTI000042395558 | 2020-10-05 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f921db95b654 | 15ea8030b2c2 |
| C13 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C14 cible | css L137-10 | LEGIARTI000037074877 | 2018-09-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | da83f26e4f58 | 13bb6e7df77e |
| C14 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C14 renvoi | css L241-3 | LEGIARTI000051289018 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | f24a47a71834 | da4cf027a0b1 |
| C15 cible | css L137-14 | LEGIARTI000053278796 | 2025-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 6a8b7011f859 | 7caf507cff08 |
| C15 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C15 renvoi | css L131-8 | LEGIARTI000053538201 | 2026-02-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 256ecfafae93 | c6eaebb3e36e |
| C16 cible | css R613-9 | LEGIARTI000038786725 | 2019-07-08 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | c0772c8145b6 | bee77bd89d56 |
| C16 renvoi | a3 41 DG ter | LEGIARTI000042161110 | 2020-07-25 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 18f486e51ba1 | a10bc26412a7 |
| C16 renvoi | css R243-19 | LEGIARTI000047480864 | 2023-04-23 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 6ad1b4436479 | 149a78f91770 |
| C17 cible | css L281-4 | LEGIARTI000025516592 | 2012-04-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | dacfcd644816 | 905caaf2e2ae |
| C17 renvoi | css R213-5 | LEGIARTI000006748552 | 1985-12-21 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | e2a74e69b942 | — |
| C17 renvoi | css R281-4 | LEGIARTI000036914411 | 2018-05-17 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 8553eeea4caa | — |
| C18 cible | css R532-8 | LEGIARTI000031694502 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 817f374d2454 | 5b8118a8dfa9 |
| C18 renvoi | css R553-3-5 | LEGIARTI000018052222 | 2008-01-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | c3ffeefd51ad | cdc285037deb |
| C18 renvoi | css R543-6 | LEGIARTI000045087752 | 2022-01-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 742de721efdb | 1b144f4cb35c |
| C19 cible | css L245-5-5 | LEGIARTI000053282639 | 2025-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 8fb965d7371e | ac273c9d2f83 |
| C19 renvoi | css R245-16-2 | LEGIARTI000019268747 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 2d07af9fa325 | 72f19875d48f |
| C19 renvoi | css R245-16-1 | LEGIARTI000019268750 | 2008-07-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 48775e173e4b | 9ce119f31b09 |
| C20 cible | css L931-26 | LEGIARTI000006745649 | 2006-06-24 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | c43b69228634 | e3731e5eecd1 |
| C20 renvoi | css L922-8 | LEGIARTI000030438909 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 8082a8da8c50 | 08d489a759c7 |
| C20 renvoi | css L941-3 | LEGIARTI000034387804 | 2017-04-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 6c617d0052e7 | — |
| C21 cible | css R152-8 | LEGIARTI000029388285 | 2014-08-23 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | c7386149755c | a705be7aae93 |
| C21 renvoi | css R123-1-1 | LEGIARTI000038790652 | 2020-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 76307c327880 | a416732f1d3a |
| C22 cible | css L162-1-9 | LEGIARTI000033715680 | 2016-12-25 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | c915c7ecb0dd | cf63112946df |
| C22 renvoi | css L162-1-9-1 | LEGIARTI000046812368 | 2022-12-25 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 1e11ccbb77d7 | 9a500ed3c040 |
| C22 renvoi | css L162-5 | LEGIARTI000051140851 | 2025-02-07 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 7bd63d10e259 | 14de1b749e6b |
| C23 cible | css L137-13 | LEGIARTI000051284578 | 2025-03-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | ab9bbbbaff33 | 4db99a9ac7ac |
| C23 renvoi | css L213-1 | LEGIARTI000048701101 | 2024-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e0fa98952d5e | 02fb8d4fd4e8 |
| C24 cible | css L162-17-1 | LEGIARTI000054226721 | 2000-06-22 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 30e91dae5d56 | 353693df0cd6 |
| C24 renvoi | css R163-7 | LEGIARTI000049737659 | 2024-06-19 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 681e92052c89 | 161565d5f18d |
| C24 renvoi | css R163-2 | LEGIARTI000053212995 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 63e04ea84e04 | 2d7f333942de |
| C25 cible | css L533-1 | LEGIARTI000017841360 | 2007-12-22 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 10b373c3fe8f | 52678b17e042 |
| C25 renvoi | css D532-2 | LEGIARTI000006737331 | 2004-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 3a5cbe137449 | 0a3cf97ff08e |
| C26 cible | css R815-46 | LEGIARTI000026854678 | 2013-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | dd6c72929bc4 | db5beffc2543 |
| C26 renvoi | css R815-48 | LEGIARTI000006753886 | 2007-01-13 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 3ebe10b15bdb | 4bf893304611 |
| C27 cible | css L153-6 | LEGIARTI000006740522 | 1994-07-27 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 86cd52e54d68 | 65268033cebe |
| C27 renvoi | css R153-2 | LEGIARTI000022055116 | 2010-04-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 3ce07f027d7e | — |
| C28 cible | css R931-3-16 | LEGIARTI000045387189 | 2022-03-20 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | cc051f670783 | 32e36ca371f4 |
| C28 renvoi | css R931-1-28 | LEGIARTI000030575584 | 2015-05-11 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | fbffed9f9705 | 1d94b8babbce |
| C29 cible | css A931-3-3 | LEGIARTI000006734960 | 2000-05-04 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | d344ab2f6b1b | 2e352c560c05 |
| C29 renvoi | css A931-1-10 | LEGIARTI000031042065 | 2015-08-15 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | bd5e2529b6cf | b1d1eb829da2 |
| C30 cible | css D848-3 | LEGIARTI000031674595 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 6ea722cf3509 | ff9cd673d0fb |
| C30 renvoi | css D848-5 | LEGIARTI000031674673 | 2016-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 829a3009b95a | 11b982a669ad |
| C31 cible | css L272-2 | LEGIARTI000006742219 | 2002-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | d1262aad196b | e7f993206bb4 |
| C31 renvoi | css L612-2 | LEGIARTI000036391005 | 2019-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 172168b27262 | bdcaa37fa907 |
| C32 cible | css R862-11-5 | LEGIARTI000032156086 | 2016-03-07 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 52c10cd44730 | cc94dc79a0e5 |
| C32 renvoi | css R862-13-1 | LEGIARTI000038701715 | 2019-11-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f0168e305c8b | 07154e5ee2c0 |
| C33 cible | css R382-86 | LEGIARTI000006749792 | 2006-11-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 4ae7f141a950 | 6ad3c60eff9c |
| C33 renvoi | css D758-3 | LEGIARTI000041968156 | 2020-05-25 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | ba69e65647b4 | — |
| C34 cible | css R815-40 | LEGIARTI000006753820 | 2007-01-13 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | 72f06257edd1 | 52dab0409fd7 |
| C34 renvoi | css R815-61 | LEGIARTI000042964341 | 2021-01-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 5c56631cb88a | — |
| C35 cible | css D512-2 | LEGIARTI000042947066 | 2021-05-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | dcf11c4f642a | beee1db4bfb7 |
| C35 renvoi | css D545-8 | LEGIARTI000045283844 | 2022-03-01 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | c5074e270808 | — |
| C36 cible | css L244-5 | LEGIARTI000006742091 | 1988-01-06 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | eff2982d1ef4 | ee103c15a27d |
| C36 renvoi | css R644-2 | LEGIARTI000047265913 | 2023-03-05 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 2767214048ff | — |
| C37 cible | css L382-9 | LEGIARTI000036392686 | 2019-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | f65a468d76dd | 0303c3258d40 |
| C37 renvoi | css L382-14 | LEGIARTI000053282119 | 2025-12-31 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 12df2791c56a | 99d336b4b01d |
| C38 cible | css L162-30 | LEGIARTI000006741387 | 2005-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | e557ada286f2 | 3857a03b85b8 |
| C38 renvoi | css R162-35-7 | LEGIARTI000054129381 | 2026-05-24 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 4f1a6e61cfec | — |
| complément | css R652-26 | LEGIARTI000052846149 | 2029-01-01 → 2999-01-01 (VIGUEUR_DIFF) | — / not_in_inventory | feee76d7766a | — |
| complément | css R652-27 | LEGIARTI000038770173 | 2019-07-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 1909750ddb2b | — |
| complément | css R652-28 | LEGIARTI000038770176 | 2019-07-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | e65bb2f4aaa3 | — |
| complément | css R652-29 | LEGIARTI000038770179 | 2019-07-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 991af5bb3b72 | — |
| complément | css R652-32 | LEGIARTI000038770188 | 2019-07-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | d6a9fd0a5e8f | — |
| complément | css R652-35 | LEGIARTI000042633643 | 2020-12-10 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | da0e3a54cace | — |
| complément | css R652-36 | LEGIARTI000038770219 | 2019-07-08 → 2999-01-01 (VIGUEUR) | retained_unchanged / pending | 1a344ec4d151 | — |
| complément | css L652-7 | LEGIARTI000051288997 | 2026-01-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | 4b6c3a29b144 | 7fb5807d0338 |
| complément | css D645-5 | LEGIARTI000006738172 | 1985-12-21 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | fba95355d108 | 004d4385cfbc |
| complément | css D532-1 | LEGIARTI000047012803 | 2023-01-04 → 2999-01-01 (VIGUEUR) | rewrite_draft / pending | f283c647a4ac | 8cb198d93905 |
| complément | css L512-2 | LEGIARTI000042920150 | 2021-05-01 → 2999-01-01 (VIGUEUR) | rewrite_draft / completed | df8f2c9a1fd5 | 9e6b8575dc6f |
