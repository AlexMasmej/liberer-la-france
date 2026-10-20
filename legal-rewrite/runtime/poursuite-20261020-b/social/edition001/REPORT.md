# Lot social B — affiliation, déclaration et recouvrement

Lot proposé, non enregistré : 24 articles de l’inventaire courant des 30 317 entrées, sans proposition à la capture. Les 24 sources et leurs notes ont été lues intégralement ; 33 cibles avec leurs notes et propositions courantes ont également été lues en entier. Les captures sont dans `source.json` et `context.json`, avec sources officielles, empreintes du corps et des notes, avant-images et empreinte des propositions antérieures. Les deux politiques actives ont été copiées et leur empreinte reste conforme au contrôle final.

Huit articles proposés entièrement, seize maintiens nécessaires avec `proposed_xml: null`. Un article maintenu n’est pas déclaré réécrit. Les modifications sont des choix normatifs ciblés ; toutes les autres dispositions de ces articles restent présentes dans le corps proposé.

## Effets réellement identifiés

**R243-8 : autorisation préalable de versement en lieu unique supprimée.** La demande existante vaut option. L’entreprise doit toujours être à jour de ses déclarations et paiements, choisir un organisme de la liste légale et respecter échéances, DSN et dette. Le régime obligatoire des grandes entreprises reste celui de R243-6-3, dont le III est conservé. Les autorisations antérieures gardent leurs effets ; les dossiers en cours ne sont pas à redéposer. Une seule mesure : `versement-unique-fin-autorisation`.

**R131-9 : accès au report de début d’activité malgré un premier paiement.** Le délai de demande de trente jours reste applicable, mais un versement déjà effectué ne ferme plus le report pour les sommes restant dues dans le champ de L131-6-1. Ce report n’ouvre pas à lui seul de remboursement des sommes payées. Douze mois, étalement maximal de cinq ans, fractions annuelles minimales de 20 %, limite d’une demande par cinq ans et absence de majoration sont conservés dans L131-6-1. Le règlement conserve dates d’exigibilité, prorata et paiement de cessation sous soixante jours. C’est une facilité de calendrier, **pas une baisse permanente de cotisations** : `indep-report-premier-versement`.

## Coordinations utiles sans nouvelles économies démontrées

Les articles L613-2, R613-1-1, R613-1-2 et R613-1-5 coordonnent la déclaration sociale subsidiaire, la demande de données fiscales et la cessation : ne pas redéclarer les données exactes, à jour et légalement disponibles ; fournir les données manquantes et corriger les erreurs. Les pénalités de 5 % ou 10 % ne reposent pas sur la seule absence d’un doublon dispensé. Les déclarations fiscales, les données réellement manquantes, les bases, les taux, le calcul provisoire, les régularisations et les dettes restent applicables. Les quatre articles partagent `indep-declaration-sociale-reemploi`.

R611-1 coordonne le signalement des changements déjà légalement reçus ; R243-43-1 coordonne la production des documents dans la demande d’arbitrage ACOSS. Ils conservent délais, motivation, pièces réellement manquantes et garanties des recours. Ni l’un ni l’autre ne revendique une nouvelle économie nette indépendante.

Cette prudence vient d’un contrôle primaire : [L113-12 du CRPA](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045213328) protège déjà le réemploi de données détenues ou obtenables par le système légal d’échange ; [L100-3](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000031367308) inclut les organismes sociaux. Les conditions de finalité et d’accès restent celles de L114-8 et L114-9. La proposition ne crée aucun pouvoir d’accès général et aucune attestation de remplacement. Elle ne prétend pas supprimer l’attestation déjà prévue par L113-13 dans son champ propre.

Les corps entiers L100-3, L113-12, L114-8 actuel et L114-9 sont extraits et hashés dans `crpa-primary-bodies.json`. Les deux fichiers `crpa-*-primary-search.json` conservent le retour primaire complet avec URL et versions. Provenance : textes Légifrance renvoyés par l’outil de recherche ; l’ouverture directe a renvoyé 403. **Aucun XML DILA original de ces quatre articles n’a été récupéré.** Les résultats historiques conservés dans la capture brute ne remplacent pas la version de L114-8 applicable depuis le 23 février 2022.

