# Groupe B01 : décisions de la troisième passe (objections P2 RT-FUTCSS-18 à 36)

Textes lus en **production**, en lecture seule (sqlite `mode=ro`, `query_only`), et non sur l'instantané : beaucoup d'objections avaient déjà été réglées par les balayages W01 à W07 et par les groupes A4 et A6. Rien n'a été écrit en production.

Contrôle : `python3 -B apply/check_changes.py B01` donne 30 changements construits et 30 validés, avec `problems` vide. Les `substantive_impact` passent aussi `substantive_impact.validate(required=True, enforce_workflow=True)`.

Diagnostics, tous voulus :
- L759-25 : renvoi L141-4 retiré ;
- L753-4-3 : longueur ×0,36 ;
- L759-6 : renvoi L137-15 ajouté ;
- L752-9-7 : longueur ×3,4 et renvois aux caisses nationales ajoutés ;
- L241-3 et R145-10 : écarts de renvois déjà présents dans les propositions.

**Articles sans groupe attribué** (`owner` absent d'`assignment.json`), modifiés ici parce que l'objection les vise :
- R142-17-2 et D461-27 (RT-FUTCSS-20) ;
- L244-7, L244-8-1, L382-32 et L243-10 (RT-FUTCSS-35, notes seulement).

À vérifier par le coordinateur : qu'aucun autre groupe P2 ne les touche.

Aucune variante pour un autre groupe n'a été nécessaire.

---

## RT-FUTCSS-18 : L351-3 — **déjà réglé**
La version du 1er novembre 2026 porte déjà le 1° fusionné et la transition (RT-INV-03).

## RT-FUTCSS-19 : R351-12, doublon DILA — **déjà réglé**
La même proposition est portée sur 054060166 et sur 054425288, et les notes signalent le doublon.

**Laissé à l'auteur :** vérifier sur Légifrance quelle version la DILA conservera.

## RT-FUTCSS-20 : R461-8 et renvois de rang à L461-1 — **appliquée**
- **R461-8, version 054060100 (new)** : le seuil de 25 % vise « l'alinéa [...] relatif aux maladies caractérisées non désignées dans un tableau ». La référence reste juste avant et après l'insertion de 2027.
- **R142-17-2 (retenu → coordination)** : le texte vise désormais les « cas où l'article L. 461-1 subordonne cette reconnaissance à l'avis motivé d'un comité régional », appréciés selon la rédaction applicable à la décision de la caisse.
- **D461-27 (retenu → coordination)** : le quorum de deux membres vise les « maladie[s] désignée[s] dans un tableau [...] dont une ou plusieurs conditions ne sont pas remplies ».
- Les notes qui disaient que la version future de L461-1 manquait sont corrigées.
- Aucune garantie n'est retirée et aucun seuil nouveau n'est créé.

## RT-FUTCSS-21 : charges publiées pour 2027 — **non appliquée** (R160-5 déjà réglé)
- **R160-5 (2027)** : la proposition consigne déjà la décision : « reprises telles quelles [...] le projet n'en décide aucune autre ».
- **L162-5-10 (2027) et L322-5-3 (2027)** : accepter ou couper ces charges relève de l'auteur.

## RT-FUTCSS-22, 23, 24 : L222-2-1, L162-16-4, L245-6 et L325-1, versions 2028 — **déjà réglées**
Les balayages W06 et W07 ont déjà donné une proposition à chacune de ces versions 2028 :
- 6° abrogé, renvoi au troisième alinéa de L1233-72 et clause du contrat unique ;
- L. 3133-1 du CSP ;
- forclusions supprimées et retrait de Mayotte.

## RT-FUTCSS-25 : L757-1 (2028) — **appliquée**
- **Version 054467090 (new)** : la version de l'ordonnance est acceptée. Au c), le renvoi devient « la caisse mentionnée à l'article L. 752-9-1 », au lieu du « troisième alinéa », qui visait le 2° sur les travailleurs indépendants.
- **Version 031324246 (maintien)** : la réserve sur L811-14 est levée dans le motif et les notes. L811-14, comme tout le chapitre L811-1 à L811-20, est abrogé au 1er janvier 2006 par l'article 3 de l'ordonnance n° 2004-605, sous réserve de son article 2. L'effet du changement de 2028 se limite donc aux droits maintenus par cet article 2, qui est hors corpus (pièce manquante). Le successeur est signalé.

## RT-FUTCSS-26 : 55 articles mahorais hors inventaire — **non appliquée (inventaire, coordinateur)**
Une inscription d'inventaire en `retained_unchanged` ne s'exprime pas dans `changes.json`. Les coordinations nominatives sont traitées sous les objections 25, 27, 28, 29 et 33.

## RT-FUTCSS-27 : adaptations mahoraises privées d'objet — **partiellement appliquée**
Les nouvelles versions recalent chaque renvoi sur la proposition du projet :
- **L759-20** : « Au quatrième alinéa » de L355-2, où est la réserve, au lieu du dernier alinéa, devenu la transition ;
- **L759-24** : « et le troisième alinéa » de L815-7 ;
- **L759-25** : le 5° est réécrit par son effet (SMIC mahorais au douzième alinéa de L821-1 jusqu'au 1er janvier 2031) ;
- **L753-4-3** : exception limitée aux mots « ainsi que sa durée » ;
- **L752-9-6** : « au premier alinéa de l'article L. 227-3 » ;
- **L759-26** : b) abrogé, puisque le 3° de L842-2 est abrogé.

**Laissé à l'auteur :**
- L757-5 2° a) : étendre à Mayotte la suppression des conditions propres aux enfants, ou maintenir expressément la condition mahoraise ;
- l'option qui déplacerait les transitions, non retenue.

