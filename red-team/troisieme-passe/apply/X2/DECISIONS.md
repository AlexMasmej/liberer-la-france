# X2 : décisions sur les 12 défauts grossiers du troisième audit aléatoire

J'ai lu la production en lecture seule : `CITE_PRODUCTION=1 tools/cite.py`, sqlite en `mode=ro`, et les lots de production en lecture seule. Les pièces citées sont sous `evidence/cited/production-20261029/`. Je n'ai rien écrit en production.

Légifrance a été consulté le 29 octobre 2026 pour l'article 26 de la loi n° 2025-127 : la page n'a pas restitué le texte. Les abrogations du CGI sont donc établies par les états et les liens LEGI du corpus.

## Bilan

- Les 12 défauts sont confirmés. Tous sont corrigés ; un seul l'est partiellement (Q230).
- `apply/X2/changes.json` modifie 42 articles. Le contrôle `python3 -B apply/check_changes.py X2` donne `problems: []`, avec 42 lignes construites et 42 validées.
- `apply/Y09b/changes.json` porte une variante pour le groupe Y09, propriétaire de R452-25. Le contrôle `check_changes.py Y09b` donne `problems: []`.
- Aucune ligne `requests` ni `skipped`.
- Identifiants des objections : `AUDIT3-Q<n>`, suivis de l'objection du registre quand elle existe.
- Diagnostics : tous voulus.
  - Renvois ajoutés : L823-7 dans les cinq décrets d'aide au logement, L145-6, R122-1 et L312-9.
  - Renvois retirés par les abrogations : A. 26-3, A. 26-4 et A. 85-1 du LPF.
  - Rapports de longueur dus aux abrogations motivées de l'annexe IV et aux transitions.
  - Les autres diagnostics sont antérieurs : ils portent sur des articles dont seules les notes changent.

## Par défaut

### Q281 — annexe II 379, 380 et 381 (RT-P1-CGI-C-04) : appliqué

- **Constat.** 115 quinquies et 1673 bis proposés abrogent la retenue pour les exercices nouveaux, « qu'ils demeurent en France ou soient désinvestis hors de France ». Or 379, 380 et 381 organisaient encore un « régime nouveau » de retenue au désinvestissement.
- **Ce qui change.**
  - **379.** La source est reprise à droit constant pour les exercices ouverts avant l'abrogation. Un 4 ajouté dispose qu'aucune déclaration ni aucun versement n'est exigé pour les exercices nouveaux. La branche « 15 du mois suivant » est retirée.
  - **380.** La période spéciale de désinvestissement et l'ancien IV (correction immédiate) sont supprimés. La phrase sur la double restitution, l'article 382 et l'article 381 est conservée. Un nouveau IV borne l'article aux retenues des exercices antérieurs, y compris pour les demandes présentées ensuite dans le délai.
  - **381.** La dernière phrase porte désormais sur les retenues des exercices antérieurs, et non plus sur des « distributions futures ».
- **Ce qui est préservé.** La révision à douze puis trois mois, la restitution au 31 décembre, la preuve libre et l'absence de double restitution.
- **Pour l'auteur.**
  - La discordance de délai entre 379 (délai de la déclaration des résultats) et 1673 bis (15 du quatrième mois ou 15 mai) existait déjà dans le droit en vigueur. Elle n'est pas tranchée.
  - Les notes de 115 quinquies et de 1673 bis, qui annoncent cette coordination, ne sont pas modifiées.

### Q301 — urba L121-8 / L121-3 : appliqué

- **Ce qui change.**
  - **L121-3**, jusque-là maintenu, passe en `rewrite_draft` / `coordination_only`. Le SCoT détermine toujours les critères et la localisation des villages et agglomérations. Pour les autres secteurs déjà urbanisés, il peut les préciser, sans que cela constitue un préalable. C'est la même formule que L141-13.
  - **Transition.** Les schémas approuvés ou en cours et les demandes en cours en bénéficient, sans nouveau dossier. Les identifications existantes restent utilisables et ne rendent aucun schéma illégal.
  - **Notes de L121-8** rectifiées, sans changement du corps.
- **Ce qui reste inchangé.** Le premier alinéa, le « second alinéa » visé par L312-9 et les dérogations littorales.
- **Pour l'auteur.** Le 2° de L312-9 (relocalisation) conserve son propre préalable : secteurs « identifiés par le SCoT et délimités par le PLU ». Il n'est pas modifié.

### Q222 — annexe IV, bloc 124 à 154 (RT-P1-ANNEXES-11) : appliqué

