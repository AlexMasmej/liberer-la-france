# Dossier RESINT : réserves documentaires et suivi des corrections intégrées

Troisième passe, red-team IA indépendante. Rapport établi le 26 octobre 2026 sur l'instantané `snapshots/20261026T230545Z`. Corpus daté du 18 octobre 2026.

Ce rapport n'est pas une validation par un juriste. La seconde passe continue en production : 11 052 articles relus, 19 262 restants. Toutes les conclusions ci-dessous sont provisoires et valent pour les empreintes citées.

Préfixes : `RT-DOC-xx` pour les réserves documentaires (partie a), `RT-INTEG-xx` pour les corrections intégrées (partie b).

---

## 1. Périmètre réellement lu

Tous les articles ont été lus avec `tools/cite.py`, en entier pour les versions citées : source, NOTA, bornes, proposition, motif, notes, lot propriétaire et inventaire. Les sauvegardes sont dans `evidence/cited/20261026T230545Z/`.

### Partie a : réserves documentaires

| Code | Numéro | Version | Bornes | État d'inventaire |
|---|---|---|---|---|
| css | Annexe I à l'art. R434-32 (7) | LEGIARTI000028675462 | 2006-02-06 → 2999 | documentary_hold_unverified, pas de proposition |
| css | Annexe I à l'art. R434-35 (7) (version antérieure) | LEGIARTI000019323362 | 1985-12-21 → 2006-02-06 | historique ; texte identique, même lacune |
| css | Annexe I à l'art. R434-32 (1) (chapitre préliminaire) | LEGIARTI000028674637 | 2006 → 2999 | pending, rewrite_draft |
| css | R434-32, toutes versions | …22073148 (→ 2026-11-01), …54060111 (VIGUEUR_DIFF à partir du 2026-11-01) | | pending / sans proposition |
| css | L434-1 A (VIGUEUR_DIFF), L434-2 (…47452183 et …51288493), D491-6, R351-24-1, D434-4/5 | | | lus pour les renvois au barème |
| a4 | 15 | LEGIARTI000019493914 | 2008-09-18 → 2999 | documentary_hold_unverified, pas de proposition |
| a4 | 13, 14, 16 (versions en vigueur et historiques) | …006300256, …027511568, …027511564 | | completed |
| a2 | 57 | LEGIARTI000025622239 | 2012 → 2999 | completed, rewrite_draft |
| cgi | 158 | LEGIARTI000054373673 | 2026-07-01 → 2999 | completed ; cible de référence de la réserve a4 15 |
| — | `source-image-gaps.json` (18 entrées), `extended-graphic-gaps.json` (9), les 16 manifestes de `attachments/records/`, l'entrée `documentary_holds` de `runtime/radical-review-20261019.json`, `notes-contradictions/INDEX.md` | | | |

Pour les autres pièces signalées dans les fichiers de lacunes (D832-11, D832-25, annexe R172-4, 49 septies ZZB bis/ZZH, A123-1, D643-7, D653-4, D912-15, R254-5, D453-7, annexes I/II et R4453-3/4 du code du travail), seuls les **manifestes** ont été lus, avec l'état et les empreintes de leurs propositions. Leurs tableaux et formules n'ont pas été relus. **CSS D351-9 est exclu** : le coordinateur le traite.

### Partie b : corrections intégrées

- Neuf corrections, preuve scellée `evidence/sealed/runtime/coherence-nine-activation-20261024T0553Z/` : `run/REPORT.md`, `run/RESOLUTION.json`, `run/worklist-published.json`, `run/current-nine-whole-source-before-after-verification.json` (images avant/après entières, cinq champs) et `REVIEW.md`.
- Deux corrections TSCA, preuve scellée `evidence/sealed/runtime/tsca-two-activation-20261024T1222Z/` : `run/REPORT.md`, `run/RESOLUTION.json`, `run/worklist-published.json`, `run/registration/{0,1}.{before,after}`, `registered.json` et `REVIEW.md`.
- Contreparties relues dans l'instantané : CGI 234 nonies ; travail L2411-1, L2371-5 et L2421-3 ; CCH L423-1-2, D423-1-1 et D423-1-2 ; urbanisme R121-22, L121-32 et L121-34 ; CGI 991 et ses versions ; annexe III 385 ; toutes les versions de CGI 1649 quater B quater.

## 2. Méthode

