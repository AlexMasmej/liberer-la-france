# Red-team juridique indépendante — troisième passe (provisoire)

Revue critique indépendante du projet de réécriture de cinq codes : Code du travail, Code général des impôts et ses annexes I à IV, Code de la sécurité sociale, Code de l'urbanisme, Code de la construction et de l'habitation. Le corpus de référence est arrêté au 18 octobre 2026.

La revue recherche les contradictions, les fragilités juridiques, les effets involontaires, les risques de contournement et les difficultés d'application. Les objections sont démontrées, sourcées, classées par priorité, et chacune est accompagnée de corrections possibles.

> **À lire avant tout usage**
> - Cette revue a été conduite par une IA (Claude, d'Anthropic : un coordinateur et 29 agents, dont certains ont délégué à des sous-agents). **Aucun juriste ne l'a validée.**
> - Ses conclusions sont **provisoires**. Elles portent sur l'instantané figé `20261026T230545Z`, pris alors que la seconde passe du projet était encore en cours (11 052 articles relus sur 30 314).
> - Une revue finale des différences avec l'état issu de la seconde passe reste à faire (§ D du rapport).
> - Les corrections proposées sont présentées **séparément des textes courants**. Aucune n'a été intégrée au projet.
> - Rien n'a été modifié dans la production du projet pendant cette revue.

## Commencer ici

| Document | Contenu |
|---|---|
| [`reports/RAPPORT.md`](reports/RAPPORT.md) | Synthèse, portée et limites, conclusions incertaines, méthode et procédure de revue finale |
| [`reports/REGISTRE.md`](reports/REGISTRE.md) | Registre des 303 objections retenues : 4 P0, 111 P1, 188 P2 |
| [`reports/CORRECTIONS.md`](reports/CORRECTIONS.md) | Corrections minimales des P0 et P1, avec les options et les éléments à préserver |
| [`reports/register.json`](reports/register.json) | Registre complet, au format machine : priorité justifiée, nature, statut, articles et versions LEGI, empreintes, citations, raisonnement, conséquences, corrections, incertitudes, preuves |
| [`reports/dossiers/`](reports/dossiers/) | Les 31 rapports de dossier, avec les rédactions intégrales proposées, dont les 5 revues de fond des domaines prioritaires (`DOM-IS`, `DOM-SUCC`, `DOM-SRU`, `DOM-CVAE`, `DOM-TS`) |
| [`reports/dedupe.json`](reports/dedupe.json) | Les 36 doublons entre dossiers et leur fusion motivée |

## Contenu du dossier

- **`reports/`**
  - `p1-work/` : qualification ligne à ligne de chaque alerte examinée (1 943 lignes) et paquets de travail ;
  - les analyses de cohérence :
    - réconciliation de l'inventaire et cohérence base / lots / registre (`consistency-*.json`) ;
    - versions concurrentes ;
    - versions futures déjà publiées ;
    - requalification mécanique des 1 421 alertes P1 de l'audit du 25 octobre (`p1-triage-*.json`) ;
    - abrogations apparues depuis l'audit ;
    - essai de l'outil de différences.
- **`tools/`** : les scripts utilisés, tous en lecture seule sur la production :
  - instantané cohérent (`snapshot.py`) ;
  - vérification de cohérence ;
  - export des pièces citées (`cite.py`) ;
  - requalification des P1 ;
  - assemblage du registre ;
  - revue des différences (`diff_review.py`).
- **Consignes données aux agents** : `BRIEF-AGENTS.md`, `BRIEF-P1.md` et `BRIEF-DOMAINES.md`.
- **`manifests/`** : empreintes par article des deux instantanés pris : source, XML, NOTA, bornes, statut, proposition, motif, notes, lot propriétaire, politiques.
  - `20261026T220621Z` : premier instantané, **rejeté** parce qu'une écriture de la production a été saisie en cours.
  - `20261026T230545Z` : instantané retenu.
- **`evidence/cited/20261026T230545Z/`** : 9 677 exports d'articles cités. Chaque export contient toutes les versions du numéro : source entière, XML LEGI, NOTA, bornes, proposition, motif, notes de revue, ligne de lot, statut d'inventaire, avec leurs empreintes.
- **`evidence/sealed/`**
  - `sealed-manifest.json` : empreintes des 6 982 fichiers des dossiers de preuve datés de la production cités par l'index des contradictions ;
  - les pièces de ces dossiers effectivement citées par une objection, comme le JO de 2010 et la formule E pour D351-9 ;
  - les résultats de l'audit GLOBAL du 25 octobre (`findings.jsonl.gz`, 89 297 signalements), avec son résumé, ses clusters et ses preuves sémantiques.

Tous les chemins `evidence/…` cités dans les rapports et le registre sont présents dans ce dossier.

## Ce qui n'est pas publié ici, et pourquoi

- **L'instantané SQLite lui-même** (2,1 Go, empreinte `809f7341307f5ca5466671783e7ead54b485f3d567db2efa3c3a04044799e309`). Il dépasse les limites de GitHub. Les bases du projet sont publiées ailleurs dans ce dépôt, en parties (`restore-databases.py`). Les empreintes de `manifests/` permettent de vérifier la correspondance de chaque article.
- **Les copies intégrales des dossiers de preuve scellés** (1,2 Go), à l'exception des pièces citées. Plusieurs fichiers dépassent la limite de taille, et 2 885 entrées sont des liens vers des lots vivants. Leurs empreintes figurent dans `evidence/sealed/sealed-manifest.json`.
- **Les journaux de travail et les transcriptions des agents.** Ce sont des sorties intermédiaires de modèle ; leurs résultats sont dans les livrables. Les brouillons du répertoire temporaire partagé n'ont pas été conservés.
- Les fichiers publiés ont été analysés avant publication, avec le même motif de détection de secrets que l'export du projet, et ne contiennent aucune adresse électronique.

## Limites principales

- **Accès aux sources.** Légifrance a répondu HTTP 403 aux agents le 26 octobre 2026. Ce refus n'a pas été contourné. Les lectures du JORF reposent donc sur les preuves déjà scellées. Le droit de l'Union a été lu sur des copies secondaires ou cité de mémoire ; ces points sont marqués « à confirmer ».
- **Périmètre non couvert.** Les ~30 300 articles n'ont pas été relus un à un. Les 87 876 alertes P2 et P3 de l'audit n'ont pas été examinées. Les domaines prioritaires (IS à la distribution, successions, SRU intégral, CVAE, taxe sur les salaires) ont été revus au fond le 27 octobre, mais pas exhaustivement : la couverture réelle de chacun est indiquée dans son rapport et au § A.4 du rapport.
- **Dépendance à la seconde passe.** 189 des 303 objections citent au moins un article que la seconde passe n'avait pas encore relu au moment de l'instantané.

## Vérifier

```sh
# Empreinte d'un export cité
python3 -c "import json,hashlib;d=json.load(open('evidence/cited/20261026T230545Z/css_D351-9_LEGIARTI000030400105.json'));print(hashlib.sha256(d['source_xml'].encode()).hexdigest()==d['source_xml_sha256'])"
```

Après restauration de `corpus.sqlite` par `restore-databases.py`, les outils de `tools/` peuvent être relancés sur un nouvel instantané. `snapshot.py` et `sealed_evidence.py` contiennent des chemins locaux propres à la machine d'origine : ils sont publiés pour la transparence de la méthode et doivent être adaptés avant usage.
