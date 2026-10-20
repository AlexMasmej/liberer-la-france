import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', s))).strip()


def effect(kind, measure, description, before, after, unit, population, transition,
           old_quote, new_quote, replacements='Aucune obligation, donnée, autorisation ou recette de remplacement n’est créée.'):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacements,
                source_quote=old_quote, proposed_quote=new_quote)


def put(number, reason, notes, assessment, limitations, burdens, proposed=None,
        classification='retained_necessary', effects=None, benefit=None, removed=None,
        repeal=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        out['classification'] = 'retained_necessary'
    if benefit:
        out['benefit_review'] = benefit
    if removed:
        out.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal:
        out.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    out['substantive_impact'] = dict(version=1, classification=classification,
                                    assessment=assessment, scope_limitations=limitations,
                                    new_burdens_review=burdens, effects=effects or [])
    answers[number] = out


put('L443-15-5-3',
    'Maintien intégral après examen des cinq obligations : pendant le transfert différé des parties communes, l’organisme reste responsable de leur conservation et de leur financement. L’information annuelle permet aux acquéreurs privés des organes de copropriété de contrôler cette gestion ; l’interdiction d’une association parallèle évite une gestion concurrente des mêmes parties. Aucune simple réécriture stylistique.',
    'L443-15-5-1 et L443-15-5-2 lus : transfert différé au plus dix ans et date commune aux lots. R443-17-4 à R443-17-6 lus : l’information annuelle couvre aussi les travaux, les charges et, dans certains cas, la consommation thermique. La supprimer isolément laisserait des garanties sans support. Les cinq numéros restent intacts ; aucun quota communal SRU ne résulte de cette gestion.',
    'Aucune réduction nouvelle revendiquée : les cinq dispositions assurent la gestion unique et la transparence d’un patrimoine encore détenu par le vendeur.',
    'Le maintien ne chiffre pas les coûts de gestion et ne vaut pas examen achevé de toute la loi SRU ou de toutes les ventes HLM.',
    'Aucune charge nouvelle identifiée : texte source intégralement maintenu, sans réunion, registre ou transmission supplémentaires.',
    benefit='Les acquéreurs conservent la prise en charge des gros travaux par le vendeur, la protection de la valeur et de la jouissance de leur lot et l’information annuelle, pour toutes les ventes futures éligibles pendant le transfert différé.')

put('L443-15-5-4',
    'Maintien intégral de l’accès strictement limité aux travaux nécessaires ou obligatoires. Le délai d’information de huit jours protège le domicile et comporte déjà une exception de sécurité ou de conservation ; il n’est donc pas supprimé. L’indemnisation des troubles graves et dégradations reste entière.',
    'Les 1° et 2° et les deux alinéas finaux sont conservés. Le renvoi à l’article 1er de la loi de 1967 concerne les normes du logement, non une relation de travail. Son texte extérieur n’est pas fourni dans ce lot ; aucune recodification supposée n’est opérée. Les contrôles de références ci-dessous distinguent expressément les trois cibles professionnelles requises.',
    'La source contient des protections de sécurité, du domicile et du droit à réparation ; aucune obligation accessoire séparable de ces fonctions n’est démontrée.',
    'Le délai de huit jours est celui de l’accès au logement ; ni les préavis d’emploi ni les indemnités de licenciement ne sont modifiés par ce maintien.',
    'Aucune charge nouvelle identifiée : mêmes travaux, même notification, mêmes exceptions urgentes et même réparation que dans la source.',
    benefit='Le droit à indemnité demeure ouvert aux futurs acquéreurs subissant un trouble de jouissance grave, même temporaire, ou des dégradations. La condition interdisant une altération durable du logement demeure également.')

put('L443-15-5-5',
    'Maintien intégral du droit réel d’usage et des trois contreparties limitatives de la contribution. Il s’agit du coût de services et d’entretien effectivement liés au logement, non d’un prélèvement fiscal accessoire. Supprimer les contreparties ou le droit d’usage déséquilibrerait le régime favorable de transfert différé.',
    'L443-15-5-1 et R443-17-2 à R443-17-6 lus. Les limites réglementaires de récupération, exclusions de dépenses, régularisations, justificatifs et paiement par douzièmes demeurent distincts et ne sont pas étendus par le présent maintien. Aucun montant ni taux de contribution nouveau.',
    'Le droit d’usage et la délimitation des charges sont maintenus sans les présenter comme une suppression de taxe ou une baisse de cotisations.',
    'Les économies possibles sur les services ou leurs prix ne sont pas établies ; le maintien ne préjuge pas de la réforme de taxes frappant le prestataire.',
    'Aucune charge nouvelle identifiée : les trois catégories existantes restent inchangées et aucun fichier, justificatif ou prélèvement de substitution n’est institué.',
    benefit='Le droit d’usage réel reste ouvert dès la vente aux futurs acquéreurs et jusqu’au transfert des parties communes. Les trois contreparties légales et les exclusions réglementaires protègent leur contribution sans en élargir l’assiette.')

put('L443-15-5-6',
    'Maintien intégral de la substitution de plein droit lors des mutations : elle dispense précisément d’un nouvel agrément ou contrat avec le vendeur et assure la continuité du droit d’usage et des obligations attachées au lot.',
    'Les mutations entre vifs volontaires ou forcées et à cause de mort restent toutes couvertes. La mention du décès est une règle civile de transmission ; elle ne constitue ni droit de succession ni prélèvement sur capital et n’est pas supprimée par la décision successions.',
    'La continuité civile automatique est nécessaire et déjà simplificatrice dans le droit source ; aucun allègement nouveau ne lui est attribué.',
    'Le maintien ne traite pas les droits fiscaux des donations ou les formalités civiles et foncières prévus par d’autres textes.',
    'Aucune charge nouvelle identifiée : aucune autorisation, notification ou pièce nouvelle ne conditionne la substitution de plein droit.',
    benefit='Les successeurs futurs, y compris héritiers et légataires, conservent automatiquement les droits de l’acquéreur. Le maintien de cette transmission civile ne fait renaître aucun impôt successoral supprimé.')

put('L443-15-5-7',
    'Maintien intégral de l’articulation entre la vente HLM, le transfert différé des parties communes et la garantie de rachat. Cette clause d’application évite un doublon de régime et maintient les dispositions particulières plus adaptées à la sous-section.',
    'L443-15-5-1 et L443-15-8 lus intégralement, ainsi que R443-12-2. La référence à la sous-section 1 s’entend des dispositions en vigueur après leurs propres coordinations ; elle ne rend pas applicables des quotas, carences ou prélèvements abrogés. Aucun texte extérieur n’est rétabli par cette clause.',
    'Aucune réduction nouvelle : la réserve de spécialité et l’application de la garantie décennale sont nécessaires aux acquéreurs.',
    'La clause ne réalise pas à elle seule la réécriture de chaque disposition de la sous-section 1 ni l’examen des 209 articles SRU.',
    'Aucune charge nouvelle identifiée : aucun second dossier ni régime d’autorisation n’est ajouté à l’application des règles existantes.',
    benefit='La garantie de rachat de L443-15-8 demeure applicable aux futurs contrats de vente à transfert différé qui satisfont ses conditions, avec les dispositions particulières de la présente sous-section.')

put('L443-15-5-8',
    'Maintien intégral de l’habilitation qui encadre les charges et leurs modalités de paiement. Elle constitue le fondement des limites opposables au vendeur et des régularisations favorables ; elle n’institue ni taxe, ni agrément, ni déclaration autonome.',
    'R443-17-2 à R443-17-6 lus en entier. Les plafonds de récupération et exclusions de R443-17-3 et le règlement par douzièmes de R443-17-4 ne doivent pas disparaître avec leur habilitation. Les dispositions réglementaires ne sont pas réécrites dans ce lot.',
    'Le maintien conserve un encadrement utile des charges privées ; aucun gain nouveau de conformité ou baisse de prélèvement n’est revendiqué.',
    'Cette habilitation ne chiffre pas le coût des prestations et ne permet pas d’augmenter la liste légale des contreparties de L443-15-5-5.',
    'Aucune charge nouvelle identifiée : l’habilitation existante est maintenue sans nouveau décret obligatoire, dépôt ou collecte de données.',
    benefit='Les limitations de charges, les exclusions des dépenses de personnel et les modalités favorables de régularisation continuent de bénéficier aux futurs acquéreurs dans le champ du transfert différé.')

n = 'L443-15-7'
proposal = '''<p>Est institué dans les communes qui le souhaitent un guichet unique dans le cadre d'une procédure d'accession sociale à la propriété.</p>
<p>Dans les mairies, ce guichet unique met à la disposition du public un dossier présentant l'ensemble des dispositifs de soutien à l'accession sociale à la propriété.</p>
<p>Aucune transmission de projets de vente, d'informations sur les opérations d'accession sociale à la propriété ou d'informations sur les prêts n'est obligatoire à la seule fin d'alimenter ce guichet. Les communications volontaires et l'utilisation des informations légalement accessibles demeurent possibles dans les conditions qui leur sont applicables.</p>
<p>Cette dispense s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux demandes de communication antérieures qui n'ont pas encore été satisfaites. Elle ne modifie ni les conditions d'accès aux dispositifs de soutien, ni les droits et engagements nés de leur attribution, ni les obligations d'information ayant un autre fondement légal.</p>'''
put(n,
    'Réduction de fond : suppression des transmissions obligatoires à la demande du maire concernant les projets de vente des bailleurs, les opérations des promoteurs et les offres de prêt. Le guichet communal reste facultatif et son information du public est conservée ; aucun circuit déclaratif ne remplace ces trois transmissions.',
    'Les deux premiers alinéas sont conservés. La liste documentaire supprimée ne créait pas les aides qu’elle citait : les prêts de L312-1, lu en entier, et les droits issus des dispositifs fiscaux conservent leur régime propre. La référence historique à 244 quater J n’est pas transformée en nouvelle aide ; les prêts récents relèvent de textes distincts. Aucun droit futur éligible n’est fermé. Les demandes en cours deviennent également non obligatoires, sans effacer les obligations autonomes envers acquéreurs ou autorités de contrôle.',
    'Trois catégories de communications imposées aux opérateurs et prêteurs pour le seul guichet sont effectivement retirées ; maintien de la faculté communale et de l’accès du public aux aides.',
    'Aucun gain financier national établi ; les informations volontairement fournies ou dues sur un autre fondement restent hors de la dispense.',
    'Aucune charge nouvelle identifiée : ni déclaration équivalente, ni collecte de remplacement, ni registre nouveau ; le dossier public existant demeure.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('obligation_removed', 'accession-sociale-guichet-fin-transmissions',
                    'Fin du reporting obligatoire des trois catégories de documents au maire pour alimenter le guichet.',
                    'Sur demande du maire, communication imposée des projets de vente, opérations d’accession et informations de prêts des opérateurs concernés.',
                    'Aucune communication obligatoire sur ce seul fondement, y compris pour les demandes non satisfaites ; information communale maintenue.',
                    'legal_duty', 'Bailleurs sociaux, promoteurs privés ou sociaux et établissements de crédit ou sociétés de financement concernés.',
                    'Dès l’entrée en vigueur ; autres informations légalement dues et droits aux aides inchangés.',
                    'Sont notamment communiqués à cette fin aux maires, à leur demande :',
                    "Aucune transmission de projets de vente, d'informations sur les opérations d'accession sociale à la propriété ou d'informations sur les prêts n'est obligatoire à la seule fin d'alimenter ce guichet.")],
    benefit='Le guichet unique et son dossier public demeurent ; la suppression des envois ne supprime aucun prêt, garantie, avance sans intérêt, aide ou exonération, pour les situations futures éligibles aussi bien que les engagements antérieurs.',
    removed=['Communication obligatoire au maire des projets de ventes de logements à leurs locataires par les bailleurs sociaux.',
             'Communication obligatoire au maire des informations relatives aux opérations des promoteurs privés ou sociaux situées dans la commune.',
             'Communication obligatoire au maire des informations de prêts proposés aux ménages modestes par les établissements de crédit et sociétés de financement.'])