- **Constat.** CGI 1559, 1560, 1563, 1565, 1566 et 1700 sont abrogés au 1er janvier 2025 (loi n° 2025-127, art. 26). CGI 1561, 1564 et 1565 bis le sont au 1er janvier 2015 (loi n° 2014-1654, art. 21). L'impôt ne visait plus que les cercles et maisons de jeux depuis 2015, puis les seules maisons de jeux depuis 2019. Les propositions de la section maintenaient ou allégeaient pourtant ses formalités, dont 152 et sa déclaration mensuelle.
- **Ce qui change.** Abrogation (`full_repeal`, `coordination_only`) de 17 articles : 126, 126 F, 127, 128, 129, 131, 131 A, 139, 145, 146, 147, 149, 150, 151, 152, 153 et 154. Trois d'entre eux (147, 153 et 154) étaient maintenus et passent en `rewrite_draft` ; les autres avaient une proposition d'allègement.
- **Transition de chaque abrogation.**
  - Les impositions nées avant les abrogations, leurs contrôles, restitutions, prescriptions et recours gardent leur régime.
  - La loi répressive plus douce s'applique.
  - Les obligations comptables, de conservation et de police des jeux ayant un autre fondement demeurent.
  - Aucune formalité de remplacement.
- **Exemption de 126 F.** L'exemption sportive est expressément maintenue pour les impositions antérieures. Pour l'avenir, l'impôt n'existe plus : aucune faveur n'est perdue.
- **Articles non modifiés.** 124, 130 et 137 sont déjà abrogés par leur proposition, et 138 par AUDIT2-T236. Les notes de 124 tiennent encore CGI 1565 pour « absent » : c'est un défaut mineur, non corrigé.
- **Pour l'auteur.**
  - Une recodification de l'impôt dans le CIBS n'est pas vérifiée, car le CIBS n'est pas au corpus. Même dans ce cas, les renvois de ce bloc au CGI seraient morts.
  - Les arrêtés d'application (modèles, arrêté de 1993) et le LPF sont hors corpus.

### Q242 — CCH L823-7 et ses décrets : appliqué

- **Ce qui change.**
  - **D823-16, D832-10, D832-24, D842-6 et D842-15**, maintenus jusque-là, passent en `coordination_only`. Leur dernier alinéa réserve le non-versement sous seuil aux mois commençant avant l'abrogation de L823-7. Pour les mois nouveaux, tout montant positif est versé, sans démarche. Le reste de chaque formule est repris mot pour mot.
  - **R823-6.** La mention du « seuil de versement » est réservée à ces mois antérieurs.
  - **Notes de L823-7** mises à jour.
- **Pourquoi c'est aligné.** La réforme est déjà décidée par L823-7 proposé. Ces modifications la rendent effective, sans extension supplémentaire.
- **Pour l'auteur.**
  - Les arrêtés de seuil, hors corpus, restent à abroger pour l'avenir.
  - Les champs `reference_coherence` et `reference_checks` hérités des lignes portent d'anciennes empreintes. Ils sont à rafraîchir par l'outil d'application.

### Q104 — urba R151-33 / L151-9 : appliqué (point pour l'auteur)

- **Ce qui change.**
  - **L151-9 proposé** reçoit un quatrième alinéa. Les interdictions et conditions particulières relatives aux usages, activités, destinations et sous-destinations ne peuvent être édictées que pour la sécurité ou la salubrité, dans le respect de la vocation générale des zones.
  - **Exclusions.** Le zonage, les règles propres aux zones A, N et F, et les régimes spéciaux : mixité, services publics, risques, nuisances, ressources, environnement, continuités écologiques, littoral, patrimoine et réseaux.
  - **Transition.** C'est celle des décrets : décisions futures et demandes en cours, sans nouveau dépôt ; les autorisations et décisions définitives sont préservées.
  - **Notes de R151-33 et R151-30** : la coordination législative « toujours ouverte » est indiquée comme faite. Leur corps est inchangé.
- **Pourquoi.** C'est la correction suggérée par l'audit, dans le sens de la réforme (moins de contraintes). Le troisième alinéa garde son rang pour CCH L631-7-1 A.
- **Pour l'auteur.** Cet alinéa élève au niveau législatif une coupe décidée au niveau réglementaire. Son étendue est celle de R151-30 et R151-33 et mérite confirmation.

### Q194 — CCH R126-14 / L126-34 / L126-35 : appliqué

- **Ce qui change.** L126-34 (premier et troisième alinéas) et L126-35 3° ne visent plus le récolement. R126-14 proposé abroge en effet le formulaire de récolement, seul texte qui l'instituait. Les notes de R126-14 sont mises à jour.
- **Ce qui reste.** Le diagnostic, sa communication aux intervenants et aux autorités (L126-37), l'indépendance du diagnostiqueur et la traçabilité des déchets du code de l'environnement.

### Q196 — annexe III 178-0 bis : appliqué (abrogation)

- **Constat.** CGI 438 est ABROGE au 1er janvier 2022 (ordonnance n° 2021-1843, art. 10, concordances vers CIBS L313-15 à L313-17). 302 D est également abrogé.
- **Ce qui change.** L'article est abrogé. Pour les opérations antérieures, le bénéfice du tarif reste régi par les règles antérieures, avec la preuve libre déjà décidée par le brouillon et les justificatifs déjà délivrés. Aucune justification n'est exigée pour l'avenir.
- **Notes.** L'affirmation « absents du corpus » est rectifiée.
- **Pour l'auteur.** Un tarif équivalent dans le CIBS, hors corpus, relève de ses propres textes. L'abrogation n'y ajoute aucune condition.

