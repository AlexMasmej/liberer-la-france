import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
    }


add('L253-1-1', [
    "I. ― La convention d'usufruit répartit les dépenses de l'immeuble entre le nu-propriétaire et l'usufruitier. Pendant la durée de la convention, l'usufruitier paie seul les provisions prévues aux articles 14-1 et 14-2-1 de la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis qui lui incombent en application de cette convention.",
    "II. ― Lorsque la convention d'usufruit porte sur un ou plusieurs lots d'un immeuble soumis au statut de la copropriété, l'usufruitier est de droit le mandataire commun prévu au second alinéa de l'article 23 de la loi n° 65-557 du 10 juillet 1965 précitée, par dérogation à cet article. Il bénéficie d'une délégation de vote pour les décisions mentionnées à l'article 24, à l'article 25, à l'exclusion du n, et au c de l'article 26 de cette loi, dès lors qu'il en assume seul la charge financière définitive en application de la convention d'usufruit. Pour les autres décisions, il doit obtenir un mandat exprès. Par dérogation au troisième alinéa du I de l'article 22 de la même loi, il peut recevoir des nus-propriétaires plus de trois délégations de vote. Lorsque la convention d'usufruit porte sur l'intégralité des lots, la délégation de vote ne s'étend pas à la décision mentionnée au c de l'article 25.",
    "III. ― La convention d'usufruit précise la répartition des charges à son expiration, le sort des avances et provisions appelées pendant sa durée et les régularisations de charges intervenant après l'extinction de l'usufruit. Ces clauses ne sont pas opposables au syndicat des copropriétaires.",
],
    "Réécriture à droit constant : les obligations de paiement, l'étendue du mandat de l'usufruitier et les limites de la délégation de vote sont exprimées par des sujets explicites. Les trois subdivisions et leurs alinéas sont conservés. Aucune réforme de fond de policy.json ne concerne cette répartition en copropriété.",
    "Conserver le renvoi de la note source aux conditions d'entrée en vigueur du VI de l'article 171 de la loi n° 2021-1104 du 22 août 2021 ; cette note ne fixe aucune date pour la réforme projetée. Les renvois aux articles 14-1, 14-2-1, 22, 23, 24, 25 et 26 de la loi du 10 juillet 1965 sont maintenus, notamment l'exclusion du n de l'article 25 et celle du c du même article lorsque l'usufruit porte sur tous les lots. Aucun contrôle externe de cette loi n'a été effectué."
)

add('L253-2', [
    "Les logements dont l'usufruit est détenu par les bailleurs mentionnés à l'article L. 253-1 peuvent bénéficier d'un financement par prêts aidés, dans les conditions fixées par décret.",
    "Ces logements peuvent faire l'objet d'une convention mentionnée à l'article L. 831-1. La durée de cette convention est identique à celle de l'usufruit.",
    "Lorsqu'une convention mentionnée au deuxième alinéa du présent article est conclue, les articles L. 353-7 et L. 353-16 s'appliquent aux locataires et occupants présents à la date de sa conclusion.",
],
    "Réécriture à droit constant : séparation de la faculté de conventionnement et de la règle de durée, puis formulation directe des effets pour les occupants présents. Les trois alinéas, la faculté de financement et les renvois sont maintenus ; aucune réforme de fond n'est appliquée.",
    "Les articles L. 253-1, L. 831-1, L. 353-7 et L. 353-16 ont été consultés dans le corpus public local. L. 253-1 vise une personne morale sans énumérer davantage les bailleurs : le renvoi de la source est conservé. La durée de conventionnement reste exactement celle de l'usufruit ; les droits des locataires et occupants déjà présents ne sont pas réduits."
)

add('L253-3', [
    "Le bail doit indiquer expressément et de manière apparente le statut juridique du logement. Il doit aussi préciser la date limite de fin du contrat prévue à l'article L. 253-4 et reproduire les dispositions des articles L. 253-5 à L. 253-7.",
],
    "Réécriture à droit constant : les trois obligations d'information du bail sont réparties entre deux phrases, dans le même alinéa. Le terme ultime du contrat et l'obligation de reproduction intégrale des articles visés sont conservés, sans réforme de fond.",
    "La date limite de fin du contrat demeure celle de L. 253-4. Le bail doit reproduire L. 253-5, L. 253-6 et L. 253-7 dans leur rédaction coordonnée ; un simple renvoi ne satisfait pas cette obligation."
)

