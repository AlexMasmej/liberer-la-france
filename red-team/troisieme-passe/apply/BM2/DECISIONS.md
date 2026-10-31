# BM2 — corrections des défauts grossiers de l'échantillon apparié (paquet `audit/baseline/fix-packet-BM2.json`)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Revue IA, sans validation par un juriste.

Décompte : 6 corrigés (4 dans `apply/BM2`, 1 dans `apply/J06cb`, 1 dans `apply/J11cb`), 0 déjà réglé, 1 non corrigé (L323-4-1 : la correction porte sur D323-3, hors paquet, déposée sous `requests`). Les sept articles ont été relus en entier avec leurs liens principaux. Trois dossiers validés (`problems` vide) ; 8 `requests` (4 textes complets validés dans un essai, 4 substitutions exactes) ; 4 `skipped`.

## Corrections appliquées

1. **travail L1255-10** (LEGIARTI000030435071, défaut introduit) : appliquée (`apply/BM2`).
   - Défaut : le 1° proposé punissait le recours au salarié « après l'expiration du délai » sans contrat écrit, puis déclarait que « la conclusion tardive de ce contrat ne constitue pas, à elle seule, un manquement ». Toute conclusion tardive suppose un recours sans contrat après le délai : l'élément matériel incriminé était celui que la seconde phrase excluait, et le moment de consommation était indéterminable. Asymétrie avec le 4° de L1255-2 proposé.
   - Correction : le 1° est rédigé comme le 4° de L1255-2 proposé : « Il recourt au salarié sans qu'ait été conclu avec un entrepreneur de travail temporaire le contrat écrit de mise à disposition prévu à l'article L. 1251-42 ». Le dernier alinéa (le seul dépassement du délai n'est plus puni ; suppression de l'emprisonnement en récidive pour le 1°) conserve le recul pénal décidé. Peines, délai de deux jours ouvrables et droits des salariés inchangés.

2. **cch R431-23** (LEGIARTI000006899477, hérité) : appliquée (`apply/BM2`).
   - Défaut : destinataire des renseignements « caisse nationale de prévoyance », organisme qui n'exerce plus la fonction de prêteur pour le compte de l'Etat ; discordance avec R431-19 (demandes au directeur général de la caisse des dépôts et consignations).
   - Correction : destinataire désigné par sa fonction, « l'organisme qui gère le prêt pour le compte de l'Etat » (formule de R431-20 et R431-25 : « prêt consenti pour le compte de l'Etat »), sans affirmer une succession institutionnelle que le corpus ne documente pas (la transformation de la CNP en société anonyme par la loi du 16 juillet 1992 n'est pas vérifiée sur source primaire). Notes et `scope_limitations` du bilan d'impact rectifiés. La réduction des envois périodiques est inchangée. Les mentions historiques de R431-20, R431-25, R432-5 et D431-6, qui identifient l'origine des prêts, ne sont pas touchées.

3. **travail R3232-7** (LEGIARTI000043128611, hérité, article maintenu) : appliquée (`apply/BM2`), passage en `rewrite_draft`, bilan d'impact `coordination_only`.
   - Défaut : le second alinéa organise des redressements « dans le calcul de la participation de l'Etat au versement des allocations complémentaires », alors que L3232-8 (« L'Etat rembourse à l'employeur une fraction de l'allocation complémentaire ») est au corpus à l'état ABROGE depuis le 17 juin 2013 (loi n° 2013-504 du 14 juin 2013, art. 16) et que L3232-7 met l'allocation à la charge de l'employeur. La note affirmait à tort L3232-8 « absent du corpus actif ».
   - Correction : le redressement de la participation de l'Etat est limité aux périodes au titre desquelles l'Etat remboursait une fraction de l'allocation en application de L3232-8 dans sa rédaction antérieure à son abrogation ; les redressements des charges sociales et la vérification de la répartition sur douze mois sont conservés en entier ; transition et absence de formalité de remplacement expresses. Textes de la source repris sans retouche de style.
   - Section traitée en entier par `requests` (voir ci-dessous) : R3232-3, R3232-4 et R3232-6 organisent encore la part de l'Etat pour l'avenir. R3232-8 (paiement direct par l'Etat au travailleur à domicile, remboursement par l'employeur de sa part) n'est pas modifié : son mécanisme d'avance reste cohérent ; l'auteur peut le revoir.
   - Point laissé à l'auteur : rétablir une participation de l'Etat exigerait une disposition législative ; le 1° de L3232-9 n'est qu'une habilitation de modalités, non coordonnée par le législateur de 2013.

