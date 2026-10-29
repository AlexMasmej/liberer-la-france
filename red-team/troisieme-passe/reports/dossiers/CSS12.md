# Dossier CSS12 : les douze coordinations de gouvernance non intégrées (CSS)

Revue red-team indépendante, troisième passe, du 26 octobre 2026. Corpus de référence : LEGI au 18 octobre 2026, instantané `snapshots/20261026T230545Z`. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste. Ses conclusions sont provisoires, car la seconde passe continue en production.

## 1. Périmètre réellement lu

**Les douze articles candidats.** Ils sont tous dans le CSS (LEGITEXT000006073189). Toutes leurs versions ont été lues avec `cite.py` (source, NOTA, bornes, proposition, motif, notes, lot). Chaque candidat a aussi été lu en entier dans `joint-answer.json` du 25 octobre : corps, motif, notes, effets, `previous_draft`, `reference_checks` et certificat.

| Article | Version en vigueur | Statut courant | Seconde passe | Lot propriétaire |
|---|---|---|---|---|
| R123-1 | LEGIARTI000029389194 (2014-08-23→) | retained_unchanged | pending | automatic-securite-sociale/00096 |
| R123-1-1 | LEGIARTI000038790652 (2020-01-01→) | rewrite_draft | pending | 00096 |
| D224-7 | LEGIARTI000046356432 (2023-01-01→, NOTA décret 2022-1283) | rewrite_draft | pending | 00250 |
| R152-8 | LEGIARTI000029388285 (2014-08-23→) | rewrite_draft | pending | 00113 |
| D224-8 | LEGIARTI000046356451 (2023-01-01→) | rewrite_draft | pending | 00250 |
| R153-2 | LEGIARTI000022055116 (2010-04-01→) | retained_unchanged | pending | 00113 |
| R151-1 | LEGIARTI000021508199 (2010-01-01→) | retained_unchanged | pending | 00112 |
| R151-3 | LEGIARTI000029389202 (2014-08-23→) | retained_unchanged | pending | 00112 |
| R612-7 | LEGIARTI000042363356 (2020-09-26→) | retained_unchanged | pending | 00192 |
| R216-2 | LEGIARTI000036914470 (2018-05-17→) | retained_unchanged | pending | 00149 |
| R281-4 | LEGIARTI000036914411 (2018-05-17→) | retained_unchanged | pending | 00160 |
| R213-5 | LEGIARTI000006748552 (1985-12-21→) | retained_unchanged | pending | 00149 |

**Articles liés lus en entier (version courante et proposition).**
- Agrément : L123-1, L123-2, L123-2-1, L123-2-2, L123-2-3, L123-3, L224-5, L224-5-1, L224-5-2, L224-5-3, L153-5, R123-48, R123-53, R123-54, R123-56, R123-59, R123-63.
- Opposition et budget : L153-1 à L153-6, R153-3, R153-4, R153-6, R153-7, D227-3. Les versions R153-x historiques ont été listées.
- Tutelle : L151-1, R151-2, R151-4, R151-5, R155-1, R155-3, R226-1, R226-2, R226-4, R224-5, D224-11, R752-3, R752-24, L224-10, L281-1, L281-3, L612-1, L612-2, L612-4, L612-5, L612-5-1, L635-4-1.
- Statuts : L216-1 à L216-4, L281-1 à L281-6, R281-3, R281-6, R231-1 à R231-4, R221-3, R216-1, R216-3, R752-1, et L752-1 dans ses deux versions : LEGIARTI000042684012 (2020→2028) et LEGIARTI000054466934 (2028→, ordonnance 2026-647).

**Pièces scellées lues.**
- `coherence-joint-twelve-readonly-20261025T1915Z/` : REPORT.md, joint-scope.json et joint-answer.json en entier. J'ai exploité whole-joint-current-inputs.json, qui contient les 92 objets d'entrée, par comparaison d'empreintes.
- `coherence-joint-twelve-typed-guard-20261025T2012Z/REPORT.md`.
- Le dossier `joint-staged-live-batches` est un lien non copié. Je ne l'ai pas utilisé : les lots viennent de l'instantané.
- Je n'ai pas lu en production le dossier facultatif `runtime/agrement-four-coherence-preparation-20261025T0801Z`, car l'instantané et les preuves scellées suffisaient. Aucune lecture en production n'a donc eu lieu.