add('L253-4', [
    "Le bail conclu dans le cadre d'un usufruit prend fin de plein droit, au plus tard, à la date à laquelle les droits d'usufruit sur le bien loué s'éteignent.",
    "Les baux régis par le présent article ne sont pas soumis aux deuxième à quatrième alinéas de l'article 595 du code civil.",
],
    "Réécriture à droit constant : explicitation de l'extinction des droits et formulation directe de la dérogation au code civil. Les deux alinéas, la fin de plein droit et la limite maximale sont préservés ; aucune réforme de fond n'est introduite.",
    "Le terme reste une date maximale et n'exclut pas une fin antérieure du bail. Le renvoi porte exclusivement sur les deuxième à quatrième alinéas de l'article 595 du code civil. Le présent article ne dispense d'aucune procédure légale d'expulsion."
)

add('L253-5', [
    "Six mois avant l'extinction de l'usufruit, le nu-propriétaire peut, par lettre recommandée avec demande d'avis de réception, choisir l'une des démarches suivantes :",
    "– soit, s'il est occupant, informer l'usufruitier de son intention de renouveler la convention d'usufruit ;",
    "– soit proposer au locataire un nouveau bail prenant effet au terme de l'usufruit et conforme à la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986 ;",
    "– soit donner congé pour vendre ou pour occuper le bien, selon les modalités de l'article 15 de la loi n° 89-462 du 6 juillet 1989 précitée, avec effet au terme de l'usufruit. Dans ce cas, le nu-propriétaire peut valablement donner seul ce congé au locataire.",
    "La notification doit reproduire les dispositions du II de l'article L. 253-6 et de l'article L. 253-7.",
],
    "Réécriture à droit constant : présentation explicite des trois démarches ouvertes au nu-propriétaire et simplification de la phrase sur la validité du congé. Les cinq alinéas, le délai, la forme de notification, les alternatives et les mentions obligatoires sont conservés. Aucune réforme des congés ou du contentieux locatif n'est ajoutée.",
    "La condition « s'il est occupant » figurant dans la première alternative de la source est conservée. Elle soulève une difficulté d'articulation avec le cadre de la location du chapitre, à contrôler sans la supprimer ni la remplacer silencieusement. Maintien du délai de six mois et du renvoi à l'article 15 de la loi du 6 juillet 1989. L'accélération du traitement judiciaire des impayés prévue par policy.json appelle notamment une modification de l'article 24 de cette loi et des textes de procédure civile et d'exécution, hors de ce lot ; elle ne découle pas de cet article."
)

add('L253-6', [
    "I. – Un an avant l'extinction de l'usufruit, le bailleur doit rappeler au nu-propriétaire et au locataire les dispositions de l'article L. 253-5.",
    "II. – Trois mois avant l'extinction de l'usufruit, le bailleur doit proposer un logement à louer au locataire qui n'a pas conclu de nouveau bail avec le nu-propriétaire et qui remplit les conditions de ressources fixées par décret. Le logement proposé doit correspondre aux besoins et aux possibilités du locataire.",
    "Le manquement de l'usufruitier-bailleur à cette obligation ne peut être opposé au nu-propriétaire.",
],
    "Réécriture à droit constant : les obligations de rappel et d'offre de relogement sont rendues explicites. Les subdivisions I et II, les trois alinéas, les deux conditions cumulatives de l'offre et l'inopposabilité au nu-propriétaire sont maintenus, sans réforme de fond.",
    "Les échéances d'un an et de trois mois avant l'extinction de l'usufruit restent distinctes. Le II demeure celui que L. 253-5 impose de reproduire dans la notification. Les besoins et possibilités sont ceux du locataire ; le texte n'ajoute ni droit automatique au renouvellement ni dispense de condition de ressources."
)

add('L253-7', [
    "À l'expiration de l'usufruit, le locataire perd tout titre d'occupation du logement s'il n'a ni conclu le contrat de location proposé par le nu-propriétaire ni accepté l'offre de relogement de l'usufruitier-bailleur.",
],
    "Réécriture à droit constant : la conséquence juridique est placée en tête de phrase et les deux absences d'acceptation restent cumulatives. La date et l'étendue de la déchéance sont conservées dans un seul alinéa, sans réforme de fond.",
    "Coordination avec les offres et notifications de L. 253-5 et L. 253-6 et avec l'obligation de reproduction de L. 253-3. La perte du titre ne constitue pas une autorisation d'expulsion privée et ne modifie pas les procédures d'exécution."
)