put('L443-15-8',
    'Maintien intégral de la garantie de rachat de dix ans : l’obligation contractuelle protège les ménages éligibles contre une perte d’emploi, une rupture familiale ou un problème de santé. Elle n’est pas un agrément ou un reporting redondant à supprimer.',
    'L443-1 et R443-12-2 lus : conditions de ressources, d’occupation et d’apport d’une part ; mise en jeu, délai d’un an, prix minimal de 80 %, minoration maximale de 1,5 % des sixième à dixième années et trois devis pour dégradations d’autre part. Ces règles réglementaires restent à leur champ propre. La perte d’emploi est un événement de logement, sans condition nouvelle d’ancienneté ni exclusion des futurs contrats uniques.',
    'Garantie sociale intégralement conservée ; aucune suppression de charge ne peut être attribuée à ce maintien.',
    'Le lot ne modifie pas les modalités réglementaires de mise en jeu ni les droits des prêteurs et ne chiffre pas le coût de la garantie.',
    'Aucune charge nouvelle identifiée : même clause, même durée et mêmes bénéficiaires que dans la source officielle.',
    benefit='La garantie de rachat systématique de dix ans reste ouverte à toutes les futures personnes physiques remplissant L443-1. Les trois événements protégés et les garanties réglementaires ne sont pas réservés aux anciens contrats ou aux anciens CDD.')

proposal = "<p>Les pensionnés de guerre ayant un taux d'invalidité égal ou supérieur à 50 p. 100 peuvent, s'ils bénéficient de prêts destinés à faciliter l'acquisition ou la construction d'habitations à loyer modéré, obtenir certains avantages dans les conditions fixées en vertu de l'article L. 443-1.</p>"
put('L443-16',
    'Coordination nécessaire : donner au bénéfice conservé un corps autonome sans le faire dépendre de la référence historique à L325 du code des pensions militaires. Le seuil de 50 %, les prêts concernés et le renvoi à L443-1 sont intégralement conservés ; aucune baisse d’impôt ou nouvelle aide n’est annoncée.',
    'L443-1 lu en entier : ressources, occupation et apport personnel restent régis par les décisions prises sur son fondement. Le code extérieur des pensions n’est pas joint au corpus fourni : aucune nouvelle numérotation n’est inventée et aucune abrogation extérieure n’est affirmée. La suppression de la formule introductive vise à éviter une dépendance à cette référence historique non concordée ; une concordance extérieure demeure à documenter, sans fermeture du bénéfice dans ce texte.',
    'La disposition favorable devient autonome sans modifier les personnes, opérations ou conditions ; il s’agit d’une coordination, pas d’une réduction nouvelle.',
    'La concordance du code des pensions militaires reste non documentée dans le contexte local ; aucune réforme de ses avantages propres n’est présentée comme accomplie.',
    'Aucune charge nouvelle identifiée : le seuil, les prêts et les conditions de L443-1 sont ceux de la source, sans dossier ni justificatif ajouté.',
    proposed=proposal, classification='coordination_only',
    effects=[effect('coordination', 'pensionnes-guerre-accession-fondement-autonome',
                    'Autonomie du fondement CCH des avantages, sans substitution d’un numéro extérieur non vérifié.',
                    'Avantages des pensionnés invalides à au moins 50 %, introduits par une référence à L325 du code des pensions.',
                    'Même bénéfice et mêmes conditions de L443-1, sans dépendance à cette référence introductive.',
                    'other', 'Pensionnés de guerre invalides à au moins 50 % empruntant pour acquérir ou construire une HLM.',
                    'Continuité du bénéfice pour opérations antérieures et futures éligibles ; aucune nouvelle condition.',
                    "Conformément à l'article L. 325 du code des pensions militaires d'invalidité et des victimes de guerre,",
                    "Les pensionnés de guerre ayant un taux d'invalidité égal ou supérieur à 50 p. 100 peuvent,")],
    benefit='Les avantages d’accession des pensionnés de guerre invalides à au moins 50 % restent ouverts aux futurs prêts éligibles sous les mêmes conditions de L443-1. Aucun seuil plus élevé ni restriction aux opérations antérieures ne sont ajoutés.')

