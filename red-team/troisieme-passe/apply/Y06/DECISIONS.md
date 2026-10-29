# Y06 — troisième balayage (S9, S10) : décisions

Texte lu : production, en lecture seule (`show.py` sur `corpus.sqlite?mode=ro` et le lot propriétaire, le 29 octobre 2026). Toutes les pistes concernent le code du travail. Le paquet contient 56 articles et 66 pistes (S9 : 48, S10 : 18).

## Bilan

- **G : 0.** Aucune correction n'est rédigée. `changes.json` ne contient aucun changement, et `check_changes.py Y06` donne `problems` vide.
- **déjà réglé : 32.** La proposition du décret ou de l'article qui déroge coordonne déjà la réduction de la loi, par exemple avec « aucune … n'est exigée », un dépôt devenu facultatif ou une sanction neutralisée.
- **faux positif : 29.** Le décret vise une formalité que la loi garde, ou l'article visé dit encore ce que la dérogation suppose. Certains renvois ne valent que pour l'ancien régime ou la transition.
- **m : 5 (F10, notes seulement).** Ces défauts ne sont pas corrigés, car aucun de ces articles n'est modifié par ailleurs (BRIEF-SWEEP, point 4). Ils sont listés sous `skipped`, avec la décision « arbitrage ».

Pour l'auteur : les cinq notes périmées peuvent être rafraîchies à l'occasion d'une autre modification. Elles n'ont aucun effet normatif.

## Une ligne par piste