add('L253-8', [
    "Le présent chapitre est d'ordre public lorsque les logements concernés sont des logements locatifs sociaux définis à l'article L. 302-5 ou des logements locatifs intermédiaires définis à l'article L. 302-16.",
],
    "Réécriture à droit constant : formulation directe de la condition qui rend le chapitre d'ordre public. Les deux catégories de logements et leurs renvois sont conservés ; aucune réforme de fond n'est appliquée.",
    "L. 302-16 a été consulté dans le corpus public local. Le caractère d'ordre public demeure subordonné aux catégories définies par L. 302-5 et L. 302-16 ; aucune convention locale n'est autorisée à écarter les obligations de logement social."
)

add('L254-1', [
    "Le bail réel immobilier est le contrat par lequel un propriétaire, personne physique ou personne morale de droit privé, consent pour une longue durée des droits réels à un preneur en vue de la location ou de l'accession temporaire à la propriété de logements. Le preneur est tenu de construire ou de réhabiliter des constructions existantes. Les logements doivent répondre aux conditions suivantes :",
    "1° Pendant toute la durée du contrat, ils sont destinés à être occupés à titre de résidence principale par des personnes physiques dont les ressources ne dépassent pas des plafonds fixés par décret en fonction de la typologie du ménage, de la localisation et du mode d'occupation du logement. Pour les logements donnés en location, ces plafonds ne peuvent être inférieurs à ceux prévus au chapitre unique du titre III du livre III ;",
    "2° Pendant toute la durée du contrat, leur prix d'acquisition ou, lorsqu'ils sont donnés en location, leur loyer ne dépasse pas des plafonds fixés par décret en fonction de la localisation du logement, de son type et, le cas échéant, de son mode de financement. Pour les logements donnés en location, ces plafonds ne peuvent être inférieurs à ceux prévus au chapitre unique du titre III du livre III.",
    "Les collectivités territoriales, leurs groupements, leurs établissements publics et les établissements publics fonciers de l'État peuvent également conclure ce contrat.",
    "Le présent chapitre régit le bail réel immobilier.",
    "Les personnes qui ont le droit d'aliéner peuvent consentir un bail réel immobilier pour une durée de dix-huit à quatre-vingt-dix-neuf ans. Le contrat ne peut prévoir aucune faculté de résiliation unilatérale et ne peut faire l'objet d'une tacite reconduction.",
    "Le preneur doit réaliser sur l'immeuble donné à bail les travaux mentionnés aux trois premiers alinéas, dans le respect des règles applicables à ces opérations. Sauf stipulations contraires, il ne peut exécuter d'autres ouvrages ou travaux que ceux prévus initialement.",
    "Les constructions et améliorations réalisées par le preneur lui appartiennent pendant le bail et deviennent la propriété du bailleur à son expiration. À l'issue du bail, le preneur ne peut, sauf stipulations contraires, demander d'indemnité pour les améliorations qu'il a réalisées.",
    "Le contrat détermine, le cas échéant, les activités accessoires qui peuvent être exercées dans l'immeuble donné à bail. Tout changement d'activité est soumis à l'accord du bailleur.",
],
    "Réécriture à droit constant : définition scindée en phrases, distinction lisible des plafonds de ressources et de prix, puis explicitation des obligations de travaux et des droits de propriété. Les neuf alinéas, les 1° et 2° et toutes les limites conventionnelles sont maintenus. Aucune réforme de fond des autorisations ou des normes techniques n'est greffée à ce régime de bail.",
    "Durée de dix-huit à quatre-vingt-dix-neuf ans maintenue ; plafonds et planchers réglementaires inchangés. Le renvoi aux trois premiers alinéas conserve sa cible malgré une formulation source peu précise : les travaux sont décrits au premier de ces alinéas. Le troisième alinéa reste le 2°, et les neuf emplacements d'alinéas sont préservés. Les démarches de transformation de bureaux relèvent des autorisations coordonnées du code de l'urbanisme, notamment L. 423-1, et les solutions techniques équivalentes du régime technique du CCH ; elles ne permettent pas d'écarter ici les conditions du bail."
)

