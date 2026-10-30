# Z02 — sixième balayage (S16b, S18, S19a, S19b), code de la sécurité sociale

Textes lus en production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite `mode=ro`), le 30 octobre 2026. Paquet : 51 articles, 63 pistes. Qualification au critère de l'audit : un juriste qui ouvre l'article le jugerait-il anormal ?

Contrôle : `python3 -B apply/check_changes.py Z02` construit et valide 5 lignes, et `python3 -B apply/check_changes.py B01zb` en construit et valide 1. Dans les deux cas, `problems` est vide. Les diagnostics sont voulus : renvois retirés (L251-1, L162-1-9, L512-2) et réductions déclarées.

Décompte : 53 faux positifs, 6 G (tous corrigés), 4 m (non corrigés, car ils portent sur des articles non modifiés ici), 0 déjà réglé. Requests : aucune.

## Corrections (G)

### Dans `apply/Z02/changes.json` (articles sans `previous_owner`)

- **SWEEP-Z02-R251-9**, R251-9 (LEGIARTI000038789380, maintenu ; S16b, F3).
  - Défaut : la phrase « qui lui sont affectées par l'arrêté pris en application de l'article L. 251-1 » renvoie à L251-1, dont aucune version n'est en vigueur depuis le 1er janvier 2001.
  - Ce qui change : le renvoi mort est retiré (« qui lui sont affectées. »). Le fonds, ses recettes, ses dépenses et les remises mutualistes restent inchangés. Aucune base de remplacement n'est inventée.
  - Mise en œuvre : la ligne passe en `rewrite_draft` et `coordination_only`.
- **SWEEP-Z02-R413-7**, R413-7 (LEGIARTI000039344544 ; S19a, F3).
  - Défaut : à partir du 1er novembre 2026, la prestation pour tierce personne passe au II de L434-2 (LEGIARTI000051288493). Le troisième alinéa de cet article devient alors la part fonctionnelle de la rente.
  - Ce qui change : « prévue au troisième alinéa de l'article L. 434-2 » devient « prévue à l'article L. 434-2 », ce qui reste exact avant et après le 1er novembre 2026. La note devenue fausse est corrigée.
- **SWEEP-Z02-D752-2-1**, D752-2-1 (LEGIARTI000041968338, maintenu ; S19a, F3).
  - Défaut : à partir du 1er janvier 2028 (LEGIARTI000054466934), le troisième alinéa de L752-1 vise Saint-Martin. La caisse de Saint-Barthélemy passe au quatrième alinéa.
  - Ce qui change : la caisse est désignée par sa mission (« à laquelle l'article L. 752-1 confie l'application de la législation de sécurité sociale à Saint-Barthélemy »).
  - Mise en œuvre : `coordination_only`.
- **SWEEP-Z02-R613-18**, R613-18 (LEGIARTI000048856323, maintenu ; S19a, F3).
  - Défaut : même décalage de L752-1 en 2028.
  - Ce qui change : « au troisième alinéa de l'article L. 752-1 » devient « à l'article L. 752-1 pour Saint-Barthélemy ». La coquille « à l'articles », qui vient de la source, est conservée. La note devenue fausse est corrigée.
- **SWEEP-Z02-L162-5**, L162-5 (LEGIARTI000051140851 ; S18, F3).
  - Défaut : le 26° dit « dans le respect des dispositions des articles L. 162-1-9 et L. 162-1-9-1 ». Or L162-1-9 (la commission des équipements lourds) est abrogé par le projet.
  - Ce qui change : le renvoi ne vise plus que L162-1-9-1. Un effet `coordination` est ajouté au bilan d'impact.

### Variante `apply/B01zb/` (article dont le `previous_owner` est B01)

- **SWEEP-Z02-L757-5**, version de L757-5 applicable à Mayotte en 2028 (LEGIARTI000054467074, sans proposition, mode `new` ; S19b, F4).
  - Défaut : le a du 2° remplace, au dernier alinéa de L842-5, « les conditions mentionnées à l'article L. 512-2 » par les conditions de séjour régulier à Mayotte exigées des enfants. Or L842-5 proposé ne contient plus ces mots. Il dit que les enfants « ne sont soumis à aucune condition supplémentaire tenant [...] à la régularité de leur entrée ou de leur séjour ».
  - Ce qui change : seul le a est retiré. Le 1° (renvoi au CESEDA applicable à Mayotte) et l'alinéa sur le statut civil de droit local sont conservés.
  - Mise en œuvre : `normative_reduction`, et `coordination_only` sous la mesure `prestations-familiales-fin-conditions-entree-enfants`.
  - Point laissé à l'auteur : garder à Mayotte une condition propre de séjour régulier des enfants serait un choix politique distinct, que le projet n'a pas tranché.

## Défauts mineurs (m), non corrigés

- **L162-14-1** (LEGIARTI000048688021) : le renvoi « en application des articles [...] L. 646-3 » vise une contribution que le projet abroge pour l'avenir. Il ne peut plus viser que les périodes antérieures. Sans effet.
- **L131-7** (A7, LEGIARTI000051285503) : « aux trois derniers alinéas de l'article L. 137-15 ». L137-15 proposé est une abrogation : la mention « dans sa rédaction antérieure » manque. Sans effet pour l'avenir. Aucune variante A7 n'est créée.
- **L131-8** (B04, LEGIARTI000053538201) : les 3° ter (L136-7-1 III) et 5° (L137-14) affectent le produit de contributions supprimées, sans la limite dans le temps écrite aux 1° et 6°. C'est seulement rédactionnel : l'article n'autorise aucun prélèvement. Aucune variante B04 n'est créée.

## Faux positifs (53), par motif

- **Renvoi limité à la transition ou à l'ancien régime** (le texte cité ne sert que pour le passé, ou il est neutralisé) :
  - R652-33 (×2), R133-9 (B09), R862-11-6, R382-95, L138-19-13, R532-3, R532-1, D545-5, R543-6 (B09), D545-8 (B09) et D742-31 ;
  - R582-8, L815-29 (×2), L243-1-3, D133-2, L382-35, L382-39, L382-41, L223-9 (×2, B01) et L162-1-9-1 ;
  - L241-6-2 (×2), L622-1 (×2), L169-2, L162-22-11-1 (B09), L162-30-4 (A4 ; le renvoi vise expressément « dans sa rédaction antérieure ») et R114-11 ;
  - L162-5 (pour L162-5-2), L241-10 (A9), L314-1, L241-3 (×4, B01), L241-13 (B01) et R373-1.
- **Liste d'affectation couverte par une clause générale sur les ressources supprimées** : L241-2 (×3, B05).
- **Article d'un autre code de même numéro** :
  - code de l'action sociale et des familles : L133-8-3, L136-1-3, L223-17 et L223-8 ;
  - code de commerce : L133-8-6 ;
  - code rural et de la pêche maritime : D531-15.
- **Version future qui n'écrase pas la réforme** :
  - L757-4 (B01) : l'adaptation porte sur le deuxième alinéa de L821-1, que le projet ne modifie pas ;
  - L758-5 : simple ajout d'un V à L911-7 ;
  - L759-22 (B01) : deux alinéas ajoutés à L351-1, dont les renvois restent exacts ;
  - L759-12 (B01) : adapte seulement L861-2, qui est maintenu.

Les articles de l'annexe II 371 et du chapitre R135 du CSS (groupe X8) n'ont pas été touchés.

Revue IA : rien de ceci ne vaut validation par un juriste.