1. Pour chaque réserve : identifier la pièce absente dans le XML LEGI, son contexte normatif, sa source officielle probable, ce que contient déjà `attachments/` et l'effet de l'absence. On distingue deux effets : une conclusion juridique bloquée, ou seulement une complétude documentaire incomplète. On a aussi lu les articles qui renvoient à la pièce, avec leurs propositions.
2. Pour chaque correction intégrée :
   - extraire l'image après intégration des preuves scellées ;
   - recalculer SHA-256(proposed_xml / reason / review_notes) selon la convention de `tools/corpus.py` ;
   - comparer avec la base de l'instantané et avec le lot propriétaire ;
   - produire un diff textuel avant → intégré (la correction elle-même) et intégré → courant (l'évolution depuis).
3. Relire les contreparties que chaque correction devait coordonner.
4. Rien n'a été réintégré. Aucun fichier de production, de l'instantané ou des preuves scellées n'a été modifié.

### Accès publics tentés (horodatés, aucun contournement)

| Heure UTC (26/10/2026) | URL | Résultat |
|---|---|---|
| 23:21:55 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028675462 | HTTP 403, contenu non obtenu |
| 23:22 | Recherche web : phrase exacte « quadranopsies peuvent être évaluées en assignant à chaque quadrant une valeur » | Aucune reproduction du cliché trouvée |
| 23:22 | Recherche web : barème AT, ophtalmologie, quadranopsie (ameli) | Aucune source exploitable ; seuls des barèmes étrangers, non transposables |
| 23:22 | Recherche web : « 30-0812 » / « 30-0813 » cerfa | Aucun résultat pertinent |
| 23:22 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019491882 (arrêté du 15 septembre 2008) | HTTP 403 |
| 23:22:35 | https://www.service-public.gouv.fr/particuliers/recherche?keyword=30-0812 | « Aucun résultat », pas de CAPTCHA |

Aucune de ces consultations ne porte sur une consolidation postérieure au 18 octobre 2026.

---

## 3. Constats, partie a : réserves documentaires

### RT-DOC-01 (P2, réserve documentaire, confirmé) : cliché absent de l'annexe I à R434-32 (7), ophtalmologie

**Pièce manquante.** Au 6.1.6 c) « Hémianopsie » du barème indicatif d'invalidité AT, le texte LEGI porte : « Les quadranopsies peuvent être évaluées en assignant à chaque quadrant une valeur de : » suivi de « [cliché non reproduit] ». La pièce absente est donc la figure qui attribue une valeur à chaque quadrant du champ visuel. Aucune valeur numérique n'est restituée dans le texte, et la phrase qui suit (« Scotomes paracentraux hémianopsiques ») commence immédiatement après.

