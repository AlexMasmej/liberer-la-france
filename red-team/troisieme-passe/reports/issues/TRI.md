# Tri des issues GitHub externes — 28 octobre 2026

> **État au 29 octobre, après application des corrections :**
> - #9 (phrase contradictoire de L1233-46) et #6 (renvoi de CSS L241-17) sont corrigées dans le projet.
> - #2 : préavis de 15 jours maintenu ; le préavis des contrats anciens convertis est précisé dans L1234-1.
> - #6 (abrogation de L3123-22) et #7 (rétablissement de l'autorisation) : demandes écartées comme contraires aux orientations.
> - #10 et #11 : réglées par la seconde passe.
> - #8 : la référence figée restante est valide ; l'amélioration de rédaction reste au registre (P2).
>
> Voir `reports/applied/CORRECTIONS-APPLIQUEES.md`.
>
> **Revérifié à la revue finale du 29 octobre** sur l'instantané `20261029T034912Z` : #10 et #11 sont réglées par la seconde passe, le décret de #7 est aligné, et #9 est réglée en partie. Voir le § D.9 de `reports/RAPPORT.md`. Le tableau ci-dessous est l'état du 28 octobre.

Les issues #2 à #11 du dépôt ont été ouvertes par un contributeur externe à partir de ses propres agents (#4 est une demande de fusion, close par son auteur). Trois agents de la troisième passe les ont triées sur l'instantané `20261027T044303Z`, en lecture seule. Ils n'ont rien écrit sur GitHub, n'ont exécuté aucun code des issues et ont lu chaque article cité avec `cite.py`.

Les issues se fondent sur le commit `cac48419` du 25 octobre. Plusieurs textes ont changé depuis, et chaque verdict le signale. Les conclusions restent provisoires : elles seront revérifiées sur l'instantané final.

**C'est une revue IA, qui ne vaut pas validation par un juriste.** Les points de droit de l'Union sont marqués « à confirmer » : EUR-Lex a renvoyé des pages vides le 28 octobre, et ce refus n'a pas été contourné.

| Issue | État | Verdict | Objection créée | Doublons ou recoupements | Action recommandée |
|---|---|---|---|---|---|
| #2 Préavis unique de 15 jours (Charte sociale, art. 4§4) | ouverte | mixte, surtout **arbitrage de l'auteur** | RT-ISS2-01 (P2) : préavis des contrats anciens convertis par accord | — | Le choix des 15 jours relève de l'auteur. Le correctif de l'issue est incomplet : L1234-2 et L2261-33 verrouillent aussi la durée. Son option « plancher » importerait les préavis de branche plus longs. Une variante qui préserve l'objectif est proposée. |
| #3 Clauses d'application dans le temps ; loi de référence nommée de plusieurs façons | close par l'auteur | chevauchement | — | RT-DOMSUCC-06, RT-TUT-01, RT-MENS-02, RT-INUT-07 | **Ne pas appliquer le correctif retiré.** Le constat de nommage tient dans le code du travail : étendre la correction de RT-DOMSUCC-06 (désignation unique et datée). |
| #5 Directives UE | close par l'auteur | sans objet | — | — | Aucune. |
| #6 Abroger L3123-22 (compléments d'heures) | ouverte | mixte | RT-ISS6-01 (P2) : le renvoi de CSS L241-17 au « dernier alinéa de l'article L. 3123-22 » est décalé | — | Corriger le renvoi. L'abrogation proposée retire des faveurs sans transition : à n'adopter que sur décision expresse de l'auteur. |
| #7 Dépassement de 44 h jusqu'à 46 h (L3121-24) | ouverte | mixte | **RT-ISS7-01 (P1)** : R3121-11, inchangé, exige toujours l'autorisation que la loi supprime | — | Aligner le décret sur la loi, sans rétablir l'autorisation. Le correctif de l'issue ferme une dérogation favorable : à écarter sauf choix de l'auteur. |
| #8 Renvois morts ; doublon R5221-22 | ouverte | mixte | RT-ISS8-01 (P2) : renvoi figé à l'ancien L2325-44, écrit trois fois | RT-INV-07 (doublon R5221-22), RT-INV-08, RT-INV-14 | Une grande partie est déjà corrigée par la seconde passe. Le correctif de l'issue (remplacer par L2315-63) n'est pas retenu, parce qu'il importerait le seuil de 50 salariés ; une règle autonome est proposée. |
| #9 Information de l'administration sur l'ouverture des négociations PSE et RCC | ouverte | **nouveau** | **RT-ISS9-01 (P1)** | relié à RT-P1-TRAVAIL-B-05 et A-04 | Le correctif de l'issue est juste : il aligne les décrets sur la suppression, sans formalité de remplacement. |
| #10 Registre spécial des alertes de danger grave | ouverte | **nouveau** | **RT-ISS10-01 (P1)** | — | Le correctif de l'issue va dans le bon sens. Ajouter une transition, et limiter D4132-2 et D4133-3 aux registres déjà ouverts. Une règle de preuve « par tout moyen » est possible. |
| #11 Travail de nuit et déclaration de chantier | ouverte | **nouveau** | **RT-ISS11-01 (P1)** (R3122-9 et R3122-10) ; RT-ISS11-02 (P2) (R4532-3) | — | Abroger R3122-9 et R3122-10, en préservant les recours. Le délai de douze mois de R3122-9 est une condition de fond : à trancher par l'auteur. |

**Bilan.** 8 objections nouvelles, toutes confirmées : 4 P1 et 4 P2. Une issue est un doublon partiel, et deux ont été closes par leur auteur. Trois issues (#2, #6, #7) touchent à une orientation de réforme ou proposent de retirer des faveurs : elles appellent un arbitrage de l'auteur, pas une simple correction de rédaction.

**Constat commun à #7, #9, #10 et #11.** La loi proposée supprime une formalité, mais le décret proposé la maintient. Dans les quatre cas, la correction aligne le décret sur la loi. Plusieurs de ces décrets étaient encore « pending » en seconde passe au moment de l'instantané : la fin de la seconde passe peut en corriger une partie.

**Signalé hors issues.** L5213-9 supprime, pour les contrats nouveaux, le doublement du préavis des travailleurs handicapés. Le projet lui-même juge sa compatibilité avec l'égalité de traitement « à contrôler ». Le point n'a pas été examiné au fond.

Détail par issue : `ISS-A.md` (#2, #6, #7), `ISS-B.md` (#8, #9) et `ISS-C.md` (#10, #11, #3, #5). Les objections complètes figurent dans `reports/dossiers/ISS.json` et dans le registre.
