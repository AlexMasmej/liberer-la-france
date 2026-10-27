# Addendum P1 — qualification des alertes « renvoi vers une abrogation proposée »

À lire **après** `BRIEF-AGENTS.md`, dont toutes les règles s'appliquent.

## Origine

L'audit GLOBAL du 25 octobre (`evidence/sealed/runtime/global-reference-audit-20261025T2341Z/`, limites dans `summary.json` → `limits`) a produit 1 421 alertes P1 structurelles. Elles ont été requalifiées mécaniquement par le coordinateur sur l'instantané `20261026T230545Z` (`reports/p1-triage-20261026T230545Z.json`) :
- 1 329 restent « live » (cible toujours abrogée par une formule explicite, renvoi toujours présent) ;
- 92 ont vu disparaître le renvoi.

**Ce ne sont pas des contradictions établies.** L'audit ne reconnaît une abrogation que par une formule initiale explicite (« Le présent article est abrogé… ») et résout les numéros sans lecture juridique.

Types :
- `proposal_refers_to_proposed_repeal` : une **proposition** cite un article dont la proposition est une abrogation ;
- `unrewritten_referrer_to_proposed_repeal` : une **source non réécrite** (ou réécrite depuis l'audit : voir `field_now` et `referrer_status_now`) cite un article abrogé par le projet ;
- `reference_introduced_in_proposal` : renvoi nouveau introduit par la proposition.

## Ton paquet

`reports/p1-work/<PAQUET>.json` contient des **clusters** par article cible abrogé. Chaque cluster comprend sa cible, ses alertes et ses articles qui y renvoient. Champs utiles par alerte : finding_id, kind, source_key (`code_id|LEGIARTI`), number, field_now, referrer_status_now, cited_number, context, target_key, target_number.

## Méthode, cluster par cluster

1. Lis **en entier** la proposition d'abrogation de la cible (`tools/cite.py`, ou SQL en lecture seule par `code_id|id`). Note ses clauses de transition, de neutralisation des renvois (par exemple « aucun renvoi ne peut rétablir… »), et ce qu'elle préserve ou redirige.
2. Pour chaque article qui y renvoie, lis **en entier** le texte courant qui porte le renvoi : la proposition si `rewrite_draft`, la source si `retained_unchanged`. Vérifie que le numéro cité vise bien la cible : même code, même article et pas un homonyme d'un autre code, d'une autre loi ou d'une version historique. Puis qualifie :
   - `alerte écartée` : renvoi en contexte historique ou transitoire assumé (« dans sa rédaction antérieure », périodes anciennes), résolution erronée du numéro, renvoi neutralisé ou redirigé par la clause de la cible, ou article qui renvoie lui-même abrogé ou coordonné ;
   - `coordination manquante` : un texte maintenu applique encore la règle abrogée comme vivante ;
   - `incohérence du projet` : une proposition réécrite s'appuie activement sur une règle abrogée (condition, exonération, procédure, sanction, autorité) ;
   - `risque juridique` : par exemple, l'abrogation de la cible fait disparaître une faveur, une garantie ou un droit acquis que le texte qui y renvoie et les orientations entendaient conserver ; ou une loi renvoie à un règlement abrogé, ou l'inverse.
3. Produis **une objection par effet juridique distinct**, pas par occurrence : le même renvoi répété dans dix articles d'un même mécanisme forme une seule objection, avec la liste des articles. Indique la conséquence concrète et une correction minimale. Rédige le passage complet proposé pour les plus importantes. Préserve les orientations, faveurs (TASCOM, dérogations littorales, contrat unique, etc.) et transitions.
4. Si un cluster touche un article d'un dossier ouvert traité par un autre agent, classe-le `couvert par dossier <ID>` sans objection en double. Articles concernés : a1 165, 185, 186 ; cgi 302 D bis ; a3 111-0 E/F/G/H, 171 ; a4 50-0 G/H/I, 50-00 D, 15 ; a2 289 ; css D351-9, R123-1, R123-1-1, D224-7, D224-8, R152-8, R153-2, R151-1, R151-3, R612-7, R216-2, R281-4, R213-5, D227-5, D227-6, L224-10, L228-1, L281-6, L216-3, R611-2, annexe I R434-32 ; travail R5221-22, R4451-39.

## Livrables (en plus du format commun)

- `reports/dossiers/<PAQUET>.md` et `reports/dossiers/<PAQUET>.json` (objections, préfixe `RT-<PAQUET>-xx`) ;
- `reports/p1-work/<PAQUET>-classification.jsonl` : **une ligne par finding_id du paquet**, avec les champs `finding_id`, `classification` (une des natures ci-dessus, `couvert par dossier <ID>` ou `non examiné`), `objection_id` (ou null), `motif` (une phrase), `read_in_full` (true/false).

Chaque alerte du paquet doit apparaître dans le fichier de classification. Si tu ne peux pas tout examiner sérieusement, classe le reste `non examiné` et dis-le. Ne laisse pas un classement superficiel passer pour une qualification.
