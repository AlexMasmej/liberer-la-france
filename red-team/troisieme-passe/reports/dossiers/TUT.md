# Dossier TUT — CSS D227-6 / L224-10 : approbation, tutelle, opposition et calendriers

Red-team juridique indépendante, troisième passe. Rédigé le 26 octobre 2026 sur l'instantané `20261026T230545Z` (corpus au 18 octobre 2026). Ce rapport est une revue assistée par IA. Il ne vaut pas validation par un juriste. Les propositions du projet évoluent encore en seconde passe : toutes les conclusions sont provisoires.

## 1. Périmètre réellement lu

Tous les articles ci-dessous ont été lus en entier avec `tools/cite.py` : toutes leurs versions, sources, NOTA, propositions, motifs et notes. Les sorties sont dans `evidence/cited/20261026T230545Z/`. La liste indique l'identifiant de la version courante ; les versions historiques ont été imprimées et sauvegardées par le même appel.

**Cœur du dossier**
- L224-10 : six versions, dont LEGIARTI000006742291 (1994), 6742292, 6742293, 17843020, 37064592 et la version courante 44404083 (`rewrite_draft`, inventaire `completed`).
- D227-6 : LEGIARTI000030773015 (`rewrite_draft`, inventaire `pending`).
- L226-4, versions historiques : LEGIARTI000006741828 et 6741829 (TRANSFERE au 1er janvier 1995).

**Institut national de formation**
- D227-1 (30773003), D227-2 (30773005), D227-3 (30773009).
- D227-4 : trois versions, dont la courante 46021933.
- D227-5 : deux versions, dont la courante 46356333.
- L228-1 (37948785), D224-1 (30774224), L216-3 (6741713), L224-5 (44404097).

**Caisses nationales et UCANSS**
- Statut et contrôle : L221-2, L221-3, L222-4, L223-1, L223-2, L223-3, L223-6, L223-7, L225-2.
- UCANSS : L224-5-1, L224-5-4, L224-11, L224-13.
- COG : L227-1, L227-2, L227-3.
- Textes réglementaires : R224-5 (deux versions), R225-5, R226-1 à R226-6 (deux versions de R226-4), D224-11, R221-12, R223-15.
- Régime des travailleurs indépendants : L612-1, L612-2, R612-7.

**Contrôle des organismes locaux**
- L151-1 (sept versions), R151-1 à R151-5.
- L152-1, R152-1 à R152-8.
- L153-1 à L153-10, R153-2, R153-3, R153-4, R153-6, R153-7, R155-1.
- L154-1, L281-3.

**Dépendants indirects de R226-4 et régimes comparables**
- D635-5 (trois versions), D632-7, L635-3, L632-3.
- L766-10, R767-6.

**Preuves scellées lues**
- `evidence/sealed/runtime/coherence-joint-twelve-readonly-20261025T1915Z/` : REPORT.md, `joint-parental-semantic-review.json` (cas « Residual Institute deliberation procedure », classé `still_open_no_calendar_certification`), passages D227-6 de `joint-answer.json`.
- Candidats non enregistrés R612-7 (lot 00192), R151-1 et R151-3 (lot 00112) dans `joint-staged-live-batches`.

**Sources publiques consultées le 26 octobre 2026**
- Conseil constitutionnel, décisions n° 2002-463 DC (considérant 18) et n° 2003-473 DC (considérant 18).

**Non examinés en profondeur, conformément au périmètre**
- Les dix autres candidats de la revue des douze (dossier CSS12).
- R612-7, R151-1, R151-3 et R153-2 ne sont cités que comme dépendances.

## 2. Méthode

1. J'ai recherché en lecture seule les articles courants et les propositions qui renvoient à « 224-10 », « 226-4 », « 227-6 » ou à l'Institut, ou qui organisent une approbation, une opposition ou une suspension de délibérations ou de budgets.
2. J'ai lu en entier, avec `cite.py`, chaque pièce retenue.
3. J'ai reconstruit le calendrier en droit courant et en projet : émetteur, destinataire, délai, effet du silence, voie d'opposition, déclencheur transitoire.
4. J'ai confronté le résultat à la preuve scellée, qui laissait ouverts le régime résiduel et le calendrier de D227-6 et L224-10.
5. J'ai vérifié la jurisprudence constitutionnelle invoquée.

