# Y15tde — variante du groupe Y15 créée par T083 (palier A)

## TIERA-T083-01 : annexe II 242-0 C (LEGIARTI000030066036), appliquée
- **Défaut G (F3).** La proposition de l'article 287 est rédigée sur la version LEGIARTI000051190827 (1er janvier 2027) :
  - son 3 est le dépôt trimestriel sous 1 000 000 € / 1 100 000 € ;
  - elle « ne rétablit aucune disposition abrogée par l'article 38 [...] notamment le régime simplifié annuel et ses acomptes semestriels ».

  Le III de 242-0 C réservait pourtant le remboursement intermédiaire aux « assujettis placés sous le régime d'acomptes prévu au 3 de l'article 287 ». Le renvoi ne désignait donc plus rien, alors que le 8 de 287 proposé déclare ce remboursement « ouvert pour ces exercices ».
- **Correction** (mode `replace`, texte complet) :
  - le III vise désormais le 3 de 287 « dans sa rédaction en vigueur avant le 1er janvier 2027, pour les périodes et exercices qui demeurent régis par ce régime en application du 8 du même article » ;
  - tout le reste est inchangé : I, II, II bis, la deuxième phrase du III (relevé sans acompte), le renvoi à 242 septies J et la transition du IV ;
  - le motif et les notes sont complétés.
- **Bilan d'impact :** les citations sont inchangées et toujours exactes. Le validateur l'accepte sans modification.
- **Origine :** la correction exécute la demande TIERA-T081-02, adressée au groupe Y15. Elle est coordonnée avec la variante Y15tdc (242 sexies).
- **Contrôle :** `python3 -B apply/check_changes.py Y15tde` renvoie `problems` vide. Le diagnostic porte seulement sur la réduction normative déjà déclarée.
- **Points pour l'auteur :**
  - la transition de 242 septies J affirme encore que les montants minimaux « demeurent inchangés » (défaut mineur hors lot) ;
  - la reprise des dispositions par le CIBS est hors corpus.

Revue IA : ce n'est pas une validation par un juriste.
