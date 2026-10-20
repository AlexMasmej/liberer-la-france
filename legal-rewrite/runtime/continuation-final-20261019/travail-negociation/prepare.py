import json, pathlib, html, hashlib

P = pathlib.Path(__file__).parent
sources = json.loads((P/'source.json').read_text())
texts = {}
reasons = {}
benefits = {}
cuts = {}
notes = {}

def article(n, paragraphs, reason, benefit, removed=None, note=''):
    texts[n] = ''.join('<p>'+html.escape(x, quote=False)+'</p>' for x in paragraphs)
    reasons[n], benefits[n], notes[n] = reason, benefit, note
    if removed: cuts[n] = removed

article('L2232-6', [
"Une convention de branche ou un accord professionnel est valide si une ou plusieurs organisations syndicales de salariés représentatives signataires ont obtenu au moins 30 % des suffrages exprimés en faveur des organisations reconnues représentatives à ce niveau aux élections prises en compte pour mesurer l'audience prévue au 3° de l'article L. 2122-5 ou à l'article L. 2122-6, quel que soit le nombre de votants.",
"Il ne doit pas faire l'objet de l'opposition d'une ou plusieurs organisations syndicales de salariés représentatives ayant obtenu, à ces mêmes élections, la majorité des suffrages exprimés en faveur des organisations représentatives, quel que soit le nombre de votants.",
"L'opposition est exercée dans les quinze jours suivant la notification de la convention ou de l'accord, dans les formes prévues à l'article L. 2231-8."
], "Maintien motivé des seuils de signature et du droit d'opposition majoritaire : ce sont les conditions du consentement collectif de branche, et non des formalités redondantes. La rédaction sépare signature, opposition et délai sans modifier leur assiette.",
"Le mécanisme permettant un accord signé à partir de 30 % en l'absence d'opposition majoritaire reste disponible pour les accords futurs. Aucun seuil de signature supplémentaire ni unanimité nouvelle n'est imposé.")

article('L2232-7', [
"La représentativité reconnue à une organisation syndicale catégorielle affiliée à une confédération syndicale catégorielle au titre des salariés qu'elle a statutairement vocation à représenter l'habilite à négocier toute disposition applicable à cette catégorie.",
"Une convention de branche ou un accord professionnel qui ne concerne qu'une catégorie professionnelle relevant d'un collège électoral est valide si une ou plusieurs organisations syndicales représentatives signataires ont obtenu, dans ce collège, au moins 30 % des suffrages exprimés en faveur des organisations reconnues représentatives à ce niveau aux élections prises en compte pour mesurer l'audience prévue au 3° de l'article L. 2122-5 ou à l'article L. 2122-6, quel que soit le nombre de votants.",
"La convention ou l'accord ne doit pas faire l'objet d'une opposition émanant d'une ou plusieurs organisations syndicales représentatives ayant obtenu, dans le même collège et aux mêmes élections, la majorité des suffrages exprimés en faveur des organisations représentatives, quel que soit le nombre de votants."
], "Conservation de l'habilitation catégorielle et du calcul des majorités dans le collège concerné. Appliquer l'audience de l'ensemble du personnel supprimerait une faculté favorable et fausserait le consentement de cette catégorie.",
"L'organisation catégorielle conserve la possibilité de négocier toutes les dispositions applicables aux salariés qu'elle représente. La validité demeure appréciée dans son collège, sans nouvelle condition de participation au scrutin.")

article('L2232-8', [
"Les conventions de branche et les accords professionnels organisent, pour les salariés participant aux négociations ou aux réunions des instances paritaires qu'ils instituent, l'exercice du droit de s'absenter, la compensation des pertes de salaire ou le maintien de la rémunération et l'indemnisation des frais de déplacement.",
"Dans les entreprises dont l'effectif est inférieur au seuil fixé par décret en Conseil d'Etat, le fonds paritaire mentionné à l'article L. 2135-9 prend en charge la rémunération des salariés participant aux négociations et les cotisations et contributions sociales correspondantes. Cette prise en charge repose sur un montant forfaitaire fixé par arrêté du ministre chargé du travail.",
"Pour établir le droit à cette prise en charge, les informations et justificatifs déjà détenus par le fonds ou déjà transmis pour la même participation sont réutilisés. Aucune nouvelle attestation ni nouvelle copie de ces pièces ne peut être exigée ; seuls les éléments nécessaires qui manquent peuvent être demandés."
], "Maintien intégral des absences, de la compensation salariale, des déplacements et de la prise en charge forfaitaire des petites entreprises. Suppression expresse des justificatifs et attestations répétés pour une même participation ; le droit au financement n'est pas transformé en dispense de paiement du salaire.",
"Le maintien ou la compensation du salaire, les frais de déplacement et la prise en charge des cotisations des entreprises éligibles restent ouverts à toutes les participations futures. La réutilisation des pièces allège l'accès au financement sans en réduire le montant ni déplacer son coût sur le salarié.",
["Demandes répétées de copies ou d'attestations pour des informations relatives à une même participation déjà détenues par le fonds."],
"Coordonner R2232-1-5 et son modèle de demande : une attestation de participation initialement nécessaire reste possible, mais elle ne doit pas être exigée à nouveau si le fonds possède déjà l'information probante. Seuil, forfait et délais de remboursement ne sont pas modifiés dans ce lot.")