proposal = by_number['L443-17']['source_xml'].replace("Conformément à l'article L. 326 du code des pensions militaires d'invalidité et des victimes de guerre, les invalides", 'Les invalides').replace('ayant ouvert droit à pension au titre de ce code', "ayant ouvert droit à pension au titre du code des pensions militaires d'invalidité et des victimes de guerre,")
put('L443-17',
    'Coordination nécessaire et limitée : conserver le fonds de garantie et ses conditions dans une disposition autonome, en retirant seulement la formule de renvoi historique à L326 du code des pensions. Aucune formalité du fonds n’est assimilée à une taxe de succession ou à une autorisation d’emploi.',
    'Les quatre alinéas sont conservés avec gestion CDC, demandes à l’Office national des combattants et des victimes de guerre, enveloppe annuelle et prise en compte de la surprime. L443-2 lu : la condition visée reste l’assurance des annuités au décès, non une condition générale d’emploi. La note du 1er janvier 2023 est une entrée en vigueur historique du nom de l’Office. Concordance du code extérieur des pensions non fournie : aucun numéro de remplacement n’est inventé ; ses règles propres restent à vérifier séparément.',
    'Coordination de fondement seulement : le mécanisme de garantie des invalides de guerre et la sélection dans les ressources disponibles demeurent entiers.',
    'Aucune hausse de crédit ni automaticité de garantie n’est démontrée ; le code des pensions extérieur au corpus n’est pas déclaré réécrit.',
    'Aucune charge nouvelle identifiée : même demande de garantie, même gestionnaire et mêmes limites budgétaires et de risque que la source.',
    proposed=proposal, classification='coordination_only',
    effects=[effect('coordination', 'pensionnes-guerre-accession-fondement-autonome',
                    'Conservation autonome de la garantie lorsque l’invalidité de guerre empêche de satisfaire la condition d’assurance.',
                    'Fonds spécial et conditions de L443-2 avec référence introductive à L326 du code des pensions.',
                    'Même fonds et mêmes critères sans dépendance à la référence introductive non concordée.',
                    'other', 'Invalides de guerre empêchés de satisfaire la condition du premier alinéa de L443-2.',
                    'Maintien continu des garanties et de l’accès futur selon disponibilités ; pas de nouvelle allocation budgétaire.',
                    "Conformément à l'article L. 326 du code des pensions militaires d'invalidité et des victimes de guerre,",
                    "Les invalides de guerre qui, par suite de blessures ou de maladies ayant ouvert droit à pension au titre du code des pensions militaires d'invalidité et des victimes de guerre")],
    benefit='La garantie du fonds spécial demeure accessible aux nouvelles demandes des invalides de guerre éligibles, selon les crédits et ressources du fonds ; les garanties déjà accordées ne sont pas retirées. La demande reste utile pour identifier le risque couvert.')

proposal = """<p>Le taux des intérêts moratoires en cas de retard dans les remboursements dus aux organismes d'habitations à loyer modéré par leurs adhérents ou emprunteurs ne peut dépasser le taux plafond fixé par décision administrative en application de l'article L. 431-2.</p>
<p>Ce plafond s'applique aux contrats en cours, nonobstant toute clause contraire. Une stipulation fixant un taux inférieur au plafond conserve son effet.</p>"""
put('L443-18',
    'Coordination nécessaire avec L431-2 proposé : viser expressément le taux administratif comme plafond, sans transformer ce plafond en taux uniforme imposé aux adhérents. La protection des contrats en cours et des stipulations inférieures est maintenue, sans taux chiffré nouveau.',
    'L431-2 officiel et sa proposition lus en entier. La source L443-18 pose déjà un maximum ; la précision conserve cet avantage et lève l’ambiguïté de « Ce taux s’applique ». La transition des intérêts antérieurs et futurs relève de L431-2 proposé ; aucune remise de capital, remboursement général ou baisse chiffrée propre à L443-18. Pas de nouveau renvoi : la cible existante conserve son numéro et sa fonction de plafond.',
    'Coordination du plafond déjà favorable ; aucun allègement supplémentaire n’est compté par rapport au maximum prévu dans la source entière.',
    'Le taux administratif applicable n’est pas chiffré ici ; l’effet de la réforme distincte de L431-2 ne devient pas une seconde baisse dans cet article.',
    'Aucune charge nouvelle identifiée : aucun avis, délai, pièce ou registre ajouté ; le renvoi existant est précisé et les clauses plus favorables conservées.',
    proposed=proposal, classification='coordination_only',
    effects=[effect('coordination', 'interets-moratoires-prets-etat-plafond',
                    'Maintien du rôle de plafond du taux administratif après la réécriture de L431-2.',
                    'Intérêts dus aux HLM plafonnés au taux de L431-2, y compris contrats en cours.',
                    'Même plafond administratif explicitement identifié, avec maintien des clauses inférieures.',
                    'other', 'Adhérents ou emprunteurs débiteurs d’un organisme HLM en retard de remboursement.',
                    'Plafond applicable aux contrats en cours ; les intérêts anciens restent soumis à la transition de la réforme de L431-2.',
                    "ne peut dépasser le taux prévu à l'article L. 431-2.",
                    "ne peut dépasser le taux plafond fixé par décision administrative en application de l'article L. 431-2.")],
    benefit='Le plafond des intérêts et son application aux contrats en cours demeurent ; toute clause inférieure reste favorable. Les futurs prêts et futurs retards dans le champ de l’article bénéficient aussi du plafond, sans limitation aux dettes anciennes.')

put('L444-1',
    'Maintien intégral de la faculté des organismes désignés de mobiliser les logements vacants par prise à bail et sous-location. Le texte ouvre une compétence sans imposer agrément, déclaration ni durée supplémentaires.',
    'La référence L422-3 reste organique ; la réforme des coopératives ne supprime pas leur habilitation. L444-2 a été lu : son accord communal fondé sur le taux de logements sociaux est retiré dans sa proposition propre, non rétabli par l’application du présent chapitre. Les conditions de logement et protections locatives autonomes demeurent.',
    'La faculté de mobilisation de logements vacants est nécessaire et favorable ; maintien sans allègement artificiellement compté.',
    'Aucune extension de catégories d’organismes ni modification des régimes locatifs de sections distinctes n’est opérée par ce maintien.',
    'Aucune charge nouvelle identifiée : texte source inchangé, sans nouvel accord communal, enregistrement ou justificatif.',
    benefit='La prise à bail de logements vacants reste possible pour les futures opérations des offices, sociétés anonymes HLM et coopératives visées, sans réserve aux seuls contrats déjà conclus.')

put('L444-3',
    'Maintien intégral des caractéristiques de décence et de la faculté de mandater l’organisme pour les travaux. La salubrité et la sécurité ont une fonction essentielle ; le mandat facultatif simplifie la réalisation des travaux sans nouvelle autorisation.',
    'Le renvoi conserve les premier et deuxième alinéas de l’article 6 de la loi de 1989 ; le texte extérieur n’est pas reproduit dans les sources assignées. Le parcours de rénovation de vingt-quatre mois annoncé par policy exige une coordination distincte de cette loi et de ses procédures, avec contrôle et compensation des surcoûts ; cet article n’en invente pas les conditions.',
    'Aucune suppression démontrée d’obligation non essentielle : la décence est conservée et la faculté existante de travaux reste ouverte.',
    'Aucune mise en location dérogatoire de vingt-quatre mois n’est créée à partir d’un renvoi dont les conditions extérieures ne sont pas réécrites ici.',
    'Aucune charge nouvelle identifiée : mêmes exigences de logement et même mandat facultatif, sans diagnostic ou attestation supplémentaire.',
    benefit='Le propriétaire conserve la possibilité de confier les travaux à l’organisme pour les futurs logements concernés ; la protection de décence continue de bénéficier à tous les sous-locataires éligibles.')

