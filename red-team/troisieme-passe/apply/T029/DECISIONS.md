# T029 — décisions (lecture systématique, palier A)

Section lue : CGI, impôt sur les sociétés, section VIII « Groupes de sociétés », articles 223 A à 223 I (11 articles). Texte lu en production, en lecture seule, le 30 octobre 2026. Aucun article n'a de version future publiée (`VIGUEUR_DIFF`).

Décompte : 1 G, 7 m, 3 « 0 ».

## TA-T029-01 — 223 D (LEGIARTI000037987493) : appliquée

- **Défaut (G, F3 + F5).** La quatrième phrase du sixième alinéa retranche « la fraction de la provision qui n'a pas été retenue en application de la deuxième phrase du présent alinéa ». Le cas visé, celui du deuxième alinéa de 223 F, concerne les provisions passées après une cession interne. Or cette règle est à la troisième phrase depuis 2010. Les versions LEGIARTI000018026899 (2007-2010) et LEGIARTI000021682331 (2010) montrent l'origine du décalage : la loi a inséré une phrase sur les sociétés intermédiaires et mis à jour les autres renvois, mais pas celui-ci. Le projet corrige le même décalage dans 223 B (« la deuxième ou de la troisième phrase ») et le laisse dans 223 D, l'article parallèle. Les notes le donnaient pour « non vérifiable dans l'historique fourni », alors que cet historique figure au corpus.
- **Correction.** Le renvoi devient « la deuxième ou de la troisième phrase du présent alinéa », comme dans 223 B. La portée littérale de la deuxième phrase est conservée. Aucune autre phrase du corps n'est modifiée.
- **Au passage (m, F10, sur l'article modifié).** Le motif ne dit plus « conservée intégralement ». Dans les notes, les remarques périmées sont corrigées : renvoi de 209 XI 1 au II de 216, déjà corrigé, et mention « identique octet pour octet ». Dans `substantive_impact.scope_limitations`, la phrase sur 209 XI 1 et sur l'historique est mise à jour, sans toucher aux citations des effets.
- **Point pour l'auteur.** Comme dans 223 B, la correction cumule deux renvois au lieu de remplacer l'un par l'autre. C'est la lecture la plus favorable, et le texte reste aligné sur celui de 223 B.

## TA-T029-02 — annexe III, 46 quater-0 ZE et 46 quater-0 ZK : demandes (`requests`)

- **Défaut (lien, F3).** Ces deux articles appliquent 223 A et le citent mal. Ils renvoient au IV de 223 A pour les accords des filiales (ZE), pour la mention de sortie (ZE) et pour la notification de la liste (ZK). Or le IV de 223 A proposé (LEGIARTI000048834056) porte le régime de distribution. Les options, accords, listes et modifications de périmètre sont aux deuxième et troisième alinéas de son III, comme le confirme le 7 de 223 L proposé (« notifiés dans les conditions du III de l'article 223 A »). Le même décalage a déjà été corrigé dans 46 quater-0 ZD et ZF (AUDIT6-E136).
- **Demande.** Remplacer « IV » par « III » dans ces renvois, avec le texte exact indiqué dans `changes.json`, et corriger les notes devenues fausses. Destinataires : J13 pour ZE (LEGIARTI000031391609) et Y17 pour ZK (LEGIARTI000045766216). Aucune formalité n'est ajoutée.

## Défauts mineurs non corrigés (articles non modifiés)

- **223 A, 223 C (m, F10 + F5 à confirmer).** Le IV de 223 A dispose : « Aucun résultat de référence individuel ou d'ensemble [...] ne rend exigible un IS ordinaire sur des bénéfices conservés ». Le premier alinéa de 223 C va dans le même sens. Or le 6 du V de 219 ouvre une option de liquidation annuelle, « exercée par la société mère pour l'ensemble des membres ». Aucun texte ne précise l'assiette de cet impôt annuel pour un groupe (résultat de référence d'ensemble ou résultat de chaque membre), ni son redevable. Une lecture reste possible, puisque 206 et 1668 rangent l'option parmi les « régimes annuels distincts », que 223 A réserve à la fin de son IV. **Arbitrage pour l'auteur** : il faut choisir l'assiette du groupe. L'assiette d'ensemble serait la plus cohérente avec la règle de 223 A IV : « La somme des cotisations individuelles ne peut supprimer les avantages d'intégration ». Aucune correction n'est faite.
- **223 A, 223 B, 223 B bis, 223 C, 223 E, 223 F, 223 I (m, F10).** Leurs notes annoncent comme restant à faire des coordinations déjà faites : 209 XI 1 renvoie désormais au IV de 216 ; 46 quater-0 ZL 9 est devenu une dispense ; 223 L 7 admet les pertes nouvelles ; 223 I I ouvre les attributions futures de 223 E ; 223 L vise les bonnes subdivisions de 223 A. Ces défauts ne sont pas corrigés, parce qu'ils portent sur des articles que le groupe ne modifie pas.
- **210 A (hors paquet, signalé par les notes de 223 D).** Le 3 a garde la reprise de « la réserve spéciale » des plus-values. Ce renvoi est neutralisé par la clause de 209 quater proposé (« Aucun renvoi au présent article ne peut rétablir, pour l'avenir, l'obligation de réserve spéciale »). Il n'y a pas de demande.

## Sans anomalie

223 A bis, 223 G, 223 H.

## Dossiers

- `apply/T029/` : 1 correction (223 D), 2 demandes. Validé par `python3 -B apply/check_changes.py T029` (`problems` vide).
- Aucun dossier de variante : la seule correction porte sur un article sans `previous_owner`.

Revue IA, sans validation par un juriste.