article('L2232-9', [
"I. – Dans chaque branche, une convention ou un accord met en place une commission paritaire permanente de négociation et d'interprétation.",
"II. – La commission exerce les missions d'intérêt général suivantes :",
"1° Elle représente la branche, notamment auprès des pouvoirs publics, et apporte un appui aux entreprises ;",
"2° Elle assure une veille sur les conditions de travail et l'emploi ;",
"3° Elle peut établir et publier des bilans ou des recommandations, sans rapport annuel imposé ni dépôt obligatoire de ces travaux dans la base mentionnée à l'article L. 2231-5-1. Ces travaux peuvent notamment porter sur les accords d'entreprise conclus dans le cadre du titre II, des chapitres Ier et III du titre III et des titres IV et V du livre Ier de la troisième partie, leurs effets sur les conditions de travail et la concurrence entre entreprises de la branche et les réponses aux difficultés constatées. Ils peuvent également porter sur l'égalité professionnelle entre les femmes et les hommes, les classifications, la mixité des emplois, les certificats de qualification professionnelle, la répartition et la nature des postes occupés par les femmes et les hommes et les outils de prévention et de traitement du harcèlement sexuel et des agissements sexistes.",
"La commission peut donner, à la demande d'une juridiction, un avis sur l'interprétation d'une convention ou d'un accord collectif, dans les conditions de l'article L. 441-1 du code de l'organisation judiciaire.",
"Elle peut exercer les missions d'un observatoire paritaire organisé conformément à l'article L. 2232-10.",
"Pour ces missions, la commission réutilise les accords publiés dans la base mentionnée à l'article L. 2231-5-1 et les informations déjà disponibles. Le présent article n'impose aux entreprises ni transmission supplémentaire d'accords, ni production d'un état ou d'une collecte de données pour les besoins d'un bilan de la commission. Les règles de confidentialité et de protection des données demeurent applicables.",
"III. – La commission arrête son calendrier de négociation dans les conditions de l'article L. 2222-3 et se réunit autant que nécessaire pour accomplir les négociations prévues au chapitre Ier du titre IV du présent livre. Aucun nombre minimal distinct de réunions annuelles n'est imposé par le présent article.",
"La suppression du rapport annuel et des transmissions supplémentaires s'applique dès l'entrée en vigueur de la présente rédaction, y compris aux rapports ou transmissions relatifs à une période antérieure qui n'ont pas encore été réalisés. Les documents déjà établis sont conservés selon les règles qui leur sont applicables. Cette suppression ne dispense d'aucune négociation, obligation de prévention ou obligation d'égalité professionnelle reposant sur un autre fondement."
], "Suppression réelle du rapport annuel obligatoire, de son dépôt, de la transmission distincte des accords d'entreprise et du minimum de trois réunions. Les études deviennent facultatives, sans nouvelle déclaration de remplacement. La commission, sa veille, l'interprétation judiciaire et les négociations obligatoires de branche subsistent ; les bilans d'égalité et de prévention ne sont pas supprimés quand ils sont dus sur un fondement autonome.",
"Les salariés et entreprises conservent l'appui de la branche, la veille, les recommandations et la faculté d'interprétation des accords. Les outils d'égalité et de lutte contre le harcèlement restent possibles et les obligations autonomes de protection demeurent ; aucune dispense ou dérogation favorable à la négociation n'est retirée.",
["Rapport annuel de la commission et dépôt obligatoire dans la base nationale.", "Transmission supplémentaire des accords d'entreprise à la commission et formalités qui ne servent que cette transmission.", "Minimum de trois réunions par an, distinct des négociations dont la périodicité légale demeure applicable."],
"Réviser D2232-1-1 (coordonnées et circuit spécifique de transmission) et abroger les obligations de transmission, anonymisation supplémentaire, information des signataires et accusé de réception de D2232-1-2 devenues sans objet. L2231-5-1 et les obligations L2241 ne sont pas abrogés. L441-1 COJ reste un renvoi autonome, non modifié ici.")

article('L2232-10', [
"Une convention de branche ou un accord professionnel peut organiser un observatoire paritaire de la négociation collective. La commission prévue à l'article L. 2232-9 peut en assurer les missions, sans création d'une instance distincte.",
"La convention ou l'accord en définit les missions et le fonctionnement. L'observatoire utilise les accords et informations déjà disponibles ; le présent article n'impose pas aux entreprises ou aux établissements une transmission supplémentaire des accords mettant en œuvre une disposition législative.",
"A compter de l'entrée en vigueur de la présente rédaction, l'obligation légale d'instituer cet observatoire et les transmissions imposées sur le seul fondement de l'ancienne rédaction cessent. Les conventions et accords qui ont organisé un observatoire demeurent applicables jusqu'à leur modification ou leur cessation selon les règles de la négociation collective ; les droits qui en résultent ne sont pas supprimés par le présent article."
], "L'observatoire et le circuit légal de réception systématique des accords deviennent facultatifs. La CPPNI peut assurer la fonction pour éviter une seconde instance. Les engagements conventionnels existants et la liberté de créer un observatoire futur sont préservés.",
"La faculté d'organiser un observatoire, de mutualiser son activité avec la CPPNI et de conserver les moyens conventionnellement accordés reste ouverte. L'allègement de l'obligation légale ne dénonce ni ne supprime les avantages prévus par des accords existants.",
["Création obligatoire d'un observatoire paritaire dans chaque branche.", "Circuit obligatoire supplétif de réception des accords d'entreprise ou d'établissement fondé sur le seul présent article."],
"Coordination interne avec L2232-9 réécrit. Les obligations librement stipulées dans un accord ne sont pas éteintes d'office ; leur révision relève des règles ordinaires, sans procédure nouvelle.")

