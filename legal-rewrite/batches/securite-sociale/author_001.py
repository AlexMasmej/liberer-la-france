"""Authored full drafts after reading CSS opening articles and official notes."""
from pathlib import Path
import html,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
source=json.loads((ROOT/'sites/liberer-la-retraite/dist/corpus/securite-sociale.json').read_text())
by_number={a['number']:a for a in source}
drafts=[]
def add(number,paragraphs,reason,review):
 a=by_number[number]
 drafts.append({k:a[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':''.join('<p>'+html.escape(p)+'</p>' for p in paragraphs),'reason':reason,'review_notes':review})

add('L111-1',[
'La sécurité sociale repose sur la solidarité nationale.',
'Toute personne qui travaille en France ou qui y réside de manière stable et régulière bénéficie, dans les conditions prévues par le présent code, de la couverture des charges de maladie, de maternité, de paternité, de famille et d’autonomie.',
'Les travailleurs sont garantis contre les risques de toute nature susceptibles de réduire ou de supprimer leurs revenus. Cette garantie résulte de leur affiliation à un ou plusieurs régimes obligatoires.',
'La sécurité sociale prend en charge les frais de santé et le soutien à l’autonomie. Elle verse les prestations d’assurance sociale, notamment les allocations vieillesse, les prestations d’accidents du travail et de maladies professionnelles et les prestations familiales.',
'Ces garanties et prestations sont mises en œuvre dans le cadre du présent code, sous réserve des conventions internationales et des règlements européens.'
], 'Réécriture intégrale : les bénéficiaires, la garantie de revenus, les prestations et la réserve internationale sont distingués, sans suppression d’un risque couvert.', 'Comparer la portée territoriale du travail en France et de la résidence avec L. 111-2 et L. 111-2-2 ; vérifier le maintien de la portée de la réserve internationale pour toutes les prestations.')

add('L111-2',[
'Le présent code s’applique en France métropolitaine. Il s’applique également, sous les réserves qu’il prévoit, en Guadeloupe, en Guyane, en Martinique, à La Réunion, à Saint-Barthélemy et à Saint-Martin.',
'À Saint-Pierre-et-Miquelon, les dispositions suivantes s’appliquent dans les conditions prévues au titre V bis du livre VII :',
'1° Les titres Ier, II et V du livre Ier ;',
'2° La sous-section 1 de la section 1 du chapitre Ier et le chapitre 8 bis du titre VI du livre Ier ;',
'3° Les titres Ier à IV du livre VIII ;',
'4° Pour la couverture des charges mentionnées au deuxième alinéa de l’article L. 111-1 : le chapitre préliminaire du titre VI du livre Ier, le chapitre 3 bis du titre II du livre II et le livre V.',
'La loi peut étendre l’organisation de la sécurité sociale à de nouvelles catégories de bénéficiaires et à des risques ou prestations que le présent code ne prévoit pas.',
'Les professions agricoles et forestières demeurent soumises au régime résultant de leur statut actuel.'
], 'Réécriture intégrale du champ territorial avec énumération distincte des dispositions applicables à Saint-Pierre-et-Miquelon ; maintien de la compétence législative et de la réserve agricole.', 'Conserver la note d’entrée en vigueur du 23 juillet 2026. Contrôler séparément chaque renvoi territorial et les adaptations ultramarines ; la numérotation des alinéas de L. 111-1 reste inchangée pour la couverture visée.')

add('L111-2-1',[
'I. — La Nation garantit une prise en charge des frais de santé universelle, obligatoire et solidaire par la sécurité sociale.',
'Chacun est protégé contre le risque et les conséquences de la maladie, quels que soient son âge et son état de santé. Chacun finance cette protection en fonction de ses ressources.',
'L’État définit les objectifs de la politique de santé publique et garantit aux assurés un accès effectif aux soins sur tout le territoire.',
'Les organismes gestionnaires des régimes d’assurance maladie participent à la mise en œuvre de la politique nationale de santé définie par l’État, dans les conditions prévues à l’article L. 1411-2 du code de la santé publique. Ils agissent en partenariat avec les organisations représentatives des professionnels de santé et avec les associations agréées en application de l’article L. 1114-1 du même code.',
'Chacun contribue au bon usage des ressources que la Nation consacre à l’assurance maladie.',
'II. — Le système de retraite associe un socle obligatoire et solidaire par répartition, un étage de capitalisation collective obligatoire constitué progressivement par redéploiement de cotisations vieillesse existantes et une épargne supplémentaire libre.',
'La répartition finance les pensions liquidées et les droits constitués dans les régimes d’origine. Les pensions servies par ces régimes restent en rapport avec les revenus tirés de l’activité. La fraction de cotisations transférée à la capitalisation ouvre des droits sur un compte personnel et ne crée pas simultanément les mêmes droits futurs par répartition.',
'Les assurés bénéficient d’un traitement équitable quant à la durée de leur retraite et au montant de leur pension, quels que soient leur sexe, leurs activités et parcours professionnels, leur espérance de vie en bonne santé, leurs régimes et leur génération.',
'La solidarité s’exerce entre les générations et au sein de chaque génération. Elle comprend l’égalité entre les femmes et les hommes, la prise en compte des périodes de privation involontaire d’emploi, totale ou partielle, et la garantie d’un niveau de vie satisfaisant pour les retraités. Les objectifs sont de réduire de moitié, en 2037, l’écart entre les pensions des femmes et des hommes constaté en 2023 et de le supprimer en 2050.',
'Le financement repose sur des contributions équitablement réparties entre les générations, les niveaux de revenus et les revenus du travail et du capital. La recherche du plein emploi y contribue. Le transfert de cotisations vers la capitalisation est subordonné au financement des pensions et des droits maintenus, des mécanismes de solidarité et des coûts de transition. Aucun rendement futur n’est réputé financer une dépense présente.',
'La loi fixe les étapes, les taux, les garanties de gestion, les abondements de solidarité et les conditions de sortie des comptes collectifs. Le capital de marché et son rendement ne bénéficient d’aucune garantie générale implicite de l’État.',
'III. — La Nation garantit une prise en charge universelle et solidaire du soutien à l’autonomie par la sécurité sociale. Chacun est protégé contre la perte d’autonomie et bénéficie du soutien nécessaire, quels que soient son âge et son état de santé.'
], 'Réécriture intégrale des trois volets. Changement de fond explicite au II : architecture à trois étages, redéploiement progressif vers la capitalisation et financement de la transition, conformément à l’orientation retraite définie. Les droits constitués, l’équité et les objectifs d’égalité 2037/2050 sont maintenus.', 'Nécessite les dispositions opérationnelles du compte collectif, le raccordement des régimes complémentaires et des autres codes, les règles de réduction des droits futurs et une évaluation constitutionnelle et financière. La note d’application source de septembre 2023 concerne l’ancienne rédaction ; elle n’est pas une date d’entrée en vigueur de la proposition. Vérifier que le « socle » ne soit pas interprété comme une réduction immédiate des droits existants.')

add('L111-2-2',[
'Sont affiliées à un régime obligatoire de sécurité sociale régi par le présent code, quel que soit leur lieu de résidence :',
'1° Les personnes qui exercent en France :',
'a) Une activité pour le compte d’un ou plusieurs employeurs, qu’ils disposent ou non d’un établissement en France ;',
'b) Une activité professionnelle non salariée ;',
'2° Les personnes qui exercent une activité professionnelle à l’étranger et auxquelles la législation française de sécurité sociale s’applique en vertu des règlements européens ou des conventions internationales.',
'Ces règles s’appliquent sous réserve des traités et accords internationaux régulièrement ratifiés ou approuvés et des règlements européens.'
], 'Réécriture intégrale conservant les deux catégories et les subdivisions a) et b) du critère territorial ; la réserve internationale est isolée sans modifier son champ.', 'Les renvois externes aux 1° a), 1° b) et 2° conservent leur cible. Ne pas confondre affiliation professionnelle et résidence stable pour la prise en charge de la santé.')

add('L111-2-3',[
'Un décret en Conseil d’État définit comment sont appréciées la stabilité de la résidence et la régularité du séjour mentionnées à l’article L. 111-1.',
'Les règles particulières applicables au service des prestations ou des allocations demeurent applicables.'
], 'Réécriture intégrale en deux alinéas distinguant l’habilitation réglementaire de la réserve des règles de service.', 'Contrôler que « définit comment sont appréciées » n’étende pas le pouvoir réglementaire au-delà des conditions d’appréciation de la source ; conserver le renvoi à L. 111-1.')

add('LO111-3',[
'Constituent des lois de financement de la sécurité sociale les trois catégories de lois suivantes :',
'1° La loi de financement de la sécurité sociale de l’année ;',
'2° La loi de financement rectificative de la sécurité sociale ;',
'3° La loi d’approbation des comptes de la sécurité sociale.'
], 'Réécriture intégrale de la règle de qualification, avec maintien des trois catégories et de leur numérotation.', 'Disposition organique : adoption par loi organique et contrôle constitutionnel requis. Conserver les dispositions transitoires propres au financement de l’année 2023, présentes dans les notes sources.')

add('LO111-3-1',[
'La loi de financement de la sécurité sociale de l’année comporte un article liminaire suivi de trois parties :',
'1° La première partie porte sur l’année en cours ;',
'2° La deuxième partie porte sur les recettes et l’équilibre général de l’année à venir ;',
'3° La troisième partie porte sur les dépenses de l’année à venir.'
], 'Réécriture intégrale de l’architecture de la LFSS annuelle ; maintien de l’article liminaire, des trois parties et de leurs exercices de référence.', 'Disposition organique, distincte d’une loi ordinaire ; contrôler les renvois aux parties dans les autres articles et conserver la note d’entrée en vigueur du 1er septembre 2022.')

add('LO111-3-2',[
'L’article liminaire de la loi de financement de la sécurité sociale de l’année présente les prévisions de dépenses, de recettes et de solde des administrations de sécurité sociale.',
'Ces prévisions sont présentées pour l’exercice en cours et pour l’année à venir.'
], 'Réécriture intégrale séparant les agrégats à présenter des deux exercices couverts.', 'Ne pas réduire le périmètre des administrations de sécurité sociale à celui des seuls régimes obligatoires de base. Exigences organiques et note d’entrée en vigueur conservées.')

add('LO111-3-3',[
'La première partie de la loi de financement de la sécurité sociale de l’année, relative à l’année en cours :',
'1° Rectifie les prévisions de recettes et les tableaux d’équilibre des régimes obligatoires de base, par branche, et des organismes qui concourent à leur financement ;',
'2° Rectifie les objectifs de dépenses de ces régimes, par branche, l’objectif national de dépenses d’assurance maladie de l’ensemble des régimes obligatoires de base et leurs sous-objectifs approuvés par la précédente loi de financement de la sécurité sociale ;',
'3° Rectifie l’objectif assigné aux organismes chargés de l’amortissement de la dette de ces régimes et des organismes qui concourent à leur financement, ainsi que les prévisions de recettes affectées à la mise en réserve à leur profit.'
], 'Réécriture intégrale des trois catégories de rectifications pour l’année en cours, avec identification de la première partie par concordance avec LO 111-3-1.', 'Vérifier que les sous-objectifs restent rattachés à tous les objectifs auxquels la source les rattache et le maintien de la distinction entre prévisions d’affectation à la réserve et réserve effectivement constituée. Loi organique requise.')

add('LO111-3-4',[
'La deuxième partie de la loi de financement de la sécurité sociale de l’année, relative aux recettes et à l’équilibre général de l’année à venir :',
'1° Approuve le rapport prévu à l’article LO 111-4 ;',
'2° Détermine sincèrement les conditions générales de l’équilibre financier de la sécurité sociale pour l’année à venir. Elle tient notamment compte des conditions économiques générales et de leur évolution prévisible. Elle définit cet équilibre au regard des données économiques, sociales et financières du rapport prévu à l’article 50 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances.',
'À cette fin, elle :',
'a) Prévoit les recettes de l’ensemble des régimes obligatoires de base, par branche, et celles des organismes qui concourent à leur financement ;',
'b) Détermine l’objectif d’amortissement de la dette pour l’année à venir des organismes chargés de l’amortissement de la dette des régimes obligatoires de base et des organismes concourant à leur financement. Elle prévoit aussi, par catégorie, les recettes affectées aux organismes chargés de la mise en réserve de recettes à leur profit ;',
'c) Approuve le montant de la compensation mentionnée à l’annexe prévue au 2° de l’article LO 111-4-1 du présent code ;',
'd) Présente l’équilibre financier dans des tableaux d’équilibre pour l’ensemble des régimes obligatoires de base, par branche, et pour les organismes qui concourent à leur financement ;',
'e) Fixe la liste des régimes obligatoires de base et des organismes qui concourent à leur financement autorisés à recourir à des ressources non permanentes. Elle fixe les limites dans lesquelles ces ressources peuvent couvrir leurs besoins de trésorerie.'
], 'Réécriture intégrale de la partie recettes et équilibre : maintien des deux compétences principales, des cinq opérations financières et des renvois organiques.', 'Contrôler particulièrement le rattachement de l’amortissement aux organismes concourant au financement et la réserve de recettes. Aucun financement automatique de la transition retraite n’est créé par cet article organique. Les nouveaux besoins devront apparaître dans les tableaux et rapports correspondants.')

add('LO111-3-5',[
'La troisième partie de la loi de financement de la sécurité sociale de l’année, relative aux dépenses de l’année à venir :',
'1° Fixe les charges prévisionnelles des organismes qui concourent au financement des régimes obligatoires de base ;',
'2° Fixe les objectifs de dépenses de l’ensemble de ces régimes, par branche, et, le cas échéant, leurs sous-objectifs. Le Gouvernement fixe la liste et le périmètre de ces sous-objectifs après consultation des commissions parlementaires saisies au fond des projets de loi de financement de la sécurité sociale ;',
'3° Fixe l’objectif national de dépenses d’assurance maladie de l’ensemble des régimes obligatoires de base et ses sous-objectifs. Le Gouvernement a l’initiative de la définition des composantes des sous-objectifs. Les commissions parlementaires saisies au fond des projets de loi de financement de la sécurité sociale sont consultées sur leur liste et la définition de leurs composantes. Il existe au moins trois sous-objectifs.'
], 'Réécriture intégrale distinguant charges, objectifs par branche et ONDAM, sans déplacer les compétences gouvernementales ni les consultations parlementaires.', 'Conserver le minimum de trois sous-objectifs de l’ONDAM et distinguer cette règle des sous-objectifs éventuels par branche du 2°. Disposition organique ; note d’entrée en vigueur conservée.')

add('LO111-3-6',[
'La première partie de la loi de financement de la sécurité sociale de l’année, relative à l’année en cours, peut comprendre :',
'1° Les dispositions qui ont un effet sur les recettes des régimes obligatoires de base ou des organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ;',
'2° Les dispositions relatives à l’affectation de ces recettes, sous réserve du III de l’article 2 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances ;',
'3° Les dispositions qui ont un effet sur les dépenses de ces régimes ou organismes ;',
'4° Les dispositions qui ont un effet sur les dettes suivantes, si elles modifient les conditions générales de l’équilibre financier de la sécurité sociale :',
'a) La dette des établissements de santé relevant du service public hospitalier ;',
'b) La dette des établissements médico-sociaux publics et privés à but non lucratif, financés en tout ou partie par les régimes obligatoires de base de sécurité sociale et soumis à un objectif de dépenses ;',
'5° Les dispositions qui améliorent l’information et le contrôle du Parlement sur l’application des lois de financement de la sécurité sociale.'
], 'Réécriture intégrale du domaine facultatif de la première partie, en explicitant le caractère cumulatif de la condition d’équilibre et des catégories de dettes du 4°.', 'Ne pas étendre la condition de modification de l’équilibre aux 1° à 3° et 5°. Préserver toutes les conditions concernant les établissements médico-sociaux et la réserve de la LOLF. Loi organique requise.')

add('LO111-3-7',[
'La deuxième partie de la loi de financement de la sécurité sociale de l’année, relative aux recettes et à l’équilibre général de l’année à venir, peut comprendre les dispositions suivantes :',
'1° Les dispositions qui ont un effet sur les recettes des régimes obligatoires de base ou des organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit, ainsi que les dispositions relatives à l’affectation de ces recettes, sous réserve du III de l’article 2 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances. Ces dispositions s’appliquent :',
'a) À l’année ;',
'b) À l’année et aux années ultérieures ;',
'c) Aux seules années ultérieures, à condition de présenter un caractère permanent ;',
'2° Les dispositions relatives à l’assiette, au taux et aux modalités de recouvrement des cotisations et contributions affectées aux régimes obligatoires de base ou aux organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ;',
'3° Les dispositions relatives à la trésorerie et à la comptabilité de ces régimes ou organismes ;',
'4° Les dispositions qui ont un effet sur la dette des régimes obligatoires de base, son amortissement et ses conditions de financement ;',
'5° Les dispositions relatives à la mise en réserve de recettes au profit des régimes obligatoires de base et à l’utilisation de ces réserves ;',
'6° Les dispositions qui améliorent l’information et le contrôle du Parlement sur l’application des lois de financement de la sécurité sociale.'
], 'Réécriture intégrale des six catégories du domaine facultatif de la partie recettes, avec maintien des trois périodes d’application au seul 1°.', 'Le renvoi « ces régimes ou organismes » du 3° inclut financement, amortissement et réserve définis au 2°. Vérifier l’absence d’élargissement temporel aux mesures seulement futures non permanentes. Loi organique requise.')

add('LO111-3-8',[
'La troisième partie de la loi de financement de la sécurité sociale de l’année, relative aux dépenses de l’année à venir, peut comprendre :',
'1° Les dispositions qui ont un effet sur les dépenses des régimes obligatoires de base, ou sur celles des organismes concourant à leur financement lorsqu’elles affectent directement l’équilibre financier de ces régimes. Elles sont applicables :',
'a) À l’année ;',
'b) À l’année et aux années ultérieures ;',
'c) Aux seules années ultérieures, si elles présentent un caractère permanent ;',
'2° Les dispositions qui modifient les règles de gestion des risques par les régimes obligatoires de base ou les règles d’organisation ou de gestion interne de ces régimes et des organismes concourant à leur financement, si elles ont pour objet ou pour effet de modifier les conditions générales de l’équilibre financier de la sécurité sociale ;',
'3° Les dispositions qui ont un effet sur les dettes suivantes, si elles modifient les conditions générales de l’équilibre financier de la sécurité sociale :',
'a) La dette des établissements de santé relevant du service public hospitalier ;',
'b) La dette des établissements médico-sociaux publics et privés à but non lucratif, financés en tout ou partie par les régimes obligatoires de base de sécurité sociale et soumis à un objectif de dépenses ;',
'4° Les dispositions qui améliorent l’information et le contrôle du Parlement sur l’application des lois de financement de la sécurité sociale.'
], 'Réécriture intégrale des quatre catégories du domaine facultatif de la partie dépenses, sans supprimer les conditions d’effet sur l’équilibre ni le caractère permanent des seules mesures futures.', 'Contrôler le rattachement de « directement » aux dépenses des organismes concourant au financement, ainsi que la portée temporelle limitée au 1°. Ne pas faire disparaître les conditions cumulatives relatives aux établissements médico-sociaux. Loi organique requise.')

add('LO111-3-9',[
'En cours d’année, les dispositions de la loi de financement de la sécurité sociale de l’année prévues au paragraphe 1 de la sous-section 1 de la présente section ne peuvent être modifiées que par :',
'1° Une loi de financement rectificative ;',
'2° Les dispositions rectificatives de la loi de financement de la sécurité sociale de l’année suivante.'
], 'Réécriture intégrale de l’exclusivité des deux véhicules rectificatifs, sans modification du champ des dispositions concernées.', 'La formule source « en cours d’année » est conservée malgré son articulation délicate avec la loi de l’année suivante ; ne pas la corriger sans décision de fond. Maintenir le renvoi structurel au paragraphe 1. Loi organique requise.')

add('LO111-3-10',[
'La loi de financement rectificative de la sécurité sociale comporte l’article liminaire mentionné à l’article 1er H de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances.',
'Elle comporte en outre deux parties :',
'1° Une première partie relative aux recettes et à l’équilibre général, correspondant à la partie de la loi de financement de la sécurité sociale de l’année consacrée à ces matières ;',
'2° Une seconde partie relative aux dépenses, correspondant à la partie de la loi de financement de la sécurité sociale de l’année consacrée aux dépenses.'
], 'Réécriture intégrale de la structure de la LFSS rectificative ; l’article liminaire reste distinct des deux parties.', 'Conserver le renvoi à l’article 1er H de la LOLF et la correspondance matérielle avec la loi annuelle. Loi organique requise ; note source d’entrée en vigueur conservée.')

add('LO111-3-11',[
'La loi de financement rectificative de la sécurité sociale :',
'1° Rectifie les prévisions de recettes et les tableaux d’équilibre des régimes obligatoires de base, par branche, et des organismes qui concourent à leur financement ;',
'2° Rectifie les objectifs de dépenses des régimes obligatoires de base, par branche, l’objectif national de dépenses d’assurance maladie de l’ensemble de ces régimes et leurs sous-objectifs approuvés par la précédente loi de financement de la sécurité sociale ;',
'3° Rectifie l’objectif assigné aux organismes chargés de l’amortissement de la dette des régimes obligatoires de base et les prévisions de recettes affectées à la mise en réserve à leur profit.'
], 'Réécriture intégrale des trois rectifications imposées à la LFSS rectificative ; distinction conservée entre la dette visée ici et le champ plus large de LO 111-3-3.', 'Ne pas harmoniser artificiellement le 3° avec LO 111-3-3 : la source du présent article vise les régimes obligatoires de base. Contrôler le rattachement des sous-objectifs. Loi organique requise.')

add('LO111-3-12',[
'Pour l’année en cours, la loi de financement rectificative de la sécurité sociale peut comprendre les dispositions suivantes :',
'1° Les dispositions qui ont un effet sur les recettes des régimes obligatoires de base ou des organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ; les dispositions relatives à l’affectation de ces recettes, sous réserve du III de l’article 2 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances ; les dispositions qui ont un effet sur les dépenses de ces régimes ou organismes ;',
'2° Les dispositions relatives à l’assiette, au taux et aux modalités de recouvrement des cotisations et contributions affectées aux régimes obligatoires de base ou aux organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ;',
'3° Les dispositions relatives à la trésorerie et à la comptabilité de ces régimes ou organismes ;',
'4° Les dispositions qui ont un effet sur la dette des régimes obligatoires de base, son amortissement et ses conditions de financement, ainsi que les dispositions relatives à la mise en réserve de recettes au profit de ces régimes et à l’utilisation de ces réserves ;',
'5° Les dispositions qui ont un effet sur les dettes suivantes, si elles modifient les conditions générales de l’équilibre financier de la sécurité sociale :',
'a) La dette des établissements de santé relevant du service public hospitalier ;',
'b) La dette des établissements médico-sociaux publics et privés à but non lucratif, financés en tout ou partie par les régimes obligatoires de base de sécurité sociale et soumis à un objectif de dépenses ;',
'6° Les dispositions qui modifient les règles de gestion des risques par les régimes obligatoires de base ou les règles d’organisation ou de gestion interne de ces régimes et des organismes qui concourent à leur financement, si elles ont pour objet ou pour effet de modifier les conditions générales de l’équilibre financier de la sécurité sociale ;',
'7° Les dispositions qui rectifient la liste des régimes obligatoires de base et des organismes qui concourent à leur financement autorisés à recourir à des ressources non permanentes, ainsi que les limites dans lesquelles ces ressources peuvent couvrir leurs besoins de trésorerie ;',
'8° Les dispositions qui améliorent l’information et le contrôle du Parlement sur l’application des lois de financement de la sécurité sociale.'
], 'Réécriture intégrale du domaine facultatif de la loi rectificative : huit catégories et les deux catégories de dettes restent distinctes ; la réserve de la LOLF est maintenue.', 'Contrôler l’identité des périmètres et des conditions d’effet sur l’équilibre aux 5° et 6° ; « ces régimes ou organismes » au 3° reprend l’ensemble des organismes du 2°. Loi organique requise.')

add('LO111-3-13',[
'La loi d’approbation des comptes de la sécurité sociale :',
'1° Comporte un article liminaire présentant, pour l’année concernée, un tableau de synthèse des recettes, des dépenses et du solde des administrations de sécurité sociale ;',
'2° Approuve les tableaux d’équilibre du dernier exercice clos des régimes obligatoires de base de sécurité sociale, par branche, et des organismes qui concourent à leur financement. Elle approuve également les dépenses constatées pendant cet exercice dans le champ de l’objectif national de dépenses d’assurance maladie ;',
'3° Approuve, pour ce même exercice, les montants des recettes affectées aux organismes chargés de mettre en réserve des recettes au profit des régimes obligatoires de base et des organismes qui concourent à leur financement, ainsi que les montants de l’amortissement de leur dette ;',
'4° Approuve le rapport mentionné au 2° de l’article LO 111-4-4.'
], 'Réécriture intégrale distinguant la synthèse des administrations de sécurité sociale, l’approbation des comptes et dépenses, les réserves et la dette, et le rapport organique.', 'Vérifier le rattachement des montants d’amortissement et l’exercice unique du 3°. Ne pas confondre comptes constatés et prévisions votées. Loi organique requise ; renvoi LO 111-4-4 conservé.')

add('LO111-3-14',[
'Seule une disposition d’une loi de financement de la sécurité sociale de l’année ou rectificative peut affecter, en tout ou partie, à une autre personne morale une recette exclusive des régimes obligatoires de base de sécurité sociale ou des organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit.',
'Lorsqu’une ressource établie au profit de ces régimes et organismes est affectée à une autre personne morale que l’État, cette règle s’applique sous réserve du III de l’article 2 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances.'
], 'Réécriture intégrale de l’exclusivité de la LFSS pour réaffecter une recette sociale, avec un alinéa distinct pour la réserve applicable aux ressources affectées à une personne morale autre que l’État.', 'Différencier « recette exclusive » du premier alinéa et « ressource établie au profit » du second ; ne pas effacer la compétence de la loi de finances résultant de la réserve de la LOLF. Loi organique requise.')

add('LO111-3-15',[
'Les ressources établies au profit de l’État et affectées, dans les conditions du III de l’article 2 de la loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances, aux régimes et organismes de sécurité sociale ne peuvent être réparties entre ces régimes et organismes que par une disposition d’une loi de financement de la sécurité sociale de l’année ou rectificative.',
'Cette répartition concerne les régimes obligatoires de base, le cas échéant leurs branches, ainsi que les organismes qui concourent à leur financement, à l’amortissement de la dette de ces régimes ou des organismes qui concourent à leur financement, ou à la mise en réserve de recettes à leur profit.'
], 'Réécriture intégrale séparant le véhicule de répartition et la liste complète des destinataires ; maintien de l’origine étatique et de l’affectation préalable par la LOLF.', 'L’expression « régimes et organismes de sécurité sociale » du premier alinéa doit être lue exclusivement avec la liste du second ; vérifier qu’elle n’élargit pas le domaine réservé. Loi organique requise.')

add('LO111-3-16',[
'I. — Seule une loi de financement de la sécurité sociale de l’année ou rectificative peut créer ou modifier une réduction ou une exonération de cotisations ou de contributions de sécurité sociale affectées aux régimes obligatoires de base, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit, lorsque cette mesure :',
'1° N’est pas compensée à ces régimes ;',
'2° Ou est instituée pour au moins trois ans et a un effet :',
'a) Sur les recettes des régimes obligatoires de base ou des organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ;',
'b) Sur l’assiette, le taux et les modalités de recouvrement de ces cotisations et contributions.',
'II. — La règle du I s’applique également :',
'1° Aux réductions ou exonérations de contributions affectées aux régimes obligatoires de base de sécurité sociale ou aux organismes qui concourent à leur financement, à l’amortissement de leur dette ou à la mise en réserve de recettes à leur profit ;',
'2° Aux réductions ou abattements de l’assiette de ces cotisations et contributions ;',
'3° Aux modifications des mesures non compensées à la date d’entrée en vigueur de la loi organique n° 2005-881 du 2 août 2005 relative aux lois de financement de la sécurité sociale.'
], 'Réécriture intégrale de l’exclusivité organique applicable aux baisses de prélèvements : maintien des alternatives, du seuil de trois ans, des deux catégories d’effets et des trois extensions du II.', 'Ne pas transformer le seuil de trois ans en condition applicable aux mesures non compensées du I, 1°. Préserver la structure des a) et b) sans trancher par une conjonction nouvelle leur articulation. La baisse de CSG et l’allègement employeur doivent utiliser le véhicule compétent. Loi organique requise.')

add('LO111-3-17',[
'Les régimes et organismes de sécurité sociale tiennent des comptes réguliers et sincères.',
'Ces comptes donnent une image fidèle de leur patrimoine et de leur situation financière.'
], 'Réécriture intégrale en deux obligations distinctes : régularité et sincérité, puis image fidèle du patrimoine et de la situation financière.', 'Maintenir les trois exigences comptables et le périmètre de tous les régimes et organismes de sécurité sociale ; loi organique requise.')

add('LO111-3-18',[
'La loi de financement de la sécurité sociale suivante prend en compte, dans ses prévisions de recettes et ses objectifs de dépenses, les conséquences de chaque disposition législative ou réglementaire susceptible d’affecter les recettes ou les dépenses :',
'1° Des régimes obligatoires de base de sécurité sociale ;',
'2° Des organismes qui concourent à leur financement ;',
'3° Des organismes chargés de l’amortissement de la dette de ces régimes.'
], 'Réécriture intégrale de l’obligation de répercuter chaque mesure sur la LFSS suivante, avec une liste distincte des trois catégories concernées.', 'Le critère reste la susceptibilité d’un effet, sans seuil de montant ni exigence d’effet déjà réalisé. Conserver l’obligation individualisée pour chaque disposition ; loi organique requise.')

(HERE/'001.json').write_text(json.dumps(drafts,ensure_ascii=False,indent=2))
print(len(drafts),'authored full drafts, CSS opening articles.')