Chaque passage cité dans `TUT.json` a été contrôlé mécaniquement comme sous-chaîne exacte du champ source ou proposé correspondant.

## 3. Chronologie du mécanisme

### 3.1 Droit courant (18 octobre 2026)

| Organe | Transmission | Contrôle | Délai et effet du silence | Urgence |
|---|---|---|---|---|
| Conseils de la CNAM (et commission AT-MP), de la CNSA, de la CNAF, de la CNAV, de l'ACOSS ; conseil d'orientation et comité exécutif de l'UCANSS ; assemblée générale du CPSTI (L612-2) | Procès-verbaux aux ministres chargés de la sécurité sociale et du budget dans les 10 jours de la séance (R224-5, R225-5 ; R612-7 pour le CPSTI) | Opposition du ministre de la sécurité sociale ou du budget (L224-10 al. 1, R226-4) | 20 jours à compter de la communication ; le silence rend la délibération exécutoire | Visa d'exécution immédiate par le ministre de la sécurité sociale, en accord avec le budget (R224-5 al. 2, R225-5 al. 2) |
| Mêmes organes, décisions prises en application de la COG, budgets compris | Réception par les ministres de la sécurité sociale et du budget, plus le ministre chargé des personnes âgées et handicapées pour la CNSA | Opposition motivée (L224-10 al. 2) | Exécutoires de plein droit 20 jours après réception. Sans COG signée au 1er janvier, retour au régime de l'alinéa 1 (al. 3) | — |
| UCANSS (D224-11) | — | « Approbation [...] dans les conditions fixées à L224-10 », alors que L224-10 la place sous opposition | Voir RT-TUT-02 | — |
| Accords collectifs nationaux UCANSS | — | Agrément ministériel, plus opposition du conseil d'orientation aux trois quarts | 1 mois (L224-5-1) | — |
| Actes des directeurs généraux de la CNAM et de la CNSA | Liste fixée par arrêté, communication dans les 10 jours | Opposition motivée pour illégalité ou méconnaissance de la COG | 15 jours (R221-12) ; 30 jours pour la CNSA, avec approbation expresse possible sous 8 jours en cas d'urgence (R223-15) | — |
| Conseil d'administration de l'Institut national de formation (D227-6) | Non précisée | Approbation du ministre de la sécurité sociale « dans les conditions fixées à L224-10 » | Indéterminé : l'Institut n'est pas cité par L224-10 (RT-TUT-02). Budget approuvé par l'UCANSS (D227-3, L153-2). Commissaire du Gouvernement (D227-4) | — |
| Caisses locales (CPAM, CARSAT, CAF, URSSAF), unions nationales (R151-4, R151-5), instances régionales du CPSTI | Communication immédiate au service de R155-1 (R151-1), avec pièces (R151-2) | Annulation pour illégalité ; suspension pour complément d'instruction | 8 jours francs, puis 40 jours pour la décision du ministre ; à défaut, exécutoire de plein droit | — |
| Mêmes organismes, risque financier | — | Suspension sous 8 jours ; la caisse qui maintient sa décision saisit la caisse nationale | Décision suspendue jusqu'à confirmation ou infirmation nationale devenue « définitive conformément à L226-4 », c'est-à-dire l'ancien numéro de L224-10, soit 20 jours (RT-TUT-03) | — |
| Budgets des organismes de base | — | Approbation par l'organisme national (L153-2) ; ARS pour les établissements de santé (R153-2) | Substitution au 1er janvier (L153-4) ; douzièmes provisoires (R153-7) | — |

### 3.2 Projet (instantané)

