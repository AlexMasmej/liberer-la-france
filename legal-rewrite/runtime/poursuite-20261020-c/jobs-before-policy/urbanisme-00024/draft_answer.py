import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}

def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = dict(proposed_xml=xml.strip(), reason=reason, review_notes=notes, status='rewrite_draft')

add('L314-5', '''
<p>Dans le cas prévu à l'article L. 314-2, les commerçants, artisans et industriels bénéficient d'un droit de priorité pour l'attribution de locaux de même nature compris dans l'opération, à condition que leur activité soit compatible avec les dispositions du plan local d'urbanisme ou du document d'urbanisme en tenant lieu.</p>
<p>Les commerçants, artisans ou industriels qui n'ont pas reçu d'offre de réinstallation dans les conditions prévues au premier alinéa bénéficient d'un droit de priorité pour acquérir un local dans un immeuble compris dans l'opération ou des parts ou actions d'une société immobilière donnant vocation à l'attribution, en propriété ou en jouissance, d'un tel local. Ce droit s'applique à condition que leur activité soit compatible avec les dispositions du plan local d'urbanisme ou du document d'urbanisme en tenant lieu.</p>
<p>L'exercice des droits prévus au présent article entraîne l'application du deuxième alinéa de l'article L. 322-12 du code de l'expropriation pour cause d'utilité publique.</p>
<p>Les priorités prévues au présent article bénéficient aux titulaires de baux portant sur les mêmes activités que celles dont l'installation est prévue dans les nouveaux locaux. Pour les commerces de chaque nature, les titulaires des baux les plus anciens sont prioritaires.</p>
''', "Réécriture à droit constant : les bénéficiaires, les deux droits de priorité et la condition de compatibilité urbanistique sont explicités. Le classement par ancienneté des baux demeure dans le quatrième alinéa. Aucune réforme de fond.", "Quatre alinéas conservés. Renvois à L. 314-2 et au deuxième alinéa de L. 322-12 du code de l'expropriation maintenus ; le cas d'éviction définitive de L. 314-2 a été vérifié dans le corpus public. L'attribution de parts ou actions reste possible en propriété ou en jouissance, sans extension des catégories d'activités prioritaires.")

add('L314-6', '''
<p>À leur demande, les commerçants et artisans sont indemnisés avant l'acte portant transfert de propriété au titre de l'activité qu'ils exercent dans un immeuble destiné à être acquis ou exproprié pour être démoli dans le cadre d'une opération d'aménagement. Par dérogation à l'article L. 322-2 du code de l'expropriation pour cause d'utilité publique, cette indemnisation est fondée sur la situation qui existait avant le commencement de l'opération. Pour le surplus, l'indemnité relève du régime des indemnités d'expropriation.</p>
<p>Pour obtenir cette indemnisation avant le transfert de propriété, l'intéressé doit :</p>
<p>1° Justifier d'un préjudice causé par la réduction progressive des facteurs locaux de commercialité à l'intérieur de l'opération et résultant directement de celle-ci ;</p>
<p>2° Prendre l'engagement de cesser son activité et, s'il est locataire, de quitter les lieux dès le versement de l'indemnité et de ne pas se réinstaller sur le territoire concerné par l'opération avant que les bénéficiaires du droit de priorité prévu à l'article L. 314-5 aient été appelés à exercer ce droit.</p>
<p>Le bail est résilié de plein droit, sans indemnité et malgré toute clause contraire, à compter de la notification au propriétaire du versement de l'indemnité prévue au présent article.</p>
<p>Les dispositions de l'article L. 231-1 du code de l'expropriation pour cause d'utilité publique s'appliquent à l'expiration du délai d'un mois prévu par cet article.</p>
<p>Lorsqu'un ou plusieurs commerçants ou artisans indemnisés avant le transfert de propriété ont libéré les lieux, les immeubles ou parties d'immeubles ainsi libérés sont évalués en tenant compte de la situation d'occupation qui existait avant leur indemnisation.</p>
''', "Réécriture à droit constant : la longue phrase relative au paiement anticipé est divisée ; les conditions préalables et les effets sur le bail sont formulés directement. La date d'évaluation dérogatoire et l'articulation des engagements du 2° sont conservées. Aucune réforme de fond.", "Sept alinéas et subdivisions 1° et 2° maintenus. Contrôle du délai d'un mois, des renvois à L. 322-2 et L. 231-1 du code de l'expropriation et à L. 314-5. La construction du 2° conserve la réserve « s'il est locataire » : sa portée sur l'engagement de non-réinstallation appelle contrôle et n'est pas tranchée par la réécriture. L'évaluation des immeubles libérés tient toujours compte de l'occupation antérieure à l'indemnisation.")