**Autres pièces.**
- Index des contradictions (ligne CSS12).
- `policy-coordinations.json`, empreinte a124c4c3… identique à celle des candidats : `cuts_and_reliefs_2026_10_19/cuts[0]` et `favourable_rules[4]`.
- Dossiers voisins UNION et INST, lus pour ne rien compter deux fois.

## 2. Méthode

1. **Applicabilité.** Pour chaque candidat, j'ai confronté son `source_sha256` et son `previous_draft` (proposition, motif, notes, ligne de lot) au manifeste de l'instantané.
2. **Évolution depuis le 25 octobre.** J'ai comparé les 92 objets scellés au 25 octobre à l'instantané, champ par champ : source, statut, proposition, motif, notes.
3. **Renvois.** J'ai recherché en base, en lecture seule (`mode=ro`, `query_only`), tous les renvois actuels et proposés aux douze articles et aux mécanismes concernés : L153-6, R123-1, R151-1, « équilibre financier des risques », R281-4, R213-5, agrément des conventions.
4. **Contradictions.** Pour chaque mécanisme, j'ai qualifié les contradictions à partir des textes lus en entier, puis vérifié s'il existait une alerte déjà écartée ou un dossier voisin.
5. **Passages.** Tous les passages cités dans le JSON ont été vérifiés par script, comme sous-chaînes exactes des champs de l'instantané ou des candidats scellés.

## 3. Applicabilité des candidats

- **Les candidats s'appliquent encore tous les douze.** Les sources, les propositions de départ, les motifs, les notes et les lignes de lot sont identiques aux empreintes courantes. La seconde passe n'a encore modifié aucun des douze articles : ils sont tous « pending ».
- **Les entrées législatives, en revanche, ont bougé depuis le 25 octobre :**
  - la proposition de L281-6 ne vise plus L216-2 ni L216-4 ;
  - la proposition de L752-1 (version 2020→2028) limite son renvoi à L281-5 et L281-6, et ajoute une transition ultramarine ;
  - les motifs et notes de L612-1 et L612-2 ont changé, ainsi que les notes de L281-2, L281-3, L281-4, L612-5 et L612-5-1.
- Ces évolutions confortent les candidats sans les rendre inapplicables. Les notes des trois candidats statuts sont toutefois périmées (RT-CSS12-11).
- Comme le rappellent les rapports scellés, la préparation de ces candidats n'est ni une intégration ni une lecture native indépendante.

## 4. Constats par mécanisme

### Agrément des conventions
- **RT-CSS12-01 (P1, incohérence du projet, confirmé).**
  - La loi proposée supprime l'agrément : L123-1, L123-2 et L123-2-1, terminés en seconde passe, disent « sont applicables sans agrément », et L224-5-1, L123-2-3 et L153-5 sont coordonnés.
  - Les règlements le maintiennent :
    - R123-1-1, dans sa proposition courante, garde un agrément tacite à un mois ;
    - D224-7 et R152-8 déclarent que « les agréments… demeurent applicables » ;
    - le motif de R123-1 se fonde sur ces agréments.
  - C'est une seule contradiction, comptée une fois. Les candidats R123-1-1, D224-7 et R152-8 la corrigent.