4. **travail R6523-2** (LEGIARTI000037584023, hérité) : appliquée (`apply/BM2`).
   - Défaut : le renvoi à L6313-1 était déjà corrigé ; subsistait le seuil « 520 fois le salaire hebdomadaire minimum de croissance », unité que le code ne définit pas (le SMIC est horaire ; aucun autre article du corpus n'emploie l'expression), ce qui rend le seuil indéterminable.
   - Correction : « 520 fois le produit du montant du salaire minimum de croissance, tel qu'il est fixé en application des articles L. 3231-2 à L. 3231-12, par le nombre d'heures correspondant à la durée légale hebdomadaire du travail », formule reprise de L3232-3. Multiplicateur, territoires, salariés visés et prorata inchangés ; bilan d'impact mis à jour.
   - Laissé à l'auteur : si la pratique retenait une autre base (par exemple une durée hebdomadaire différente), la substituer ; la question de compétence (dispense réglementaire d'une contribution légale, L6131-1 et L6331-1) reste « à confirmer » et la franchise, favorable, est conservée (`skipped`).

5. **cch Annexe I à l'article D353-127** (LEGIARTI000039049086, hérité, propriétaire J06) : appliquée dans le dossier de variante `apply/J06cb`.
   - Défaut : le défaut principal officiel (indexation ICC au 1er juillet contraire à L353-9-2 et L353-9-3) était déjà réglé. La pénalité de l'article 7 restait versée « au fonds national de l'habitation », organisme que le code ne connaît plus ; L811-1 finance l'aide personnalisée au logement par le fonds national d'aide au logement.
   - Correction : bénéficiaire « fonds national d'aide au logement » ; taux (... p. 100), mise en demeure et recouvrement inchangés. Scories coordonnées au passage, sans effet normatif : loyer maximum « ... euros le mètre carré » (valeur en blanc), « Date de dépôt de la déclaration attestant l'achèvement et la conformité des travaux prévue à l'article L. 462-1 du code de l'urbanisme » au lieu du certificat de conformité disparu, « Le ministre chargé de la construction et de l'habitation, agissant au nom de l'Etat », « Elle expire le 30 juin ..... » (année en blanc comme les autres dates du modèle). Notes rectifiées (la concordance n'est plus « supplémentaire »).
   - Non corrigé (hors corpus) : « inspection générale de l'équipement » (article 8), successeur absent du corpus.
   - Mêmes mentions du fonds dans les annexes III à D353-127, III à D353-32, III à D353-190 (J06) et V à D353-127 (B08) : `requests` de substitution exacte.

6. **annexe II (CGI) 206** (LEGIARTI000049904359, both, propriétaire J11) : appliquée en partie dans le dossier de variante `apply/J11cb`.
   - Défaut officiel (IV 3 : « a, b et c […] respectivement » alors que le b de CGI 298 est abrogé depuis 2022) : déjà réglé par la proposition, qui remplace le IV 3.
   - Défaut du projet : CGI 298 (LEGIARTI000044873424) est ABROGE_DIFF au 1er janvier 2027 (ordonnance n° 2025-1247 ; seul le 2 est maintenu). Les renvois du IV 3 et du VII au « 1° du 4 de l'article 298 » deviennent morts ; le IV 1 vise encore « aux 2 à 4 » alors que le 4 est abrogé.
   - Correction : IV 3 et 1° bis visés « dans sa rédaction en vigueur au 31 décembre 2026, ou dans les dispositions du code des impositions sur les biens et services qui s'y substituent à compter du 1er janvier 2027 » (aucun numéro du CIBS, hors corpus) ; VII renvoie « aux produits mentionnés au 3 du IV » ; IV 1 : « aux 2 et 3 ». `proposed_quote` et `scope_limitations` du bilan d'impact mis à jour ; le certificat sera recalculé par le coordinateur.
   - Non appliqué (`skipped`, hors corpus) : un règlement ne peut écarter des exclusions législatives recodifiées ; la suppression des exclusions de déduction sur carburants et lubrifiants doit être portée dans le CIBS par la loi de réforme (clause non codifiée de RT-FUTFISC-07). À défaut, le IV 3 reste sans effet sur ce point.

## Non corrigé dans le paquet, correction déposée sous `requests`

7. **css L323-4-1** (LEGIARTI000053283672, both) : l'article de loi n'appelle pas de modification (il supprime la durée minimale ; ses notes signalent la coordination ouverte). Le défaut est dans D323-3 (LEGIARTI000006736472, hors paquet, sans propriétaire), qui conserve « de plus de trois mois » et subordonne la communication du médecin du travail à l'examen de préreprise que R4624-29 (maintenu) réserve aux arrêts de plus de trente jours. Request avec texte complet, motif, notes et bilan d'impact (validés dans un essai) : « Au cours de toute interruption de travail, sans durée minimale préalable », examen de préreprise « le cas échéant […] lorsque l'assuré peut en bénéficier », transition ajoutée. R4624-29 n'est pas étendu : extension de faveur non décidée (`skipped`, arbitrage).

## `requests` (articles hors paquet, textes exacts)

| Article | Propriétaire | Demande |
|---|---|---|
| css D323-3 (LEGIARTI000006736472) | aucun | Texte complet validé : seuil retiré, préreprise « le cas échéant », transition ; bilan d'impact joint. |
| travail R3232-3 (LEGIARTI000018533840) | aucun | Texte complet validé : taux de 50 % limité aux périodes couvertes par L3232-8 avant son abrogation ; aucun remboursement pour l'avenir sur ce fondement ; notes rectifiées (L3232-8 au corpus, ABROGE) ; bilan d'impact joint. |
| travail R3232-4 (LEGIARTI000043128618) | aucun | Texte complet validé : « Pour les périodes mentionnées à l'article R. 3232-3, l'aide de l'Etat est versée… » ; dispense de visa et délai inchangés. |
| travail R3232-6 (LEGIARTI000022357066) | aucun | Texte complet validé : paiement direct de la part de l'Etat « au titre des périodes mentionnées à l'article R. 3232-3 ». |
| cch Annexe III à D353-127, III à D353-32, III à D353-190 | J06 | Remplacer chaque « fonds national de l'habitation » par « fonds national d'aide au logement » ; note de troisième passe. |
| cch Annexe V à D353-127 | B08 | Idem. |

## `skipped`

- **a2 206** : reprise législative dans le CIBS (hors corpus).
- **R6523-2** : compétence réglementaire pour la dispense (à confirmer).
- **Annexe I à D353-127** : « inspection générale de l'équipement » (hors corpus).
- **L323-4-1 / R4624-29** : extension de la visite de préreprise sous trente jours (arbitrage).

## Résumé

6 corrigés, 1 non corrigé (request sur D323-3), 0 déjà réglé. Dossiers : `apply/BM2` (4 changements, 8 requests, 4 skipped), `apply/J06cb` (1), `apply/J11cb` (1), tous validés sans problème. Points pour l'auteur : participation de l'Etat à l'allocation complémentaire (base légale abrogée en 2013 ; rétablissement = loi), reprise CIBS de la suppression des exclusions de déduction sur carburants, base de calcul du seuil de R6523-2. Revue IA : rien de ceci ne vaut validation par un juriste.
