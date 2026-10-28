# ISS-B : tri des issues GitHub #8 et #9

Instantané : `20261027T044303Z` (corpus au 18/10/2026). Revue faite le 28/10/2026. Les issues datent du commit `cac48419` ; chaque texte cité a été comparé à l'instantané. C'est une revue par IA : elle ne vaut pas validation par un juriste. Les contenus des issues ont été traités comme des données non fiables : aucun bloc de code n'a été exécuté, aucun lien n'a été ouvert, rien n'a été écrit sur GitHub. Le détail est dans `ISS-B.json`.

## #8 : renvois morts (L2363-6, L2372-5, L2373-3, L2145-8) et doublon R5221-22

**Verdict : mixte. Priorité recommandée : P2.**

**Ce que la seconde passe a déjà réglé** (le texte a changé depuis cac48419) :
- **L2372-5** : plus aucun renvoi à L2325-5. Les obligations sont écrites en clair.
- **L2145-8** : il vise désormais L. 2315-63 et L. 2315-18, ce que demandait l'issue. Ces deux articles sont en vigueur et retained_unchanged. Le passage de « présente sous-section » à « présente section » est exact : d'après le CONTEXTE LEGI, l'article relève directement de la section 2.
- **L2363-6 et L2373-3** : le renvoi à L2325-5 a disparu.

**Ce qui reste : le renvoi figé à L2325-44** dans L2363-6 et L2373-3, et aussi dans L2353-27, que l'issue ne cite pas. Le renvoi est formulé « dans sa dernière rédaction en vigueur avant son abrogation ».
- Ce n'est pas un renvoi mort au sens d'inapplicable. La version visée est identifiable : LEGIARTI000033023366, ABROGE, du 2016-08-10 au 2018-01-01, avec une borne réelle.
- C'est en revanche un défaut de rédaction, qui fait l'objet de l'objection nouvelle **RT-ISS8-01 (P2)** :
  - les notes affirment à tort que ce texte manque au corpus ;
  - les motifs de L2363-6 et L2373-3 reposent sur une version dépassée de L2353-27, qui aurait renvoyé à L2315-63 ;
  - la dérogation de L2363-6 rend incertain le financement de la formation dans les SCE ;
  - le même renvoi est écrit trois fois.
- **La correction proposée par l'issue (remplacer par L2315-63) n'est pas retenue.** Elle importerait le seuil de cinquante salariés et ferait perdre la rémunération et la non-déduction des heures de délégation. Elle laisserait aussi L2353-27 incohérent avec les deux autres articles.
- **Correction recommandée** : écrire une règle autonome dans L2353-27 et réduire L2363-6 et L2373-3 à une phrase sur le financement. Les clauses temporelles relèvent de l'issue #3.