### Q286 — CCH L633-5 : appliqué

- **Ce qui change.** Le quatrième tiret vise désormais les programmes des troisième et cinquième alinéas du III de L441-2, y compris ceux des autres bailleurs du septième alinéa, ainsi que les programmes autorisés avant la réforme. L'article, jusque-là maintenu, passe en `coordination_only`.
- **Conséquence.** L'exclusion du régime des logements-foyers survit à la suppression des autorisations spécifiques, sans formalité.

### Q287 — CSS R122-1 / R123-50-1 : appliqué

- **Ce qui change.**
  - **R123-50-1, 2°.** L'agrément des agents comptables de la MSA nationale appartient au seul ministre chargé de l'agriculture, « sans agrément conjoint du ministre chargé du budget, dans les conditions de l'article R. 122-1 ».
  - **Transition** identique à R122-1 : procédures en cours sans nouveau dossier, agréments en vigueur maintenus.
  - **Le 3°** (retrait conjoint) est conservé, comme le prévoit R122-1.
  - **Notes de R122-1** mises à jour.

### Q158 — CCH R452-25 : appliqué dans `apply/Y09b/` (propriétaire Y09)

- **Ce qui change.** La phrase annonçant l'abrogation de L452-5 au 1er janvier 2027 est remplacée par un renvoi à L452-5 « dans ses rédactions successives, y compris celle applicable à compter du 1er janvier 2027 ».
- **Notes.** Elles sont corrigées : le successeur LEGIARTI000053151495 figure au corpus et porte une proposition.
- **Ce qui ne change pas.** Le reste de l'article.

### Q110 — CSS R752-18-5 et R752-18-4 : appliqué

- **Ce qui change.** La présidence de la section de La Réunion-Mayotte revient à un magistrat « nommé dans les conditions prévues à l'article L. 145-6 ». C'est la même rédaction et la même transition que R752-18-3 pour les Antilles-Guyane. Les deux articles, jusque-là maintenus, passent en `coordination_only`. Les assesseurs et la compétence sont inchangés.
- **Pour l'auteur.**
  - Aucune loi ultramarine dérogatoire hors CSS n'a été vérifiée, et R752-17 n'a pas été relu en entier.
  - La nomination des assesseurs par le président du tribunal administratif, alors que L145-6 la confie à « l'autorité compétente de l'Etat », n'est pas modifiée. C'est aussi le cas aux Antilles.

### Q230 — annexe II 242 nonies B (RT-P1-ANNEXES-02) : partiellement appliqué

- **Ce qui change.**
  - **Pièces d'immatriculation.** Les transmissions de données à l'administration (supprimées par 289 E, 290 et 290 A) et la solution de 242 nonies G (abrogée) n'en conditionnent plus aucune :
    - 7° c devient une dispense ;
    - au 7° d, l'essai avec 242 nonies G est retiré ;
    - aux 5°, 7° b et 7° e, les mentions des données de facturation, de transaction et de paiement sont retirées.
  - **Transition (VI).** Elle couvre ces suppressions et préserve les immatriculations délivrées.
  - **Motif.** L'erreur sur le « précédent V » est rectifiée.
- **Non traité.** 242 nonies C organise toujours un renouvellement triennal, alors que 290 B proposé attribue le numéro « sans limitation de durée ». Je ne l'ai pas abrogé : 41 septies A de l'annexe IV renvoie au 1° et au IV de 242 nonies C, et organise encore les audits de renouvellement et de surveillance ainsi que les contrôles de transmission. Une coordination propre exigerait de traiter aussi la partie annexe IV de RT-P1-ANNEXES-02 (41 septies A, D, G, H, M et P), hors de mon lot.
- **Pour l'auteur.** Traiter ensemble 242 nonies C et 41 septies A, D, G, H, M et P.

## Résumé

12 défauts confirmés, dont 11 corrigés entièrement et 1 partiellement (Q230 : 242 nonies C et l'annexe IV laissés). 42 articles sont modifiés dans X2 et 1 dans Y09b, et les deux contrôles donnent `problems: []`. Aucune formalité ni sanction de remplacement n'est créée ; les droits acquis, les impositions antérieures et les instances en cours ont leur transition.

Points laissés à l'auteur :
- L151-9 élève au niveau législatif la coupe de R151-30 et R151-33 ;
- le CIBS est hors corpus pour l'annexe IV et pour 178-0 bis ;
- les arrêtés de seuil des aides au logement restent à abroger ;
- 242 nonies C et 41 septies A restent à traiter ;
- le préalable propre de L312-9 n'est pas modifié.

Revue IA : rien de ceci ne vaut validation par un juriste.
