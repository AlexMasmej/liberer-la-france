import json
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_num = {a['number']: a for a in sources}
answers = {}


def text(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))


def ps(*items):
    return ''.join('<p>' + html.escape(s, quote=False) + '</p>' for s in items)


def effect(kind, mid, description, before, after, unit, population, transition, burdens, sq, pq):
    return dict(kind=kind, measure_id=mid, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=sq, proposed_quote=pq)


def impact(cls, assessment, limits, burdens, effects=None):
    return dict(version=1, classification=cls, assessment=assessment,
                scope_limitations=limits, new_burdens_review=burdens, effects=effects or [])


def make(number, xml, reason, notes, benefits, si, removed=None):
    source = by_num[number]
    a = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='retained_unchanged' if xml is None else 'rewrite_draft',
             classification=si['classification'], benefit_review=benefits,
             substantive_impact=si)
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    answers[number] = a


def retain(number, reason, notes, benefits, assessment, limits, burdens):
    make(number, None, reason, notes, benefits,
         impact('retained_necessary', assessment, limits, burdens))


retain('L434-9',
       "Maintien intégral du régime de rente du survivant lors d'une nouvelle union : le capital de remplacement, le maintien prioritaire de la rente en présence d'enfants rentiers et la récupération du droit après rupture protègent le revenu familial. Les imputations évitent de payer deux fois les mêmes périodes ou revenus de remplacement. L'article n'institue ni impôt de succession, ni cotisation accessoire, ni agrément ; ses règles de liquidation forment un ensemble utile de remplacement du soutien familial.",
       "Les cinq alinéas, le report du rachat tant qu'un enfant perçoit une rente de L434-10 et tous les régimes du 2° sont conservés. R434-14, lu dans le corpus, fixe la période à trois ans et règle la demande de rétablissement ; ses formalités ne sont pas réputées réécrites ici. L711-1 et L413-12 ont été lus. La note du 1er janvier 2020 est historique. La correction institutionnelle proposée à L434-10 n'en modifie pas les bénéficiaires.",
       "Le capital lors de la nouvelle union, la rente maintenue en présence d'enfants bénéficiaires et son rétablissement après séparation, divorce, veuvage ou rupture sont préservés, y compris pour les situations futures éligibles. Les imputations existantes ne sont ni étendues ni aggravées.",
       "Aucune réduction revendiquée : l'article règle une prestation sociale et ses cumuls, sans prélèvement sur le décès. Capital, protection des enfants et rétablissement de rente restent nécessaires.",
       "La cessation lors d'une nouvelle union et les imputations demeurent dans ce régime de remplacement du soutien familial. Leur maintien ne vaut pas simplification ; R434-14 n'est pas modifié ici.",
       "Aucune charge nouvelle n'est identifiée : la source entière reste applicable, sans déclaration périodique, condition d'ancienneté, pièce ou registre supplémentaire.")

retain('L434-11',
       "Maintien intégral de la désignation du destinataire du paiement de la rente de l'enfant. Elle protège l'emploi de la prestation au profit du mineur et évite les paiements concurrents ; aucune autorisation, déclaration répétée ou taxe n'est instituée. Aucune reformulation stylistique n'est produite.",
       "Le renvoi à L434-10 vise la rente des enfants, non une indemnité de rupture. Père, mère, tuteur et personne ayant la garde restent tous visés. La correction institutionnelle proposée à L434-10 ne change ni le titulaire de la rente ni le destinataire de son paiement.",
       "Le versement à chacune des personnes légalement habilitées est conservé pour les rentes existantes et futures. Aucune restriction à la tutelle ou condition de situation professionnelle de l'enfant n'est ajoutée.",
       "Aucun allègement matériel revendiqué : le texte détermine le destinataire protecteur du paiement, sans formalité autonome à supprimer.",
       "Les règles civiles de garde et de tutelle ne sont pas réécrites ; ce maintien ne vérifie pas à lui seul leur application dans chaque dossier.",
       "Aucune charge nouvelle n'est identifiée : les destinataires existants restent désignés sans attestation ni dépôt nouveau.")

retain('L434-12',
       "Maintien intégral de la faculté judiciaire de confier la perception de la rente au délégué aux prestations familiales. Le contrôle du juge et la prise en charge des frais protègent les besoins essentiels de l'enfant ; leur suppression retirerait une protection utile sans supprimer une taxe ou un doublon.",
       "Le renvoi à L434-10 demeure cohérent. L552-6, lu en entier, met les frais à la charge de l'organisme prestataire, ou du plus important en cas de pluralité. Code civil 375-9-1 : référence source conservée ; son texte intégral n'est pas fourni dans le corpus autorisé et aucune modification de procédure civile n'est affirmée.",
       "La faculté d'intervention judiciaire et son financement par l'organisme compétent restent disponibles pour les familles futures éligibles. Aucun coût de la mesure n'est transféré à l'enfant ou à sa famille.",
       "Aucune réduction revendiquée : protection judiciaire des prestations de l'enfant et financement de cette protection maintenus sans nouveau corps.",
       "La procédure civile extérieure aux cinq codes n'est pas réécrite ; le renvoi à 375-9-1 garde son champ propre, sans attribution au contrat privé.",
       "Aucune charge nouvelle n'est identifiée : aucun dossier, délai, registre ou coût familial supplémentaire n'est créé par le maintien.")

retain('L434-13',
       "Maintien intégral du droit à rente viagère des ascendants. La preuve de l'obligation alimentaire possible ou de la charge effective identifie le soutien familial remplacé ; elle n'est pas une attestation périodique redondante. Le choix de la date la plus favorable et les exclusions liées à l'abandon de famille ou au retrait total de l'autorité parentale protègent le bénéficiaire et les victimes.",
       "Les 1° et 2°, les deux dates alternatives et les deux exclusions sont conservés. R434-16, lu, fixe à 10 % la fraction individuelle ; aucun taux n'est ajouté à la loi. Le réemploi des informations légalement disponibles demeure soumis au droit existant, sans nouvel allègement CRPA compté.",
       "La rente viagère, la pension alimentaire seulement possible dans la première hypothèse et le choix entre date d'accident et date du décès restent accessibles aux situations futures éligibles. Les deux structures familiales ne sont pas fusionnées au détriment des ascendants.",
       "Aucune réduction revendiquée : maintien du droit des ascendants, des conditions identifiant le soutien remplacé et de l'option temporelle favorable.",
       "Les plafonds collectifs de L434-14 et les preuves d'éligibilité subsistent ; aucun allègement national de prélèvements n'est déduit de ce maintien.",
       "Aucune charge nouvelle n'est identifiée : mêmes conditions, sans formulaire, certificat périodique ou contrôle préalable supplémentaire.")

retain('L434-15',
       "Maintien intégral du salaire annuel comme assiette de calcul des rentes et de l'habilitation réglementaire qui en assure l'application. Cette assiette est nécessaire à la réparation de l'incapacité ou du décès ; la supprimer ferait perdre la base de liquidation sans retirer de charge administrative autonome.",
       "La fiche source annonce ABROGE_DIFF et valid_until=2026-11-01. Le maintien de cette version ne proroge pas sa vigueur ni n'écarte la réforme AT-MP déjà programmée : elle demeure seulement dans son champ temporel légal. Le corps de remplacement complet et sa transition ne sont pas fournis ici et ne sont pas inventés.",
       "L'assiette annuelle de la rente des victimes et ayants droit est préservée pour toutes les situations couvertes par cette version, y compris les liquidations futures de faits auxquels elle demeure applicable selon la transition légale.",
       "Aucune simplification revendiquée : maintien d'une règle d'assiette de prestation dans sa période d'application, sans changement de taux ou de financement.",
       "L'abrogation au 1er novembre 2026 et la transition AT-MP sont préexistantes. Le maintien n'est ni leur réécriture ni une prolongation de cette version.",
       "Aucune charge nouvelle n'est identifiée : les deux alinéas et l'habilitation existante restent entiers, sans justificatif salarial ou dépôt périodique nouveau.")

