# X6 : décisions sur les 10 défauts grossiers du cinquième audit (H01 à H10)

Lecture faite en production, en lecture seule, le 29 octobre 2026 (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite en `mode=ro`). Les pièces citées sont sous `evidence/cited/production-20261029/`. Rien n'a été écrit en production.

Les textes sont produits par `apply/X6/build_x6.py`. Le script relit la production au moment de la génération et fait des remplacements exacts, contrôlés à l'occurrence près. Il vérifie aussi que chaque citation d'impact (`source_quote`, `proposed_quote`) est un passage exact.

Revue IA, sans validation par un juriste.

## Bilan

- **Défauts corrigés :** 10 sur 10. Aucun n'était déjà réglé en production.
- **Articles modifiés :** 23 lignes au total.
  - `apply/X6/` : 16 lignes.
  - Variantes, pour les articles attribués à un autre groupe :
    - `apply/W08z/` : D5134-1 et D5134-3, 2 lignes ;
    - `apply/J09z/` : annexe II, article 74 SI, 1 ligne ;
    - `apply/W02z/` : A932-4-1 du code de la sécurité sociale, 1 ligne ;
    - `apply/A3z/` : les deux versions de l'article 200 du CGI, 2 lignes ;
    - `apply/Y06z/` : R5212-2-4, 1 ligne.
- **Contrôle :** `python3 -B apply/check_changes.py <dossier>` donne `problems: []` pour les six dossiers. Toutes les lignes sont construites et validées.
- **Diagnostics, tous voulus :**
  - longueur : 50 sexies G, L7123-10, R5212-2-5, 371 ter D et 371 ter H, en raison d'un alinéa de transition ou d'un corps d'abrogation plus long qu'une source très courte ;
  - renvois : R5212-1 retiré et L243-6-3 ajouté (R5212-2-3) ; L243-6-3 et L5212-5-1 ajoutés (R5212-2-5) ; R5212-1 retiré, D5212-8 et L5212-5-1 ajoutés (R5212-2-4) ; L5132-1 retiré (D5134-1) ; renvois CIBS déjà présents sur la version 2026 de l'article 200.
- **Point technique :** 74 SI, D5134-1, D5134-3 et L7123-10 portent un bloc `reference_coherence` calculé sur l'ancienne proposition. `check_changes` ne le recalcule pas, et le validateur ne l'a pas refusé.

## Par défaut

1. **H091, travail D5134-1 et D5134-3 (variante W08z) : appliqué, abrogation.**
   - **Constat :** le régime législatif du contrat emploi-jeune (L5134-1 à L5134-19) est abrogé. Ses versions LEGI prennent fin le 8 août 2015. Les propositions ajoutaient pourtant des règles pour des contrats uniques futurs. Les notes disaient à tort que L5134-1 et L5134-2 étaient « absents du corpus ».
   - **Correction :** les deux articles sont abrogés pour l'avenir (`full_repeal`), sans pièce ni condition de remplacement. Les conventions, contrats, aides, contrôles et recours antérieurs restent régis par leurs règles jusqu'à leur terme. Le CUI (L5134-19-1 et suivants) n'est pas visé.
   - **Pour l'auteur :** D5134-2 et D5134-4 à D5134-13 relèvent du balayage M02 (pistes S16 et S17). Leur alignement sur la même solution est à vérifier par le coordinateur.

2. **H161, annexe II 74 SI (variante J09z) : appliqué.**
   - **Constat :** 150 U proposé supprime la condition de remploi du 4° du II pour les cessions faites à compter de la loi. 74 SI demandait toujours les pièces de remploi.
   - **Correction :**
     - la justification du remploi, sur demande seulement, est réservée aux cessions antérieures ;
     - aucune justification n'est exigée pour les cessions nouvelles ;
     - les pièces de 150 VA III et de 150 VB II restent inchangées ;
     - la formule « remploi de l'indemnité » de la source est conservée, sans être étendue.
   - Les notes erronées sont corrigées : elles disaient que le projet « garde le remploi intégral sous douze mois ».