article('L2232-10-1', [
"Un accord de branche peut prévoir des stipulations spécifiques pour les entreprises de moins de cinquante salariés. Il peut prendre la forme d'un accord type comportant plusieurs choix ouverts à l'employeur et traiter de tout thème pouvant faire l'objet d'une négociation d'entreprise en application du présent code.",
"L'employeur peut appliquer cet accord type par un document unilatéral qui indique les choix retenus. Il en informe préalablement le comité social et économique, lorsqu'il existe, ainsi que les salariés, par tout moyen.",
"Les choix doivent rester dans les options dont le contenu est prédéfini par l'accord de branche ; cette faculté ne permet pas à l'employeur d'en adapter unilatéralement le contenu."
], "Conservation de l'accès simplifié aux accords types pour les entreprises de moins de cinquante salariés. La limite déjà inscrite à D2232-1-6 est explicitée pour ne pas transformer les options négociées en pouvoir d'imposer librement un accord. L'information préalable demeure une garantie légère et utile.",
"Les petites entreprises conservent le document unilatéral et toutes les options prédéfinies de l'accord type, sur tous les thèmes admis. Aucun vote ou agrément supplémentaire n'est ajouté ; les salariés gardent l'information et les limites résultant de l'accord de branche.", note="D2232-1-6 lu en entier : options prédéfinies sans adaptation par l'employeur. Ce rappel ne crée pas une restriction nouvelle et ne ferme aucune option de l'accord de branche.")

article('L2232-11', [
"La présente section fixe les modalités selon lesquelles s'exerce le droit des salariés à la négociation dans l'entreprise et dans le groupe.",
"Sauf disposition contraire, l'expression « convention d'entreprise » désigne les conventions et accords conclus au niveau du groupe, de l'entreprise ou de l'établissement."
], "Maintien du champ du droit à la négociation et de la définition commune évitant de répéter les trois niveaux dans chaque article. Retirer cette règle ne réduirait aucune charge et rendrait incertains les renvois.",
"Le droit de négocier reste reconnu aux niveaux du groupe, de l'entreprise et de l'établissement. La définition commune conserve les facultés attachées à chacun de ces niveaux, sous réserve des dispositions spéciales.")

article('L2232-12', [
"Un accord d'entreprise ou d'établissement est valide s'il est signé par l'employeur ou son représentant et par une ou plusieurs organisations syndicales de salariés représentatives ayant obtenu plus de 50 % des suffrages exprimés en faveur des organisations représentatives au premier tour des dernières élections des titulaires au comité social et économique, quel que soit le nombre de votants.",
"A défaut de cette majorité, lorsqu'un accord est signé par l'employeur et par des organisations syndicales représentatives ayant obtenu plus de 30 % des suffrages définis au premier alinéa, une ou plusieurs de ces organisations totalisant plus de 30 % de ces suffrages peuvent demander une consultation des salariés pour le valider. Elles disposent d'un mois à compter de la signature pour le demander. A l'expiration de ce mois, l'employeur peut demander la consultation, sauf opposition de l'ensemble de ces organisations.",
"Huit jours après la demande syndicale ou l'initiative de l'employeur, si les signatures supplémentaires n'ont pas permis d'atteindre la majorité requise au premier alinéa et si les conditions du deuxième alinéa restent remplies, la consultation est organisée dans les deux mois.",
"La consultation respecte les principes généraux du droit électoral et peut avoir lieu par voie électronique. Ses modalités sont convenues entre l'employeur et une ou plusieurs organisations syndicales représentatives ayant obtenu plus de 30 % des suffrages définis au premier alinéa. Leur accord identifie le texte soumis au vote et les modalités de cette consultation. Il peut reprendre, par un renvoi écrit accepté par ces mêmes parties, les dispositions toujours adaptées d'un protocole antérieur : un protocole matériellement distinct ou la reproduction de dispositions identiques ne sont pas exigés. Aucune modalité n'est réputée acceptée du seul fait du silence.",
"Les salariés des établissements couverts par l'accord qui ont la qualité d'électeur selon l'article L. 2314-18 participent à la consultation. Les mesures facilitant la représentation prévues à l'article L. 2314-15 et le contrôle de la liberté et de la régularité du scrutin prévu à l'article L. 2314-17 restent applicables.",
"L'approbation à la majorité des suffrages exprimés valide l'accord. En l'absence d'approbation, celui-ci est réputé non écrit.",
"Un décret précise les conditions de la consultation, sans exiger un protocole distinct lorsque les modalités ont été valablement convenues conformément au quatrième alinéa."
], "Suppression du document spécifique matériellement distinct lorsque les parties compétentes acceptent expressément de réutiliser des modalités existantes adaptées au scrutin. Conservation de toutes les majorités, de l'initiative prioritaire des syndicats, de l'opposition collective à l'initiative patronale, des huit jours permettant des signatures supplémentaires et du vote des salariés. Correction du renvoi à L2314-18-1 abrogé en 2018, sans remettre en vigueur l'ancien régime des délégués du personnel.",
"La voie référendaire d'un accord signé à plus de 30 % reste ouverte, comme le vote électronique. Les syndicats conservent leur mois d'initiative et les salariés un scrutin loyal ; réutiliser un protocole requiert l'accord des mêmes parties et ne permet aucune validation par silence.",
["Obligation d'établir un protocole matériellement distinct ou de reproduire des modalités déjà convenues et encore adaptées, avec accord exprès des parties compétentes."],
"Renvoi source L2314-18-1 contrôlé : seul document LEGIARTI000019353566, ABROGE au 1er janvier 2018, relatif à l'ancien régime des salariés mis à disposition. Le renvoi est retiré et non remplacé par une restauration de ses anciennes conditions. D2232-2, D2232-3, D2232-4 et D2232-6 lus ; conserver information quinze jours, secret, temps de travail, procès-verbal et recours. Les renvois réglementaires obsolètes R2324-5 à R2324-17 doivent être examinés hors lot ; aucune prétention de résolution ici.")

