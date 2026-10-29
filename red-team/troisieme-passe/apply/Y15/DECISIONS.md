# Y15 : troisième balayage (S9), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-Y15.json`, soit 53 articles des annexes I à III du CGI et 58 pistes, toutes S9 (aucune S10). Contrôle : `python3 -B apply/check_changes.py Y15` donne 10 lignes construites, 10 validées et `problems` vide. Seul diagnostic : longueur de l'annexe II 298 (ratio 5,58), voulu (abrogation pour l'avenir et transition, sur le modèle de 295 à 297).

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G, corrigé | 11 (10 articles) |
| déjà réglé | 18 |
| faux positif | 29 |
| m | 0 (2 observations hors piste, non corrigées) |

Corrections : 10 lignes en mode `replace`. Deux demandes (`requests`). Rien d'écarté (`skipped` vide).

## Défauts confirmés et corrigés

Dans chaque cas, le décret ou l'annexe organisait encore une formalité que la proposition de la loi visée retire, ou contredisait expressément cette proposition. Les corrections alignent le texte sur la loi proposée et en reprennent la transition. Elles ne créent aucune formalité ni sanction de remplacement, et ne touchent à aucun autre point.

1. **Annexe II 91 quater B** (LEGIARTI000006293903) / CGI 157. Le II exigeait encore les renseignements propres au PEP lorsque des produits sont versés. Or le 22° de 157 proposé en dispense les organismes gestionnaires. Le II est aligné sur cette dispense, avec la transition de 157 : échéances postérieures et loi répressive plus douce. Le I est inchangé.
2. **Annexe II 260 J** (LEGIARTI000006294562) / CGI 298 bis. Le texte imposait encore une option écrite adressée à part et formulée avant l'exercice. 298 bis I 1° proposé prévoit une option portée par une mention dans la première déclaration, sans envoi distinct. Le premier alinéa est aligné. La transition du VI de 298 bis s'applique : exercices ouverts après l'entrée en vigueur. La renonciation par écrit est inchangée.
3. **Annexe II 298** (LEGIARTI000006294774) / CGI 809. La règle d'évaluation visait une déclaration que 809 II et 295 à 297 proposés suppriment pour les changements de régime futurs. L'article est abrogé pour ces changements (`full_repeal`), comme 295 à 297. La règle de la source est conservée pour les changements antérieurs.
4. **Annexe II 242-0 C** (LEGIARTI000030066036) / CGI 287. Le III renvoyait au « dernier alinéa » de 242 sexies, qui est désormais sa transition (F3). Le renvoi désigne maintenant le relevé par son objet. Pour les exercices où 287 proposé écarte les acomptes, le remboursement sur immobilisations peut être demandé par le même relevé, sans acompte, comme le prévoit 287 proposé.
5. **Annexe II 289** (LEGIARTI000054363092) / CGI 302 D bis et 302 V bis. Deux compétences portaient sur des formalités supprimées :
   - le 15°, sur les numéros issus de la déclaration de profession ;
   - le 68°, sur l'agrément du représentant fiscal.

   Les deux sont abrogées pour l'avenir. Leurs numéros restent à leur place, et les transitions de 111-0 F et de 302 V bis sont reprises. Le `benefit_review` est mis à jour.
6. **Annexe II 171 quater A** (LEGIARTI000054363221) / CGI 244 bis A. L'accréditation du représentant fiscal était organisée sans limite de temps. Un XIII la réserve aux cessions antérieures et aux responsabilités qui en sont nées. Pour les cessions nouvelles, aucune accréditation ni garantie n'est exigée.
7. **Annexe II 171 quater** (LEGIARTI000054363238, auparavant maintenu) / CGI 244 bis A. L'obligation de désigner un représentant accrédité est réservée aux cessions antérieures. La mention du représentant devient conditionnelle. Sans représentant, le dépôt sans acte se fait au service compétent à l'égard du cédant. L'article passe en `rewrite_draft`, en coordination.
8. **Annexe II 310-0 H bis** (LEGIARTI000047785488) / CGI 1384 A. 1384 A I bis proposé supprime le circuit attestation – certificat – transmission avec 1406. L'article est abrogé pour les impositions futures (`full_repeal`), y compris pour la période d'exonération restant à courir. Les années antérieures gardent l'ancien régime avec les allègements déjà retenus. La note erronée a été retirée.
9. **Annexe III 38 sexdecies RB** (LEGIARTI000006296668) / CGI 74 A. Le c ajoutait le bilan simplifié, alors que 74 A proposé en dispense. Le c reprend cette dispense, avec la transition de 74 A.
10. **Annexe III 98 bis** (LEGIARTI000006296971) / CGI 290 bis. Les 1, 3, 4 et 6 rendaient l'attestation obligatoire, la faisaient joindre à la déclaration et renvoyaient à l'attestation annuelle supprimée de 290 bis et à un modèle que 266 n'impose plus. Mandat et attestation deviennent facultatifs. Le non-cumul et l'opposabilité au client sont conservés. La transition est celle de 290 bis.

