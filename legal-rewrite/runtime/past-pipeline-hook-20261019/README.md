# Proposition de branchement mémoire au pipeline

Le fichier `run_exhaustive.past-hook.proposed.patch` ne modifie que `legal-rewrite/run_exhaustive.py`. Il n’est pas appliqué. Les fichiers juridiques du paquet de 45 articles, la base, les lots, la politique active et les instructions ne sont pas modifiés.

Activation explicite attendue, à créer par le responsable dans `legal-rewrite/past-setup/integration.json` :

```json
{"enabled": true, "recall_mode": "only_when_useful"}
```

Un fichier absent, illisible, non objet, un booléen différent de `true` ou un mode différent désactive le branchement. Aucun réseau ni lecture de clé n’est alors déclenché par ce hook. Il désactive dans tous les cas `mcp_servers.past` pour le worker, ainsi que l’alias local lorsqu’il est inactif.

## Comportement proposé

- Au début d’un lot qui contient effectivement du travail, avant la capture des politiques et avant le premier appel de rédaction : `Synchronizer`, aliasé `SyncEngine`, exécute `run("updates")` dans un sous-processus local borné à trente secondes. Ce moteur ne charge pas de client ou de clé si les corps approuvés sont inchangés. Il garde son périmètre approuvé, ses gardes et son intention durable existants.
- En cas d’échec, d’import manquant, de verrou occupé ou de délai dépassé, la rédaction continue sur les sources locales. Seul un message fixe est affiché ; ni réponse distante, ni exception brute, ni contenu de document, ni identifiant secret ne sont ajoutés aux journaux des jobs.
- Une ingestion en attente peut nécessiter un contrôle réseau même sans nouveau corps modifié. Le cas **sans modification et sans ingestion en attente** n’instancie aucun client. Cette nuance vient du moteur existant ; elle n’est pas masquée par la promesse de « changed-only ».
- Chaque tentative `codex exec` reçoit les options `-c` : serveur compte administrateur désactivé, serveur local `legal_rewrite_memory` en stdio, liste autorisée `past_recall` seulement, serveur facultatif (`required=false`). Aucun rappel n’est lancé, aucun texte de mémoire n’est injecté dans le prompt et aucun appel d’administration n’est exposé par cet alias.
- L’activation est lue une fois au démarrage du lot ; les trois tentatives éventuelles de ce même lot réutilisent la configuration ainsi obtenue. Une modification d’activation s’applique au lot suivant.

Le moteur existant s’appelle `Synchronizer`, et non `SyncEngine`. Le patch emploie un alias dans le sous-processus ; il ne change ni `past_sync.py` ni `past_memory_mcp.py`. Si le serveur local est absent, la rédaction continue et le serveur administrateur reste désactivé. Les règles d’utilisation « seulement lorsque c’est utile » restent à inscrire par le responsable dans les instructions ; le patch n’invente pas de rappel obligatoire.

## Vérification locale, sans appel mémoire réel

`codex-cli 0.160.1` accepte les arguments TOML proposés. Une lecture de configuration par `codex mcp get legal_rewrite_memory --json` a confirmé le transport stdio, l’interpréteur et le chemin local exacts, l’activation et la liste `past_recall`. Cette commande affiche la configuration de l’alias ajouté ; elle ne lance ni agent, ni serveur de mémoire, ni rappel. Les paramètres sont dans `cli-verification.json`, sans clé ou valeur de compte.

Les trente-cinq tests passent : vingt-et-un contrats de synchronisation existants, quatre contrôles mémoire existants et dix contrôles nouveaux du branchement. Les nouveaux contrôles couvrent activation stricte, configuration invalide, indisponibilité et expiration sans blocage, absence de serveur local, propagation des options à toutes les tentatives, saut des lots déjà terminés, absence de client pour un moteur inchangé et envoi du seul corps approuvé modifié avec un client simulé. Les fabriques de clés sont interdites dans ces tests ; les clients réseau sont simulés.

Le contrôle d’application `git apply --check` passe contre le fichier canonique au moment du contrôle. `patch-manifest.json` conserve les empreintes du fichier de base, de la proposition et du patch. La base complète est fournie à titre de comparaison ; si les instructions évoluent entretemps, intégrer seulement les trois zones du patch et refaire le contrôle, jamais remplacer silencieusement tout le fichier par la copie.

## Documentation primaire consultée

- [MCP dans Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) : serveur stdio, `enabled`, `required`, `enabled_tools` et délais.
- [Commandes développeur Codex](https://learn.chatgpt.com/docs/developer-commands?surface=cli) : option répétable `-c key=value` pour `codex exec`.

Les options ont aussi été vérifiées avec l’aide du binaire installé. Aucune modification de configuration personnelle, aucune activation de la mémoire, aucun envoi past.dev, aucune exécution de modèle et aucun service payant n’ont été effectués pour ce patch.