article('L2232-13', [
"Une organisation syndicale catégorielle affiliée à une confédération syndicale catégorielle, dont la représentativité est reconnue au titre des salariés qu'elle a statutairement vocation à représenter, peut négocier toute disposition applicable à cette catégorie.",
"Une convention ou un accord d'entreprise ou d'établissement ne concernant qu'une catégorie professionnelle relevant d'un collège électoral est valide s'il est signé par l'employeur ou son représentant et par une ou plusieurs organisations syndicales représentatives ayant obtenu plus de 50 % des suffrages exprimés en faveur des organisations représentatives dans ce collège, au premier tour des dernières élections des titulaires au comité social et économique, quel que soit le nombre de votants.",
"Les règles de validité de l'article L. 2232-12 s'appliquent. Les seuils de 30 % et de 50 % s'apprécient à l'échelle du collège concerné ; la consultation éventuelle est organisée à cette même échelle."
], "Conservation de la négociation et du calcul d'audience propres au collège. La simplification du protocole autorisée à L2232-12 bénéficie aussi à cette consultation, sans élargir le corps électoral ni réduire son consentement.",
"Les syndicats catégoriels conservent leur habilitation et l'appréciation des seuils dans le collège qu'ils représentent. La faculté de consultation et le réemploi accepté des modalités de vote restent ouverts sans seuil supplémentaire.")

article('L2232-14', [
"En cas de carence au premier tour des élections professionnelles, lorsqu'est appliqué le premier alinéa de l'article L. 2143-23, un accord d'entreprise ou d'établissement négocié et conclu avec le représentant de la section syndicale n'est valide qu'après approbation des salariés à la majorité des suffrages exprimés.",
"La consultation respecte les principes généraux du droit électoral et les conditions fixées par décret. Si les salariés ne l'approuvent pas, l'accord est réputé non écrit."
], "Maintien de cette voie dérogatoire de négociation et de sa ratification nécessaire en l'absence de représentativité électorale du signataire. Supprimer le vote permettrait un accord imposé, contraire à la consigne de consentement.",
"La faculté de négocier avec un représentant de section syndicale dans le cas légal de carence reste disponible. Elle n'est ni soumise à une autorisation nouvelle ni étendue au-delà du mandat et des conditions de L2143-23.", note="L2143-23 et sa note de 2008 lus intégralement ; les exclusions historiques du champ des entreprises doivent être conservées dans leur contexte et ne sont pas abrogées par cet article.")

article('L2232-16', [
"Les conventions et accords d'entreprise sont négociés entre l'employeur et les organisations syndicales de salariés représentatives dans l'entreprise, sous réserve des modalités particulières prévues pour les entreprises dépourvues de délégué syndical.",
"Ils peuvent être conclus au niveau d'un établissement ou d'un groupe d'établissements dans les mêmes conditions.",
"Ces règles valent également pour leur révision et leur dénonciation, quelles qu'aient été les modalités de leur négociation ou de leur ratification initiale."
], "Clarification de l'articulation avec les dérogations de la sous-section des entreprises sans délégué syndical. La faculté de réviser ou dénoncer indépendamment du mode de conclusion initial demeure ; pas de réitération de la procédure initiale imposée.",
"Les niveaux établissement et groupe d'établissements ainsi que les modalités dérogatoires pour les entreprises sans délégué syndical sont expressément préservés. Aucun accord existant n'est figé par son ancien mode de négociation ou de ratification.")

article('L2232-17', [
"La délégation de chaque organisation représentative participant à la négociation comprend son délégué syndical dans l'entreprise. Si elle y dispose de plusieurs délégués syndicaux, au moins deux d'entre eux en font partie.",
"Chaque organisation peut compléter sa délégation par des salariés de l'entreprise. L'employeur et l'ensemble des organisations représentatives participant à la négociation conviennent de leur nombre.",
"Faute d'accord sur ce nombre, le nombre de salariés supplémentaires de chaque délégation ne peut dépasser celui des délégués syndicaux qui la composent. Lorsqu'une entreprise ne compte qu'un seul délégué syndical, ce nombre de salariés supplémentaires peut être porté à deux."
], "Maintien des moyens de représentation et du régime supplétif évitant qu'un désaccord sur la composition bloque la négociation. Le bénéfice de deux salariés supplémentaires avec un délégué unique est conservé. Aucun nouveau formulaire de composition ou autorisation administrative n'est créé.",
"L'organisation conserve les salariés supplémentaires admis par accord et le nombre garanti à défaut d'accord. L'avantage spécifique des deux salariés accompagnant l'unique délégué syndical de l'entreprise subsiste pour les négociations futures.")

