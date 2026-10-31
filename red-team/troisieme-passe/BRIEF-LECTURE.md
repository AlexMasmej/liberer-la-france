# Brief — lecture systématique, palier A : articles réécrits du CGI et de ses annexes

À lire **après** :
- `BRIEF-AGENTS.md`, pour les interdits et la discipline de lecture (ses livrables sous `reports/dossiers/` ne s'appliquent pas ici) ;
- `BRIEF-AUDIT.md`, pour la lecture de la production, la qualification G / m / 0 et les familles F1 à F10 ;
- `BRIEF-APPLY.md`, pour le critère d'alignement, la rédaction, le format de `changes.json` et l'outil de contrôle ;
- `BRIEF-SWEEP.md`, pour les règles de correction par famille, en particulier les sections « Cinquième balayage » et « Sixième balayage ».

Leurs règles s'appliquent. Tu n'écris **jamais** en production.

## Pourquoi cette lecture

Six audits aléatoires mesurent environ 3,4 % d'articles avec un défaut grossier. Dans les articles **réécrits** du CGI et de ses annexes, le taux est de 9 à 12 %. Les balayages par famille n'ont pas fait baisser la mesure. Ce palier lit donc **chacun** de ces articles, comme un juriste, et corrige les défauts grossiers.

## Ton paquet

`audit/tier-a/packet-<GROUPE>.json` liste des articles réécrits en vigueur au 18 octobre 2026, dans l'ordre du code. Ils appartiennent à une même section ou à des sections voisines (`section_path`). Les articles déjà lus par les audits aléatoires sont exclus.

Lis la section **comme un ensemble**. Beaucoup de défauts viennent d'un article qui ne suit plus ses voisins : chapitre à moitié abrogé, renvoi à un article voisin supprimé, formalité supprimée ici et maintenue là.

## Pour chaque article

1. **Lis-le en entier** dans la production :

   ```sh
   CITE_PRODUCTION=1 python3 -I tools/cite.py <code> <numéro|LEGIARTI>
   ```

   Lis la source au 18 octobre 2026, la proposition, le motif, les notes et les versions futures (`VIGUEUR_DIFF`).
2. **Lis ses liens directs**, au moins les trois plus importants :
   - pour un article d'annexe, l'article du CGI qu'il applique (sa base légale) ;
   - les articles qu'il cite : leur proposition actuelle ;
   - pour un article du CGI, les articles d'annexe qui l'appliquent : cherche son numéro dans les annexes, en lecture seule.

   Dis ce que tu n'as pas lu.
3. **Qualifie-le** G, m ou 0, au critère de l'audit : un juriste qui ouvre l'article le jugerait-il anormal ?
   - Un renvoi mort ou décalé qui rend une règle inapplicable ou incertaine est un **G**, pas un m.
   - Ne cherche pas l'exhaustivité. Un article sans anomalie après lecture de son texte et de ses liens principaux est un **0**.
   - Donne une citation exacte avec l'identifiant LEGIARTI pour tout G ou m.
4. **Points à contrôler**, tirés des défauts déjà trouvés dans le CGI :
   - **base légale abrogée ou éteinte** : une annexe organise encore un régime dont l'article du CGI a disparu. Exemple : les centres de gestion agréés, alors que les articles 1649 quater C à O sont abrogés depuis 2025 (F1, F3) ;
   - **chapitre à moitié abrogé** : un article non abrogé s'appuie sur un voisin que le projet abroge (F1, F5) ;
   - **loi réduite, annexe inchangée** : le projet retire une formalité, une condition ou un justificatif de l'article du CGI, mais l'annexe l'exige encore. Lis `removed_provisions` dans le lot de l'article du CGI (F1) ;
   - **pénalité** (articles 17xx et suivants) qui vise une obligation supprimée, ou un alinéa devenu la clause de suppression (F2) ;
   - **version future** publiée sans proposition qui rétablit ce que le projet supprime (F4) ;
   - **renvoi à un alinéa, un I ou un n°** que la proposition a déplacé ou supprimé (F3) ;
   - **tableau amputé** ou texte tronqué (F7) ;
   - **faveur supprimée sans décision** (F8) : qualifie-la. Corrige seulement si `policy-coordinations.json` conserve expressément cette faveur ; sinon, c'est un arbitrage pour l'auteur (`skipped`, « arbitrage »).

## Corriger les défauts G

Pour chaque **G**, rédige la correction alignée, au format et selon les règles de `BRIEF-APPLY.md` et de `BRIEF-SWEEP.md` :
- aucune réécriture de style ;
- aucun choix politique nouveau ;
- aucune formalité, condition ni sanction de remplacement ;
- exonérations, dérogations favorables, droits acquis et transitions conservés ;
- aucune extension de faveur non décidée.

**Traite la section en entier.** Si tu abroges ou alignes un article, vérifie ses voisins de la même section et ceux qui le citent. Un cinquième tour a abrogé une partie d'un chapitre en laissant les voisins organiser encore le régime. Ne refais pas cette erreur.

Les défauts **m** ne se corrigent que sur un article que tu modifies déjà, par exemple une note devenue fausse.

## Qui possède quoi

- **Article de ton paquet sans `previous_owner`** : il est à toi. La correction va dans `apply/<GROUPE>/changes.json`.
- **Article de ton paquet avec `previous_owner`** : crée le dossier de variante `apply/<previous_owner><SUFFIXE>/`. Ton suffixe est donné dans ta consigne. Par exemple, avec le suffixe `taa`, un article de Y12 va dans `apply/Y12taa/`.
- **Article hors de ton paquet** : ne le modifie pas. Mets la modification voulue sous `requests` dans `apply/<GROUPE>/changes.json`, avec le texte exact. Cela vaut aussi pour l'article du CGI qui sert de base légale à une annexe.

Valide chaque dossier avec la commande suivante, jusqu'à ce que `problems` soit vide :

```sh
python3 -B apply/check_changes.py <dossier>
```

Ne crée pas de dossier vide.

## Livrables

- `audit/tier-a/<GROUPE>.json` : une entrée par article du paquet, sans exception.

  ```json
  {"group": "...", "read_from": "production",
   "articles": [{"code": "...", "number": "...", "source_id": "...",
     "verdict": "G|m|0", "families": [], "description": "...", "evidence": "...",
     "links_read": [], "links_not_read": "...", "corrected": false, "folder": null}]}
  ```

  Pour un `0`, `description` peut tenir en quelques mots.
- `apply/<GROUPE>/changes.json` et `apply/<GROUPE>/DECISIONS.md`, s'il y a une correction ou une demande. Ajoute les dossiers de variante.
- Termine par un **résumé court** :
  - décompte G / m / 0 ;
  - nombre de corrections ;
  - dossiers créés ;
  - `requests` laissées à d'autres groupes.

Revue IA : ce n'est pas une validation par un juriste.