## Maintiens et protections

Les seize maintiens sont motivés individuellement : champ d’affiliation et options des loueurs ; informations et simulation ; procédure contradictoire de radiation ; affiliation territoriale et dérogations ; proratas ; remboursement et ordre d’imputation des trop-versés ; échéancier déjà commun à plusieurs appels ; contrôle de données complémentaires nécessaires ; notification de redressement et réponse motivée ; échéances ; paiement trimestriel déjà reconduit tacitement ; interlocuteur des employeurs étrangers ; droit à correction sans majoration dans les conditions légales.

R613-18 prévoit déjà le rapprochement avec les pièces reçues et les informations légalement communicables. Aucune suppression nouvelle de doublon n’y est fabriquée. R613-5 prévoit déjà un échéancier multi-usages et R243-6-1 une reconduction automatique : ils ne sont pas revendiqués comme des fusions nouvelles. Les avertissements de radiation et de redressement servent des phases différentes et conservent les recours.

Les cinq règlements initialement rencontrés du microsocial ont été retirés de la sélection. L613-7, D613-4, D613-6, Acre, les taux et exonérations DOM ne sont pas modifiés. L613-2 conserve intégralement son III microsocial ; les autres références à ce régime dans les articles maintenus ne le réécrivent pas. La version historique concurrente de R611-2 a aussi été retirée : seule LEGIARTI000043292679 est sélectionnée.

Aucune règle du contrat unique, des quinze jours, de l’indemnité de 0,20 mois, du seuil d’un an ou du plafond de six mois n’est modifiée. La durée du séjour ou de la période de paiement de L243-1-2 ne devient pas un terme automatique du contrat. Aucun salaire, congé, remboursement, protection, avantage futur recevable ou droit acquis n’est supprimé. Aucun transfert vers la capitalisation n’est compté comme baisse de cotisations.

Aucun renvoi direct à la taxe sur les salaires ou à l’article 231 n’a été trouvé dans les 24 sources sélectionnées. Les renvois fiscaux, notamment 170/175 et les formalités 87/87-0 A dans le contexte DSN, sont conservés ; aucune suppression de taxe sur les salaires n’est annoncée ni opérée ici.

## Vérifications et limites

`validate_answer` passe sur les 24 objets sans changer leurs certificats. Le contrôle final relit les sources, corps, notes et avant-images des 57 articles dans une transaction SQLite en lecture seule : **228 gardes**, plus deux politiques. Les textes modifiés sont encore sans proposition en base au contrôle ; leurs empreintes doivent être revérifiées sous le verrou d’inscription par le parent.

Les trois dossiers ayant les journaux les plus récemment modifiés sont des relectures Travail et ne contiennent aucun de ces 24 IDs. Cette observation de métadonnées n’est pas une preuve de tous les processus actifs ni une réservation contre une attribution future : le contrôle de concurrence doit être refait à l’inscription. Les articles retenus ne figurent pas dans l’inventaire des sources graphiques bloquées.

Des incohérences ordinales préexistantes dans R613-1-2, notamment le renvoi de son V aux I à III alors qu’aucun III autonome ne figure dans la source capturée, restent signalées ; elles ne sont pas corrigées silencieusement. Les notes officielles d’entrée en vigueur, dont les modalités anciennes des revenus 2020/2021 et de la radiation 2023, restent attachées aux sources ; elles ne datent pas la réforme proposée.

Le coût du traitement administratif et l’économie nationale sont inconnus. Les certificats établissent la concordance technique des textes, citations et empreintes, sans validation juridique indépendante. Les fichiers de proposition restent soumis à la contrelecture et à l’inscription gardée du parent ; aucune mutation de base, politique ou site n’a été effectuée.
