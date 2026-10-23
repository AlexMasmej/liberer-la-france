# Diagnostic des différés — 22 octobre 2026, 22 h 27 UTC

Lecture seule du corpus et des preuves ; seules les pièces de ce nouveau dossier ont été écrites. Aucun lancement, signal, changement de place, politique, catalogue, source ou écriture canonique. La lecture SQLite utilise `mode=ro` et une transaction cohérente ; aucune nouvelle copie volumineuse.

## Transition 18713 → 3122 : faits et limites

- `stop-request.json` atteste que **18713 a reçu SIGTERM (15) à 20 h 45 min 26 UTC**. Son journal s'achève sur « STOP requested; preserving current jobs and all accepted batches. » Plusieurs tâches ont retourné `stopped`. On ne peut donc pas décrire cette disparition comme une fin naturelle démontrée de la file.
- L'identité de l'émetteur du signal et son motif ne sont **pas établis** par ces pièces. Le dernier `coordinator-exit.json` copié porte encore 90405 : il ne certifie aucun code de sortie de 18713. Le journal de 18713 ne contient pas de nouvelle trace ENOSPC dans sa fin conservée. Ne pas attribuer son arrêt au stockage, au quota ou au superviseur sans preuve supplémentaire.
- Le superviseur constate l'absence de coordinateur à **20 h 54 min 10 UTC** et lance 3122 à **20 h 54 min 15 UTC**. Le nouveau fichier de démarrage porte 3122, capacité autorisée 8, admission effective 6 nouveaux + 1 relecture, Astra/Moyen. Il est ensuite adopté par le superviseur. Les événements utiles sont dans `supervision-transition.json`, les en-têtes et dispositions dans les entrées hachées du manifeste.
- À la capture, les métriques de 3122 attestent **6 lots nouveaux acceptés (144 articles)** et **1 lot relu (1 article)**, avec sessions natives distinctes Astra/Moyen et réponses effectivement commencées. Les journaux d'exécution et les compteurs confirment des acceptations ; le seul PID ou la configuration ne constituent pas ces preuves.

## Huit nouveaux différés de la cohorte 3122

| Cause observée | Lots | Nouveaux articles | Articles à relire |
| --- | ---: | ---: | ---: |
| Échecs d'invocation pendant les erreurs de routage/transport | 7 | 144 | 12 |
| Citation d'impact non exacte après deux invocations échouées | 1 | 24 | 0 |
| Total | 8 | 168 | 12 |

Les sept lots de transport sont `travail-00390-resume-8xwzxqkr`, `00391-resume-9ddhfzp3`, `00392-resume-r8slrmae`, `00393-resume-79i5mk7x`, `00394-resume-s23jiobi`, `00395-resume-_hyx052s` et `review-travail-LEGIARTI000035653236-00001`. Le huitième est `travail-00396-resume-d9t22r7o`.

Les trois essais de chacun des sept premiers lots ont des erreurs natives `workspace routing discovery failed` ou `timed out`, reconnexions et erreurs d'envoi du transport MCP ; aucun début de réponse de modèle n'est attesté pour eux. Les copies filtrées conservent les lignes natives d'erreur, les chemins et empreintes des journaux complets restent dans `inputs-manifest.json`.

Ces lignes d'erreur n'établissent **aucune erreur de quota, de facturation, 401/403 ou 429**. Aucun test authentifié ni modification de compte n'a été tenté. Le succès de nouvelles réponses puis de lots acceptés établit une reprise ultérieure ; les résultats mêlant la panne et cette reprise ne servent pas à prouver un gain de débit ni à rétablir la deuxième place de relecture. Les 27 reprises `invocation` de cette cohorte ne sont pas 27 collisions juridiques.

Le registre complet compte 79 échecs historiques à la capture. `failed-job-resolutions.json` a été lu : il contient la résolution explicite de travail-00124 seulement. L'absence d'une entrée de résolution ne prouve pas qu'un ancien article est encore absent ; la disposition est mesurée ci-dessous pour les huit lots demandés. Les anciennes douze secondes passes CSS déjà achevées ne sont pas réouvertes.

## Disposition canonique mesurée

