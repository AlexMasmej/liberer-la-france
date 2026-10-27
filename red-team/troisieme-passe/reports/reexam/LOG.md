# Réexamen LOG : instantané 20261026T230545Z → 20261027T044303Z

Groupe LOG, 16 objections des dossiers P1-URBA, P1-CCH, DOM-SRU et FUT-TRAV-LOG. Revue faite par un agent IA le 2026-10-26, en lecture seule. **Elle ne vaut pas validation par un juriste.** Le détail figure dans `reports/reexam/LOG.json` : trace, citations, empreintes et fichiers de preuve.

## Synthèse

| Verdict | Nombre | Objections |
|---|---|---|
| maintenue | 6 | RT-DOMSRU-01 (P1), RT-FUTTL-02 (P1), RT-FUTTL-06 (P1), RT-FUTTL-09 (P1), RT-DOMSRU-05 (P2, à confirmer), RT-FUTTL-19 (P2) |
| reformulée | 3 | RT-P1-URBA-07 (P1, à confirmer), RT-P1-CCH-12 (P2), RT-P1-URBA-02 (P2) |
| résolue | 7 | RT-P1-CCH-02 (P1), RT-P1-URBA-01 (P1), RT-FUTTL-18, RT-P1-URBA-06, RT-P1-URBA-08, RT-P1-URBA-09, RT-P1-URBA-10 (P2) |
| obsolète | 0 | — |

Aucune priorité n'a changé parmi les objections qui subsistent. Deux P1 sont résolues : RT-P1-CCH-02 et RT-P1-URBA-01. Il reste donc 5 P1 sur les 7 du paquet.

### Ce que la seconde passe a corrigé (code de l'urbanisme, coordinations réglementaires)

- **Agrément de bureaux en Île-de-France (RT-P1-URBA-01, -02)** : tout le chapitre R*510 est abrogé à la date d'abrogation de L510-1. R*510-8 interdit désormais que l'absence d'agrément bloque le permis, les fonds publics ou l'affectation des bâtiments. R431-16 g est abrogé à terme. R*510-14 contient la clause de non-rétablissement. Seul **L111-12** maintient encore « les obligations et sanctions fondées sur [...] L. 510-1 », sans réserve de la loi répressive plus douce. RT-P1-URBA-02 est reformulée sur ce seul point.
- **Division de logements (RT-P1-CCH-02)** : R425-15-2 ne laisse plus vivre l'autorisation de L126-19 ni l'accord de l'EPCI, et R423-70-1 est abrogé en même temps.
- **Délais de consultation des commissions nationales (RT-P1-URBA-06)** : R*423-27 reprend la correction proposée. Les trois textes décrivent maintenant le même état : un mois pour les saisines nouvelles, trois mois pour les anciennes, quatre mois d'instruction.
- **Plan intérieur (RT-P1-URBA-08)**, **consultation financière dans le certificat d'urbanisme (RT-P1-URBA-09)**, **Cerfa 14600 et taxe bureaux en Île-de-France (RT-P1-URBA-10)** : chaque renvoi est borné ou retiré, avec une transition sans formalité de remplacement, et les faveurs anciennes sont conservées.
- **PTZ, II bis de D31-10-9 (RT-FUTTL-18)** : les notes assument désormais l'extinction au 31 décembre 2027 (« sans [...] prolonger l'avantage temporaire »). L'alerte est résolue sur le plan documentaire.

### Ce qui subsiste