- **RT-CSS12-02 (P1, coordination manquante, confirmé), introduit par le candidat R123-1.** L'abrogation de R123-1 prive R123-54, maintenu, de l'autorité qui fixe la date des élections aux commissions paritaires nationales (« autorité compétente… déterminée conformément à l'article R. 123-1 »). Les notes de R123-56 le relèvent déjà.
- **RT-CSS12-03 (P2, incohérence du projet, confirmé), introduit par le candidat R123-1-1.**
  - Le candidat D224-7 supprime dès le décret l'avis du comité exécutif des directeurs. Le candidat R123-1-1 maintient jusqu'à la loi la source qui exige ce même avis, avec ses prorogations.
  - Il perd ainsi l'allègement intermédiaire que le brouillon courant accordait déjà.
- **RT-CSS12-04 (P2, incohérence du projet, confirmé).** R152-8 est abrogé « à compter de l'entrée en vigueur de la loi » sans désigner cette loi. Le candidat R123-1-1 attribue à tort à la loi la suppression de l'agrément de R152-8, qui est réglementaire.
- **Simple alerte, non comptée.** La « dérogation aux articles L. 123-1 et L. 123-2 » de L224-5-3 devient sans objet une fois l'agrément supprimé. Elle est inoffensive.

### Approbation des statuts
- La contradiction est réelle et déjà établie par le dossier UNION :
  - R216-2 maintenu (RT-UNION-03) ;
  - R281-4, R213-5 et R752-1 maintenus alors que L281-4 est abrogé (RT-UNION-04) ;
  - version 2028 de L752-1 non inventoriée (RT-UNION-05).
- Je ne la recompte pas.
- Les candidats R216-2, R281-4 et R213-5 corrigent RT-UNION-03 et RT-UNION-04 pour la métropole et les URSSAF. Ils ne couvrent ni R752-1 ni la version 2028 de L752-1.
- **RT-CSS12-11 (P2, anomalie d'inventaire, confirmé).** Les notes des trois candidats et de R281-6 décrivent un état de L281-6 ou de R281-4 périmé.
- Les candidats ne créent aucune formalité de remplacement. Ils préservent les approbations expresses et tacites acquises, et ne régularisent aucune illégalité.

### Nomination
- D224-8 et D227-5 (avis de nomination de l'Institut) relèvent de **RT-INST-01**, qui en traite. Je ne les recompte pas.
- Le candidat D224-8 s'applique toujours aux empreintes courantes.
- R612-7, dernier alinéa (avis du CPSTI sous onze jours), est conservé à l'identique par le candidat : pas de constat.

### Opposition
- **RT-CSS12-05 (P2, incohérence du projet, confirmé).** Le deuxième alinéa de R153-2, maintenu, désigne l'autorité de l'opposition de L153-6, que la loi proposée abroge. Le candidat le corrige.
- **RT-CSS12-08 (P2, incohérence du projet, confirmé).**
  - R612-7, maintenu, garde « L'opposition prévue à l'article L. 224-10 est exercée par ces mêmes ministres » pour le CPSTI.
  - Or L224-10 proposé rend les délibérations nouvelles exécutoires dès leur adoption, et R226-4, R224-5 et D224-11 sont déjà coordonnés.
  - Le candidat corrige l'écart sans rétablir l'approbation des orientations supprimée par L612-1. Le calendrier de L224-10 et D227-6 relève de RT-TUT.

### Budget
- Aucune contradiction.
- L153-2 maintenu (approbation par l'organisme national) et le premier alinéa de R153-2 (approbation des établissements par l'ARS), conservé à l'identique par le candidat, sont cohérents entre eux.
- L153-5 est déjà coordonné avec la fin de l'agrément.
- D227-3 (budget de l'Institut approuvé par l'Union) est maintenu. Il relève des dossiers INST et TUT.

### Tutelle
- **RT-CSS12-06 (P1, incohérence du projet, confirmé).**
  - R151-1 (troisième alinéa) et R151-3 (deuxième alinéa), maintenus, organisent la suspension pour risque financier et la confirmation nationale que L151-1 proposé supprime.
  - Ce serait un pouvoir de tutelle réglementaire sans base légale.
  - Les candidats le corrigent et conservent à l'identique la légalité, les huit et quarante jours et les délais francs.
- **RT-CSS12-07 (P2, coordination manquante, confirmé).** Le paquet des douze est incomplet :
  - R226-2 proposé organise encore la saisine de la caisse nationale après suspension financière ;
  - R226-1 renvoie au « troisième alinéa » de R151-1, qui deviendrait l'alinéa transitoire ;
  - R752-24 affirme un « contrôle financier prévu par L. 151-1 » qui disparaît.
- **RT-CSS12-09 (alerte écartée).** J'ai examiné le risque de vide de tutelle financière sur des organismes gérant des fonds publics.
  - La fonction reste assurée : approbation des budgets (L153-2), établissement et inscription d'office (L153-4, L153-5, R153-7), annulation pour illégalité (R151-1), contrôle sur pièces et sur place (R155-1, R155-3), mesures de crise (L281-1 à L281-3), Cour des comptes.
  - Pour le CPSTI : plafond ministériel des aides (L612-5), certification des comptes (L612-5-1), gestion des réserves par l'ACOSS (L635-4-1).
  - Une réserve résiduelle reste à confirmer. Au niveau national, aucun texte lu ne donne à l'État un pouvoir administratif d'annuler une délibération illégale isolée. Elle est signalée à RT-TUT, sans être comptée.

### Compétence de la loi et du règlement
- **RT-CSS12-10 (alerte écartée).** Aucun candidat n'abroge une exigence législative par règlement avant la loi.
- Chaque retrait d'un circuit législatif est ancré sur la date de la loi correspondante. Seules des formalités réglementaires sont retirées à la date du décret.
- Le vrai risque est inverse : des règlements maintenus conservent des exigences que la loi supprime. Il est compté en RT-CSS12-01, -05, -06, -08, et pour les statuts en RT-UNION-03 et RT-UNION-04.

## 5. Verdict sur les douze candidats

| Candidat | Corrige un problème démontré ? | Verdict |
|---|---|---|
| R123-1 | Oui, en partie : motif contradictoire (RT-CSS12-01) | **Introduit un problème** (RT-CSS12-02). À remplacer par la réécriture de C2. |
| R123-1-1 | Oui (RT-CSS12-01, P1) | Utile, mais **introduit un problème de calendrier** (RT-CSS12-03) et une attribution inexacte (RT-CSS12-04). À amender. |
| D224-7 | Oui (réserve déclarative contraire à la loi, RT-CSS12-01) | Utile, portée limitée. À adopter. |
| R152-8 | Oui (même réserve, RT-CSS12-01) | Utile. À adopter en précisant la loi visée (RT-CSS12-04). |
| D224-8 | Voir RT-INST-01 | Non évalué ici. Il s'applique toujours. |
| R153-2 | Oui (RT-CSS12-05) | Utile. À adopter tel quel. |
| R151-1 | Oui (RT-CSS12-06, P1) | Utile. À adopter, et à compléter par RT-CSS12-07. |
| R151-3 | Oui (RT-CSS12-06, P1) | Utile. À adopter en retirant les `<br />` hérités de la source. |
| R612-7 | Oui (RT-CSS12-08) | Utile. À adopter. |
| R216-2 | Oui (RT-UNION-03) | Utile. Notes à mettre à jour (RT-CSS12-11). |
| R281-4 | Oui (RT-UNION-04) | Utile. Ne couvre pas R752-1. Notes à mettre à jour. |
| R213-5 | Oui (RT-UNION-04, volet URSSAF) | Utile. Notes à mettre à jour. |

Aucun candidat n'est obsolète ni inutile. Les candidats D224-7 et R152-8 ont une faible portée normative : la loi prime de toute façon. Ils restent nécessaires à la cohérence du projet.

## 6. Propositions de correction (séparées des constats)

**C1, pour RT-CSS12-01.**
- Adopter les candidats R123-1-1 (avec C3 et C4), D224-7 et R152-8 (avec C4).
- Pour R123-1, adopter C2.
- Remplacer le motif courant de R123-1.
- Dépendances : L123-1, L123-2 et L123-2-1 proposés ; ancrage sur la même loi.

**C2, pour RT-CSS12-02. R123-1, rédaction complète :**
> L'autorité compétente de l'Etat mentionnée à l'article R. 123-54 est le ministre chargé de la sécurité sociale et, pour les organismes de mutualité sociale agricole, le ministre chargé de l'agriculture.
>
> À compter de l'entrée en vigueur de la loi supprimant l'agrément prévu aux articles L. 123-1, L. 123-2 et L. 123-2-1, la présente désignation ne permet d'exiger aucun agrément, avis ou déclaration au titre de ces articles, y compris pour les conventions et avenants dont l'examen est en cours ou qui n'ont pas encore été déposés. Les agréments acquis, les refus devenus définitifs et les recours relatifs aux périodes antérieures sont préservés.

Justification : cette rédaction garde l'autorité électorale, supprime l'agrément et ne crée aucune formalité. Autre possibilité : désigner directement les ministres dans R123-54, puis abroger R123-1.

**C3, pour RT-CSS12-03. Alinéa à insérer en tête du candidat R123-1-1 :**
> Jusqu'à la date mentionnée à l'alinéa suivant, l'agrément des accords d'entreprise et des décisions mentionnées à l'article R. 152-8 n'est subordonné à aucun avis préalable obligatoire ; ces actes sont réputés agréés si le ministre compétent n'a pas notifié une décision expresse dans le délai d'un mois à compter de leur réception par ses services ; ce délai ne peut être ni prorogé ni renouvelé ; aucun agrément tacite déjà acquis ni aucune date plus favorable n'est reporté.

Dépendance : la date d'entrée en vigueur du décret ; voir aussi RT-TUT pour le calendrier général.

**C4, pour RT-CSS12-04.**
- R152-8 : écrire « à compter de la date d'entrée en vigueur de la loi portant la suppression de l'agrément prévue aux articles L. 123-1, L. 123-2 et L. 123-2-1 ».
- Candidat R123-1-1 : remplacer « , qui supprime également l'agrément des décisions mentionnées à l'article R. 152-8 » par « ainsi que de l'abrogation de l'article R. 152-8 ».

**C5, pour RT-CSS12-05.** Adopter le candidat R153-2 tel quel.

**C6, pour RT-CSS12-06.** Adopter les candidats R151-1 et R151-3, après avoir retiré les balises `<br />` de R151-3.

**C7, pour RT-CSS12-07.**
- R226-2 : ajouter « Le présent article cesse de s'appliquer à compter de l'entrée en vigueur de la suppression du circuit de suspension pour risque financier prévue à l'article L. 151-1 ; les saisines déjà effectuées sont closes sans décision nationale, conformément à cet article. »
- R226-1, dernier 2° : écrire « pour l'application de l'article R. 151-1 dans sa rédaction antérieure à la suppression du circuit de suspension pour risque financier, compte tenu de la nature du risque en cause ».
- R752-24 : écrire « au contrôle de légalité prévu par les articles L. 151-1 et R. 151-1 ».

**C8, pour RT-CSS12-08.** Adopter le candidat R612-7.

**C9, pour RT-CSS12-11.** Mettre à jour les notes des candidats R216-2, R281-4 et R213-5, ainsi que celles de R281-6, à l'état courant de L281-6 et L752-1. Pour R752-1 et la version 2028 de L752-1, appliquer les corrections C4 et C5 du dossier UNION.

**À préserver dans toutes les corrections :**
- la suppression des agréments, approbations, oppositions et suspensions financières demandée par la réforme, sans aucune formalité de remplacement ;
- les agréments et approbations expresses ou tacites déjà acquis, les refus et annulations définitifs, ainsi que les droits, engagements et recours antérieurs ;
- le contrôle de légalité et ses délais : huit et quarante jours, délais francs ;
- l'approbation budgétaire, les inscriptions d'office et les mesures de crise ;
- l'opposition interne des trois quarts à l'UCANSS ;
- les modèles de L281-5 ;
- l'avis de onze jours du CPSTI ;
- les élections paritaires.

Aucune contribution, exonération, prestation ni règle du contrat unique n'est touchée par ces coordinations.

## 7. Incertitudes et éléments non examinés

- **Textes hors corpus, non lus :**
  - code rural, notamment un éventuel agrément propre aux accords de la MSA ;
  - décret d'application de L153-6 ;
  - CASF L312-1 ;
  - L226-4 ;
  - arrêtés de modèles de statuts et arrêtés pris sur R155-3 ;
  - décret 97-464 ;
  - L224-5-4 et L224-9, connus seulement par les notes de L281-3 ;
  - règles de placement de R139-1 et suivants, non relues en entier.
- **Hors périmètre :**
  - D224-8, D227-5 et la note de L228-1 relèvent de RT-INST ;
  - D227-6, L224-10 et leurs calendriers relèvent de RT-TUT ;
  - les catégories de L281-6 et le double avis relèvent de RT-UNION-02.
- Les dates réelles des futurs textes ne sont pas connues.
- Aucune source primaire n'a été consultée en ligne : toutes les références sont des identifiants LEGI lus dans le corpus local au 18 octobre 2026.
- La seconde passe peut encore modifier les articles « pending », dont les douze candidats et R123-54, R226-1, R226-2 et R752-24.

## 8. Résumé

Onze objections sont recensées dans CSS12.json.

| Priorité | Nombre | Statut |
|---|---|---|
| P1 | 3 | confirmées |
| P2 | 8 | 6 confirmées, 2 faux positifs (alertes écartées) |

Couverture : les douze candidats et environ 75 articles liés, lus en entier dans l'instantané. Les renvois ont été recherchés sur tout le CSS en vigueur.