- **T_L, entrée en vigueur de la loi.** Les délibérations nationales nouvelles sont exécutoires dès leur adoption, y compris les budgets et décisions liées à la COG (L224-10 proposé). La transmission est maintenue. Les approbations spéciales et l'opposition prévue par L224-5-1 sont réservées. Le critère de bascule est la date d'adoption. Suivent sur le même déclencheur : R226-4 (abrogé pour l'avenir), R224-5 et R225-5 (plus de visa d'urgence), D224-11, et le candidat R612-7. La suspension pour seul risque financier disparaît ; les suspensions en cours cessent (L151-1 proposé, candidats R151-1 et R151-3). L'approbation triennale de L153-8 est supprimée, y compris pour les délibérations en attente.
- **T_D6, décret qui « prononce » l'abrogation de D227-6.** L'approbation ministérielle des délibérations de l'Institut disparaît pour les délibérations adoptées à compter de cette date. Les délibérations antérieures restent régies par l'ancien régime.
- **Autres déclencheurs.** « Présent décret » ou « présent texte » : R226-2, R151-2, D227-5, D227-2, D224-1. « Décret portant la présente rédaction » : D632-7. « La réforme » : D635-5. « La loi » dans des articles réglementaires : R152-1, R152-2, R152-6.

### 3.3 Délais devenus incompatibles et renvois vers des procédures supprimées