put('L444-4',
    'Maintien intégral de l’attribution suivant les règles du logement social. Ces règles organisent l’accès équitable aux logements mobilisés ; l’article n’exige aucun dossier ou autorisation autonome et ne constitue pas un quota communal SRU.',
    'Renvoi à la section 1 du chapitre Ier du titre IV conservé dans son champ d’attribution des logements, avec les évolutions propres de cette section. Ne pas le confondre avec le I de L302-5 relatif aux anciens objectifs communaux : ce texte ne les vise pas et ne les rétablit pas.',
    'Maintien nécessaire de l’accès social et de l’égalité d’attribution ; aucun régime ou reporting supplémentaire n’est supprimé dans cet article.',
    'L’examen des procédures générales de la section visée appartient à leurs articles respectifs ; aucune purge exhaustive de leurs formalités n’est affirmée.',
    'Aucune charge nouvelle identifiée : le simple renvoi existant est maintenu sans créer de dépôt, d’information ou de délai supplémentaire.',
    benefit='Les conditions et priorités légales d’accès au logement social demeurent applicables aux nouveaux sous-locataires éligibles ; la suppression des quotas communaux n’est pas un motif de retrait de ces droits individuels.')

put('L444-5',
    'Maintien intégral des garanties locatives, du transfert sous condition d’éligibilité, du plafond de loyer et du congé motivé pour motif légitime et sérieux. Ce sont des protections substantielles des occupants, non des doublons déclaratifs.',
    'La liste exacte des articles et subdivisions de la loi de 1989 reste inchangée, notamment les deuxième et troisième alinéas du I de 15 et le d de 17. Leur texte extérieur n’est pas joint ; aucune renumérotation supposée n’est inventée. Les règles spéciales de L444-9 et L444-14 restent distinctes et leurs congés ne sont pas des licenciements.',
    'Les garanties contractuelles, plafonds et restrictions au congé sont conservés sans présenter leur maintien comme une baisse fiscale ou une simplification nouvelle.',
    'Le régime locatif extérieur à ce code n’est pas réécrit ; l’allègement spécial de préavis proposé dans deux autres articles ne se généralise pas à cette section.',
    'Aucune charge nouvelle identifiée : même liste de garanties et même motivation du congé, sans certificat ou formalité additionnelle.',
    benefit='Le transfert et la poursuite du contrat restent possibles aux futurs bénéficiaires qui satisfont les conditions HLM ; plafonds de loyers et motifs de congé restent opposables dans les nouvelles sous-locations aussi.')

put('L444-6',
    'Maintien intégral de l’articulation entre restitution au propriétaire et relogement du sous-locataire éligible. Le délai de trois mois est une anticipation protectrice, non un délai d’attente administratif pouvant être retiré sans priver les occupants de solution.',
    'Les deux alinéas demeurent : absence de titre à l’expiration du bail principal, et proposition trois mois avant pour les personnes sans bail direct remplissant les conditions HLM. La fin du titre ne constitue pas une autorisation d’expulsion privée ; les protections et procédures judiciaires autonomes ne sont pas abrogées.',
    'Le maintien conserve la solution de relogement et les droits du propriétaire ; aucune obligation accessoire démontrée n’est supprimée.',
    'Les obligations procédurales civiles d’une restitution forcée et les aides au relogement conservent leurs bases distinctes hors de cet article.',
    'Aucune charge nouvelle identifiée : même calendrier de proposition, mêmes conditions d’éligibilité et aucune attestation nouvelle.',
    benefit='La proposition de location correspondant aux besoins et possibilités du sous-locataire reste due pour les futurs bénéficiaires éligibles, trois mois avant la fin du bail principal, et ne dépend pas d’un ancien contrat de travail.')

proposal = '<p>' + by_number['L444-7']['source_xml'].strip().replace('sous réserve des dispositions des articles L. 444-8 et L. 444-9.', "sous réserve des dispositions de l'article L. 444-9.") + '</p>'
put('L444-7',
    'Coordination nécessaire : retirer du renvoi d’exception L444-8 dont le minimum de six ans est abrogé pour l’avenir. Maintien de L444-5, L444-6 et L444-9, du conventionnement, des logements meublés ou non et des deux populations bénéficiaires.',
    'L321-4, L321-8, L301-1 et L444-9 lus intégralement. Le d de L321-4 conserve son propre minimum de six ans pour la convention d’aide : ce n’est pas la durée du bail principal supprimée dans L444-8. Les baux principaux antérieurs gardent la durée et le régime transitoire prévus dans l’article abrogé. Cette coordination n’efface aucune aide ANAH ni aucune condition de décence ou de relogement.',
    'Simple coordination de la mesure de suppression du minimum du bail principal ; elle n’est pas comptée comme une seconde suppression de durée.',
    'Les durées conventionnelles d’aide et les protections de sous-location restent opposables ; les contrats d’emploi sont hors du champ du renvoi.',
    'Aucune charge nouvelle identifiée : un renvoi rendu inutile est retiré, sans nouveau dossier ou condition d’accès au logement.',
    proposed=proposal, classification='coordination_only',
    effects=[effect('coordination', 'sous-location-conventionnee-fin-minimum-bail',
                    'Retrait de la référence au minimum de durée du bail principal abrogé pour les nouveaux baux.',
                    'Application de L444-5 et L444-6 sous réserve de L444-8 et L444-9.',
                    'Même champ et mêmes garanties, sous réserve de L444-9 ; transition des anciens baux portée par L444-8.',
                    'other', 'Organismes, propriétaires et occupants de logements conventionnés relevant de cette section.',
                    'Coordination avec l’abrogation prospective de L444-8 ; durées des conventions d’aide inchangées.',
                    'sous réserve des dispositions des articles L. 444-8 et L. 444-9.',
                    "sous réserve des dispositions de l'article L. 444-9.")],
    benefit='La sous-location conventionnée demeure ouverte aux personnes en difficulté de L301-1 II et à celles nécessitant une transition locative, pour les nouveaux dossiers également. Conventionnement, loyers protégés et solutions de relogement restent applicables.')

proposal = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme pour les baux conclus à compter de cette date. Aucune durée minimale de six ans n'est imposée par le présent article à ces baux.</p>
<p>Les baux conclus antérieurement conservent leur durée et demeurent régis, pour cette durée, par les dispositions antérieures. Leur renouvellement ou leur reconduction à compter de cette date n'est pas soumis à ce minimum légal.</p>
<p>La suppression de ce minimum ne réduit ni la durée ni les droits résultant des sous-locations en cours. Les obligations de relogement et les protections des occupants demeurent applicables. Elle ne modifie pas la durée des conventions d'aide ni les engagements qui en résultent.</p>"""
put('L444-8',
    'Abrogation prospective du minimum légal de six ans entre propriétaire et organisme. Ce verrou s’ajoute à la durée de la convention d’aide et aux protections distinctes des occupants ; sa suppression laisse les parties choisir la durée sans les dispenser du relogement ni autoriser la rupture des sous-locations en cours.',
    'Coordination opérée dans L444-7. L321-4 et L321-8 lus : le minimum conventionnel de six ans de l’aide ANAH n’est pas abrogé. L444-6 et L444-9 conservent leurs propositions de logement et délais de trois mois. Une durée plus courte n’autorise pas l’organisme à concéder des droits d’occupation qu’il ne peut assurer. Les anciens baux ne sont pas raccourcis ; les renouvellements futurs ne sont pas soumis à ce seul plancher. Aucun effet prétendu sur un contrat de travail.',
    'Le minimum de six ans du bail principal est effectivement retiré pour les nouveaux contrats, renouvellements et reconductions ; les garanties locatives et conventions d’aide sont réservées.',
    'Le minimum de durée d’une convention d’aide, les durées contractuelles déjà acquises et les droits des sous-locataires restent hors de l’abrogation ; aucun gain monétaire national n’est établi.',
    'Aucune charge nouvelle identifiée : pas d’autorisation, déclaration, durée de remplacement ni nouvel engagement ; les protections locatives réservées existaient déjà.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('obligation_removed', 'sous-location-conventionnee-fin-minimum-bail',
                    'Suppression de l’obligation de durée minimale du seul bail principal entre propriétaire et organisme.',
                    'Bail principal obligatoirement conclu pour au moins six ans dans la section des logements conventionnés.',
                    'Pas de minimum sur ce fondement pour baux nouveaux ou renouvelés ; durée des conventions d’aide et droits des occupants inchangés.',
                    'legal_duty', 'Propriétaires et organismes HLM prenant à bail un logement conventionné pour sous-location de transition.',
                    'À compter de l’entrée en vigueur pour nouveaux baux, renouvellements et reconductions ; durée des anciens contrats conservée.',
                    "Le bail établi entre l'organisme d'habitations à loyer modéré et le propriétaire est conclu pour une durée d'au moins six ans.",
                    "Aucune durée minimale de six ans n'est imposée par le présent article à ces baux.")],
    benefit='Le minimum du bail principal ne constitue pas une exonération ou une dérogation favorable d’accès à l’aide ; les durées acquises sont conservées. Les occupants futurs gardent les protections et relogements légaux, et les conventions ANAH gardent leurs avantages et leur durée propre.',
    repeal='Suppression, pour les baux nouveaux, renouvelés ou reconduits, de l’obligation de conclure le bail principal pour au moins six ans ; durées contractuelles antérieures, conventions d’aide et droits des occupants préservés.')

