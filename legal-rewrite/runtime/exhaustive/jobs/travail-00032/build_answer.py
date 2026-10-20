import json
from pathlib import Path


DRAFTS = {
    "L2145-9": (
        """<p>Les demandeurs d'emploi peuvent suivre des stages de formation économique, sociale et environnementale et de formation syndicale, dans les limites de douze et de dix-huit jours par période annuelle prévues pour les salariés, selon le cas.</p>
<p>Pendant ces stages, les travailleurs privés d'emploi conservent le bénéfice du revenu de remplacement auquel ils ont droit.</p>""",
        "Réécriture à droit constant : la première phrase rattache directement la participation aux limites annuelles applicables ; la seconde place au premier plan le maintien du revenu de remplacement pendant le stage. Aucune réforme de fond n'est appliquée à ce droit de formation.",
        "Les limites de douze et de dix-huit jours sont conservées. Le renvoi matériel aux durées prévues pour les salariés est maintenu ; L. 2145-7, consulté dans le corpus public, distingue le plafond ordinaire et celui des animateurs. Le revenu conservé reste celui auquel le travailleur a droit, sans création d'une prestation nouvelle.",
    ),
    "L2145-10": (
        """<p>Les congés de formation économique, sociale et environnementale et de formation syndicale ne réduisent pas la durée du congé payé annuel.</p>
<p>La durée de ces congés est assimilée à du travail effectif pour déterminer la durée des congés payés, les droits aux prestations d'assurances sociales et aux prestations familiales, ainsi que l'ensemble des autres droits que l'intéressé tient de son contrat de travail.</p>""",
        "Réécriture à droit constant : l'interdiction d'imputer ces congés sur le congé annuel est formulée directement et les droits couverts par l'assimilation au travail effectif sont explicités dans le même alinéa. Aucune réforme de fond.",
        "Les deux alinéas sont conservés. L'assimilation couvre les congés payés, les prestations d'assurances sociales, les prestations familiales et tous les autres droits issus du contrat ; elle n'est pas limitée à l'ancienneté ou à un seul de ces droits.",
    ),
    "L2145-11": (
        """<p>Le salarié a droit au congé de formation économique, sociale et environnementale et de formation syndicale. L'employeur ne peut le refuser que s'il estime, après avis conforme du comité social et économique, que l'absence pourrait porter préjudice à la production et à la bonne marche de l'entreprise.</p>
<p>L'employeur doit motiver son refus.</p>
<p>En cas de différend, ce refus peut être contesté directement devant le bureau de jugement du conseil de prud'hommes, dans les conditions fixées par décret en Conseil d'État.</p>""",
        "Réécriture à droit constant : le droit au congé et l'exception autorisant un refus sont séparés en deux phrases ; l'obligation de motivation est attribuée à l'employeur. Le recours direct et ses conditions réglementaires sont conservés. Aucune réforme de fond.",
        "L'avis du comité social et économique demeure conforme, et non simplement consultatif. Le risque de préjudice reste lié à la production et à la bonne marche de l'entreprise. Les trois alinéas et la saisine directe du bureau de jugement sont maintenus.",
    ),
    "L2145-12": (
        """<p>Les conventions ou accords collectifs de travail peuvent :</p>
<p>1° Prévoir des dispositions plus favorables que celles de la présente sous-section, notamment en matière de rémunération ;</p>
<p>2° Préciser les périodes de congé qui répondent le mieux aux nécessités de chaque profession ;</p>
<p>3° Déterminer les modalités de financement de la formation afin de couvrir les frais pédagogiques et l'indemnisation des frais de déplacement et d'hébergement des stagiaires et des animateurs ;</p>
<p>4° Définir des procédures amiables pour régler les difficultés d'application des dispositions qui précèdent ;</p>
<p>5° Prévoir la création de fonds mutualisés pour assurer la rémunération des congés et le financement de la formation.</p>
<p>Les accords d'établissement peuvent répartir les congés par service ou par catégorie professionnelle.</p>""",
        "Réécriture à droit constant : les cinq facultés de négociation sont présentées dans des alinéas identifiés, avec des formulations directes pour les dépenses couvertes et le règlement amiable. La faculté propre aux accords d'établissement reste distincte. Aucune réforme de fond.",
        "Les 1° à 5° et l'alinéa relatif aux accords d'établissement gardent leur ordre. Anomalie préexistante : le 1° vise la « présente sous-section », alors que le classement fourni et la structure publique du corpus placent l'article dans la section 2 sans sous-section identifiée. Ce renvoi est conservé ; son éventuelle rectification exige une coordination explicite, notamment avec L. 2145-8 qui emploie aussi cette désignation. Les frais de déplacement et d'hébergement couvrent les stagiaires comme les animateurs.",
    ),
    "L2145-13": (
        """<p>Un décret en Conseil d'État détermine les conditions d'application des dispositions relatives au congé de formation économique, sociale et environnementale et de formation syndicale, ainsi que celles applicables au personnel des entreprises publiques énumérées par le décret prévu à l'article L. 2233-1.</p>""",
        "Réécriture à droit constant : le décret en Conseil d'État devient le sujet de la phrase et le champ relatif au personnel des entreprises publiques est distingué dans la même phrase. Aucune réforme de fond ni extension à d'autres personnels.",
        "Le renvoi à L. 2233-1 et le niveau du décret en Conseil d'État sont conservés. Le corpus public de L. 2233-1 a été consulté ; la désignation des entreprises publiques demeure celle de la source et ne vaut pas extension à l'ensemble de la fonction publique.",
    ),
    "L2146-1": (
        """<p>Quiconque entrave l'exercice du droit syndical défini aux articles L. 2141-4, L. 2141-9 et L. 2141-11 à L. 2143-22 encourt un an d'emprisonnement et 3 750 euros d'amende.</p>""",
        "Réécriture à droit constant : l'auteur de l'entrave et les peines encourues sont formulés directement. Le périmètre de l'infraction demeure défini par les mêmes articles. Aucune réforme de fond des sanctions ou des libertés collectives.",
        "Peines conservées cumulativement : un an d'emprisonnement et 3 750 euros d'amende. Les deux renvois isolés et la plage L. 2141-11 à L. 2143-22 sont repris sans modification ; les bornes ont été retrouvées dans le corpus public.",
    ),
    "L2146-2": (
        """<p>L'employeur qui méconnaît les dispositions des articles L. 2141-5 à L. 2141-8 relatives à la discrimination syndicale encourt 3 750 euros d'amende.</p>
<p>En cas de récidive, les peines sont d'un an d'emprisonnement et de 7 500 euros d'amende.</p>""",
        "Réécriture à droit constant : l'employeur est désigné directement comme auteur de l'infraction et les peines de récidive sont présentées dans un alinéa séparé, comme dans la source. Aucune réforme de fond.",
        "Le champ reste celui des articles L. 2141-5 à L. 2141-8. L'amende initiale de 3 750 euros et, en récidive, l'emprisonnement d'un an avec l'amende de 7 500 euros sont conservés ; aucune peine de récidive n'est appliquée au premier manquement.",
    ),
    "L2151-1": (
        """<p>I. - Pour être représentative, une organisation professionnelle d'employeurs doit satisfaire cumulativement aux critères suivants :</p>
<p>1° Le respect des valeurs républicaines ;</p>
<p>2° L'indépendance ;</p>
<p>3° La transparence financière ;</p>
<p>4° Une ancienneté minimale de deux ans dans le champ professionnel et géographique couvrant le niveau de négociation. Cette durée court à compter du dépôt légal des statuts ;</p>
<p>5° L'influence, appréciée en priorité au regard de l'activité et de l'expérience ;</p>
<p>6° L'audience, mesurée d'après le nombre d'entreprises volontairement adhérentes ou le nombre de leurs salariés soumis au régime français de sécurité sociale. Selon le niveau de négociation, cette mesure s'effectue en application du 3° de l'article L. 2152-1 ou du 3° de l'article L. 2152-4.</p>
<p>II. - Pour l'application du présent titre, les syndicats professionnels d'employeurs mentionnés à l'article L. 2131-1 et les associations d'employeurs mentionnées à l'article L. 2231-1 sont considérés comme des organisations professionnelles d'employeurs.</p>""",
        "Réécriture à droit constant : l'exigence de satisfaire à tous les critères est formulée comme une condition de représentativité ; le calcul de l'ancienneté et les deux bases de mesure de l'audience sont explicités. Le II est réordonné pour identifier directement les entités concernées. Aucune réforme de fond.",
        "Les I et II, les six critères et leur ordre sont conservés. Maintien des deux ans à compter du dépôt légal des statuts, du caractère volontaire de l'adhésion et du rattachement des salariés au régime français de sécurité sociale. Les renvois aux seuls 3° de L. 2152-1 et L. 2152-4 restent distincts des autres critères de ces articles.",
    ),
    "L2152-1": (
        """<p>Dans une branche professionnelle, la représentativité est reconnue aux organisations professionnelles d'employeurs qui remplissent les conditions suivantes :</p>
<p>1° Satisfaire aux critères mentionnés aux 1° à 5° de l'article L. 2151-1 ;</p>
<p>2° Disposer d'une implantation territoriale équilibrée au sein de la branche ;</p>
<p>3° Avoir des entreprises et des organisations adhérentes à jour de leur cotisation qui représentent soit au moins 8 % de l'ensemble des entreprises adhérant à des organisations professionnelles d'employeurs de la branche, soit au moins 8 % des salariés de ces mêmes entreprises. Pour déterminer cet ensemble, seules sont retenues les organisations qui satisfont aux critères mentionnés aux 1° à 4° de l'article L. 2151-1 et qui ont fait la déclaration de candidature prévue à l'article L. 2152-5. Pour chacune de ces organisations, un commissaire aux comptes atteste le nombre d'entreprises adhérentes et le nombre de leurs salariés, dans des conditions fixées par voie réglementaire. Ce commissaire peut être celui de l'organisation. L'audience est mesurée tous les quatre ans.</p>
<p>Dans les branches qui couvrent exclusivement les activités agricoles mentionnées aux 1° à 4° de l'article L. 722-1 du code rural et de la pêche maritime ainsi que les activités des coopératives d'utilisation de matériel agricole, les seuils du 3° du présent article s'apprécient au niveau national, dans les secteurs d'activités concernés. Les entreprises et exploitations adhérentes prises en compte sont celles qui relèvent, l'année précédant la mesure de l'audience, du a du 3° de l'article L. 723-15 du code rural et de la pêche maritime, quel que soit le nombre d'heures effectuées par les salariés concernés. Dans ces branches, les associations d'employeurs constituées conformément à la loi du 1er juillet 1901 relative au contrat d'association et dont l'objet statutaire est la défense d'intérêts professionnels sont également assimilées aux organisations professionnelles d'employeurs mentionnées au II de l'article L. 2151-1 du présent code.</p>""",
        "Réécriture à droit constant : les conditions d'accès à la représentativité sont formulées à l'infinitif ; le 3° distingue les seuils, le périmètre de référence, l'attestation et la périodicité. L'exception agricole est découpée en phrases conservant ses conditions et les associations assimilées. Aucune réforme de fond.",
        "Les cinq alinéas et les 1° à 3° restent en place. Les deux seuils alternatifs de 8 %, la mesure tous les quatre ans et la possibilité de recourir au commissaire aux comptes de l'organisation sont conservés. Pour le dénominateur, les critères demeurent les 1° à 4° de L. 2151-1 avec candidature, tandis que l'organisation demandant sa représentativité doit satisfaire aux 1° à 5°. L'exception agricole conserve le niveau national, l'année précédant la mesure, le a du 3° de L. 723-15, l'absence de seuil d'heures et la loi du 1er juillet 1901.",
    ),
    "L2152-2": (
        """<p>La représentativité au niveau national et multi-professionnel est reconnue aux organisations professionnelles d'employeurs qui remplissent les conditions suivantes :</p>
<p>1° Satisfaire aux critères mentionnés aux 1° à 5° de l'article L. 2151-1 ;</p>
<p>2° Être elles-mêmes représentatives, ou avoir des organisations adhérentes représentatives, sur le fondement de l'article L. 2152-1 du présent code, dans le plus grand nombre de branches relevant soit de l'économie sociale et solidaire, soit du secteur du spectacle vivant et enregistré, et situées hors du champ couvert par les organisations professionnelles d'employeurs représentatives au niveau national et interprofessionnel ;</p>
<p>3° Compter au moins quinze organisations adhérentes relevant de l'un des champs d'activités mentionnés au 2° du présent article ;</p>
<p>4° Justifier d'une implantation territoriale couvrant au moins un tiers du territoire national, au niveau départemental ou au niveau régional.</p>
<p>Pour les activités agricoles mentionnées aux 1° à 4° de l'article L. 722-1 et au 2° de l'article L. 722-20 du code rural et de la pêche maritime, la représentativité au niveau national et multiprofessionnel est reconnue aux organisations professionnelles qui satisfont aux critères de l'article L. 501-1 du même code.</p>""",
        "Réécriture à droit constant : les quatre conditions sont présentées comme des exigences explicites ; l'alternative entre représentativité propre et représentativité des adhérents est clarifiée. Le régime agricole demeure dans son alinéa spécial. Aucune réforme de fond.",
        "Maintien du plus grand nombre de branches dans les deux champs expressément visés et de leur exclusion du champ national interprofessionnel, des quinze organisations adhérentes et du tiers du territoire national apprécié au niveau départemental ou régional. Le régime agricole reste fondé sur L. 501-1 du code rural et de la pêche maritime, avec les mêmes activités visées à L. 722-1 et L. 722-20 ; les quatre conditions générales ne lui sont pas substituées.",
    ),
    "L2152-3": (
        """<p>Avant l'ouverture d'une négociation nationale et interprofessionnelle, puis de nouveau avant sa conclusion, les organisations professionnelles d'employeurs représentatives à ce niveau informent les organisations représentatives au niveau national et multi-professionnel des objectifs poursuivis par la négociation et recueillent leurs observations.</p>""",
        "Réécriture à droit constant : les deux moments d'information sont formulés dans leur ordre et le recueil des observations reste associé à cette obligation. La phrase est ponctuée et placée dans un paragraphe. Aucune réforme de fond.",
        "L'information et le recueil des observations interviennent avant l'ouverture puis avant la conclusion, sans être transformés en droit de veto. La note source relative à l'article 29 VI de la loi n° 2014-288 du 5 mars 2014 situe à compter de 2017 la première mesure d'audience prévue par L. 2152-1 à L. 2152-6 dans leur rédaction issue du I de cet article. Ce repère historique, conservé ici, ne constitue pas une date d'entrée en vigueur du projet et n'appelle pas de réouverture des mesures déjà réalisées.",
    ),
    "L2152-4": (
        """<p>La représentativité au niveau national et interprofessionnel est reconnue aux organisations professionnelles d'employeurs qui remplissent les conditions suivantes :<br/>1° Satisfaire aux critères mentionnés aux 1° à 5° de l'article L. 2151-1 ;<br/>2° Avoir des organisations adhérentes représentatives à la fois dans des branches de l'industrie, de la construction, du commerce et des services ;<br/>3° Avoir des entreprises et des organisations adhérentes à jour de leur cotisation qui représentent soit au moins 8 % de l'ensemble des entreprises adhérant à des organisations professionnelles d'employeurs, soit au moins 8 % des salariés de ces mêmes entreprises. Pour déterminer cet ensemble, seules sont retenues les organisations qui satisfont aux critères mentionnés aux 1° à 4° de l'article L. 2151-1 et qui ont fait la déclaration de candidature prévue à l'article L. 2152-5. Pour chacune de ces organisations, un commissaire aux comptes atteste le nombre d'entreprises adhérentes et le nombre de leurs salariés, dans des conditions fixées par voie réglementaire. Ce commissaire peut être celui de l'organisation. L'audience est mesurée tous les quatre ans.<br/>Lorsqu'une organisation professionnelle d'employeurs adhère à plusieurs organisations professionnelles d'employeurs ayant statutairement vocation à être présentes au niveau national et interprofessionnel, elle répartit ses entreprises adhérentes entre ces organisations pour permettre la mesure de l'audience prévue au présent article. La part d'entreprises affectée à chacune de ces organisations ne peut être inférieure au pourcentage fixé par décret, lequel est compris entre 10 % et 20 %. La clé de répartition retenue s'applique aussi au nombre de salariés de ces entreprises. L'organisation professionnelle d'employeurs précise cette répartition dans la déclaration de candidature prévue à l'article L. 2152-5. Les entreprises adhérentes sont informées de la répartition retenue.</p>""",
        "Réécriture à droit constant : les conditions de représentativité, le calcul de l'audience et sa certification sont distingués par des phrases plus courtes. La règle de répartition des adhésions multiples identifie successivement l'assiette, le minimum réglementaire, les salariés et l'information. Aucune réforme de fond.",
        "La structure d'origine en un paragraphe avec retours à la ligne et les 1° à 3° sont conservés. Maintien des quatre secteurs, des deux seuils alternatifs de 8 %, de la périodicité de quatre ans, du commissaire aux comptes éventuellement propre à l'organisation et du pourcentage réglementaire compris entre 10 % et 20 %, sans fixer ce pourcentage. La même clé s'applique aux salariés ; déclaration L. 2152-5 et information des entreprises sont maintenues. La note source de l'article 29 VI de la loi n° 2014-288 du 5 mars 2014 prévoit la première mesure d'audience à compter de 2017 pour L. 2152-1 à L. 2152-6 dans leur rédaction issue du I de cet article ; cette indication historique est conservée ici, sans devenir une échéance de la réforme.",
    ),
    "L2152-5": (
        """<p>Les organisations professionnelles d'employeurs qui demandent la reconnaissance de leur représentativité au titre du présent chapitre déposent une déclaration de candidature dans les conditions fixées par voie réglementaire.<br/>Dans cette déclaration, elles indiquent le nombre de leurs entreprises adhérentes et le nombre de salariés employés par ces entreprises.</p>
<p>Pour l'application de l'article L. 2135-13, elles indiquent également dans cette même déclaration le nombre de leurs entreprises adhérentes qui emploient au moins un salarié.</p>""",
        "Réécriture à droit constant : la candidature est formulée comme une démarche explicite et la phrase sur les effectifs précise que les salariés décomptés sont ceux des entreprises adhérentes. La donnée supplémentaire destinée au financement paritaire reste distincte. Aucune réforme de fond.",
        "Les deux paragraphes et le retour à la ligne du premier sont conservés. Le seuil d'au moins un salarié n'est appliqué qu'au décompte supplémentaire destiné à L. 2135-13, consulté dans le corpus public, et non à toutes les entreprises adhérentes. La note source de l'article 29 VI de la loi n° 2014-288 du 5 mars 2014 fixe à compter de 2017 la première mesure d'audience de L. 2152-1 à L. 2152-6 dans leur rédaction issue du I de cet article ; ce contexte historique est conservé ici et ne crée aucune nouvelle date de réforme.",
    ),
    "L2152-6": (
        """<p>Après avoir recueilli l'avis du Haut Conseil du dialogue social, le ministre chargé du travail arrête la liste des organisations professionnelles d'employeurs reconnues représentatives par branche professionnelle ainsi que celle des organisations professionnelles d'employeurs reconnues représentatives au niveau national et interprofessionnel ou multi-professionnel. À cette fin, il vérifie le respect des critères définis au présent chapitre. Il s'assure notamment que le montant des cotisations versées par les entreprises et, le cas échéant, par les organisations professionnelles adhérentes permet d'établir la réalité de leur adhésion.</p>""",
        "Réécriture à droit constant : la décision ministérielle, la vérification des critères et le contrôle de la réalité des adhésions sont répartis en trois phrases dans le même alinéa. Aucune réforme de fond de la procédure de reconnaissance.",
        "L'avis préalable du Haut Conseil reste un avis, sans exigence nouvelle de conformité. Les trois niveaux de représentativité et le contrôle des cotisations des entreprises ainsi que, le cas échéant, des organisations adhérentes sont maintenus. La note source de l'article 29 VI de la loi n° 2014-288 du 5 mars 2014 situe à compter de 2017 la première mesure d'audience pour L. 2152-1 à L. 2152-6 dans leur rédaction issue du I de cet article ; cette référence historique est conservée ici et n'est pas assimilée à l'entrée en vigueur du projet.",
    ),
    "L2152-7": (
        """<p>Sauf disposition contraire, un décret en Conseil d'État fixe les conditions d'application du présent chapitre.</p>""",
        "Réécriture à droit constant : le décret devient le sujet de la phrase et la réserve des dispositions contraires reste en tête. Aucune réforme de fond de la compétence réglementaire.",
        "La réserve des dispositions contraires et le recours à un décret en Conseil d'État sont tous deux conservés. Aucun seuil ni délai nouveau n'est ajouté.",
    ),
    "L2211-1": (
        """<p>Le présent livre s'applique aux employeurs de droit privé et à leurs salariés.</p>
<p>Il s'applique également :</p>
<p>1° Aux établissements publics à caractère industriel et commercial ;</p>
<p>2° Aux établissements publics à caractère administratif qui emploient du personnel dans les conditions du droit privé.</p>""",
        "Réécriture à droit constant : l'application du livre est énoncée directement, puis les deux catégories d'établissements publics sont maintenues dans leur énumération. Aucune réforme de fond du champ de la négociation collective.",
        "Les quatre alinéas et les 1° et 2° sont conservés. La condition d'emploi de personnel dans les conditions du droit privé reste attachée aux établissements publics à caractère administratif ; elle n'est ni supprimée ni déplacée vers le 1°.",
    ),
    "L2212-1": (
        """<p>Les salariés et les employeurs ou leurs représentants peuvent suivre des formations communes destinées à améliorer les pratiques du dialogue social dans les entreprises. Ces formations sont dispensées par des centres, instituts ou organismes de formation. L'Institut national du travail, de l'emploi et de la formation professionnelle contribue à leur création et à leur mise en œuvre. Les magistrats judiciaires ou administratifs et les autres agents de la fonction publique peuvent également suivre ces formations.</p>
<p>Les crédits du fonds prévu à l'article L. 2135-9 peuvent financer tout ou partie de ces formations.</p>
<p>Un décret en Conseil d'État fixe les conditions d'application du présent article.</p>""",
        "Réécriture à droit constant : la finalité des formations communes, leurs dispensateurs et le concours de l'institut sont distingués en phrases courtes. Le financement est formulé directement, sans rendre obligatoire une prise en charge facultative. Aucune réforme de fond.",
        "Les trois alinéas substantiels sont conservés. Tous les participants et dispensateurs sont maintenus, y compris les magistrats des deux ordres et les autres agents publics. Le financement reste facultatif, total ou partiel, par le fonds de L. 2135-9 consulté dans le corpus public ; aucun crédit nouveau n'est chiffré ni déclaré ouvert.",
    ),
    "L2212-2": (
        """<div>Les conventions ou accords collectifs d'entreprise ou de branche peuvent définir :<br/>1° Le contenu des formations communes prévues à l'article L. 2212-1 et leurs conditions de réalisation ;<br/>2° Les modalités de financement de ces formations, afin de couvrir les frais pédagogiques, les dépenses d'indemnisation ainsi que les frais de déplacement et d'hébergement des stagiaires et des animateurs.</div>""",
        "Réécriture à droit constant : le renvoi aux formations communes est conservé et la seconde rubrique identifie directement les dépenses que leur financement doit couvrir. L'attribut de présentation du div source est retiré pour respecter le format XML autorisé. Aucune réforme de fond.",
        "Les deux niveaux de négociation, entreprise et branche, demeurent des alternatives et aucune priorité nouvelle n'est instituée ici. Les 1° et 2°, le renvoi à L. 2212-1 et les quatre catégories de dépenses sont conservés ; les dépenses d'indemnisation restent distinctes des frais de déplacement et d'hébergement.",
    ),
    "L2221-1": (
        """<p>Le présent livre régit la détermination des relations collectives entre employeurs et salariés. Il fixe les règles d'exercice du droit des salariés à négocier collectivement l'ensemble de leurs conditions d'emploi, de formation professionnelle et de travail, ainsi que leurs garanties sociales.</p>""",
        "Réécriture à droit constant : la formule introductive devient directe et le droit à la négociation collective est exprimé par le verbe négocier, avec l'intégralité de son objet. Aucune réforme de fond de l'étendue du droit de négociation.",
        "L'emploi, la formation professionnelle, le travail et les garanties sociales sont tous conservés. Les orientations favorisant les accords d'entreprise ne modifient pas cet objet général ; leur mise en œuvre relève des dispositions spéciales d'articulation des accords et de durée du travail, sans suppression du droit général énoncé ici.",
    ),
    "L2221-2": (
        """<p>La convention collective a vocation à couvrir, pour toutes les catégories professionnelles concernées, l'ensemble des matières mentionnées à l'article L. 2221-1.</p>
<p>L'accord collectif porte sur un ou plusieurs sujets déterminés parmi ces matières.</p>""",
        "Réécriture à droit constant : la portée générale de la convention est distinguée du ou des sujets déterminés de l'accord, en rattachant explicitement ces sujets aux matières du même ensemble. Aucune réforme de fond.",
        "Les deux alinéas sont conservés. La vocation générale de la convention ne devient pas une obligation de traiter systématiquement toutes les matières ; l'accord peut toujours porter sur un seul sujet ou sur plusieurs. Le renvoi à L. 2221-1 est maintenu.",
    ),
    "L2221-3": (
        """<p>Le titre Ier du livre IX du code de la sécurité sociale fixe les règles de détermination des garanties collectives dont les salariés bénéficient en complément de celles qui résultent de l'organisation de la sécurité sociale.</p>""",
        "Réécriture à droit constant : la règle de renvoi au code de la sécurité sociale est formulée à la voix active et le caractère complémentaire des garanties reste explicite. Aucune réforme de fond ni transfert automatique de ces garanties vers un autre régime.",
        "Le renvoi au titre Ier du livre IX a été vérifié dans le classement public de L. 911-1 du code de la sécurité sociale et reste inchangé. Les orientations sur la retraite n'étendent pas, par cet article, leur champ aux garanties collectives complémentaires.",
    ),
    "L2222-1": (
        """<p>Les conventions et accords collectifs de travail, désignés respectivement « conventions » et « accords » dans le présent livre, fixent leur champ d'application territorial et professionnel. Leur champ professionnel est défini par les activités économiques concernées.</p>
<p>Pour les professions agricoles mentionnées aux 1° à 3°, 6° et 7° de l'article L. 722-20 du code rural et de la pêche maritime, le champ d'application des conventions et accords peut également tenir compte du statut juridique des entreprises concernées ou du régime de protection sociale auquel leurs salariés sont affiliés.</p>
<p>Sauf stipulations contraires, les conventions et accords collectifs de travail de champ national s'appliquent en Guadeloupe, en Guyane, en Martinique, à Mayotte, à La Réunion, à Saint-Barthélemy, à Saint-Martin et à Saint-Pierre-et-Miquelon dans les six mois suivant leur date d'entrée en vigueur. Pendant ce délai, les organisations syndicales de salariés et d'employeurs habilitées à négocier dans ces collectivités peuvent, si elles le souhaitent, conclure des accords dans le même champ. Pour la Guadeloupe, la Guyane, la Martinique, La Réunion, Saint-Barthélemy, Saint-Martin et Saint-Pierre-et-Miquelon, le présent alinéa est applicable à compter du 1er avril 2017 aux conventions et accords conclus après cette date. À Mayotte, il est applicable à compter du 1er janvier 2018.</p>""",
        "Réécriture à droit constant : les deux dimensions du champ conventionnel et les critères particuliers aux professions agricoles sont explicités. L'alinéa outre-mer distingue l'application dans les six mois et la faculté locale de négocier ; les conditions historiques de la note source sont intégrées à ce même alinéa pour préserver leur portée temporelle. Aucune réforme de fond.",
        "Les trois alinéas, la liste des huit collectivités, l'exception des stipulations contraires et le délai de six mois sont conservés. Les professions agricoles restent celles des 1° à 3°, 6° et 7° de L. 722-20, avec des critères supplémentaires facultatifs. La note de l'article 26 de la loi n° 2016-1088 du 8 août 2016 est reprise : 1er avril 2017 et accords conclus après cette date pour les sept collectivités autres que Mayotte ; application à Mayotte à compter du 1er janvier 2018. La note formule séparément le cas de Mayotte sans y répéter la condition relative à la date de conclusion : cette articulation requiert contrôle de l'article 26, sans correction silencieuse ni extension supposée aux contrats ou accords anciens. Ces dates historiques ne sont pas celles de la réforme future. Aucun nouvel alinéa ne déplace le troisième alinéa visé par la note.",
    ),
    "L2222-2": (
        """<p>Lorsqu'un avenant ou une annexe a un champ d'application différent de celui de la convention ou de l'accord qu'il modifie ou complète, cet avenant ou cette annexe doit préciser son champ conformément à l'article L. 2222-1.</p>""",
        "Réécriture à droit constant : le pronom ambigu visant le champ est remplacé par une obligation expressément portée par l'avenant ou l'annexe. Le fait déclencheur et le renvoi restent identiques. Aucune réforme de fond.",
        "L'obligation vise le champ différent de celui du texte modifié ou complété, sans être étendue aux avenants et annexes de champ identique. Le renvoi à L. 2222-1 couvre les dimensions territoriale et professionnelle dans les mêmes conditions que la source.",
    ),
    "L2222-3": (
        """<p>La convention ou l'accord collectif de travail définit les éléments suivants, dans les conditions prévues au titre IV du livre II de la deuxième partie du présent code :</p>
<p>1° Le calendrier des négociations ;</p>
<p>2° Les modalités selon lesquelles sont prises en compte, dans la branche ou l'entreprise, les demandes portant sur les thèmes de négociation présentées par une ou plusieurs organisations syndicales de salariés représentatives.</p>""",
        "Réécriture à droit constant : le texte conventionnel devient le sujet placé en tête et l'origine des demandes thématiques est formulée directement. Le calendrier et les modalités de prise en compte restent deux objets distincts. Aucune réforme de fond.",
        "Les trois alinéas et les 1° et 2° sont conservés. Le renvoi au titre IV du livre II de la deuxième partie et les deux niveaux, branche et entreprise, sont maintenus. La prise en compte des demandes ne devient ni une obligation d'accepter chaque thème ni un pouvoir réservé à une seule organisation ; une ou plusieurs organisations représentatives peuvent les présenter.",
    ),
}


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(DRAFTS) == {s["number"] for s in sources}
    answer = []
    for source in sources:
        proposed_xml, reason, review_notes = DRAFTS[source["number"]]
        row = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        row.update(proposed_xml=proposed_xml, reason=reason, review_notes=review_notes, status="rewrite_draft")
        answer.append(row)
    Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
