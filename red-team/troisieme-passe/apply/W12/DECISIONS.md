# W12 : balayage par famille de défauts (CCH), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-W12.json`, soit 67 articles et 84 pistes. Contrôle : `python3 -B apply/check_changes.py W12` donne 12 lignes construites, 12 validées et `problems` vide. Les diagnostics sont voulus : renvois changés (R423-91 retiré de R441-9, renvois R824 de l'annexe de 2027, L302-7 et L353-7 déjà retirés de L371-4), réductions déjà déclarées, longueur de D317-7 inchangée par cette passe.

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 14, toutes corrigées (10 défauts, 12 lignes) |
| m | 2 (dispense de L443-14 abrogé dans les annexes I et II à R423-86, sans effet) |
| déjà réglé | 13 |
| faux positif | 55 |

Corrections : 12 lignes. Dix en mode `replace` : L126-8, R441-9, L421-3, L422-3, L421-4, L342-14, R421-1, L183-4, L371-4 et D317-7 (ce dernier n'est attribué à aucun groupe). Deux en mode `new` : l'annexe II à l'article R. 373-3 dans sa version du 1er janvier 2027 et L183-4 dans sa version du 1er janvier 2028. Aucune demande à un autre groupe, aucun `skipped`.

## Défauts confirmés et corrigés

- **L126-8** (LEGIARTI000041565235), S7/F3, G, `replace`.
  - Défaut : « la garantie prévue au dernier alinéa de l'article L. 543-1 ». La proposition de L543-1 ajoute deux alinéas après la garantie : le dernier réserve les astreintes suspendues.
  - Correction : « au sixième alinéa ». Le motif, les notes et le bilan d'impact sont mis à jour.
- **R441-9** (LEGIARTI000041615492), S8/F3, G, `replace`.
  - Défaut : la liste « R. 421-15, R. 422-2, R. 422-9-1, R. 423-91 et R. 481-5 » vise R*423-91. Cet article a été abrogé au 1er septembre 2019 par le décret n° 2019-911, art. 1er. La note qui le disait absent du corpus était fausse.
  - Correction : le renvoi est retiré et la note rectifiée. Les règles de la commission ne changent pas.
- **L421-3, L422-3, L421-4** (LEGIARTI000044375084, LEGIARTI000053546162, LEGIARTI000053546287), S7/F3, G, 5 pistes, `replace`.
  - Défaut : « Dans le respect du dernier alinéa de l'article L. 411-2 ». La proposition de L411-2 ajoute un 17e alinéa de transition, qui devient le dernier. La règle visée, celle du compte réservé aux résultats SIEG et du dividende, est au 16e.
  - Correction : le renvoi désigne l'objet de la règle (« règles d'affectation des résultats de l'activité relevant de la gestion de services d'intérêt économique général prévues à l'article L. 411-2 »). C'est la formule que L422-2 proposé emploie déjà.
- **L342-14** (LEGIARTI000048840423), S2/F2, G, 2 pistes, `replace`.
  - Défaut : la sanction ANCOLS du I 1° b (non-respect des règles du SLS de L441-3, dans les montants de L441-11) n'a pas de borne temporelle. Or les deux articles sont abrogés, et L441-11 proposé interdit toute pénalité pour un manquement postérieur.
  - Correction : le b ne s'applique plus qu'aux manquements antérieurs, sous réserve de la loi répressive plus douce. Aucun manquement postérieur ne peut être sanctionné, y compris pour le recouvrement d'anciens suppléments.
- **R421-1** (LEGIARTI000049243543), S1/F1, G, `replace`.
  - Défaut : « les mesures de l'article L. 423-1 demeurent applicables » et « sauf dans le cas prévu à l'article L. 423-1 ». Or L423-1 est abrogé et toute dissolution ou acquisition forcée nouvelle est interdite.
  - Correction : les deux renvois sont limités aux dissolutions prononcées avant l'abrogation et à leurs liquidations. Les pouvoirs de L421-6 sont inchangés.
- **L183-4** (LEGIARTI000046123749, maintenu, et version 2028 LEGIARTI000047475406), S2/F2, G, `replace` et `new`.
  - Défaut : le délit vise toujours les « obligations imposées par » L. 152-3, que le projet abroge (comptage de l'eau froide). C'est la seule cible abrogée de la liste. La version de 2028 conserve le même renvoi.
  - Correction : L. 152-3 est retiré de la liste. Un alinéa final s'applique aux faits antérieurs, avec la loi pénale plus douce. L'article maintenu devient `rewrite_draft` (`coordination_only`). La version de 2028 reçoit la même coordination, et L. 171-5 y est conservé.
- **Annexe II à l'article R. 373-3, version 2027** (LEGIARTI000053470634, successeur de LEGIARTI000047400423), S5/F4, G, `new`.
  - Défaut : la version issue du décret n° 2026-84, sans proposition, reproduit à l'identique les formalités que la réforme supprime : préavis d'un mois, justificatifs, paraphe, carnet annuel, dossier annuel au préfet, liste annuelle certifiée et justification des poursuites. Elles reviendraient le 1er janvier 2027.
  - Correction : la proposition en vigueur est reportée en entier, à deux exceptions près.
    - L'article 7 est coordonné avec le régime des impayés de 2027 :
      - R824-1 assimile le gestionnaire au bailleur ;
      - R824-2 définit l'impayé ;
      - R824-3 fixe le signalement à deux mois ;
      - R824-6 à R824-11 régissent le maintien et la suspension, cette dernière étant décidée par la commission saisie en application de L824-2.
    - La phrase qui bornait l'application au 1er janvier 2027 est retirée.
  - Les références mortes de la version officielle (R824-4 ancien, R824-31, R824-1 comme définition) sont remplacées.
- **D317-7** (LEGIARTI000039047511, non attribué ; piste AUDIT sur R321-13), F3, G, `replace`.
  - Défaut : « le fondement du dernier alinéa de l'article R. 321-13 ». R321-13 proposé ajoute un 6e alinéa de transition ; le non-cumul est désormais au 5e, que R318-9 vise déjà.
  - Correction : « cinquième alinéa », dans le texte, le motif et les notes.
- **L371-4** (LEGIARTI000052093580), piste AUDIT F3+F4, G, `replace`.
  - Défaut : le 4° réécrit renvoie au « code général des impôts de Mayotte » pour le secret des agents. Cela contredit L313-6 proposé (CGI) et sa version 2027 (LPF).
  - Correction : « 4° (Abrogé) ». Une phrase préserve les contrôles et le secret pour les périodes antérieures.
  - La correction est sûre quelle que soit la confirmation demandée : la substitution source était déjà inopérante (« fixés » contre « fixées »).
  - Ordonnance n° 2013-837 du 19 septembre 2013 identifiée, non consultée en ligne. À coordonner avec RT-FUTTL-03 (L313-6).

## Points laissés à l'auteur

1. **Annexe II à R. 373-3, version 2027, seuil d'impayé.**
   - La version officielle garde « deux fois le montant mensuel brut de la redevance ». Ce seuil contredit R824-2 dans sa version de 2027 (trois mois après un premier défaut, ou plus de 450 €).
   - La proposition s'en remet à R824-2, comme la proposition en vigueur s'en remettait à R824-1.
   - Si l'auteur veut garder un seuil conventionnel propre, il faut le rétablir expressément.
2. **L183-4, version 2028.** La date de 2028 n'est pas celle de la réforme. La coordination ne s'applique qu'à compter de l'abrogation de L152-3.
3. **Notes dépassées non corrigées (m, F10), sur des articles non modifiés :**
   - R862-2 (« version ultérieure ... non examinée ») ;
   - L31-10-2 (« texte de substitution ... ne figurent pas dans le lot ») ;
   - annexe II à R. 373-3 en vigueur (« versions de remplacement au 1er janvier 2027 ... ne sont pas fournis »).
4. **Annexes I et II à R423-86.** La dispense de L443-14, abrogé, est sans objet et sans effet. Elle n'est pas corrigée, car ce serait une réécriture de style et la faveur est conservée.
5. **D317-7** n'est attribué à aucun groupe dans `assignment.json`. Le coordinateur doit vérifier qu'aucun autre groupe ne le modifie.

## Une ligne par piste

| N° | Article (version) | Piste → cible | Qualification | Correction |
|---|---|---|---|---|
| 1 | R862-2 (LEGIARTI000041419269) | S5/F4 → LEGIARTI000054394059 | faux positif | — |
| 2 | L435-1 (LEGIARTI000041466716) | S2/F2 → L452-4-1 | faux positif | — |
| 3 | L452-4 (LEGIARTI000041473209) | S2/F2 → L452-4-1 | faux positif | — |
| 4 | L452-4 (LEGIARTI000041473209) | S2/F2 → L441-3 | faux positif | — |
| 5 | L452-4 (LEGIARTI000041473209) | S2/F2 → L831-2 | faux positif | — |
| 6 | L126-8 (LEGIARTI000041565235) | S7/F3 → L543-1 | G | replace L126-8 |
| 7 | L183-14 (LEGIARTI000041570625) | S2/F2 → L126-19 | déjà réglé | — |
| 8 | R441-5 (LEGIARTI000041615478) | S1/F1 → L302-9-1-2 | faux positif | — |
| 9 | R441-9 (LEGIARTI000041615492) | S8/F3 → R423-91 | G | replace R441-9 |
| 10 | L511-16 (LEGIARTI000042338102) | S7/F3 → L511-11#1 | faux positif | — |
| 11 | L511-16 (LEGIARTI000042338102) | S7/F3 → L511-11#2 | faux positif | — |
| 12 | L511-16 (LEGIARTI000042338102) | S7/F3 → L511-11#3 | faux positif | — |
| 13 | L302-16-1 (LEGIARTI000042857888) | S5/F4 → LEGIARTI000053151493 | déjà réglé | — |
| 14 | L302-16-2 (LEGIARTI000042857903) | S5/F4 → LEGIARTI000053151487 | déjà réglé | — |
| 15 | R511-11 (LEGIARTI000042877845) | S7/F3 → L511-11 | faux positif | — |
| 16 | R511-9 (LEGIARTI000042877867) | S7/F3 → L511-11 | faux positif | — |
| 17 | R511-6 (LEGIARTI000042877949) | S7/F3 → L511-11#1 | faux positif | — |
| 18 | R511-6 (LEGIARTI000042877949) | S7/F3 → L511-11#2 | faux positif | — |
| 19 | R126-15 (LEGIARTI000043818595) | S8/F3 → R111-22 | faux positif | — |
| 20 | R165-19 (LEGIARTI000043819361) | S2/F2 → R165-16 | déjà réglé | — |
| 21 | R173-1 (LEGIARTI000043819413) | S8/F3 → R111-22 | faux positif | — |
| 22 | R173-6 (LEGIARTI000043819425) | S8/F3 → R312-3 | faux positif | — |
| 23 | R174-22 (LEGIARTI000043819501) | S8/F3 → R111-22 | faux positif | — |
| 24 | L421-3 (LEGIARTI000044375084) | S7/F3 → L411-2#1 | G | replace L421-3 |
| 25 | L421-3 (LEGIARTI000044375084) | S7/F3 → L411-2#2 | G | replace L421-3 |
| 26 | R863-11 (LEGIARTI000044636797) | S8/F3 → R142-6 | faux positif | — |
| 27 | R452-25-1 (LEGIARTI000044637005) | S1/F1 → L452-4-1 | déjà réglé | — |
| 28 | R452-25-1 (LEGIARTI000044637005) | S8/F3 → L128-1 | faux positif | — |
| 29 | L302-7-1 (LEGIARTI000045201381) | S7/F3 → L302-7#1 | faux positif | — |
| 30 | L302-7-1 (LEGIARTI000045201381) | S7/F3 → L302-7#2 | faux positif | — |
| 31 | L301-5-1 (LEGIARTI000045211697) | S7/F3 → L302-3 | faux positif | — |
| 32 | Annexe I à l'article R423-86 (LEGIARTI000045646952) | S1/F1 → L423-2 | déjà réglé | — |
| 33 | Annexe I à l'article R423-86 (LEGIARTI000045646952) | S1/F3 → L443-14 | m | non (m, sans effet) |
| 34 | Annexe II à l'article R423-86 (LEGIARTI000045646995) | S1/F3 → L443-14 | m | non (m, sans effet) |
| 35 | R113-13 (LEGIARTI000045966369) | S8/F3 → L111-14 | faux positif | — |
| 36 | L183-4 (LEGIARTI000046123749) | S2/F2 → L152-3 | G | replace L183-4 + new L183-4 (2028) |
| 37 | R302-1-3 (LEGIARTI000046415207) | S1/F1 → L302-8 | déjà réglé | — |
| 38 | R435-3 (LEGIARTI000047216633) | S1/F1 → L302-9-1 | faux positif | — |
| 39 | R435-3 (LEGIARTI000047216633) | S1/F1 → L302-7 | faux positif | — |
| 40 | R374-1 (LEGIARTI000047398611) | S8/F3 → R313-1 | faux positif | — |
| 41 | Annexe II à l'article R. 373-3 (LEGIARTI000047400423) | S5/F4 → LEGIARTI000053470634 | G | new Annexe II R. 373-3 (2027) |
| 42 | R541-3 (LEGIARTI000047547395) | S8/F3 → R521-6 | faux positif | — |
| 43 | R541-4 (LEGIARTI000047547398) | S8/F3 → R521-6 | faux positif | — |
| 44 | D861-10 (LEGIARTI000047985420) | S8/F3 → L351-8 | faux positif | — |
| 45 | D842-16 (LEGIARTI000047985424) | S8/F3 → L351-8 | faux positif | — |
| 46 | R823-4 (LEGIARTI000047985801) | S8/F3 → L351-8 | faux positif | — |
| 47 | R822-6 (LEGIARTI000047985814) | S8/F3 → L351-8 | faux positif | — |
| 48 | L31-10-2 (LEGIARTI000048826443) | S5/F4 → LEGIARTI000053151472 | faux positif | — |
| 49 | L342-14 (LEGIARTI000048840423) | S2/F2 → L441-11 | G | replace L342-14 |
| 50 | L342-14 (LEGIARTI000048840423) | S2/F2 → L441-3 | G | replace L342-14 |
| 51 | L313-19-2 (LEGIARTI000048840464) | S8/F3 → L313-23 | faux positif | — |
| 52 | R421-1 (LEGIARTI000049243543) | S1/F1 → L423-1 | G | replace R421-1 |
| 53 | D319-14 (LEGIARTI000049356951) | S2/F2 → D319-11 | déjà réglé | — |
| 54 | L442-8-1-2 (LEGIARTI000049392176) | S7/F3 → L441-1 | faux positif | — |
| 55 | L511-15 (LEGIARTI000049398505) | S7/F3 → L511-11 | faux positif | — |
| 56 | L511-17 (LEGIARTI000049398967) | S7/F3 → L511-11 | faux positif | — |
| 57 | D323-9 (LEGIARTI000049977460) | S7/F3 → D323-5 | faux positif | — |
| 58 | R256-7 (LEGIARTI000050005462) | S7/F3 → R256-4 | faux positif | — |
| 59 | D31-11-11 (LEGIARTI000050175502) | S2/F2 → D31-11-8 | déjà réglé | — |
| 60 | L631-9 (LEGIARTI000050623458) | S7/F3 → L631-7 | faux positif | — |
| 61 | R132-21 (LEGIARTI000050726089) | S8/F3 → L125-2-2 | faux positif | — |
| 62 | R132-20 (LEGIARTI000050726092) | S8/F3 → L125-2-2 | faux positif | — |
| 63 | R132-18 (LEGIARTI000050726098) | S8/F3 → L125-2-2 | faux positif | — |
| 64 | R132-15 (LEGIARTI000050726107) | S8/F3 → L125-2-2 | faux positif | — |
| 65 | R132-14 (LEGIARTI000050726110) | S8/F3 → L125-2-2 | faux positif | — |
| 66 | R132-12 (LEGIARTI000050726116) | S8/F3 → L125-2-2 | faux positif | — |
| 67 | R132-11 (LEGIARTI000050726120) | S8/F3 → L125-2-2 | faux positif | — |
| 68 | R132-10 (LEGIARTI000050726123) | S8/F3 → L125-2-4 | faux positif | — |
| 69 | R132-10 (LEGIARTI000050726123) | S8/F3 → L125-2-2 | faux positif | — |
| 70 | R861-5 (LEGIARTI000050811209) | S8/F3 → L351-8 | faux positif | — |
| 71 | R321-13 (LEGIARTI000051354350) | AUDIT/F3 → AUDIT | G | replace D317-7 |
| 72 | L371-4 (LEGIARTI000052093580) | AUDIT/F3+F4 → AUDIT | G | replace L371-4 |
| 73 | Annexe II à l'article D353-90 (LEGIARTI000053356309) | S2/F2 → D353-93-1 | déjà réglé | — |
| 74 | L422-3 (LEGIARTI000053546162) | S7/F3 → L411-2#1 | G | replace L422-3 |
| 75 | L422-3 (LEGIARTI000053546162) | S7/F3 → L411-2#2 | G | replace L422-3 |
| 76 | L422-3 (LEGIARTI000053546162) | S7/F3 → L302-5 | déjà réglé | — |
| 77 | L422-2 (LEGIARTI000053546225) | S7/F3 → L302-5 | déjà réglé | — |
| 78 | L421-4 (LEGIARTI000053546287) | S7/F3 → L302-5 | déjà réglé | — |
| 79 | L421-4 (LEGIARTI000053546287) | S7/F3 → L411-2 | G | replace L421-4 |
| 80 | L302-1 (LEGIARTI000053546338) | S8/F3 → L152-6 | faux positif | — |
| 81 | R163-6 (LEGIARTI000054301904) | S8/F3 → L111-22 | faux positif | — |
| 82 | R302-14 (LEGIARTI000054551251) | S7/F3 → dernier alinéa du V de l'article L. 302-5 | faux positif | — |
| 83 | R302-14 (LEGIARTI000054551251) | S7/F3 → dernier alinéa du II de l'article L. 302-5 | faux positif | — |
| 84 | R302-14 (LEGIARTI000054551251) | S7/F3 → troisième alinéa du II de l'article L. 302-5 | faux positif | — |
Le détail des citations (identifiant LEGIARTI et passage exact) de chaque piste figure dans `audit/sweeps/W12.json`.