add('L254-2', [
    "Le preneur ne peut apporter aucun changement qui diminue la valeur de l'immeuble. Sauf stipulation contraire, il ne peut démolir, en vue de les reconstruire, les ouvrages existants ou ceux qu'il a édifiés.",
    "Le preneur jouit librement des constructions de l'immeuble ainsi que des installations ou constructions qu'il a édifiées ou rénovées, à condition de ne porter atteinte ni à la destination de l'immeuble mentionnée à l'article L. 254-1 ni à l'état dans lequel il a été convenu de remettre ces constructions en fin de bail.",
    "Dans les conditions prévues aux articles L. 254-4 à L. 254-6, le preneur peut céder son droit au bail, céder son droit de propriété temporaire sur les constructions édifiées et consentir librement des baux sur l'immeuble. Ces baux prennent fin à l'expiration du bail réel immobilier, sauf si ce dernier prévoit leur continuation par le bailleur. Cette règle s'applique sous réserve du troisième alinéa de l'article L. 254-4. Le droit de propriété temporaire constitué prend fin à l'expiration du bail réel immobilier.",
    "Le preneur peut acquérir des servitudes actives et consentir les servitudes passives indispensables à la réalisation des constructions et ouvrages édifiés en application du bail. Il ne peut constituer de servitudes passives au-delà de la durée du bail qu'avec l'accord du bailleur.",
    "Le preneur doit maintenir en bon état d'entretien et de réparations les constructions existant à la conclusion du bail et celles qu'il réalise pendant sa durée. Il doit effectuer les réparations de toute nature sur les constructions existant au moment du bail et sur celles édifiées ensuite. Toutefois, il n'est pas tenu de les reconstruire s'il prouve qu'elles ont été détruites par cas fortuit ou force majeure, ou qu'elles ont péri en raison d'un vice de la construction antérieure au bail.",
    "Le preneur supporte toutes les charges, taxes et impôts relatifs à l'immeuble donné à bail et aux constructions réalisées.",
],
    "Réécriture à droit constant : les droits de jouissance, de cession et de constitution de servitudes sont formulés avec leurs limites ; les obligations de réparation et leur exception sont séparées en phrases. Les six alinéas de fond sont matérialisés par six paragraphes pour conserver, notamment, la cible du troisième alinéa. Aucune réforme de fond n'est ajoutée.",
    "Le troisième alinéa doit rester celui de la cession et de l'extinction des baux : L. 254-4 l'impose dans les contrats et y déroge. Maintien des renvois L. 254-4 à L. 254-6, de la possibilité de continuation prévue au contrat, de l'extinction du droit temporaire et de la preuve exigée pour l'exception de reconstruction. Le vice visé reste celui de la construction antérieure au bail."
)

add('L254-3', [
    "Le preneur doit payer une redevance dont le montant tient compte des conditions d'occupation des logements faisant l'objet du bail réel immobilier. Le fait de délaisser l'immeuble ne le libère ni du paiement de la redevance ni de l'exécution des conditions du bail.",
    "Le bail réel immobilier peut obliger le preneur à payer la redevance par avance pour tout ou partie de la durée du bail.",
    "Si le preneur n'exécute pas ses obligations contractuelles, le bailleur peut demander au juge la résiliation du bail réel immobilier, notamment lorsque le défaut de paiement de la redevance n'a pas été régularisé six mois après une mise en demeure signifiée par acte extrajudiciaire. En cas de résiliation amiable ou judiciaire, les baux d'habitation conclus par le preneur sont transférés de plein droit au bailleur.",
    "Le droit réel issu du bail réel immobilier et les constructions édifiées ou réhabilitées sur le terrain donné à bail peuvent être cédés dans les conditions de l'article L. 254-2 et hypothéqués. Ce droit peut être saisi selon les formes de la saisie immobilière. Les parties peuvent fixer librement la date d'échéance des sûretés qu'elles constituent. Si elles ne fixent pas cette date, les sûretés prennent fin lors de la résiliation du bail.",
],
    "Réécriture à droit constant : désignation directe du débiteur, explicitation de la demande de résiliation judiciaire et de la règle supplétive d'échéance des sûretés. Les quatre alinéas, le transfert des baux et le délai de régularisation sont conservés. Le délai propre à ce bail n'est pas modifié au titre de l'accélération générale du contentieux des impayés.",
    "Maintien des six mois après mise en demeure par acte extrajudiciaire pour le défaut de paiement visé, sans étendre ce délai à tous les autres manquements. Le transfert de plein droit concerne les baux d'habitation et intervient aussi en cas de résiliation amiable. La réforme du contentieux des impayés d'habitation appelle notamment l'article 24 de la loi n° 89-462 du 6 juillet 1989 et les textes procéduraux hors des cinq codes ; ce régime du bail réel immobilier reste distinct."
)