add('L314-7', '''
<p>Toute offre de relogement, définitif ou provisoire, doit être notifiée au moins six mois à l'avance. L'occupant dispose de deux mois pour faire connaître son acceptation ou son refus. S'il ne répond pas dans ce délai, il est réputé avoir accepté l'offre.</p>
<p>Lorsque les occupants bénéficient du droit à réintégration prévu au quatrième alinéa de l'article L. 314-3, le propriétaire doit, dès l'achèvement des travaux, les mettre en demeure de lui indiquer s'ils entendent exercer ce droit. Il leur adresse cette mise en demeure par lettre recommandée avec demande d'avis de réception ou par acte extrajudiciaire. Les occupants doivent répondre dans le délai d'un mois et dans la même forme. À peine de nullité, la notification doit mentionner la forme et le délai de cette réponse.</p>
''', "Réécriture à droit constant : les délais, l'effet du silence et les formalités de réintégration sont présentés dans des phrases distinctes, sans modifier les deux alinéas de fond. Aucune réforme de fond.", "Délais de six mois, de deux mois et d'un mois conservés ; le quatrième alinéa de L. 314-3 porte bien sur la réintégration dans le corpus. La note source rappelle l'article 4 de l'ordonnance n° 2005-868 du 28 juillet 2005 : pour l'application à Mayotte des articles L. 314-1 et suivants, les occupants non français doivent remplir les conditions d'entrée et de séjour réguliers prévues par l'ordonnance n° 2000-373 du 26 avril 2000 modifiée. Cette règle territoriale demeure signalée comme donnée de la source ; son articulation avec les textes ultérieurs sur Mayotte doit être contrôlée sans lui substituer une règle inventée.")

add('L314-8', '''
<p>Lorsque des dispositions législatives ou réglementaires interdisent l'exercice de l'activité prévue au bail dans le local commercial, industriel ou artisanal que son titulaire a le droit de réintégrer après les travaux, celui-ci peut être autorisé par l'autorité judiciaire à changer la nature de son commerce ou de son industrie, si le bail ne le prévoit pas. Cette autorisation reste soumise aux dispositions législatives ou réglementaires qui s'opposeraient à l'exercice de la nouvelle activité choisie dans ce local.</p>
''', "Réécriture à droit constant : la condition d'interdiction de l'activité initiale et la réserve applicable à l'activité nouvelle sont distinguées en deux phrases. L'autorisation reste judiciaire et conditionnée par le contenu du bail. Aucune réforme de fond.", "Un seul alinéa de fond conservé. Ne pas confondre ce changement d'activité avec une autorisation générale de transformation en logement. La note source rappelle l'article 4 de l'ordonnance n° 2005-868 du 28 juillet 2005 : à Mayotte, les occupants non français concernés par L. 314-1 et suivants doivent satisfaire aux conditions d'entrée et de séjour réguliers de l'ordonnance n° 2000-373 du 26 avril 2000 modifiée. Cette indication territoriale est conservée ici ; son articulation avec les textes ultérieurs sur Mayotte appelle un contrôle distinct.")

add('L314-9', '''
<p>Les conditions d'application du présent chapitre sont précisées, en tant que de besoin, par un décret en Conseil d'État.</p>
''', "Réécriture à droit constant : l'objet du décret est placé en tête de phrase, sans changer son niveau ni la réserve de nécessité. Aucune réforme de fond.", "Maintien du renvoi réglementaire à un décret en Conseil d'État et du périmètre limité au présent chapitre ; aucune compétence nouvelle ni date d'application ajoutée.")

