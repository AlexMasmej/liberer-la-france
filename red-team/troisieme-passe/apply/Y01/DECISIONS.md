# Y01 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-Y01.json`, soit 52 articles du CSS et 57 pistes (48 S9, 9 S10). Contrôle : `python3 -B apply/check_changes.py Y01` donne 2 lignes construites, 2 validées et `problems` vide. Les diagnostics sont voulus : réductions déclarées, renvois ajoutés (L356-3 pour D356-2, L138-15 pour R138-10) et longueur de R138-10.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes du paquet | Constats connexes |
|---|---|---|
| G | 1 (R138-10), corrigé | 1 (D356-2, 4° conjugal), corrigé |
| m | 0 | 1 (motif tronqué de R252-29), non corrigé |
| déjà réglé | 35 | |
| faux positif | 21 | |

Corrections : 2 lignes en mode `replace`, D356-2 et R138-10. Aucune demande à un autre groupe, rien d'écarté (`skipped` vide).

## Défauts confirmés et corrigés

- **R138-10** (LEGIARTI000028093189), piste S9 vers L138-15, G (F1 et F4), corrigé.
  - Défaut : la proposition impose sans limite de temps la déclaration du chiffre d'affaires « conformément au I de l'article L. 138-15 ». Or la version de L138-15 applicable au 1er janvier 2027 (LEGIARTI000051287301), que le projet accepte (RT-FUTCSS-06), remplace cette déclaration par la transmission du montant remboursé par la CNAM, l'ATIH et l'ANSP. Le décret aurait maintenu une formalité que la loi supprime.
  - Correction : un alinéa final borne l'article aux contributions régies par la rédaction de L138-15 antérieure à la loi n° 2023-1250, sur le modèle exact des propositions de L138-15 et L138-11. Il précise qu'aucune déclaration n'est exigée pour les contributions régies par la rédaction de 2027. Le reste du corps est inchangé. La note fausse (« versions différées de 2027 non reproduites ») est corrigée.
- **D356-2** (LEGIARTI000023413984), constat connexe relevé à la lecture de la piste S9 (L356-1), G (F5 et F1), corrigé.
  - Défaut : le 4° (« Ne pas être remarié, ne pas avoir conclu de pacte civil de solidarité et ne pas vivre en concubinage ») contredit L356-3 proposé (1° abrogé, nouvelle union sans effet à elle seule). Il contredit aussi D356-11 et D356-12 proposés, qui ont déjà retiré leurs renvois à ce 4°.
  - Correction : le 4° devient « Abrogé » et garde sa place, pour ne pas décaler les renvois de D356-11 et D356-12. La transition de L356-3 est reprise : périodes nouvelles, même si le décès ou l'union est antérieur ; les périodes passées et les décisions définitives sont conservées. Les 1° à 3°, la suppression de la forclusion et sa transition sont inchangés. Le motif « Les quatre conditions » est corrigé.

## Points laissés à l'auteur