add('L254-4', [
    "Lorsque le titulaire des droits réels sur un logement faisant l'objet d'un bail réel immobilier décide de le mettre en location, le contrat de location doit reproduire en caractères apparents les dispositions de l'article L. 254-1 et du troisième alinéa de l'article L. 254-2. À défaut, le contrat de location est nul.",
    "Dans les baux qu'il consent en application de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986 et des chapitres II et III du titre III du livre VI du présent code, le preneur doit indiquer en caractères apparents la date d'extinction du bail réel immobilier et les effets de cette extinction sur le contrat de bail en cours.",
    "À défaut de cette indication, et par dérogation au troisième alinéa de l'article L. 254-2, les bénéficiaires du droit au bail d'habitation consenti en application de la loi n° 89-462 du 16 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986 peuvent se maintenir dans les lieux pendant trente-six mois à compter de l'expiration du bail réel immobilier. Ils doivent payer une indemnité d'occupation égale au dernier loyer d'habitation expiré et payable dans les mêmes conditions. Pour les bénéficiaires de baux consentis en application des chapitres II et III du titre III du livre VI du présent code, cette durée est réduite à douze mois.",
],
    "Réécriture à droit constant : séparation de l'obligation de reproduction et de sa sanction, puis clarification de l'indication obligatoire et du maintien temporaire dans les lieux en cas d'omission. Les trois alinéas, les durées et les conditions de l'indemnité sont préservés, sans réforme de fond.",
    "Anomalie préexistante conservée et signalée : le troisième alinéa de la source date la loi n° 89-462 du « 16 juillet 1989 », alors que le deuxième alinéa la date du 6 juillet 1989. Aucune correction silencieuse n'est faite. Les durées restent de trente-six mois et de douze mois ; l'indemnité reste égale au dernier loyer et payable dans les mêmes conditions. Le troisième alinéa de L. 254-2 est conservé à sa place dans la proposition correspondante."
)

add('L254-5', [
    "Pour tout projet de cession des droits réels relatifs aux logements faisant l'objet du bail réel immobilier, le cédant doit remettre à l'acquéreur une offre préalable d'acquisition. Cette offre mentionne expressément et en caractères apparents le caractère temporaire du droit réel et sa date d'extinction ; elle reproduit en termes apparents les dispositions du présent chapitre.",
    "Le cédant doit maintenir cette offre pendant au moins trente jours à compter de sa réception par l'acquéreur potentiel. Celui-ci ne peut l'accepter en signant une promesse de vente ou une vente avant l'expiration d'un délai de dix jours à compter de cette réception.",
    "Le non-respect des règles fixées aux alinéas précédents entraîne la nullité de la vente.",
    "Le cédant doit prouver le contenu de l'offre et sa notification.",
],
    "Réécriture à droit constant : le cédant est expressément désigné comme débiteur de l'offre et de la preuve ; les deux délais sont distingués. Les quatre alinéas et la nullité de la vente pour méconnaissance des règles précédentes sont conservés, sans réforme de fond.",
    "Les trente jours de maintien minimal et les dix jours avant acceptation ont tous deux pour point de départ la réception de l'offre par l'acquéreur potentiel. L'acceptation par promesse de vente est également visée. Coordonner la reproduction intégrale du chapitre avec l'ensemble des articles L. 254-1 à L. 254-9 ; aucune réduction des protections de L. 271-1 à L. 271-3 visées par L. 254-6."
)

add('L254-6', [
    "Les actes conclus pour acquérir des droits réels sur les logements faisant l'objet d'un bail réel immobilier sont soumis aux dispositions des articles L. 271-1 à L. 271-3 relatives à la protection de l'acquéreur.",
],
    "Réécriture à droit constant : les actes protégés sont placés en sujet de la phrase, sans modifier le champ des droits réels ni celui des protections applicables. L'alinéa unique et les renvois sont préservés ; aucune réforme de fond n'est introduite.",
    "Le renvoi reste à l'ensemble des articles L. 271-1 à L. 271-3. Il s'ajoute au dispositif d'offre préalable de L. 254-5 et ne le remplace pas."
)