article('L2232-18', [
"Tout temps consacré à la négociation est rémunéré comme du temps de travail. La rémunération correspondante est versée à l'échéance normale."
], "Maintien du paiement du temps de négociation : sa suppression ferait supporter l'exercice d'un droit collectif au salarié. La règle est formulée directement sans créer de justification ou de validation supplémentaire.",
"Le paiement comme temps de travail et le versement à l'échéance normale sont conservés pour toute négociation. Aucun report, forfait inférieur, compensation conditionnelle ou récupération de ces heures n'est introduit.")

article('L2232-19', [
"Lorsqu'une entreprise emploie des travailleurs appartenant à une ou plusieurs entreprises extérieures, dans ses locaux ou sur un chantier dont elle assure la direction comme entreprise générale, les délégués syndicaux des organisations représentatives de ces entreprises extérieures sont entendus pendant les négociations s'ils le demandent."
], "Maintien de l'audition sur demande des représentants des salariés extérieurs ou sous-traitants, sans audition systématique ni procédure de saisine ajoutée. Ce droit ne les transforme pas en signataires d'un accord hors de leur champ.",
"Les représentants des salariés d'entreprises extérieures et sous-traitantes conservent la faculté d'être entendus à leur demande. Aucun accord préalable de l'employeur, seuil d'effectif ou formalité particulière n'est ajouté à cette faculté.")

article('L2232-20', [
"L'employeur et les organisations syndicales représentatives dans l'entreprise déterminent l'objet et la périodicité des négociations ainsi que les informations nécessaires à remettre préalablement aux délégués syndicaux de l'entreprise ou de l'établissement. Ils respectent les articles L. 2222-3 et L. 2222-3-1, sans préjudice des négociations annuelles obligatoires prévues aux articles L. 2242-1 et suivants.",
"Une information déjà accessible aux délégués syndicaux dans une base ou un dossier existant n'a pas à être reproduite ou remise une seconde fois lorsque son emplacement leur est indiqué, que son contenu est à jour et qu'ils peuvent effectivement y accéder et l'utiliser en temps utile pour négocier. Les informations nécessaires absentes ou incomplètes leur sont communiquées avant la négociation ; un simple renvoi inaccessible ou ne permettant pas cet usage ne vaut pas remise."
], "Suppression des doubles remises et reproductions d'informations déjà effectivement accessibles, avec réemploi du dossier existant. L'information préalable utile et la loyauté subsistent ; l'employeur ne peut remplacer un accès effectif par une référence vide. Les négociations annuelles du régime supplétif ne sont pas abolies dans cet article.",
"Les délégués conservent les informations nécessaires avant la négociation et les moyens supplémentaires convenus selon L2222-3-1. La dispense de copie ne prive pas d'accès effectif, de données à jour ou des informations manquantes ; aucune négociation obligatoire n'est supprimée par simple renvoi.",
["Reproduction ou remise répétée d'informations déjà à jour et effectivement accessibles et utilisables par les délégués avant la négociation."],
"L2222-3-1 renvoie encore à l'ancienne base L2323-8 : la présente règle vise toute base ou tout dossier existant sans réactiver cet article. Les obligations autonomes de tenue ou d'information de la BDESE restent hors lot.")

article('L2232-21', [
"Dans une entreprise dont l'effectif habituel est inférieur à onze salariés et qui est dépourvue de délégué syndical, l'employeur peut proposer aux salariés un projet d'accord ou d'avenant de révision portant sur l'ensemble des thèmes ouverts à la négociation collective d'entreprise par le présent code.",
"Le projet est communiqué à chaque salarié. La consultation du personnel ne peut avoir lieu moins de quinze jours après cette communication, afin que chacun puisse en prendre connaissance et se prononcer librement.",
"Un décret en Conseil d'Etat précise les modalités d'application du présent article."
], "Conservation de la voie directe de ratification dans les très petites entreprises et de tous les thèmes négociables. Le minimum de quinze jours est maintenu : en l'absence de représentants négociateurs, il assure une réflexion réelle sur un texte proposé par l'employeur et ne constitue pas un délai administratif doublon.",
"L'employeur conserve la possibilité de proposer un accord ou une révision sans créer une délégation syndicale préalable. Tous les salariés gardent le texte individuel, le délai de réflexion et la majorité protectrice de L2232-22 ; aucun accord n'est imposé par silence.", note="R2232-10 à R2232-13 lus : consultation personnelle et secrète, hors présence de l'employeur, pendant le temps de travail, publicité du résultat et recours. Leur suppression n'est pas proposée.")