## Demandes à d'autres groupes (`requests`)

- **Annexe II 242 septies A** (LEGIARTI000049826453, sans groupe). Son 2 et sa transition prévoient encore des acomptes et des modulations pour les exercices décalés, que 287 proposé supprime. Le texte à ajouter figure dans la demande.
- **Annexe IV 50-0 A bis** (LEGIARTI000042147351, groupe Y18). Il organise encore la demande et le numéro d'agrément du représentant fiscal que 302 V bis proposé supprime. La demande est à appliquer si Y18 ne l'a pas déjà fait.

## Points laissés à l'auteur

- **171 quater** : pour un cédant sans représentant et une cession non constatée par un acte, le dépôt renvoie au « service des impôts compétent à l'égard du cédant ». Aucun service nouveau n'est désigné.
- **38 sexdecies RB** : le relevé des provisions et l'état des provisions non déductibles subsistent, comme dans la source, malgré la dispense générale de 74 A. Ce décalage préexistant n'est pas tranché.
- **267 quater F et H** (maintenus) : la rédaction 2027 de 287 issue de la LF 2025 décale leur renvoi au « dernier alinéa du 2 ». C'est un conflit de source, et non un effet du projet. Il n'est pas corrigé, et 302 bis WA et WC sont en abrogation différée.
- **242 sexies** : les acomptes des exercices civils au régime simplifié disparaissent en 2027 par l'effet de la LF 2025. Le texte n'est pas modifié.

## Qualification de chaque piste