add('L254-7', [
    "Sans préjudice des articles 515-6, 763 et 764 du code civil et par dérogation à l'article L. 254-4, les conditions de ressources définies à l'article L. 302-16 ne s'appliquent pas aux transmissions successorales des logements au conjoint survivant, quel que soit le régime matrimonial, ni au partenaire d'un pacte civil de solidarité prévu aux articles 515-1 à 515-7-1 du code civil, quel que soit le régime de ce pacte. Elles ne s'appliquent pas non plus aux personnes mentionnées à l'article 14 de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986, ni au conjoint survivant cotitulaire du bail dans les conditions de l'article 1751 du code civil. Ces bénéficiaires peuvent continuer à occuper les lieux.",
],
    "Réécriture à droit constant : la longue phrase est répartie en trois phrases au sein du même alinéa, en conservant chaque catégorie de bénéficiaires et son droit à poursuivre l'occupation. Les réserves, les régimes matrimoniaux et de pacte ainsi que les renvois demeurent ; aucune réforme de fond n'est appliquée.",
    "Le renvoi dérogatoire à L. 254-4 paraît peu directement articulé aux conditions de ressources, que L. 254-1 prévoit pour ce bail ; le renvoi de la source à L. 302-16, relatif aux logements intermédiaires, est également conservé. Ces articulations appellent contrôle et ne sont pas corrigées silencieusement. Aucune nouvelle dispense de plafond de prix n'est créée."
)

add('L254-8', [
    "Les contrats de bail réel immobilier conclus sans respecter l'article L. 254-1 sont nuls. Un décret en Conseil d'État précise les personnes qui peuvent exercer l'action en nullité et les conditions d'exercice de cette action.",
],
    "Réécriture à droit constant : formulation directe de la nullité et explicitation des titulaires de l'action. La sanction, le renvoi à L. 254-1 et la compétence du décret en Conseil d'État restent inchangés sur le fond.",
    "Le texte ne crée ni titulaire supplémentaire ni nouveau délai d'action. La détermination des titulaires et des conditions d'exercice demeure renvoyée au décret en Conseil d'État."
)

add('L254-9', [
    "Un décret en Conseil d'État fixe les modalités d'application du présent chapitre. Il détermine notamment les modalités de contrôle de l'affectation des logements, les sanctions en cas de méconnaissance de cette affectation et la méthode de calcul de la valeur des droits réels relatifs aux logements faisant l'objet du bail, applicable à chaque cession de ces droits.",
],
    "Réécriture à droit constant : la compétence réglementaire générale et ses objets particuliers sont séparés en deux phrases dans le même alinéa. Le caractère non exhaustif de l'énumération et l'application du calcul à chaque cession sont conservés ; aucune réforme de fond n'est introduite.",
    "La valeur visée reste celle des droits réels relatifs aux logements et non celle de la pleine propriété. Les contrôles et sanctions liés à l'affectation ne sont pas supprimés par les orientations de simplification des démarches."
)

add('L255-1', [
    "Le bail réel solidaire est le contrat par lequel un organisme de foncier solidaire consent des droits réels à un preneur, dans les conditions de l'article L. 329-1 du code de l'urbanisme et pour une durée comprise entre dix-huit et quatre-vingt-dix-neuf ans, en vue de la location ou de l'accession à la propriété de logements. Le preneur est tenu, s'il y a lieu, de construire ou de réhabiliter des constructions existantes.",
    "Pendant toute la durée du contrat, ces logements sont destinés à être occupés à titre de résidence principale.",
],
    "Réécriture à droit constant : la définition et l'obligation éventuelle de travaux sont séparées en phrases ; la destination des logements reste dans son alinéa. La durée, les finalités et le renvoi au code de l'urbanisme sont maintenus, sans réforme de fond.",
    "L'article L. 329-1 du code de l'urbanisme a été consulté dans le corpus public local. La durée reste comprise entre dix-huit et quatre-vingt-dix-neuf ans. Le bail réel solidaire demeure un régime distinct du bail réel immobilier et conserve l'exigence de résidence principale pendant toute sa durée."
)

add('L255-2', [
    "Un bail réel solidaire peut être consenti à un preneur qui occupe le logement. Un décret en Conseil d'État fixe les plafonds du prix de cession des droits réels et des ressources du preneur.",
    "L'organisme de foncier solidaire peut appliquer des seuils inférieurs à ces plafonds en fonction de ses objectifs et des caractéristiques de chaque opération.",
    "En fonction de ses objectifs et des caractéristiques de chaque opération, le contrat de bail peut obliger le preneur à occuper le logement faisant l'objet des droits réels et lui interdire de le louer.",
],
    "Réécriture à droit constant : présentation directe de la fixation des plafonds et de la faculté contractuelle d'imposer l'occupation personnelle. Les trois alinéas, la modulation à la baisse et les critères propres à chaque opération sont conservés, sans réforme de fond.",
    "Les plafonds ne sont ni chiffrés ni relevés : ils demeurent fixés par décret en Conseil d'État. Le troisième alinéa conserve la référence aux objectifs et caractéristiques de chaque opération sans substituer un autre titulaire aux termes de la source. La faculté d'interdire la location reste contractuelle, et n'est pas transformée en interdiction générale."
)

