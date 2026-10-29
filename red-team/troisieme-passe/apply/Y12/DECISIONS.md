# Y12 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-Y12.json`, soit 45 articles du CCH et 59 pistes (49 S9, 10 S10). Pour chaque piste S9, j'ai lu la ligne `removed_provisions` de la loi visée et sa proposition, puis vérifié si le décret ou l'annexe organise encore la formalité retirée. Pour les grandes annexes (conventions types de R373-3, R353-159, D353-90 et D353-59), la vérification a été faite par recherche ciblée des formalités retirées dans le texte entier, et non par une lecture ligne à ligne.

Contrôle : `python3 -B apply/check_changes.py Y12` donne 0 ligne construite et `problems` vide.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9 | S10 | Total |
|---|---|---|---|
| G | 0 | 0 | 0 |
| m (sur la piste) | 0 | 0 | 0 |
| déjà réglé | 25 | 0 | 25 |
| faux positif | 24 | 10 | 34 |

Corrections : aucune. Aucune demande à un autre groupe, rien d'écarté (`skipped` vide). Les défauts `m` connexes ci-dessous ne sont pas corrigés : le brief n'autorise à corriger un `m` que sur un article déjà modifié.

## Constats connexes `m`, non corrigés

- **R863-4** (LEGIARTI000047985799), F7 : l'alinéa transitoire (« Pour les aides dues au titre des mois commençant à compter de l'entrée en vigueur de la loi mentionnée au 8° … ») suit le 9°. La citation du 9° n'est pas fermée dans la source, donc l'alinéa peut se lire comme une partie de R. 822-24 adapté. Le sens se retrouve, sans effet de fond.
- **R122-25** (LEGIARTI000048562951) et **R122-28** (LEGIARTI000048562945), F10 : leurs notes disent que R125-16-1 et R125-22 à R125-26 « restent à coordonner ». Ils le sont déjà en production (R125-22, R125-23, R125-25, R125-27 à R125-31 abrogés ; R125-16-1, R125-24 et R125-26 alignés).
- **L126-20** (LEGIARTI000049398228), F10 : la note « L183-14 doit être coordonné hors lot » est périmée. L183-14 proposé (LEGIARTI000041570625) exclut déjà toute amende pour le seul défaut de l'autorisation de L126-19.
- **L631-12** (LEGIARTI000038834038), F10, hors paquet : sa note dit que les troisième et quatrième alinéas de D331-6 « conservent les autorisations de L441-2 ». D331-6 proposé les a supprimées.

## Points laissés à l'auteur

