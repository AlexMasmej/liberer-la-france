# Y18 : troisième balayage (S9), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Les exports sont dans `evidence/cited/production-20261029/`. Le paquet `audit/sweeps/packet-Y18.json` compte 51 articles des annexes III et IV du CGI et 62 pistes, toutes de type S9. Il n'y a aucune piste S10.

Contrôle : `python3 -B apply/check_changes.py Y18` construit 4 lignes, en valide 4, et `problems` est vide. Les diagnostics sont voulus : réductions déclarées pour 41 quater et 50-0 A bis, changements de longueur pour 41 quater et 170 septies H.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G, corrigé | 4 (41 quater, 50-0 A bis, 170 septies H, 170 decies) |
| m, non corrigé | 2 (344-0 B 10°, 41 ter) |
| déjà réglé | 26 |
| faux positif | 30 |

À cela s'ajoute un constat connexe m, non corrigé : les notes de 2 sexdecies A.

Corrections : 4 lignes en mode `replace`, toutes en annexe IV. Une demande est adressée au groupe Y15 (annexe II 289, 68°). Rien n'est écarté (`skipped` vide). Aucune fermeture de faille. Aucune disposition non codifiée.

## Défauts confirmés et corrigés

- **41 quater** (LEGIARTI000006300373), piste S9 vers 286 quater. G, F1.
  - Défaut : l'article impose encore des registres « identifiés » et tenus dans l'ordre chronologique, sans réserve, pour les registres du II de 286 quater (façonniers et prestataires, via 41 ter). Or 286 quater III proposé dispose : « Aucun support spécial, aucune seconde saisie de ces informations et aucun registre distinct de ces écritures et pièces ne sont exigés au seul titre du II ». Il interdit aussi à l'arrêté de rétablir ces obligations.
  - Correction : un alinéa dit que, pour les registres des 1 et 3 du II, les écritures et pièces ordinaires en tiennent lieu. Les exigences d'identification et de chronologie sont alors satisfaites sans support spécial. C'est le modèle de 29 E proposé pour 277 A. La transition reprend le IV de 286 quater.
  - Inchangés : le registre de 41 bis (I de 286 quater), la centralisation facultative, le contenu originel et L. 102 B. La liste `removed_provisions` reçoit une entrée de coordination.
