# Lot fiscal C — textes et bilan bornés

Les 48 sources assignées sont des entrées de l’inventaire canonique `impots.json`, encore sans proposition au contrôle final en lecture seule. Elles ont été lues intégralement avec leurs notes. Le lot contient **29 propositions entières et 19 maintiens explicites sans nouveau corps**. Une coordination distincte de **881 L**, déjà proposé, est fournie avec son avant-image entière dans `csi-coordination/`. Aucun maintien n’est compté comme réécriture ou comme baisse nouvelle.

## Trois familles de mesures, avec sous-champs explicites

1. **Contribution de sécurité immobilière : suppression entière prospective.** Le 879 est le support matériel ; ses tarifs, minima, avances, quittances et refus de dépôt exclusivement fiscaux sont coordonnés dans le même identifiant `contribution-securite-immobiliere-suppression`. Les publications à 0,10 %, inscriptions/subrogations à 0,05 %, radiations et tarifs fixes de renseignements/copies/relevés disparaissent pour les nouvelles demandes ; il ne s’agit pas de dix-sept taxes différentes. Le champ déjà exonéré dans la proposition antérieure de l’annexe III 253 est inclus dans cette abolition générale, sans double perte de recette comptée.

2. **Droits fixes ciblés : retrait des seuls prélèvements des 679, 680, 686, 687, 691 bis, 846 bis, 1020 et 1051 ; coordination 1048 ter.** La famille commune est dédupliquée sous `droits-fixes-actes-cibles-suppression` et les sous-champs restent détaillés article par article. Les montants retirés sont de 125 € ou 25 € selon l’article. Ce n’est pas l’abolition de tous les droits fixes du CGI. Le 686 garde ses conditions de faculté réservée et de déclaration publique notifiée sous vingt-quatre heures ; le régime distinct d’une déclaration hors conditions subsiste. Le 691 bis conserve les conditions et prolongations favorables du 1594-0 G. L’exception de l’usucapion du 846 bis ne change pas. Dans 1051, les catégories sociales et les dates historiques restent entières ; les opérations relevant encore du 4° transitoire bénéficient aussi du retrait du seul fixe pour leurs nouveaux faits générateurs, sans perdre les autres avantages. La seule suppression du fixe ne peut entraîner une taxation proportionnelle de substitution.

3. **Minimum général de perception de 25 € du 674 : retrait du seul relèvement au plancher.** Identifiant `enregistrement-minimum-perception-suppression`. Les taux et assiettes proportionnels/progressifs et l’arrondi du 675 restent. Le gain n’est pas automatiquement 25 € par acte : il dépend du montant effectivement calculé avant plancher. Aucune estimation nationale n’est faite.

Le 1020 conserve son taux proportionnel autonome de **0,70 %** dans son champ. Les actes auparavant au seul fixe, notamment 1039, ne basculent pas dans ce taux. La référence à 1053 est retirée de sa liste parce que l’actuelle proposition de 1053 exonère déjà ces opérations ; cette coordination n’est pas une nouvelle baisse de 0,70 %. Les successions futures déjà exonérées ne deviennent pas imposables par ce renvoi.

## Dates et droits conservés

Pour la CSI, la date déterminante est la présentation de la réquisition ou de la demande : une nouvelle radiation d’une ancienne inscription, ou une demande nouvelle de copie d’un ancien acte, n’est pas taxée. Les anciennes demandes gardent leurs règles de liquidation et leurs exonérations, réductions, remboursements, prescriptions et recours. Aucun remboursement général de contributions antérieurement dues ; aucune imputation ou restitution deux fois d’un même paiement. La somme perçue sans fondement après suppression reste un indu, sans exiger l’annulation du contrat sous-jacent.

Pour les droits fixes et le minimum, la transition distingue les conventions/actes futurs obligatoirement déclarés ou enregistrés et les présentations volontaires futures dans les autres cas, selon la distinction déjà portée par les notes de l’article 95 IV de la loi de 2004. Les dates historiques 2006, 2013, 2018, 2021, 2022 ou 2028 ne deviennent pas des dates inventées de promulgation.

Le II de 881, relatif aux états exécutoires et hypothèques, demeure **exactement inchangé**. Les règles civiles de publicité, d’authenticité, de rang et d’opposabilité et les droits des tiers restent. Les DMTO/TPF, cotisations, IS à la distribution, assurance-vie/droits de succession supprimés, CVAE et CFE micro ne sont pas remplacés ou restaurés. Les rémunérations et émoluments distincts légalement dus ne sont pas confondus avec une taxe supprimée.

## Charges nettes et finances

Aucun impôt, attestation, déclaration, agrément ou garantie de remplacement n’est institué. Les informations nécessaires à une autre imposition ou à une formalité civile restent requises dans leur champ. La seule réutilisation d’actes déjà détenus n’est pas comptée comme un gain nouveau CRPA ; notamment, les justificatifs de paiement des autres droits du 1702 bis sont conservés.

La suppression de recettes ne supprime pas le travail du service de publicité foncière. Sa charge et son financement public restent à évaluer. La perte brute de recettes et le solde public consolidé ne sont pas chiffrés ; aucun montant de compensation, recette nouvelle, autofinancement ou baisse automatique d’émoluments n’est présumé.

## Lectures, contrôles et limites

Les 48 sources/notes, 34 références fiscales sources/notes/propositions éventuelles et huit dépendances directes complémentaires ont été lues en entier. Six vues nécessaires du protocole de renvois sont également fournies et lues ; les trois cibles Travail demandées pour 1043 sont matériellement inapplicables à cette exonération de transfert patrimonial public, ce qui est expliqué sans modifier les contrats privés ou les statuts publics. Le balayage des neuf exports canoniques porte sur les sources, notes et propositions : les faux positifs numériques ne sont pas présentés comme des articles entièrement relus.

Au dernier contrôle : 450 gardes d’articles en transaction SQLite `mode=ro BEGIN`, six vues du protocole, leurs sources/notes et les deux politiques concordent. `validate_answer` passe sur les 48 et la révision séparée de 881 L. Les comparaisons de conservation des subdivisions et alinéas sont jointes : 1961 conserve notamment au même rang son deuxième alinéa renvoyant au premier. Ces contrôles techniques ne constituent pas l’approbation juridique indépendante attendue du parent.

Les décrets et arrêtés hors code de publicité foncière, le LPF, le Code civil, le CPCE, le CGCT et les formulaires ne sont pas prétendus réécrits. Le fichier `unresolved-coordinations.json` distingue les textes à vérifier et les conséquences fiscales directement écartées par la loi proposée. Les deux lacunes graphiques fiscales hors lot demeurent explicites. Pas de prétention d’achèvement global du CGI ni des cinq codes.

**Aucune modification de base, de lot canonique, de module actif, de politique, de site ou de source synchronisée.** Le projet d’ajout de politique est isolé et ne s’active pas automatiquement.