`deferred-disposition.json` conserve les 180 identités une par une et les contrôles source/NOTA/versions, dans une seule transaction de lecture :

- **168 nouveaux articles : aucun draft en base**, aucune acceptation revendiquée pour ces lots. Leurs identités figurent dans la file persistée au démarrage de 3122.
- **12 articles de relecture : les 12 drafts antérieurs existent, mais les 12 secondes passes restent `pending`**. L'existence de l'ancien draft ne signifie pas que la relecture échouée a été acceptée. Ils figurent dans la file persistée de relecture.
- Toutes les sources, NOTA et versions comparées concordent avec les affectations figées. Une appartenance à la file de démarrage ne signifie ni admission active ni acceptation ; ces lots ont été consommés comme différés dans la cohorte active et doivent être repris lors d'une reconstruction coordonnée sûre, sans arrêter un lot valide.

## Correctif de seule métadonnée préparé, non intégré

Le dernier essai de `travail-00396-resume-d9t22r7o` a produit une réponse Astra/Moyen complète et est sorti 0, puis le validateur a correctement refusé le lot. L'unique erreur de passage exact détectée est dans R5315-5 (`LEGIARTI000033407486`), effet `afpa-comites-facultatifs` :

- Ancienne citation : `… institué ;3° Un comité …`
- Citation exacte dans le texte déjà proposé : `… institué ; 3° Un comité …`

Le parseur officiel insère une séparation entre les deux paragraphes ; l'autocontrôle du rédacteur utilisait une suppression de balises qui les concaténait. Ce constat explique le refus sans le contourner. Le correctif ajoute **une seule espace dans `substantive_impact.effects[0].proposed_quote`** et ne change aucun des 24 textes normatifs, motifs ou notes. La source et la proposition complètes de R5315-5, les NOTA vides, la réforme des comités, le maintien de l'audit, des nominations, du contrôle économique et financier, des compétences du conseil et de la transition ont été lus ; ce contrôle borné ne certifie pas le fond des 24 articles ni leurs normes extérieures.

Pièces dans `metadata-repair/` : original conservé, candidat distinct, sources et cibles figées, contexte entier de l'article, résultat natif, échec original et `validation.json`.

Les vrais contrôles hors ligne ont donné :

- refus de l'original reproduit ;
- `validate_answer` candidat : 24 articles conformes ;
- `accept_checks` candidat : conforme ;
- `check_guards` sur les cibles actuelles : conforme à la capture ;
- `register_batches.validate_batches` sur le seul lot candidat dans un dossier isolé : 24 articles conformes ;
- sources/NOTA/versions/politiques : concordantes ; les 24 avant-images restent absentes ;
- aucun certificat nouveau n'a été injecté dans le candidat préparé et aucune intégration n'a été exécutée.

Avant une éventuelle intégration, le parent doit recontrôler les identités, propriétaires et absences d'avant-image, toutes les empreintes sources/NOTA/versions/politiques/code, les cibles entières et leurs gardes, puis utiliser les réservations et gardes transactionnelles normales dans une phase coordonnée. Si une garde a dérivé, ne pas recycler son ancien certificat. Les autres lots de transport demandent de nouvelles réponses, pas une fabrication de contenu ni une acceptation d'un fichier vide. Le candidat préparé ne compte pas comme 24 articles traités.

À la demande du parent, un helper distinct et borné est prêt dans `metadata-repair/register_metadata_only.py`, accompagné de `INTEGRATION-DRAINED-ONLY.md`, d'un manifeste de 35 fichiers et de 24 gardes canoniques. Il refuse toute application pendant les lots actifs et exige les quatre verrous non bloquants supervision/coordinator/writer/manualslots ainsi qu'un inventaire système connu, vide de coordinateurs/workers du chantier. Ses 25 tests isolés passent ; ses gardes fichiers/sources/NOTA/documents/versions/absence et renvois ont encore été contrôlées en lecture seule à 22 h 33 min 57 UTC. **Son point d'entrée opérationnel n'a pas été exécuté** : ni précontrôle drainé réel, ni application, ni signal, ni prise de place. Ces tests ne prouvent pas une disponibilité des verrous ou un point drainé effectif.
