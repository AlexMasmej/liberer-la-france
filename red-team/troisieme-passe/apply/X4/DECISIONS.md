# X4 : décisions sur les 8 défauts grossiers du quatrième audit et les 7 constats incidents (S14)

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 tools/cite.py` et sqlite en `mode=ro`. Les pièces citées sont sous `evidence/cited/production-20261029/`.

Chaque texte est dérivé de la proposition actuelle par des remplacements exacts, contrôlés à l'occurrence près. Le script de construction relit la production au moment de la génération. Rien n'a été écrit en production.

## Bilan

- **Défauts corrigés :** 8 sur 8.
- **Constats incidents S14 :** 4 corrigés, dont 2 se recoupent avec K058 et K098. Les 3 autres ne sont pas corrigés : 2 sont déjà réglés et 1 est un faux positif.
- **`apply/X4/changes.json` :** 16 articles. `check_changes.py X4` donne `problems: []`, avec 16 lignes construites et 16 validées.
- **Variante `apply/Y12x/` :** l'annexe I à l'article D353-59 appartient au groupe Y12. 1 ligne, `problems: []`.
- **Diagnostics, tous voulus :**
  - renvois ajoutés : L2314-20, L2314-21, L2314-22, L2314-23, L2314-18, L2314-19 et L6323-17-5-1 ;
  - rapports de longueur sur L2314-18, L2314-20, L2314-21 et l'article 79 de l'annexe I.
- **Point technique :** les lignes L2314-19, L2314-20, L2314-21 et D6123-26-1 portent un bloc `reference_coherence` calculé sur l'ancienne proposition. `check_changes` ne le recalcule pas, et le validateur ne l'a pas refusé.

## Par défaut

1. **K011, annexe II art. 74 S septies (CGI 150 VL) : appliqué.**
   - Le circuit d'exportation n'est conservé que pour les exportations antérieures au III de 150 VI. Il s'agit de la déclaration accompagnée du paiement avant les formalités douanières, puis de sa présentation en douane, avec renvoi au 2° du I de 150 VM dans sa rédaction applicable à la date de l'exportation.
   - La mention de l'exportateur au deuxième alinéa est bornée de la même façon.
   - Une phrase écarte toute option, déclaration, justification ou paiement pour une exportation sans cession postérieure.
   - La révocabilité et sa transition sont inchangées.
   - Le motif, qui disait le « circuit d'exportation conservé », est rectifié.
   - Un effet de coordination est ajouté. La mesure reste comptée à 150 VI.
2. **K041, CSS D351-1-15 : appliqué (retour à la source).**
   - J'ai retiré la condition suspensive, qui attendait une modification de L351-4-2 que le projet ne fait pas.
   - L'article redevient `retained_unchanged` et reprend son motif de maintien d'origine.
   - La source « égal ou supérieur à 80 % » conserve le seuil favorable. La faveur n'est pas étendue, et L351-4-2 n'est pas touché.
3. **K202, travail L2314-18 à L2314-21 : appliqué.**
   - **L2314-20 et L2314-21.** Les salariés temporaires et les salariés portés liés à l'entreprise lors de la confection des listes votent et sont éligibles sans ancienneté, comme les autres salariés. Le rattachement suit L2314-22 pour l'intérim et le contrat en cours pour le portage, y compris sans prestation.
   - **Règles propres conservées pour les élections partielles d'un cycle antérieur :**
     - l'intérim garde les trois et six mois, la totalisation des missions et du CDI, intermissions comprises, l'absence de remise à zéro en cas de conversion, les fenêtres de douze et dix-huit mois et leur réduction à six mois ;
     - le portage reste régi par les règles du scrutin antérieur, rappelées expressément.
     - Pour L2314-20, cette réserve manquait ; les notes de L2314-21, L2314-24 et L2314-25 la demandaient.
   - **L2314-18 et L2314-19.** La réserve des « conditions spéciales » renvoie désormais à L2314-20 et L2314-21. La condition de présence des salariés mis à disposition (L2314-23) est maintenue.
   - Les motifs fondés sur un « seuil général d'un an » sont corrigés.
   - *Pour l'auteur :* pour les élections partielles d'intérimaires, j'ai gardé la totalisation favorable déjà proposée, intermissions comprises, et non la seule règle ancienne. L2314-10 renvoie, lui, aux dispositions de l'élection précédente.
4. **K058, travail R4224-17, avec les constats S14 sur R4215-2 et R4211-3 : appliqué.**
   - **R4224-17.** Le renvoi « prévu à l'article R. 4211-3 » de la source est rétabli. La phrase « sans rétablir une obligation de constitution après l'abrogation de cet article » est supprimée. L'allègement relatif à l'éclairage est conservé.
   - **R4215-2.** L'article revient à la source et redevient `retained_unchanged` : le dossier technique fait partie du dossier de maintenance, sans condition.
   - **R4211-3.** Seules les notes changent : sa version de 2027 (LEGIARTI000052645178) le maintient, et ce n'est pas une abrogation sans successeur.
   - Aucune proposition n'est nécessaire sur la version de 2027, puisque l'article est maintenu.
5. **K098, annexe I art. 79, 81 et 85, avec le constat S14 V02 : appliqué.**
   - **81.** Il ne maintient plus l'information de distillation de l'article 85, que sa proposition abroge. La mention est remplacée par « les pouvoirs de contrôle prévus par les dispositions distinctes ».
   - **79.** Le renvoi devient « 80, 82 à 84 et 87 », et la clause de non-rétablissement vise aussi 85.
   - Les motifs, les notes et le bilan d'impact sont mis en cohérence.
6. **K299, CCH annexe I à D353-59 (variante Y12x) : appliqué. L'annexe II à D353-190 est déjà réglée.**
   - À l'article 7, 3° a) et b), la formule de l'annexe I à D353-1 est reprise : « subventions prévues au 1° […] ou […] anciens 2° ou 3° […] dans leur rédaction applicable à la date de leur octroi ».
   - Les seuils de 30 % et 10 % sont inchangés.
   - L'annexe II à D353-190, art. 1, ne vise déjà plus R331-15.
   - *Pour l'auteur :* le 1° actuel couvre toutes les opérations de D331-1. La formule jumelle est donc reprise telle quelle ; elle n'invente pas une correspondance plus fine avec les anciens 2° et 3°.
7. **K260, annexe II art. 95 ZE et 95 ZJ (CGI 170 ter) : appliqué.**
   - **95 ZE.** Le 2° (« conserver un exemplaire ») est abrogé. La transition ne vise plus que l'information du 1°. La dispense du second exemplaire s'applique aux contrats en cours, sans avenant.
   - **95 ZJ.**
     - La convention devient à durée indéterminée.
     - Le professionnel peut la dénoncer à tout moment.
     - L'administration la dénonce par décision motivée, avec un préavis de trois mois au moins, qui est conservé.
     - La restitution court à compter de la notification de la dénonciation.
     - Les conventions en cours se poursuivent sans nouvelle signature.
   - Les motifs et notes périmés sont rectifiés : il n'y a plus de « durée légale de trois ans », et 170 ter n'impose plus le double.
8. **K290, travail D6123-26-1 : appliqué.**
   - Un IV est ajouté. À compter du 1er janvier 2027, les fonds de transition professionnelle sont versés à l'instance paritaire nationale, qui les répartit et les verse aux commissions régionales. Le circuit suit le 5° de L6123-5 et le 3° de L6323-17-5-1, dans leurs versions de 2027.
   - Le III cesse de s'appliquer à cette date, et le II est rattaché au 5° bis.
   - Les versements antérieurs sont acquis. Aucune transmission ni aucun critère nouveau.
   - L'article, jusqu'ici maintenu, passe en `rewrite_draft` / `coordination_only`.
   - *Réserve documentaire :* aucun décret d'application de la loi n° 2025-989 n'est au corpus.

## Constats incidents (S14)

1. **R4215-2 et R4211-3 : corrigés** avec K058 (point 4).
2. **Annexe IV 41 septies D : corrigé.** Le renvoi à 242 nonies J de l'annexe II, abrogé, est remplacé par l'article 289 bis du CGI (RT-P1-ANNEXES-02). Les 26 données du I et le caractère facultatif du II sont inchangés.
3. **Annexe IV 41 septies I : non corrigé, faux positif (non G).** Il ne fixe que le protocole sécurisé des transmissions des plateformes, et un flux subsiste vers l'annuaire de 289 bis III.
4. **Annexe III art. 79 (INC-U08-01) : corrigé.** « Le délai […] prévu à l'article 84 demeure applicable » devient « Une nouvelle option peut être exercée sans délai après une renonciation, l'article 84 étant abrogé ». Les notes et le bilan d'impact suivent.
5. **Travail L6323-17-5-1, versions 2027 et 2028 (INC-U10-01) : déjà réglé.** Les deux versions ont une proposition qui supprime la transmission systématique.
6. **CSS L245-6, version future (INC-U10-02) : déjà réglé.** LEGIARTI000054703326 a une proposition de suppression.
7. **Annexe I art. 81, 85 et 79 : corrigés** avec K098 (point 5).

Rien de ceci n'est une réécriture de style. Je n'ai ajouté aucune formalité ni sanction de remplacement, et n'ai étendu aucune faveur non décidée. Les droits acquis et les transitions sont conservés.

Revue IA : rien de ceci ne vaut validation par un juriste.
