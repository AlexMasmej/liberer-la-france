# D351-9 : graphique récupéré, concordance entière réservée

Le graphique mensuel E du décret 2003-1376 est retrouvé dans le JO du 1er janvier 2004, PDF page 47 / page imprimée 47. La page entière et le début de D351-9 page 46 ont été rendus et lus. Un détail natif à 300 dpi a permis de contrôler k=0, la borne k=57, les soustractions séparées −11/24 et −1/12, les rapports de survie et l’exposant A−B. Le rectificatif du 31 janvier 2004, NOR SOCS0325036Z, ne modifie pas cette formule. La substitution expresse 57→55 en 2010 est claire. Aucune simplification n’est faite.

Le conflit porte sur une définition environnante conservée dans la source canonique, et non sur la lecture du graphique.

## Position réelle avant 2010

La version officielle LEGIARTI000019993446 est en vigueur du 25 décembre 2008 au 1er janvier 2011. La page entière, ouverte avec la date 2009-06-26, est conservée dans `web-14.json` : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019993446/2009-06-26.

La fin du corps normatif, sans ajout après la dernière définition, est dans cet ordre :

1. L(A+k), effectif à l’âge A+k (ligne de restitution 172).
2. L(A), effectif à l’âge de soixante ans (ligne 174).
3. L(B), effectif à l’âge B (ligne 176, dernière définition).

L(A) est donc bien l’avant-dernier alinéa de cette version. La page officielle le confirme directement ; il ne s’agit pas d’un comptage fondé uniquement sur le texte de 2004. Les notes de la source canonique courante sont vides et sont conservées.

## Modifications expresses examinées

| Texte | Disposition | Portée constatée |
|---|---|---|
| Décret 2006-879 du 17 juillet 2006 | Article 1 III, et article 7 | Au 1°, modifie la majoration projetée du plafond ; remplace la définition de B par la date d’acceptation ; ajoute une dérogation transitoire pour certaines demandes 2006. Aucun opérateur E modifié. |
| Décret 2008-1383 du 19 décembre 2008 | Article 2 III | Remplace les formulations relatives à la date d’acceptation par la date de présentation de la demande. Ne remplace ni l’âge numérique de L(A), ni le graphique. |
| Décret 2010-1737 du 30 décembre 2010 | Article 1, point 3, 2° | Vise expressément les a, b et c du 4° **et l’avant-dernier alinéa** pour remplacer les mots « de soixante ans » par « de soixante-deux ans ». La dernière cible est la définition L(A) identifiée ci-dessus. |
| Même décret 2010 | Point 3, 3° et 4° | Remplace 57 par 55 dans la formule et la définition de k ; remplace l’âge de référence A fixé à 60 par 62. Ces éléments sont cohérents avec le corps canonique courant. |
| Décret 2015-332 du 24 mars 2015 | Article 2 | Change les tables de mortalité référencées et le nombre de trimestres D de 167 à 172. Aucune instruction relative à L(A) et aucune modification des opérateurs de E. |

Preuves : `web-9.json` et `web-11.json` (2006 et 2015), `../web/open-10-2008-initial.json` (texte 2008 entier), `../pages/modif2010-2.png` et PDF 2010 entier (2010), `web-14.json` (position réelle pré2010). Les textes primaires sont https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000790599, https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019986224, https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387 et https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030398366.

## Écart conservé et décision

Le corps canonique courant LEGIARTI000030400105 porte toujours « L (A) est l’effectif à l’âge de soixante ans », alors que A y est fixé à soixante-deux ans. La clause expresse de 2010 vise pourtant le passage de 60 à 62 dans cette définition. L’HTML officiel antérieur au 1er janvier 2011 permet de localiser cette cible sans ambiguïté. Le contrôle de 2015 n’apporte pas de disposition qui résolve l’écart.

Le dossier ne choisit pas silencieusement entre le texte consolidé et l’instruction du décret. Le candidat conserve strictement le corps canonique hors de l’omission graphique. `graphic_recovery_complete=true`, mais `documentary_recovery_complete=false`, `canonical_version_concordance_complete=false` et `ready_for_activation=false`.

Une proposition de correction textuelle, gardée par empreinte et séparée du candidat, est fournie dans `d351-definition-correction-proposal.json`. Elle ne constitue ni une modification du canonique, ni une activation. Elle est explicitement présentée comme la conséquence textuelle apparente d’une instruction modificatrice, jamais comme une simplification algébrique.
