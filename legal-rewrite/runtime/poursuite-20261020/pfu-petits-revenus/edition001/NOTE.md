# Proposition de plafond du PFU pour les petits revenus

Ce dossier propose un article 200 A complet, sans inscription dans la base ni modification d’une politique active. Le C ajouté au 1 institue une réduction effective de la charge fiscale française. Tout le corps antérieur est conservé exactement : suppression du coefficient 1,25, option globale au barème rectifiable, régimes historiques et transitions compris. Les treize sources, leurs notes et les propositions antérieures ont été lues intégralement ; les six articles du circuit sont dans `source-all.json`, les sept cibles dans `references.json`.

Le taux de 20 %, le seuil de ressources et le lissage sont le calibrage de ce projet. [La proposition officielle de David Lisnard, publiée le 16 avril 2026](https://www.unenouvelleenergie.fr/changer-de-logiciel-fiscal/), soutient un PFU allégé et stable ; elle ne donne ni ce taux pour les petits revenus ni ce seuil. Son taux de 20 % concerne l’impôt sur les sociétés : il ne prouve pas un PFU à 20 %. Aucune promesse de rendement ou d’autofinancement n’est reprise.

## Calcul précis

Pour chaque groupe homogène de revenus soumis au 200 A, 1 B :

- B : fraction positive réellement imposable, après exonérations, abattements et pertes légalement imputables. Une vente n’est pas un gain ; un remboursement de capital n’est pas un produit imposable. Un PEA exonéré et une fraction d’assurance-vie abattue ne sont jamais réintroduits dans B.
- T : CSG, CRDS et prélèvement de solidarité effectivement dus sur cette même fraction. Les prélèvements antérieurement acquittés sur les mêmes produits d’assurance-vie sont décomptés une seule fois, nets des restitutions. La fraction sociale portant sur les produits exonérés d’IR reste hors calcul du crédit.
- J : IR français forfaitaire après crédits et réductions affectables à ces revenus, notamment les crédits conventionnels étrangers, dans leurs limites. L’impôt étranger n’est jamais une charge remboursable par ce crédit.
- U : IR total du foyer après avantages affectables, avant avantages généraux ; F : montant positif après ces derniers avantages. Tous deux sont calculés avant le nouveau crédit et avant les acomptes. I = J × min(1, F/U), ou zéro si U est nul. Cette répartition des avantages généraux empêche de créditer une charge française déjà éteinte.
- G = min(I, max(0, I + T − 0,20 B)), avec G = 0 si B = 0.

Le calcul par groupes évite qu’un placement déjà taxé à moins de 20 % fournisse artificiellement une base inutilisée qui diminuerait la baisse accordée à un autre placement. Les régimes favorables ne sont donc pas sacrifiés au plafonnement. Le bornage par I empêche de rembourser des impôts étrangers, des prélèvements sociaux ou l’impôt d’autres revenus. Pour les régimes ordinaires visés, la charge sociale seule est inférieure à 20 % : le bornage ne fait pas obstacle au plafond. Ce dossier ne crée pas un taux social supérieur à 20 % pour simuler un crédit. Les régimes autonomes hors 200 A, notamment les prélèvements libératoires spéciaux, ne sont pas étendus à ce nouveau dispositif.

R est le RFR correspondant aux revenus de l’année N, calculé selon les composantes du IV de 1417 pour cette même année, avant le crédit. Le renvoi ne reprend pas l’année précédente utilisée dans le contexte de taxe foncière du 1417. Les revenus mobiliers et les réintégrations légales restent dans R ; le crédit ne diminue pas les revenus déclarés. Les parts sont celles de N. S = parts de N × limite supérieure de la tranche à 11 % du 197 applicable à N. Le montant de 29 579 € par part n’est qu’une illustration du barème actuellement capturé, jamais un seuil légal figé dans le nouveau texte.

Crédit du foyer C = max(0, ΣG − 0,50 × max(0, R − S)). Il est imputé après les avantages existants et avant les avances. Son montant ne dépasse pas l’IR français restant. Le remboursement éventuel provient ensuite de l’excédent des avances déjà payées, une seule fois : ce dispositif ne crée pas un crédit remboursable au-delà de l’impôt français effectivement dû. Le parent a approuvé cette architecture de crédit IR ; si un crédit remboursable au-delà de cet impôt était voulu, il faudrait une autre décision et une autre rédaction.

## Taux et assiettes préservés

En 2026, lorsque les assiettes coïncident, le PFU ordinaire est 12,8 % d’IR + 10,6 % de CSG + 0,5 % de CRDS + 7,5 % de solidarité = 31,4 %. Le taux de CSG de 9,2 % subsiste pour les exceptions du IV de L136-8, dont les produits d’assurance-vie : la charge sociale correspondante est 17,2 %. Les exonérations d’affiliation européenne, bases particulières, seuils de recouvrement et restitutions sont pris selon leurs règles effectives ; 31,4 % n’est pas appliqué aveuglément à toute épargne.

La source DILA entière de L136-8 et celle du 235 ter sont conservées. Pour la CRDS, le taux de 0,5 % a été corroboré par le résultat primaire de l’article 19 de l’ordonnance 96-50, [LEGIARTI000041466982](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000041466982/2026-05-23) ; l’ouverture du corps intégral distant a renvoyé 403 et aucun document entier n’a été récupéré. Cette réserve documentaire reste explicite. Le taux n’est pas recréé dans le texte proposé, qui vise la contribution effectivement due.

Les dividendes au forfait n’obtiennent pas l’abattement de 40 % réservé au barème. L’option du 2 reste globale, annuelle et rectifiable : il faut comparer la charge de l’ensemble du foyer selon les règles propres de chaque régime, avec la déductibilité de CSG éventuelle. Un foyer non imposable au barème peut ainsi conserver une charge sociale de 18,6 %, inférieure à 20 %. Le crédit n’est pas cumulé avec cette option et aucun choix par banque ou revenu n’est introduit.

Les produits d’assurance-vie gardent le taux de 7,5 % et l’abattement de 4 600 € ou 9 200 € lorsqu’ils y sont éligibles. Exemple célibataire : 5 000 € de produits, 4 600 € abattus, B = 400 €, IR = 30 €, prélèvements sociaux sur les produits = 860 €. Seuls 68,80 € de prélèvements sociaux sont attribués à B ; le crédit vaut 18,80 €. Les 791,20 € de prélèvements sur la fraction exonérée restent dus et n’ouvrent pas un nouveau crédit. Les anciens prélèvements libératoires restent à leur régime autonome.

Les crédits étrangers ne sont pas remboursés deux fois. Exemple : B = 10 000 €, IR brut = 1 280 €, crédit conventionnel de 1 000 € réellement imputable, charge sociale = 1 860 €. I = 280 €, crédit nouveau = 140 €, IR final = 140 €. Si 1 280 € d’avance ont été payés, la restitution est 1 140 € au total, comprenant 1 000 € de crédit conventionnel et 140 € de crédit nouveau. Un crédit conventionnel éteignant déjà tout l’IR laisse un nouveau crédit nul.

## Lissage et limites

Un seuil sec serait mauvais : sur B = 10 000 €, la perte brutale du crédit de 1 140 € pour un euro supplémentaire de RFR produirait une hausse de 1 140 €. Une extinction au rythme de 1 € de crédit par euro de ressources ferait encore monter la charge de 1,20 € pour un euro supplémentaire de capital pendant la sortie du dispositif. Ces contre-exemples justifient le coefficient proposé de 0,50, qui est un choix technique du projet.

À bases et autres règles constantes, la perte de crédit est de 0,50 € au maximum par euro supplémentaire de RFR. Pour un euro supplémentaire de revenu mobilier ordinaire entrant également pour un euro dans le RFR, la charge de ce revenu augmente de 0,70 € dans la phase de retrait, puis de 0,314 € après extinction ; il n’y a aucun saut au seuil ni à la fin du lissage. Les tests parcourent plusieurs milliers de valeurs et vérifient les raccordements sans arrondi intermédiaire. Le crédit peut s’éteindre avant la fin de l’année si le RFR final dépasse suffisamment S : ce n’est pas un prélèvement mensuel garanti à 20 %.

Ces bornes ne constituent pas une garantie universelle de taux marginal du foyer inférieur à 100 % après tous impôts, aides, changements de parts, régimes dérogatoires ou variations de bases. Un euro de RFR n’est pas dans tous les régimes un euro de ressource brute ; les autres seuils et prestations n’ont pas été simulés. Le texte supprime l’effet de seuil propre au nouveau crédit. Aucun simulateur complet de liquidation fiscale, modèle comportemental ou chiffrage national n’est revendiqué.

## Coordinations et coûts

117 quater, 125 A et 125 D renvoient déjà au 1 ou au 2 du 200 A. L’insertion dans le 1 est donc opérante sans modifier leur collecte. Les avances de 12,8 % ou 7,5 %, les dispenses fondées sur les revenus de N−2 et les délais demeurent. La charge finale est régularisée à la déclaration annuelle ; aucun débit immédiat de 20 % n’est annoncé. 154 quinquies reste inchangé car aucune CSG n’est remboursée. L136-8 ne change pas de taux.

Le dispositif est classé `mixed` : il réduit l’IR mais ajoute un calcul par groupes, une attribution de crédits et un lissage. Aucun formulaire autonome ni inscription nouvelle n’est créé ; cela ne prouve pas que tous les échanges d’information déjà disponibles suffisent à une liquidation automatisée dans chaque cas, notamment pour les prélèvements d’assurance-vie antérieurs. Ce point doit être vérifié opérationnellement, sans inventer une déclaration supplémentaire.

Le coût budgétaire est inconnu. Les recettes sociales restent au droit applicable ; la baisse porte sur l’IR. Le nombre d’articles rédigés n’est ni une économie ni un score de simplification. Aucune compensation automatique des ressources locales supprimées dans un autre volet, notamment la CFE, n’est imputée à cette mesure. Les deux effets déclarés partagent un unique identifiant de mesure ; ils ne représentent pas deux baisses d’impôt.