retain('L434-17',
       "Maintien intégral de la revalorisation annuelle des rentes AT-MP au 1er avril. Cette garantie du revenu réparateur n'est ni une cotisation, ni une formalité à supprimer. La suspension d'indexation proposée pour certaines pensions de retraite ne réduit pas ces rentes.",
       "L434-15 et L161-25 ont été lus ; le coefficient général et son plancher à un restent applicables. Les trois versions L434-15 à L434-17 sont données comme abrogées à effet différé au 1er novembre 2026 : leur maintien ne prolonge pas leur vigueur. La version nouvelle de L434-3 du corpus mentionne cette revalorisation ; son raccordement temporel avec la réforme AT-MP reste à coordonner, sans inventer de futur corps.",
       "La revalorisation des rentes couvertes et le plancher du coefficient restent applicables aux situations relevant légalement de cette version, sans transformer ces rentes en pensions soumises au gel temporaire proposé.",
       "Aucun allègement revendiqué : maintien d'une garantie d'indexation de prestation réparatrice dans le champ temporel de la source entière.",
       "L'abrogation différée et la succession des textes ne sont pas refondues ici ; aucun gel des rentes ni prorogation indéfinie de cette version n'est décidé.",
       "Aucune charge nouvelle n'est identifiée : la revalorisation reste automatique selon le coefficient existant, sans demande ou attestation nouvelle.")

retain('L434-18',
       "Maintien intégral de l'incessibilité et de l'insaisissabilité des rentes. Ces garanties protègent les ressources réparant la perte de capacité de travail et de soutien familial ; les supprimer ouvrirait la captation d'un revenu essentiel, sans retirer une formalité administrative.",
       "Le champ reste toutes les rentes du livre IV, sans condition nouvelle de nationalité, résidence ou date d'accident. Les procédures d'exécution des autres codes ne sont ni modifiées ni présentées comme auditées.",
       "Les deux protections demeurent pour les rentes actuelles et futures, y compris celles servies à l'étranger selon la proposition de L434-20. Aucune renonciation du bénéficiaire n'est créée.",
       "Aucune réduction revendiquée : maintien d'une protection patrimoniale essentielle directement applicable, sans prélèvement ou rapport associé.",
       "Les procédures d'exécution extérieures ne sont pas réécrites et aucun gain global de conformité n'est démontré par le maintien.",
       "Aucune charge nouvelle n'est identifiée : aucune donnée, inscription, autorisation ou démarche du rentier n'est ajoutée.")

retain('L434-19',
       "Maintien intégral du fondement des règles locales de paiement des rentes dans le Haut-Rhin, le Bas-Rhin et la Moselle. Il protège la continuité territoriale du versement ; l'article n'institue ni formalité redondante ni taxe autonome. L'habilitation transitoire reste limitée à ce besoin.",
       "Les trois départements et la référence à l'article 612 du code local des assurances sociales du 19 juillet 1911 sont conservés. Ce texte local intégral et les éventuelles mesures transitoires ne sont pas fournis dans le corpus autorisé : leur examen matériel n'est pas prétendu achevé et aucun effet favorable n'est supprimé par inférence.",
       "Le maintien évite d'effacer les modalités locales de paiement éventuellement favorables, y compris pour les futures situations éligibles. Le seul article de renvoi ne permet pas d'épuiser ou de quantifier leur contenu.",
       "Aucun changement matériel revendiqué : maintien de la continuité du paiement local sans inventer de charge supprimée dans un texte externe non fourni.",
       "L'article 612 local et ses transitions ne sont pas disponibles intégralement ici ; leur examen matériel ne peut être déclaré achevé à partir de ce renvoi.",
       "Aucune charge nouvelle n'est identifiée : aucun justificatif territorial, déclaration ou circuit supplémentaire n'est ajouté au texte maintenu.")

retain('L434-21',
       "Maintien intégral de l'habilitation d'application de L434-4 et L434-5. Ces articles règlent la conversion de rente de personnes détenues ou relevant de l'éducation surveillée. L'habilitation n'ajoute ni agrément, ni déclaration, ni prélèvement : sa suppression isolée n'allégerait pas leurs règles substantielles et fragiliserait leur exécution.",
       "L434-4 et L434-5, lus en entier, visent la conversion de L434-3. La version récente de ce dernier, également lue, porte sur la conversion partielle en rente réversible et renvoie à un I de L434-2 absent de la version ancienne fournie comme cible. Cette discordance temporelle préexistante est à coordonner avec la réforme AT-MP de 2025 ; elle ne permet pas de déclarer les conversions disparues ni de supprimer leurs avantages. Les deux cibles directes de L434-21 existent.",
       "Le fondement d'application de la conversion reste entier sans suppression de l'option de réversion. Les conditions temporelles des articles visés gardent leur champ ; le maintien n'est pas limité à une extinction administrative des anciens droits.",
       "Aucune réduction revendiquée : habilitation d'exécution conservée pour la protection et la conversion de rente, sans obligation administrative supplémentaire dans la source.",
       "Les restrictions de conversion et la succession des versions AT-MP ne sont pas réformées par cet article d'application ; leur raccordement futur n'est pas déclaré achevé.",
       "Aucune charge nouvelle n'est identifiée : compétence réglementaire existante maintenue sans nouvelle autorisation, pièce ou demande.")

retain('L435-1',
       "Maintien intégral de la prise en charge des frais funéraires par la caisse. Les frais réellement exposés et le maximum réglementaire bornent le remboursement sans instituer de taxe ; supprimer ce dispositif retirerait une prestation essentielle aux proches.",
       "Les deux limites cumulatives et le maximum par arrêté interministériel sont conservés. La note du décret 73-598 étend l'application aux salariés agricoles et reste une donnée d'application, sans extension implicite des autres réformes. Aucun montant de plafond absent de la source n'est inventé.",
       "Le paiement reste ouvert aux décès futurs éligibles du livre IV et, selon la note, au régime obligatoire des salariés agricoles. Cette prestation n'est pas un droit de succession supprimé par l'orientation de l'auteur.",
       "Aucun allègement revendiqué : maintien d'une dépense sociale limitée aux frais réels, distincte d'un prélèvement sur le décès.",
       "Le maximum et les justificatifs de l'arrêté ne sont pas refondus à partir de cet article ; aucun coût national ni économie n'est chiffré.",
       "Aucune charge nouvelle n'est identifiée : aucune facture supplémentaire, autorisation ou procédure nouvelle n'est ajoutée.")

retain('L435-2',
       "Maintien intégral du remboursement du transport du corps au lieu de sépulture en France choisi par la famille lorsque le coût résulte du recrutement éloigné ou d'un déplacement professionnel. Ces circonstances rattachent le coût au travail ; aucune taxe ou formalité redondante autonome n'est instituée.",
       "Les deux faits ouvrant droit, les frais entièrement exposés ou seulement augmentés, la demande familiale et la destination en France restent tous conservés. La note agricole du décret 73-598 est maintenue. Aucun montant ou nouveau justificatif n'est substitué au décret de calcul des frais.",
       "Le choix familial et la prise en charge totale ou du surcoût demeurent possibles pour les situations futures éligibles, y compris agricoles dans le champ de la note. Aucune condition d'ancienneté ou de contrat nouveau n'est ajoutée.",
       "Aucun changement matériel revendiqué : maintien de la prise en charge du coût professionnel du transport funéraire et de ses deux cas d'ouverture.",
       "La couverture n'est pas étendue à toute sépulture à l'étranger ou à un transport sans lien professionnel ; aucun coût ou gain de conformité n'est estimé.",
       "Aucune charge nouvelle n'est identifiée : mêmes circonstances et modalités réglementaires de calcul, sans pièce ni autorisation nouvelle.")

retain('L436-1',
       "Maintien intégral de l'astreinte judiciaire pour retard injustifié du paiement des prestations en espèces. Elle rend effectif le versement d'une réparation essentielle ; il ne s'agit ni d'une majoration de cotisations à supprimer, ni d'un délai minimal administratif imposé à l'entreprise.",
       "Indemnité journalière, capital et rentes restent couverts. Déclenchement, périodicité et taux relèvent du décret en Conseil d'Etat, sans valeur inventée. Le juge reste compétent. Aucun rapprochement avec le préavis de quinze jours ou l'indemnité ordinaire de rupture n'est opéré.",
       "Le recours à l'astreinte demeure accessible aux bénéficiaires actuels et futurs pour les trois prestations. Le caractère injustifié du retard et le contrôle du juge ne sont pas aggravés ni remplacés par un visa administratif.",
       "Aucun allègement revendiqué : sanction judiciaire de retard protectrice du bénéficiaire, distincte d'un prélèvement social accessoire.",
       "Les valeurs réglementaires et procédures contentieuses ne sont pas refondues ; ce maintien ne démontre aucun raccourcissement du délai réel de paiement.",
       "Aucune charge nouvelle n'est identifiée : ni nouvelle mise en demeure ni nouveau registre n'est ajouté au recours existant.")

