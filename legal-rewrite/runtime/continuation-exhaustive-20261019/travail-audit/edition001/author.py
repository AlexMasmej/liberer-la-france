"""Four whole-article corrective proposals. No registration or canonical writes."""
from pathlib import Path
import json

P=Path(__file__).resolve().parent
sources=json.loads((P/'source.json').read_text())
by={r['number']:r for r in sources}
answers=[]

def add(number,body,reason,notes,benefit,**metadata):
    source=by[number]
    row={k:source[k] for k in ['code_id','source_id','source_sha256','number']}
    row.update(status='rewrite_draft',proposed_xml=body,reason=reason,review_notes=notes,
               benefit_review=benefit,**metadata)
    answers.append(row)

add('R1221-41',
    '<p>Le salarié qui n’a pas reçu les informations mentionnées aux articles R. 1221-34 et R. 1221-36 dans les délais prévus, respectivement, au deuxième alinéa de l’article R. 1221-35 et au deuxième alinéa de l’article R. 1221-37 peut saisir directement la juridiction prud’homale pour en obtenir la communication ou le complément, conformément à l’article L. 1221-5-1, tant que les informations requises ne lui ont pas été intégralement communiquées.</p>'
    '<p>Aucune mise en demeure préalable de l’employeur ni aucun délai d’attente lié à une telle mise en demeure ne conditionne cette saisine. Une demande amiable demeure possible sans constituer une condition de recevabilité de l’action.</p>'
    '<p>Ces règles s’appliquent aux actions introduites à compter de l’entrée en vigueur de la loi portant la présente réforme ainsi qu’aux instances en cours à cette date, y compris lorsque l’information était due antérieurement. Les décisions devenues définitives ne sont pas remises en cause. L’obligation d’information et les relations de travail auxquelles elle s’applique restent soumises à leurs conditions propres d’application, notamment à l’entrée en vigueur au 1er novembre 2023 des dispositions issues du décret n° 2023-1004 du 30 octobre 2023 ; aucun nouveau délai de remise de l’information ne commence du seul fait de la présente réforme.</p>',
    'Supprime le préalable de mise en demeure que la proposition réglementaire conservait encore à tort après la suppression de ce même préalable par L1221-5-1. Conserve le champ des informations et leurs échéances ; aligne la transition procédurale sur la proposition législative, y compris pour les instances en cours.',
    'L1221-5-1, R1221-34 à R1221-37 et R1221-39 ont été lus intégralement avec leurs notes. Les deuxièmes alinéas de R1221-35 et R1221-37 portent toujours les délais : septième jour/un mois et information avant départ. Le délai de sept jours après mise en demeure est supprimé, sans modifier le délai de sept jours de remise après embauche. La note du décret2023-1004 réserve son entrée en vigueur au1novembre2023. Aucun report de cette obligation ni réouverture des décisions définitives. Proposition corrective seulement, aux empreintes capturées.',
    'La saisine directe bénéficie au salarié sans lui retirer la faculté de demander amiablement les informations. Les dispenses légales et la remise sans doublon des écrits déjà exacts restent régies par L1221-5-1 et R1221-35/37/39 ; leurs bénéficiaires futurs ne perdent aucun avantage.',
    change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=['Suppression de la mise en demeure préalable et de tout délai d’attente attaché à celle-ci avant la saisine prud’homale pour obtenir les informations contractuelles manquantes.'])

body=by['L1226-4']['previous_draft']['proposed_xml']
before='le préavis est de quinze jours calendaires à compter de la notification du licenciement et le contrat prend fin à son expiration.'
after='le préavis est de quinze jours calendaires, calculés conformément à l’article L. 1234-3 : le décompte commence le lendemain de la présentation ou, dans les cas où une autre forme de notification est légalement admise, de la réception ou de la remise de la notification au salarié. Le contrat prend fin à l’expiration du quinzième jour, même non travaillé.'
assert body.count(before)==1
add('L1226-4',body.replace(before,after),
    'Coordonne expressément le décompte du préavis d’inaptitude non professionnelle avec L1234-3. La formule « à compter de la notification » pouvait être comprise comme incluant le jour de notification, alors que le régime général commence le lendemain. La reprise du salaire après un mois, la non-exécution et la dérogation à compensation restent inchangées.',
    'Source entière et proposition antérieure relues. Le délai de quinze jours est décompté selon la proposition de L1234-3, sans modifier la forme légalement applicable de notification. La même fin effective sert au seuil d’un an et au montant de L1234-9 ; aucune première année n’est retranchée. Contrats antérieurs : fin à notification et prise en compte du préavis pour le calcul maintenues. Aucune modification du reclassement, de la santé ni des procédures. Ambiguïté de coordination précisée, sans prétendre qu’un contentieux aurait déjà tranché cette rédaction proposée.',
    'La reprise du salaire à l’expiration d’un mois demeure due aux salariés actuels et futurs, y compris en cas d’inaptitude à tout emploi. La dérogation spéciale à l’indemnité compensatrice reste limitée au préavis non exécuté de cette inaptitude ; elle ne supprime ni l’indemnité spéciale éventuellement ouverte, ni les droits plus favorables autonomes.')

