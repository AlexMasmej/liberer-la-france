# Brief — rédiger les corrections des objections P0 et P1, pour application

À lire **après** `BRIEF-AGENTS.md`, dont les règles de lecture et de qualification s'appliquent. Ce brief change ton rôle : tu ne qualifies plus seulement, **tu rédiges les textes de correction** qui seront appliqués au projet.

## Qui écrit

- **Toi : jamais en production.** Tu écris uniquement dans `apply/<GROUPE>/`. Tu lis la production en lecture seule.
- **Le coordinateur applique** tes textes, après les avoir contrôlés, avec l'outil gardé du projet (`review_prior.commit` et `register_batches`).
- **Lecture des textes** : `python3 -I tools/cite.py <code> <numéro|LEGIARTI>` lit l'instantané final `20261029T034912Z`. Il est identique à la production, à deux articles près, déjà corrigés et hors de ton périmètre : L1233-46 et CSS L241-17.

## Critère d'alignement : n'applique que ce qui sert les orientations

L'auteur demande d'appliquer les P0 et P1 **alignées sur le programme 2027 de David Lisnard**. La référence opérationnelle est celle des orientations du projet, inspirées de ce programme.
- Lis `snapshots/20261029T034912Z/policy-coordinations.json`, en particulier :
  - `editorial_direction_2026_10_19` ;
  - `cuts_and_reliefs_2026_10_19` ;
  - `preserved_benefits_2026_10_19` ;
  - `substantive_outcomes_2026_10_19` ;
  - la section du domaine que tu traites.
- **En résumé :** moins d'impôts et moins de contraintes ; suppression des impôts de production ; simplification ; aucune formalité de remplacement. Les exonérations, dérogations favorables, droits acquis et transitions sont conservés. Plus de droits de succession ; les donations restent taxées.
- **Contrat unique, TASCOM, dérogations littorales :** inchangés.

**Une correction est appliquée** si elle fait l'une de ces trois choses :
- elle rend effective une réforme déjà décidée par le projet, par exemple en empêchant qu'une version future la rétablisse ;
- elle supprime une contradiction ;
- elle ferme une faille qui contredit l'objet déclaré du projet.

**Elle n'est pas appliquée** (`skipped`, avec le motif) si elle :
- crée ou augmente un impôt ou un prélèvement, ou en étend l'assiette ;
- crée une formalité, une autorisation, une déclaration ou une condition nouvelle ;
- supprime une exonération, une dérogation favorable ou un droit acquis ;
- revient sur un choix explicite de l'auteur ;
- suppose un arbitrage politique que l'objection laisse ouvert. Seule exception : l'objection désigne elle-même une option « conforme aux orientations ». Dans ce cas, applique cette option et dis-le.

**Cas particuliers :**
- **Faille qui fait échapper au prélèvement que le projet conserve** (par exemple, droits de donation contournés) : applique la fermeture si elle ne fait que rétablir le champ que le projet déclare. Marque-la `"loophole_closure": true` dans `changes`, pour que l'auteur puisse la revoir.
- **Pièce manquante** ou **texte hors corpus** (CIBS, arrêtés, ordonnances non codifiées) : ne l'invente pas. Indique `skipped`, avec « pièce manquante » ou « hors corpus ».
- **Correction rédigée « dans la loi de réforme »** (disposition non codifiée) : préfère une solution codifiée équivalente. Le plus souvent, c'est la rédaction d'une proposition sur la version future, de sorte que la réforme s'y applique aussi. Si aucune solution codifiée n'existe, mets le texte de la disposition non codifiée sous `uncodified`, avec son objet, sans l'appliquer à un article.

**Objections « à confirmer » :** applique-les seulement si la correction est sûre quel que soit le point à confirmer, par exemple une coordination neutre. Sinon, `skipped` avec « à confirmer ».

## Rédaction

Pour chaque objection, lis dans `reports/register.json` :
- l'objection complète ;
- `reexam.revised_minimal_correction` s'il existe : c'est la version la plus récente ;
- le rapport du dossier `reports/dossiers/<dossier>.md`, qui contient souvent la rédaction intégrale.

Puis lis en entier, avec `cite.py`, chaque article à changer : source, proposition actuelle, motif et notes.

1. **Texte complet.** Pour chaque article modifié, rédige le **texte complet** de la nouvelle proposition (`proposed_xml`), du motif (`reason`) et des notes (`review_notes`).
   - Ne laisse aucun « […] » ni aucun texte inchangé sous-entendu.
   - Reprends sans changement tout ce que la correction ne touche pas.
   - HTML autorisé : `p`, `br`, `table` et ses sous-éléments, `b`, `strong`, `i`, `em`, `u`, `sup`, `sub`, `ul`, `ol`, `li`, `div`, `span`, `blockquote`. Aucun attribut, sauf `rowspan` et `colspan`. Garde toutes les lignes et cellules des tableaux, sauf réduction normative déclarée.
2. **Notes de revue.** Ajoute à la fin une phrase : « Correction de la troisième passe (objection RT-…) : … ». Corrige au passage les affirmations des notes rendues fausses, par exemple une version dite « non fournie » alors qu'elle est au corpus.
3. **Mode.**
   - `replace` pour un article qui a déjà une proposition.
   - `new` pour une version sans brouillon, typiquement une version future (`VIGUEUR_DIFF`). Sa proposition doit reporter la réforme du projet sur cette version, et seulement elle.
4. **Champs de la ligne de lot** (`overrides`) :
   - **suppression intégrale :** `change_type: "full_repeal"`, `repeal_policy_id: "editorial_direction_2026_10_19"`, `repeal_scope` (au moins 30 caractères, propre à l'article). Le corps commence par « Le présent article est abrogé… » ou « Abrogé ».
   - **réduction qui retire des dispositions ou des cellules de tableau :** `change_type: "normative_reduction"`, `reform_policy_id: "editorial_direction_2026_10_19"` et `removed_provisions`, une liste de chaînes d'au moins 30 caractères.
   - **ligne qui porte un `substantive_impact` :** chaque `source_quote` et `proposed_quote` doit rester un passage **exact** de la source ou de la nouvelle proposition. Mets-le à jour dans `overrides.substantive_impact`, avec l'objet complet. Le coordinateur recalcule le certificat.
5. **Propriété des articles.** `apply/assignment.json` attribue chaque article à un seul groupe.
   - Ne modifie que les articles de ton groupe.
   - Pour un article d'un autre groupe, mets la modification voulue sous `requests`, avec le texte exact.
6. **Contrôle.** Lance `python3 -B apply/check_changes.py <GROUPE>` jusqu'à ce que `problems` soit vide. L'outil reconstruit les lignes et les passe au validateur du projet, sans rien écrire en production. Les `diagnostics` (changement de longueur, renvois modifiés) ne sont pas des erreurs, mais vérifie qu'ils sont voulus.

## Livrable

Écris `apply/<GROUPE>/changes.json`, au format décrit en tête de `apply/check_changes.py`. Ajoute :
- `"loophole_closure": true` si nécessaire ;
- `"uncodified": [...]` s'il y a lieu.

Écris aussi `apply/<GROUPE>/DECISIONS.md` en français. Pour chaque objection :
- appliquée, partiellement appliquée ou non appliquée, avec le motif ;
- les articles touchés ;
- ce qui change en une phrase ;
- les points laissés à l'auteur.

Termine par un résumé court. Revue IA : rien de ceci ne vaut validation par un juriste.