- **SRU, fait générateur (RT-DOMSRU-01, P1)** : R302-17, R302-18 et R302-19 ont seulement été datés. Aucune règle ne dit encore quand naît le prélèvement annuel ou la majoration de l'année de bascule.
- **Fausses abrogations ABROGE_DIFF (RT-FUTTL-02, P1)** : L3422-5 dit toujours « Le présent article est abrogé à compter du 1er janvier 2028 », et ses nouvelles notes renforcent cette lecture. 1382-0 garde « Le présent V n'a pas pour effet de prolonger la période légale d'application ». Ses notes ont été corrigées, ce qui ne résout pas un défaut du texte.
- **ESUS (RT-FUTTL-06, P1)**, **Mayotte (RT-FUTTL-09, P1)**, **anomalie d'inventaire des versions futures (RT-FUTTL-19)** : propositions inchangées. Les nouvelles notes affirment encore l'absence de versions successeurs pourtant présentes : L3332-17-1 2027, 1382-0 2027, L3422-5 2028.
- **Seuils de 50 % de logements sociaux pour la TFPB (RT-DOMSRU-05)** : le numérateur n'a toujours pas de source de données.
- **Recours des associations (RT-P1-URBA-07, P1, à confirmer)** : L600-1-1 est inchangé. R*423-6 retire désormais son renvoi. Si la correction de L600-1-1 est retenue, il faut garder pour les demandes déjà publiées l'équivalence entre publication électronique et affichage. Le texte complet est dans le JSON.
- **Toilettage CCH (RT-P1-CCH-12)** : R213-2 est corrigé ; cinq instances sur six restent ouvertes, dont quatre n'ont pas encore eu leur seconde passe.

## Nouveaux constats

- **RT-RXLOG-01 (P2, anomalie d'inventaire)** : notes de revue périmées. Douze articles d'urbanisme ont été coordonnés des deux côtés, mais chacun annonce encore une contradiction chez l'autre. Exemples : « Le corpus propose encore dans R*510-1 et R*510-2 un agrément et son instruction » ; « R425-15-2 proposé rétablit l'accord… » ; « Hors lot, retirer R. 423-52 de R*410-10 ». La correction consiste à mettre ces notes à jour.
- **RT-RXLOG-02 (P2, incohérence du projet)** : le dernier alinéa ajouté à R*423-61 interprète un renvoi de R*423-27 au « délai propre » qui n'existe plus. L'alinéa est inerte et peut être supprimé.

## Alertes P1 liées

Les 19 alertes du paquet sont toutes passées de « live » à `reference_gone`. Chacune a été relue dans le texte courant et classée **alerte écartée** : le renvoi est soit neutralisant (« aucun accord ne peut être exigé sur le fondement de… »), soit transitoire (« jusqu'à l'entrée en vigueur de… », « pour les seuls faits générateurs… »), soit couvert par une clause générale (R*431-36). Une alerte hors paquet a aussi été écartée : 1382-0 → 1530, encore classée `live` par le triage mécanique alors que le IV proposé borne ce renvoi.

## Couverture réelle

- Lues **en entier**, ancienne et nouvelle version (proposition, motif, notes) : les 34 versions modifiées du paquet (37 lignes de changement). Lus aussi en entier, dans le texte courant : les propositions de L302-5, L302-7, L510-1, L600-1-1, L126-18, L126-19, L213-2 et L111-12, les articles R*510-4, -6, -7, -9, -10, -11 et -15, et les versions futures de L3422-5, L3332-17-1, 1382-0 et D31-10-9.
- **Contrôlés par empreintes** (inchangés entre les deux manifestes, non relus) : environ 60 autres versions des objections. Ce sont surtout les articles de RT-FUTTL-02 et RT-FUTTL-09, les instances fusionnées RT-FUTFISC-24 et -25, et les cinq instances restantes de RT-P1-CCH-12.
- **Non examinés** : textes extérieurs aux neuf recueils (CGCT L2332-2, ordonnances 2002-411 et 2026-647, loi 2026-403, article 90 de la LF 2025, décret de catégories ESUS), formulaires Cerfa, autres lots. Aucune consultation web.
- La seconde passe est arrêtée (statut `blocked`). Plusieurs articles visés (R*442-3-3, R481-11, R362-2, R441-12, 1840 P, D2135-7/8, D1142-x) sont encore `pending` et peuvent changer. Ces conclusions restent provisoires.