proposal = """<p>Les rapports entre l'organisme d'habitations à loyer modéré et les occupants sont régis par un contrat de sous-location conclu pour une durée d'un an. Le bailleur peut renouveler deux fois le contrat pour la même durée. Le bailleur doit proposer, trois mois avant le terme définitif du contrat, une solution de logement correspondant aux besoins et aux possibilités des occupants.</p>
<p>Les occupants peuvent mettre fin au contrat à tout moment, sans préavis. Leur congé prend effet dès sa réception par le bailleur ou à une date ultérieure qu'ils indiquent. Par dérogation à l'article L. 444-5, le délai de préavis est de trois mois si le congé émane du bailleur et, dans ce cas, le congé ne peut être donné que pour un motif légitime et sérieux, notamment l'inexécution par les occupants de l'une des obligations leur incombant ou le refus d'une offre de relogement définitif correspondant à leurs besoins et à leurs possibilités.</p>
<p>La dispense de préavis des occupants s'applique aux congés qu'ils donnent à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les sous-locations en cours. Les congés antérieurs restent régis par les dispositions qui leur étaient applicables. Cette dispense ne supprime ni les dettes antérieures ni les obligations de restitution du logement.</p>"""
put('L444-9',
    'Réduction de fond favorable aux occupants : retirer leur mois de préavis pour permettre un départ sans attente, y compris dans les sous-locations en cours après notification nouvelle. Maintien intégral de l’année contractuelle, des deux renouvellements, de la proposition de logement trois mois avant le terme et du préavis de trois mois du bailleur avec motif légitime et sérieux.',
    'L444-5 et L444-6 lus : les garanties locatives et le relogement restent applicables via L444-7. La prise d’effet à réception du congé assure une date opposable et laisse le choix d’une date ultérieure sans imposer un nouveau support ou justificatif. Le mois supprimé est civil et ne vaut pas automatiquement trente jours ; ce n’est pas le préavis professionnel de quinze jours. Aucun nouveau délai maximal d’occupation ni terme d’emploi. La proposition autonome de L444-8 préserve durées des anciens baux et conventions d’aide.',
    'Suppression effective du préavis d’un mois dû par les seuls occupants ; les délais et motifs qui protègent ceux-ci contre le bailleur demeurent.',
    'La dispense ne s’étend pas à tous les baux HLM ou aux préavis d’emploi ; dettes déjà nées, restitution et congés antérieurs restent hors de la réforme.',
    'Aucune charge nouvelle identifiée : le congé existe déjà ; sa réception fixe l’effet de la dispense sans attestation, nouveau canal ou condition d’ancienneté.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('deadline_reduced', 'sous-location-sociale-fin-preavis-occupant',
                    'Suppression du mois de préavis de départ des occupants du logement conventionné de transition.',
                    'Occupants libres de partir à tout moment mais avec un mois de préavis ; bailleur soumis à trois mois et à un motif légitime et sérieux.',
                    'Occupants dispensés de préavis dès réception du congé, sauf date ultérieure choisie ; bailleur toujours soumis à trois mois et au même motif.',
                    'other', 'Occupants des sous-locations conventionnées visées par L444-7.',
                    'Congés des occupants donnés à compter de l’entrée en vigueur, y compris contrats en cours ; congés antérieurs inchangés.',
                    "le délai de préavis est d'un mois si le congé émane des occupants.",
                    'Les occupants peuvent mettre fin au contrat à tout moment, sans préavis.')],
    benefit='Tous les avantages restent ouverts aux occupants futurs éligibles : durée d’un an renouvelable deux fois, solution adaptée proposée trois mois avant le terme, départ à tout moment désormais sans préavis, et protection par un motif légitime et sérieux et trois mois de préavis lorsque le bailleur donne congé. Aucun de ces droits n’est conditionné à un ancien CDD ou à l’ancienneté professionnelle.',
    removed=['Obligation des occupants de respecter un mois de préavis avant de mettre fin à la sous-location conventionnée de transition.'])