retain('L437-1',
       "Maintien intégral de la charge de réparation attribuée aux caisses primaires. Cette règle désigne le débiteur des prestations et évite de laisser leur financement à la victime ; elle ne fixe ni taux de cotisation, ni prélèvement accessoire ou déclaration autonome.",
       "La note du 1er janvier 2018 est historique. Malgré l'intitulé du chapitre relatif au fonds commun, le corps n'ordonne ni nouveau fonds ni versement particulier : aucune structure ou taxe fictive n'est supprimée. Les nouveaux droits de L434-20 restent à chiffrer sans financement compensateur inventé.",
       "Le financement de la réparation par les caisses est maintenu ; cela ne promet pas une réparation sans plafonds de tous les préjudices. Aucun droit du bénéficiaire n'est remplacé par une obligation de financer sa propre prestation.",
       "Aucun transfert ou baisse de prélèvement revendiqué : le débiteur reste la caisse primaire et aucune taxe propre au fonds du titre n'est instituée dans la source.",
       "Les cotisations de branche et les équilibres d'autres réformes ne sont pas fixés ici ; aucun autofinancement des nouveaux droits n'est présumé.",
       "Aucune charge nouvelle n'est identifiée : attribution financière inchangée, sans rapport, recette compensatrice ou donnée supplémentaire.")

retain('L441-1',
       "Maintien intégral de l'information initiale de l'employeur et de ses trois excuses. Ce signalement permet déclaration et prévention rapides d'un risque professionnel ; il n'est pas un doublon de la déclaration à la caisse, dont le destinataire et la fonction diffèrent.",
       "R441-2, lu en entier, prévoit la journée ou vingt-quatre heures et permet l'information sur place, sinon un moyen conférant date certaine. Force majeure, impossibilité absolue et motifs légitimes restent conservés. Aucune déchéance du droit aux prestations n'est inventée. La note de 1987 est historique.",
       "La victime peut faire informer l'employeur ou un préposé et conserve les trois exceptions au délai pour tous les futurs accidents, sans condition d'ancienneté ou de type de contrat.",
       "Aucun gain nouveau revendiqué : le signalement nécessaire et ses dispenses légitimes sont maintenus intégralement, sans preuve formelle additionnelle.",
       "Le délai réglementaire d'information subsiste ; il ne se confond ni avec la prescription de déclaration à la caisse ni avec le préavis de rupture du contrat.",
       "Aucune charge nouvelle n'est identifiée : le droit de faire informer et les excuses demeurent sans nouveau moyen exclusif de transmission.")

retain('L441-3',
       "Maintien intégral des constatations nécessaires dès connaissance de l'accident et de l'avis immédiat à l'inspection compétente. L'instruction rend les droits effectifs même hors circuit déclaratif ; l'avis sert la prévention. Leurs fonctions distinctes ne révèlent pas de doublon privé inutile.",
       "Le déclenchement par quelque moyen que ce soit reste entier, sans formulaire obligatoire nouveau. Le fonctionnaire exerçant les attributions de l'inspecteur dans une législation spéciale demeure visé. La dispense de second dépôt de L441-2 ne supprime ni constatation ni avis de sécurité.",
       "La connaissance de la caisse par tout moyen continue de déclencher les constatations nécessaires, pour les futurs accidents comme pour les régimes spéciaux visés. La garantie ne dépend pas du seul dépôt de l'employeur.",
       "Aucun allègement revendiqué : maintien de l'instruction des droits et du signalement à l'autorité de sécurité, sans obligation privée nouvelle.",
       "Le fonctionnement interne et le coût des échanges ne sont pas chiffrés ; aucune fusion avec une notification extérieure non fournie n'est affirmée.",
       "Aucune charge nouvelle n'est identifiée : mêmes constatations et avis, sans rapport, registre ou transmission supplémentaire exigé de la victime.")

retain('L441-5',
       "Maintien intégral de la feuille d'accident délivrée par l'employeur. Elle ouvre l'accès aux soins sans avance selon L432-3 ; la supprimer sans support de droits effectivement équivalent risquerait de transférer un coût à la victime. La source n'impose pas de copies de conservation redondantes.",
       "L432-3, lu en entier, interdit les honoraires à la victime présentant la feuille, sous réserve du dépassement autorisé. L471-1 et R471-3, lus, visent précisément le premier alinéa de délivrance. Le décret d'utilisation est conservé sans inventer de nouvel accès informatique aux données.",
       "La feuille et la dispense d'avance qu'elle permet restent ouvertes aux futurs accidents, sous contrats anciens ou uniques. Aucun seuil d'ancienneté, accord patronal de reconnaissance ou frais de délivrance n'est ajouté.",
       "Aucune réduction revendiquée : maintien d'un justificatif servant la dispense d'avance de frais et l'accès effectif aux soins, sans formalité de remplacement.",
       "Le formulaire et ses modalités réglementaires ne sont pas refondus ; aucun gain nouveau de réemploi ou d'interopérabilité n'est démontré ici.",
       "Aucune charge nouvelle n'est identifiée : même remise et habilitation existantes, sans pièce additionnelle ou nouvelle condition de prise en charge.")

retain('L441-6',
       "Maintien intégral des certificats initial et de guérison ou consolidation, de leurs deux destinataires et de la protection contre les honoraires en cas de manquement hors urgence. L'un établit lésions et suites, l'autre les conséquences définitives. Copie au patient et transmission à la caisse protègent des intérêts distincts ; leur nombre ne prouve pas une duplication inutile.",
       "L321-2 et L432-3 ont été lus. L'avis d'interruption, toutes les pièces du certificat final et la réserve sur les conséquences non antérieurement constatées demeurent. R441-7, lu, utilise le certificat initial pour l'instruction de trente jours francs : il ne peut être effacé sans altérer les droits. La proposition séparée de L321-2 ne supprime pas l'avis authentique. La note du 1er novembre 2021 est historique. Le mot 'exemplaire' ne prouve pas deux originaux ou deux consultations ; aucune suppression fictive de ces exigences n'est comptée.",
       "La victime conserve son exemplaire, toutes les pièces de consolidation et la protection contre les honoraires hors urgence en cas de manquement du praticien. Les futurs soins et consolidations restent couverts sans restriction d'avantage.",
       "Aucune simplification démontrée : deux stades médicaux et deux destinataires répondent à des besoins distincts. Un nouveau libellé conservant les mêmes fonctions ne prouverait aucune obligation supprimée.",
       "Aucun examen systématique supplémentaire n'est ajouté ; deux originaux ou consultations ne sont pas déduits du seul texte. Les coûts techniques de transmission ne sont pas chiffrés.",
       "Aucune charge nouvelle n'est identifiée : mêmes certificats, avis, copies et pièces, sans nouveau formulaire ou rendez-vous.")


