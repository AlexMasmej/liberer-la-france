# X3 : décisions sur les 12 défauts grossiers du pilote « notes » (S11pilot P1 à P5)

Lecture : production en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, lots lus par `review_prior.batch_owners`), le 29 octobre 2026. Les pièces citées sont sous `evidence/cited/production-20261029/`. Avant la construction, j'ai vérifié que les 17 articles modifiés n'avaient pas changé depuis ma lecture. Rien n'a été écrit en production.

## Bilan

- 11 défauts corrigés, 1 ignoré (`skipped`) parce que déjà réglé (L200-9-1).
- `apply/X3/changes.json` modifie 15 articles. `check_changes.py X3` donne `problems: []`, avec 15 lignes construites et 15 validées.
- Variantes pour les propriétaires :
  - `apply/Y15t/` : 242 sexies de l'annexe II, propriétaire Y15 ; 1 ligne, `problems: []`.
  - `apply/B05t/` : CGI 1586, propriétaire B05 ; 1 ligne, `problems: []`.
- Identifiants des objections : `AUDIT-S11N-01` à `-12`, suivis de l'objection du registre quand elle existe.
- Diagnostics : tous voulus.
  - Rapports de longueur : ils portaient déjà sur les propositions précédentes, et pour 50 quaterdecies-0 A ter ils viennent de la transition.
  - Renvois ajoutés : R373-3, L3345-4 et L113-10.
  - Renvoi retiré : R123-221, qui figurait au 4° abrogé de 41 septies A.

## Par défaut

1. **cch R353-162 (conventions types de R373-3) : appliqué.** Le quatrième alinéa dispensait de l'envoi au préfet les stipulations des seules conventions types de R353-159. Il vise désormais aussi celles annexées à R373-3, et mentionne expressément les collectivités territoriales de Guyane et de Martinique signataires. Les annexes ne sont pas réécrites. *Pour l'auteur :* l'assimilation de la CTG et de la CTM au département délégataire est explicite ; vérifiez-la.
2. **urba L132-10 (relevé sur R313-8) : appliqué.** L'État n'est plus désigné comme destinataire de la notification initiale. La dispense du 1° de L132-11 lui est déclarée applicable. L'avis sur le projet arrêté est conservé. *Pour l'auteur :* L153-11 proposé (PLU) maintient la notification aux personnes publiques de L132-7, alors que L132-11 1° y déroge. Ce point n'est pas tranché.
3. **annexe IV 50 quaterdecies-0 A ter (CGI 302 bis WC) : appliqué.** L'article, jusqu'ici maintenu, passe en `rewrite_draft` / `coordination_only`. La ligne ovoproduits est conservée, mais bornée aux introductions antérieures. Aucun tarif ne s'applique aux introductions nouvelles. Le tarif du lait et les créances anciennes sont inchangés. Les deux lignes et les deux cellules du tableau sont conservées.
4. **css D412-97 : appliqué (retour à la source).** L'alinéa qui supposait l'abrogation de L434-16 est retiré : L434-16 est remplacé au 1er novembre 2026, pas abrogé. L'article redevient `retained_unchanged`, par une proposition provisoire puis `proposed_xml: null` en surcharge, comme dans B02. Les notes fausses (« privé de support », « successeur de L434-2 manque ») sont rectifiées.
5. **cch L200-9-1 (relevé sur R201-1) : ignoré, déjà réglé.** RT-P1-CCH-09 l'a corrigé en production aujourd'hui : le renvoi à L202-9-1 abrogé est remplacé par la durée de deux ans, écrite en toutes lettres. Une autre borne reste un choix de l'auteur.
6. **annexe II 242 sexies (relevé sur CGI 297 A), variante Y15t : appliqué, avec un écart par rapport à la piste.**
   - Les acomptes de juillet et de décembre sont bornés aux échéances antérieures à la réforme, conformément à 287 proposé.
   - Le relevé qui vaut demande de remboursement du crédit sur immobilisations ne comporte plus d'acompte quand aucun n'est dû.
   - La demande n'est **pas** rattachée à la seule déclaration annuelle, contrairement à la piste. Ce rattachement supprimerait le remboursement intermédiaire, que 287 et 242-0 C III proposés maintiennent.
   - *Pour l'auteur :* le renvoi d'ouverture au « 3 de l'article 287 » ne correspond plus à la version de 2027. Il relève de la source et des textes CIBS, hors corpus.