article('L2232-22', [
"Le projet d'accord ou d'avenant proposé conformément à l'article L. 2232-21 devient un accord d'entreprise valide s'il est approuvé par les deux tiers du personnel.",
"L'employeur peut dénoncer l'accord ou l'avenant ainsi conclu dans les conditions qu'il prévoit ou, à défaut, dans celles des articles L. 2261-9 à L. 2261-13.",
"Les salariés peuvent également dénoncer l'accord ou l'avenant dans les conditions qu'il prévoit ou, à défaut, dans celles des articles L. 2261-9 à L. 2261-13. La dénonciation par les salariés respecte en outre les conditions suivantes :",
"– Les salariés représentant les deux tiers du personnel notifient collectivement et par écrit la dénonciation à l'employeur ;",
"– Cette notification peut intervenir à tout moment ; elle n'est pas limitée au mois précédant la date anniversaire de l'accord. Les préavis et les règles de maintien des effets, de négociation de remplacement et de garantie de rémunération résultant des dispositions applicables demeurent respectés.",
"La suppression de la fenêtre annuelle de dénonciation s'applique dès l'entrée en vigueur de la présente rédaction, y compris aux accords déjà conclus. Elle ne réduit ni les préavis en cours ni les droits résultant d'une dénonciation antérieure."
], "Suppression de la fenêtre annuelle d'un mois qui contraignait la dénonciation collective par les salariés. Le seuil des deux tiers du personnel, l'écrit collectif, les préavis, la survie temporaire et la garantie de rémunération restent maintenus : la simplification ouvre un droit sans permettre la rupture instantanée de l'accord.",
"Les salariés peuvent désormais exercer leur droit collectif toute l'année, sans attendre l'anniversaire. Le seuil des deux tiers et les protections de L2261-9 à L2261-13 restent applicables ; aucune garantie de rémunération ni faculté de négociation de remplacement n'est retirée.",
["Restriction de la dénonciation par les salariés au seul mois précédant chaque date anniversaire de l'accord."],
"Les deux subdivisions en tirets sont conservées. Les conditions conventionnelles subsistent dans leur champ, mais ne peuvent restaurer la fenêtre annuelle légale supprimée. L2261-9 à L2261-13 lus en entier avec notes d'application.")

article('L2232-22-1', [
"Les modalités de révision et de dénonciation fixées à l'article L. 2232-22 s'appliquent également aux accords, quelles que soient leurs modalités de conclusion initiales, lorsque l'entreprise remplit ultérieurement les conditions prévues aux articles L. 2232-21 et L. 2232-23."
], "Maintien de la passerelle permettant de réviser ou dénoncer un accord malgré un mode initial de conclusion différent. La suppression de la fenêtre annuelle bénéficie aux accords entrant dans ce champ, sans nouvelle ratification de leur existence.",
"La faculté favorable de changer de mode de révision ou de dénonciation lorsque la situation de l'entreprise évolue est conservée. Elle s'étend à tous les accords visés sans imposer leur conclusion à nouveau ni retirer les droits déjà produits.")

article('L2232-23', [
"Dans les entreprises dont l'effectif habituel est compris entre onze et vingt salariés et qui ne disposent d'aucun membre élu de la délégation du personnel du comité social et économique, les articles L. 2232-21, L. 2232-22 et L. 2232-22-1 s'appliquent."
], "Maintien de l'extension de la procédure directe aux entreprises de onze à vingt salariés sans élu, avec les conditions de L2232-21, notamment l'absence de délégué syndical. Cette dérogation ne doit pas disparaître sous prétexte d'uniformiser les seuils.",
"Les entreprises de onze à vingt salariés sans membre élu conservent la procédure directe et les salariés le vote aux deux tiers ainsi que les droits de révision et de dénonciation. Le renvoi conserve toutes les conditions protectrices du dispositif de départ.")

article('L2232-23-1', [
"I. – Dans les entreprises dont l'effectif habituel est d'au moins onze salariés et inférieur à cinquante, en l'absence de délégué syndical dans l'entreprise ou l'établissement, les accords d'entreprise ou d'établissement peuvent être négociés, conclus, révisés ou dénoncés :",
"1° Par un ou plusieurs salariés expressément mandatés par une ou plusieurs organisations syndicales représentatives dans la branche ou, à défaut, au niveau national et interprofessionnel. Ces salariés peuvent être membres ou non de la délégation du personnel du comité social et économique. Une même organisation ne peut mandater qu'un salarié ;",
"2° Ou par un ou plusieurs membres titulaires de la délégation du personnel du comité social et économique.",
"Ces accords peuvent traiter de toute mesure ouverte à la négociation d'entreprise ou d'établissement par le présent code.",
"II. – Un accord ou un avenant de révision conclu avec des membres de la délégation du personnel du comité social et économique, mandatés ou non, est valide si les signataires représentent la majorité des suffrages exprimés en faveur des membres du comité lors des dernières élections professionnelles.",
"Lorsque des membres titulaires de la délégation du personnel du comité social et économique central concluent l'accord, chaque titulaire reçoit, pour apprécier cette majorité, un poids égal au rapport entre les suffrages exprimés dans son établissement en sa faveur et le nombre total des suffrages exprimés dans chaque établissement en faveur des titulaires composant cette délégation.",
"Un accord ou un avenant de révision conclu avec des salariés mandatés qui ne sont pas membres de la délégation du personnel du comité social et économique n'est valide qu'après approbation des salariés à la majorité des suffrages exprimés, dans les conditions fixées par décret et le respect des principes généraux du droit électoral."
], "Conservation des deux voies ouvertes dans les entreprises de onze à moins de cinquante salariés et de tous les thèmes négociables. Les majorités et la pondération du CSE central sont intégralement conservées. Aucune consultation nouvelle n'est ajoutée aux élus majoritaires et aucune ratification n'est retirée au mandaté non élu.",
"Les salariés peuvent négocier avec ou sans mandat lorsqu'ils sont élus et, s'ils ne sont pas élus, avec mandat et approbation collective. Le recours à la représentativité nationale à défaut de représentativité de branche et l'ensemble des thèmes demeurent ouverts.", note="Le calcul de poids du CSE central est conservé sur son assiette source, sans addition de seuil ou modification du dénominateur. Les garanties et moyens autonomes de L2232-27 à L2232-29, lus en entier, restent applicables.")