| Article (version) | Loi visée | Qualification | Motif |
|---|---|---|---|
| a1 50 (LEGIARTI000051821232) | 302 G | faux positif | a1 50 proposé (LEGIARTI000051821232) : la « déclaration prescrite par l'article 48 » est la déclaration de distillation. |
| a2 1 D (LEGIARTI000006293664) | 31 | déjà réglé | 1 D proposé (LEGIARTI000006293664) : « Aucun compte spécial de dépôt des parts n'est exigé ». |
| a2 16 G (LEGIARTI000006293681) | 39 quinquies GB | déjà réglé | 16 G proposé (LEGIARTI000006293681) : « L'obligation de produire un compte d'exploitation récapitulatif supplémentaire est supprimée » et de même pour l'état récapitulatif, conforme à 39 quinquies GB proposé. |
| a2 74 SH (LEGIARTI000006293831) | 150 VG | faux positif | 74 SH (LEGIARTI000006293831) organise la déclaration de 150 VG, que 150 VG proposé (LEGIARTI000027978330) maintient (« Une déclaration, qui peut être établie sur le modèle proposé par l'administration ou sur un support comportant . |
| a2 74 SJ (LEGIARTI000006293834) | 150 VG | faux positif | 74 SJ proposé (LEGIARTI000006293834) retire déjà la mention de l'adresse du service et son refus. |
| a2 91 quater B (LEGIARTI000006293903) | 157 | G | F1+F5. 91 quater B II proposé (LEGIARTI000006293903) exigeait encore, en cas de versement de produits, « Les nom, prénoms et adresse du titulaire. Corrigé. |
| a2 171 A (LEGIARTI000006294225) | 238 bis J | déjà réglé | 171 A proposé (LEGIARTI000006294225) : « Il ne rétablit pas l'état détaillé spécial de la provision de réévaluation supprimé au II de l'article 238 bis J ». |
| a2 242 undecies (LEGIARTI000006294514) | 298 sexies | faux positif | 242 undecies (LEGIARTI000006294514) fixe les mentions de facture des livraisons exonérées de moyens de transport neufs. |
| a2 260 J (LEGIARTI000006294562) | 298 bis | G | F1+F5. 260 J proposé (LEGIARTI000006294562) : l'option « est adressée au service [...] par tout écrit » et « est formulée avant le début du premier exercice pour lequel elle est souscrite, conformément au même article 298 bis », a. Corrigé. |
| a2 294 E (LEGIARTI000006294770) | 1055 bis | déjà réglé | 294 E proposé (LEGIARTI000006294770) : « 4° Abrogé pour les ventes relevant de la nouvelle rédaction de l'article 1055 bis » et « aucune indication, déclaration, affirmation, engagement ou copie supplémentaire n'est exigé » pour l. |
| a2 298 (LEGIARTI000006294774) | 809 | G | F1+F5. 298 proposé (LEGIARTI000006294774) appliquait sa règle d'évaluation « aux changements de régime fiscal intervenant à compter de l'entrée en vigueur de la loi » et son motif affirmait que « la valeur vénale et la déclaration. Corrigé. |
| a2 310 HQ (LEGIARTI000006294851) | 1477 | déjà réglé | 310 HQ proposé (LEGIARTI000006294851) : « ne rétablit aucune déclaration exclusivement destinée à la cotisation foncière des entreprises pour une activité qui en est dispensée ». |
| a2 171 bis (LEGIARTI000006295425) | 237 bis A | faux positif | 171 bis (LEGIARTI000006295425) ne vise ni le dépôt de l'accord de participation à la DDTE ni l'autorisation ministérielle de transfert, seuls retirés de 237 bis A proposé. |
| a2 310 G (LEGIARTI000006295726) | 1131 | déjà réglé | 310 G proposé (LEGIARTI000006295726) : « Ces obligations ne sont pas exigées au titre d'une transmission résultant d'un décès survenu à compter de l'entrée en vigueur ». |
| a2 383 ter (LEGIARTI000006296208) | 287 | faux positif | 383 ter (LEGIARTI000006296208, maintenu) règle l'imputation des acomptes du 3 de 287 dans sa rédaction antérieure. |
| a2 1 C (LEGIARTI000020425469) | 31 | déjà réglé | 1 C proposé (LEGIARTI000020425469) : option « dans sa déclaration du résultat [...] ou dans une réclamation recevable ». |
| a2 242 duodecies (LEGIARTI000022179464) | 298 sexies | déjà réglé | 242 duodecies proposé (LEGIARTI000022179464) : « aucune nouvelle caution ni attestation spéciale n'est exigée ». |
| a2 383 (LEGIARTI000022179520) | 231 | déjà réglé | 383 proposé (LEGIARTI000022179520) : « ne s'applique qu'à la taxe sur les salaires afférente aux rémunérations versées avant la date d'entrée en vigueur de la loi portant suppression de la taxe sur les salaires ». |
| a2 383 (LEGIARTI000022179520) | 1754 | faux positif | 383 renvoie aux I et IV de 1754 (recouvrement des pénalités, charge de succession). |
| a2 310 G bis (LEGIARTI000024045321) | 1378 octies | faux positif | 310 G bis (LEGIARTI000024045321, maintenu) organise la procédure contradictoire de suspension. |
| a2 242 C (LEGIARTI000025622311) | 261 | déjà réglé | 242 C proposé (LEGIARTI000025622311) : « Aucune certification des comptes [...] n'est exigée au seul titre du présent article » et « Aucun document annuel attestant le montant des ressources [...] n'est à communiquer ». |
| a2 74 S sexies (LEGIARTI000029101320) | 150 VM | faux positif | 74 S sexies (LEGIARTI000029101320, maintenu) énumère le contenu de la déclaration de 150 VM. |
| a2 267 quater H (LEGIARTI000030066006) | 287 | faux positif | 267 quater H (LEGIARTI000030066006, maintenu) adosse la redevance aux déclarations de TVA, non à l'autorisation du délai supplémentaire retirée de 287. Observation hors piste (m, conflit de source) : le renvoi au « dernier alinéa . |
| a2 267 quater F (LEGIARTI000030066011) | 287 | faux positif | 267 quater F (LEGIARTI000030066011, maintenu) : même analyse que 267 quater H. |
| a2 242-0 C (LEGIARTI000030066036) | 287 | G | F3+F5. 242-0 C III proposé (LEGIARTI000030066036) renvoie au « relevé mentionné au dernier alinéa de l'article 242 sexies », dont le dernier alinéa proposé est la transition (renvoi décalé signalé par les notes de 242 sexies, 242 . Corrigé. |
| a2 242-0 C (LEGIARTI000030066036) | 1693 bis | faux positif | 242-0 C II (LEGIARTI000030066036) vise l'option agricole de 1693 bis pour ouvrir le remboursement. |
| a2 242 terdecies (LEGIARTI000030783030) | 298 sexies | faux positif | 242 terdecies (LEGIARTI000030783030) maintient la demande et la présentation du certificat fiscal du V bis, que 298 sexies proposé conserve. |
| a2 286 M (LEGIARTI000032881388) | 302 G | faux positif | 286 M (LEGIARTI000032881388) organise compensation et remboursement du IV de 302 G. |
| a2 202 C (LEGIARTI000036437229) | 261 | déjà réglé | 202 C proposé (LEGIARTI000036437229) : « Aucune cessation de l'exonération ne peut être fondée, pour les opérations nouvelles, sur l'absence de l'attestation fiscale supprimée ». |
| a2 202 B (LEGIARTI000036437238) | 261 | déjà réglé | 202 B proposé (LEGIARTI000036437238) : « choisit l'exonération en l'appliquant à ses opérations, sans demande ni déclaration supplémentaire ». |
| a2 1 B (LEGIARTI000037094726) | 31 | déjà réglé | 1 B proposé (LEGIARTI000037094726) : option « dans la déclaration de revenus ou dans une réclamation ». |
| a2 384 A ter (LEGIARTI000037273424) | 982 | faux positif | 384 A ter (LEGIARTI000037273424) vise la déclaration IFI du 1 du I de 982, maintenue. |
| a2 384 A bis (LEGIARTI000037273432) | 982 | faux positif | 384 A bis (LEGIARTI000037273432) : même renvoi au dépôt IFI maintenu. |
| a2 384-0 A bis (LEGIARTI000037273439) | 982 | faux positif | 384-0 A bis (LEGIARTI000037273439) : même renvoi au délai de dépôt IFI maintenu. |
| a2 286 J (LEGIARTI000038668387) | 302 G | faux positif | 286 J proposé (LEGIARTI000038668387) organise la comptabilité matières maintenue par 302 G. |
| a2 202 A (LEGIARTI000038668421) | 261 | déjà réglé | 202 A proposé (LEGIARTI000038668421) : « n'ont à obtenir aucune attestation fiscale distincte. Aucune demande, aucun imprimé, aucun envoi recommandé ni déclaration de remplacement ». |
| a2 294 ter (LEGIARTI000038702040) | 787 B | déjà réglé | 294 ter proposé (LEGIARTI000038702040) : « Aucune attestation du présent article n'est exigée pour une transmission résultant d'un décès survenu à compter de l'entrée en vigueur ». |
| a2 91 quater H (LEGIARTI000041589962) | 157 | faux positif | 91 quater H (LEGIARTI000041589962, maintenu) concerne le PEA (5° bis de 157), dont le reporting n'est pas retiré. |
| a2 91 quater G (LEGIARTI000041589978) | 157 | faux positif | 91 quater G proposé (LEGIARTI000041589978) concerne le PEA et retient déjà « avant l'expiration de la troisième année », conforme au 5° ter de 157 proposé. |
| a2 294 bis (LEGIARTI000042160525) | 787 B | déjà réglé | 294 bis proposé (LEGIARTI000042160525) : II abrogé pour les décès nouveaux et « Ces obligations ne sont pas exigées au titre d'une transmission résultant d'un décès ». |
| a2 318 E (LEGIARTI000047278797) | 1382 | faux positif | 318 E (LEGIARTI000047278797, maintenu) vise le 1° de 1382 (constructions publiques). |
| a2 310-0 H bis (LEGIARTI000047785488) | 1384 A | G | F1+F5. 310-0 H bis proposé (LEGIARTI000047785488) organise encore attestation accréditée, certificat départemental et transmission avec la déclaration de 1406, sa note affirmant que « 1384 A I bis impose encore le certificat dépar. Corrigé. |
| a2 310-0 H bis (LEGIARTI000047785488) | 1406 | faux positif | 310-0 H bis III vise la déclaration de 1406, que 1406 proposé maintient (seule la déchéance pour retard est retirée). |
| a2 242 sexies (LEGIARTI000049826459) | 287 | faux positif | 242 sexies (LEGIARTI000049826459) régit les acomptes des exercices civils au régime simplifié, qui disparaissent au 1er janvier 2027 par la LF 2025. |
| a2 254 (LEGIARTI000050811261) | 287 | faux positif | 254 (LEGIARTI000050811261, maintenu) renvoie au c du 6 de 287, inchangé dans 287 proposé (franchises 293 B bis). |
| a2 285 A (LEGIARTI000052522035) | 302 F ter | faux positif | 285 A (LEGIARTI000052522035) concerne l'agrément d'acheteur-revendeur de tabacs du code de la santé publique. |
| a2 289 (LEGIARTI000054363092) | 302 D bis | G | F1+F5. 289 15° (LEGIARTI000054363092) attribuait encore la compétence d'« Attribution et retrait du numéro d'identification des intermédiaires [...] et des utilisateurs », alors que 302 D bis III proposé (LEGIARTI000041472187) exc. Corrigé. |
| a2 289 (LEGIARTI000054363092) | 302 G | faux positif | 289 4°, 5° et 6° visent caution, retrait d'agrément et remboursement de 302 G, maintenus. |
| a2 289 (LEGIARTI000054363092) | 302 V bis | G | F1+F5. 289 68° (LEGIARTI000054363092) : « Délivrance de l'agrément de représentant fiscal, prévu à l'article 302 V bis », alors que 302 V bis proposé (LEGIARTI000041472195) : « Le représentant fiscal exerce son activité sans agrém. Corrigé. |
| a2 171 quater A (LEGIARTI000054363221) | 244 bis A | G | F1+F5. 171 quater A (LEGIARTI000054363221) organise sans limite de temps l'accréditation du représentant fiscal, caution, compte dédié et engagement, alors que 244 bis A IV proposé (LEGIARTI000048806274) : « Aucun représentant fis. Corrigé. |
| a2 171 quater (LEGIARTI000054363238) | 244 bis A | G | F1+F5. 171 quater (LEGIARTI000054363238, maintenu) : « désignent un représentant, accrédité dans les conditions prévues par cet article », contraire au IV de 244 bis A proposé pour les cessions nouvelles. Corrigé. |
| a3 10 duodecies (LEGIARTI000006296511) | 204 | faux positif | 10 duodecies proposé (LEGIARTI000006296511) vise la déclaration de résultats et supprime déjà l'engagement distinct. |
| a3 38 sexdecies Q (LEGIARTI000006296657) | 53 A | faux positif | 38 sexdecies Q (LEGIARTI000006296657, maintenu) vise les déclarations des exploitants agricoles à l'IR. |
| a3 38 sexdecies RB (LEGIARTI000006296668) | 74 A | G | F1+F5. 38 sexdecies RB c proposé (LEGIARTI000006296668) ajoutait « ainsi que le bilan simplifié prévu à l'article 74 A », alors que 74 A proposé (LEGIARTI000006307817) : « Ces exploitants sont dispensés de produire un bilan simpli. Corrigé. |
| a3 73 H (LEGIARTI000006296946) | 286 | faux positif | 73 H proposé (LEGIARTI000006296946) supprime déjà les attestations. |
| a3 98 bis (LEGIARTI000006296971) | 290 bis | G | F1+F5+F3. 98 bis proposé (LEGIARTI000006296971) : « les attestations qu'ils doivent joindre à la déclaration annuelle », « établissent une attestation pour chaque client », « l'attestation annuelle prévue par l'article 290 bis », . Corrigé. |
| a3 324 AL (LEGIARTI000006297318) | 53 A | déjà réglé | 324 AL proposé (LEGIARTI000006297318) : « Le renvoi à l'article 53 A n'impose par lui-même ni déclaration annuelle supplémentaire ni imposition annuelle des bénéfices conservés ». |
| a3 2 undecies (LEGIARTI000006297479) | 31 | déjà réglé | 2 undecies proposé (LEGIARTI000006297479) : « Le bailleur n'est pas tenu de joindre de pièces justificatives ». |
