# BL3 — défauts grossiers de l'échantillon apparié : décisions

Lecture faite en production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et sqlite en `mode=ro`), le 31 octobre 2026. Contrôle : `python3 -B apply/check_changes.py BL3` → `problems: []`, 3 lignes construites et validées. Aucun dossier de variante n'a été créé : les trois articles qui ont un propriétaire antérieur (M05, Y12, W08) sont déjà corrigés, et 259 D (W14) n'est pas corrigeable dans le corpus.

## Décompte

- **Corrigés : 3.** D161-13, D756-3 et R162-8 (CSS).
- **Déjà réglés : 4.** Annexe II 371 M, annexe IV 152, CCH L371-4 et code du travail D5134-1.
- **Non corrigés : 3.** CGI 259 D (hors corpus), CSS R641-4 (arbitrage) et code du travail R3232-4 (arbitrage).
- **Demandes (`requests`) : 8.** CSS D161-6 à D161-12 et D757-14. Ces articles n'ont pas de groupe propriétaire.

## Par article

### CSS D161-13 (LEGIARTI000006735400) : appliquée (abrogation)

- **Ce qui change :** le comité national paritaire de l'information médicale était créé par l'article L. 161-30. Cet article est abrogé depuis le 28 janvier 2016 (loi n° 2016-41, art. 193, selon le lien ABROGE du corpus). D161-13 est donc abrogé. Les avis antérieurs sont conservés, L. 161-29 garde ses garanties, et rien ne remplace le comité.
- **Notes corrigées :** les notes antérieures disaient L. 161-30 « absent du corpus ». C'était faux.
- **Dépendance :** les articles D161-6 à D161-12 (composition, nominations, réunion, règlement intérieur, délibérations, frais) doivent être abrogés en même temps. Ces demandes figurent sous `requests`, avec le texte complet. Sans elles, le comité resterait organisé sans aucune mission.
- **Points pour l'auteur :**
  - D161-8 a été retouché par le décret n° 2025-906, ce qui signale que l'administration tient encore le comité pour vivant.
  - Un comité consultatif peut être créé par simple décret. Garder le comité sur une base réglementaire autonome reste un choix possible, mais il faudrait alors lui rendre une mission explicite.
  - L'article 193 de la loi n° 2016-41 n'a pas été relu au JORF.

### CSS D756-3 (LEGIARTI000034726217) : appliquée (coordination d'un article maintenu)

- **Ce qui change :** le corps source reste identique. Un dernier alinéa :
  - limite l'article aux titulaires de l'allocation aux vieux travailleurs non salariés que l'article 2 de l'ordonnance n° 2004-605 a maintenus ;
  - rattache le seuil de revenu à la dernière rédaction de D. 812-4, abrogé en 2007 ;
  - précise que les cotisations visées sont celles des périodes considérées.
- **Droits :** aucune allocation en cours n'est touchée. Aucun droit nouveau ne pouvait plus s'ouvrir depuis l'abrogation de L. 812-1, au 1er janvier 2006.
- **Notes corrigées :** les notes disaient D812-4 « absent du corpus ». C'était faux.
- **Demande :** D757-14 contient le même renvoi mort à D. 812-4. La coordination neutre est demandée sous `requests`.
- **Point pour l'auteur :** la date d'entrée en vigueur de l'ordonnance n° 2004-605 n'est pas reprise, car elle n'a pas été vérifiée.

### CSS R162-8 (LEGIARTI000006747526) : appliquée (coordination)

- **Ce qui change :** la clause « ne dérogent pas au régime de l'accord national » ne couvrait pas le régime subsidiaire légal du dernier alinéa de L. 162-32-2 : à défaut d'accord, ou pour les centres non adhérents, les tarifs sont ceux des conventions de chaque profession. Elle est remplacée par une exclusion expresse des centres de santé. Les paiements antérieurs et les droits des assurés sont conservés.
- **Ce qui ne change pas :** la suppression du visa préfectoral, déjà décidée par le projet.
- **Pourquoi l'article n'est pas abrogé :** d'autres catégories de dispensaires figurent encore dans les textes (R145-1 vise des « dispensaires antituberculeux »).
- **Points pour l'auteur :**
  - le sort de l'article pour ces structures ;
  - R162-3 (conventions communes avec les dispensaires), non modifié.

### CGI 259 D (LEGIARTI000048835152, W14) : non appliquée, hors corpus

- **Ce qui reste :** le rétablissement des I, II 1 et III est déjà neutralisé. Mais la dénonciation libre de l'option n'est portée que par le 2 du II, maintenu seulement jusqu'à sa reprise réglementaire au CIBS. La cible de cette reprise est discordante (L. 222-17 selon la NOTA, L. 232-17 selon le tableau de l'article 15) et hors corpus.
- **Pourquoi rien n'est fait ici :** la disposition non codifiée existe déjà sous `uncodified` dans `apply/W14/changes.json`.

### CSS R641-4 (LEGIARTI000006751755) : non appliquée, arbitrage

- **Le défaut :** le chapitre VIII du titre II du livre Ier du code de commerce ne prévoit plus de condamnation ni de sanction. Il organise aujourd'hui le fichier national des interdits de gérer.
- **Pourquoi c'est un arbitrage :** viser l'interdiction de gérer crée une condition nouvelle ; supprimer le renvoi retire un filtre d'honorabilité.
- **Autres articles concernés :** le même renvoi figure dans CSS D432-2, CCH L241-7 et l'annexe III 46 quindecies N.
- **Hors périmètre ici :** la restriction de nationalité aux États de l'Union (F9) et la mention « agent comptable ».

### Code du travail R3232-4 (LEGIARTI000043128618) : non appliquée, arbitrage

- **Le défaut :** l'aide de l'État à l'allocation complémentaire n'a plus de base de fond depuis l'abrogation de L. 3232-8 en 2013. Pourtant, le 1° de L. 3232-9 vise encore la « part » de l'État.
- **Pourquoi c'est un arbitrage :** abroger R3232-3, R3232-4, R3232-6, R3232-7 et R3232-8 supprimerait une aide ; la rétablir dans la loi créerait une dépense.

### Déjà réglés

- **Annexe II 371 M (M05) :** tout le bloc 371 A à 371 Z sexdecies est abrogé.
- **Annexe IV 152 :** abrogé avec 146 à 154.
- **CCH L371-4 (Y12) :** 4° abrogé, 7° et 1° corrigés.
- **Code du travail D5134-1 (W08) :** abrogé avec D5134-2 à D5134-13.

## Réserve sur la mesure

Ces dix articles viennent de l'échantillon apparié qui sert à mesurer le taux de défauts grossiers. Corriger les articles tirés au sort ne fait pas baisser le taux de la population. L'échantillon cesse simplement d'être représentatif après correction.

Pour l'article :
- garder la mesure d'origine, faite avant correction ;
- signaler que ces articles ont été corrigés depuis ;
- ne présenter un taux « après correction » que s'il vient d'un nouvel échantillon indépendant.

Revue IA : rien de ceci ne vaut validation par un juriste.