body=by['L1226-14']['previous_draft']['proposed_xml']
before='le préavis individuel est de quinze jours calendaires à compter de la notification du licenciement ; il n’est pas exécuté et le contrat prend fin à son expiration.'
after='le préavis individuel est de quinze jours calendaires, calculés conformément à l’article L. 1234-3 à partir du lendemain de la présentation ou, dans les cas où une autre forme de notification est légalement admise, de la réception ou de la remise de la notification au salarié ; il n’est pas exécuté et le contrat prend fin à l’expiration du quinzième jour, même non travaillé.'
assert body.count(before)==1
add('L1226-14',body.replace(before,after),
    'Rend explicite le calcul du préavis d’inaptitude professionnelle selon L1234-3, afin de fixer la même date de fin et d’ancienneté dans les textes coordonnés. Conserve entièrement l’indemnité compensatrice, le minimum spécial double, l’absence de condition minimale d’ancienneté, les exceptions et le régime antérieur.',
    'Le renvoi aux1°à3°deL1226-12 est correct dans sa proposition structurée ; L1226-16 conserve la base spéciale des trois mois reconstitués. Le plafond de six mois sert de base avant doublement et ne réduit pas l’indemnité spéciale à six mois ; les minima conventionnels plus favorables subsistent. Les composantes antérieure et nouvelle sont additionnées sans double compte et seule la composante nouvelle est plafonnée avant doublement. Les quinze jours ne créent pas une seconde indemnité de préavis cumulable pour la même période. Proposition entière inchangée sur ces garanties, avec seul décompte harmonisé.',
    'Les futurs bénéficiaires conservent l’indemnité spéciale sans condition d’ancienneté, son doublement, la compensation de préavis et les garanties conventionnelles plus favorables. Le non-cumul historique des avantages de même nature reste limité à ceux visés au7janvier1981 et le refus abusif de reclassement conserve son exception précise.')

add('R1221-34',
    '<p>Les documents remis en application de l’article L. 1221-5-1 comportent au moins les informations suivantes :</p>'
    '<p>1° L’identité des parties à la relation de travail ;</p>'
    '<p>2° Le ou les lieux de travail et, si elle est distincte, l’adresse de l’employeur ;</p>'
    '<p>3° L’intitulé du poste, les fonctions, la catégorie socioprofessionnelle ou la catégorie d’emploi ;</p>'
    '<p>4° La date d’embauche ;</p>'
    '<p>5° Pour une relation à durée déterminée conclue avant l’entrée en vigueur de la loi instituant le contrat de travail unique, sa date de fin ou sa durée prévue ; pour le contrat unique conclu à compter de cette entrée en vigueur, sa durée indéterminée ;</p>'
    '<p>6° Pour le salarié temporaire mentionné à l’article L. 1251-1, l’identité de l’entreprise utilisatrice, dès qu’elle est connue ;</p>'
    '<p>7° Le cas échéant, la durée et les conditions de la période d’essai. Pour un contrat unique conclu à compter de l’entrée en vigueur de la loi l’instituant, l’information précise l’interdiction de renouveler cette période d’essai ;</p>'
    '<p>8° Le droit à la formation assuré par l’employeur conformément à l’article L. 6321-1 ;</p>'
    '<p>9° La durée du congé payé auquel le salarié a droit ou les modalités de son calcul ;</p>'
    '<p>10° La procédure à observer par l’employeur et le salarié en cas de cessation de leur relation de travail. Pour le contrat unique nouveau, l’information précise le préavis de quinze jours calendaires, son point de départ selon l’article L. 1234-3, son application à l’essai selon les articles L. 1221-25 et L. 1221-26, les dispenses légalement applicables ainsi que la distinction entre l’indemnité ordinaire de rupture et les autres sommes dues ;</p>'
    '<p>11° Les éléments de rémunération mentionnés à l’article L. 3221-3, indiqués séparément, y compris les majorations pour heures supplémentaires, ainsi que la périodicité et les modalités du paiement ;</p>'
    '<p>12° La durée de travail quotidienne, hebdomadaire ou mensuelle ou ses modalités d’aménagement sur une autre période de référence selon les articles L. 3121-41 à L. 3121-47, les conditions d’accomplissement d’heures supplémentaires ou complémentaires et, le cas échéant, les modalités de changement d’équipe en cas de travail en équipes successives alternantes ;</p>'
    '<p>13° Les conventions et accords collectifs applicables au salarié dans l’entreprise ou l’établissement ;</p>'
    '<p>14° Les régimes obligatoires d’affiliation, les contrats de protection sociale complémentaire dont les salariés bénéficient collectivement en application d’un accord collectif ou d’une décision unilatérale de l’employeur et leurs éventuelles conditions d’ancienneté.</p>',
    'Corrige le7°de la proposition intégrée : l’interdiction de renouvellement concerne la période d’essai et non le contrat unique à durée indéterminée. Conserve les quatorze rubriques, restaure le renvoi définissant les éléments de rémunération et précise au10°les points de départ et les dispenses, sans créer de document supplémentaire.',
    'Source complète, note du décret2023-1004 et proposition intégrée lues. Les numéros1°à14°restent stables, notamment pour les renvois de R1221-35. R1221-35 et R1221-37 gardent leurs délais et le réemploi des écrits ; R1221-39 garde les modalités de communication. Le nouveau7°vise seulement le non-renouvellement de l’essai du contrat unique, sans interdire une modification licite de ce contrat ni renouveler un CDD. Le10°n’écarte pas les dispenses favorables, notamment liées à la maternité. Le délai de quinze jours ne remplace aucune procédure collective ou autorisation protégée. Les35heures/1607heures d’aménagement ne sont pas relevées implicitement par le renvoi aux articles L3121-41à47.',
    'Les régimes complémentaires, leurs garanties et les dispenses favorables de préavis restent explicitement applicables aux salariés éligibles futurs. Les écrits déjà complets et exacts continuent à satisfaire aux obligations selon L1221-5-1 et R1221-35/37/39 ; aucune seconde remise ni document supplémentaire ne résulte de ces précisions.')

assert len(answers)==len(sources)==4
(P/'answer.json').write_text(json.dumps(answers,ensure_ascii=False,indent=2)+'\n')
print('Four complete corrective proposals written; none registered.')