- Si T_L précède T_D6, D227-6 renvoie aux « conditions fixées à L224-10 » alors que celui-ci n'en contient plus, et R226-4 ne fixe plus de délai pour ces délibérations. Les délibérations de l'Institut adoptées entre T_L et T_D6 ne relèvent ni de l'ancien régime de L224-10 (réservé aux délibérations adoptées avant la loi) ni du nouveau régime de D227-6 (qui ne vaut qu'après le décret) : RT-TUT-01.
- D635-5 reste lié au délai de R226-4. Le fond est coordonné, mais le déclencheur et le critère ne le sont pas : RT-TUT-08.
- R226-2 et le dernier 2° de R226-1 organisent encore la saisine nationale prévue par le circuit de suspension financière que L151-1 supprime : RT-TUT-04.
- Le troisième alinéa de L224-10 proposé (repli en l'absence de COG) n'a plus d'objet : RT-TUT-06.
- Le renvoi à L226-4 dans L151-1 et R225-5 désigne en réalité l'ancien L224-10 : RT-TUT-03.
- Délibérations en cours à la bascule : l'approbation de l'Institut reste due pour les délibérations antérieures, alors que L153-8, L612-1, L216-3 et L224-5-1 dispensent les dossiers pendants (RT-TUT-01). Une infirmation nationale non encore définitive à T_L voit son sort laissé incertain (RT-TUT-05).

## 4. Constats

| ID | Priorité | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-TUT-01 | P1 | incohérence du projet | confirmé | Désynchronisation entre D227-6 (décret) et L224-10 (loi). Renvoi vers une procédure vidée, vide transitoire, régime des délibérations pendantes divergent, article qui se déclare lui-même abrogé, exigence de L228-1 V |
| RT-TUT-02 | P2 | conflit de source | confirmé | D227-6 et D224-11 soumettent à une « approbation dans les conditions de L224-10 », article qui organise une opposition et exclut les approbations de son champ |
| RT-TUT-03 | P2 | conflit de source | confirmé | L226-4, cité par L151-1 et R225-5, est l'ancien numéro de L224-10 (transféré en 1995, texte identique). Les notes du projet le disent à tort absent du corpus ; les corps proposés sont corrects |
| RT-TUT-04 | P2 | coordination manquante | confirmé | R226-2 et le dernier 2° de R226-1 proposés maintiennent la saisine nationale du circuit financier supprimé par L151-1 proposé. R226-2 ne fait pas partie des douze candidats |
| RT-TUT-05 | P2 | incohérence du projet | à confirmer | Infirmation nationale votée avant T_L mais pas encore définitive : la cessation des suspensions (L151-1) se heurte au maintien de l'ancien régime pour les délibérations antérieures (L224-10) |
| RT-TUT-06 | P2 | incohérence du projet | confirmé | Troisième alinéa de L224-10 proposé sans objet ; perte silencieuse du repli en l'absence de COG |
| RT-TUT-07 | P2 | risque juridique | à confirmer | Plus aucun contrôle par opposition des budgets nationaux d'établissements publics, alors que les actes des directeurs restent soumis à opposition (R221-12, R223-15) et que d'autres articles du projet gardent une opposition non suspensive (L766-10, R767-6). Inconstitutionnalité non démontrée |
| RT-TUT-08 | P2 | coordination manquante | confirmé | Déclencheurs hétérogènes : « la réforme » et la date de présentation dans D635-5 ; « présent texte » dans R151-2 contre « la loi » dans R152-1 et R152-2 |

Total : 8 objections (1 P1, 7 P2 ; 6 confirmées, 2 à confirmer). Aucun P0.

### Alertes écartées ou non comptées

- **R612-7** (opposition de L224-10 exercée par les ministres sur l'assemblée du CPSTI) : en l'état de l'instantané, c'est une contradiction effective avec L224-10 et L612-2 proposés. Elle est déjà traitée par le candidat non enregistré du lot 00192, sur le même déclencheur que la loi. Je la renvoie au dossier CSS12 et ne la compte pas.
- **R151-1 et R151-3**, conservés sans changement dans l'instantané alors que L151-1 proposé supprime la suspension financière : même situation. Les candidats du lot 00112 couvrent ce point ; il n'est pas compté.
- **D224-11** : la proposition est correctement datée sur la réforme de L224-10. Ce n'est pas une contradiction ; il sert de modèle à la correction de RT-TUT-01.
- **D227-3 et L153-2** : l'approbation budgétaire de rattachement par l'UCANSS est bien distincte de l'approbation ministérielle supprimée par D227-6. Aucune contradiction.
- **L153-8 et L224-10** : une délibération triennale en attente d'approbation à T_L est dispensée et ne retombe pas sous l'opposition de L224-10 (elle en était exclue). Écarté, mais mentionné dans les incertitudes.
- **Forme « Le présent article est abrogé à compter de… »** : ce procédé se retrouve dans plusieurs propositions (L153-6, L153-9, R152-6, R152-8). Il n'est traité que pour D227-6, dans RT-TUT-01, où il se combine avec un déclencheur circulaire. Je ne le compte pas comme objection générale.

## 5. Propositions de correction (séparées)

### C1 — D227-6 (RT-TUT-01, et RT-TUT-02 par voie de conséquence)

Texte proposé complet :

> Les délibérations du conseil d'administration de l'Institut national de formation adoptées à compter de la date d'entrée en vigueur de la loi supprimant le régime général d'opposition prévu à l'article L. 224-10 sont exécutoires dès leur adoption, sous réserve des règles de publication ou de notification qui leur sont applicables. Elles ne sont soumises à aucune approbation du ministre chargé de la sécurité sociale ; aucune autorisation ni déclaration équivalente ne peut être exigée sur le fondement du présent article.
>
> Les délibérations adoptées avant cette date qui n'ont été ni approuvées ni refusées à cette date deviennent exécutoires à cette même date, sans nouvelle délibération ni nouvelle demande. Les approbations déjà accordées, les refus notifiés avant cette date et les recours qui s'y rapportent demeurent régis par les dispositions antérieures.
>
> Le contrôle de la gestion et l'approbation du budget de l'Institut par l'Union des caisses nationales de sécurité sociale prévus à l'article D. 227-3, la présence du commissaire du Gouvernement prévue à l'article D. 227-4 ainsi que les contrôles de légalité et les contrôles financiers reposant sur un fondement autonome demeurent applicables dans leur champ propre.

**Justification.** Le texte retient le même déclencheur et le même critère (adoption) que L224-10, R226-4, R224-5, R225-5 et D224-11. Il traite les dossiers pendants comme L153-8 et L612-1, ce qui rend inutile toute qualification de l'ancien délai indéterminé. Une règle positive satisfait L228-1 V (modalités de la tutelle de l'État) sans créer de formalité.

**Dépendances.** L224-10 proposé ; R226-4, R224-5, R225-5 et D224-11 proposés ; D227-1, D227-3 et D227-4 maintenus.

**Ce qui est préservé.** Budget de rattachement, contrat pluriannuel, refus et recours antérieurs, nominations antérieures.

**Autres options.** Abrogation par un décret entrant en vigueur au plus tard à T_L, avec une transition placée dans le décret d'abrogation ; ou neutralisation directe dans L224-10, option moins propre.

### C2 — R226-2 et R226-1, dernier 2° (RT-TUT-04)

R226-2, texte proposé complet :

> Pour l'application du troisième alinéa de l'article R. 151-1 dans sa rédaction antérieure à la date d'entrée en vigueur de la loi supprimant la suspension pour seul risque financier prévue à l'article L. 151-1, l'organisme dont la décision a été suspendue par le responsable du service mentionné à l'article R. 155-1 saisit la caisse nationale compétente s'il maintient sa décision, sans nouvelle délibération obligatoire du conseil ou du conseil d'administration. Cette dispense n'empêche pas le conseil ou le conseil d'administration de modifier ou de retirer sa décision dans les conditions qui lui sont applicables.
>
> La dispense s'applique aux saisines effectuées à compter de l'entrée en vigueur du présent décret. À compter de la date d'entrée en vigueur de la loi mentionnée au premier alinéa, aucune saisine de la caisse nationale n'est requise ni ouverte sur le fondement du présent article. Les décisions rendues, les délais expirés et les recours ne sont pas remis en cause.

R226-1, dernier 2° proposé :

> 2°) pour l'application du troisième alinéa du même article dans sa rédaction antérieure à la date d'entrée en vigueur de la loi supprimant la suspension pour seul risque financier prévue à l'article L. 151-1, compte tenu de la nature du risque en cause.

