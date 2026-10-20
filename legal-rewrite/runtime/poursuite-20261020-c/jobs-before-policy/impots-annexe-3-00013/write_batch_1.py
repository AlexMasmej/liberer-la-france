import json
from pathlib import Path
items = {}
def add(i, xml, reason, notes):
    Path(f'fragments/{i:02d}.xml').write_text(xml.strip()+'\n')
    items[str(i)] = {'reason': reason, 'review_notes': notes}

add(0, '''
<p>Le logement doit être destiné, en dernier lieu, à une location non meublée à usage de résidence principale. Le loyer doit être normal au regard des loyers habituellement pratiqués dans le voisinage pour des logements comparables.</p>
''',
"Réécriture à droit constant : le logement est désigné comme objet de l'obligation d'affectation et le critère de normalité du loyer est formulé directement, sans modifier la comparaison avec les logements du voisinage. Aucune réforme de fond de ce régime n'est définie dans le cadrage.",
"Maintien de la destination finale en location non meublée et du critère de résidence principale. Le contexte historique ressort de l'article 46 AG sexies du corpus, qui vise les investissements réalisés jusqu'au 31 décembre 2000 ; aucune extension aux investissements nouveaux n'est introduite.")

add(1, '''
<p>Les contribuables qui bénéficient de la réduction d'impôt prévue au troisième alinéa du 4 de l'article 199 undecies du code général des impôts joignent à leur déclaration de revenus de l'année au titre de laquelle ils demandent cette réduction :</p>
<p>1. Un engagement de louer le logement non meublé à usage de résidence principale, dans le délai et pour la durée prévus au 1 de l'article 199 undecies du code général des impôts ;</p>
<p>2. Une copie du bail ;</p>
<p>3. Une note indiquant les éléments suivants :</p>
<p>L'identité et l'adresse du contribuable ;</p>
<p>L'adresse et la surface du logement concerné ;</p>
<p>Le prix de revient ou d'acquisition du logement, accompagné des justificatifs ;</p>
<p>La date d'achèvement du logement ou, si elle est postérieure, la date de son acquisition ;</p>
<p>Le nom du sous-locataire ainsi que le nom et l'adresse de son employeur.</p>
<p>Si le bail n'est pas signé à la date de souscription de cette déclaration, le contribuable joint les documents mentionnés aux 2 et 3 à sa déclaration de revenus de l'année au cours de laquelle le bail est signé.</p>
<p>La même obligation s'applique en cas de changement de locataire ou de sous-locataire pendant la durée de l'engagement prévu au 1 de l'article 199 undecies du même code.</p>
''',
"Réécriture à droit constant : les pièces à joindre, les informations de la note et le report de leur production en l'absence de bail sont exprimés avec un sujet explicite. Les numéros 1 à 3 et les alinéas de la liste sont conservés. Aucune modification de fond n'est apportée.",
"Le renvoi à l'article 199 undecies, absent du corpus courant fourni, est historique et demeure inchangé ; l'article 46 AG sexies rattache ce dispositif aux investissements réalisés jusqu'au 31 décembre 2000. Le report concerne bien les documents des 2 et 3, et non l'engagement du 1. Maintien de la nouvelle production en cas de changement de locataire ou de sous-locataire.")

add(2, '''
<p>Lorsque le logement est construit par une société, son gérant accomplit les obligations déclaratives prévues à l'article 46 AG octies.</p>
<p>Il adresse les documents, avec la déclaration d'achèvement, dans les six mois suivant l'achèvement du logement, à la direction départementale ou, le cas échéant, régionale des finances publiques auprès de laquelle la société souscrit ses déclarations de résultats.</p>
<p>Le gérant remet aux souscripteurs de titres, en double exemplaire, un document attestant que la location et la sous-location remplissent les conditions fixées aux articles 46 AG sexies à 46 AG nonies. Chaque souscripteur joint un exemplaire de ce document à sa déclaration de revenus de l'année au titre de laquelle le bail est signé.</p>
''',
"Réécriture à droit constant : les obligations du gérant et celles des souscripteurs sont distinguées par des sujets explicites. La phrase relative à l'attestation est scindée, tout en conservant les trois alinéas et l'ensemble des modalités de transmission. Aucune réforme de fond.",
"Contrôle du délai de six mois à compter de l'achèvement, de la déclaration d'achèvement jointe et du double exemplaire. Les renvois aux articles 46 AG sexies à 46 AG nonies sont maintenus dans leur champ historique, sans extension du régime ancien.")