## RT-FUTCSS-28 : renvois à des prélèvements supprimés — **partiellement appliquée**
- **L759-6, L759-7, L759-11 (new)** : le texte officiel et ses tableaux sont gardés en entier. Un dernier alinéa borne chaque article au champ résiduel du forfait social, de la CSA et de la CASA, et de la cotisation subsidiaire. Aucun taux nouveau.
- **R613-10-1 (2027, new)** : la dispense vise R. 613-9 « pour les échéances déclaratives antérieures à [son] abrogation ».
- **L861-3, deux versions (replace)** : le 2° vise le forfait journalier « pour les journées antérieures à sa suppression ».
- **Déjà réglés** : L241-13 et L223-9.
- **Non appliqué** : retirer « et l'article L. 174-4 » du I de L753-4-1. Ce serait supprimer une mention favorable dans le seul but de rendre les textes cohérents.

## RT-FUTCSS-29 : convergence des taux mahorais — **partiellement appliquée**
- **L759-22-1 (new)** : « Ces conditions de convergence ne peuvent instituer aucun montant ni aucune assiette minimale obligatoire de cotisation », en cohérence avec L635-1 proposé.
- **Laissé à l'auteur** : la convergence des taux réduits (L759-3, L759-5, L759-9), maintenue ou gelée.

## RT-FUTCSS-30 et 31 : non-cumul AB/AF et conditions d'accès propres à Mayotte — **non appliquées (arbitrage)**
Les appliquer reviendrait à étendre une faveur ou une dépense que le projet n'a pas décidée. L'objection 30 propose d'ailleurs aussi l'option inverse, et l'objection 31 n'impose aucune correction.

## RT-FUTCSS-32 : capitalisation et salariés de la CSSM — **partiellement appliquée**
- **L241-3, II (replace)** : ajout de « Il ne s'étend pas aux salariés employés dans le secteur agricole, y compris ceux dont le risque vieillesse est géré par la caisse de sécurité sociale de Mayotte ». C'est une décision explicite de l'orientation retraite.
- **Laissé à l'auteur** : le report ou l'inclusion des autres salariés mahorais du régime général.

## RT-FUTCSS-33 : immobilier de la CSSM — **appliquée**
- **L752-9-7 (new, `normative_reduction`)** : la caisse décide elle-même, après avis de son conseil. Les caisses nationales exercent un contrôle a posteriori, « qui ne peut les subordonner à un agrément ni à une décision préalable ». Les opérations antérieures sont conservées.
- **L752-9-2, II (new)** : le contrôle est exercé a posteriori.
- **Laissé à l'auteur** : il peut préférer garder la règle de l'ordonnance pendant la transition.

## RT-FUTCSS-34 : erreurs matérielles du texte officiel — **non appliquée (hors corpus)**
L'objection demande un rectificatif après vérification du JORF, et non une correction silencieuse.

## RT-FUTCSS-35 : versions 2029 (CPP recodifié) — **partiellement appliquée, le reste déjà réglé**
- **L114-9 (2029, new, `normative_reduction`)** : la synthèse annuelle reste supprimée, et L. 3413-5 et L. 4415-5 sont repris.
- **Déjà réglés** : L355-2, L244-1, L114-12-1 et L412-8 en 2029.
- **Notes « successeur non fourni » corrigées** : L114-12-1, L355-2, L244-7, L244-8-1, L382-32 et L243-10. Les corps sont inchangés.

## RT-FUTCSS-36 : versions différées 2222 — **appliquée pour R145-10, le reste déjà réglé ou compatible**
- **R145-10, version 2018 036592776 (new)** : elle reçoit la proposition fondée sur le décret de 2025, sans RSI ni avis finaux.
- **R145-10, version 052208286** : la note sur ABROGE_DIFF est corrigée.
- **R382-72 (2012)** : la version a déjà une proposition.
- **R146-x** : versions compatibles, acceptées telles quelles.
- **Laissé à l'auteur** : constater les renouvellements.

---

**Résumé :**
- **Appliquées** (3) : RT-FUTCSS-20, 25 et 33.
- **Partiellement appliquées** (6) : RT-FUTCSS-27, 28, 29, 32, 35 et 36.
- **Déjà réglées** (5) : RT-FUTCSS-18, 19, 22, 23 et 24.
- **Non appliquées** (5) :
  - RT-FUTCSS-21 : arbitrage ; R160-5 déjà réglé ;
  - RT-FUTCSS-26 : inventaire ;
  - RT-FUTCSS-30 et 31 : arbitrage ;
  - RT-FUTCSS-34 : rectificatif.

En tout, 30 lignes, dont 17 nouvelles propositions sur des versions sans brouillon et 13 remplacements, parmi lesquels 8 ne changent que les notes ou le motif. Aucune `loophole_closure`, aucune entrée `uncodified`.

Revue IA, sans validation par un juriste.
