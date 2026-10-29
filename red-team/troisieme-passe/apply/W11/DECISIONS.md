# W11 : décisions du balayage (troisième passe)

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`). Les preuves sont sous `evidence/cited/production-20261029/`. Le code concerné est le code de la construction et de l'habitation.

## Bilan

- 68 articles et 104 pistes : 43 faux positifs, 42 déjà réglés, 12 défauts mineurs (m) et 7 défauts grossiers (G).
- 7 corrections dans `apply/W11/changes.json`, dont 4 propositions nouvelles (mode `new`) sur des versions futures et 3 remplacements. Le contrôle `python3 -B apply/check_changes.py W11` donne `problems: []`. Ses diagnostics sont voulus : réduction normative déclarée, longueur et renvois modifiés.
- Une objection connue hors paquet est laissée à l'auteur (`skipped`, arbitrage) : RT-P1-CCH-09 (L200-9-1).

## Corrections appliquées

1. **SW-W11-AUDIT-L651-5** : piste AUDIT de L631-4, correction portée par L651-5 (LEGIARTI000006825957), appliquée.
   - Défaut : L631-4 proposé supprime l'arrêté ministériel des primes locales, alors que L651-5 punissait encore le fait de « faire fixer cette prime à un taux supérieur à l'un de ceux fixés par l'arrêté prévu à l'article L. 631-4 ».
   - Changement : ce membre de l'incrimination est retiré. Un dernier alinéa applique la loi pénale plus douce aux faits non définitivement jugés, sans restitution des amendes exécutées. La perception et la tentative de perception indues restent punies (trois mois, 3 000 euros).
   - Motif, notes et bilan d'impact sont corrigés : le « taux abusif maintenu » est supprimé et un effet de coordination est ajouté.
2. **SW-W11-S5-L621-6** : nouvelle proposition sur la version de 2029 (LEGIARTI000052846041, ordonnance n° 2025-1091), appliquée.
   - Elle reprend l'abrogation déjà proposée pour la version en vigueur : fin de la transmission au service municipal et de l'expulsion spéciale pour occupation insuffisante, avec la même transition.
   - Elle est codée `full_repeal`. L'objection RT-P1-CCH-04 est ainsi rendue effective.
3. **SW-W11-S5-L443-15** : nouvelle proposition sur la version de 2027 (LEGIARTI000053151467), appliquée.
   - Elle reporte la suppression du seuil de 60 % des voix pour désigner un autre syndic, avec la même transition. Les autres alinéas sont ceux de 2027.
   - La phrase sur la TVA (CGI 261 B) n'est pas rétablie : l'ordonnance la retire et CGI 261 B cesse d'être en vigueur au 1er janvier 2027. Le relais au CIBS n'est pas vérifié (RT-FUTTL-03).
4. **SW-W11-S5-R711-16** : nouvelle proposition sur la version du 21 février 2027 (LEGIARTI000052123156), appliquée.
   - Elle donne aux notaires l'accès à « l'ensemble des données du registre, conformément à l'article L. 711-3 ».
   - La version de 2027 renvoyait aux 1° à 3° du III de L711-2, que le projet abroge. L'objection RT-FUTTL-14 est ainsi rendue effective.
5. **SW-W11-S5-L862-3** : nouvelle proposition sur la version de 2028 (LEGIARTI000054475023), appliquée. Elle reporte la correction « les 3°, 4° et 5° deviennent » ; la limitation du 5° à L. 781-8 décidée par l'ordonnance est conservée. L'objection RT-FUTTL-20 est ainsi traitée.
6. **SW-W11-S8-L445-2** (LEGIARTI000038834104) : appliquée. « II de l'article R. 331-1 » devient « II de l'article D. 331-1 » (transfert par l'article 5 du décret n° 2019-873). Le fond ne change pas.
7. **SW-W11-S8-R365-1** (LEGIARTI000039048439) : appliquée.
   - Au 1° a, « R. 331-1 » devient « D. 331-1 ».
   - Les notes sont corrigées : elles disaient R331-1 et R381-5 absents du corpus.
   - Le renvoi du 1° f à R381-5 est laissé en l'état et signalé. Son successeur D381-5 a été abrogé en 2022 sans relais, et supprimer la condition élargirait l'agrément.

## Points pour l'auteur

1. **L200-9-1 I 2°** (hors paquet, sans groupe propriétaire ; objection RT-P1-CCH-09). Le texte renvoie encore à la durée de L202-9-1, que le projet abroge. Deux options restent ouvertes : une occupation temporaire sans limite tirée de L202-9-1 (moins de contraintes), ou une durée statutaire. Rien n'est appliqué.
2. **Règlements orphelins** (conflit de source hérité, m). Aucun successeur n'est identifié, aucun renvoi n'est inventé, et l'abrogation éventuelle, avec une transition pour les droits anciens, revient à l'auteur :
   - R315-69, R315-72, R315-73 et R315-75 : la base L315-19 à L315-32 a été abrogée par l'article 180 de la loi n° 2011-525 ;
   - R318-27 : il vise R318-3, abrogé en 2010 ;
   - D331-104 : il vise R353-165-4, abrogé en 2011.
3. **R824-4 à R824-16** (m, F4/F10). Les propositions parlent de « l'abrogation du présent article prévue au 1er janvier 2027 ». Or ces articles sont remplacés à cette date par le nouveau régime des impayés, qui atteint déjà les allègements du projet. La formule est sans effet normatif. Rédaction suggérée : « le remplacement de la rédaction du présent article le 1er janvier 2027 ».
4. **Notes inexactes** (F10, sans effet normatif). Elles disent « absent du corpus » ou « successeur non fourni » pour des textes qui y figurent, ou sont périmées :
   - L251-9, L313-6, L443-15 (version en vigueur), L862-3 (version en vigueur), R315-69 à R315-75, R318-27, R662-1, R631-20, D331-104, R824-4 ;
   - L411-8 : il dit que L411-8-1 garde l'arrêté, ce qui n'est plus vrai ;
   - R481-11 : il évoque un « maintien résiduel de L442-3-4 » dans R*442-3-3, qui a été retiré ;
   - annexe I à D331-65 : « La convention ne rouvre pas ce champ ».
5. **L411-8** (m). La dérogation « au dernier alinéa de l'article L. 411-8-1 » est devenue redondante : cet alinéa ne prévoit plus d'approbation. Elle est sans effet contraire.

## Une ligne par article (qualification des pistes)

- L251-8 (LEGIARTI000006824561) : S7/F3 → L251-5 : **faux positif**.
- L251-9 (LEGIARTI000006824671) : S7/F3 → L251-5 : **déjà réglé**.
- L313-6 (LEGIARTI000006824846) : S5/F4 → LEGIARTI000053151478 : **faux positif**.
- L642-11 (LEGIARTI000006825925) : S7/F3 → L642-10 : **faux positif**.
- L651-1 (LEGIARTI000006825945) : S2/F2 → L631-6 : **faux positif** ; S2/F2 → L641-14 : **faux positif**.
- L651-3 (LEGIARTI000006825952) : S2/F2 → L631-6 : **faux positif** ; S2/F2 → L641-14 : **faux positif**.
- L651-5 (LEGIARTI000006825957) : S2/F2 → L631-6 : **faux positif**.
- Annexe I à l'article R313-31 (LEGIARTI000006832791) : S8/F3 → R313-31 : **déjà réglé** ; S8/F3 → L313-28 : **déjà réglé** ; S8/F3 → R313-31-2 : **déjà réglé**.
- Annexe II à l'article R313-31-2 (LEGIARTI000006832792) : S8/F3 → R313-31 : **déjà réglé** ; S8/F3 → L313-28 : **déjà réglé** ; S8/F3 → R313-31-2 : **déjà réglé**.
- Annexe III aux articles R313-31, R313-31-2 (LEGIARTI000006832793) : S8/F3 → R313-31 : **déjà réglé** ; S8/F3 → L313-28 : **déjà réglé** ; S8/F3 → R313-31-2 : **déjà réglé**.
- R315-69 (LEGIARTI000006897038) : S8/F3 → L315-32 : **m** ; S8/F3 → L315-26 : **m** ; S8/F3 → L315-19 : **m**.
- R315-72 (LEGIARTI000006897041) : S8/F3 → L315-25 : **m**.
- R315-73 (LEGIARTI000006897042) : S8/F3 → L315-21 : **m**.
- R315-75 (LEGIARTI000006897045) : S8/F3 → L315-21 : **m**.
- R318-1 (LEGIARTI000006897099) : S8/F3 → L128-1 : **faux positif**.
- R318-27 (LEGIARTI000006897137) : S8/F3 → R318-3 : **m**.
- R411-1 (LEGIARTI000006899222) : S7/F3 → L411-1 : **faux positif**.
- R662-1 (LEGIARTI000006900587) : S8/F3 → R261-19 : **faux positif** ; S8/F3 → R261-18 : **faux positif** ; S8/F3 → R261-20 : **faux positif**.
- L631-4 (LEGIARTI000019286925) : AUDIT/F2+F3 → audit : **G** — corrigé (SW-W11-AUDIT-L651-5).
- D481-5-7 (LEGIARTI000021632161) : S8/F3 → L111-3 : **faux positif**.
- D442-20 (LEGIARTI000025099614) : S8/F3 → L111-3 : **faux positif**.
- L411-8 (LEGIARTI000028808988) : S7/F3 → L411-8-1 : **m**.
- R202-1 (LEGIARTI000031682360) : S1/F1 → L202-9-1 : **déjà réglé**.
- Annexe à l'article R423-85 (LEGIARTI000032660331) : S1/F1 → L443-14 : **faux positif** ; S8/F3 → R423-92 : **déjà réglé** ; S8/F3 → R423-90 : **déjà réglé** ; S8/F3 → R423-91 : **déjà réglé**.
- R711-16 (LEGIARTI000033073023) : S5/F4 → LEGIARTI000052123156 : **G** — corrigé (SW-W11-S5-R711-16).
- L301-4-1 (LEGIARTI000033725351) : S8/F3 → L151-3 : **faux positif**.
- D731-3 (LEGIARTI000033823214) : S7/F3 → D731-2 : **faux positif**.
- L302-2 (LEGIARTI000033973020) : S7/F3 → L302-1 : **faux positif**.
- R302-1-1 (LEGIARTI000036662013) : S8/F3 → L101-2 : **faux positif**.
- L631-19 (LEGIARTI000037650025) : S7/F3 → L442-8-1 : **faux positif**.
- L423-16 (LEGIARTI000037668236) : S8/F3 → L313-13 : **faux positif**.
- L421-2 (LEGIARTI000037668612) : S8/F3 → L215-10 : **faux positif**.
- L443-15 (LEGIARTI000037669097) : S5/F4 → LEGIARTI000053151467 : **G** — corrigé (SW-W11-S5-L443-15).
- R*442-3-3 (LEGIARTI000038688721) : S1/F1 → L442-3-4 : **déjà réglé**.
- R411-6 (LEGIARTI000038688767) : S1/F1 → L423-2 : **déjà réglé** ; S1/F1 → L481-1-2 : **déjà réglé** ; S1/F1 → L481-1-1 : **déjà réglé**.
- L862-3 (LEGIARTI000038814753) : S5/F4 → LEGIARTI000054475023 : **G** — corrigé (SW-W11-S5-L862-3).
- L843-4 (LEGIARTI000038814833) : S7/F3 → L843-3 : **faux positif**.
- L822-5 (LEGIARTI000038814936) : S8/F3 → L313-12 : **faux positif**.
- L353-15-2 (LEGIARTI000038833832) : S3/F3 (échantillon) → L724-1 : **faux positif**.
- L631-12 (LEGIARTI000038834038) : S8/F3 → L351-2 : **déjà réglé**.
- L445-2 (LEGIARTI000038834104) : S8/F3 → R331-1 : **G** — corrigé (SW-W11-S8-L445-2).
- R445-5 (LEGIARTI000038863437) : S1/F1 → L452-4-1 : **déjà réglé**.
- R843-5 (LEGIARTI000038878637) : S7/F3 → L843-1 : **faux positif**.
- R843-2 (LEGIARTI000038878643) : S7/F3 → L843-1 : **faux positif**.
- R825-1 (LEGIARTI000038878788) : S8/F3 → R142-6 : **faux positif**.
- R824-16 (LEGIARTI000038878839) : S5/F4 → LEGIARTI000053470497 : **faux positif**.
- R824-13 (LEGIARTI000038878847) : S5/F4 → LEGIARTI000053470503 : **faux positif**.
- R824-11 (LEGIARTI000038878851) : S4/F4 → LEGIARTI000053470490 : **m** ; S5/F4 → LEGIARTI000053470490 : **faux positif**.
- R824-9 (LEGIARTI000038878857) : S4/F4 → LEGIARTI000053470478 : **m** ; S5/F4 → LEGIARTI000053470478 : **faux positif**.
- R824-8 (LEGIARTI000038878859) : S5/F4 → LEGIARTI000053470481 : **faux positif**.
- R824-7 (LEGIARTI000038878861) : S5/F4 → LEGIARTI000053470483 : **faux positif**.
- R824-6 (LEGIARTI000038878863) : S5/F4 → LEGIARTI000053470485 : **faux positif**.
- R824-4 (LEGIARTI000038878867) : S5/F4 → LEGIARTI000053470467 : **faux positif**.
- R472-1 (LEGIARTI000038928787) : S1/F1 → L441-3 : **déjà réglé**.
- D31-10-3 (LEGIARTI000038973589) : S8/F3 → L128-1 : **faux positif**.
- D331-7 (LEGIARTI000038974860) : S8/F3 → L122-1 : **faux positif**.
- R213-2 (LEGIARTI000039041931) : S1/F1 → L213-2 : **déjà réglé**.
- R481-11 (LEGIARTI000039042810) : S1/F1 → L482-3-1 : **déjà réglé**.
- R441-23 (LEGIARTI000039043017) : S1/F1 → L441-3 : **déjà réglé**.
- R441-12 (LEGIARTI000039043098) : S1/F1 → L441-2-5 : **déjà réglé**.
- R631-20 (LEGIARTI000039043600) : S8/F3 → R111-11 : **déjà réglé** ; S8/F3 → R111-5 : **déjà réglé** ; S8/F3 → R129-12 : **déjà réglé** ; S8/F3 → R111-16 : **déjà réglé** ; S8/F3 → R111-18-3 : **déjà réglé** ; S8/F3 → R111-18-1 : **déjà réglé** ; S8/F3 → R111-10 : **déjà réglé** ; S8/F3 → R111-18-2 : **déjà réglé** ; S8/F3 → R111-20 : **déjà réglé** ; S8/F3 → R111-6 : **déjà réglé** ; S8/F3 → R111-15 : **déjà réglé** ; S8/F3 → R111-18 : **déjà réglé** ; S8/F3 → R111-8 : **déjà réglé** ; S8/F3 → R111-3 : **déjà réglé** ; S8/F3 → R111-14 : **déjà réglé**.
- D331-104 (LEGIARTI000039048258) : S8/F3 → R353-165-4 : **m**.
- R365-1 (LEGIARTI000039048439) : S8/F3 → R331-1 : **G** — corrigé (SW-W11-S8-R365-1) ; S8/F3 → R381-5 : **m**.
- Annexe I à l'article D331-65 (LEGIARTI000039049354) : S1/F1 → L831-2 : **déjà réglé**.
- Annexe à l'article R422-6 (LEGIARTI000039049534) : S1/F1 → L451-5 : **faux positif** ; S1/F1 → L443-14 : **faux positif**.
- Annexe à l'article R422-1 (LEGIARTI000039049603) : S1/F1 → L443-14 : **faux positif**.
- L621-6 (LEGIARTI000039279909) : S5/F4 → LEGIARTI000052846041 : **G** — corrigé (SW-W11-S5-L621-6).
- R423-85 (LEGIARTI000039652810) : S7/F3 → L423-1-2 : **faux positif**.

Revue IA : ce travail ne vaut pas validation par un juriste.
