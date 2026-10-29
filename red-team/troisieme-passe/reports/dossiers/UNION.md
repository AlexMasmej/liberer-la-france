# Dossier UNION — CSS L216-3, L281-6 et modèles de statuts

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z`, corpus arrêté au 18 octobre 2026. Rapport du 26 octobre 2026.

Ce rapport est une revue par IA. Il ne vaut pas validation par un juriste. Ses conclusions sont provisoires : la seconde passe continue, et plusieurs textes en cause sont encore « pending ».

## 1. Périmètre réellement lu

Tous les articles ci-dessous ont été lus en entier par `tools/cite.py` : source, NOTA, bornes, proposition, motif et notes. Ils sont sauvegardés sous `evidence/cited/20261026T230545Z/`.

| Article | Versions lues (LEGIARTI, bornes) | Statut proposition / inventaire |
|---|---|---|
| L281-6 | 000006742237 (1985-1988), 000006742238 (1988-2004), 000006742239 (2004-) | rewrite_draft / completed (lot 00049) |
| L216-3 | 000006741708 à 000006741712 (1985-2006), 000006741713 (2006-) | rewrite_draft / completed (lot 00039) |
| L216-1 | 000006741699 à 000021941737, 000025516594 (2012-) | rewrite_draft / completed |
| L216-2 | 000006741703 à 000006741706, 000006741707 (2006-) | rewrite_draft / completed |
| L216-4 | 000006741714, 000006741715 (abrogée 1996), 000006741716 (2006-2019), 000041398754 (2019-) | rewrite_draft / completed |
| L281-1 à L281-5 | toutes versions (L281-4 : 000025516592 en vigueur ; L281-5 : 000021941698) | L281-4 abrogé ; L281-1/2/3/5 maintenus |
| L752-1 | 6 versions dont 000042684012 (ABROGE_DIFF 2020→2028) et 000054466934 (VIGUEUR_DIFF 2028-) | 2020 : rewrite_draft ; 2028 : **not_in_inventory** |
| R216-2 | 000006748639 (1985-2018), 000036914470 (2018-) | retained_unchanged / pending |
| R281-4 | 000006749025, 000006749026, 000021508312, 000036914411 (2018-) | retained_unchanged / pending |
| R213-5, R281-6, R752-1, R281-10 | versions en vigueur | retained_unchanged (R281-10 : abrogation) / pending |
| L224-5, L224-5-1, L224-5-4, L224-6, L224-10, L228-1 | toutes versions | rewrite_draft / completed |
| D224-8, D227-6, R111-1-1, R155-1, L283-1 | toutes versions | divers (voir JSON) |

Recherche dans la base, en lecture seule (`mode=ro`, `query_only`) : tous les articles en vigueur au 18 octobre 2026 qui mentionnent L. 281-4, L. 281-5, L. 281-6, L. 216-3, « statuts types », « modèle(s) de statuts », « unions ou fédérations », « union nationale au sens » ou l'approbation des statuts ; ainsi que toutes les propositions et notes qui citent ces articles. Le résultat CGI 1776 vise L. 216-3 du code de la consommation : c'est un faux positif. Les approbations de statuts d'autres régimes (L922-6, L652-1, D641-5, R731-3, R922-x) ont un champ distinct et ne sont pas traitées ici.

J'ai lu en entier les deux dossiers de preuves scellés : REPORT, CONTROL, exigences restantes, qualifications, texte entier de l'article 69 de la loi 2004-810 et de l'article 75 de la loi 2001-1246, et index du rectificatif.

## 2. Méthode

1. J'ai reconstitué l'historique des catégories de L281-6 à partir des versions LEGI de L216-2, L216-3 et L216-4. J'ai aussi utilisé les liens CITATION du XML LEGI de la version en vigueur de L281-6 : ils pointent vers les versions **de 1985** des trois articles.
2. J'ai confronté le sélecteur de l'article 69 I 54° de la loi 2004-810 aux trois versions de L281-6, au rectificatif du 27 novembre 2004 et au texte consolidé.
3. J'ai contrôlé la cohérence des propositions L216-3, L281-4, L281-6 et L752-1 avec les textes réglementaires d'exécution (R216-2, R281-4, R213-5, R752-1) et avec la version future de L752-1.
4. Le 26 octobre 2026, j'ai tenté de consulter Légifrance directement : JORFTEXT000000627150 et `loda/id/JORFTEXT000000625158`. Les deux réponses sont des HTTP 403. Rien n'a été contourné.

## 3. Le sélecteur « V » (question 2)

**Ce que prescrivait l'acte.** Le texte imprimé de l'article 69 I 54° de la loi 2004-810 (copie HAS du JO du 17 août 2004, p. 38) dit : « Au dernier alinéa du V de l'article L. 281-6, après les mots : « cas, le conseil », les mots : « d'administration » sont supprimés. »

**Ce que montre le droit consolidé.** L281-6 n'a jamais comporté de subdivision V :

- la version de 1985 (codification, décret 85-1353) a deux alinéas ;
- la version de 1988 est textuellement identique ; son lien LEGI la rattache à la loi 88-16, art. 1 ;
- la version de 2004 a aussi deux alinéas.

Supprimer « d'administration » après le seul passage « cas, le conseil d'administration » reconstitue exactement la version LEGI de 2004.

**Le rectificatif.** Le rectificatif du JORF n° 276 du 27 novembre 2004 (texte n° 5) est connu par son contenu indexé, conservé dans la preuve scellée. Il ne corrige que deux points :

- « médiateur » en « conciliateur », à l'article 58 (copie HAS, l. 1917) ;
- « des I et II » en « des II et III », à l'article 74 IV (l. 2512).

L'article 69 n'est pas concerné.

**Qualification.** Ce n'est pas une erreur de consolidation LEGI : LEGI applique l'instruction au seul passage possible. Ce n'est pas non plus une modification ultérieure : aucune version n'est postérieure à 2004. C'est une **erreur matérielle du sélecteur dans l'acte modificatif lui-même**, que la consolidation neutralise. Elle est classée comme conflit de source, sans effet normatif (RT-UNION-01).

Il reste une **réserve documentaire** de provenance : la copie HAS n'est pas un fac-similé DILA authentifié, et le rectificatif n'est connu que par l'index. Elle ne change pas la qualification. Le sélecteur ne doit pas être « corrigé » : ne pas créer de V, ne pas déplacer la modification vers un autre article.

## 4. Constats

Le JSON donne le détail de chaque constat, avec empreintes et passages.

- **RT-UNION-01 (P2, conflit de source, confirmé).** Le sélecteur « V » est une erreur de l'acte de 2004, déjà neutralisée par LEGI. Il faut seulement ajouter une note de traçabilité.

- **RT-UNION-02 (P1, incohérence du projet, confirmé). Catégories et double avis.**
  - En 1985, les trois catégories étaient disjointes parce qu'elles étaient définies par leur fondement : ancien L216-2, ancien L216-4, ancien L216-3 (fédérations mixtes maladie et famille). Le double avis CNAM + CNAF visait les fédérations mixtes.
  - Depuis 1996, L216-3 fonde toutes les unions et fédérations ; la loi 2001-1246 (art. 75 III) y a ajouté les organismes nationaux.
  - La proposition supprime l'ancrage « constituées en application de L. 216-2 / L. 216-4 » et définit les catégories par leur composition. La troisième catégorie (« fédérations mentionnées à l'article L. 216-3 ») englobe alors les deux autres : une fédération de CAF relève à la fois du simple avis et du double avis.
  - De plus, les unions de caisses d'assurance maladie créées sur L216-3 depuis 1996 entrent dans le régime des dispositions obligatoires des modèles. Le bilan du lot affirme au contraire « catégories historiques préservées » et « aucune charge nouvelle ».

- **RT-UNION-03 (P1, coordination manquante, confirmé). R216-2.** Il est maintenu sans changement et répartit encore l'approbation des statuts des unions entre le ministre et le service de R155-1. Après réécriture, le « deuxième alinéa de L. 216-3 » qu'il vise devient l'alinéa qui écarte cette approbation. C'est une formalité supprimée par la loi et maintenue par le règlement.

- **RT-UNION-04 (P1, coordination manquante, confirmé). R281-4, R213-5 et R752-1.** Les trois sont maintenus et renvoient à L281-4, que la proposition abroge. L'approbation avec opposition à trente jours subsiste pour les caisses, pour les URSSAF et pour les caisses ultramarines. Pour les URSSAF, la transition de L281-4 ne vise que les organismes « qui relevaient du présent article ». La mesure est comptée une seule fois.

- **RT-UNION-05 (P1, anomalie d'inventaire, confirmé). L752-1, version du 1er janvier 2028.** La version LEGIARTI000054466934 (ordonnance 2026-647) n'est pas inventoriée. Elle rétablit « L. 281-4 à L. 281-6 » et ferait disparaître la transition ultramarine.
  - Signalé hors périmètre : dans cette version, l'insertion d'un alinéa sur Mayotte rend inexact le renvoi à la caisse de MSA « mentionnée aux troisième et quatrième alinéas ».

- **RT-UNION-06 (P2, anomalie d'inventaire, confirmé).** Les notes de L216-2, L216-3 et L216-4 décrivent encore l'ancienne proposition de L281-6, qui conservait les renvois périmés.

- **RT-UNION-07 (P2, incohérence du projet, confirmé).** La même mesure reçoit quatre transitions divergentes (L216-3, L281-4, L281-6, L752-1). Elles diffèrent par leur point de départ, par la réserve d'illégalité, par la mention des règlements intérieurs et par le qualificatif « valablement constitués ».
  - La fin de l'approbation des délibérations de l'INF (D227-6, abrogé à la date d'un décret) relève du dossier D227-6/L224-10 et n'est pas recomptée ici.

**Alertes écartées.**

- L'UCANSS (L224-5, L224-5-1) et l'INF (L228-1) sont des unions nationales au sens de L216-3. Leurs statuts sont adoptés par leurs organes sans approbation propre. La dispense de L216-3 est cohérente avec ces articles, sous réserve de RT-UNION-03.
- L281-1 à L281-3 et L283-1 ne recréent pas l'approbation.
- L281-5, maintenu, ne concerne que les modèles.
- R111-1-1 e) reste cohérent.
- Aucune autre approbation de statuts du régime général n'a été trouvée dans le corpus.

## 5. Corrections proposées (séparées)

**C1, pour RT-UNION-01.** Le corps de L281-6 ne change pas. Ajouter à ses notes : « L'article 69 I 54° de la loi 2004-810 vise le "dernier alinéa du V" d'un article qui n'a jamais comporté de V ; la consolidation LEGI applique la suppression au seul passage "cas, le conseil d'administration". Aucun V n'est créé. »

**C2, pour RT-UNION-02.** Nouvelle rédaction des deux premiers alinéas de L281-6 proposé ; le paragraphe transitoire actuel est conservé tel quel :

> Les dispositions de l'article L. 281-5 sont applicables aux unions et fédérations de caisses d'assurance maladie constituées en application de l'article L. 216-2 dans sa rédaction en vigueur avant le 25 avril 1996, aux fédérations de caisses d'allocations familiales constituées en application de l'article L. 216-4 dans sa rédaction en vigueur avant cette date, ainsi qu'aux autres fédérations constituées en application de l'article L. 216-3.
>
> Pour ces autres fédérations, le conseil de la Caisse nationale de l'assurance maladie et le conseil d'administration de la Caisse nationale des allocations familiales sont appelés l'un et l'autre à donner leur avis.

Justification : cette rédaction restaure le sens officiel par un ancrage daté (date tirée des bornes LEGI), supprime les renvois dynamiques périmés et lève le chevauchement sans ajouter de consultation ni de charge. Il faut aussi corriger le motif et l'effet déclaré.

Deux options restent au choix de l'auteur :
- **Option B** : définir les catégories par leur composition (« qui ne regroupent que… », puis « autres fédérations »), en déclarant l'extension aux unions postérieures à 1996.
- **Option C** : supprimer l'extension des modèles aux groupements volontaires. C'est une coupe de fond, à ne pas adopter par simple souci de cohérence.

**C3, pour RT-UNION-03. R216-2 :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'approbation des statuts des unions et fédérations prévue à l'article L. 216-3. Les demandes d'approbation pendantes à cette date sont closes sans décision ni nouveau dépôt. Aucune approbation, aucun visa ni aucune déclaration ne peut être exigé sur le fondement du présent article. Les approbations antérieurement données, les actes accomplis sur leur fondement et les recours correspondants conservent leurs effets.

Dépendance : la date du décret doit coïncider avec celle de la loi.

**C4, pour RT-UNION-04.**

- **R281-4 :**

  > Le présent article est abrogé à compter de l'entrée en vigueur de l'abrogation de l'article L. 281-4. Les procédures d'approbation en cours prennent fin sans nouveau dépôt ; aucun visa, aucune homologation ni aucune déclaration préalable ne peut être exigé sur son fondement. Les actes antérieurs, les droits qu'ils ont créés et les recours correspondants sont préservés.

- **R213-5 :**

  > Les dispositions des articles L. 281-5, R. 231-1 et R. 281-6 sont applicables aux conseils d'administration des unions de recouvrement des cotisations de sécurité sociale et d'allocations familiales. Leurs statuts et règlements intérieurs ainsi que leurs modifications ne sont plus soumis à approbation à compter de l'entrée en vigueur de l'abrogation de l'article L. 281-4 ; les procédures en cours prennent fin sans nouveau dépôt.

- **R752-1 :**

  > Les dispositions des articles R. 231-1 et R. 281-6 sont applicables aux caisses générales de sécurité sociale et caisses d'allocations familiales des départements mentionnés à l'article L. 751-1.

Autre possibilité : ajouter à L281-4 proposé « y compris les organismes auxquels ses dispositions étaient rendues applicables par d'autres textes ».

**C5, pour RT-UNION-05.** Inscrire LEGIARTI000054466934 à l'inventaire et lui donner une proposition identique au texte officiel, avec deux changements :

- aux sixième et septième alinéas, remplacer « L. 281-4 à L. 281-6 » par « L. 281-5 et L. 281-6 » ;
- ajouter : « Les statuts et règlements intérieurs des caisses mentionnées au présent article, ainsi que leurs modifications, ne sont pas soumis à approbation préalable ; aucune procédure de remplacement ne peut être imposée. Les actes, droits et engagements antérieurs et les recours correspondants sont préservés. »

Vérifier séparément le renvoi « troisième et quatrième alinéas » du dernier alinéa.

**C6, pour RT-UNION-06.** Une fois C2 arrêtée, remplacer les phrases périmées des notes de L216-2, L216-3 et L216-4 par : « L281-6 proposé traite les catégories historiques des groupements ; aucune coordination supplémentaire n'est requise dans le présent article. »

**C7, pour RT-UNION-07.** Aligner les quatre transitions sur une formule unique, ou les regrouper dans une disposition finale de la loi :

> À compter de l'entrée en vigueur de la loi n° … , [objet] ne sont plus soumis à approbation préalable. Les procédures en cours prennent fin sans nouveau dépôt ; aucun visa, aucune homologation ni aucune déclaration de remplacement ne peut être exigé. Les actes antérieurs, les droits et engagements qu'ils ont valablement créés et les recours correspondants sont préservés ; la présente disposition ne régularise pas les illégalités antérieures.

**À préserver dans toutes les corrections :**
- la suppression des approbations ;
- l'absence de toute formalité de remplacement ;
- les modèles de L281-5 et leurs avis ;
- les contrôles de L281-1 à L281-3 et du service de R155-1 ;
- les autorisations sectorielles autonomes ;
- les organismes historiques, les actes, droits, engagements et recours antérieurs.

## 6. Incertitudes et éléments non examinés

**Réserves documentaires :**
- pas de fac-similé DILA authentifié de la loi 2004-810 ;
- rectificatif du 27 novembre 2004 connu seulement par son contenu indexé (consultation directe en 403 le 26 octobre 2026) ;
- actes de 1996 et de 2006 (articles 140 et 141) non lus en entier ;
- tableaux de la loi de 2001 non obtenus ;
- ordonnance 2026-647 non lue.

**Non vérifiés :**
- les arrêtés de modèles extérieurs au corpus (statuts types UGECAM, « annexe 14 ») : l'effet réel de l'extension décrite en RT-UNION-02 n'est pas mesuré ;
- le défaut d'avis de la CNAV et de l'ACOSS pour les modèles des fédérations hétérogènes et des URSSAF. Il est préexistant, et le corriger ajouterait une consultation.

**Non examinés :**
- R281-10 et L281-7 (absent du corpus) ;
- le calendrier D227-6/L224-10, qui relève d'un autre dossier ;
- les régimes non généraux.

**Caractère provisoire :** R216-2, R281-4, R213-5, R752-1, R281-6 et D227-6 sont « pending » ; la seconde passe peut encore les traiter.