add('L255-3', [
    "Un bail réel solidaire peut être consenti à un opérateur qui, le cas échéant, construit ou réhabilite des logements. Cet opérateur s'engage à vendre les droits réels immobiliers attachés à ces logements à des bénéficiaires remplissant les conditions de ressources fixées en application de l'article L. 255-2 et à un prix fixé en application de ce même article, ou à proposer la souscription de parts ou d'actions permettant à ces bénéficiaires de jouir du bien, dans le respect des conditions de l'article L. 255-2.",
    "En cas de vente, celle-ci doit respecter les conditions et délais des articles L. 255-10-1, L. 255-11-1, L. 255-13 et L. 255-15.",
    "La cession des droits réels immobiliers par l'opérateur à chaque preneur établit un lien direct et individuel entre l'organisme de foncier solidaire et ce preneur. Elle désolidarise les preneurs entre eux ainsi que chaque preneur de l'opérateur.",
    "À l'issue de la cession, le preneur est réputé titulaire d'un bail réel solidaire portant sur son logement. Ce bail a une date de prise d'effet propre à ce preneur, fixée au jour de la cession.",
],
    "Réécriture à droit constant : les deux engagements possibles de l'opérateur sont distingués et les effets de la cession sont répartis en phrases courtes. Les quatre alinéas, les conditions de ressources et de prix, les délais par renvoi et la prise d'effet individuelle sont maintenus, sans réforme de fond.",
    "Maintien exact des renvois L. 255-10-1, L. 255-11-1, L. 255-13 et L. 255-15. La cession produit le lien individuel et la désolidarisation ; ces effets ne sont pas étendus sans texte à une simple proposition de souscription. La date d'effet reste le jour de chaque cession, sans date législative nouvelle."
)

add('L255-4', [
    "Un bail réel solidaire peut être consenti à un opérateur qui s'engage à mettre des logements en location et, le cas échéant, les construit ou les réhabilite.",
    "Un décret en Conseil d'État fixe les plafonds du loyer applicable et des ressources du locataire.",
    "L'organisme de foncier solidaire peut imposer des seuils inférieurs à ces plafonds en fonction de ses objectifs et des caractéristiques de chaque opération.",
],
    "Réécriture à droit constant : mise en évidence de l'engagement locatif et de la répartition entre fixation réglementaire des plafonds et abaissement par l'organisme. Les trois alinéas et le caractère éventuel des travaux sont préservés, sans réforme de fond.",
    "Aucun montant de loyer ni plafond de ressources n'est inventé. La faculté de l'organisme reste limitée à des seuils inférieurs et liée aux objectifs et caractéristiques de l'opération. Les plafonds de ce régime ne sont pas confondus avec ceux du bail réel immobilier."
)

add('L255-5', [
    "En cas de mutation, le prix de vente ou la valeur maximale des droits réels immobiliers, des parts et des actions permettant la jouissance du bien ne peut dépasser leur valeur initiale, actualisée selon les modalités fixées par décret en Conseil d'État.",
    "L'acquéreur, le donataire ou l'ayant droit à la succession portant sur les droits réels immobiliers, les parts ou les actions donnant droit à l'attribution en jouissance du bien doit remplir les conditions définies aux articles L. 255-2, L. 255-3 ou L. 255-4.",
],
    "Réécriture à droit constant : formulation du plafond de valeur sous la forme d'une interdiction de dépassement et clarification de l'objet de la transmission. Les deux alinéas, l'actualisation réglementaire et chaque catégorie de bénéficiaire demeurent, sans réforme de fond.",
    "La règle couvre les mutations et non seulement les ventes : le donataire et l'ayant droit à la succession restent visés. La méthode d'actualisation n'est ni remplacée par un taux inventé ni confondue avec une valeur de marché libre. Les renvois alternatifs à L. 255-2, L. 255-3 ou L. 255-4 sont maintenus."
)

add('L255-6', [
    "Le bail réel solidaire ne peut accorder au bailleur une faculté de résiliation unilatérale que dans les cas prévus au présent chapitre. Il ne peut faire l'objet d'une tacite reconduction.",
],
    "Réécriture à droit constant : séparation de la limite à la résiliation unilatérale et de l'interdiction de tacite reconduction, dans le même alinéa. Les exceptions légales et le seul bailleur visé par la première règle sont conservés, sans réforme de fond.",
    "Ne pas appliquer au bail réel solidaire l'interdiction de toute faculté de résiliation unilatérale du bail réel immobilier prévue à L. 254-1 : les cas admis par le présent chapitre sont maintenus. Aucune nouvelle cause de résiliation n'est créée."
)