add('L315-1', '''
<p>Dans les secteurs urbains exclusivement ou majoritairement composés d'habitat individuel ou dans les zones d'activité économique au sens de l'article L. 318-8-1, les opérations de transformation urbaine ont pour objet de favoriser l'évolution ou la requalification du bâti existant et d'optimiser l'utilisation de l'espace. Elles visent à réaliser les orientations d'aménagement et de programmation prévues en application de l'article L. 151-7-3.</p>
<p>Le conseil municipal ou l'organe délibérant de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme ou de document en tenant lieu définit l'opération de transformation urbaine par délibération. Cette délibération fixe les objectifs, la durée et le périmètre de l'opération. Elle comprend notamment un programme prévisionnel des actions à réaliser, une estimation du coût de l'opération et les conditions de financement envisagées, y compris, le cas échéant, pour les besoins en équipements publics.</p>
<p>Le conseil municipal ou l'organe délibérant de l'établissement public de coopération intercommunale peut, par délibération, désigner un opérateur ayant vocation à réaliser tout ou partie des actions à conduire pour le compte de la commune ou de l'établissement public et lui confier ces actions. Leur mise en œuvre peut faire l'objet d'une convention avec cet opérateur.</p>
<p>L'opération donne lieu à une concertation dans les conditions prévues aux articles L. 103-2 à L. 103-6.</p>
''', "Réécriture à droit constant : le champ territorial, l'autorité qui définit l'opération et celle qui désigne l'opérateur sont explicités. Les objectifs, le financement prévisionnel et la concertation sont conservés. Aucune réforme de fond : cet outil existant accompagne la transformation urbaine sans constituer, à lui seul, un droit à construire.", "Quatre alinéas maintenus. Renvois à L. 318-8-1, L. 151-7-3 et L. 103-2 à L. 103-6 conservés. Vérification de L. 151-7-3 dans le corpus : il prend en compte stationnement, transports, réseaux d'eau, d'assainissement et d'énergie, équipements publics et qualité environnementale et d'insertion. Les mesures de densification retenues à L. 151-4 et L. 151-26 ne justifient pas leur suppression ici. Les coûts et financements, y compris des équipements publics, restent prévisionnels ; aucun budget ni financement acquis n'est inventé.")

add('L318-1', '''
<p>Un décret en Conseil d'État peut, après avis de la personne morale de droit public intéressée, décider le déclassement et le transfert de propriété de toute dépendance du domaine public pour faciliter l'exécution des opérations et travaux définis au présent livre et relevant de la compétence de l'État, d'une collectivité locale ou d'un établissement public.</p>
''', "Réécriture à droit constant : le pouvoir de décision, la consultation préalable et la finalité des déclassements et transferts sont regroupés dans une phrase à sujet explicite. Aucune réforme de fond.", "Le recours au décret en Conseil d'État et l'avis préalable sont maintenus ; l'avis n'est pas transformé en accord. Le champ reste celui des opérations et travaux du présent livre relevant des personnes publiques énumérées.")

add('L318-2', '''
<p>À défaut d'accord, les équipements mobiliers ou immobiliers destinés à un service public ou à l'usage public et appartenant à l'État, à des collectivités locales ou à des établissements publics peuvent être transférés à titre gratuit aux collectivités locales et aux établissements publics dans la circonscription desquels ils se trouvent. Ces transferts peuvent intervenir au fur et à mesure de la réalisation des équipements et, au plus tard, à l'issue des opérations et travaux définis au présent livre. Ils sont décidés par décret en Conseil d'État, après une enquête publique réalisée conformément au code de l'expropriation pour cause d'utilité publique et après consultation des assemblées délibérantes intéressées. Ce décret classe, s'il y a lieu, les équipements transférés dans le domaine public de leurs bénéficiaires.</p>
''', "Réécriture à droit constant : la phrase unique est divisée pour distinguer les biens et bénéficiaires, le calendrier, la procédure et le classement domanial. La gratuité et la condition de défaut d'accord sont maintenues. Aucune réforme de fond.", "Un alinéa de fond conservé. Le terme ultime reste l'issue des opérations et travaux, sans rendre obligatoire un transfert facultatif. La note source réserve l'application de ces dispositions aux projets, plans, programmes et autres documents de planification dont l'arrêté d'ouverture et d'organisation de l'enquête publique est publié à compter du premier jour du sixième mois après la publication du décret en Conseil d'État prévu à L. 123-19 du code de l'environnement. Cette transition historique reste à prendre en compte ; aucune date calendaire n'est déduite sans disposer du décret.")

exec(compile(Path('draft_part2.py').read_text(), 'draft_part2.py', 'exec'))

exec(compile(Path('draft_part3.py').read_text(), 'draft_part3.py', 'exec'))

if __name__ == '__main__':
    out = []
    for s in sources:
        if s['number'] not in drafts:
            continue
        a = {k:s[k] for k in ('code_id','source_id','source_sha256','number')}
        a.update(drafts[s['number']])
        out.append(a)
    Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(out)} articles rédigés')
