# Y15tdc — variante du groupe Y15 créée par T081 (palier A)

## TIERA-T081-01 — annexe II 242 sexies (LEGIARTI000049826459) : appliquée
- Défaut G (F3, F5). La proposition de l'article 287 est rédigée sur la version LEGIARTI000051190827 (1er janvier 2027). Dans cette version, le 3 désigne le dépôt trimestriel, et le texte « ne rétablit aucune disposition abrogée par l'article 38 [...] notamment le régime simplifié annuel et ses acomptes semestriels ». L'article 242 sexies proposé rattachait encore les acomptes de juillet et de décembre à « la déclaration mentionnée au 3 de l'article 287 ». Il maintenait aussi ces acomptes jusqu'à l'entrée en vigueur de la réforme, donc pour 2027.
- Correction (mode `replace`, texte complet) :
  - le renvoi vise désormais le 3 de l'article 287 « dans sa rédaction en vigueur avant le 1er janvier 2027 » ;
  - les acomptes ne sont plus déterminés que pour les opérations dont la taxe est devenue exigible avant le 1er janvier 2027 ;
  - aucun acompte n'est dû pour les opérations postérieures ;
  - sont conservés : la suppression des acomptes à compter de la réforme, la dispense de relevé, le relevé qui vaut demande de remboursement (242-0 C, III et 242 septies J) et la déclaration annuelle.
  - Il n'y a aucune formalité, condition ni sanction nouvelle. Le motif et les notes sont complétés.
- Contrôle : `python3 -B apply/check_changes.py Y15tdc` renvoie `problems` vide. Les diagnostics sont une réduction normative déjà déclarée et un changement de longueur voulu.
- Points pour l'auteur : la coordination du III de 242-0 C est demandée au groupe Y15 (TIERA-T081-02). Le bilan d'impact (dispense de relevé) n'a plus d'effet pratique après 2027. La reprise CIBS est hors corpus.

Revue IA : ce n'est pas une validation par un juriste.