**Dépendances.** L151-1 proposé ; candidats R151-1 et R151-3 (CSS12).

### C3 — L151-1, troisième alinéa (RT-TUT-05, à confirmer)

Insérer après « ne sont plus requises. » :

> Toutefois, lorsque le conseil ou le conseil d'administration de la caisse nationale a explicitement infirmé la décision avant cette date, celle-ci demeure suspendue jusqu'à ce que la délibération nationale soit devenue définitive selon l'article L. 224-10 dans sa rédaction antérieure ; si une opposition est formée contre cette délibération, la décision suspendue devient exécutoire.

**Option inverse.** Déclarer expressément sans effet les infirmations non définitives.

**Dépendances.** Candidats R151-1 et R151-3, à aligner.

### C4 — L224-10 (RT-TUT-06)

Texte complet proposé : voir `TUT.json`, RT-TUT-06, `minimal_correction`. Seul le deuxième alinéa change ; le troisième alinéa est supprimé et son cas est intégré au deuxième (« il en va de même lorsque la convention n'est pas signée avant le 1er janvier de la première année de sa mise en œuvre »). Le reste de la proposition est repris à l'identique.

### C5 — L224-10, dernière phrase du deuxième alinéa (RT-TUT-07)

Correction minimale, purement explicative :

> Les contrôles et recours prévus par les autres dispositions applicables, notamment l'opposition aux actes des directeurs prévue par voie réglementaire, l'évaluation contradictoire des conventions d'objectifs et de gestion, le contrôle de la Cour des comptes prévu à l'article L. 154-1 et les recours juridictionnels, demeurent exercés dans leur champ.

**Option B, à arbitrer politiquement** (elle préserve l'exécution immédiate, sur le modèle de L766-10 proposé) : une opposition motivée, non suspensive, dans les vingt jours, limitée aux délibérations budgétaires qui méconnaissent la loi ou la COG. Elle ferait obstacle à l'exécution à partir de sa notification. Ce n'est ni une formalité ni une attente, mais elle rétablit un pouvoir que le projet a voulu supprimer.

C4 et C5 se combinent dans le même deuxième alinéa.

### C6 — D635-5, R151-2, R152-1 et R152-2 (RT-TUT-08)

- D635-5 : remplacer « pour les demandes d'approbation présentées à compter de l'entrée en vigueur de la réforme » par « pour les délibérations adoptées à compter de la date d'entrée en vigueur de la loi supprimant le régime général d'opposition prévu à l'article L. 224-10 », et « Pour les demandes antérieures » par « Pour les délibérations antérieures ».
- R151-2, R152-1 et R152-2 : choisir une même date, de préférence au moyen d'un article transitoire unique du décret d'application.

### C7 — Notes de revue (RT-TUT-03)

Corriger les notes de L151-1, L224-10 et R225-5 : L226-4 (LEGIARTI000006741828 et 6741829) est présent dans le corpus. Son texte est identique à celui de L224-10 en 1994, et il a été transféré au 1er janvier 1995. Aucun changement de corps n'est requis.

## 6. Évaluation du risque juridique

**Compétence loi / règlement.**
- La suppression de l'opposition générale de L224-10 relève de la loi ; le projet la porte bien dans un article législatif.
- R226-4 est un décret en Conseil d'État pris en application de L224-10. Il perd sa base pour les délibérations nouvelles et doit être abrogé pour l'avenir, ce que fait le projet.
- D227-6 est un décret simple, pris sur le fondement de L228-1 V. Ce texte exige qu'un décret précise « le contrôle et la tutelle exercés par l'État ». Une abrogation sèche laisserait le chapitre sans disposition expresse de tutelle d'État, hors présence du commissaire du Gouvernement. C1 y répond sans créer de formalité.
- Aucune incompétence négative n'est établie.

**Contrôle de l'emploi des fonds publics.** Les caisses nationales sont des établissements publics nationaux à caractère administratif (L221-2, L222-4, L223-2, L223-6, L225-2). Le projet supprime la seule voie d'opposition aux budgets nationaux (L224-10 al. 2) et l'approbation des règles triennales (L153-8). Il maintient en revanche l'opposition aux actes des directeurs (R221-12, R223-15) : l'asymétrie est réelle (RT-TUT-07).

**Exigences constitutionnelles.**
- L'équilibre financier de la sécurité sociale est un objectif de valeur constitutionnelle (décision n° 2002-463 DC, considérant 18).
- Le « bon usage des deniers publics » est reconnu dans la décision n° 2003-473 DC (considérant 18), à propos de la commande publique et de la protection des propriétés publiques.
- Ni l'une ni l'autre n'impose, en l'état des pièces lues, une tutelle a priori déterminée. Une censure n'est pas démontrable : le risque est qualifié de P2 à confirmer.

## 7. Incertitudes et éléments non examinés

- Les dates relatives de la loi et des décrets sont hypothétiques. Le vide de RT-TUT-01 n'existe que si la loi précède le décret.
- L'application de R151-4 et R151-5 à l'Institut, en tant qu'« union nationale », est plausible mais non établie.
- Je n'ai pas examiné le titre III du décret GBCP n° 2012-1246 (extérieur au corpus), ni d'éventuels textes de contrôle économique et financier applicables aux caisses nationales.
- Je n'ai pas recherché un par un les régimes d'opposition aux actes des directeurs de la CNAV, de la CNAF et de l'ACOSS.
- La pratique administrative de D227-6 est inconnue : délai effectif, approbation expresse ou tacite.
- L'acte JORF du transfert de L226-4 vers L224-10 n'a pas été consulté. Le chevauchement des dates LEGI (1994-1995) n'est pas expliqué.
- Je n'ai pas analysé en profondeur les dix autres candidats de la revue des douze (CSS12), ni les régimes R115-4 (GIE), R123-18 (EN3S), R135-5 (FSV) et R766-63 (CFE), qui ne dépendent pas de L224-10 : seul leur statut de projet a été relevé.
- La seconde passe continue : une proposition peut changer après l'instantané.
