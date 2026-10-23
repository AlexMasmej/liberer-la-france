# Incident d’enregistrement du 22 octobre, contrôle de16hUTC

Le coordinateur75807 reste unique. Deux secondes passes ont successivement conservé le verrou d’écriture pendant la revalidation et le réenregistrement du corpus entier. Les six rédacteurs avaient terminé leurs réponses, mais leurs enregistrements et les nouvelles admissions attendaient. Les deux prélèvements de piles montrent un calcul et des écritures SQLite en cours ; aucun interblocage définitif n’a été établi.

La progression a repris le22octobre à16h15UTC. Les admissions de seconde passe sont provisoirement limitées à une, avec les six places de rédaction conservées. Les lots déjà actifs finissent normalement. Le plafond autorisé reste huit, sans transfert de place entre les deux rôles. Aucun code actif ni source n’a été modifié par ce diagnostic.

## Correctif prêt, non activé

Le candidat ne modifie que `_register` dans `register_batches.py`. La validation intégrale de tous les lots, la relecture des empreintes avant transaction, les contrôles des sources, avantages, impacts et renvois, les archives, le registre et les rapports sont conservés. Il évite les écritures de lignes strictement identiques sur leurs sept champs et n’analyse les notes une seconde fois que si la preuve source manque réellement. Il n’existe aucun cache de validation entre appels.

Douze cas différentiels, puis25tests existants sur chaque version, passent : contenu de base, preuves source, registre, diagnostics, archives et manifeste de seconde passe identiques. Les sources modifiées, doublons et lot invalide sans rapport avec le lot courant sont toujours refusés. Trois lignes inchangées passent de trois écritures à zéro ; une ligne modifiée produit une seule écriture. Ce résultat de test n’est pas une mesure de gain opérationnel. Les cinq tests du transfert contrôlé passent ; aucun transfert réel n’a été exécuté.

Le contrôle automatique d’autorisation a rejeté la commande comprenant le contrôle préalable du transfert, en considérant qu’une bascule de code et de coordinateur nécessitait un accord explicite sur ce périmètre. La mise en service reste bloquée en attendant cet accord. Aucune exécution indirecte ni relance automatique de cette bascule ne doit être faite avant réponse.

## Reprises conservées

Le correctif CCH combiné reste hors ligne. Bien que149tests isolés et116tests de régression passent, la proposition AnnexeII actuellement enregistrée échoue à la nouvelle garde stricte sur les blancs du modèle. Ce contrôle ciblé a empêché une activation qui aurait bloqué les enregistrements globaux. Les trois autres entrées CCH restent à traiter ; les anciennes réponses ont aussi un renvoi devenu périmé. Une revue de fond et de nouvelles gardes sont nécessaires, sans modifier la source ni forcer le validateur.

Les douze articles de l’ancienne reprise CSS ont désormais tous une seconde passe enregistrée naturellement. L’ancien paquet préparé n’est pas pour autant intégré : onze avant-images et plusieurs gardes ont changé. Ne pas rejouer son ancien utilitaire. Aucun transfert vers la capitalisation n’est compté comme baisse de prélèvement.

Le rafraîchissement de l’audit global reste différé sous le seuil impératif de6Gio libres. Aucune nouvelle capture volumineuse n’a été lancée. Les contrôles par lot continuent ; l’audit final et la validation juridique humaine restent à faire.


## Mise en service approuvée et vérifiée

Accord explicite reçu de l’utilisateur, conservé dans user-approval.json. La première attente a été suspendue sur un délai de lecture système ; la reprise conserve le verrou de supervision pendant tout inventaire indisponible et refuse de le traiter comme vide (7tests de transfert conformes). L’ancien coordinateur75807 a fini ses lots, les validations et la publication des cinq sites puis est sorti avec code0. Le seul module register_batches.py a été remplacé par le candidat épinglé. Le coordinateur90405 est unique, avec six places nouvelles et une de relecture provisoire. Sept réponses réelles Astra/medium et les premières acceptations sont attestées. À la première vérification, les98entrées en vol étaient retrouvées :85déjà enregistrées,12relues et1remise en file. Cette dernière a ensuite été traitée :86sont enregistrées et12relues. Voir RESOLUTION.json et resumption-verification.json pour les compteurs horodatés. Aucun gain de débit ni achèvement juridique global n’est déclaré. Les correctifsCCH/CSS restent exclus ; le nouvel examen CCH est conservé hors ligne dans runtime/cch-current-annexeII-semantic-20261022T1735Z.