old = by_num['L434-10']['source_xml']
new = old.replace('L. 311-7 du code du travail', 'L. 5312-1 du code du travail')
assert new != old
make('L434-10', new,
     "Coordination nécessaire à droit constant : remplacement de l'ancien renvoi institutionnel L311-7 du code du travail par L5312-1, qui définit France Travail et sa mission d'inscription des demandeurs d'emploi. Les cinq alinéas de rente sont intégralement conservés ; aucune condition de durée d'emploi n'est ajoutée pour l'apprentissage en contrat unique.",
     "Nouveau renvoi à une cible non fournie dans reference-targets.json : travail L5312-1, LEGIARTI000053606086, lu en entier avec ses notes dans travail.json du corpus autorisé. Son I et son 3° visent l'institution et l'inscription. La correction ne conditionne pas la rente aux autres missions d'accompagnement. R434-15, lu, fixe notamment l'âge à vingt ans et les fractions à 25 %, 20 % et 30 % ; aucun paramètre n'est modifié. Les possibilités législatives de relèvement d'âge demeurent, sans extension réglementaire prétendue. La phase d'apprentissage peut être limitée sans limiter l'emploi nouveau.",
     "Filiation adoptive, quatre motifs de relèvement d'âge, majoration des orphelins des deux parents, progression selon le nombre d'enfants, catégories de plusieurs lits et assimilation des descendants et enfants recueillis à charge sont conservés. Ces avantages restent ouverts aux futures situations éligibles, notamment aux apprentis en contrat indéterminé.",
     impact('coordination_only',
            "Seul le numéro de l'article désignant l'institution d'inscription est actualisé ; montant, âge, champ familial et devoir déclaratif ne changent pas par rapport à la source entière.",
            "La correction n'est pas une baisse de cotisations et ne modifie pas le barème réglementaire. Le contrat unique ne fixe pas la durée de la rente et ne transforme pas l'apprentissage en CDD.",
            "Aucune charge nouvelle n'est identifiée : même inscription déjà requise, sans justificatif, délai ou formulaire supplémentaire.",
            [effect('coordination', 'rentes-at-mp-renvoi-france-travail',
                    "Actualisation de la référence légale de l'institution d'inscription.",
                    "Inscription auprès de l'institution désignée par l'ancien L311-7 pour l'un des cas de relèvement d'âge.",
                    "Même inscription et même relèvement, avec renvoi à L5312-1 désignant France Travail.",
                    'other', "Enfants rentiers recherchant leur première activité professionnelle.",
                    "Correction sans extinction de droit antérieur ni restriction des situations futures.",
                    "Aucun dépôt ou condition supplémentaire.",
                    "inscrits comme demandeurs d'emploi à l'institution mentionnée à l'article L. 311-7 du code du travail",
                    "inscrits comme demandeurs d'emploi à l'institution mentionnée à l'article L. 5312-1 du code du travail")]))

old = by_num['L434-14']['source_xml']
new = old.replace("allouées en application du présent article à l'ensemble des ayants droit",
                  "allouées en application des articles L. 434-7 à L. 434-13 à l'ensemble des ayants droit")
assert new != old
make('L434-14', new,
     "Coordination nécessaire du second alinéa : le renvoi autoréférentiel est remplacé par les articles ouvrant les rentes d'ayants droit. Les deux plafonds, leurs assiettes et les réductions proportionnelles demeurent entiers. La correction explicite le champ collectif sans inventer de taux, plafond ou économie.",
     "Incohérence préexistante : le second alinéa renvoyait au présent article, qui n'ouvre aucune catégorie de rente. Nouveau renvoi explicite à L434-7 à L434-13, non fourni comme ensemble de cibles pour cet article : L434-7 et L434-8 ont été lus dans le corpus, L434-9 à L434-13 dans les sources intégrales du lot. R434-16, lu, distingue expressément les plafonds de 30 % pour les ascendants et 85 % pour tous les ayants droit. Valeurs et assiette annuelle ne changent pas. Ce n'est pas une nouvelle réduction de prestations.",
     "Les droits individuels et la réduction proportionnelle à l'intérieur des catégories sont conservés. Le renvoi n'ajoute aucun cumul au plafond et ne retire aucun droit à rente, pour les anciens dossiers comme pour les familles futures éligibles.",
     impact('coordination_only',
            "Le champ du second plafond est explicité par les articles ouvrant les rentes, sans changement de quotité, assiette ou répartition par rapport à la fonction de la source entière.",
            "La lecture est confortée par R434-16 ; aucun gain financier ou retrait de formalité n'est démontré. Les règles concrètes de liquidation restent à leur champ.",
            "Aucune charge nouvelle n'est identifiée : le renvoi corrigé ne demande aucune donnée, démarche, notification ou preuve supplémentaire.",
            [effect('coordination', 'at-mp-plafond-ayants-droit-renvoi',
                    "Correction du renvoi autoréférentiel obscurcissant le plafond collectif.",
                    "Rentes allouées en application du présent article, bien que leur ouverture soit définie aux articles précédents.",
                    "Rentes des articles L434-7 à L434-13, avec mêmes plafond et réduction proportionnelle.",
                    'other', "Ensemble des ayants droit d'une victime d'accident du travail.",
                    "Clarification à droit constant sans réduction nouvelle ni modification de droit antérieur.",
                    "Aucune obligation de remplacement ou donnée nouvelle.",
                    "Le total des rentes allouées en application du présent article à l'ensemble des ayants droit de la victime",
                    "Le total des rentes allouées en application des articles L. 434-7 à L. 434-13 à l'ensemble des ayants droit de la victime")]))

old = by_num['L434-16']['source_xml']
new = old.replace("salaire minimum déterminé à l'alinéa précédent",
                  "salaire minimum déterminé au premier alinéa du présent article")
assert new != old
new += ps("La présente rédaction ne modifie ni la date d'abrogation du présent article déjà fixée au 1er novembre 2026, ni le champ d'application dans le temps des règles de calcul des rentes.")
make('L434-16', new,
     "Coordination nécessaire à droit constant : le troisième alinéa renvoie au premier alinéa qui détermine le minimum salarial et non au deuxième qui ne le définit pas. Minimum, revalorisation au 1er avril, rentes individuelles et collectives, dégressivité et accidents successifs restent entiers. Une réserve temporelle empêche de proroger l'article dont l'abrogation est déjà programmée.",
     "Incohérence préexistante : le minimum ne figure pas au deuxième alinéa. R434-27/R434-28, lus, renvoient au premier ; le double du minimum, le tiers d'excédent et la limite de huit fois le minimum de R434-28 restent inchangés. Le quatrième alinéa de L434-2 fourni vise les accidents successifs. Sa structure ancienne et la version récente de L434-3 du corpus présentent une articulation temporelle à coordonner avec la réforme AT-MP de 2025 ; aucun futur corps n'est reconstitué. ABROGE_DIFF au 1er novembre 2026 est préservé, non une date de promulgation proposée. L161-25, lu en entier avec sa proposition, conserve l'indexation générale et le plancher à un : le gel des pensions n'est pas étendu aux rentes.",
     "Le plancher de salaire, son indexation et les protections des accidents successifs restent applicables aux situations dans le champ temporel de l'article. Dégressivité et conditions ne sont pas aggravées ; aucun gel de rente n'est créé au titre de la retraite.",
     impact('coordination_only',
            "Correction de l'alinéa désignant le minimum et réserve de la limite temporelle existante ; aucune baisse de prélèvement ou de prestation revendiquée.",
            "L'article n'est pas prorogé au-delà de l'abrogation prévue au 1er novembre 2026. Le raccordement du futur régime AT-MP est distinct de la version assignée.",
            "Aucune charge nouvelle n'est identifiée : mêmes calculs existants, sans formulaire, délai, contrôle ou donnée supplémentaire.",
            [effect('coordination', 'at-mp-salaire-minimum-renvoi',
                    "Correction de l'alinéa qui détermine réellement le salaire minimum.",
                    "Le troisième alinéa renvoie au minimum de l'alinéa précédent, bien que le deuxième n'en fixe aucun.",
                    "Renvoi au premier alinéa, sans changement du minimum ni de la dégressivité.",
                    'other', "Victimes dont la rente relève de cette version de L434-16.",
                    "Même champ temporel sans prorogation de la vigueur déjà bornée.",
                    "Aucune nouvelle condition ou démarche.",
                    "salaire minimum déterminé à l'alinéa précédent",
                    "salaire minimum déterminé au premier alinéa du présent article")]))

xml20 = ps(
    "Les travailleurs étrangers victimes d'accidents qui cessent de résider sur le territoire français conservent le droit au service de leur rente. Ils peuvent choisir de recevoir, en remplacement des arrérages futurs de cette rente, un capital égal à un multiple du montant annuel de leur rente.",
    "Il en est de même pour les ayants droit étrangers cessant de résider sur le territoire français, sans toutefois que le capital choisi puisse alors dépasser la valeur de la rente d'après le tarif résultant du présent code.",
    "Le droit à indemnisation des ayants droit étrangers d'un travailleur étranger n'est pas subordonné à leur résidence sur le territoire français au moment de l'accident.",
    "Les dispositions des trois alinéas précédents peuvent toutefois être modifiées par traités ou par conventions internationales, dans la limite des indemnités prévues au présent livre.",
    "La présente rédaction s'applique aux arrérages afférents aux périodes commençant à compter de l'entrée en vigueur de la loi portant sa modification, y compris lorsque l'accident est antérieur, sous réserve des règles de prescription applicables. Les périodes antérieures restent régies par les dispositions qui leur étaient applicables. Les capitaux régulièrement versés demeurent acquis à leurs bénéficiaires. Les capitaux déjà versés pour éteindre une rente ne donnent pas droit à un nouveau service de cette rente ni à un second capital. Aucun remboursement général de ces capitaux n'est institué. Le choix du capital pour une rente encore servie n'impose aucune déclaration périodique supplémentaire.")