proposal = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. Pour les prises à bail conclues, renouvelées ou reconduites à compter de cette date dans les conditions de l'article L. 444-10, la qualité du propriétaire et les liens de parenté ou d'alliance entre ses associés ne sont pas limités par le présent article.</p>
<p>Les baux et sous-locations valablement conclus antérieurement conservent leurs effets et les droits qui en sont issus. La présente abrogation ne les résilie pas, ne modifie pas leurs clauses et n'impose aucune nouvelle formalité à leurs parties.</p>
<p>Les conditions tenant aux organismes habilités, à la vacance et au caractère meublé des logements, aux travailleurs bénéficiaires, aux ressources, aux loyers et aux protections des occupants demeurent applicables dans leur champ propre.</p>"""
put('L444-11',
    'Abrogation de fond de la restriction aux propriétaires personnes physiques et SCI exclusivement familiales jusqu’au quatrième degré. La parenté des propriétaires ne démontre pas une protection nécessaire du sous-locataire ; la supprimer élargit les logements mobilisables tout en conservant les organismes habilités, l’objet saisonnier, les ressources, les plafonds et les garanties locatives.',
    'L444-10 officiel et proposition lus : le caractère saisonnier qualifie les tâches et non la durée de l’emploi, les futurs salariés en contrat unique gardant l’accès au logement. L444-12 à L444-14 maintiennent leurs garanties propres. La disparition de la condition familiale n’étend pas automatiquement les aides fiscales ou agréments relevant d’autres textes et n’exonère pas de la décence. Aucun nouveau CDD ou terme d’emploi n’est autorisé.',
    'Restriction de catégorie du propriétaire effectivement supprimée ; ouverture aux propriétaires institutionnels ou sociétés non familiales sans nouvelle procédure de substitution.',
    'Aucune augmentation automatique d’aides, d’exonérations ou de stock disponible n’est démontrée ; les conditions autonomes des régimes d’aide demeurent.',
    'Aucune charge nouvelle identifiée : suppression d’un critère d’éligibilité et de son examen, sans nouvelle déclaration, contrôle préalable ou justificatif.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('obligation_removed', 'logement-saisonnier-fin-restriction-proprietaire',
                    'Retrait de l’exclusion des propriétaires personnes morales non familiales du dispositif de prise à bail pour sous-location saisonnière.',
                    'Logement nécessairement détenu par personnes physiques ou SCI exclusivement entre parents et alliés jusqu’au quatrième degré inclus.',
                    'Aucune restriction de propriétaire ou de parenté sur ce fondement ; autres conditions du dispositif inchangées.',
                    'legal_duty', 'Propriétaires de logements vacants meublés, organismes habilités et travailleurs saisonniers éligibles.',
                    'Nouvelles prises à bail, renouvellements et reconductions dès l’entrée en vigueur ; contrats antérieurs conservés.',
                    "doit appartenir à une ou plusieurs personnes physiques ou à une société civile immobilière constituée exclusivement entre parents et alliés jusqu'au quatrième degré inclus.",
                    "la qualité du propriétaire et les liens de parenté ou d'alliance entre ses associés ne sont pas limités par le présent article.")],
    benefit='Les travailleurs futurs en emploi saisonnier, y compris sous contrat unique, gardent l’accès au dispositif de L444-10 ; les conditions de ressources, plafonds de loyers et protections de L444-12 à L444-14 demeurent. Le critère familial n’était pas une exonération fiscale ou une dispense favorable au locataire.',
    repeal='Suppression de l’obligation de détenir le logement en propriété de personnes physiques ou de SCI exclusivement familiales jusqu’au quatrième degré pour les prises à bail, renouvellements et reconductions futurs, sans retrait des droits locatifs acquis.')

put('L444-12',
    'Maintien intégral de la liste des garanties de la loi de 1989 applicables aux sous-locations de travailleurs saisonniers. Ces protections de décence, d’état des lieux, de dépôt et de rapports locatifs restent utiles ; aucune contrainte déclarative autonome n’est créée par cet article.',
    'Liste conservée sans perte du l exclu à l’article 4 ni des articles 7-1, 8-1, 20-1 et 25-4 à 25-11 expressément énumérés. L444-10 proposé permet l’accès futur des salariés en contrat unique sur les tâches saisonnières ; le renvoi d’objet demeure cohérent sans recopier une condition d’ancien CDD. L444-14 constitue la règle spéciale de congé, coordonnée dans ce lot. Texte intégral de la loi extérieure non fourni : aucune modification implicite de ses subdivisions.',
    'Maintien nécessaire des protections du sous-locataire, sans nouvelle réduction revendiquée et sans restriction aux travailleurs titulaires d’anciens contrats.',
    'Le texte extérieur de la loi de 1989 n’est pas réécrit ici ; les différences entre bail meublé, sous-location et contrat de travail restent réservées.',
    'Aucune charge nouvelle identifiée : même liste et même exception à l’article 4 ; aucun dépôt ou justificatif d’emploi supplémentaire.',
    benefit='L’ensemble des garanties locatives énumérées conserve son application aux futurs travailleurs saisonniers éligibles sous contrat unique comme aux bénéficiaires antérieurs ; l’allègement du préavis de L444-14 n’efface pas ces garanties.')

put('L444-13',
    'Maintien intégral des ressources et du plafond de loyer applicables à la sous-location saisonnière. La finalité est l’accès social au logement à loyer plafonné ; supprimer ces critères ne serait pas une simple dispense de justificatifs mais une modification du bénéfice protégé.',
    'L441-1 est visé pour ses seules conditions de ressources et non pour un quota communal ou l’ensemble des formalités d’attribution. Le plafond de loyer reste fixé par zones, sans nouveau montant. Les régimes futurs d’emploi ne modifient pas ces conditions locatives.',
    'Les deux conditions substantielles d’accès social et de loyer restent nécessaires et ne sont pas comptées comme des prélèvements ou obligations nouvellement supprimés.',
    'Aucune baisse de loyer ou suppression des pièces réglementaires n’est démontrée dans cet article ; les conditions d’aides autonomes restent distinctes.',
    'Aucune charge nouvelle identifiée : mêmes conditions de ressources et même plafond, sans nouvelle déclaration ni critère d’ancienneté.',
    benefit='Le plafonnement du loyer protège les nouveaux sous-locataires saisonniers éligibles ; leurs droits ne dépendent ni d’un CDD ancien ni d’un quota communal. Le maintien du plafond préserve cet avantage pour l’avenir.')

proposal = """<p>Les occupants peuvent mettre fin au contrat à tout moment, sans préavis. Leur congé prend effet dès sa réception par le bailleur ou à une date ultérieure qu'ils indiquent. Le contrat de sous-location est conclu pour une durée n'excédant pas six mois.</p>
<p>Les occupants ne bénéficient pas du droit au maintien dans les lieux.</p>
<p>Le congé ne peut être donné par l'organisme mentionné à l'article L. 444-10 avant le terme du contrat de sous-location, sauf pour un motif légitime et sérieux, notamment l'inexécution par les occupants de l'une des obligations leur incombant. Le congé doit mentionner le motif allégué. Le délai de préavis applicable au congé donné par cet organisme est d'un mois.</p>
<p>Le congé doit être notifié par lettre recommandée avec demande d'avis de réception, signifié par acte d'huissier ou remis en main propre contre récépissé ou émargement. Le délai de préavis du congé donné par le bailleur court à compter du jour de la réception de la lettre recommandée, de la signification de l'acte d'huissier ou de la remise en main propre.</p>
<p>Pendant le délai de préavis, le sous-locataire n'est redevable du loyer et des charges que pour le temps où il a occupé réellement les lieux si le congé a été notifié par le bailleur. Si le congé a été notifié par les occupants, le loyer et les charges ne sont dus que jusqu'à sa prise d'effet. Si les occupants ont choisi une prise d'effet ultérieure à la réception du congé, ils sont déchargés des loyers et charges pour la période pendant laquelle le logement se trouve, avant cette date, occupé par un autre locataire en accord avec le bailleur.</p>
<p>A la prise d'effet du congé des occupants ou à l'expiration du délai de préavis du congé du bailleur, le sous-locataire est déchu de tout titre d'occupation des locaux loués.</p>
<p>La dispense de préavis des occupants et les règles de loyer et de charges qui en résultent s'appliquent aux congés qu'ils donnent à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les sous-locations en cours. Les congés antérieurs restent régis par les dispositions qui leur étaient applicables. Les dettes antérieures et les obligations de restitution du logement demeurent.</p>"""
put('L444-14',
    'Réduction de fond coordonnée avec L444-9 : suppression du mois de préavis des occupants et du loyer afférent à un mois désormais inexigible après prise d’effet du congé. Les six alinéas de fond restent à leur place : durée locative maximale de six mois, absence de maintien, motif du congé du bailleur, notification, loyers et fin du titre. Le préavis d’un mois du bailleur demeure.',
    'L444-10 officiel et proposé lus ; son accès au logement des travailleurs en contrat unique n’est pas conditionné au terme de l’emploi. Les six mois sont la durée maximale du logement, non d’une mission ou d’un CDD. Les trois modes de notification sont conservés sans substitution implicite d’un courriel. Le bénéfice d’absence de loyer pour non-occupation sur congé du bailleur et la décharge en cas de relocation anticipée agréée par le bailleur sont maintenus. L’expiration du titre ne permet pas une expulsion privée. Le mois civil n’est pas converti artificiellement en trente jours.',
    'Suppression réelle d’un mois de préavis de départ pour l’occupant saisonnier ; coordination des loyers correspondants, sans deuxième mesure comptée pour le même délai.',
    'Le préavis du bailleur et la durée de six mois du logement demeurent. La réforme ne s’étend pas aux autres baux ni aux règles professionnelles de rupture.',
    'Aucune charge nouvelle identifiée : les modes de congé restent ceux de la source, la date ultérieure est facultative et aucun registre, preuve de CDD ou donnée supplémentaire n’est demandé.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('deadline_reduced', 'sous-location-sociale-fin-preavis-occupant',
                    'Fin du préavis d’un mois dû par le sous-locataire saisonnier et de la dette de loyer attachée au seul délai supprimé.',
                    'Un mois de préavis des occupants, avec loyers et charges du délai entier sauf relocation consentie ; bailleur également tenu à un mois.',
                    'Congé des occupants effectif à réception ou date ultérieure choisie, sans mois supplémentaire dû ; préavis et garanties du congé du bailleur maintenus.',
                    'other', 'Occupants saisonniers des sous-locations de logements vacants meublés de L444-10.',
                    'Congés des occupants donnés dès entrée en vigueur, même sous-location en cours ; anciens congés et dettes antérieures préservés.',
                    "Les occupants peuvent mettre fin au contrat à tout moment, sous réserve de respecter un délai de préavis d'un mois.",
                    'Les occupants peuvent mettre fin au contrat à tout moment, sans préavis.')],
    benefit='Le départ à tout moment devient sans préavis pour les futurs congés. Sont conservés le congé motivé du bailleur, son préavis d’un mois, la limitation de loyer au temps réellement occupé sur son congé, et la décharge pour relocation anticipée consentie quand l’occupant choisit une date ultérieure. Ces droits restent ouverts aux futurs salariés saisonniers en contrat unique.',
    removed=['Obligation des occupants saisonniers de respecter un mois de préavis avant le départ de la sous-location.',
             'Obligation de payer le loyer et les charges du mois de préavis des occupants après la prise d’effet immédiate de leur congé, sauf relocation déjà prévue dans la source.'])

proposal = by_number['L445-1-1']['source_xml'].replace(
    "La convention d'utilité sociale comporte des indicateurs permettant de mesurer le niveau de réalisation des objectifs fixés pour chaque aspect de la politique des organismes mentionnés au présent article. Ces indicateurs sont définis par décret.",
    "Aucun indicateur normalisé, tableau de suivi ou développement qualitatif distinct n'est exigé pour rendre compte de la convention. Cette dispense ne modifie pas les engagements mentionnés aux 1° à 5°.")
proposal += """<p>Cette dispense s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les conventions en cours et les périodes antérieures dont les indicateurs n'ont pas encore été produits ou transmis. Aucun dépôt de rattrapage n'est exigé sur ce seul fondement. Les informations déjà légalement recueillies restent utilisables dans les conditions qui leur sont applicables.</p>
<p>Les engagements patrimoniaux, financiers, d'entretien et de service de la convention demeurent opposables. Les contrôles et les obligations comptables prévus par d'autres dispositions législatives restent applicables ; aucun état distinct de remplacement n'est exigé au titre des indicateurs supprimés.</p>"""
put('L445-1-1',
    'Réduction de fond ciblée : supprimer les indicateurs réglementaires obligatoires et les tableaux et développements de suivi qui les exécutent, sans rapport de substitution. Les cinq engagements de la convention de six ans, l’entretien, le service aux locataires et la sanction des manquements graves restent intégraux. Le contrôle du respect d’engagements concrets n’exige pas un second dispositif normalisé de mesure pour chaque aspect de la politique.',
    'L422-4, L411-2 et D445-5-6 lus en entier, tableau compris : les six indicateurs PP-SV-1 à 3, ACC-SV-1, SR-SV-1 et 2 et les trois développements qualitatifs doivent être retirés dans la coordination réglementaire de D445-5-6, hors lot, sans supprimer décotes, garanties des acquéreurs, plafonds ou contrôles indépendants. La présente règle législative écarte leur exigibilité, y compris pour les conventions en cours ; ce règlement n’est pas déclaré réécrit ici. Le contradictoire d’un mois, le plafond de 200 € par logement et l’affectation au FNAP restent inchangés pour les manquements aux engagements maintenus. Les contrôles SIEG, la comptabilité séparée et la prévention de surcompensation requise par le cadre européen ne sont pas supprimés. Aucun quota SRU ni sanction de carence ne sont recréés.',
    'L’obligation législative de produire des indicateurs normalisés est retirée ; les engagements sociaux et leur contrôle subsistent sans nouvel état de remplacement.',
    'La coordination réglementaire de D445-5-6 est précisément identifiée mais n’est pas une réécriture de ce règlement dans ce lot. Aucun coût net de contrôle ou rendement de sanction n’est chiffré.',
    'Aucune charge nouvelle identifiée : les cinq engagements et les contrôles autonomes sont préexistants ; aucun rapport, collecte, registre ou délai de remplacement n’est institué.',
    proposed=proposal, classification='material_reduction',
    effects=[effect('obligation_removed', 'societes-vente-hlm-fin-indicateurs-cus',
                    'Suppression des indicateurs normalisés de la convention et de leurs tableaux et développements distincts de suivi.',
                    'Indicateurs définis par décret obligatoires pour chaque aspect de la politique des sociétés de vente HLM.',
                    'Aucun indicateur normalisé ni tableau ou développement distinct exigible ; cinq engagements substantiels et sanction de leurs manquements maintenus.',
                    'legal_duty', 'Sociétés de vente HLM de L422-4 liées à l’État par convention d’utilité sociale.',
                    'À l’entrée en vigueur, conventions nouvelles et en cours ; aucune production de rattrapage sur le seul fondement supprimé.',
                    "La convention d'utilité sociale comporte des indicateurs permettant de mesurer le niveau de réalisation des objectifs fixés pour chaque aspect de la politique des organismes mentionnés au présent article. Ces indicateurs sont définis par décret.",
                    "Aucun indicateur normalisé, tableau de suivi ou développement qualitatif distinct n'est exigé pour rendre compte de la convention.")],
    benefit='Le soutien à l’accession des personnes remplissant L443-1, les conditions des ventes et acquisitions, l’entretien et la qualité du service demeurent opposables dans les futures conventions. La suppression des indicateurs ne supprime ni décote, ni garantie, ni exonération ou aide SIEG ; leurs conditions autonomes sont réservées.',
    removed=['Obligation d’établir des indicateurs réglementaires pour chacun des aspects de la politique couverts par la convention d’utilité sociale des sociétés de vente HLM.',
             'Production des tableaux de suivi et développements qualitatifs distincts exigés au seul titre des indicateurs réglementaires, y compris pour les conventions et périodes en cours.'])