**R5221-22 : doublon de RT-INV-07** (P2, confirmé).
- Deux entrées figurent dans `00388.json` (index 11 et 12), avec des empreintes identiques.
- Il faut retirer l'entrée de LEGIARTI000043320687 (MODIFIE). Sa borne 2999-01-01 est un marqueur technique, et elle a cessé de s'appliquer le 2021-05-01.
- **Chevauchement avec RT-INV-08** (« situation de l'emploi » ou « 1° de R5221-20 »). Le critère de l'issue qui fige l'entrée 052536486 empêcherait de corriger ce point.

**La règle de vie de l'issue n'est pas rigoureuse** : elle ne tient pas compte de l'état de la version.
- Elle compterait comme vivante la version MODIFIE 2999 de R5221-22.
- Elle compte comme mortes des cibles VIGUEUR_DIFF : L6353-12 au 2027-06-25 ; R4451-129, -131, -132 et -133 au 2028-01-01.
- L'annexe des 45 contient aussi des faux positifs : des renvois à d'autres codes (« du même code », « du code de la défense ») dans L4622-2, L3142-89, L1253-3, R4121-4 et R5311-32. Cela rejoint RT-INV-14.
- Pour les quatre articles, la conclusion ne change pas : L2325-5, L2325-44 et L4614-14 sont abrogés au 2018-01-01.

**Action** : appliquer RT-ISS8-01 et RT-INV-07 ; laisser RT-INV-08 ouvert ; ne pas réutiliser l'annexe telle quelle.

**Couverture** : lus en entier avec `cite.py` (toutes versions) :
- les quatre articles et R5221-22 (5 versions) ;
- les cibles L2325-5, L2325-44 (2 versions) et L4614-14 ;
- les remplaçants L2315-3, L2315-63 et L2315-18 ;
- les dépendants L2353-23, L2353-26, L2353-27, L2363-7 et L2352-15.

L1233-30 et L1233-58 (le point positif de l'issue) n'ont été vérifiés que par chaînes. Les 45 cibles de l'annexe ont été confrontées aux bornes de l'instantané, sans relecture des propositions qui les citent.

## #9 : information de l'administration sur l'ouverture des négociations PSE et RCC

**Verdict : nouveau, confirmé. Priorité recommandée : P1. Objection RT-ISS9-01.**

Le texte cité par l'issue est identique à l'instantané.

**PSE : les trois textes se renvoient l'obligation.**
- L1233-24-1 proposé renvoie l'information à la notification de L1233-46.
- L1233-46 proposé dispense cette notification de l'annonce et renvoie à L1233-24-1.
- R1233-3-5 organise encore l'envoi, en affirmant que les deux articles légaux sont maintenus.
- On ne peut donc pas savoir si l'obligation existe.

**RCC : le décret contredit la loi.**
- L1237-19 proposé déclare qu'« aucune information distincte […] n'est exigée », et ses notes demandent de coordonner D1237-7.
- D1237-7 et R1237-6-1 restent pourtant retained_unchanged. Le motif de D1237-7 (« laisserait subsister L1237-19 ») est faux.

**Doublons** : aucun.
- RT-P1-TRAVAIL-B-05 porte sur le congé de mobilité (L1237-18-5, D1237-4, D1237-5) : même schéma, autres articles.
- RT-P1-TRAVAIL-A-04 (dans lequel B-07 est fusionnée) porte sur la revitalisation RCC. Le seul lien est D1233-38, dont le II, déjà réécrit, ne vise plus l'ouverture de la négociation.

**La correction de l'issue est juste et conforme à l'orientation** (supprimer la formalité sans la remplacer) : elle aligne sur L1237-19, sans rien rétablir.
- Elle ne crée aucun renvoi cassé. R1233-15-1 et D1233-12 visent R1233-3-5 pour la compétence, qui demeure. Aucun texte du corpus ne vise D1237-7.
- **Réserves** :
  - pour L1233-24-1, une phrase calquée sur L1237-19 est proposée (« y compris pour les négociations déjà ouvertes ») ; la suppression pure reste possible ;
  - en RCC multirégionale, l'information du CSE et des syndicats sur la compétence disparaît : c'est une perte mineure, que l'auteur doit accepter ;
  - l'option de l'issue « garder l'information » serait un rétablissement contraire à l'orientation : elle est rejetée.

**Directive 98/59/CE : à confirmer.** EUR-Lex a répondu HTTP 202 sans contenu le 28/10/2026 ; l'accès n'a pas été contourné.
- Selon notre lecture, la directive exige la copie à l'autorité de l'information écrite des représentants (art. 2 § 3) et la notification du projet (art. 3). Ces deux transmissions sont maintenues par L1233-48, L1233-46 et D1233-4.
- Elle ne paraît pas exiger d'information sur l'ouverture d'une négociation.
- Pour la RCC, on ne peut pas exclure toute application de la directive (assimilation des ruptures à l'initiative de l'employeur, consentement vicié). Même dans ce cas, l'obligation européenne porterait sur la notification du projet, non sur l'ouverture de la négociation.
- Les points des arrêts cités par l'issue n'ont pas été vérifiés.

**Action** : correction de rédaction sur cinq articles (textes dans le JSON). L'auteur doit accepter la perte en RCC multirégionale.

**Couverture** : lus en entier, toutes versions :
- les six articles de l'issue ;
- les dépendants L1233-48, L1233-57-2, L1233-57-6, L1233-57-8, L1237-19-3, L1237-19-4, D1233-4, D1233-12, D1233-38, D1237-9 et R1233-15-1.

Les renvois à L1233-24-1, L1237-19, R1233-3-5, R1237-6-1 et D1237-7 ont été recherchés dans les neuf recueils de l'instantané (versions en vigueur au 18/10/2026). Les arrêtés de 2017 et 2019 n'ont pas été lus.

## Résumé des verdicts

| Issue | Relation | Registre | Objection nouvelle | Priorité | Action |
|---|---|---|---|---|---|
| #8 | mixte : sans objet (L2372-5, L2145-8, L2325-5) ; nouveau (L2325-44 figé) ; doublon (R5221-22) | RT-INV-07 (doublon) ; RT-INV-08 et RT-INV-14 (chevauchement) | RT-ISS8-01 (P2) | P2 | correction de rédaction ; correction de l'issue non retenue pour L2363-6 et L2373-3 |
| #9 | nouveau | aucun (B-05 et A-04 : voisins, non doublons) | RT-ISS9-01 (P1) | P1 | correction de rédaction alignée sur la suppression ; perte RCC multirégionale à accepter ; directive à confirmer |