make('L434-20', xml20,
     "Réforme de fond : suppression de la perte automatique du service de la rente lors d'un départ à l'étranger et de l'exclusion des ayants droit étrangers non résidents au jour de l'accident. Ces conditions spéciales ne servent ni la constatation du risque professionnel ni le calcul du dommage. Le capital obligatoire devient une option, avec son multiple et le plafond actuariel des ayants droit préservés. Aucun impôt sur le décès n'est en cause. Le quatrième alinéa international reste entier.",
     "R434-35, lu, fixe le capital du premier alinéa à trois fois la rente annuelle : même paramètre pour l'option, sans barème d'indemnité de rupture. Coordonner les règles réglementaires de paiement et preuve d'existence sans rétablir résidence ou rachat forcé. Le quatrième alinéa réserve les traités, conventions et contraintes européennes ; leur vérification complète n'est pas affirmée à partir du corpus national. Les conditions communes et les plafonds collectifs de L434-14 demeurent ; l'incidence distributive des nouvelles ouvertures dans ces plafonds et le coût social ne sont pas chiffrés. Seulement des arrérages nouveaux dans les limites de prescription ; aucun second paiement après rachat définitif, aucune recette compensatrice.",
     "L'option favorable de capital, son assiette, son multiple et le plafond propre aux ayants droit sont conservés. La rente devient exportable sans résidence continue en France et les ayants droit non résidents au jour de l'accident ne sont plus exclus pour ce motif. Les avantages conventionnels gardent leur champ ; les capitaux payés restent acquis sans double indemnisation.",
     impact('mixed',
            "Deux restrictions territoriales sont retirées : rachat forcé au départ et exclusion totale de certains ayants droit. Cet élargissement ajoute corrélativement des prestations à servir par les caisses. Aucun solde net ni baisse de taux fiscal ou de cotisation n'est revendiqué.",
            "Conditions communes, plafonds et cadre international subsistent. Périodes anciennes et rentes déjà rachetées ne sont pas rouvertes ; coût et effets entre catégories restent non chiffrés.",
            "Aucune charge obligatoire nouvelle n'est identifiée pour recevoir la rente : choix facultatif du capital et absence de déclaration périodique nouvelle. Les paiements à l'étranger et nouvelles liquidations peuvent accroître dépenses et traitement des caisses ; le solde n'est pas établi.",
            [effect('relief_extended', 'at-mp-rentes-sans-condition-de-residence',
                    "Suppression des deux restrictions territoriales : rente conservée au départ avec option de capital et fin de l'exclusion des ayants droit non résidents lors de l'accident. Une seule mesure est recensée pour ces deux composantes.",
                    "Travailleur étranger quittant la France : capital obligatoire égal à un multiple de la rente annuelle, fixé à trois par R434-35 ; ayant droit étranger quittant la France : même mécanisme sous plafond actuariel. Ayants droit étrangers d'un travailleur étranger non résidents au jour de l'accident : aucune indemnité sur ce fondement, sous réserve des règles internationales.",
                    "Victimes et ayants droit étrangers quittant la France : service de rente conservé, capital facultatif avec mêmes multiple, assiette annuelle et plafond actuariel des ayants droit. Ayants droit non résidents au jour de l'accident : indemnisation selon les conditions communes sans cette exclusion. Aucun taux fiscal ou social modifié.",
                    'regime', "Victimes étrangères et ayants droit étrangers quittant la France, ainsi que les ayants droit étrangers d'un travailleur étranger non résidents au jour de l'accident, dans le champ du livre IV.",
                    "Arrérages des périodes commençant dès l'entrée en vigueur, même pour un accident antérieur, dans les limites de prescription ; périodes anciennes et rentes déjà rachetées exclues du nouveau service, sans second capital ; règles internationales réservées.",
                    "Aucune déclaration périodique ou taxe de remplacement ; choix facultatif du capital. Paiements et liquidations publics supplémentaires recensés sous obligation_added pour cette même mesure, avec coût net non établi.",
                    text(by_num['L434-20']['source_xml']).split('Il en est de même')[0].strip(),
                    text(xml20).split('Il en est de même')[0].strip())]),
     ["Rachat obligatoire de la rente des travailleurs étrangers et de leurs ayants droit du seul fait du départ de France, remplacé par le maintien du service avec option de capital.",
      "Exclusion de toute indemnisation des ayants droit étrangers d'un travailleur étranger non résidents en France au moment de l'accident."])

answers['L434-20']['substantive_impact']['effects'].append(
    effect('obligation_added', 'at-mp-rentes-sans-condition-de-residence',
           "Contrepartie des droits élargis : prestations et liquidations supplémentaires à la charge des caisses, sans constituer une seconde mesure de réduction.",
           "Pour les ayants droit étrangers non résidents au jour de l'accident, aucune indemnité due sur le fondement du troisième alinéa, sauf règles internationales ; pour les départs, versement d'un capital en lieu de rente.",
           "Les caisses doivent liquider les droits des ayants droit désormais éligibles et poursuivre le service des rentes exportées, sauf option de capital et sous les conditions communes. Charge publique supplémentaire non chiffrée.",
           'legal_duty', "Caisses débitrices des prestations du livre IV et nouveaux bénéficiaires étrangers éligibles.",
           "Seulement arrérages des nouvelles périodes dans les limites de prescription ; capitaux acquis et périodes anciennes non remis en cause, cadre international réservé.",
           "Obligation publique corrélative aux droits sociaux nouveaux ; aucune déclaration périodique ou taxe de financement nouvelle. Le solde public et les effets distributifs ne sont pas établis.",
           "Les ayants droit étrangers d'un travailleur étranger ne reçoivent aucune indemnité si, au moment de l'accident, ils ne résident pas sur le territoire français.",
           "Le droit à indemnisation des ayants droit étrangers d'un travailleur étranger n'est pas subordonné à leur résidence sur le territoire français au moment de l'accident."))

xml4412 = ps(
    "L'employeur ou l'un de ses préposés doit déclarer tout accident dont il a eu connaissance à la caisse primaire d'assurance maladie dont relève la victime selon des modalités et dans un délai déterminés. Lorsque la victime ou ses représentants ont déjà régulièrement déclaré le même accident à cette caisse et que celle-ci a communiqué cette déclaration à l'employeur, cette communication dispense l'employeur d'une seconde déclaration portant sur le même accident. La dispense prend effet à la date de cette communication et n'efface pas un manquement antérieur à l'obligation de déclaration. Elle ne nécessite ni confirmation, ni dépôt de remplacement et ne prive pas l'employeur de la faculté d'émettre des réserves motivées dans les conditions qui lui sont applicables.",
    "La déclaration à la caisse peut être faite par la victime ou ses représentants jusqu'à l'expiration de la deuxième année qui suit l'accident.",
    "La dispense s'applique aux déclarations à accomplir à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pour un accident antérieur, dès lors que leur délai n'est pas déjà expiré à cette date. Elle ne dispense pas des déclarations dues pour d'autres accidents. Les manquements antérieurs restent soumis aux dispositions qui leur sont applicables, sous réserve de l'application de la loi répressive plus douce.")