- **50-0 A bis** (LEGIARTI000042147351), piste S9 vers 302 V bis. G, F1.
  - Défaut : le I organise encore la demande d'agrément, l'admission et l'attribution d'un numéro (« la demande d'agrément est transmise »). Or 302 V bis proposé dispose : « Le représentant fiscal exerce son activité sans agrément préalable ». Ses notes signalaient cette contradiction.
  - Correction : le I constate l'absence d'agrément et de toute demande de remplacement. La justification de la caution, que la loi maintient et que la source exigeait déjà, est conservée sans décision et sans délai nouveau. Aux II 2° et III a 2°, le numéro devient « le cas échéant », pour les représentants déjà agréés. La transition reprend 302 V bis : demandes sans objet, numéros existants utilisables.
  - Inchangés : le mandat, la déclaration par vendeur, la comptabilité et la conservation. Une note fausse est corrigée (« agrément, caution et comptabilité y sont exigés »). La citation exacte de `substantive_impact` est conservée.
- **170 septies H** (LEGIARTI000006301159), piste S9 vers 238 bis. G, F1.
  - Défaut : la compétence vise toutes les demandes d'agrément du 4 de 238 bis, « aux demandes nouvelles » comprises. Or 238 bis 4 proposé dispose : « sans agrément fiscal préalable ». Son 9 ne garde que les demandes « utiles aux dons et versements antérieurs ». Les notes de 238 bis signalaient le défaut.
  - Correction : la compétence est bornée aux demandes résiduelles. Aucune demande n'est présentée ni instruite pour les dons nouveaux. Les demandes pendantes qui ne concernent que ces dons deviennent sans objet. Les décisions acquises sont conservées. C'est le modèle de 121 Z sexies proposé.
  - La note devenue fausse (« aucune telle abrogation n'est prétendue ici ») est retirée. Les citations de `substantive_impact` sont mises à jour.
- **170 decies** (LEGIARTI000045759960), maintenu, piste S9 vers 244 quater W. G, F1.
  - Défaut : le I, le I bis, le II et le III organisent la délivrance et la saisine de l'agrément du 4 de 199 undecies A, des II quater et III de 217 undecies et du VII de 244 quater W. Les trois propositions législatives suppriment cet agrément. Les notes de 244 quater W et de 217 undecies signalaient la coordination ouverte.
  - Correction : mode `replace`, avec le statut `rewrite_draft` et la classification `coordination_only`. Les I à IV de la source sont repris à l'identique. Un V les borne aux agréments antérieurs, à leur contestation et à leur retrait, sans demande nouvelle ni déclaration de remplacement. Les demandes pendantes n'ont pas à être renouvelées, et les droits et recours acquis sont préservés.
  - Le motif et les notes « Maintien intégral » sont réécrits.

## Défauts mineurs non corrigés (articles non modifiés)

- **344-0 B 10°** (LEGIARTI000053732969), m, F5. Le renvoi à la déclaration de 990 F n'a pas la borne temporelle des autres taxes supprimées, alors que 990 F proposé borne la taxe de 990 D aux années antérieures. L'effet est nul : la clause finale dispose « Le présent article désigne seulement le service destinataire des déclarations légalement requises ».
- **41 ter** (LEGIARTI000006300371), m, F5. Il garde l'intitulé « registre spécial » et la condition d'expédition depuis un autre État membre, devenue le champ même du registre. Le fond est couvert par la correction de 41 quater.
- **2 sexdecies A** (LEGIARTI000049642649), constat connexe, m, F10. Les notes disent encore « permet la suspension après trois ans », alors que 31 l proposé dispose « sans durée minimale de location préalable ». Le corps est conforme.

## Points laissés à l'auteur

- La justification de la caution au I de 50-0 A bis est conservée sans échéance. L'auteur peut préférer une production sur demande seulement. Ce serait un allègement supplémentaire, non décidé ici.
- La demande à Y15 porte sur l'annexe II 289, 68° (« Délivrance de l'agrément de représentant fiscal »), qui est à borner aux agréments antérieurs. Elle est à ignorer si Y15 l'a déjà traité.
- Coordinations signalées par les notes du projet, hors paquet et non vérifiées ici :
  - 242 septies, et 1740 et 1743 3°, qui renvoient aux agréments ultramarins supprimés (voir les notes de 244 quater W) ;
  - 344 O, la déclaration d'acomptes de taxe d'aménagement, dont le bornage aux autorisations antérieures n'a pas été vérifié ici.
- Le régime simplifié annuel de 287, retiré au 1er janvier 2027 par la LF 2025 (droit officiel), touche 50 duodecies A bis 2°. C'est une question de version future, hors S9.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| a3 2 octodecies (LEGIARTI000049642600) | S9/F1+F5 | 31 | déjà réglé | non |
| a3 2 septdecies (LEGIARTI000049642610) | S9/F1+F5 | 31 | déjà réglé | non |
| a3 2 sexdecies A (LEGIARTI000049642649) | S9/F1+F5 | 31 | déjà réglé | non |
| a3 2 sexdecies (LEGIARTI000049642655) | S9/F1+F5 | 31 | faux positif | non |
| a3 95 (LEGIARTI000049826491) | S9/F1+F5 | 289 A | faux positif | non |
| a3 95 (LEGIARTI000049826491) | S9/F1+F5 | 287 | faux positif | non |
| a3 95 (LEGIARTI000049826491) | S9/F1+F5 | 277 A | faux positif | non |
| a3 344 N (LEGIARTI000050735686) | S9/F1+F5 | 1635 quater P | faux positif | non |
| a3 344 N (LEGIARTI000050735686) | S9/F1+F5 | 1406 | faux positif | non |
| a3 322 A (LEGIARTI000050735717) | S9/F1+F5 | 1418 | déjà réglé | non |
| a3 46 quater-0 ZZB (LEGIARTI000050735886) | S9/F1+F5 | 223 WW | déjà réglé | non |
| a3 46 quater-0 ZZC (LEGIARTI000050735888) | S9/F1+F5 | 223 WW | déjà réglé | non |
| a3 315 ter A (LEGIARTI000050737774) | S9/F1+F5 | 1384 C bis | déjà réglé | non |
| a3 88 (LEGIARTI000050741244) | S9/F1+F5 | 278 sexies A | déjà réglé | non |
| a3 88 (LEGIARTI000050741244) | S9/F1+F5 | 1384 C bis | faux positif | non |
| a3 366 B (LEGIARTI000050741762) | S9/F1+F5 | 223 WW | déjà réglé | non |
| a3 95 C (LEGIARTI000051183527) | S9/F1+F5 | 287 | faux positif | non |
| a3 49 septies ZZ quater (LEGIARTI000051762503) | S9/F1+F5 | 223 A | faux positif | non |
| a3 322 ter (LEGIARTI000051892176) | S9/F1+F5 | 1407 | déjà réglé | non |
| a3 322 (LEGIARTI000051892179) | S9/F1+F5 | 1407 | déjà réglé | non |
| a3 46 quindecies P (LEGIARTI000052040025) | S9/F1+F5 | 238 bis | déjà réglé | non |
| a3 49 septies ZZX bis (LEGIARTI000052050854) | S9/F1+F5 | 244 quater X | faux positif | non |
| a3 344-0 C (LEGIARTI000052589641) | S9/F1+F5 | 223 A | faux positif | non |
| a3 344-0 A (LEGIARTI000052589674) | S9/F1+F5 | 223 A | faux positif | non |
| a3 344-0 A (LEGIARTI000052589674) | S9/F1+F5 | 256 C | faux positif | non |
| a3 39 (LEGIARTI000053218832) | S9/F1+F5 | 231 | déjà réglé | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 231 | déjà réglé | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 990 F | m | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 231 ter | déjà réglé | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 256 C | faux positif | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 299 septies | faux positif | non |
| a3 344-0 B (LEGIARTI000053732969) | S9/F1+F5 | 223 WW | faux positif | non |
| a3 95 ter (LEGIARTI000054364224) | S9/F1+F5 | 289 A bis | déjà réglé | non |
| a3 95 ter (LEGIARTI000054364224) | S9/F1+F5 | 277 A | faux positif | non |
| a4 41 ter (LEGIARTI000006300371) | S9/F1+F5 | 286 quater | m | non |
| a4 41 quater (LEGIARTI000006300373) | S9/F1+F5 | 286 quater | G | oui |
| a4 50-0 I (LEGIARTI000006300444) | S9/F1+F5 | 302 D bis | déjà réglé | non |
| a4 121 VA (LEGIARTI000006300843) | S9/F1+F5 | 1066 | déjà réglé | non |
| a4 170 septies H (LEGIARTI000006301159) | S9/F1+F5 | 238 bis | G | oui |
| a4 36 (LEGIARTI000006301304) | S9/F1+F5 | 287 | faux positif | non |
| a4 196 A (LEGIARTI000006301986) | S9/F1+F5 | 991 | déjà réglé | non |
| a4 29 E (LEGIARTI000023103009) | S9/F1+F5 | 277 A | déjà réglé | non |
| a4 50-00 I (LEGIARTI000024526467) | S9/F1+F5 | 302 H ter | faux positif | non |
| a4 50-00 J (LEGIARTI000024526469) | S9/F1+F5 | 302 H ter | faux positif | non |
| a4 121 quinquies DB quater (LEGIARTI000027511497) | S9/F1+F5 | 1465 | faux positif | non |
| a4 188-0 I (LEGIARTI000037351336) | S9/F1+F5 | 125 D | faux positif | non |
| a4 170 quinquies (LEGIARTI000038491979) | S9/F1+F5 | 1465 | faux positif | non |
| a4 191 (LEGIARTI000041438607) | S9/F1+F5 | 283 bis | déjà réglé | non |
| a4 192 bis (LEGIARTI000041455751) | S9/F1+F5 | 283 bis | déjà réglé | non |
| a4 50-0 A bis (LEGIARTI000042147351) | S9/F1+F5 | 302 V bis | G | oui |
| a4 121 Z sexies (LEGIARTI000042202007) | S9/F1+F5 | 978 | déjà réglé | non |
| a4 01 ter (LEGIARTI000042522459) | S9/F1+F5 | 31 | faux positif | non |
| a4 41 bis A (LEGIARTI000043573764) | S9/F1+F5 | 286 quater | faux positif | non |
| a4 41 bis (LEGIARTI000043584966) | S9/F1+F5 | 286 quater | faux positif | non |
| a4 41 quinquies (LEGIARTI000043592499) | S9/F1+F5 | 286 quater | faux positif | non |
| a4 170 decies (LEGIARTI000045759960) | S9/F1+F5 | 244 quater W | G | oui |
| a4 50 duodecies A bis (LEGIARTI000045866114) | S9/F1+F5 | 287 | faux positif | non |
| a4 41-0 bis (LEGIARTI000046327698) | S9/F1+F5 | 287 | faux positif | non |
| a4 29 G (LEGIARTI000047621518) | S9/F1+F5 | 277 A | déjà réglé | non |
| a4 29 D (LEGIARTI000047621534) | S9/F1+F5 | 277 A | déjà réglé | non |
| a4 29 C (LEGIARTI000047621545) | S9/F1+F5 | 277 A | déjà réglé | non |
| a4 32 (LEGIARTI000051757588) | S9/F1+F5 | 287 | faux positif | non |