add(3, '''
<p>Pour l'application du troisième alinéa du 7 de l'article 199 undecies A du code général des impôts, le personnel des organismes publics ou privés qui peut sous-louer le logement comprend les personnes employées par ces organismes dont les rémunérations principales relèvent des traitements et salaires au sens de l'article 79 du même code. En sont exclus :</p>
<p>a) Le propriétaire du logement, son conjoint, les membres de son foyer fiscal ainsi que ses ascendants ou descendants ;</p>
<p>b) Les conjoints, les membres du foyer fiscal ainsi que les descendants ou ascendants des associés des sociétés mentionnées à l'article 8 du même code.</p>
''',
"Réécriture à droit constant : la définition du personnel sous-locataire est séparée de l'annonce des exclusions. Les catégories exclues restent réparties sous les lettres a et b, sans changement de leur portée. Aucune réforme de fond.",
"Le troisième alinéa du 7 de l'article 199 undecies A du corpus vise bien la location à un organisme pour loger son personnel. Les exclusions des a et b demeurent distinctes ; les associés ne sont pas ajoutés à la liste du b, qui vise leurs proches et les membres de leur foyer fiscal.")

add(4, '''
<p>Pour l'application du 2° du 6 de l'article 199 undecies A du code général des impôts, les plafonds de loyer et de ressources du locataire sont fixés comme suit :</p>
<p>1. Pour les baux conclus en 2026, les plafonds annuels de loyer, hors charges, sont fixés, par mètre carré de surface habitable, à :</p>
<p>1° 211 € dans les départements d'outre-mer, à Saint-Barthélemy et à Saint-Martin. Ce plafond est révisé le 1er janvier de chaque année, selon la plus forte variation de la moyenne annuelle des indices des prix à la consommation hors tabac constatée parmi les cinq départements d'outre-mer ;</p>
<p>2° 249 € en Polynésie française, dans les îles Wallis et Futuna et les Terres australes et antarctiques françaises, à Saint-Pierre-et-Miquelon et en Nouvelle-Calédonie. Ce plafond est révisé le 1er janvier de chaque année, selon la plus forte variation de la moyenne annuelle des indices des prix à la consommation constatée entre la Polynésie française et la Nouvelle-Calédonie.</p>
<p>1 bis. Pour calculer les plafonds mentionnés au 1, la variation retenue est :</p>
<p>1° Dans les départements d'outre-mer, à Saint-Barthélemy et à Saint-Martin, la dernière variation annuelle publiée par l'Institut national de la statistique et des études économiques au 1er décembre de l'année précédant celle de la conclusion du bail ;</p>
<p>2° En Polynésie française, dans les îles Wallis et Futuna et les Terres australes et antarctiques françaises et à Saint-Pierre-et-Miquelon, la dernière variation annuelle publiée par l'Institut de la statistique de la Polynésie française au 1er décembre de l'année précédant celle de la conclusion du bail ;</p>
<p>3° En Nouvelle-Calédonie, la dernière variation annuelle publiée par l'Institut territorial de la statistique et des études économiques au 1er décembre de l'année précédant celle de la conclusion du bail.</p>
<p>2. Les ressources du locataire correspondent aux revenus nets de frais professionnels figurant sur son avis d'imposition établi au titre des revenus de l'année précédant celle de la conclusion du bail ou, à défaut, de l'année antérieure.</p>
<p>Pour les baux conclus en 2026, les plafonds annuels de ressources sont fixés comme suit :</p>
<table><thead><tr><th rowspan="2">Composition du foyer du locataire</th><th colspan="2">Plafond annuel de ressources (en €)</th></tr><tr><th>Départements d'outre-mer, Saint-Barthélemy et Saint-Martin</th><th>Polynésie française, Nouvelle-Calédonie, îles Wallis et Futuna, Terres australes et antarctiques françaises et Saint-Pierre-et-Miquelon</th></tr></thead><tbody><tr><td>Personne seule</td><td>38 313</td><td>35 228</td></tr><tr><td>Couple</td><td>70 849</td><td>65 148</td></tr><tr><td>Personne seule ou couple ayant une personne à charge</td><td>74 946</td><td>68 913</td></tr><tr><td>Personne seule ou couple ayant deux personnes à charge</td><td>79 045</td><td>72 683</td></tr><tr><td>Personne seule ou couple ayant trois personnes à charge</td><td>84 519</td><td>77 714</td></tr><tr><td>Personne seule ou couple ayant quatre personnes à charge</td><td>89 995</td><td>82 750</td></tr><tr><td>Majoration par personne à charge à partir de la cinquième</td><td>+ 5 757</td><td>+ 5 293</td></tr></tbody></table>
<p>Ces plafonds sont relevés chaque année selon les modalités prévues au 1.</p>
<p>Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du code général des impôts.</p>
<p>3. Dans le cas prévu au troisième alinéa du 7 de l'article 199 undecies A du code général des impôts, le respect des conditions des 1 et 2 s'apprécie au regard :</p>
<p>a) Du montant du loyer payé au bailleur par l'organisme locataire ;</p>
<p>b) Du montant du loyer payé à cet organisme par le sous-locataire ;</p>
<p>c) Du montant des ressources du sous-locataire.</p>
''',
"Réécriture à droit constant : les règles de révision et de détermination des ressources sont formulées directement. Le tableau est intégralement restitué, avec une ligne par composition de foyer afin de rendre explicite la correspondance entre chaque catégorie et ses deux plafonds. Les subdivisions 1, 1 bis, 2 et 3 sont conservées. Aucune réforme de fond ni actualisation chiffrée autonome.",
"Tous les montants de 2026 sont conservés : loyers de 211 € et 249 €, quatorze valeurs du tableau, dont les majorations de 5 757 € et 5 293 €. La distinction entre indices hors tabac des cinq départements et indices de Polynésie française/Nouvelle-Calédonie est maintenue, comme les trois sources statistiques du 1 bis et la date du 1er décembre. La source combine, au 1, le maximum de variations entre territoires et, au 1 bis, des publications territorialisées : articulation conservée sans la corriger implicitement. La note source cite l'article 1er du décret n° 2001-137 du 31 décembre 2001 ; cette référence historique, dont le couple numéro/date appelle vérification, n'est ni une date de réforme future ni une base pour changer les chiffres. Les plafonds peuvent concerner des opérations anciennes ; aucune réouverture du champ légal de l'article 199 undecies A n'est créée.")