make('L441-2', xml4412,
     "Réforme de fond : retrait de la seconde déclaration patronale du même accident quand la caisse a reçu une déclaration régulière de la victime et l'a communiquée à l'employeur. La connaissance du risque, l'information de l'employeur et ses réserves disposent déjà de leur circuit : ce dépôt identique supplémentaire n'a pas de fonction essentielle distincte. Le dépôt initial patronal demeure dans les autres cas ; le droit autonome de la victime pendant deux ans reste entier.",
     "R441-3 et R441-6, lus, prévoient quarante-huit heures hors dimanches et jours fériés, transmission du double par la caisse et réserves dans les dix jours francs. Aucun de ces délais ne devient quinze jours de préavis. La communication effective doit intervenir avant l'échéance pour éviter le double dépôt ; la dispense ne rouvre pas d'échéance ancienne. Coordonner R441-1/R441-3 et formulaires sans second dépôt sous un autre nom ; données manquantes utiles et contradictoire de R441-6 subsistent. L471-1 et R471-3, lus, ne doivent pas sanctionner l'absence du dépôt désormais dispensé ; les sanctions autonomes et leur champ fraude/travail dissimulé restent distincts.",
     "Le droit de la victime ou de ses représentants de déclarer jusqu'à l'expiration de la deuxième année suivant l'accident est reproduit intégralement. La dispense patronale ne le conditionne pas à un accord de l'employeur et ne réduit pas la prise en charge, pour les accidents futurs sous contrat unique comme pour les contrats anciens.",
     impact('material_reduction',
            "Le dépôt patronal du même accident déjà régulièrement déclaré et communiqué par la caisse est réellement supprimé. Déclarations initiales des autres accidents et informations nécessaires à l'instruction demeurent.",
            "Le gain concerne le seul double dépôt évité avant l'échéance patronale. Signalement de sécurité, déclarations distinctes et sanctions autonomes ne sont pas supprimés ; aucun coût national n'est calculé.",
            "Aucune charge nouvelle n'est identifiée : transmission du double et réserves existaient déjà selon R441-6. Aucune attestation, confirmation ou déclaration de remplacement ne conditionne la dispense.",
            [effect('obligation_removed', 'at-mp-declaration-unique-meme-accident',
                    "Suppression du double dépôt employeur/victime après communication de la déclaration régulière.",
                    "Tout accident connu doit être déclaré par l'employeur sans dispense législative pour celui déjà déclaré par la victime et transmis par la caisse ; délai réglementaire de quarante-huit heures hors dimanches et jours fériés.",
                    "Pas de second dépôt patronal après communication par la caisse de la déclaration régulière de la victime ; même délai et même obligation initiale pour les autres accidents.",
                    'legal_duty', "Employeurs ou préposés ayant reçu de la caisse la déclaration régulière du même accident faite par la victime ou ses représentants.",
                    "Obligations non encore échues dès l'entrée en vigueur, même accidents antérieurs ; communication effective, réserves et droit autonome de la victime préservés.",
                    "Aucun dépôt de remplacement ; utilisation du circuit de transmission déjà prévu par R441-6.",
                    "L'employeur ou l'un de ses préposés doit déclarer tout accident dont il a eu connaissance à la caisse primaire d'assurance maladie dont relève la victime selon des modalités et dans un délai déterminés.",
                    "cette communication dispense l'employeur d'une seconde déclaration portant sur le même accident.")]),
     ["Seconde déclaration patronale du même accident déjà régulièrement déclaré par la victime ou ses représentants et effectivement communiqué à l'employeur par la caisse."])

xml4414 = ps(
    "L'employeur peut, selon les modalités de tenue du registre prévues par décret, remplacer la déclaration des accidents n'entraînant ni arrêt de travail, ni soins médicaux par une inscription sur un registre ouvert à cet effet. Cette faculté est ouverte sans condition particulière tenant à la présence permanente d'un professionnel de santé ou d'un secouriste, à l'existence d'un poste de secours d'urgence ou au respect préalable des obligations de représentation du personnel. Elle n'est subordonnée ni à une autorisation ni à une déclaration préalable à un organisme de sécurité sociale. Elle ne dispense d'aucune obligation de prévention, de secours ou de représentation du personnel applicable par ailleurs.",
    "L'employeur est tenu d'en aviser le comité social et économique.",
    "Ce registre est tenu à la disposition des agents de contrôle des organismes chargés de la gestion des accidents du travail et des maladies professionnelles mentionnés à l'article L. 114-10 ainsi que des ingénieurs conseils et contrôleurs de sécurité dûment habilités auprès des caisses d'assurance retraite et de la santé au travail, de l'autorité compétente de l'Etat et du comité social et économique.",
    "Lorsqu'un accident ayant fait l'objet d'une simple inscription sur un registre entraîne ultérieurement un arrêt de travail ou des soins médicaux, l'employeur est tenu d'adresser à la caisse primaire dont relève la victime la déclaration prévue à l'article L. 441-2 dans un délai déterminé.",
    "Les présentes dispositions s'appliquent aux inscriptions et formalités à accomplir à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pour un accident antérieur. Elles ne dispensent pas de conserver les inscriptions antérieures pendant leur durée réglementaire, ni de déclarer une aggravation ou de respecter les droits de la victime. Aucune déclaration initiale de recours au registre n'est exigée après cette date, y compris pour un registre déjà ouvert.")
make('L441-4', xml4414,
     "Réforme de fond : ouverture du registre des accidents bénins sans les trois conditions d'accès imposées par décret et sans déclaration initiale à l'organisme social. Personnel de soins permanent, poste de secours et régularité préalable du CSE ne sont plus des prérequis à ce seul mode d'enregistrement d'un accident sans arrêt ni soins. Les obligations de sécurité et de représentation demeurent indépendamment exigibles. Registre, avis au CSE, accès de contrôle et déclaration d'aggravation sont préservés ; aucune déclaration équivalente de remplacement n'est créée.",
     "D441-1 à D441-4 et R441-5 ont été lus en entier. Coordonner les 1° à 3° de D441-1 comme conditions d'accès, la déclaration CARSAT de D441-2 et le motif de retrait lié à ces seules conditions dans D441-4 2°. Support au choix, mentions, signature de la victime, contrôle et cinq ans de conservation restent à leur champ ; ils ne sont pas supprimés. R441-5 conserve les quarante-huit heures pour l'aggravation. La législation 'ni soins médicaux' et la formulation réglementaire plus étroite 'soins ... pris en charge' de D441-3 présentent une différence préexistante à coordonner sans restreindre les droits. Alinéas 2 à 4 maintenus à leur place pour R441-5, L471-1 et R471-3. L'autorisation préalable était déjà supprimée en 2021 : aucun nouveau gain d'autorisation supprimée n'est compté.",
     "La dispense par registre devient accessible aux entreprises futures et à celles sans personnel de soins permanent ; les devoirs de secours restent exigibles. Registre consultable, information du CSE et déclaration d'aggravation protègent toujours la victime. Aucun ancien registre ni droit à indemnisation n'est fermé.",
     impact('material_reduction',
            "Les prérequis particuliers d'une dispense et l'information initiale de l'organisme social sont retirés. Registre et garanties de prévention, contrôle et prise en charge après aggravation restent entiers.",
            "Les obligations générales de secours et de CSE ne sont pas supprimées. L'allègement concerne seulement les accidents sans arrêt ni soins et appelle les coordinations réglementaires identifiées, sans multiplier le compte par texte d'exécution.",
            "Aucune charge nouvelle n'est identifiée : le registre reste une option préexistante avec mentions et accès actuels ; aucune déclaration équivalente ne remplace l'information initiale CARSAT supprimée. Le coût public net n'est pas évalué.",
            [effect('relief_extended', 'at-mp-registre-benins-acces-simplifie',
                    "Extension de la dispense par registre sans prérequis particuliers de moyens de secours ou de régularité préalable du CSE.",
                    "Option conditionnée par décret ; D441-1 exige soignant ou secouriste permanent, poste de secours et respect de L2311-2, D441-2 une information initiale à la CARSAT.",
                    "Option sans ces prérequis ni déclaration initiale à un organisme social ; prévention, secours, CSE, enregistrement, contrôles et déclaration d'aggravation subsistent.",
                    'regime', "Employeurs enregistrant des accidents sans arrêt de travail ni soins médicaux dans le champ du livre IV.",
                    "Inscriptions et formalités futures dès l'entrée en vigueur, même accidents ou registres antérieurs ; archives existantes et droits des victimes conservés.",
                    "Aucun nouveau registre, agrément ou dépôt de remplacement ; garanties du registre existant maintenues.",
                    "L'employeur, dès lors qu'il remplit des conditions fixées par décret, peut, selon des modalités prévues par décret, remplacer la déclaration des accidents n'entraînant ni arrêt de travail, ni soins médicaux par une inscription sur un registre ouvert à cet effet.",
                    "Cette faculté est ouverte sans condition particulière tenant à la présence permanente d'un professionnel de santé ou d'un secouriste, à l'existence d'un poste de secours d'urgence ou au respect préalable des obligations de représentation du personnel.")]),
     ["Condition d'accès au registre subordonnée aux trois prérequis réglementaires de personnel de soins permanent, poste de secours et conformité préalable de la représentation du personnel.",
      "Information initiale de recours au registre auprès d'un organisme de sécurité sociale, y compris pour un registre déjà ouvert dont la formalité resterait à accomplir."])

