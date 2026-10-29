# Brief — balayages par famille de défauts : qualifier les pistes et rédiger les corrections

À lire **après** :
- `BRIEF-AGENTS.md`, pour la lecture et les interdits ;
- `BRIEF-AUDIT.md`, pour les familles F1 à F10 et la lecture de la production ;
- `BRIEF-APPLY.md`, pour le critère d'alignement, la rédaction, le format de `changes.json` et l'outil de contrôle.

Leurs règles s'appliquent. Tu n'écris **jamais** en production.

## Ce que contient ton paquet

`audit/sweeps/packet-<GROUPE>.json` liste des articles à examiner. Chacun porte une ou plusieurs **pistes** :

| Code | Ce que l'outil a détecté |
|---|---|
| **S1/F1** | Un article réglementaire cite un article législatif dont la proposition est une abrogation, sans être lui-même abrogé. |
| **S2/F2** | Une disposition qui porte une sanction cite un article abrogé par le projet. |
| **S3/F3** | Renvoi à un numéro absent de tous les codes du corpus (échantillon). |
| **S4/F4** | La proposition affirme ne pas reporter une abrogation, alors que la version suivante remplace le texte. |
| **S5/F4** | La version en vigueur porte une proposition, mais sa version suivante déjà publiée n'en a pas (`successor`). |
| **S7/F3** | Renvoi à un « n-ième alinéa » ou au « dernier alinéa » d'un article dont la proposition a déplacé ou changé cet alinéa. |
| **S8/F3** | Renvoi à un article du même code dont toutes les versions ont pris fin entre 2009 et 2026. |
| **AUDIT** | Défaut grossier relevé par l'audit aléatoire, avec sa description et parfois une correction suggérée. |

**Les pistes S1 à S8 sont mécaniques et contiennent beaucoup de faux positifs.**

Exemples de faux positifs :
- un renvoi qui figure seulement dans une transition ou un régime antérieur ;
- un renvoi à un article d'un autre code de même numéro ;
- un décret qui garde une fonction utile ;
- une version suivante qui ne touche pas la réforme.

## Ta tâche, article par article

1. Lis l'article en entier dans la **production** (`CITE_PRODUCTION=1 python3 -I tools/cite.py …`), puis chaque article visé par ses pistes.
2. Qualifie chaque piste :
   - `faux positif` ;
   - `déjà réglé` ;
   - `défaut confirmé` (G ou m, famille).

   Donne une citation exacte et l'identifiant LEGIARTI.
3. **Pour tout défaut confirmé `G`**, rédige la correction alignée sur les orientations, au format de `BRIEF-APPLY.md`, dans `apply/<GROUPE>/changes.json`. Les règles :
   - **renvoi mort ou décalé (F3)** : corrige le renvoi vers la bonne disposition, ou supprime-le s'il est sans objet ; ne change pas le fond ;
   - **formalité, obligation ou sanction qui survit à sa suppression (F1, F2)** : aligne l'article sur la suppression, sans formalité ni sanction de remplacement, avec la transition et la loi pénale plus douce pour les faits passés ; garde une protection essentielle (fraude, risques graves) si la loi la garde ;
   - **version suivante sans proposition (S5)** : crée une proposition (`new`) qui reporte la réforme du projet sur cette version, et seulement elle. Si la version suivante ne touche pas la réforme, c'est un faux positif ;
   - **article maintenu (`retained_unchanged`) dont seul un renvoi est mort** : corrige le renvoi en mode `replace`, en donnant un texte complet. Si le validateur exige un bilan d'impact, mets à jour `overrides.substantive_impact`. S'il refuse, note la piste comme « correction non applicable par l'outil » sans contourner.
   - Ne fais **aucune réécriture de style**, et ne touche à aucune orientation politique.
4. **Les défauts `m`** (notes et motifs erronés, F10) ne se corrigent que s'ils sont sur un article que tu modifies déjà.
5. Valide avec `python3 -B apply/check_changes.py <GROUPE>` jusqu'à ce que `problems` soit vide. Les articles de ton paquet t'appartiennent. Pour un article d'un autre groupe, utilise `requests`.

## Livrables

- `apply/<GROUPE>/changes.json` ;
- `apply/<GROUPE>/DECISIONS.md` : une ligne par piste, avec la qualification et la correction faite ou non ;
- `audit/sweeps/<GROUPE>.json` : `{"group": "...", "leads": [{"key": "...", "family": "...", "qualification": "faux positif|déjà réglé|G|m", "evidence": "...", "corrected": true}]}`.

Termine par un résumé court : nombre de pistes par qualification, nombre de corrections, points pour l'auteur. Revue IA : ce n'est pas une validation par un juriste.