add('L255-7', [
    "Le preneur doit, s'il y a lieu, effectuer les travaux de construction ou de réhabilitation prévus par le bail réel solidaire. Sauf stipulations contraires ou avenant au bail, il ne peut exécuter d'autres ouvrages ou travaux que ceux prévus initialement. Cette restriction ne s'applique pas aux travaux nécessaires à la conservation du bien en état d'usage, réalisés conformément aux stipulations du bail.",
    "Le preneur ne peut apporter aucun changement qui diminue la valeur de l'immeuble. Sauf stipulation contraire du bail, il ne peut démolir les ouvrages existants ou ceux qu'il a édifiés ou réhabilités, même en vue de les reconstruire.",
    "Les constructions et améliorations réalisées par le preneur lui appartiennent pendant le bail et deviennent la propriété de l'organisme de foncier solidaire à l'expiration du bail.",
    "Le preneur jouit librement des droits réels immobiliers ainsi que des installations ou constructions qu'il a édifiées, rénovées ou réhabilitées, à condition de ne porter atteinte ni à la destination de l'immeuble ni à l'état dans lequel il a été convenu de remettre ces droits réels immobiliers en fin de bail.",
    "Le contrat détermine, le cas échéant, les activités accessoires qui peuvent être exercées dans le bien donné à bail. Tout changement d'activité ou d'affectation est soumis à l'accord de l'organisme de foncier solidaire.",
    "Le preneur peut acquérir des servitudes actives et consentir les servitudes passives indispensables à la réalisation des constructions et ouvrages édifiés ou à réhabiliter en application du bail. Il ne peut constituer de servitudes passives au-delà de la durée du bail qu'avec l'accord de l'organisme de foncier solidaire.",
    "Le preneur doit maintenir en bon état d'entretien et de réparations les constructions existant à la conclusion du bail et celles qu'il réalise pendant sa durée. Il doit effectuer les réparations de toute nature sur les constructions existant au moment du bail et sur celles édifiées ensuite. Toutefois, il n'est pas tenu de les reconstruire s'il prouve qu'elles ont été détruites par cas fortuit ou force majeure, ou qu'elles ont péri en raison d'un vice de la construction antérieure au bail. En cas de sinistre entraînant la résiliation du bail, le preneur est indemnisé de la valeur de ses droits réels dans les conditions prévues par le bail.",
    "Dans les immeubles en copropriété où tous les logements ou, à défaut, tous les logements d'un volume distinct font l'objet de baux réels solidaires auprès du même organisme de foncier solidaire, les titulaires de ces baux confèrent au syndicat des copropriétaires la gestion de leurs droits réels indivis. Cette gestion complète les missions attribuées au syndicat, notamment par l'article 14 de la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis. Le règlement de copropriété peut également confier au syndic un mandat de recouvrement des redevances en application de l'article L. 255-8 du présent code.",
],
    "Réécriture à droit constant : séparation des interdictions et exceptions de travaux, explicitation des obligations d'entretien et de réparation, puis clarification du rôle du syndicat et du syndic. Les huit alinéas, l'indemnisation après sinistre, les droits de propriété et les limites de jouissance sont maintenus. Aucune réforme de fond des normes de construction n'est appliquée à ces stipulations de bail.",
    "Les travaux de conservation restent admis conformément au bail, sans suppression des réserves de stipulation contraire ou d'avenant. Le vice visé est celui de la construction antérieure au bail ; le preneur doit en apporter la preuve. L'indemnisation suppose un sinistre entraînant la résiliation. La gestion des droits indivis suppose tous les logements de l'immeuble ou, à défaut, d'un volume distinct sous baux réels solidaires auprès du même organisme. L. 255-8 a été consulté dans le corpus local ; le mandat de recouvrement demeure facultatif. La voie de rénovation locative limitée à vingt-quatre mois appelle notamment les articles 6 et 20-1 de la loi n° 89-462 du 6 juillet 1989 et son décret n° 2002-120 du 30 janvier 2002, hors des cinq codes, pour les conditions de décence, les travaux contrôlés et la compensation des surcoûts énergétiques ; elle n'est pas instaurée par cet article."
)


assert len(sources) == 24
assert len(drafts) == 24
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    item['status'] = 'rewrite_draft'
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