- R138-10 : la frontière entre contributions « régies par la rédaction antérieure » et contributions régies par celle de 2027 reprend la formule des propositions de L138-15 et L138-11. Les notes de L138-15 (2027) indiquent que les années concernées ne sont pas établies avec certitude.
- D356-2 : la décision de fond (fin de l'exclusion pour nouvelle union) est celle de L356-3 proposé. La correction ne fait que l'aligner.
- Hors paquet, signalé par les notes du projet et non vérifié ici : R922-32 (circuit d'approbation des modifications statutaires, voir les notes de L922-6) et D432-5 (avis conforme, voir les notes de L432-10). Leur propriétaire n'est pas désigné dans `assignment.json`. R582-5 et R148-1/R148-3, également cités par ces notes, relèvent des groupes Y03 et Y02.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| D162-18 (LEGIARTI000006735376) | S9/F1+F5 | L162-31 | déjà réglé | non |
| D162-20 (LEGIARTI000006735380) | S9/F1+F5 | L162-31 | déjà réglé | non |
| D324-1 (LEGIARTI000006736473) | S9/F1+F5 | L324-1 | déjà réglé | non |
| D412-71 (LEGIARTI000006736815) | S9/F1+F5 | L461-5 | faux positif | non |
| D412-14 (LEGIARTI000006736890) | S9/F1+F5 | L441-2 | déjà réglé | non |
| D412-35 (LEGIARTI000006736934) | S9/F1+F5 | L461-5 | faux positif | non |
| D461-8 (LEGIARTI000006737056) | S9/F1+F5 | L461-5 | déjà réglé | non |
| D461-14 (LEGIARTI000006737075) | S9/F1+F5 | L461-5 | faux positif | non |
| D461-16 (LEGIARTI000006737082) | S9/F1+F5 | L461-5 | faux positif | non |
| L224-5-3 (LEGIARTI000006742284) | S10/F5 (échantillon) | L123-2 | faux positif | non |
| L432-8 (LEGIARTI000006743036) | S10/F5 (échantillon) | L432-9 | faux positif | non |
| R138-21 (LEGIARTI000006747133) | S9/F1+F5 | L138-20 | déjà réglé | non |
| R138-23 (LEGIARTI000006747135) | S9/F1+F5 | L138-20 | déjà réglé | non |
| R173-18 (LEGIARTI000006747888) | S10/F5 (échantillon) | L161-21 | faux positif | non |
| R245-4 (LEGIARTI000006748874) | S9/F1+F5 | L245-6 | déjà réglé | non |
| R245-4 (LEGIARTI000006748874) | S9/F1+F5 | L138-20 | déjà réglé | non |
| R252-29 (LEGIARTI000006748964) | S10/F5 (échantillon) | L212-1 | faux positif | non |
| R315-1-3 (LEGIARTI000006749191) | S9/F1+F5 | L315-2 | déjà réglé | non |
| R315-7 (LEGIARTI000006749198) | S9/F1+F5 | L145-7 | faux positif | non |
| R441-4 (LEGIARTI000006750407) | S9/F1+F5 | L441-2 | déjà réglé | non |
| R441-5 (LEGIARTI000006750408) | S9/F1+F5 | L441-2 | déjà réglé | non |
| R442-1 (LEGIARTI000006750430) | S9/F1+F5 | L441-2 | faux positif | non |
| R444-1 (LEGIARTI000006750459) | S9/F1+F5 | L441-2 | déjà réglé | non |
| R461-6 (LEGIARTI000006750483) | S9/F1+F5 | L461-5 | déjà réglé | non |
| R471-3 (LEGIARTI000006750491) | S9/F1+F5 | L441-4 | faux positif | non |
| R581-4 (LEGIARTI000006750781) | S9/F1+F5 | L582-1 | faux positif | non |
| R581-5 (LEGIARTI000006750782) | S9/F1+F5 | L582-1 | faux positif | non |
| R922-7 (LEGIARTI000006754722) | S9/F1+F5 | L922-6 | déjà réglé | non |
| R133-42 (LEGIARTI000018503702) | S9/F1+F5 | L133-9-1 | déjà réglé | non |
| R255-5 (LEGIARTI000020882557) | S9/F1+F5 | L225-1-3 | faux positif | non |
| R713-18 (LEGIARTI000021740681) | S9/F1+F5 | L713-21 | déjà réglé | non |
| R162-54-3 (LEGIARTI000022284594) | S9/F1+F5 | L162-33 | déjà réglé | non |
| R162-54-1 (LEGIARTI000022284634) | S9/F1+F5 | L162-33 | déjà réglé | non |
| D356-2 (LEGIARTI000023413984) | S9/F1+F5 | L356-1 | déjà réglé | non |
| R148-4 (LEGIARTI000024045206) | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| D454-1 (LEGIARTI000026510732) | S9/F1+F5 | L454-1 | déjà réglé | non |
| D454-1 (LEGIARTI000026510732) | S10/F5 (échantillon) | L454-1 | faux positif | non |
| R815-44 (LEGIARTI000026618365) | S10/F5 (échantillon) | L815-13 | déjà réglé | non |
| R138-10 (LEGIARTI000028093189) | S9/F1+F5 | L138-15 | G | oui |
| Annexe I à l'art. R434-32 (1) (LEGIARTI000028674637) | S9/F1+F5 | L443-1 | déjà réglé | non |
| R322-10-4 (LEGIARTI000028987742) | S9/F1+F5 | L160-14 | déjà réglé | non |
| R123-1 (LEGIARTI000029389194) | S9/F1+F5 | L123-1 | déjà réglé | non |
| R123-1 (LEGIARTI000029389194) | S9/F1+F5 | L123-2 | déjà réglé | non |
| R123-1 (LEGIARTI000029389194) | S9/F1+F5 | L123-2-1 | déjà réglé | non |
| D351-14-2 (LEGIARTI000030075867) | S10/F5 (échantillon) | L351-14-1 | faux positif | non |
| R138-3 (LEGIARTI000030305810) | S9/F1+F5 | L138-9-1 | déjà réglé | non |
| R138-24-1 (LEGIARTI000031093023) | S9/F1+F5 | L138-20 | faux positif | non |
| R165-7-1 (LEGIARTI000031604259) | S9/F1+F5 | L165-1 | faux positif | non |
| R162-1-9 (LEGIARTI000031828614) | S9/F1+F5 | L162-1-15 | faux positif | non |
| R114-18 (LEGIARTI000031828742) | S9/F1+F5 | L165-1 | faux positif | non |
| R862-11-4 (LEGIARTI000032156084) | S9/F1+F5 | L862-4 | déjà réglé | non |
| R174-20 (LEGIARTI000034623669) | S9/F1+F5 | L174-18 | déjà réglé | non |
| D225-2 (LEGIARTI000034623787) | S9/F1+F5 | L225-1-3 | déjà réglé | non |
| D225-2 (LEGIARTI000034623787) | S9/F1+F5 | L225-1-4 | déjà réglé | non |
| D162-30 (LEGIARTI000034731961) | S9/F1+F5 | L162-5-14-2 | déjà réglé | non |
| R932-4-4-3 (LEGIARTI000036330368) | S10/F5 (échantillon) | R932-4-15 | faux positif | non |
| L612-2 (LEGIARTI000036391005) | S10/F5 (échantillon) | L231-6-1 | déjà réglé | non |
| D356-2 (LEGIARTI000023413984) | F5+F1 | L356-3 | G | oui |
| R252-29 (LEGIARTI000006748964) | F10 | — | m | non |

## Motifs des qualifications

- **D162-18 → L162-31** (S9/F1+F5, déjà réglé) : D162-18 proposé (LEGIARTI000006735376) : « menées dans le cadre de l'article L. 162-31 » remplace « agréées conformément » et « les conventions mentionnées au présent article ne sont subordonnées ni à cet agrément ni à cette approbation » ; l'agrément ne figure plus que dans la transition.
- **D162-20 → L162-31** (S9/F1+F5, déjà réglé) : D162-20 proposé (LEGIARTI000006735380) : « la personne physique ou morale qui mène l'action expérimentale » remplace « titulaire de l'agrément » ; « aucun agrément particulier de l'action ni déclaration de remplacement n'est exigé ».
- **D324-1 → L324-1** (S9/F1+F5, déjà réglé) : D324-1 proposé (LEGIARTI000006736473) : « Il n'est tenu d'attester ni la prise de connaissance du protocole ni, par une attestation distincte, la conformité de ces prescriptions au protocole », conforme à L324-1 proposé (LEGIARTI000041399098).
- **D412-71 → L461-5** (S9/F1+F5, faux positif) : D412-71 proposé (LEGIARTI000006736815) réduit le certificat final à « un seul exemplaire » ; L461-5 proposé (LEGIARTI000036393199) ne régit que le certificat initial (« Un seul exemplaire de ce certificat complète la déclaration ») : aucune formalité retirée n'est rétablie.
- **D412-14 → L441-2** (S9/F1+F5, déjà réglé) : D412-14 proposé (LEGIARTI000006736890) : « Le directeur bénéficie de la dispense de seconde déclaration prévue à l'article L. 441-2 », avec la réserve d'aggravation de L441-4.
- **D412-35 → L461-5** (S9/F1+F5, faux positif) : D412-35 proposé (LEGIARTI000006736934) : certificat final « établi en un seul exemplaire par le médecin » ; la déclaration de L461-5 subsiste dans la loi proposée (« doit être, par les soins de la victime, déclarée à la caisse primaire ») ; rien de retiré n'est rétabli.
- **D461-8 → L461-5** (S9/F1+F5, déjà réglé) : D461-8 proposé (LEGIARTI000006737056) : « y compris lorsqu'une demande expresse de réparation déjà transmise vaut déclaration en application de cet article » ; aucun second dépôt.
- **D461-14 → L461-5** (S9/F1+F5, faux positif) : D461-14 maintenu (LEGIARTI000006737075) : « Au dépôt de la déclaration prévue à l'article D. 461-8 » et « certificat descriptif mentionné à l'article L. 461-5 » ; la déclaration et le certificat subsistent dans L461-5 proposé, seuls la seconde déclaration et les exemplaires multiples sont retirés, et D461-8 proposé assimile la demande expresse à cette déclaration.
- **D461-16 → L461-5** (S9/F1+F5, faux positif) : D461-16 maintenu (LEGIARTI000006737082) : « En cas de décès de la victime avant la déclaration de maladie prévue à l'article L. 461-5 » ; simple repère temporel, la déclaration subsiste dans L461-5 proposé.
- **L224-5-3 → L123-2** (S10/F5 (échantillon), faux positif) : L224-5-3 proposé (LEGIARTI000006742284) : « Par dérogation aux articles L. 123-1 et L. 123-2, ... s'appliquent de plein droit » ; L123-2 proposé (LEGIARTI000037948868) rend les conventions « applicables sans agrément » mais conserve l'agrément pour les périodes antérieures (« Les conventions déjà applicables ... sont préservés ») : la dérogation garde un objet transitoire et ne contredit pas la cible. Redondance pour l'avenir, sans effet.
- **L432-8 → L432-9** (S10/F5 (échantillon), faux positif) : L432-8 proposé (LEGIARTI000006743036) : « sans préjudice des dispositions des articles L. 432-9 et L. 432-10 » ; L432-9 proposé (LEGIARTI000006743038) conserve le droit « d'être admise gratuitement dans un établissement ... de rééducation professionnelle », seul l'examen psychotechnique systématique est retiré.
- **R138-21 → L138-20** (S9/F1+F5, déjà réglé) : R138-21 proposé (LEGIARTI000006747133) : « Ce renvoi ne rétablit aucune contribution, déclaration, majoration ou pénalité supprimée » ; L138-20 proposé (LEGIARTI000051287267) supprime la seule majoration de support.
- **R138-23 → L138-20** (S9/F1+F5, déjà réglé) : R138-23 proposé (LEGIARTI000006747135) : « Aucune évaluation ni demande de données ne peut porter sur les charges ou années pour lesquelles la contribution concernée est supprimée » et « ne rétablit aucune majoration ni pénalité supprimée ».
- **R173-18 → L161-21** (S10/F5 (échantillon), faux positif) : R173-18 proposé (LEGIARTI000006747888) vise « au cinquième alinéa de l'article L. 161-21 » : dans L161-21 proposé (LEGIARTI000006741253), le cinquième alinéa reste « Les premier, deuxième et troisième alinéas s'appliquent aux assurés des régimes d'assurance vieillesse » ; la règle subsidiaire suit la suppression de la condition de succession.
- **R245-4 → L245-6** (S9/F1+F5, déjà réglé) : R245-4 proposé (LEGIARTI000006748874) : « ils restent applicables aux contributions prévues à l'article L. 245-6 légalement dues au titre des années civiles antérieures à leur suppression » et « Aucun de ces renvois ne rétablit une contribution ».
- **R245-4 → L138-20** (S9/F1+F5, déjà réglé) : R245-4 proposé (LEGIARTI000006748874) : « la majoration pour emploi d'une voie autre que dématérialisée supprimée à l'article L. 138-20 ne peut être rétablie ».
- **R252-29 → L212-1** (S10/F5 (échantillon), faux positif) : R252-29 proposé (LEGIARTI000006748964) : « Sans préjudice des mesures prévues à l'article L. 271-1, les organismes et services autorisés par les dispositions réglementaires prises en application de l'article L. 212-1 » ; L212-1 proposé (LEGIARTI000031686187) conserve « un décret peut autoriser certains organismes ou services ».
- **R315-1-3 → L315-2** (S9/F1+F5, déjà réglé) : R315-1-3 proposé (LEGIARTI000006749191) : « l'absence d'un accord préalable qui n'est plus exigé en application de cet article ne peut fonder une suspension » ; L315-2 proposé (LEGIARTI000048687768) exclut les seuls motifs économiques.
- **R315-7 → L145-7** (S9/F1+F5, faux positif) : R315-7 maintenu (LEGIARTI000006749198) : « déclaration ... mentionnant ses liens directs ou indirects » des praticiens-conseils ; L145-7 proposé (LEGIARTI000038888229) retire seulement la « consultation de l'ordre » sur l'arrêté indemnitaire : formalités distinctes.
- **R441-4 → L441-2** (S9/F1+F5, déjà réglé) : R441-4 proposé (LEGIARTI000006750407) : « Lorsque l'employeur est dispensé de la déclaration en application de l'article L. 441-2, les seules informations restant à communiquer sont transmises » ; « aucune attestation distincte n'est exigée ».
- **R441-5 → L441-2** (S9/F1+F5, déjà réglé) : R441-5 proposé (LEGIARTI000006750408) : « sous réserve de la dispense prévue à l'article L. 441-2 lorsque la déclaration de la victime ... porte également sur l'arrêt de travail ou les soins médicaux survenus ultérieurement ».
- **R442-1 → L441-2** (S9/F1+F5, faux positif) : R442-1 proposé (LEGIARTI000006750430) : « dès qu'elle a connaissance de l'accident par la déclaration prévue à l'article L. 441-2 ou par quelque moyen que ce soit » ; mode de connaissance, aucune déclaration imposée.
- **R444-1 → L441-2** (S9/F1+F5, déjà réglé) : R444-1 proposé (LEGIARTI000006750459) : « Les déclarations mentionnées au présent article ne sont exigées que sous réserve de la dispense de seconde déclaration prévue au premier alinéa de l'article L. 441-2 ».
- **R461-6 → L461-5** (S9/F1+F5, déjà réglé) : R461-6 proposé (LEGIARTI000006750483) : triple exemplaire limité au certificat final ; « Le nombre d'exemplaires du certificat initial demeure régi par ce dernier article » ; « aucune attestation distincte » pour les informations salariales.
- **R471-3 → L441-4** (S9/F1+F5, faux positif) : R471-3 maintenu (LEGIARTI000006750491) sanctionne le défaut d'inscription « sur le registre ouvert à cet effet » ; L441-4 proposé (LEGIARTI000042686351) conserve le registre et retire seulement les conditions d'accès et l'information de la CARSAT ; le premier alinéa de L441-2 proposé intègre la dispense de seconde déclaration, qui n'est donc pas sanctionnée.
- **R581-4 → L582-1** (S9/F1+F5, faux positif) : R581-4 proposé (LEGIARTI000006750781) : notification d'admission au recouvrement par lettre recommandée ; L582-1 proposé (LEGIARTI000044629452) retire la pénalité de non-transmission, non cette notification ; réserve d'intermédiation déjà ajoutée.
- **R581-5 → L582-1** (S9/F1+F5, faux positif) : R581-5 proposé (LEGIARTI000006750782) : notification de l'apurement « sous réserve des obligations résultant de l'intermédiation financière prévue à l'article L. 582-1 » ; sans lien avec la pénalité retirée.
- **R922-7 → L922-6** (S9/F1+F5, déjà réglé) : R922-7 proposé (LEGIARTI000006754722) : « Les modifications des statuts et du règlement de la fédération sont dispensées d'approbation ministérielle dans les conditions et selon les dispositions transitoires de l'article L. 922-6 » ; l'approbation initiale subsiste comme dans L922-6 proposé.
- **R133-42 → L133-9-1** (S9/F1+F5, déjà réglé) : R133-42 proposé (LEGIARTI000018503702) : « Les conventions ne sont soumises à aucune homologation particulière ... à compter de l'entrée en vigueur de la disposition législative supprimant l'homologation » ; l'homologation n'est maintenue que « Jusqu'à cette date » (transition).
- **R255-5 → L225-1-3** (S9/F1+F5, faux positif) : R255-5 maintenu (LEGIARTI000020882557) : « Les conventions conclues en application de l'article L. 225-1-3 fixent notamment les conditions tarifaires du dépôt » ; aucune approbation n'y est organisée.
- **R713-18 → L713-21** (S9/F1+F5, déjà réglé) : R713-18 proposé (LEGIARTI000021740681) : « la convention prévue à cet alinéa et ses avenants ne sont pas soumis à l'approbation de ces ministres » ; seule l'approbation du budget, conservée par L713-21 proposé, reste visée.
- **R162-54-3 → L162-33** (S9/F1+F5, déjà réglé) : R162-54-3 proposé (LEGIARTI000022284594) : « 3° Aucune ancienneté minimale à compter du dépôt légal des statuts n'est exigée ».
- **R162-54-1 → L162-33** (S9/F1+F5, déjà réglé) : R162-54-1 proposé (LEGIARTI000022284634) : « 3° Aucune ancienneté minimale à compter du dépôt légal des statuts n'est exigée ».
- **D356-2 → L356-1** (S9/F1+F5, déjà réglé) : D356-2 proposé (LEGIARTI000023413984) : « Aucun délai de forclusion à compter du décès n'est opposable à la demande » ; le dépôt n'est plus enfermé dans un délai, conforme à L356-1 proposé (LEGIARTI000023034909).
- **R148-4 → L162-1-15** (S9/F1+F5, déjà réglé) : R148-4 proposé (LEGIARTI000024045206) : « la présente procédure ne peut être engagée ou poursuivie pour les actes, prescriptions et prestations futurs sur le seul fondement de ces motifs ».
- **D454-1 → L454-1** (S9/F1+F5, déjà réglé) : D454-1 proposé (LEGIARTI000026510732) : « Aucune attestation d'envoi par une autre personne n'est exigée au titre de cette dispense » et IV « Aucune indemnité forfaitaire de gestion ne naît ».
- **D454-1 → L454-1** (S10/F5 (échantillon), faux positif) : D454-1 proposé vise « la dispense prévue au cinquième alinéa de l'article L. 454-1 » : dans L454-1 proposé (LEGIARTI000036393227), le cinquième alinéa contient bien « L'information effectivement reçue par la caisse de l'une de ces personnes satisfait, pour les autres, à cette obligation ».
- **R815-44 → L815-13** (S10/F5 (échantillon), déjà réglé) : R815-44 proposé (LEGIARTI000026618365) : « La réserve relative à l'article L. 815-13 ne concerne que les décès antérieurs à l'entrée en vigueur de la loi supprimant la récupération sur succession » ; cohérent avec l'abrogation proposée de L815-13 (LEGIARTI000048697753).
- **R138-10 → L138-15** (S9/F1+F5, G) : F1+F4. R138-10 proposé (LEGIARTI000028093189) impose sans limite de temps : « sont tenues de remettre ... la déclaration ... permettant de déterminer le chiffre d'affaires ... avant le 1er avril de l'année suivante, conformément au I de l'article L. 138-15 ». La version cible (LEGIARTI000046805500) conserve cette déclaration, mais elle prend fin le 1er janvier 2027 ; la version suivante de L138-15 (LEGIARTI000051287301, VIGUEUR_DIFF 2027), acceptée par le projet (objection RT-FUTCSS-06), confie au I la transmission du « montant total remboursé par l'assurance maladie » à la CNAM, l'ATIH et l'ANSP et ne prévoit plus de déclaration de l'entreprise ; L138-11 (LEGIARTI000048688952) et L138-12 (LEGIARTI000053282649) de 2027 assoient la contribution sur ce montant. Le décret aurait maintenu une formalité que la loi supprime. Correction : bornage aux contributions régies par la rédaction de L138-15 antérieure à la loi n° 2023-1250, sur le modèle des propositions de L138-15 et L138-11.
- **Annexe I à l'art. R434-32 (1) → L443-1** (S9/F1+F5, déjà réglé) : Annexe I à R434-32 proposée (LEGIARTI000028674637) : « Cet intervalle n'est pas opposable à une demande de la victime tendant à l'augmentation des réparations » ; conforme à L443-1 proposé (LEGIARTI000026799850 et sa version suivante LEGIARTI000051288476).
- **R322-10-4 → L160-14** (S9/F1+F5, déjà réglé) : R322-10-4 proposé (LEGIARTI000028987742) : « n'est plus subordonnée à l'accord préalable » ; pour le f, entrée en vigueur « à la même date que la suppression de l'accord préalable propre au 19° de l'article L. 160-14 ».
- **R123-1 → L123-1** (S9/F1+F5, déjà réglé) : R123-1 proposé (LEGIARTI000029389194) : « Cette désignation ne soumet à aucun agrément les conventions collectives relevant des articles L. 123-1, L. 123-2 et L. 123-2-1 ».
- **R123-1 → L123-2** (S9/F1+F5, déjà réglé) : Même passage de R123-1 proposé (LEGIARTI000029389194) ; L123-2 proposé (LEGIARTI000037948868) : « applicables sans agrément ».
- **R123-1 → L123-2-1** (S9/F1+F5, déjà réglé) : Même passage de R123-1 proposé (LEGIARTI000029389194) ; L123-2-1 proposé (LEGIARTI000036391616) retire l'agrément.
- **D351-14-2 → L351-14-1** (S10/F5 (échantillon), faux positif) : D351-14-2 proposé (LEGIARTI000030075867) : « En application du III de l'article L. 351-14-1 » ; le III de L351-14-1 proposé (LEGIARTI000047452730) conserve la réduction pour les assistants maternels de 1975 à 1990 ; seule la catégorie d'établissements du 1° est retirée.
- **R138-3 → L138-9-1** (S9/F1+F5, déjà réglé) : R138-3 proposé (LEGIARTI000030305810) : III « aucune pénalité ne peut être prononcée au seul motif du support utilisé » et non-reconduction annuelle, conformes à L138-9-1 proposé (LEGIARTI000051287416).
- **R138-24-1 → L138-20** (S9/F1+F5, faux positif) : R138-24-1 proposé (LEGIARTI000031093023) maintient la voie dématérialisée que L138-20 proposé conserve (« Les déclarations et versements afférents à ces contributions sont effectués par voie dématérialisée ») ; seules la majoration de support et l'exclusivité du virement sont retirées.
- **R165-7-1 → L165-1** (S9/F1+F5, faux positif) : R165-7-1 proposé (LEGIARTI000031604259) : déclaration de conformité aux spécifications techniques de la description générique renforcée ; L165-1 proposé (LEGIARTI000046822845) retire la certification promotionnelle et la déclaration sur l'honneur d'absence de promotion : formalités distinctes.
- **R162-1-9 → L162-1-15** (S9/F1+F5, faux positif) : R162-1-9 proposé (LEGIARTI000031828614) organise les observations et l'audition avant mise sous accord préalable, procédure conservée pour le 1° de L162-1-15 proposé (LEGIARTI000054335791) ; aucun motif statistique n'est rétabli.
- **R114-18 → L165-1** (S9/F1+F5, faux positif) : R114-18 proposé (LEGIARTI000031828742) vise les « déclarations, attestations et justificatifs ... fournis par les assurés sociaux » et les listes de L165-1 ; sans lien avec la certification promotionnelle retirée.
- **R862-11-4 → L862-4** (S9/F1+F5, déjà réglé) : R862-11-4 proposé (LEGIARTI000032156084) : « peut être acquittée par virement bancaire ou par un autre mode légal de paiement » et « Aucun document distinct de la déclaration de taxe ne peut être exigé systématiquement ».
- **R174-20 → L174-18** (S9/F1+F5, déjà réglé) : R174-20 proposé (LEGIARTI000034623669) : « La caisse centralisatrice des paiements procède à la liquidation ... sans autorisation préalable distincte de la caisse gestionnaire ».
- **D225-2 → L225-1-3** (S9/F1+F5, déjà réglé) : D225-2 proposé (LEGIARTI000034623787) : « Cette convention n'est pas soumise à approbation ministérielle » et « Le présent article ne rétablit aucune approbation supprimée par ces dispositions ».
- **D225-2 → L225-1-4** (S9/F1+F5, déjà réglé) : Même passage de D225-2 proposé (LEGIARTI000034623787) ; L225-1-4 proposé (LEGIARTI000045355468) retire l'approbation des conventions d'avance.
- **D162-30 → L162-5-14-2** (S9/F1+F5, déjà réglé) : D162-30 proposé (LEGIARTI000034731961) : « 2° À toute heure et quel que soit le jour » et « Aucune attestation sur l'honneur distincte n'est exigée » ; le certificat de décès lui-même n'est pas une formalité retirée.
- **R932-4-4-3 → R932-4-15** (S10/F5 (échantillon), faux positif) : R932-4-4-3 proposé (LEGIARTI000036330368) écarte « les deuxième et dernier alinéas de l'article R. 932-4-15 » ; R932-4-15 proposé (LEGIARTI000036332440) a toujours trois alinéas (calcul, affectation d'actifs, arrêté d'évaluation) : la dispense vise des règles existantes.
- **L612-2 → L231-6-1** (S10/F5 (échantillon), déjà réglé) : L612-2 proposé (LEGIARTI000036391005) désigne l'exception par son objet (« la disposition prévoyant la perte du mandat des personnes dont le remplacement est demandé ») au lieu du « dernier alinéa », que la transition ajoutée à L231-6-1 proposé (LEGIARTI000044404032) aurait déplacé.
- **D356-2 → L356-3** (F5+F1, G) : Relevé à la lecture de la piste S9 de D356-2. D356-2 proposé (LEGIARTI000023413984) conservait « 4° Ne pas être remarié, ne pas avoir conclu de pacte civil de solidarité et ne pas vivre en concubinage », alors que L356-3 proposé (LEGIARTI000023034902) dispose « 1° Abrogé » et « Le remariage, la conclusion d'un pacte civil de solidarité ou le concubinage ne peuvent, à eux seuls, faire obstacle à l'attribution, au maintien ou au rétablissement de l'allocation de veuvage », et que D356-11 (LEGIARTI000023397362) et D356-12 (LEGIARTI000023397496) proposés ont déjà retiré leurs renvois à ce 4°. Contradiction signalée par les notes de L356-3 et D356-11 (« D356-2 4° reste à corriger hors lot »), sans objection au registre. Correction : 4° Abrogé, avec la transition de L356-3.
- **R252-29 → F10** (F10, m) : Motif de R252-29 (LEGIARTI000006748964) tronqué : « Seconde passe : Coordination nécessaire : la source vise « par l'arrêté pris en application de l'article L. Le corps du brouillon est conservé » ; sans effet normatif, non corrigé (article non modifié par ailleurs).