article('L2232-24', [
"Dans les entreprises dont l'effectif habituel atteint cinquante salariés, lorsque l'entreprise ou l'établissement n'a pas de délégué syndical, les membres titulaires de la délégation du personnel du comité social et économique peuvent négocier, conclure, réviser ou dénoncer des accords collectifs s'ils disposent d'un mandat exprès d'une ou plusieurs organisations syndicales représentatives dans la branche de l'entreprise ou, à défaut, au niveau national et interprofessionnel. Chaque organisation ne peut mandater qu'un salarié.",
"L'employeur informe ces organisations syndicales de sa décision d'engager la négociation. Une information déjà adressée à la même organisation pour la même négociation satisfait à cette obligation : aucune nouvelle notification identique n'est exigée lors de l'application de l'article L. 2232-25-1 ou du passage à la procédure de l'article L. 2232-26.",
"Les accords et avenants de révision ainsi conclus n'ont de validité qu'après approbation des salariés à la majorité des suffrages exprimés, dans les conditions fixées par décret et le respect des principes généraux du droit électoral."
], "Maintien du mandat syndical, de l'information des syndicats leur permettant de mandater et du référendum. Suppression d'une nouvelle notification identique lorsque la même négociation poursuit le circuit des articles L2232-25-1 et L2232-26 ; un changement de négociation ou d'organisation destinataire reste à informer.",
"Les élus conservent le recours au mandat de branche ou, à défaut, national et interprofessionnel. Les syndicats doivent effectivement être informés, et le vote des salariés reste requis ; la dispense ne concerne que la répétition de la même information déjà reçue.",
["Réitération d'une information syndicale identique pour la même négociation déjà annoncée au même destinataire."],
"Coordination interne avec L2232-26 : aucune omission du premier avis aux organisations représentatives n'est autorisée. Les droits de mandatement et les garanties L2232-27 à L2232-29 subsistent.")

article('L2232-25', [
"Dans les entreprises dont l'effectif habituel atteint cinquante salariés, si aucun membre de la délégation du personnel du comité social et économique n'est mandaté selon l'article L. 2232-24, les membres titulaires de cette délégation qui n'ont pas reçu un tel mandat peuvent négocier, conclure, réviser ou dénoncer des accords collectifs.",
"Cette voie est limitée aux mesures dont la loi subordonne la mise en œuvre à un accord collectif. Elle ne permet pas de conclure les accords mentionnés à l'article L. 1233-21.",
"Un accord ou un avenant de révision ainsi conclu est valide si les membres de la délégation signataires représentent la majorité des suffrages exprimés en faveur des membres du comité social et économique aux dernières élections professionnelles.",
"Lorsque l'accord est conclu par des membres titulaires de la délégation du personnel du comité social et économique central, chaque titulaire reçoit, pour apprécier cette majorité, un poids égal au rapport entre les suffrages exprimés dans son établissement en sa faveur et le nombre total des suffrages exprimés dans chaque établissement en faveur des titulaires composant cette délégation."
], "Conservation de la voie supplétive sans mandat, de sa majorité et de la pondération centrale. Le champ limité et l'exclusion des accords de procédure de licenciement collectif ne sont pas effacés : élargir sans mandat ni ratification à tous les thèmes changerait la légitimité de la négociation et retirerait une protection essentielle non examinée ici.",
"Les élus sans mandat conservent la possibilité de conclure les accords légalement nécessaires sans ratification supplémentaire. La majorité électorale suffit dans ce champ ; aucun agrément de branche ou autorisation administrative n'est ajouté.")