- **L371-4 3° a** (LEGIARTI000052093580) lit, dans le premier alinéa de L313-1, un passage que la proposition de L313-1 ne contient plus. J'ai qualifié la piste de faux positif : l'adaptation ne vaut que « Jusqu'à l'entrée en vigueur à Mayotte de l'article 231 », et CGI 231, 5 (LEGIARTI000054370158) prévoit déjà un taux de 2,55 % pour Mayotte. Elle est donc échue, comme le dit le dernier alinéa de L371-4. Ce texte échu pourrait être abrogé par souci de clarté, mais c'est un choix de rédaction, pas une correction nécessaire.
- **D323-5, D323-9, R353-157-1, D353-16-1** renvoient au d du 6° du I de CGI 278 sexies A. Cet article est `ABROGE_DIFF` au 1er janvier 2027 (LEGIARTI000049641491), comme 278 sexies (LEGIARTI000053545600), et le texte qui les remplace n'est pas au corpus. Leurs notes signalent déjà une « reprise fiscale au 1er janvier 2027 hors corpus à coordonner ». C'est une réserve documentaire hors pistes S9/S10, non traitée ici.
- **Annexe 1 au III de R353-159** (LEGIARTI000053561433) : le gestionnaire y est désigné « Organisme agréé gestionnaire du logement-foyer », alors que R353-159 I 1° n'exige l'agrément que pour les résidences sociales. C'est une rédaction de la source, sans lien avec les pistes (L301-5-1, L301-5-2). Je ne l'ai pas qualifiée.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| Annexe II à l'article R. 373-3 (LEGIARTI000047400423) | S9/F1+F5 | L301-5-2 | faux positif | non |
| Annexe II à l'article R. 373-3 (LEGIARTI000047400423) | S9/F1+F5 | L365-4 | faux positif | non |
| D331-6 (LEGIARTI000047601935) | S9/F1+F5 | L441-2 | déjà réglé | non |
| D331-6 (LEGIARTI000047601935) | S9/F1+F5 | L631-12 | déjà réglé | non |
| R863-4 (LEGIARTI000047985799) | S9/F1+F5 | L822-5 | déjà réglé | non |
| R125-16-1 (LEGIARTI000048521237) | S9/F1+F5 | L122-12 | déjà réglé | non |
| R125-24 (LEGIARTI000048521633) | S9/F1+F5 | L122-12 | déjà réglé | non |
| R125-26 (LEGIARTI000048521655) | S9/F1+F5 | L122-12 | déjà réglé | non |
| R122-32 (LEGIARTI000048562930) | S9/F1+F5 | L122-12 | faux positif | non |
| R122-30 (LEGIARTI000048562939) | S9/F1+F5 | L122-12 | faux positif | non |
| R122-28 (LEGIARTI000048562945) | S9/F1+F5 | L122-12 | déjà réglé | non |
| R122-25 (LEGIARTI000048562951) | S9/F1+F5 | L122-12 | déjà réglé | non |
| R321-12 (LEGIARTI000048685289) | S9/F1+F5 | L365-2 | faux positif | non |
| R321-12 (LEGIARTI000048685289) | S9/F1+F5 | L615-1 | faux positif | non |
| R321-12 (LEGIARTI000048685289) | S9/F1+F5 | L741-1 | faux positif | non |
| L313-19-1 (LEGIARTI000048840482) | S10/F5 | L313-20-1 | faux positif | non |
| D323-17 (LEGIARTI000048897252) | S9/F1+F5 | L441-2 | déjà réglé | non |
| D323-13 (LEGIARTI000048897272) | S9/F1+F5 | L365-2 | faux positif | non |
| R452-14 (LEGIARTI000049158573) | S9/F1+F5 | L452-2-1 | déjà réglé | non |
| R452-12 (LEGIARTI000049158591) | S9/F1+F5 | L452-1 | déjà réglé | non |
| R452-12 (LEGIARTI000049158591) | S9/F1+F5 | L452-3 | déjà réglé | non |
| R452-5 (LEGIARTI000049158610) | S9/F1+F5 | L452-2 | déjà réglé | non |
| R421-1 (LEGIARTI000049243543) | S9/F1+F5 | L421-7 | déjà réglé | non |
| L731-1 (LEGIARTI000049398074) | S10/F5 | L731-4 | faux positif | non |
| L126-20 (LEGIARTI000049398228) | S10/F5 | L126-19 | faux positif | non |
| L126-20 (LEGIARTI000049398228) | S10/F5 | L126-18 | faux positif | non |
| L615-6 (LEGIARTI000049398607) | S10/F5 | L615-10 | faux positif | non |
| L615-6 (LEGIARTI000049398607) | S10/F5 | L615-7 | faux positif | non |
| D323-9 (LEGIARTI000049977460) | S9/F1+F5 | 278 sexies A | déjà réglé | non |
| D323-5 (LEGIARTI000049977468) | S9/F1+F5 | 278 sexies A | déjà réglé | non |
| D323-5 (LEGIARTI000049977468) | S9/F1+F5 | L441-2 | déjà réglé | non |
| D323-1 (LEGIARTI000049977491) | S9/F1+F5 | L365-2 | faux positif | non |
| R635-5 (LEGIARTI000050432448) | S9/F1+F5 | L635-1 | déjà réglé | non |
| R353-157-1 (LEGIARTI000051279686) | S9/F1+F5 | 278 sexies A | déjà réglé | non |
| D353-16-1 (LEGIARTI000051281615) | S9/F1+F5 | 278 sexies A | déjà réglé | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S9/F1+F5 | L301-5-1 | faux positif | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S9/F1+F5 | L301-5-2 | faux positif | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S9/F1+F5 | 278 sexies | faux positif | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S9/F1+F5 | L631-12 | déjà réglé | non |
| D31-10-2 (LEGIARTI000051397186) | S9/F1+F5 | 278 sexies | faux positif | non |
| R452-16-2 (LEGIARTI000051927361) | S9/F1+F5 | L365-2 | faux positif | non |
| R312-7-7 (LEGIARTI000051991902) | S9/F1+F5 | L741-1 | faux positif | non |
| L421-6-1 (LEGIARTI000052042903) | S10/F5 | L443-13 | faux positif | non |
| L371-4 (LEGIARTI000052093580) | S10/F5 | L313-1 | faux positif | non |
| R122-11 (LEGIARTI000052644802) | S9/F1+F5 | L122-3 | déjà réglé | non |
| R122-7 (LEGIARTI000052644812) | S9/F1+F5 | L122-3 | déjà réglé | non |
| R141-11 (LEGIARTI000052644863) | S9/F1+F5 | L112-9 | faux positif | non |
| R141-11 (LEGIARTI000052644863) | S9/F1+F5 | L112-10 | faux positif | non |
| Annexe II à l'article D353-90 (LEGIARTI000053356309) | S9/F1+F5 | L631-12 | faux positif | non |
| Annexe I à l'article D353-59 (LEGIARTI000053537850) | S9/F1+F5 | L481-2 | déjà réglé | non |
| L422-2 (LEGIARTI000053546225) | S10/F5 | L313-34 | faux positif | non |
| L421-1 (LEGIARTI000053546314) | S10/F5 | L302-5 | faux positif | non |
| Annexe 2 au III art R353-159 (LEGIARTI000053561389) | S9/F1+F5 | L301-5-2 | faux positif | non |
| Annexe 2 au III art R353-159 (LEGIARTI000053561389) | S9/F1+F5 | L365-4 | faux positif | non |
| Annexe 1 au III art R353-159 (LEGIARTI000053561433) | S9/F1+F5 | L301-5-1 | faux positif | non |
| Annexe 1 au III art R353-159 (LEGIARTI000053561433) | S9/F1+F5 | L301-5-2 | faux positif | non |
| R353-159 (LEGIARTI000053561436) | S9/F1+F5 | L365-4 | faux positif | non |
| Annexe à l'article R366-1 (LEGIARTI000053744828) | S9/F1+F5 | L366-1 | déjà réglé | non |
| R302-14 (LEGIARTI000054551251) | S9/F1+F5 | L441-2-1 | faux positif | non |