# Les vues sont des propositions pour le travail et L444-10, mais seulement une
# source officielle pour L444-9 : aucune de ces empreintes n'est remplacée par
# celle de la rédaction ci-dessus.
assessments = {
 'L443-15-5-4': {
  'L1234-1': 'L1234-1 officiel règle le préavis de licenciement selon l’ancienneté ; sa proposition vise quinze jours pour les nouveaux emplois et conserve les anciens contrats. L443-15-5-4 règle l’accès au domicile pour travaux : les huit jours de notification et l’urgence sont indépendants, sans renvoi à rectifier vers le droit du travail.',
  'L1221-2': 'L1221-2 proposé impose l’emploi nouveau à durée indéterminée et préserve les contrats antérieurs. Les travaux et l’accès au logement de l’acquéreur ne sont ni un emploi ni une mission ; leur durée ne forme aucun CDD et ne conditionne aucun avantage à un ancien contrat.',
  'L1234-9': 'L1234-9 officiel concerne l’indemnité de licenciement à huit mois ; sa proposition vise un an au terme effectif, préavis inclus, puis 0,20 mois par année totale et six mois de plafond ordinaire. L’indemnité de L443-15-5-4 répare des travaux dommageables : elle reste intégrale, sans ancienneté, seuil ou plafond professionnel.'
 },
 'L444-7': {
  'L1234-1': 'Le renvoi de L444-7 porte sur des sous-locations conventionnées, non sur un licenciement. Le préavis patronal professionnel de quinze jours de la proposition L1234-1, avec transition des anciens emplois, ne remplace ni le congé du bailleur de trois mois dans L444-9 ni le relogement ; aucune ancienneté d’emploi ne s’y ajoute.',
  'L1221-2': 'L1221-2 proposé interdit les nouveaux CDD tout en conservant les situations anciennes ; L444-7 vise les besoins de logement de transition et le II de L301-1, pas une catégorie de contrat professionnel. Les futurs salariés en contrat unique restent éligibles selon leur situation locative, sans durée d’emploi nouvelle.',
  'L1234-9': 'Le seuil professionnel proposé d’un an, préavis inclus, et le calcul ordinaire 0,20 mois sur toute l’ancienneté plafonné à six mois concernent une rupture par l’employeur. L444-7 n’attribue aucune indemnité de rupture : ressources, vulnérabilité et transition de logement demeurent sans ce seuil ni exclusion des anciens contrats.',
  'L444-9': 'La vue fournie de L444-9 est uniquement officielle : sous-location d’un an renouvelable deux fois, relogement trois mois avant le terme, congé occupant d’un mois et bailleur de trois mois. Le présent lot supprime seulement le préavis des occupants ; L444-7 conserve la réserve à L444-9 et retire L444-8 pour ne pas rétablir son minimum de bail principal.'
 },
 'L444-8': {
  'L1234-1': 'Le minimum de six ans de L444-8 concerne le bail propriétaire-organisme. Son abrogation ne touche pas L1234-1, dont la proposition établit un préavis professionnel de quinze jours pour nouveaux contrats et protège les anciens. Les congés locatifs et autorisations professionnelles restent distincts ; aucune ancienneté d’emploi ne mesure ce bail.',
  'L1221-2': 'La durée du bail principal de L444-8 est indépendante de la durée d’emploi. L1221-2 proposé supprime les nouveaux CDD mais permet une mission limitée sans terme de l’emploi ; retirer un plancher locatif ne recrée ni CDD, ni fin automatique de contrat unique et ne change pas les anciens contrats de travail.',
  'L1234-9': 'L1234-9 proposé conserve les droits des anciens emplois et règle l’indemnité ordinaire après un an au terme effectif, préavis inclus, à 0,20 mois par année totale avec plafond de six mois. Aucun de ces seuils n’est applicable au bail principal de L444-8 ; son abrogation ne supprime pas des créances salariales ou indemnités spéciales.',
  'L444-9': 'La source officielle fournie de L444-9 organise un an de sous-location, deux renouvellements et une offre adaptée trois mois avant le terme ; ces garanties ne découlent pas du minimum de six ans du bail principal. Elles demeurent, avec le congé bailleur de trois mois, et la présente abrogation réserve expressément les sous-locations en cours et les conventions d’aide.'
 },
 'L444-9': {
  'L1234-1': 'L1234-1 proposé règle le licenciement des nouveaux salariés avec quinze jours de préavis et transition des anciens emplois. Les trois mois du congé bailleur de L444-9 sont une protection locative ; ils sont conservés. La dispense nouvelle de l’occupant est décidée pour le logement, sans appliquer artificiellement quinze jours ou une ancienneté professionnelle.',
  'L1221-2': 'Le contrat d’un an renouvelable deux fois de L444-9 est une sous-location conventionnée, pas un contrat de travail à terme. L1221-2 proposé n’en commande pas la conversion en durée indéterminée ; il n’exclut pas les futurs salariés en contrat unique de l’accès au logement transitoire ni ne résilie les contrats de logement antérieurs.',
  'L1234-9': 'Le préavis inclus dans le seuil professionnel d’un an et le calcul de 0,20 mois sur ancienneté totale plafonné à six mois de L1234-9 proposé ne concernent aucune somme de L444-9. L’offre de relogement et le congé sans préavis des occupants sont sans ancienneté d’emploi ; anciens droits salariaux et indemnités spéciales restent hors de ce régime locatif.'
 },
 'L444-11': {
  'L1234-1': 'La source L444-11 limite la qualité du propriétaire du logement, sans règle de rupture d’emploi. L1234-1 proposé fixe quinze jours pour nouveaux salariés avec maintien des anciens régimes ; il ne s’applique pas à cette qualité ni aux congés locatifs de L444-14. Aucun seuil d’ancienneté ou délai professionnel n’est substitué au critère familial supprimé.',
  'L1221-2': 'L1221-2 proposé impose la durée indéterminée des emplois nouveaux et réserve les anciens contrats. La suppression de la parenté des propriétaires dans L444-11 ne recrée aucun CDD : elle élargit la mobilisation locative au profit des travailleurs saisonniers dont l’emploi peut être un contrat unique, sans terme d’emploi tiré du bail.',
  'L1234-9': 'L1234-9 proposé règle l’indemnité ordinaire de l’employeur après un an au terme effectif avec préavis, sur ancienneté totale à 0,20 mois par an, plafond six mois, et réserve anciens droits et indemnités spéciales. L444-11 ne concerne aucune indemnité professionnelle ; la restriction patrimoniale supprimée ne devient pas une condition d’ancienneté du travailleur.',
  'L444-10': 'La proposition fournie de L444-10 conserve la vacance et le meublé, définit les tâches saisonnières et admet les futurs contrats uniques, avec anciens baux et emplois protégés. L’abrogation de L444-11 retire uniquement la restriction de propriétaire ; elle n’étend pas le dispositif à des tâches non saisonnières ni ne supprime les ressources, loyers et protections des autres articles.'
 },
 'L444-12': {
  'L1234-1': 'La liste de L444-12 vise exclusivement les garanties de la loi locative de 1989. L1234-1 proposé concerne le préavis de licenciement des nouveaux salariés et les anciens régimes selon ancienneté ; ni les quinze jours ni les anciennes durées d’emploi ne remplacent les congés spéciaux du logement de L444-14.',
  'L1221-2': 'Le renvoi à L444-10 demeure cohérent avec L1221-2 proposé : les tâches peuvent rester saisonnières dans un emploi indéterminé. Les protections locatives de L444-12 s’appliquent aux futures personnes éligibles, pas seulement aux anciens CDD ; aucune nouvelle durée de travail ni condition professionnelle n’est introduite par la liste maintenue.',
  'L1234-9': 'L1234-9 officiel et proposé portent sur l’indemnité de licenciement, avec transition des anciens contrats et, pour nouveaux emplois, seuil d’un an préavis inclus, 0,20 mois par année totale et plafond six mois. Les dépôts, garanties et réparations locatives de L444-12 n’en relèvent pas ; aucun de ces seuils ou plafonds ne leur est appliqué.',
  'L444-10': 'L444-10 officiel renvoie au caractère saisonnier du 3° de L1242-2 ; sa proposition fournie autonomise les tâches saisonnières et protège les baux antérieurs tout en ouvrant les futurs contrats uniques. La liste des garanties de L444-12 conserve exactement ce champ par renvoi, sans renvoi direct au CDD, sans perte du l exclu de l’article 4 et sans terme nouveau de l’emploi.'
 },
 'L444-14': {
  'L1234-1': 'Le mois de préavis de L444-14 est locatif ; L1234-1 proposé ne l’abroge pas et ses quinze jours pour nouveaux emplois ne doivent pas le remplacer par analogie. La présente réforme décide séparément la dispense de l’occupant, conserve le mois du bailleur et réserve les congés antérieurs ; les procédures et protections d’emploi restent extérieures.',
  'L1221-2': 'Les six mois de L444-14 limitent la sous-location du logement ; ils ne terminent pas le contrat unique prévu par L1221-2 proposé. La fin des tâches saisonnières ou du logement ne devient pas un CDD spécial. Les futurs travailleurs en emploi indéterminé gardent les garanties locatives et les anciens emplois conservent leur transition propre.',
  'L1234-9': 'Le seuil d’un an au terme effectif avec préavis et l’indemnité patronale 0,20 mois par année totale, plafond six mois, de L1234-9 proposé n’ont aucun rapport avec les six mois de sous-location. Loyers, charges et réparations locatives restent autonomes ; aucune indemnité spéciale ou créance salariale ancienne n’est supprimée par la dispense locative.',
  'L444-10': 'L444-10 proposé conserve les bénéficiaires saisonniers sur les tâches réelles, admet les contrats uniques et protège les anciens baux. Le renvoi du troisième alinéa de L444-14 désigne l’organisme habilité, pas une durée de travail : il demeure exact. La réforme conserve le maximum locatif de six mois et la motivation du bailleur, avec accès futur sans condition d’ancien CDD.'
 }
}

for number, out in answers.items():
    key = out['code_id'] + '|' + out['source_id']
    checks = []
    for target in refs['requirements'][key]:
        t = refs['targets'][target]
        checks.append(dict(target_key=target, view_sha256=t['view_sha256'],
                           assessment=assessments[number][t['number']]))
    out['reference_checks'] = checks

result = [answers[a['number']] for a in sources]
assert len(result) == 24
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