xml4424 = ps(
    "La caisse doit, si les ayants droit de la victime le sollicitent ou avec leur accord si elle l'estime elle-même utile à la manifestation de la vérité, demander au tribunal judiciaire dans le ressort duquel l'accident s'est produit de faire procéder à l'autopsie dans les conditions prévues aux articles 232 et suivants du code de procédure civile. L'opposition des ayants droit à l'autopsie demandée par la caisse n'emporte, à elle seule, ni renversement de la charge de la preuve du lien de causalité entre l'accident et le décès, ni privation du bénéfice des présomptions légalement applicables. Ce lien est apprécié au vu des autres éléments de preuve admissibles et des règles d'instruction applicables.",
    "La suppression de la conséquence probatoire attachée à la seule opposition à l'autopsie s'applique aux demandes et aux instances en cours à la date d'entrée en vigueur de la loi portant la présente modification. Elle ne remet pas en cause les décisions juridictionnelles devenues irrévocables.")
make('L442-4', xml4424,
     "Réforme de fond : suppression du transfert automatique de la charge de la preuve aux ayants droit pour le seul refus d'autopsie. Cette conséquence spéciale n'est pas nécessaire à la recherche de causalité puisque preuves, instruction et présomptions légalement applicables demeurent. Droit de solliciter l'autopsie, accord requis lorsque la caisse en prend l'initiative et intervention du tribunal sont conservés.",
     "La première phrase conserve le tribunal du lieu de l'accident et les articles 232 et suivants du code de procédure civile. Leur corps n'est pas fourni dans le corpus autorisé : aucune réécriture de procédure civile, expertise pénale ou autopsie imposée sur un fondement autonome n'est affirmée. Seule la conséquence sociale du refus est retirée ; aucune présomption absolue de décès professionnel ni interdiction des preuves contraires n'est créée. Application aux demandes et instances en cours sans réouverture des décisions irrévocables ni rappel forfaitaire général.",
     "Le droit des proches de demander l'autopsie et de consentir ou non à celle sollicitée par la caisse demeure pour les futurs décès et les dossiers en cours. Le refus seul ne fait plus perdre les règles ordinaires de preuve et les présomptions favorables ; le lien avec l'accident reste nécessaire.",
     impact('material_reduction',
            "La contrainte probatoire spéciale attachée au seul refus d'autopsie est effectivement retirée. L'exigence de causalité et les moyens ordinaires d'investigation subsistent.",
            "Aucune causalité professionnelle automatique. Expertises et autopsies fondées sur d'autres textes et décisions irrévocables restent hors réforme ; aucun effet budgétaire global n'est établi.",
            "Aucune charge nouvelle n'est identifiée : aucune attestation ou expertise de remplacement n'est imposée. Les autorités apprécient les preuves selon les règles existantes sans registre ou procédure obligatoire nouveau.",
            [effect('obligation_removed', 'at-mp-autopsie-fin-charge-preuve-speciale',
                    "Retrait de la charge probatoire spéciale automatiquement imposée par le seul refus.",
                    "En cas d'opposition à l'autopsie demandée par la caisse, les ayants droit doivent prouver le lien entre accident et décès selon une règle spéciale.",
                    "Le refus seul ne renverse plus la preuve et ne prive pas des présomptions légales ; causalité appréciée sur les autres preuves admissibles.",
                    'legal_duty', "Ayants droit s'opposant à l'autopsie demandée par la caisse pour un accident du travail mortel.",
                    "Demandes et instances en cours dès l'entrée en vigueur, puis demandes futures ; décisions irrévocables conservées.",
                    "Aucune expertise ou pièce obligatoire de remplacement ; autopsie volontaire et instruction ordinaire maintenues.",
                    "Si les ayants droit de la victime s'opposent à ce qu'il soit procédé à l'autopsie demandée par la caisse, il leur incombe d'apporter la preuve du lien de causalité entre l'accident et le décès.",
                    "L'opposition des ayants droit à l'autopsie demandée par la caisse n'emporte, à elle seule, ni renversement de la charge de la preuve du lien de causalité entre l'accident et le décès, ni privation du bénéfice des présomptions légalement applicables.")]),
     ["Renversement automatique de la charge de la preuve du lien causal entre accident et décès au seul motif de l'opposition des ayants droit à l'autopsie demandée par la caisse."])