| # | Article (LEGIARTI) | Piste | Cible | Qualification | Correction | Motif |
|---|---|---|---|---|---|---|
| 1 | D1221-23-1 (LEGIARTI000029814209) | S9/F1+F5 | L1221-13 | faux positif | non | renvoi "stagiaire mentionné au troisième alinéa" exact (3e al. L1221-13 inchangé); L1221-13 ne retire que la ressaisie/copie. |
| 2 | R3245-1 (LEGIARTI000030420807) | S9/F1+F5 | L3245-2 | déjà réglé | non | proposition retire la transmission systématique, "déclaration" n'apparaît que dans "Aucune ... déclaration de remplacement". |
| 3 | R1227-7 (LEGIARTI000030422217) | S9/F1+F5 | L1221-13 | faux positif | non | L1221-13 retire seulement la ressaisie; R1227-7 proposé exclut déjà la sanction des dispenses de réutilisation. |
| 4 | L1254-13 (LEGIARTI000030442369) | S10/F5 | L1254-12 | faux positif | non | dérogation visée 'L1254-12 dans sa rédaction antérieure' pour anciens CDD; L1254-12 proposé (abrogation) réserve expressément ce report. |
| 5 | R6341-4 (LEGIARTI000030520564) | S9/F1+F5 | L6341-4 | déjà réglé | non | proposition reprend "La décision accordant le financement ... vaut agrément du stage ... sans demande ni décision d'agrément distincte" (L6341-4 proposé). |
| 6 | R3332-21-1 (LEGIARTI000030776877) | S9/F1+F5 ; F10 | L3332-17-1 | m | non | proposition retire l'engagement lié à l'agrément ("sans engagement formel distinct", "date à laquelle elles se prévalent de la qualité"); seul défaut: notes disent succession au 1er janvier 2027 absente du corpus alors que LEGIARTI000054140237 y figure (notes de L3332-17-1). Non corrigé (m). |
| 7 | R3132-17 (LEGIARTI000031213123) | S9/F1+F5 | L3132-23 | déjà réglé | non | 'bénéficie de plein droit', 'Aucune autorisation d'extension ... n'est exigée'. |
| 8 | R1233-15-1 (LEGIARTI000031403149) | S9/F1+F5 | L1233-57-17 | déjà réglé | non | proposition ajoute "la qualité de destinataire ... n'impose aucune notification particulière de ce recours", transition identique. |
| 9 | R1233-15-1 (LEGIARTI000031403149) | S9/F1+F5 | L1233-57-20 | faux positif | non | L1233-57-20 garde le rapport "communiqué à l'autorité administrative" (seuls réunion distincte et support séparé retirés); R1233-15-1 ne les impose pas. |
| 10 | L2222-3-1 (LEGIARTI000033008810) | S10/F5 | L2232-33 | faux positif | non | 'sans préjudice ... L. 2232-33' ; L2232-33 proposé garde 'L'accord de méthode définit les thèmes auxquels cette dispense s'applique'. |
| 11 | L3141-30 (LEGIARTI000033020675) | S10/F5 | L3141-32 | faux positif | non | L3141-32 proposé garde l'affiliation obligatoire et laisse 'à l'employeur le service des congés ... lorsque le salarié n'est pas déclaré'; cohérent avec l'exclusion bornée. |
| 12 | L3134-1 (LEGIARTI000033021075) | S10/F5 | L3132-14 | faux positif | non | L3132-14 proposé reste dans la plage ; ses notes rectifiées disent déjà que l'autorisation de l'inspecteur est retirée. |
| 13 | L3134-1 (LEGIARTI000033021075) | S10/F5 ; F10 | L3133-7 | m | non | norme cohérente (la suppression de L3133-7 s'applique en Alsace-Moselle), mais notes disent "L3133-7 proposé conserve expressément la contribution de L137-40 CSS" et "conserve le renvoi au fondement autonome de la contribution", alors que L3133-7 proposé dispose "Aucune contribution de solidarité pour l'autonomie ... n'est due". Non corrigé (m). |
| 14 | L2232-20 (LEGIARTI000033022881) | S10/F5 | L2222-3 | faux positif | non | renvoi à L2222-3 qui garde calendrier (sous réserve) et prise en compte des demandes ; cohérent. |
| 15 | L2363-6 (LEGIARTI000033023049) | S10/F5 | L2363-7 | faux positif | non | L2363-7 proposé définit bien secret professionnel et discrétion pour le comité SCE. |
| 16 | L2363-6 (LEGIARTI000033023049) | S10/F5 | L2353-23 | faux positif | non | L2353-23 proposé vise L2353-26 ; L2363-6 substitue L2363-7 pour l'application SCE ; cohérent. |
| 17 | R5212-2-4 (LEGIARTI000033310296) | S9/F1+F5 | L5212-5 | faux positif | non | L5212-5 proposé maintient la déclaration DSN (seule la présomption de non-respect est retirée) ; R5212-2-4 la vise sans rétablir la présomption. |
| 18 | R3121-11 (LEGIARTI000033443497) | S9/F1+F5 | L3121-24 | déjà réglé | non | "Ce dépassement n'est soumis ni à la demande, ni au dossier, ni au rapport d'instruction, ni à la décision d'autorisation prévus à l'article R. 3121-10." |
| 19 | R3121-11 (LEGIARTI000033443497) | S9/F1+F5 | L3121-26 | faux positif | non | avis CSE maintenu par L3121-26 proposé; "Aucune déclaration ni transmission administrative de l'avis ne les remplace". |
| 20 | R3124-15 (LEGIARTI000033471412) | S9/F1+F5 | L3122-21 | déjà réglé | non | "l'absence de ces autorisations ou des pièces exclusivement destinées à leur obtention ne peut être sanctionnée". |
| 21 | R3124-15 (LEGIARTI000033471412) | S9/F1+F5 | L3122-22 | déjà réglé | non | même alinéa couvre L3122-22. |
| 22 | R3124-11 (LEGIARTI000033471420) | S9/F1+F5 | L3121-24 | déjà réglé | non | "La sanction ne peut être fondée sur l'absence de l'autorisation ou de la transmission de l'avis ... supprimées pour les dépassements relevant de l'article L. 3121-24". |
| 23 | D3123-4 (LEGIARTI000033515858) | S9/F1+F5 | L3123-38 | déjà réglé | non | 'n'établit pas une liste limitative de secteurs et ne subordonne pas le bénéfice ... à une inscription réglementaire'. |
| 24 | D7233-1 (LEGIARTI000033747505) | S9/F1+F5 | L7233-2 | déjà réglé | non | 2° "si celle-ci a été demandée" ; 11° "L'absence de déclaration ne justifie pas cette mention pour un avantage qui en est légalement dispensé." |
| 25 | R7232-20 (LEGIARTI000033747511) | S9/F1+F5 | L7233-2 | déjà réglé | non | perte "dans la seule mesure où ces conditions déterminent légalement leur attribution. Le seul retrait de l'enregistrement ne prive pas d'un avantage qui ne dépend pas de la déclaration." |
| 26 | R7232-17 (LEGIARTI000033747559) | S9/F1+F5 | L7233-2 | déjà réglé | non | engagements distincts retirés ; "Les dispenses de déclaration prévues à l'article L. 7233-2 ... demeurent applicables". |
| 27 | R7232-16 (LEGIARTI000033747562) | S9/F1+F5 ; F10 | L7233-2 | m | non | corps aligné ("n'est pas exigée pour le seul bénéfice d'un avantage pour lequel l'article L. 7233-2 dispense de déclaration") ; notes disent les successeurs au 1er janvier 2027 "non fournis" alors que LEGIARTI000053151858 (L7233-2) et LEGIARTI000053151864 (L7232-1-1) figurent au corpus. Non corrigé (m). |
| 28 | R4624-15 (LEGIARTI000033769066) | S9/F1+F5 | L4624-1 | faux positif | non | L4624-1 maintient l'attestation (seul le modèle devient facultatif) ; R4624-15 l'utilise pour une dispense favorable. |
| 29 | R5141-7 (LEGIARTI000034644045) | S9/F1+F5 | L5141-1 | déjà réglé | non | 4° 'inscrits sur la liste des demandeurs d'emploi' sans durée, transition identique à L5141-1. |
| 30 | D1453-2-12 (LEGIARTI000034733926) | S10/F5 | D1453-2-10 | faux positif | non | dérogation à D1453-2-10 qui garde le remboursement de l'employeur ; champ distinct (rémunéré uniquement à la commission). |
| 31 | D1453-2-13 (LEGIARTI000034733928) | S10/F5 | D1453-2-12 | faux positif | non | exclusion visant D1453-2-12 (indemnité directe), cohérente ; non-cumul explicite. |
| 32 | R1232-13 (LEGIARTI000036212577) | S9/F1+F5 | L1232-6 | faux positif | non | les formes LRAR/remise contre récépissé visent la demande et la communication de précisions, non la notification du licenciement dont L1232-6 retire l'exclusivité du recommandé ; R1232-13 vise déjà 'la notification écrite du licenciement'. |
| 33 | D2241-1 (LEGIARTI000036226423) | S9/F1+F5 | L2241-8 | déjà réglé | non | 'sans rapport distinct ni délai minimal général de quinze jours'. |
| 34 | R4162-4 (LEGIARTI000036409862) | S9/F1+F5 | L4162-2 | déjà réglé | non | II ne vise plus que l'accord ou le plan ; 'aucun dépôt de ce procès-verbal n'est exigé'. |
| 35 | R2312-58 (LEGIARTI000036413355) | S9/F1+F5 | L2315-61 | faux positif | non | maintenu ; il exclut déjà 'toute obligation relative à l'utilisation de la subvention de fonctionnement' ; rien de la réduction de L2315-61 n'est réintroduit. |
| 36 | D2315-38 (LEGIARTI000036433857) | S9/F1+F5 | L2315-61 | déjà réglé | non | "le rapport peut renvoyer aux informations inscrites dans les comptes annuels ... sans les reproduire". |
| 37 | D1233-4 (LEGIARTI000036483183) | S9/F1+F5 ; F10 | L1233-46 | m | non | corps maintenu cohérent (notification du projet conservée par L1233-46) ; notes disent encore "la même proposition maintient une information séparée sans délai sur l'ouverture ... correction requise de L1233-46", alors que L1233-46 proposé (RT-ISS9-01) ne la contient plus. Non corrigé (m). |
| 38 | R3122-9 (LEGIARTI000036483202) | S9/F1+F5 | L3122-21 | déjà réglé | non | "ne requiert ni demande d'autorisation à l'inspecteur du travail ni déclaration de remplacement" ; "sans document spécifique". |
| 39 | R1233-9 (LEGIARTI000036483247) | S9/F1+F5 ; F10 | L1233-46 | m | non | corps cohérent (transmission simultanée avec la notification maintenue) ; notes disent "L1233-46 proposé maintient « l'information sans délai sur l'ouverture effective »", phrase supprimée par RT-ISS9-01. Non corrigé (m). |
| 40 | R3132-13 (LEGIARTI000036483260) | S9/F1+F5 | L3132-14 | déjà réglé | non | "la seule organisation du travail en continu ou le seul recours aux équipes de suppléance n'est plus soumis à la demande ni à la décision prévues au présent article" ; demande limitée au dépassement de R3132-12. |
| 41 | R3132-13 (LEGIARTI000036483260) | S9/F1+F5 | L3132-18 | déjà réglé | non | même alinéa. |
| 42 | D3323-3 (LEGIARTI000036483322) | S9/F1+F5 | L3323-6 | faux positif | non | consultation du CSE maintenue (renvoi corrigé au troisième alinéa) ; seul le délai de quinze jours retiré, D3323-3 ne le rétablit pas. |
| 43 | D3323-3 (LEGIARTI000036483322) | S9/F1+F5 | L3323-4 | déjà réglé | non | "peut être déposée" ; "Le dépôt demeure facultatif dans le champ et selon la transition de l'article L. 3323-4". |
| 44 | R3323-5 (LEGIARTI000036483400) | S9/F1+F5 | L3323-4 | déjà réglé | non | mention "si les parties choisissent le dépôt facultatif prévu à l'article L. 3323-4". |
| 45 | D4133-3 (LEGIARTI000036484001) | S9/F1+F5 | L4133-1 | déjà réglé | non | "Les écrits consignant les alertes ... sont conservés" — plus de registre spécial. |
| 46 | D4133-3 (LEGIARTI000036484001) | S9/F1+F5 | L4133-2 | déjà réglé | non | idem. |
| 47 | D4133-2 (LEGIARTI000036484003) | S9/F1+F5 | L4133-2 | déjà réglé | non | "sans obligation d'inscription dans un registre spécial". |
| 48 | D4133-2 (LEGIARTI000036484003) | S9/F1+F5 | L4133-1 | faux positif | non | D4133-2 ne renvoie plus au registre de D4133-1 ; D4133-1 proposé l'a lui-même supprimé. |
| 49 | D4132-2 (LEGIARTI000036484007) | S9/F1+F5 | L4132-2 | déjà réglé | non | "Les écrits consignant les avis prévus à l'article L. 4132-2 sont conservés". |
| 50 | D4132-1 (LEGIARTI000036484010) | S9/F1+F5 | L4132-2 | déjà réglé | non | "Aucun registre spécial, numérotation des pages, authentification par tampon ... n'est exigé". |
| 51 | D2231-7 (LEGIARTI000036920591) | S9/F1+F5 | L2231-6 | déjà réglé | non | dépôt unique maintenu par L2231-6 ; "sans second exemplaire", "aucune version publiable distincte n'est à fournir", réemploi des pièces accessibles. |
| 52 | D2231-6 (LEGIARTI000036920594) | S9/F1+F5 | L2231-6 | déjà réglé | non | "aucune liste distincte n'est exigée" si les informations figurent au texte ; réemploi via L2231-6. |
| 53 | R4451-49 (LEGIARTI000037024672) | S9/F1+F5 | L4711-5 | faux positif | non | maintenu ; renvoi au(x) registre(s) de L4711-5, dont seule la condition de facilitation du registre unique est retirée ; rien n'est réintroduit. |
| 54 | L5213-13-1 (LEGIARTI000037378686) | S10/F5 | L1224-2 | faux positif | non | 'Le premier alinéa de l'article L. 1224-2 n'est pas applicable' ; L1224-2 proposé garde au premier alinéa la reprise des obligations (le remboursement entre employeurs est déplacé plus bas). |
| 55 | L1262-6 (LEGIARTI000037379225) | S10/F5 | L1262-3 | faux positif | non | "Sans préjudice de l'article L. 1262-3" ; L1262-3 proposé (droit constant) garde l'exclusion du faux détachement. |
| 56 | L1262-6 (LEGIARTI000037379225) | S10/F5 | L1262-1 | faux positif | non | L1262-1 proposé garde les 1° et 2° visés. |
| 57 | L1251-58-4 (LEGIARTI000037379976) | S10/F5 | L1251-36 | faux positif | non | exclusion de L1251-36, lui-même abrogé ; exclusion sans objet mais inoffensive (L1251-36 proposé note que L1251-58-4 l'exclut déjà). |
| 58 | L6332-1-1 (LEGIARTI000037387398) | S10/F5 | L6523-1 | faux positif | non | 'sans préjudice des dispositions de l'article L. 6523-1' ; L6523-1 proposé garde un régime ultramarin propre (sans autorisation) ; notes de L6332-1-1 confirment que la réserve ne rétablit rien. |
| 59 | D1233-50 (LEGIARTI000037387813) | S10/F5 | D1233-49 | faux positif | non | "Par dérogation à l'article D. 1233-49" ; D1233-49 proposé garde les 20 % et renvoie lui-même à la prise en charge complémentaire de D1233-50. |
| 60 | D1233-49 (LEGIARTI000037387819) | S10/F5 | L1233-65 | faux positif | non | L1233-65 proposé conserve les "périodes de formation" du parcours ; renvoi exact. |
| 61 | R2315-31-1 (LEGIARTI000037535713) | S9/F1+F5 | L2315-61 | déjà réglé | non | "sans plafond exprimé en proportion" ; "Le rapport ... peut renvoyer à ces informations sans les reproduire". |
| 62 | D2622-1 (LEGIARTI000037583846) | S9/F1+F5 | L2622-1 | déjà réglé | non | 'même en l'absence de clause particulière. L'absence d'une telle clause ne fait pas obstacle à leur extension.' |
| 63 | R6332-4 (LEGIARTI000037934233) | S9/F1+F5 | L6332-1-1 | déjà réglé | non | 3° "Aucun montant minimal de contributions gérées ni nombre minimal d'entreprises couvertes n'est exigé" (tournure maladroite dans l'énumération « lorsque les opérateurs... : 3° Aucun montant... n'est exigé », sans effet ; numérotation gardée pour R6332-6). |
| 64 | R6332-1 (LEGIARTI000037934237) | S9/F1+F5 | L6332-1-1 | faux positif | non | maintenu ; l'agrément ministériel subsiste au I de L6332-1-1 proposé, seuls les seuils sont retirés. |
| 65 | R6341-2 (LEGIARTI000038061778) | S9/F1+F5 | L6341-4 | déjà réglé | non | même phrase d'équivalence ; avis supprimés. |
| 66 | L1262-2 (LEGIARTI000038156567) | S10/F5 | L1251-33 | faux positif | non | exclusion de L1251-32/33 pour les CDI étrangers ; pour les CDD étrangers renvoi exprès à "leur rédaction antérieure" ; L1251-33 abrogé avec transition. |

Revue IA : rien de ceci ne vaut validation par un juriste.