add(5, '''
<p>I. – La surface retenue pour l'application du a du 2 et du 5 de l'article 199 undecies A, du sixième alinéa du I de l'article 217 undecies du code général des impôts et du 1 de l'article 46 AG duodecies est celle définie au III du présent article.</p>
<p>II. – Pour l'application du a du 2 de l'article 199 undecies A du code général des impôts, la limite de surface habitable dépend du nombre de personnes destinées à occuper le logement à titre principal, selon le tableau suivant :</p>
<table><thead><tr><th>Nombre de personnes destinées à occuper le logement à titre principal</th><th>Limite de surface habitable (en m²)</th></tr></thead><tbody><tr><td>Personne seule</td><td>65</td></tr><tr><td>Couple</td><td>77,5</td></tr><tr><td>Personne seule ou couple ayant une personne à charge</td><td>90</td></tr><tr><td>Majoration par personne à charge supplémentaire, dans la limite de cinq personnes</td><td>12</td></tr></tbody></table>
<p>Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du code général des impôts.</p>
<p>III. – La surface retenue est la surface habitable définie à l'article R. 156-1 du code de la construction et de l'habitation. La surface des varangues est toutefois prise en compte, dans la limite de 14 mètres carrés.</p>
''',
"Réécriture à droit constant : le I rassemble les renvois sans en modifier l'objet, le II annonce directement la règle de surface et le III exprime clairement l'inclusion limitée des varangues. Le tableau et toutes ses valeurs sont maintenus. Aucune réforme de fond.",
"Valeurs conservées : 65 m², 77,5 m², 90 m², majoration de 12 m² et limite de 14 m² pour les varangues. La formule source « dans la limite de cinq personnes » est conservée dans le tableau : elle ne précise pas expressément si ce décompte vise les seules personnes supplémentaires ou l'ensemble des personnes à charge ; aucune interprétation nouvelle n'est imposée. Le renvoi à R. 156-1 a été vérifié dans le corpus et concerne bien la définition de la surface habitable. Les autres renvois et leur champ historique demeurent inchangés.")

add(6, '''
<p>Pour l'application du e du 2 de l'article 199 undecies A du code général des impôts, constituent des travaux de réhabilitation des logements les travaux de modification ou de remise en état du gros œuvre ainsi que les travaux d'aménagement interne qui, par leur nature, équivalent à une reconstruction. Les travaux d'amélioration indissociables de ces travaux sont également compris dans les travaux de réhabilitation.</p>
''',
"Réécriture à droit constant : la définition est répartie en deux phrases, la seconde maintenant expressément les travaux d'amélioration indissociables. La qualification de reconstruction reste attachée aux travaux d'aménagement interne. Aucune réforme de fond.",
"Les trois composantes de la définition sont conservées : modification ou remise en état du gros œuvre, aménagement interne équivalant par nature à une reconstruction et améliorations indissociables. Le dispositif de rénovation locative de vingt-quatre mois décrit par policy.json relève d'un autre champ et appelle notamment la loi n° 89-462 et les textes procéduraux ; il n'est pas introduit dans cette définition fiscale.")

Path('metadata_1.json').write_text(json.dumps(items, ensure_ascii=False, indent=2)+'\n')