3. **H274, CGI 219 bis : appliqué, selon l'orientation donnée.**
   - **Correction :** pour les exercices ouverts à compter de l'entrée en vigueur des V et VI de 219, le taux de 24 % devient 20 %. Les taux de 10 % et de 15 % sont maintenus.
   - **Ce qui n'est pas fait :** l'imposition reste annuelle. Ces organismes ne distribuent pas : leur appliquer le report jusqu'à la distribution reviendrait à les exonérer. Ce serait un avantage au-delà du droit commun proposé, qui n'a pas été décidé.
   - **Transition :** les exercices antérieurs restent régis par les règles qui leur étaient applicables.
   - **Contrôles :** le motif erroné (« Aucun conflit [...] n'est établi ») est corrigé. Les renvois de 1668, 119 bis, 187, 234 quaterdecies et de l'annexe III (362, 381 quater) restent exacts.
   - **Pour l'auteur :** il s'agit d'une baisse d'impôt (`material_reduction`), non chiffrée. L'égalité devant les charges publiques reste à confirmer.

4. **H056, annexe IV 50 sexies G, H et I : appliqué (défaut unique, trois articles).**
   - **Constat :** 290 quater est abrogé, et le V de 50 sexies B écarte déjà la billetterie fiscale pour les spectacles futurs.
   - **Correction pour les spectacles futurs :**
     - **G :** la comptabilité des billets, leur présentation et les dispositifs de contrôle de conformité ne valent plus que pour les spectacles antérieurs. L'accès des agents ne joue plus que pour les vérifications qui ont un fondement légal distinct.
     - **H :** le relevé quotidien des billets émis est borné aux spectacles antérieurs. Les obligations comptables et déclaratives de droit commun sont réservées.
     - **I :** la conformité au cahier des charges de 1993 est bornée aux spectacles antérieurs. La phrase « Les obligations de conformité du I et les contrôles de l'article 50 sexies G demeurent applicables » ne vise plus que ces spectacles.
   - **Garanties :** aucun billet, registre ni équipement de remplacement n'est exigé. Les pièces anciennes sont conservées, sans mise en conformité.
   - **Pour l'auteur :** 50 sexies C, D et E gardent des règles sur les billets. Le V de B couvre déjà C ; D et E ne sont pas traités ici. 50 sexies B appartient à A7 et relève de M07 au balayage 5. Le cahier des charges de 1993 et la reprise CIBS L. 216-48 sont hors corpus.

5. **H117, CGI 1729 C ter : appliqué.**
   - **Correction :** l'exclusion d'amende vise désormais « l'obligation de déclaration annuelle de l'utilisation d'un dispositif transfrontière prévue au dernier alinéa du II de l'article 1649 AG dans sa rédaction antérieure à la loi supprimant cette déclaration ».
   - **Effet :** les échéances anciennes restent hors amende. L'obligation supprimée ne peut plus être sanctionnée. Les plafonds sont inchangés.
   - **Pour l'auteur :** la directive 2011/16/UE n'a pas été consultée.

6. **H068, travail L7123-10 : appliqué.**
   - **Contrats antérieurs :** les trois alinéas d'origine sont conservés (indemnité à chaque prestation, au moins un dixième).
   - **Contrats uniques :**
     - la fin d'une prestation ne rompt pas le contrat ;
     - les congés sont pris en nature, sans paiement de remplacement pendant l'emploi ;
     - à la fin effective du contrat, l'indemnité reste garantie à au moins un dixième, sans condition d'ancienneté ni plafond, et sans double indemnisation ;
     - une conversion ne déclenche pas à elle seule le paiement.
   - Cette rédaction est alignée sur L1242-16 et L1251-58-4 proposés.
   - **Pour l'auteur :** la conformité à l'article 7 de la directive 2003/88/CE est à confirmer sur source primaire. Les accords collectifs des mannequins n'ont pas été lus.

7. **H198, CSS A932-4-1 (variante W02z) : appliqué, coordination.**
   - **III :** il vise R932-4-14 « dans sa rédaction antérieure à son abrogation au 31 décembre 2017 ».
   - **IV :**
     - la répartition des droits de R932-4-20, qui renvoie à un arrêté de bases techniques, garde les tables (désignées par A931-10-10 dans sa rédaction antérieure au 1er janvier 2016) et les taux ;
     - la provision mathématique théorique et les équivalences gardent ces modalités pour les seules périodes antérieures ;
     - depuis le 31 décembre 2017, la provision suit l'arrêté auquel renvoie R932-4-15.
   - **Inchangé :** taux, I, II et étalement historique. Les notes erronées (« absents de l'extraction ») sont corrigées.
   - **Pour l'auteur :** les dates sont tirées du corpus LEGI, et l'arrêté R441-21 du code des assurances est hors corpus. Aucune table de remplacement n'a été inventée.

8. **H228, CGI 200, deux versions LEGIARTI000053543932 et LEGIARTI000053154489 (variante A3z) : appliqué.**
   - **Correction :** le chapeau du 1 reprend la structure de la source : « Ouvrent droit à une réduction d'impôt sur le revenu égale à 66 % de leur montant, dans la limite de 20 % du revenu imposable, les dons et versements [...] au profit : ».
   - **Inchangé :** le reste des deux propositions et le bilan d'impact.

9. **H309, travail R5212-2-3 à R5212-2-5 (R5212-2-4 en variante Y06z) : appliqué, abrogation.**
   - **Constat :** la base légale, L5212-5-1, est abrogée au 1er janvier 2020 (corpus). Le rescrit opposable sur l'obligation d'emploi relève de L243-6-3 du CSS. Cet article est déjà opposable « tant que la situation de fait exposée ou la législation appliquée n'ont pas été modifiées », donc sans limite de durée.
   - **Correction :**
     - les trois articles sont abrogés, sans demande ni pièce de remplacement ;
     - les demandes déjà adressées n'ont pas à être renouvelées sur ce fondement ;
     - les positions notifiées gardent leurs effets, et aucune position expirée n'est rétablie ;
     - les déclarations des années antérieures gardent leurs règles ;
     - les droits et recours antérieurs sont préservés.
   - Les notes erronées (« non vérifiable ») sont corrigées.
   - **Pour l'auteur :** reporter, s'il le souhaite, l'absence de caducité dans les textes d'application de L243-6-3 (R243-43-x, non relus).

10. **H160, annexe II 371 ter A à 371 ter H : appliqué, abrogation d'ensemble (8 articles).**
    - **Constat :** 1649 quater N est abrogé (fin le 16 février 2025). Il ne servait qu'au c du 1° du 7 de l'article 158 (majoration de 1,25), lui-même abrogé dans la version en vigueur.
    - **Correction :**
      - aucune demande n'est reçue ni instruite ;
      - aucune convention n'est conclue, renouvelée ou reconduite ;
      - les conventions en cours prennent fin sans formalité (371 ter E) ;
      - aucune information des clients n'est exigée ;
      - les impositions et recours des périodes antérieures restent régis par leurs règles.
    - **Statut :** C et D, jusque-là maintenus, passent en `full_repeal`. Les articles 371 ter I à S (commissions des valeurs locatives) ne sont pas touchés.
    - **Réserve :** l'article 11 de la loi n° 2025-127 n'a pas été lu au JORF. S'il avait transféré le régime, il faudrait réécrire les renvois au lieu d'abroger. C'est lié à RT-P1-ANNEXES-05.

## Résumé

10 défauts G du cinquième audit, 10 corrigés, 23 lignes réparties dans 6 dossiers (X6 et les variantes W08z, J09z, W02z, A3z et Y06z), tous à `problems: []`. Aucune formalité ni sanction de remplacement n'est créée. Les droits acquis et les transitions sont conservés. Seule baisse d'impôt : le taux de 219 bis passe de 24 % à 20 %, selon l'orientation donnée.

Points pour l'auteur :
- aligner D5134-2 et suivants avec M02 ;
- traiter 50 sexies D et E ;
- vérifier l'article 11 de la loi n° 2025-127 et le droit de l'Union (directives 2003/88/CE et 2011/16/UE) ;
- confirmer les dates d'abrogation tirées du corpus LEGI.

Revue IA, sans validation par un juriste.
