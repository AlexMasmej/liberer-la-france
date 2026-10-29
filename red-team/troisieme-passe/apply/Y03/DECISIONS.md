# Groupe Y03 — décisions (troisième balayage, S9/S10)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`). Paquet : `audit/sweeps/packet-Y03.json`, 52 articles et 70 pistes (60 S9, 10 S10), toutes du code de la sécurité sociale, sauf une cible du CGI (article 998). Pour chaque piste S9, j'ai lu les `removed_provisions` du lot de la loi visée et sa proposition entière, puis la proposition du décret. Pour chaque piste S10, j'ai vérifié que l'article visé contient encore la règle à laquelle la dérogation se rapporte.

## Bilan

- 70 pistes traitées : 69 faux positifs, 1 défaut G confirmé (corrigé), aucune piste non traitée.
- 1 correction (`apply/Y03/changes.json`, mode `replace`) ; `python3 -B apply/check_changes.py Y03` renvoie `problems: []`. Le seul diagnostic, `length_change` (ratio 2,66), est voulu : un alinéa de champ a été ajouté.
- Aucune demande à un autre groupe. Aucune piste écartée pour défaut d'alignement.

## Correction appliquée

**SW-Y03-D138-2**, CSS D138-2 (LEGIARTI000043743140), F5/F4, G : appliquée.
- La piste S9 elle-même est un faux positif : la déclaration de l'entreprise est maintenue par L138-15, seuls le modèle exclusif et la majoration sont retirés, et le décret ne les rétablit pas.
- Le défaut est apparu à la lecture. L138-15 (LEGIARTI000046805500) est en ABROGE_DIFF au 1er janvier 2027. Sa version suivante (LEGIARTI000051287301, issue de l'article 28 de la LFSS pour 2024, entrée en vigueur le 1er janvier 2027 selon le NOTA) est acceptée par le projet. Elle supprime la déclaration de l'entreprise, ouvre une rectification de la liste sous vingt jours et fixe la communication des remises par le CEPS avant le 31 juillet.
- D138-2 proposé imposait encore, sans borne de champ, l'échéance du 15 juillet et la rectification de « la déclaration qu'elles ont transmise, conformément au I de l'article L. 138-15 ».
- Correction : ajout d'un alinéa de champ, symétrique de la clause déjà inscrite dans la proposition de L138-15. Il limite l'article aux contributions régies par la rédaction antérieure et n'impose aucune déclaration, rectification ou échéance supplémentaire pour les contributions régies par la version de 2027.
- Rien d'autre ne change : délais, remises et garanties restent les mêmes. `substantive_impact` est mis à jour (`scope_limitations`, `conditions_and_transition`) ; les citations restent exactes.
- Point pour l'auteur : D138-2 officiel est lui aussi dépassé à partir de 2027 (conflit de source). Le règlement qui sera pris pour la version de 2027 reste hors corpus.

## Une ligne par piste

| # | Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|---|
| 1 | R612-14 (LEGIARTI000042363296) | S9/F1+F5 | css L612-6 (LEGIARTI000036390970) | faux positif | non |
| 2 | R612-9 (LEGIARTI000042363331) | S9/F1+F5 | css L243-6-3 (LEGIARTI000048700846) | faux positif | non |
| 3 | R612-9 (LEGIARTI000042363331) | S9/F1+F5 | css L612-3 (LEGIARTI000036390989) | faux positif | non |
| 4 | R612-9 (LEGIARTI000042363331) | S10/F5 (échantillon) | css L243-6-5 (LEGIARTI000039279570) | faux positif | non |
| 5 | R612-2 (LEGIARTI000042363381) | S10/F5 (échantillon) | css R612-1 (LEGIARTI000042363384) | faux positif | non |
| 6 | D582-2 (LEGIARTI000042385697) | S9/F1+F5 | css L582-1 (LEGIARTI000044629452) | faux positif | non |
| 7 | R582-1 (LEGIARTI000042385806) | S9/F1+F5 | css L582-2 (LEGIARTI000044629425) | faux positif | non |
| 8 | R138-19 (LEGIARTI000042389712) | S9/F1+F5 | css L245-6 (LEGIARTI000053282660) | faux positif | non |
| 9 | R138-19 (LEGIARTI000042389712) | S9/F1+F5 | css L138-20 (LEGIARTI000051287267) | faux positif | non |
| 10 | L862-4 (LEGIARTI000042698839) | S10/F5 (échantillon) | cgi 998 (LEGIARTI000053545572) | faux positif | non |
| 11 | R862-11 (LEGIARTI000042904693) | S9/F1+F5 | css L862-4 (LEGIARTI000042698839) | faux positif | non |
| 12 | R861-20 (LEGIARTI000042904705) | S9/F1+F5 | css L861-7 (LEGIARTI000042686126) | faux positif | non |
| 13 | R861-19 (LEGIARTI000042904710) | S9/F1+F5 | css L861-7 (LEGIARTI000042686126) | faux positif | non |
| 14 | R461-4 (LEGIARTI000043128334) | S9/F1+F5 | css L461-4 (LEGIARTI000006743137) | faux positif | non |
| 15 | R165-95 (LEGIARTI000043182199) | S9/F1+F5 | css L165-1-5 (LEGIARTI000046812781) | faux positif | non |
| 16 | R138-2 (LEGIARTI000043198094) | S9/F1+F5 | css L138-9-1 (LEGIARTI000051287416) | faux positif | non |
| 17 | R611-2 (LEGIARTI000043292679) | S9/F1+F5 | css L613-4 (LEGIARTI000038595817) | faux positif | non |
| 18 | R611-2 (LEGIARTI000043292679) | S9/F1+F5 | css L641-2 (LEGIARTI000042685415) | faux positif | non |
| 19 | R611-2 (LEGIARTI000043292679) | S10/F5 (échantillon) | css R123-1 (LEGIARTI000029389194) | faux positif | non |
| 20 | R165-101 (LEGIARTI000043298555) | S9/F1+F5 | css L165-2-2 (LEGIARTI000039779219) | faux positif | non |
| 21 | R165-101 (LEGIARTI000043298555) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 22 | R165-101 (LEGIARTI000043298555) | S9/F1+F5 | css L165-5-1 (LEGIARTI000048697505) | faux positif | non |
| 23 | R165-102 (LEGIARTI000043298557) | S9/F1+F5 | css L165-2-2 (LEGIARTI000039779219) | faux positif | non |
| 24 | R165-103 (LEGIARTI000043298559) | S9/F1+F5 | css L165-2-2 (LEGIARTI000039779219) | faux positif | non |
| 25 | D162-25-2 (LEGIARTI000043412725) | S9/F1+F5 | css L162-1-7 (LEGIARTI000053283421) | faux positif | non |
| 26 | R162-52-1 (LEGIARTI000043413468) | S9/F1+F5 | css L162-1-7 (LEGIARTI000053283421) | faux positif | non |
| 27 | R162-52-1 (LEGIARTI000043413468) | S9/F1+F5 | css L315-2 (LEGIARTI000048687768) | faux positif | non |
| 28 | D441-4 (LEGIARTI000043464450) | S9/F1+F5 | css L441-4 (LEGIARTI000042686351) | faux positif | non |
| 29 | D441-4 (LEGIARTI000043464450) | S9/F1+F5 | css L441-2 (LEGIARTI000006743085) | faux positif | non |
| 30 | D441-2 (LEGIARTI000043464456) | S9/F1+F5 | css L441-4 (LEGIARTI000042686351) | faux positif | non |
| 31 | D642-4-3 (LEGIARTI000043656684) | S9/F1+F5 | css L642-4-2 (LEGIARTI000051290062) | faux positif | non |
| 32 | D642-4-2 (LEGIARTI000043656695) | S9/F1+F5 | css L642-4-2 (LEGIARTI000051290062) | faux positif | non |
| 33 | D138-2 (LEGIARTI000043743140) | S9/F1+F5 | css L138-15 (LEGIARTI000046805500) | G | oui (SW-Y03-D138-2) |
| 34 | R163-53 (LEGIARTI000043758797) | S9/F1+F5 | css L162-16-5-2 (LEGIARTI000046812499) | faux positif | non |
| 35 | R315-14 (LEGIARTI000043762366) | S9/F1+F5 | css L315-2 (LEGIARTI000048687768) | faux positif | non |
| 36 | R162-37 (LEGIARTI000043912223) | S9/F1+F5 | css L162-16-5-2 (LEGIARTI000046812499) | faux positif | non |
| 37 | D165-2 (LEGIARTI000044133692) | S9/F1+F5 | css L165-5-1 (LEGIARTI000048697505) | faux positif | non |
| 38 | D165-2 (LEGIARTI000044133692) | S9/F1+F5 | css L165-1-5 (LEGIARTI000046812781) | faux positif | non |
| 39 | L861-11 (LEGIARTI000044628815) | S10/F5 (échantillon) | css L861-1 (LEGIARTI000037950247) | faux positif | non |
| 40 | R225-1 (LEGIARTI000045133663) | S9/F1+F5 | css L225-1-1 (LEGIARTI000051289059) | faux positif | non |
| 41 | R313-5 (LEGIARTI000045250320) | S9/F1+F5 | css L341-2 (LEGIARTI000041398963) | faux positif | non |
| 42 | R582-5 (LEGIARTI000045250569) | S9/F1+F5 | css L582-1 (LEGIARTI000044629452) | faux positif | non |
| 43 | D323-6-2 (LEGIARTI000045368068) | S9/F1+F5 | css L441-2 (LEGIARTI000006743085) | faux positif | non |
| 44 | D323-6-2 (LEGIARTI000045368068) | S9/F1+F5 | css L461-5 (LEGIARTI000036393199) | faux positif | non |
| 45 | R861-18 (LEGIARTI000045601938) | S9/F1+F5 | css L861-5 (LEGIARTI000046806509) | faux positif | non |
| 46 | R162-34-12 (LEGIARTI000045635497) | S9/F1+F5 | css L162-16-5-1 (LEGIARTI000042685888) | faux positif | non |
| 47 | R133-22 (LEGIARTI000046176903) | S10/F5 (échantillon) | css R243-21 (LEGIARTI000039222687) | faux positif | non |
| 48 | R133-20 (LEGIARTI000046176912) | S9/F1+F5 | css L133-8-7 (LEGIARTI000048700647) | faux positif | non |
| 49 | R133-20 (LEGIARTI000046176912) | S9/F1+F5 | css L133-8-4 (LEGIARTI000048700659) | faux positif | non |
| 50 | D224-7 (LEGIARTI000046356432) | S9/F1+F5 | css L224-5-1 (LEGIARTI000037948891) | faux positif | non |
| 51 | D224-7 (LEGIARTI000046356432) | S9/F1+F5 | css L123-1 (LEGIARTI000037948839) | faux positif | non |
| 52 | D224-7 (LEGIARTI000046356432) | S9/F1+F5 | css L123-2 (LEGIARTI000037948868) | faux positif | non |
| 53 | L165-4-1 (LEGIARTI000046812815) | S10/F5 (échantillon) | css L165-4 (LEGIARTI000053282805) | faux positif | non |
| 54 | R147-8 (LEGIARTI000046844852) | S9/F1+F5 | css L315-2 (LEGIARTI000048687768) | faux positif | non |
| 55 | R147-8 (LEGIARTI000046844852) | S9/F1+F5 | css L162-1-15 (LEGIARTI000054335791) | faux positif | non |
| 56 | D162-32 (LEGIARTI000046876929) | S9/F1+F5 | css L162-51 (LEGIARTI000044565984) | faux positif | non |
| 57 | R162-106 (LEGIARTI000046880044) | S9/F1+F5 | css L162-51 (LEGIARTI000044565984) | faux positif | non |
| 58 | R162-107 (LEGIARTI000046880046) | S9/F1+F5 | css L162-51 (LEGIARTI000044565984) | faux positif | non |
| 59 | R165-5-2 (LEGIARTI000046883789) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 60 | R165-87 (LEGIARTI000046884412) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 61 | R165-87 (LEGIARTI000046884412) | S9/F1+F5 | css L165-5-1 (LEGIARTI000048697505) | faux positif | non |
| 62 | R165-10 (LEGIARTI000046884478) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 63 | R165-5 (LEGIARTI000046884493) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 64 | R165-91 (LEGIARTI000047384103) | S9/F1+F5 | css L165-1-5 (LEGIARTI000046812781) | faux positif | non |
| 65 | R165-91 (LEGIARTI000047384103) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 66 | R165-89 (LEGIARTI000047384113) | S9/F1+F5 | css L165-1-5 (LEGIARTI000046812781) | faux positif | non |
| 67 | R165-89 (LEGIARTI000047384113) | S9/F1+F5 | css L165-1 (LEGIARTI000046822845) | faux positif | non |
| 68 | R243-17 (LEGIARTI000047437207) | S10/F5 (échantillon) | css R243-59 (LEGIARTI000053220874) | faux positif | non |
| 69 | R243-19 (LEGIARTI000047480864) | S9/F1+F5 | css L133-8-7 (LEGIARTI000048700647) | faux positif | non |
| 70 | R147-9-2 (LEGIARTI000047502404) | S9/F1+F5 | css L315-2 (LEGIARTI000048687768) | faux positif | non |

Le détail des citations exactes de chaque piste est dans `audit/sweeps/Y03.json`.

## Observations hors pistes (non corrigées, signalées à l'auteur)

- L245-6 (LEGIARTI000053282660, ABROGE_DIFF au 2028-01-01) a une version future, LEGIARTI000054703326 (2028), et L861-5 (LEGIARTI000046806509) en a une, LEGIARTI000048702075, avec la borne technique 2222-02-22. Ces deux versions relèvent de la piste S5 et ne sont pas dans ce paquet : je ne les ai pas examinées.
- R611-2 V (LEGIARTI000043292679) écrit « L. 613-4 du même code » juste après une mention du code de commerce. La formule vient de la source et l'ambiguïté n'a pas d'effet de fond : défaut m, non corrigé, car l'article n'est pas modifié.
- R147-9-2 3° (LEGIARTI000047502404) vise L162-1-17 pour la mise sous accord préalable des centres de santé. R147-8 vise L162-1-15, dont le I bis couvre ces centres. C'est un point préexistant, hors piste, à vérifier.

Revue assistée par IA : elle ne vaut pas validation par un juriste.
