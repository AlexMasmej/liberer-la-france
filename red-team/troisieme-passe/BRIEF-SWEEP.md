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

## Troisième balayage : contradictions entre propositions (S9, S10)

| Code | Ce que l'outil a détecté |
|---|---|
| **S9/F1+F5** | Un décret ou une annexe applique une loi que le projet a **réduite** (`normative_reduction`), et il mentionne encore une formalité du même type que celle retirée de la loi (par exemple, la loi retire l'autorisation et le décret parle encore d'autorisation). |
| **S10/F5** (échantillon) | Une proposition déroge à une autre proposition (« nonobstant », « par dérogation », « sans préjudice », « à l'exception »…). |

**Pour S9**, lis la ligne `removed_provisions` de la loi visée (dans son lot) et la proposition de la loi. La question est de savoir si le décret organise encore la formalité ou la condition retirée, ou s'il la vise seulement pour l'ancien régime (transition).

**Pour S10**, vérifie que l'article visé dit encore ce que la dérogation suppose. Si la dérogation porte sur une règle que l'article visé ne contient plus, ou contredit ce qu'il dit désormais, c'est un défaut F5.

## Quatrième balayage : familles tirées du quatrième audit (S9x, S9a, S12, S13, S15)

| Code | Ce que l'outil a détecté | Exemple de l'audit |
|---|---|---|
| **S9x/F1+F5** | Un décret ou une annexe applique une loi **réduite**, et il emploie encore des mots distinctifs des dispositions retirées de cette loi (`shared_words`). | Annexe II 74 S septies garde déclaration, paiement et justificatif d'exportation que 150 VL ne demande plus. |
| **S9a/F1+F5** | Un article des annexes du CGI applique un article du CGI réduit par le projet (piste large). | Annexe II 95 ZE et 95 ZJ maintiennent le double conservé et la convention de trois ans que 170 ter supprime. |
| **S12/F4** | Une proposition tient un autre article pour abrogé, alors que sa version actuelle est `ABROGE_DIFF` et qu'une version `VIGUEUR_DIFF` publiée la remplace (`cited_successor`). | R4224-17 dit R4211-3 abrogé ; la version 2027 le maintient. |
| **S13/F3** | Renvoi au « n° de l'article X » alors que X, tel que proposé ou dans sa prochaine version publiée, n'a plus ce n°. | Annexe D353-59 vise « 2° ou 3° de l'article R. 331-15 », qui n'a plus que deux items. |
| **S15/F5** | Une proposition fait dépendre son effet d'une modification législative future. | D351-1-15 attend une modification de L351-4-2 que le projet ne fait pas. |

Pour **S9x** et **S9a** : lis `removed_provisions` de la loi visée et sa proposition. La question reste de savoir si le texte d'application organise encore ce qui a été retiré, ou s'il le vise seulement pour l'ancien régime.

Pour **S12** : beaucoup de fenêtres attrapent un simple « (Abrogé) » d'un item voisin. C'est un faux positif. Le défaut, c'est une phrase qui dit que l'article cité disparaît alors que sa version future le maintient. Corrige la phrase (renvoi à l'article dans sa rédaction en vigueur), sans recréer de formalité que le projet a supprimée ailleurs.

Pour **S15** : si la loi visée ne fait pas, en production, la modification attendue, retire la condition et reviens au texte qui produit l'effet voulu. N'étends aucune faveur qui n'est pas décidée.

Le champ `previous_owner` indique qu'un autre groupe possède déjà l'article. Dans ce cas, crée un dossier de variante pour ce groupe (par exemple `apply/B06j/` pour B06), et valide-le aussi.

## Cinquième balayage : CGI et bases légales mortes (S1c, S2c, S8c, S16, S17)

Les pistes S1, S2 et S8 antérieures ne lisaient que les numéros L, R, D et A. Elles n'ont donc rien produit dans le CGI ni dans ses annexes. `tools/sweeps5.py` lit les numéros du CGI (« 290 quater », « 1649 quater N »).

| Code | Ce que l'outil a détecté | Exemple de l'audit |
|---|---|---|
| **S1c/F1** | Un article d'annexe, non abrogé, cite un article du CGI dont la proposition est une abrogation. | Annexe IV 50 sexies G garde la billetterie de 290 quater abrogé. |
| **S2c/F2+F3** | Un article du CGI qui porte une sanction cite un article du CGI abrogé, réduit (pour les articles 17xx) ou éteint. | 1729 C ter vise « le dernier alinéa du II de l'article 1649 AG », devenu la clause de suppression. |
| **S8c/F3** | Un article du CGI ou d'annexe s'appuie sur un article du CGI dont toutes les versions ont pris fin. | Annexe II 371 ter A à H réforment les conventions de 1649 quater N, abrogé en 2025. |
| **S16/F3** | Un décret réécrit, dans un autre code, cite hors transition un article L du même code éteint. | D5134-1 organise le contrat emploi-jeune de L5134-1, abrogé en 2015, pour les contrats futurs. |
| **S17** | Piste d'un balayage antérieur qualifiée « m » et non corrigée. | A932-4-1 (renvois morts structurants) et D5134-1 étaient des « m » ; l'audit 5 les juge G. |

Pour **S8c** et **S16**, quand la base légale est éteinte, la correction alignée est de cesser d'organiser le régime pour l'avenir (abrogation ou limitation aux situations en cours), sans formalité de remplacement et avec une transition. Ne réécris pas un régime mort.

Pour **S17**, requalifie avec le critère de l'audit : un juriste qui ouvre l'article le jugerait-il anormal ? Si oui, c'est un G à corriger, même si le défaut vient de la source. Sinon, il reste m.