**Historique.** La version de 1985 (LEGIARTI000019323362, num « Annexe I à l'art. R434-35 (7) », début 1985-12-21) a un texte identique après normalisation : 9 971 caractères, égalité vérifiée. La même lacune existe donc depuis l'entrée dans LEGI. La version de 2006 n'a été créée que par la renumérotation R434-35 → R434-32 (décret n° 2006-111 du 2 février 2006, JORFTEXT000000261498, lien `MODIFICATION` du XML).

**Source officielle à obtenir.** Le fac-similé JORF de l'annexe I telle que codifiée, date LEGI du 21 décembre 1985, ou du texte d'approbation du barème AT d'origine. **Ni l'identifiant JORF de cette publication, ni celui de l'acte d'origine ne figurent dans l'instantané ; ils restent à établir.** Aucun acte n'est présumé ici. Le 6 février 2006, rien n'a été republié.

**Ce qui existe dans `attachments/`.** Rien : aucun manifeste dans `records/`, aucun média, aucun document. Aucun fichier de l'instantané ne mentionne `28675462`, « cliché » ou « quadranops ».

**Effet sur l'article source.** Le barème est expressément indicatif. Le chapitre préliminaire (LEGIARTI000028674637) dit : « Il ne peut avoir qu'un caractère indicatif […] le médecin chargé de l'évaluation garde […] l'entière liberté de s'écarter des chiffres du barème ; il doit alors exposer clairement les raisons ». La phrase manquante est elle-même facultative (« peuvent être évaluées »). Les autres taux d'hémianopsie (homonyme 30 à 35, horizontale inférieure 30 à 50, etc.) et le tableau général d'évaluation sont complets. L'absence **ne bloque donc aucune conclusion juridique** sur la détermination du taux, qui reste possible et motivable. Elle bloque seulement :
- la complétude documentaire ;
- la vérification d'une valeur de référence précise pour les quadranopsies ;
- toute proposition qui se dirait « intégrale » pour ce chapitre.

**Effet sur les articles qui renvoient au barème.**
- R434-32, version en vigueur au 18 octobre (LEGIARTI000022073148) : annexe les barèmes au livre IV. La proposition `e7811f74…` conserve l'alinéa des barèmes intact et ne touche que l'accès au rapport médical. Elle ne dépend pas du cliché.
- L434-2 (LEGIARTI000047452183, retained_unchanged) et D491-6 (retained_unchanged) visent « un barème indicatif ». D434-4/5 : comité d'actualisation. Ces articles n'utilisent pas la figure ; aucune proposition n'en dépend.
- Chapitre préliminaire (1), proposition `3edda22a…` : coordination ciblée (travail aménagé, délais de révision), sans lien avec la figure.

**Point de transition, à signaler sans en faire une contradiction.** À compter du 1er novembre 2026, deux textes changent :
- L434-1 A (VIGUEUR_DIFF, LEGIARTI000051288442) prévoit des barèmes indicatifs d'incapacité professionnelle et fonctionnelle « déterminé par arrêté des ministres chargés du travail et de la santé », applicables « aux victimes dont l'état est consolidé à compter de cette date » (NOTA, art. 90 V de la loi n° 2025-199 dans sa rédaction issue de l'art. 95 de la loi n° 2025-1403).
- La version de R434-32 en vigueur à cette date (LEGIARTI000054060111, VIGUEUR_DIFF, sans proposition) ne comporte plus l'alinéa « Les barèmes indicatifs […] sont annexés au présent livre ».

L'annexe I reste formellement en vigueur (fin 2999-01-01). Elle continuera de régir au moins les consolidations antérieures. La figure manquante garde donc un intérêt pour les droits acquis et les révisions. Ces deux versions sont postérieures au 18 octobre ; elles figurent dans le corpus comme versions différées.

**Conclusion.** Il s'agit d'une réserve de complétude, non d'une contradiction. La seconde passe ne doit ni inventer de valeurs, ni substituer un barème étranger (anciens combattants canadiens, Québec, etc.), ni s'appuyer sur le guide-barème des pensions militaires. Ces sources ne sont pas l'annexe I.

### RT-DOC-02 (P2, réserve documentaire, confirmé) : modèles CERFA 30-0812 et 30-0813 de l'annexe IV, art. 15

**Pièce manquante.** Le 1° dispose : « Les relevés sont établis sous forme de fiches individuelles conformes aux modèles ci-après (non reproduits-Cerfa n° 30-0812 et n° 30-0813) ». Ce sont les deux modèles de fiches individuelles de relevés de coupons. Le manifeste `attachments/records/fiscalite-cerfa-15-reserve.json` constate `documentary_recovery_complete: false`, sans aucun média, document ni transcription. Il interdit aussi de substituer les formulaires modernes 2561/2078 sans preuve d'équivalence.

**Source officielle.** La version en vigueur depuis le 18 septembre 2008 résulte de l'arrêté du 15 septembre 2008, art. 1 (JORFTEXT000019491882, NOR BCFL0818512A, lien du XML). Le XML porte déjà « non reproduits ». Le modèle relève des imprimés administratifs CERFA de la DGFiP, et non du texte normatif publié. Aucune source ne l'a fourni au 26 octobre 2026 : Légifrance a répondu 403, service-public.gouv.fr ne donne aucun résultat (voir le tableau d'accès).

**Effet sur l'article source.**
- Le contenu obligatoire des relevés est entièrement écrit dans le texte. Le 2°, de a à f, liste les mentions d'identification ; le 4°, de a à e, liste les montants. Le contenu de l'obligation déclarative est donc déterminable sans les modèles.
- Ce qui reste indéterminé : la présentation imposée, et l'étendue exacte des « renseignements que comportent ces modèles », condition de la faculté de substitution par fiche mécanographique d'au plus 21 × 13 cm. Les modèles pourraient comporter des cases sans équivalent aux 2° et 4°. Rien ne le prouve dans un sens ou dans l'autre.
- L'absence bloque donc une rédaction « à droit constant » complète du 1°. Elle ne bloque pas une conclusion juridique sur l'existence et le contenu de l'obligation.

**Effet sur les articles proposés qui en dépendent.**
- Annexe II, 57, proposition `3ea5b3ad…` : la déclaration de l'article 242 ter « tient lieu du relevé » ; « aucun relevé distinct de coupons n'est exigé » dans le champ de 242 ter. Ses notes demandent que les articles 7 à 17 de l'annexe IV « et leurs formulaires » soient coordonnés « pour ne pas rétablir le circuit supprimé ». Sans proposition, l'article 15 continue de décrire des fiches conformes aux modèles CERFA pour tous les relevés. Juridiquement, le renvoi de l'article 14 à l'article 57 limite déjà le champ des relevés subsistants. Le risque est surtout que les formulaires CERFA, s'ils existent encore, rétablissent un support pour le champ supprimé.
- Annexe IV, 14 (retained_unchanged) et 16 (bordereau supprimé, `484b199c…`) : cohérents avec l'article 57 par renvoi ; 16 ne dépend pas du modèle.
- CGI 158 (LEGIARTI000054373673), seule cible de garde enregistrée pour cette réserve : le 4° a de l'article 15 vise « l'abattement prévu au troisième alinéa du 3 de l'article 158 ». La proposition de 158 garde l'abattement de 40 % au 2° du 3. La correspondance de ce renvoi ancien avec la structure actuelle du 3 de 158 n'est **pas vérifiée**. De même, la mention du « crédit d'impôt attaché » au 4° d, qui paraît historique, n'est pas vérifiée. Ces deux points sont des alertes à examiner lors de la rédaction de l'article 15. Ils ne sont pas établis ici comme des erreurs.

**Proposition de correction** : voir la section 5, P-DOC-02.

### RT-DOC-03 (P2, réserve documentaire, à confirmer) : récupérations documentaires des fichiers de lacunes non confrontées au Journal officiel authentifié

Classement des 18 entrées de `source-image-gaps.json` et des 9 de `extended-graphic-gaps.json`, qui se recoupent. Le classement suit les manifestes de `attachments/records/`, non une relecture des tableaux :

| Classe | Articles | État documentaire | Effet |
|---|---|---|---|
| **A. Ouverte, sans pièce** | css Annexe I R434-32 (7) ; a4 15 ; css D351-9 (exclu, coordinateur) | documentary_hold_unverified, first_pass_open | Complétude bloquée ; voir RT-DOC-01 et 02 |
| **B. Récupérée sur fac-similé officiel du JO** (sans validation cryptographique) | urba A123-1 ; a3 49 septies ZZH ; css D643-7 ; css D653-4 ; cch R254-5 ; cch D453-7 | `official_jo_crosscheck_complete: true`, activation documentaire faite | Réserve résiduelle d'authenticité seulement |
| **C. Récupérée sur une copie publique du JO** (hébergeur tiers, sans signature) | css annexes D912-15 (téléchargement officiel en 403) ; travail R4453-3 et R4453-4 (copie Next INpact ; rectificatif du 8 avril 2017, NOR ETST1611714Z, non récupéré pour R4453-4) | `authenticated_jo_crosscheck_complete: false` | Confrontation au JO authentifié à faire |
| **D. Récupérée sur une source non JO** | cch D832-11 et D832-25 (brochure ministérielle d'avril 2024) ; cch annexe R172-4 (37 renvois, consolidation ministérielle « sans valeur juridique », JO bloqué par Cloudflare) ; a3 49 septies ZZB bis (BOFiP retiré en novembre 2024 ; JO JORFTEXT000038934588 en 403) ; travail annexe I et annexe II (directive 2006/25/CE consolidée en 2014) | Confrontation au JO français restante | Réserve la plus sensible : voir ci-dessous |

Le point qui justifie un suivi concerne **l'annexe II du code du travail** (LEGIARTI000023018851, proposition `8770def1…`, pending). D'après son motif, elle « corrige les corruptions typographiques documentées » du XML français, puisque ses notes listent : mm au lieu de min, une borne, 311 au lieu de 3111, des puissances 10^3, nm au lieu de mn. Ces corrections ont été faites par confrontation à la directive européenne, et non au JO français du 4 juillet 2010, texte 11. Le manifeste reconnaît que cette confrontation reste à faire. Une valeur de seuil de protection est ainsi portée au projet sur la base d'une autre source que le texte national. Ce n'est pas une contradiction établie. Il faut confirmer ces valeurs sur le JO avant toute conclusion d'exactitude.

Le même raisonnement vaut, à moindre degré, pour l'annexe I du travail. Pour D832-11 et D832-25, les montants de l'arrêté n'ont pas été figés, ce qui est correct.

### RT-DOC-04 (P2, réserve documentaire, à confirmer) : actes et modèles extérieurs signalés dans les dossiers lus

Ces pièces, citées par les propositions lues dans ce dossier, sont absentes du corpus autorisé. Elles sont signalées sans être comptées comme des contradictions :
- Codes hors corpus : LPF, code des assurances, code de la mutualité, CMF, conventions fiscales. `outside_corpus_coordination_pending` de l'inventaire en compte cinq. S'y ajoutent le code de commerce (L229-3, L233-3), le CRPA (chapitre de l'enquête publique) et le CMF (L313-13 à L313-16, L511-6), cités par L2411-12, R2372-17, L423-16 et R121-23.
- Articles historiques CGI 1002 et 1003, cités par les articles 388 et 387 de l'annexe III. Ils sont absents du fichier public : notes de CGI 991 et de l'annexe IV 196 A.
- Formulaires d'exécution : 2065/2072 et relevés d'acompte CRL (notes de 234 nonies) ; formulaires TSCA ; CERFA des relevés de coupons (RT-DOC-02).
- Modèles de statuts et acte de 2004 « sélecteur V » de L281-6. Déjà ouvert dans l'index (dossier union-statutes) ; renvoi ici sans double comptage.
- Arrêté ministériel des futurs barèmes AT-MP (L434-1 A), non publié dans le corpus.

---

## 4. Constats, partie b : corrections intégrées

### 4.1 Tableau de vérification

« int. » désigne l'empreinte intégrée le 24 octobre, reconstruite depuis l'image après de la preuve scellée. « cour. » désigne l'empreinte de l'instantané (DB = lot propriétaire). Les empreintes sont tronquées à 12 caractères ; les valeurs complètes sont dans le JSON. La source (`source_sha256`) est inchangée pour les onze articles.

| # | Article (version) | Objet de la correction | proposed int. → cour. | motif / notes | 2e passe | Classement |
|---|---|---|---|---|---|---|
| 1 | a3 38 (LEGIARTI000026348040) | CRL : la rubrique I a ne vise que les recettes perçues avant la suppression de la CRL, « dans les conditions transitoires » de 234 nonies | `407a3dde23…` → `4aaadbaa94…` | réécrits | completed (réécriture native postérieure, avec `prior_proposal_sha256` = int.) | **Modifiée mais compatible** |
| 2 | travail L2411-12 (…19121659) | Comité de la société issue d'une « opération transfrontalière » ; transition pour les licenciements engagés après la réforme | `8dd4e5386c…` = | motif complété, notes réécrites | completed | **Intacte** |
| 3 | travail L2413-1 (…36262730) | 7° ter « opération transfrontalière » et transition CDD | `cb0da87383…` = | = | pending | **Intacte** |
| 4 | travail L2421-4 (…35652497) | 2° ter « opération transfrontalière » et transition | `99f9395442…` = | = | pending | **Intacte** |
| 5 | travail R2372-17 (…47631123) | Aucune transmission systématique à l'inspection du travail ; aucun envoi de remplacement | `f7d6ec7901…` = | = | pending | **Intacte** |
| 6 | travail R2373-5 (…47631067) | Abrogation alignée sur L2371-5 et R2372-17 | `ab9fb2ba9c…` = | = | pending | **Intacte** |
| 7 | cch L423-16 (…37668236) | « Sous réserve de la dispense prévue au 5° de l'article L. 423-1-2 » | `5abff10d2d…` = | motif complété, notes réécrites | completed | **Intacte** (contrepartie réglementaire : RT-INTEG-02) |
| 8 | cch L423-15 (…37668247) | Même réserve | `89d254622e…` = | motif complété, notes réécrites | completed | **Intacte** (RT-INTEG-02) |
| 9 | urba R121-23 (…31720973) | Renvoi au « délai d'observations d'au moins quinze jours prévu à l'article R. 121-22, avec les règles transitoires » | `bc4d46a6a3…` = | motif =, notes réécrites | completed | **Intacte** (notes des contreparties obsolètes : RT-INTEG-01) |
| 10 | a4 196 A (…006301986) | Déclaration TSCA limitée aux faits générateurs antérieurs à la suppression | `eef873d76c…` = | motif et notes réécrits | completed (lecture native du 24 octobre, corps identique) | **Intacte** |
| 11 | cgi 1649 quater B quater XV (…51764508, 2025-06-19 → 2027-01-01) | Télédéclaration TSCA réservée aux faits anciens | `77f1263217…` = | = | pending | **Intacte sur sa version** (versions différées : RT-INTEG-03) |

Aucune correction n'est **perdue ou contredite**. Aucune n'est **non vérifiable** : les onze images intégrées étaient disponibles en entier dans les preuves scellées.

### 4.2 Détail des points sensibles

**a3 38, CRL.** La seconde passe a réécrit deux passages :
- le III, qui réserve désormais la dispense de bilan du VI de 302 septies A bis ;
- le dernier alinéa, qui porte sur l'IS à la distribution : interdiction d'un dépôt annuel au seul titre des bénéfices conservés, et dépôt facultatif avant distribution.

La ligne CRL corrigée est restée identique : « a. […] le montant des seules recettes nettes perçues avant l'entrée en vigueur de la loi supprimant la contribution sur les revenus locatifs et restant soumises à la contribution mentionnée à l'article 234 nonies […], dans les conditions transitoires de cet article ».

Contrepartie : la proposition de CGI 234 nonies (`10a6b1dd…`, completed) dispose que « Les recettes perçues avant cette entrée en vigueur restent seules soumises à la contribution ». Elle interdit aussi tout « relevé, justificatif » pour les recettes nouvelles. La concordance est complète.

**Opérations transfrontalières.** La contrepartie L2411-1 (`b50d3c0b…`, completed) porte toujours le 7° ter « société issue d'une opération transfrontalière » et la même transition « licenciements engagés à compter de l'entrée en vigueur ». L2371-5 (`92f5ddac…`, completed) porte la suppression des transmissions systématiques sur laquelle R2372-17 et R2373-5 s'alignent mot pour mot. Les protections autonomes sont préservées : autorisation de l'inspecteur, pouvoirs de contrôle. Aucun préavis de quinze jours n'est importé dans le statut protecteur.

**CCH.** La proposition de L423-1-2 5° (`8d5d6193…`, completed) dispense bien les prêts et avances « entre la société et ses associés ou entre ses associés » de la déclaration préalable et du délai d'opposition. Les corrections de L423-15 et L423-16 la réservent. Les décrets d'application ne la réservent pas : voir RT-INTEG-02.

**R121-23.** La contrepartie R121-22 (`3438478c…`, completed) dit : « Ce délai peut courir pendant celui fixé par l'arrêté prescrivant l'ouverture de l'enquête et ne s'y ajoute pas systématiquement ». Ses notes reconnaissent que le conflit est résolu. Les corps de L121-32 et L121-34 suppriment bien l'avis communal distinct (« aucun avis ni délibération distincts ne sont requis »). Leurs notes, elles, annoncent encore la contradiction : voir RT-INTEG-01.

**TSCA.** La proposition de CGI 991 (`5c1efc50…`, pending) dispose que « La taxe spéciale sur les conventions d'assurances est supprimée pour les faits générateurs intervenant à compter de l'entrée en vigueur » et que « Aucune déclaration […] ne peut être exigé ». 196 A et le XV y sont bornés. L'annexe III 385 (`90c8ea62…`) est abrogée pour les faits nouveaux, ce qui est compatible.

### RT-INTEG-01 (P2, anomalie d'inventaire, confirmé) : notes de revue obsolètes qui contredisent des corrections déjà intégrées

Les corps normatifs sont cohérents, mais quatre notes de revue décrivent encore comme ouvertes des incohérences que les corrections du 24 octobre ont résolues :
- **urba L121-32** (completed), notes : « Incohérence effective hors lot : R121-23 proposé réserve encore « le délai supplémentaire de quinze jours » ». C'est faux pour le corps courant de R121-23 (`bc4d46a6…`).
- **urba L121-34** (completed), notes : « sa formule « le délai supplémentaire de quinze jours » reste à mettre en cohérence avec R121-22 proposé ». Même constat.
- **a3 385** (completed), notes : 196 A « n'exclut pas encore expressément les faits nouveaux » et « Le XV de 1649 quater B quater doit aussi réserver la télédéclaration TSCA aux dettes anciennes ». Les deux sont faits (`eef873d7…`, `77f12632…`).
- **a3 38** (completed), notes : « son XV et 196 A annexe IV restent à borner au stock TSCA ancien hors lot ». C'est fait.

La note de R121-23 l'annonce déjà (« Les notes de L121-32 et L121-34 du corpus qui annoncent encore cette contradiction doivent être actualisées »), comme celle de 196 A pour 385.

Effet : aucun effet normatif. En revanche, un risque de reprise erronée : une lecture native future pourrait « corriger » une seconde fois un texte déjà corrigé, ou un audit pourrait compter une contradiction inexistante.

### RT-INTEG-02 (P2, coordination manquante, à confirmer) : D423-1-1 et D423-1-2 ne réservent pas la dispense du 5° de L423-1-2

Les corrections de L423-15 et L423-16 introduisent « Sous réserve de la dispense prévue au 5° de l'article L. 423-1-2 ». Les propositions réglementaires d'application, encore pending, contiennent toutes deux : « La déclaration préalable et le délai légal d'opposition demeurent applicables » (D423-1-1 `19fcdde9…`, D423-1-2 `7a0604c1…`), sans réserve. Leurs notes ne mentionnent que l'information SGA. Les notes courantes de L423-15 (« Son maintien général de déclaration doit encore réserver la dispense de L423-1-2 ») et de L423-16 (« D423-1-2 […] doit réserver la dispense spéciale ») le constatent elles-mêmes.

En droit, la hiérarchie des normes et le libellé « À l'appui de la déclaration préalable » limitent la portée du décret aux cas où une déclaration est due. Une lecture isolée de la phrase pourrait pourtant laisser croire à un maintien général de la déclaration pour les financements intra-groupe de la société de coordination. Il s'agit d'une coordination manquante à effet limité. Le statut reste « à confirmer » parce que les deux articles n'ont pas encore reçu leur seconde passe.

### RT-INTEG-03 (P2, coordination manquante, à confirmer) : la correction XV de 1649 quater B quater n'est portée que sur une version qui expire le 1er janvier 2027

La correction TSCA du XV est intacte sur LEGIARTI000051764508 (ABROGE_DIFF, 2025-06-19 → 2027-01-01). Les versions suivantes n'ont aucune proposition (not_in_inventory) :
- LEGIARTI000053188914 (VIGUEUR_DIFF, 2027-01-01 → 2030-01-01) ;
- LEGIARTI000049473689 (VIGUEUR_DIFF, à partir de 2030).

Toutes deux gardent le XV source : « Les déclarations de la taxe sur les conventions d'assurance mentionnée à l'article 991, des taxes assimilées prévues aux articles 990 I et 1635 bis A […] sont souscrites par voie électronique ». La TSCA y est sans borne temporelle, et 990 I sans la restriction aux décès antérieurs.

Les notes de 196 A le relèvent : « Sa borne de version au 1er janvier 2027 ne fixe pas la date de réforme : version suivante à vérifier avant insertion définitive ».

L'effet pratique est limité. La proposition de 991 interdit toute déclaration pour un fait générateur nouveau, et le XV ne fait que fixer un canal. Mais si la réforme entre en vigueur après le 1er janvier 2027, le texte consolidé applicable ne porterait plus la coordination.

Ce n'est pas un cas isolé : 519 versions VIGUEUR_DIFF n'ont aucune proposition, et 216 numéros associent une version ABROGE_DIFF rédigée à un successeur différé non rédigé. Exemple du même dossier : la proposition de R434-32 (suppression du délai de dix jours et du formulaire) porte sur une version qui expire le 1er novembre 2026, et la version suivante (…54060111) garde « dans un délai de dix jours, à l'aide d'un formulaire ». Le chantier des « différés » est déjà déclaré ouvert par le projet (REPORT TSCA). Il est signalé ici pour les seules corrections de ce dossier, sans compter les autres cas comme des objections distinctes.

---

## 5. Propositions de correction, présentées séparément

Aucune n'est appliquée. Chacune est gardée par les empreintes du JSON et doit être revérifiée contre la version courante avant usage.

### P-DOC-01 : annexe I R434-32 (7)

Ne pas rédiger de valeurs pour les quadranopsies. Si une proposition est faite pour ce chapitre, conserver la phrase et remplacer le marqueur par : « [figure du Journal officiel non reproduite dans la base LEGI : valeur attribuée à chaque quadrant, à reproduire d'après le fac-similé officiel] ». Joindre la référence JORF dès qu'elle est obtenue. Garder l'état documentary_hold tant que le fac-similé n'est pas obtenu. Dépendance : aucune proposition existante n'en dépend.

### P-DOC-02 : annexe IV 15, 1° (texte proposé pour le seul 1°, reste de l'article inchangé)

> 1° Les relevés encore exigés par le 1 de l'article 57 de l'annexe II au code général des impôts sont établis sous forme de fiches individuelles, sur tout support, y compris mécanographique ou électronique, comportant les renseignements mentionnés aux 2° et 4°. L'usage des modèles administratifs n° 30-0812 et n° 30-0813 est facultatif. Aucun relevé n'est établi pour les paiements dont la déclaration prévue à l'article 242 ter du code général des impôts tient lieu de relevé. Ces dispositions s'appliquent aux relevés établis à compter de l'entrée en vigueur de la loi ; les relevés antérieurement établis selon les modèles restent valables et ne sont pas à refaire.

Justification :
- La phrase supprime la dépendance à des modèles introuvables, sans perte d'information puisque les 2° et 4° restent intégralement exigés.
- Elle suit le précédent de 196 A, où le modèle est rendu facultatif.
- Elle coordonne l'article 15 avec la proposition de l'annexe II, 57, sans créer de formalité de remplacement.
- Elle supprime la limite de format de 21 × 13 cm, qui ne servait qu'à la substitution.

Dépendances :
- annexe II 57 et CGI 242 ter ;
- annexe IV 14 et 16 ;
- vérification préalable du renvoi « troisième alinéa du 3 de l'article 158 » et du « crédit d'impôt » du 4° d, à faire sans invention.

Réserve : les modèles pourraient comporter des renseignements absents des 2° et 4°. La phrase en ferait alors une simplification de fond, à assumer comme telle dans le motif.

### P-INTEG-01 : notes (pas de changement normatif)

Actualiser les notes de revue de L121-32, L121-34, annexe III 385 et annexe III 38. Supprimer les mentions de contradiction ou de bornage « restant à faire » et renvoyer aux corps courants de R121-23 (`bc4d46a6…`), 196 A (`eef873d7…`) et 1649 XV (`77f12632…`). Aucune modification des corps.

### P-INTEG-02 : D423-1-1 et D423-1-2, dernière phrase

Remplacer « La déclaration préalable et le délai légal d'opposition demeurent applicables. » par :

> Sous réserve de la dispense prévue au 5° de l'article L. 423-1-2, la déclaration préalable et le délai légal d'opposition demeurent applicables ; aucune pièce n'est à fournir pour les prêts et avances entrant dans le champ de cette dispense, y compris lorsque la déclaration d'un financement antérieur n'a pas été déposée.

Ne rien changer d'autre. Il faut conserver :
- le seuil « au moins égale à 5 % » de D423-1-1 ;
- la suppression de la clause suspensive ;
- la survie des clauses anciennes.

### P-INTEG-03 : 1649 quater B quater, versions différées

Lorsque les versions …53188914 et …49473689 seront rédigées, reprendre à l'identique le XV corrigé (borne TSCA aux faits générateurs antérieurs et restriction de 990 I aux décès antérieurs), en l'adaptant au seul texte de chaque version. Faire de même pour R434-32 …54060111 avec la suppression du délai de dix jours et du formulaire. Aucune autre modification.

---

## 6. Incertitudes restantes et éléments non examinés

- Identifiant JORF exact de la publication du barème AT contenant le cliché : non établi. Légifrance a répondu 403 ; aucune source officielle accessible.
- Existence actuelle des CERFA 30-0812 et 30-0813 et leur contenu : inconnus.
- Renvois du 4° a et d de l'annexe IV 15 à 158 et au crédit d'impôt : non qualifiés.
- Classes B à D de RT-DOC-03 : seuls les manifestes ont été lus, ni les tableaux ni les formules. Les valeurs de l'annexe II du code du travail n'ont pas été confrontées.
- Corrections intégrées : seuls les corps, motifs et notes ont été comparés, ainsi que les contreparties citées. Les métadonnées de lot (`substantive_impact`, certificats) et la publication sur les cinq sites n'ont pas été revérifiées.
- Les réécritures postérieures de a3 38, en dehors de la ligne CRL (III et dernier alinéa sur l'IS), n'ont pas été évaluées au fond. Elles relèvent d'autres dossiers (IS à la distribution).
- Les autres versions différées (519) ne sont pas examinées.
- Seconde passe en cours : les articles pending (L2413-1, L2421-4, R2372-17, R2373-5, 1649 XV, D423-1-1/2, 991) peuvent changer.
