# Groupe A2 — décisions de la troisième passe (FUT-FISC)

Revue IA. Rien de ceci ne vaut validation par un juriste.

Lecture : `tools/cite.py` sur l'instantané `20261029T034912Z`. Chaque version modifiée a été lue en entier : source, NOTA, proposition, motif, notes et ligne de lot. Les exports sont dans `evidence/cited/20261029T034912Z/`. Contrôle : `python3 -B apply/check_changes.py A2` → 19 changements construits et validés, `problems` vide. Les diagnostics restants sont voulus : renvois CIBS ajoutés ou retirés, et retrait des formules d'amende supprimées.

## Règle commune

La loi de réforme ne peut pas entrer en vigueur avant le 1er janvier 2027. Pour chaque article, j'ai donc fait deux choses :

- la proposition de la version courante (`ABROGE_DIFF` jusqu'au 1er janvier 2027) est remplacée par le texte rebasé sur la version publiée qui lui succède ;
- le même texte est créé (mode `new`) sur la ou les versions futures (`VIGUEUR_DIFF`).

Ainsi, quelle que soit la version lue, aucune rédaction « ainsi rédigé » ne fait revivre un régime abrogé et aucune version future ne rétablit une coupe du projet. Les changements qui viennent de la LF 2025 ou des ordonnances ne sont jamais comptés comme des gains du projet.

## Objections

### RT-FUTFISC-04 (P0) — CGI 287 : appliquée

- **Articles :** 287 LEGIARTI000048826856 (replace) et LEGIARTI000051190827 (new).
- **Ce qui change :** le texte est rebasé sur la version de la LF 2025 (art. 38). On ne garde que les gains qui subsistent :
  - le délai supplémentaire d'un mois est ouvert au choix, sans demande ni autorisation, et l'acompte de 1693 reste dû ;
  - pour les exercices décalés encore au régime simplifié (VI de l'art. 38), aucun acompte semestriel n'est exigé après la réforme, et le remboursement intermédiaire sur immobilisations reste ouvert sans minimum ;
  - une clause empêche la reprise réglementaire CIBS (L. 161-1, L. 172-3) de rétablir l'autorisation.
- **Ce qui n'est pas rétabli :** le régime simplifié annuel, le 3 bis, le 3 ter et le seuil de 4 000 €.
- **Points laissés à l'auteur :**
  - le 4 garde « régime simplifié » (défaut de la source). Réserver les 60 jours aux redevables trimestriels serait une extension de faveur ;
  - coordinations hors groupe : 1693 (« autorisés ») ; annexe II 242-0 C, 242 sexies, 242 septies A et J ; annexe III 383 ter ; annexe IV 39 ;
  - les notes de 302 septies A (retained_unchanged, pas modifiable par l'outil, qui exige un `proposed_xml`) disent encore que le projet de 287 « conserve déclaration annuelle ». À corriger par le coordinateur.

### RT-FUTFISC-23 (P0) — CGI 150 VM : appliquée

- **Articles :** 150 VM LEGIARTI000030752146 (replace) et LEGIARTI000053154469 (new).
- **Ce qui change :**
  - la phrase « ne proroge pas l'application du présent article au-delà de sa date d'abrogation déjà prévue au 1er janvier 2027 » est supprimée ;
  - le texte est rebasé sur la version de l'ordonnance 2025-1247 : constatation selon L. 161-1 CIBS, recouvrement et réclamations selon le régime des taxes sur les biens et services ;
  - la suppression de la déclaration et du paiement pour les exportations sans cession est conservée ;
  - la transition couvre les faits générateurs antérieurs, y compris ceux régis par la rédaction 2027.
- **Point ouvert :** le contenu de L. 161-1 CIBS est hors corpus.

### RT-FUTFISC-02 (P1) — CGI 1741 : appliquée (`loophole_closure: true` sur la version courante)

- **Articles :** 1741 LEGIARTI000051742509 (replace), LEGIARTI000054566825 et LEGIARTI000052848545 (new).
- **Ce qui change :**
  - le champ du délit couvre de nouveau les impositions du CIBS, comme dans la version 2027. Sans cela, la TVA sortirait du délit général après la recodification ;
  - la peine complémentaire de privation des avantages fiscaux reste supprimée ;
  - le casier judiciaire est visé sans numéro d'article (versions courante et 2027). La version 2029 garde les renvois L. 5514-x du CPP ;
  - la note fausse selon laquelle « la disposition de remplacement n'est pas fournie » est retirée.
- **Pourquoi `loophole_closure` :** la correction rétablit seulement le champ que le projet déclare conserver. L'auteur peut la revoir.
- **Point ouvert :** la coquille « 2026-1247 » de la NOTA 2027 reste à vérifier.

### RT-FUTFISC-03 (P1, à confirmer) — CGI 220 Z septies : partiellement appliquée

- **Articles :** 220 Z septies LEGIARTI000048826400 (replace) et LEGIARTI000054567230 (new).
- **Ce qui est appliqué :**
  - le III est fusionné sur la base 2027 (L. 231-66 CIBS) ;
  - les conditions de mixité et de quota supprimées par la loi sur les quotas sont neutralisées de façon autonome ;
  - la dispense de location en exonération de TVA est maintenue ;
  - une garantie empêche une condition neutralisée de faire cesser la créance ;
  - les allègements du projet sont reportés : VI (modèle facultatif), IS à la distribution, transitions.
- **Pourquoi c'est sûr :** la neutralisation tient quel que soit le contenu de L. 231-66.
- **Ce qui n'est pas appliqué (`skipped`, à confirmer) :** le rebasement du IV sur L. 231-100 CIBS. Le contenu de cet article est hors corpus et il pourrait élargir les cas de cessation. Le renvoi officiel 2027 au II bis de 284 est conservé : c'est un défaut de la source, laissé à l'auteur.

### RT-FUTFISC-05 (P1, à confirmer) — CGI 256 C : appliquée pour la partie codifiée

- **Articles :** 256 C LEGIARTI000046872949 (replace) et LEGIARTI000051190942 (new).
- **Ce qui change :**
  - le dépôt exclusivement mensuel de la version 2027 est remplacé par un renvoi aux 2 à 3 bis de 287. C'est l'ouverture voulue par le projet ;
  - « souscrite mensuellement » est retiré du 6 ;
  - les autres coupes du projet sont reprises : engagement de trois ans, 31 octobre, accord au retrait, liste du 10 janvier ;
  - une clause interdit aux mesures de reprise CIBS citées par la NOTA de rétablir ces contraintes.
- **Pourquoi c'est sûr quel que soit le point à confirmer :** si l'article est abrogé, le texte est sans effet. S'il est maintenu jusqu'à la reprise, il est opérant.
- **Non appliqué (`hors corpus`) :** la réécriture des articles CIBS de reprise.
- **À noter :** 231 A (groupe A1) n'a pas besoin de modification.

### RT-FUTFISC-06 (P1, à confirmer) — CGI 99 : appliquée

- **Articles :** 99 LEGIARTI000053546818 (replace) et LEGIARTI000051190987 (new).
- **Ce qui change :**
  - le seuil de la faculté de la date bancaire renvoie au c du III de 302 septies A bis, comme la version 2027 ;
  - le seuil antérieur est conservé pour les recettes des années avant 2027 ;
  - la saisie périodique et le support commun sont inchangés.
- **Pourquoi c'est sûr :** c'est une coordination neutre, qui ne fait perdre la faveur à personne.

### RT-FUTFISC-08 (P1) — CGI 1770 duodecies : appliquée pour la partie codifiée

- **Articles :** 1770 duodecies LEGIARTI000053546759 (replace) et LEGIARTI000054567638 (new), en `full_repeal`.
- **Ce qui change :**
  - l'abrogation vise l'article dans toutes ses rédactions, y compris celle de l'ordonnance 2026-671, art. 2 ;
  - l'amende de 7 500 € est supprimée, que le certificat soit exigé par 286 ou par L. 216-40 CIBS ;
  - l'inaltérabilité, la conservation et l'article 1770 undecies sont conservés.
- **Non appliqué (`hors corpus`) :** la neutralisation de l'obligation de certificat de L. 216-40 CIBS.
- **Anomalie de source :** la NOTA de la version 2027 donne le 1er septembre 2026, alors que LEGI fait commencer la version au 1er janvier 2027.

### RT-FUTFISC-10 (P1) — CGI 1788 A : appliquée, plus une demande à A1

- **Articles :** 1788 A LEGIARTI000044983701 (replace), LEGIARTI000054566837 et LEGIARTI000053294012 (new).
- **Ce qui change :**
  - le texte est rebasé sur les renvois CIBS ;
  - l'amende de 5 % et sa formule des opérations assimilées sont supprimées ;
  - la comptabilité et les pièces ordinaires suffisent, sans registre ni double ;
  - la réforme est reportée sur la version du 1er juillet 2030, qui garde l'abrogation favorable des amendes des états récapitulatifs (a des 1 et 2) ;
  - la phrase « ne reportent pas l'abrogation du présent article prévue au 1er janvier 2027 » est supprimée. Cela règle aussi la partie 1788 A de RT-RXF01-01, que l'assignation n'attribue à aucun groupe.
- **Points laissés à l'auteur :**
  - le nouveau 2 c (amende de 15 €, information prévue à L. 216-12 CIBS) que crée la version 2030 est conservé tel que publié. Le projet ne l'a pas examiné ; le supprimer serait un arbitrage de l'auteur ;
  - la loi de réforme doit écarter le II de l'article 20 de l'ordonnance 2025-1247 en tant qu'il rétablit ce que la réforme supprime.
- **Demande de A3 intégrée (RT-FUTFISC-27) :**
  - la version 2030 conserve « a. (Abrogé) ; » au 1 et au 2 ;
  - dans les trois textes, la transition précise que les amendes des états récapitulatifs ne s'appliquent plus aux périodes postérieures au 30 juin 2030. Le texte rebasé sur 2027 garde ces amendes jusqu'à cette date.
- **Demande à A1 :** reporter l'abrogation du IV bis de 1737 sur LEGIARTI000053293950 (2030) et LEGIARTI000054567168 (2027), avec le texte exact.

### RT-FUTFISC-12 (P1) — CGI 1788 F : appliquée pour la partie codifiée

- **Article :** 1788 F LEGIARTI000054561288 (new, nouveau numéro au 1er janvier 2027). 262-0 bis est inchangé : sa proposition traite déjà la suppression.
- **Ce qui disparaît de 1788 F :**
  - la caducité de l'agrément en cas de cession ou de prise de contrôle ;
  - l'amende de 300 000 € et l'interdiction de trois ans pour exercice sans agrément.
- **Ce qui est conservé :** l'amende plafonnée à 300 000 € et le contradictoire de trente jours, pour les seules obligations techniques maintenues au II de 262-0 bis proposé ou dans les mesures de L. 215-40.
- **Transition :** loi plus douce ; les certifications déjà délivrées restent valables ; les sanctions douanières sont intactes.
- **Non appliqué (`hors corpus`) :** l'abrogation du 1° de L. 215-40 CIBS. Les annexes II 202 E à O et IV 50 sexies L restent à aligner (autres groupes).

## Fichiers

- `apply/A2/changes.json` : 19 changements, 1 demande (A1, 1737), 4 parties non appliquées.
- `apply/A2/rows.built.json` : lignes construites par l'outil de contrôle.
- Articles du groupe non modifiés : 279-0 bis A, 284, 286, 302 septies A et 262-0 bis. Aucune correction ne l'exigeait. Pour 302 septies A, voir la note sous RT-FUTFISC-04.