7. **travail D3325-6 (relevé sur L3325-2) : appliqué.** L'article, jusqu'ici maintenu, passe en coordination. Il renvoie au certificat de l'article 77 dans les conditions de 81 bis de l'annexe II, qui peut être intégré à la demande, sans certificat distinct. Les 1° et 2° sont inchangés et une transition est ajoutée. La mention de l'avoir fiscal est conservée.
8. **annexe IV 41 septies A, G, M et P (relevé sur 242 nonies E ; RT-P1-ANNEXES-02, RT-P1-CGI-A-01) : appliqué.**
   - **41 septies A**
     - Au 1° b du I, le raccordement à la solution de 242 nonies G est retiré.
     - Les 4° et 5° du I sont abrogés.
     - Le 7° c du I se limite aux processus de traitement des factures.
     - Le IV porte la transition.
     - *Extension, dans le même article :* le III organisait encore l'audit de surveillance que 242 nonies B (d du 6° du I) et C (IV) proposés suppriment. Il est remplacé par la règle selon laquelle aucun audit de surveillance n'est exigé.
   - **41 septies G :** aucun statut, y compris « encaissée », n'est plus transmis à l'administration. Le renvoi à 41 septies H, abrogé, est retiré. Le 4° du I ne renvoie plus à 242 nonies P. Au II, le renvoi à 290 A est figé dans sa rédaction antérieure à l'abrogation.
   - **41 septies M et P :** abrogation (`full_repeal`). Elle reprend la transition des articles qu'ils appliquaient : aucune transmission, même ancienne, et application de la loi répressive plus douce.
   - *Points non traités :* 41 septies D, J, K, L, N et O, et l'annexe II.
   - *Note technique :* les lignes M et P portent `reform_policy_id` et `removed_provisions` à `null`. L'outil ne permet pas de retirer une clé.
9. **urba L422-3 (relevé sur R*422-3 et R*422-4) : appliqué.** L'obligation de confirmer la délégation est supprimée. La délégation dure jusqu'à une délibération contraire. Une transition s'applique aux délégations en cours, sans faire revivre celles qui sont éteintes. La condition d'entrée en vigueur de R*422-4 est ainsi remplie. C'est une coordination : elle est comptée sous la mesure de R*422-4. *Pour l'auteur :* les notes de L422-3 avaient retenu le maintien de la confirmation, mais j'ai retenu la réforme décidée à R*422-4. Réversible si l'auteur préfère l'inverse ; il faudrait alors abandonner R*422-4.
10. **annexe II 242 nonies A (relevé sur 242 undecies) : appliqué.** Les renvois du 17° du I et du b du II à 298 sexies sont figés « dans sa rédaction en vigueur avant le 1er septembre 2026 », comme dans 242 undecies et 242 duodecies. Une clause précise que rien n'est remis en vigueur. Aucune mention n'est ajoutée. Les renvois à 297 A (16° et 18°) ne sont pas examinés.
11. **travail L3312-5 (relevé sur D3345-6 et L3345-4) : appliqué.** Le critère du II vise désormais un « accord de branche agréé avant la suppression de l'agrément ». Une phrase précise qu'un accord de branche sans agrément ne ferme pas la voie de la décision unilatérale. La faveur des entreprises de moins de 50 salariés n'est ni restreinte ni étendue.
12. **CGI 1586 (variante B05t), 1635 quater A, L et M (relevé sur urba R113-18 et L113-10) : appliqué.**
    - La part départementale de la taxe d'aménagement est retirée pour les faits générateurs postérieurs à la loi qui abroge L113-10 :
      - les départements sont retirés du 2° du I de 1635 quater A, et un IV porte la transition ;
      - le II de 1635 quater L, le II de 1635 quater M et le II de 1586 sont bornés à ces faits générateurs.
    - Sont conservés : les faits générateurs antérieurs, les substitutions de Lyon et de Paris pour ces faits, et les autres parts.
    - La baisse est comptée une seule fois, à L113-10.
    - Les mentions des départements dans les régimes d'exonération (1635 quater D et E, 1639 A bis) ne sont pas modifiées : elles sont sans effet nuisible.

## Ce qui n'a pas été fait

- Aucune réécriture de style. Aucune formalité ni sanction de remplacement.
- Pièces hors corpus : CIBS, CGCT, arrêtés et spécifications techniques.

Revue IA : rien de ceci ne vaut validation par un juriste.