article('L2232-25-1', [
"Pour appliquer les articles L. 2232-24 et L. 2232-25, l'employeur informe les membres de la délégation du personnel du comité social et économique de son intention de négocier par tout moyen donnant date certaine à cette information.",
"Les élus disposent d'un mois pour faire connaître leur souhait de négocier et préciser, s'il y a lieu, le mandat reçu d'une organisation mentionnée à l'article L. 2232-24.",
"La négociation commence à l'expiration de ce mois avec les élus qui se sont déclarés mandatés ou, à défaut, avec les élus non mandatés selon l'article L. 2232-25. Elle peut commencer avant son expiration si tous les élus destinataires de l'information ont librement communiqué leur choix exprès et définitif de participer ou de ne pas participer, ainsi que leur situation au regard du mandat. Un élu n'est pas tenu de répondre avant la fin du mois et son silence ne vaut ni refus de négocier ni renonciation au mandat. Les organisations mentionnées à l'article L. 2232-24 doivent avoir été informées de la négociation et avoir pu exercer leur faculté de mandatement ; l'employeur ne peut en empêcher ou en précipiter l'exercice.",
"L'ouverture anticipée ne modifie pas la priorité des élus mandatés, les conditions de validité de l'accord, les droits d'information ni les garanties d'indépendance et de concertation prévues à l'article L. 2232-29. Elle ne peut résulter d'une renonciation exigée par l'employeur."
], "Dispense de l'attente du mois entier seulement lorsque tous les élus ont librement et expressément arrêté leur choix et que la faculté syndicale de mandater a été effective. Le mois reste un droit de réponse individuel : aucune absence de réponse ne déclenche la dispense. La priorité des mandatés et la concertation restent intactes.",
"Les élus conservent le mois complet s'ils le souhaitent et la possibilité de rechercher un mandat ; les syndicats gardent un exercice effectif de leur faculté de mandater. La négociation peut démarrer plus tôt uniquement si aucun choix ni droit utile ne reste en attente.",
["Attente automatique jusqu'au terme du mois alors que tous les élus ont librement donné une réponse définitive et que le droit de mandatement a pu être exercé."],
"Le déclenchement anticipé est une faculté sous conditions cumulatives, non une présomption de refus. L2232-26 renvoie à l'issue de cette procédure : il reste nécessaire qu'aucun élu ne souhaite négocier avant de recourir aux seuls salariés mandatés.")

article('L2232-26', [
"Dans les entreprises dont l'effectif habituel atteint cinquante salariés et qui n'ont pas de délégué syndical, si aucun membre de la délégation du personnel du comité social et économique n'a souhaité négocier à l'issue de la procédure de l'article L. 2232-25-1, un ou plusieurs salariés peuvent négocier, conclure, réviser ou dénoncer des accords d'entreprise ou d'établissement s'ils sont expressément mandatés par une ou plusieurs organisations syndicales représentatives dans la branche ou, à défaut, au niveau national et interprofessionnel. Chaque organisation ne peut mandater qu'un salarié.",
"L'employeur informe ces organisations de sa décision d'engager la négociation. Il n'a pas à répéter une information déjà adressée au même destinataire pour cette même négociation conformément à l'article L. 2232-24 ; il communique seulement les éléments nouveaux nécessaires.",
"Le présent article s'applique de plein droit, sans passage par la procédure de l'article L. 2232-25-1, lorsque l'entreprise est dépourvue de délégué syndical et qu'un procès-verbal de carence a établi l'absence de représentants élus du personnel. Le procès-verbal existant peut être utilisé tant qu'il établit encore cette absence ; un nouveau procès-verbal n'est pas exigé pour chaque négociation.",
"Ces accords peuvent porter sur toute mesure ouverte à la négociation d'entreprise ou d'établissement par le présent code.",
"Un accord signé par un salarié mandaté n'est valide qu'après approbation des salariés à la majorité des suffrages exprimés, dans les conditions fixées par décret et le respect des principes généraux du droit électoral."
], "Dispense de notification syndicale répétée pour la même négociation et clarification de la réutilisation du procès-verbal de carence existant. La dispense de procédure préalable en cas de carence est conservée. Aucun accord n'est validé sans mandat ni vote, et l'absence actuelle d'élus doit toujours être établie.",
"Le recours direct aux salariés mandatés en cas de carence demeure ouvert, sans nouveau constat pour chaque négociation. Tous les thèmes et le recours syndical national à défaut de branche subsistent ; la majorité des suffrages et les garanties d'indépendance sont préservées.",
["Notification syndicale répétée pour le même objet déjà communiqué au même destinataire.", "Exigence d'un nouveau procès-verbal de carence pour chaque négociation lorsque celui déjà établi prouve encore l'absence d'élus."],
"Aucune dispense d'organiser les élections légalement dues ni validation d'un procès-verbal devenu inexact n'est créée. D2232-8 et D2232-9 conservent délai de consultation, information et recours ; L2232-27 à L2232-29 demeurent applicables.")

rows=[]
for s in sources:
    n=s['number']
    historical = (' Note DILA lue intégralement et conservée dans la source : les dispositions historiques d’entrée en vigueur ne sont ni supprimées ni réactivées par cette réécriture.' if s['source_notes_xml'].strip() else ' La note DILA de la source est vide.')
    a={k:s[k] for k in ('code_id','source_id','source_sha256','number')}
    a.update(status='rewrite_draft',proposed_xml=texts[n],reason=reasons[n],benefit_review=benefits[n],review_notes=(notes[n]+' '+historical+' Les effets déjà produits, droits antérieurs et recours applicables sont conservés ; aucun accord existant n’est invalidé par cette seule réécriture. La rédaction reste un avant-projet sans validation juridique revendiquée.').strip())
    if n in cuts:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',removed_provisions=cuts[n])
    rows.append(a)
out=json.dumps(rows,ensure_ascii=False,indent=2)+'\n'
tmp=P/'answer.tmp';tmp.write_text(out);tmp.replace(P/'answer.json')
print(len(rows),hashlib.sha256(out.encode()).hexdigest())
