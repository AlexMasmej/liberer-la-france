# B04tbo — variante du groupe B04 (palier A, groupe T041)

Lecture systématique du palier A, paquet T041. L'article CGI 289 bis (version courante LEGIARTI000053546660) appartient au groupe B04. Sa version suivante publiée, LEGIARTI000053576899, n'appartient à aucun groupe.

## TA-T041-01 (avec RT-FUTFISC-11) : 289 bis, version du 1er juillet 2030 — **appliquée**

- **Article touché** : CGI 289 bis, LEGIARTI000053576899 (VIGUEUR_DIFF au 1er juillet 2030, loi n° 2026-103, art. 123, V, D, 1). Mode `new`, car cette version n'avait pas de brouillon.
- **Défaut** : sans proposition, cette version rétablissait au 1er juillet 2030 deux obligations que la proposition de la version courante rend facultatives :
  - l'émission électronique obligatoire selon des normes fixées par arrêté ;
  - le recours obligatoire à une plateforme agréée.

  C'est un défaut de famille F4.
- **Ce qui change** :
  - la proposition de la version courante est reprise mot pour mot ;
  - le V est celui de la source publiée pour 2030, qui ne vise plus le 1° du I de 262 ter ;
  - une phrase réserve les factures dont la forme électronique est imposée par le droit de l'Union européenne.
- **Pourquoi c'est aligné** : la correction rend effective une réforme déjà décidée et empêche qu'une version future la rétablisse. Elle ne crée aucune formalité, condition ni sanction. La réserve européenne joue seulement si le droit de l'Union impose déjà la forme électronique : elle est sûre quel que soit le point laissé « à confirmer » dans RT-FUTFISC-11.
- **Champs du lot** : `normative_reduction`, `removed_provisions`, `benefit_review`, `substantive_impact`. Les passages cités sont exacts dans la source de 2030 et dans la nouvelle proposition.
- **Contrôle** : `python3 -B apply/check_changes.py B04tbo` donne `problems: []`. Le seul diagnostic est `explicit_normative_reduction`, qui est voulu.
- **Points laissés à l'auteur** :
  - le chevauchement des données LEGI (version courante bornée au 2222-02-22, abrogation par l'ordonnance n° 2025-1247 au 1er janvier 2027 avec maintien jusqu'à reprise réglementaire, version publiée en 2030) ;
  - la reprise au CIBS (L. 215-39, L. 216-44), hors corpus (RT-INV-06, RT-P1-CGI-A-03) ;
  - le contenu exact de la directive (UE) 2025/516, non consultée.

## Résumé

Une correction (mode `new`), aucune demande, rien d'écarté. Les notes de la version courante restent périmées sur 1737 et sur 41 septies M et P (défaut m) : cette ligne n'a pas été modifiée.

Revue IA : ce n'est pas une validation par un juriste.