checks = {
    'L434-9': {
        'L1234-1': "L434-9 règle la rente du survivant après nouvelle union, non un licenciement. Les quinze jours du contrat nouveau, leur départ sur notification et les durées anciennes de L1234-1 ne déterminent aucune période de rente ou de rachat.",
        'L1221-2': "La nouvelle union du rentier ne se confond pas avec la fin d'une mission ou formation. Le contrat unique prospectif et les contrats antérieurs restent sans incidence sur ce droit dérivé d'un décès professionnel ; aucun CDD n'est requis ou rétabli.",
        'L1234-9': "Le capital de trois années de rente et son imputation ne sont pas l'indemnité ordinaire patronale. Ni l'année au terme effectif préavis inclus, ni 0,20 mois par année totale, ni le plafond de six mois ne s'appliquent à la prestation de survivant.",
        'L413-12': "Le 2° vise les pensions des régimes réservés par L413-12 : marine, marins, manufactures d'armes et fonctionnaires. Le corps et la note QPC de 2011 ont été lus ; ces régimes, notamment publics, ne sont pas convertis en contrat privé soumis au préavis de quinze jours.",
        'L434-10': "Le deuxième alinéa maintient la rente du survivant tant qu'un enfant de la victime perçoit une rente d'orphelin. Filiation, âge et relèvements de L434-10 restent préservés. La cible fournie est la source officielle, distincte de notre correction du renvoi institutionnel.",
    },
    'L434-10': {
        'L1234-1': "La limite d'âge de la rente d'orphelin, notamment en apprentissage, n'est pas un préavis. Quinze jours pour les contrats nouveaux et durées anciennes ne réduisent pas la prestation ; aucune notification de rupture n'est requise pour la percevoir.",
        'L1221-2': "L'apprentissage ouvrant éventuellement relèvement d'âge reste une phase pédagogique dans un emploi indéterminé. L1221-2 proposé interdit le terme automatique de l'emploi ; l'avantage n'est pas réservé aux anciens CDD et aucun CDD spécial n'est rétabli.",
        'L1234-9': "La rente n'est pas l'indemnité ordinaire de licenciement. Ni les huit mois de la source de L1234-9 ni l'année au terme effectif avec préavis de sa proposition ne conditionnent le droit de l'enfant ; 0,20 mois et plafond de six mois sont inapplicables.",
    },
    'L434-11': {
        'L1234-1': "Désigner père, mère, tuteur ou gardien comme destinataire du paiement ne constitue pas une notification de licenciement. Aucun préavis de quinze jours ou durée ancienne de L1234-1 n'est appliqué à la remise de la rente.",
        'L1221-2': "Le renvoi à L434-10 reste cohérent si l'enfant est apprenti en contrat unique indéterminé. L434-11 fixe le destinataire du versement, sans durée de formation ni terme de l'emploi et sans réserver l'avantage aux contrats antérieurs.",
        'L1234-9': "Le représentant recevant la rente n'a pas à justifier d'une ancienneté de licenciement. Année à la fin effective préavis inclus, calcul de 0,20 mois et plafond de six mois ne concernent ni la rente de l'enfant ni sa remise au représentant.",
        'L434-10': "Le renvoi couvre toutes les rentes des enfants et assimilés de L434-10 sans modifier filiation, limites d'âge ou avantages. La correction institutionnelle proposée dans ce lot laisse intacte la désignation du destinataire de L434-11.",
    },
    'L434-12': {
        'L1234-1': "La décision judiciaire sur la perception par le délégué n'est pas une rupture de contrat. Préavis individuel, départ sur notification et anciennes durées ne remplacent pas la mesure judiciaire et ne conditionnent pas le droit de l'enfant.",
        'L1221-2': "La gestion du budget familial relève du juge civil et du financement social. Elle ne crée pas d'emploi à terme ; les enfants futurs éligibles en contrat unique gardent leur rente sans qu'une durée d'emploi soit déduite de la durée de la mesure.",
        'L1234-9': "Les frais judiciaires relèvent de L552-6, non d'une indemnité patronale. Huit mois anciens, année au terme préavis inclus, 0,20 mois par année et plafond de six mois n'ont aucun champ dans cette prise en charge protectrice de l'enfant.",
        'L434-10': "Le délégué peut percevoir la rente d'orphelin pour les besoins familiaux sans en acquérir la propriété ni supprimer majorations ou relèvements d'âge. La mise à jour institutionnelle de L434-10 laisse cette faculté judiciaire entière.",
    },
    'L434-14': {
        'L1234-1': "L434-14 plafonne des rentes d'ayants droit, sans fixer de délai de rupture. Le préavis de quinze jours calendaires des contrats nouveaux, courant après présentation ou réception de la notification, et les préavis des anciens contrats ne déterminent ni quotité ni assiette de ces plafonds.",
        'L1221-2': "Le plafond collectif vise les rentes du survivant, des enfants et des ascendants, indépendamment du contrat privé ancien ou unique. L'apprentissage pouvant justifier le relèvement d'âge de L434-10 reste une phase de formation sans terme automatique de l'emploi nouveau ; l'avantage futur demeure.",
        'L1234-9': "Les fractions du salaire annuel plafonnent des prestations AT-MP, non l'indemnité ordinaire patronale. Ni le seuil d'un an mesuré au terme effectif préavis inclus, ni 0,20 mois par année totale et fractions en mois complets, ni le plafond de six mois ne s'y substituent ; les droits des anciens contrats restent distincts.",
        'L434-10': "Le deuxième plafond comprend les rentes collectives d'enfants et assimilés de L434-10, avec leurs limites et relèvements d'âge, majorations et catégories familiales. Le renvoi explicite à L434-7 à L434-13 conserve ce champ ; la correction institutionnelle de L434-10 ne modifie pas son inclusion dans le plafond.",
    },
    'L434-16': {
        'L1234-1': "Le 1er avril d'indexation et le calcul de l'incapacité ne sont pas un préavis. Les quinze jours sur notification du contrat nouveau et les durées antérieures de L1234-1 ne modifient pas ce minimum de prestation AT-MP.",
        'L1221-2': "Le salaire annuel indemnise l'accident quel que soit le contrat ancien ou nouveau. Le contrat unique n'autorise ni terme automatique de rente ni perte du minimum pendant une phase de formation ou mission à durée limitée.",
        'L1234-9': "La dégressivité de rente n'est pas le barème de rupture. L'année au terme effectif avec préavis et le calcul de 0,20 mois par année totale plafonné à six mois ne remplacent pas les minima et calculs d'indemnisation AT-MP.",
        'L434-2': "Le quatrième alinéa fourni vise accidents successifs, cumul de taux, choix rente/capital et limite salariale, sans ancienneté ou notification de rupture. Ce renvoi reste entier ; seule l'erreur interne de L434-16 est corrigée, sans validation prétendue de la future structure temporelle de L434-2.",
    },
    'L434-20': {
        'L1234-1': "Cesser de résider en France n'est pas une rupture notifiée par l'employeur. Maintien de rente et option de capital ne dépendent ni des quinze jours des nouveaux contrats ni des préavis antérieurs conservés par L1234-1.",
        'L1221-2': "Exporter la rente est un droit social, non un terme d'emploi. Contrat unique et anciens contrats gardent leurs transitions propres ; une mission ou formation achevée ne déclenche pas un rachat de rente et ne rétablit pas un emploi à terme.",
        'L1234-9': "Le capital reste assis sur la rente annuelle avec multiple de R434-35 et plafond des ayants droit. Ce n'est pas l'indemnité patronale ordinaire : année préavis inclus, 0,20 mois par année totale et plafond de six mois ne s'y appliquent pas.",
    },
    'L436-1': {
        'L1234-1': "Le délai réglementaire ouvrant l'astreinte pour retard de prestation n'est pas le préavis individuel. Il ne devient pas quinze jours à partir d'une notification de rupture et ne reçoit pas les durées de préavis des anciens contrats.",
        'L1221-2': "L'astreinte protège le paiement d'accident indépendamment du contrat ancien ou unique. Une formation ou mission limitée n'est pas un terme de l'emploi nouveau et ne termine pas le droit à paiement ou à sanction du retard.",
        'L1234-9': "Indemnités journalières, capital AT-MP et rentes ne sont pas l'indemnité ordinaire de L1234-9. Ni année préavis inclus ni plafond de six mois ne conditionnent l'astreinte ; zéro indemnité ordinaire avant un an n'efface pas ces prestations.",
    },
    'L441-2': {
        'L1234-1': "La déclaration d'accident est distincte de la notification de rupture. Hors double dépôt dispensé, les quarante-huit heures réglementaires demeurent ; ni les quinze jours du préavis nouveau ni les durées anciennes ne s'y substituent.",
        'L1221-2': "La dispense du même accident déjà déclaré vaut quel que soit l'emploi. Les contrats uniques futurs restent couverts sans CDD spécial ; la fin d'une mission ou formation ne termine pas l'emploi et ne dispense pas d'une déclaration nécessaire.",
        'L1234-9': "Déclarer et agir pour la victime pendant deux ans ne dépend d'aucune ancienneté de licenciement. L'année à la fin avec préavis, 0,20 mois et plafond de six mois ne réduisent ni indemnisation d'accident ni sanctions subsistantes.",
        'L471-1': "L471-1 vise L441-2 puis prévoit recouvrement des dépenses et pénalité en cas de manquement. La dispense doit exclure la sanction du second dépôt devenu non dû sans supprimer déclaration nécessaire, sanctions autonomes ou champ de séjour irrégulier et travail dissimulé du troisième alinéa.",
    },
    'L441-4': {
        'L1234-1': "Registre bénin et déclaration d'aggravation relèvent de la prévention, non de la rupture. Les quarante-huit heures de R441-5 restent distinctes des quinze jours sur notification du préavis et des durées anciennes de L1234-1.",
        'L1221-2': "L'accès élargi au registre couvre emplois anciens et contrats uniques futurs. Aucun CDD de mission ou formation n'est rétabli : l'absence d'arrêt ou de soins qualifie l'accident, jamais un terme ou une durée du contrat.",
        'L1234-9': "La prise en charge après aggravation ne dépend ni des huit mois anciens ni de l'année au terme avec préavis. L'indemnité de 0,20 mois et le plafond de six mois ne suppriment pas prestations, registre ou recours AT-MP.",
        'L471-1': "Les renvois à L441-4 restent opérants pour le registre, l'avis au CSE, les accès et la déclaration d'aggravation : alinéas 2 à 4 conservés à leur place. Les prérequis d'accès supprimés ne doivent plus être sanctionnés ; fraude et travail dissimulé gardent leurs règles autonomes.",
    },
    'L441-5': {
        'L1234-1': "La feuille d'accident sert les soins et non la notification de licenciement. Son obligation ne devient pas un préavis de quinze jours, ne dépend pas des préavis anciens et n'est pas supprimée du seul fait de la rupture.",
        'L1221-2': "La feuille reste due pour les contrats uniques futurs comme pour les emplois anciens. Une mission, affectation ou formation limitée ne termine pas automatiquement l'emploi nouveau et ne prive pas la victime de sa feuille et des soins.",
        'L1234-9': "La dispense d'avance de frais ne dépend d'aucun seuil d'ancienneté. Zéro indemnité ordinaire avant un an puis 0,20 mois par année totale préavis inclus n'effacent ni feuille, ni soins, ni réparation d'une illégalité.",
        'L471-1': "Le premier alinéa de L471-1 vise exactement le premier alinéa de L441-5 maintenu à sa place : non-délivrance contrôlable et conséquences existantes non aggravées. Le renvoi ne vise pas le décret d'utilisation et n'est pas une règle de notification ou d'indemnité de rupture.",
    },
}

for source in sources:
    key = source['code_id'] + '|' + source['source_id']
    answer = answers[source['number']]
    answer['reference_checks'] = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        answer['reference_checks'].append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': checks[source['number']][target['number']],
        })

ordered = [answers[a['number']] for a in sources]
(ROOT / 'answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(f'Wrote {len(ordered)} articles to answer.json')
