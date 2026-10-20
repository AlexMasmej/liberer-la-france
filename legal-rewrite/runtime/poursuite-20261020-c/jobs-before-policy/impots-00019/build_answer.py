import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / "source.json").read_text())

drafts = {
    "150-0 B": {
        "fragments": ["150-0-B.xml"],
        "reason": "Réécriture à droit constant des trois alinéas : présentation directe des opérations qui échappent à l'article 150-0 A l'année de l'échange, séparation des deux critères territoriaux et formulation explicite de l'imposition de la soulte. La réserve de l'article 150-0 B ter et l'exclusion propre aux apports dans le critère du dépositaire sont maintenues. Aucune réforme de fond de policy.json ne vise ce sursis ; l'orientation relative à l'investissement ne crée pas une exonération générale des bénéfices ou des plus-values réinvestis.",
        "review_notes": "Trois alinéas conservés, sans déplacement. Contrôles : liste complète des opérations, conformité à la réglementation, société soumise à l'IS, critère du lieu de l'opération et critère distinct du lieu d'établissement du dépositaire ; ce second critère exclut les apports à une société soumise à l'IS. Soulte limitée à 10 % de la valeur nominale et taxation à concurrence de son montant l'année de l'échange. Les renvois aux articles 150-0 A et 150-0 B ter sont maintenus. Aucun taux d'IS, régime territorial ou mécanisme de retraite nouveau n'est introduit dans cet article.",
    },
    "150-0 B bis": {
        "fragments": ["150-0-B-bis.xml"],
        "reason": "Réécriture à droit constant : le texte identifie expressément l'imposition du gain comme objet du report, distingue les événements portant sur les titres du transfert antérieur du domicile fiscal, puis explicite les trois conditions cumulatives. L'option expresse, l'antériorité de l'apport par rapport à l'exigibilité en numéraire et les obligations déclaratives sont conservées. Aucune réforme de fond de policy.json ne vise ce régime de créance de complément de prix.",
        "review_notes": "Cinq alinéas et lettres a à c conservés. Contrôles : renvoi au deuxième alinéa du 2 du I de l'article 150-0 A ; transmission, rachat, remboursement et annulation ; article 167 bis si le transfert intervient avant ; exercice continu pendant cinq ans ; soulte de 10 % au plus et taxation de cette soulte l'année de l'échange ; deux déclarations et leurs délais. Le renvoi aux fonctions du 1° du 1 du III de l'article 975 a été vérifié dans le corpus public. La note source relative à l'article 31 de la loi n° 2017-1837 du 30 décembre 2017 est conservée comme donnée historique : IFI à compter du 1er janvier 2018, rédaction au 31 décembre 2017 pour l'ISF dû jusqu'en 2017 inclus. Elle ne fixe aucune entrée en vigueur de réforme future et n'est pas transformée en disposition nouvelle.",
    },
    "150-0 B ter": {
        "fragments": ["150-0-B-ter-I.xml", "150-0-B-ter-II-VI.xml"],
        "reason": "Réécriture à droit constant de l'intégralité des I à VI, y compris le V bis : phrases divisées pour distinguer l'apport, les événements mettant fin au report, les emplois du réinvestissement, les obligations des fonds et les conséquences des manquements. Les dispositions sur les donations, le contrôle, les apports ou échanges successifs et les reports historiques sont conservées. Les 44 alinéas restent dans le même ordre ; la deuxième phrase du 2° du I et la quatrième phrase du d gardent leur objet pour préserver leurs renvois. Aucune réforme de fond de policy.json n'est applicable à ce report ; aucune exonération générale du réinvestissement n'est créée.",
        "review_notes": "Contrôles effectués sur les 44 alinéas : soulte de 10 % ; délai de cession de trois ans depuis l'apport et délai de réinvestissement de trois ans depuis la cession ; réinvestissement minimal de 70 % ; engagements, appels et versements sur cinq ans ; quota de 75 %, seuil de plus d'un quart du capital et des droits de vote, deux limites distinctes de 10 % ; conservation de cinq ans ; compléments de prix et reliquats ; délais du donataire de six et onze ans ; présomption de contrôle de 33,33 %. Exceptions personnelles et familiales, points de départ des intérêts et renvois historiques antérieurs aux 1er janvier 2000, 2006 et 2014 maintenus. La note source réserve la rédaction issue du I de l'article 11 de la loi n° 2026-103 du 19 février 2026 aux cessions de titres apportés réalisées à compter du lendemain de sa publication : cette transition doit rester attachée à la réécriture, sans extension aux cessions antérieures. Points préexistants signalés sans correction de fond : après les trois tirets du d, le renvoi au délai de trois ans du premier alinéa du 2° ne distingue pas les deux points de départ que cet alinéa contient ; au c du 2°, l'articulation entre les activités et le renvoi au c du 3° du II de l'article 150-0 D ter reste à contrôler, ce dernier visant l'IS et le siège de direction effective ; au V, le calcul proportionnel aux titres cédés, rachetés, remboursés ou annulés est aussi rattaché par renvoi au transfert de domicile, sans précision propre à ce cas. Au V, la formule fautive « et au aux » est remplacée par « ou aux » pour énumérer les deux séries d’événements sans exiger leur cumul ; cette clarification est rédactionnelle. Les renvois de phrase et l'avant-dernier alinéa du 2° du I n'ont pas été déplacés.",
    },
    "150-0 B quater": {
        "fragments": ["150-0-B-quater.xml"],
        "reason": "Réécriture à droit constant : distinction des conditions de classement monétaire, de versement et de déclaration ; formulation directe des conséquences d'un manquement, d'un retrait et d'un transfert de domicile. Les règles du versement partiel et les cas d'exonération sont intégralement maintenus. Aucune réforme de fond de policy.json n'est appliquée à ce dispositif historique de versement sur un PEA destiné aux PME et ETI.",
        "review_notes": "Onze alinéas conservés avec les I à VI et les A à C du II. Champ limité aux opérations intervenant entre le 1er avril 2016 et le 31 mars 2017 ; aucune réouverture pour les opérations nouvelles. Versement dans le mois, après prélèvements sociaux, report limité à la quote-part correspondante en cas de versement partiel, délai de cinq ans et transfert de domicile antérieur maintenus. Les exceptions de licenciement, d'invalidité de deuxième ou troisième catégorie et de décès, ainsi que le champ du contribuable et de l'imposition commune, sont conservés. Renvois aux articles L. 214-23, L. 214-24-62 et L. 221-32-1 du code monétaire et financier, 170, 1727 et 167 bis du CGI et L. 341-4 du CSS inchangés. L'exonération définitive propre à ce dispositif n'est pas étendue à l'épargne retraite proposée par la réforme.",
    },
    "150-0 B quinquies": {
        "fragments": ["150-0-B-quinquies.xml"],
        "reason": "Réécriture à droit constant des règles du compte : séparation du calcul du solde, de son plafonnement au retrait, des abattements et de l'imputation des pertes ; distinction des retraits de liquidités, des retraits de titres, de la clôture et du transfert fiscal hors de France. Les règles de datation des rédactions applicables et les exceptions sont préservées. Aucune réforme de fond de policy.json ne vise ce compte, qui n'est pas assimilé au futur compte de retraite collectif individualisé.",
        "review_notes": "Seize alinéas conservés ; le renvoi au cinquième alinéa du I reste sur le gain positif imposé. Vérification des distributions des 7 et 7 bis du II de l'article 150-0 A et du 1 du II de l'article 163 quinquies C, des exclusions du deuxième alinéa et de tous les abattements ; montants bruts et rédaction à la date de perception ou de réalisation maintenus. Pertes imputables dans le compte sans limite de délai, d'abord sur les plus-values antérieures les plus anciennes, puis sur celles de l'année et des années suivantes afférentes aux souscriptions les plus anciennes ; après clôture, imputation jusqu'à la dixième année incluse. Retrait des titres à leur valeur de souscription et exception des titres apportés selon l'article L. 221-32-5 du code monétaire et financier conservés. En cas de transfert fiscal, distinction des plus-values réalisées et latentes, du sursis de paiement et de ses causes d'expiration ; références à l'article 235 ter, à l'article L. 136-6 du CSS et à l'article 15 de l'ordonnance n° 96-50 du 24 janvier 1996 conservées. La baisse de CSG salariale privée ne s'applique pas à ces revenus du capital.",
    },
    "150-0 C": {
        "fragments": ["150-0-C.xml"],
        "reason": "Réécriture à droit constant du régime historique : séparation des événements de sortie du report et de la condition de réinvestissement, formulation explicite des obligations du cédant et de la société, clarification des exclusions dans le calcul de la détention du capital et des reports successifs. Les I et II, les numéros 1 à 7, les lettres a à h et leurs alinéas sont conservés, y compris le 7 abrogé. Aucune réforme de fond de policy.json n'est appliquée : le texte ne rouvre pas ce dispositif et ne crée pas d'exonération générale des sommes réinvesties.",
        "review_notes": "La note source sur l'article 29, XVI, de la loi n° 2005-1720 du 30 décembre 2005 est déterminante : l'article est abrogé pour les cessions à compter du 1er janvier 2006 et demeure applicable aux plus-values en report à cette date. La proposition est à lire dans ce seul champ historique, y compris pour les mécanismes de maintien ou de renouvellement ; elle ne vaut pas rétablissement du régime. Contrôles : investissement avant le 31 décembre de l'année suivant la cession, seuil strictement supérieur à 5 %, trois années d'activité, société créée depuis moins de quinze ans, libération intégrale, détention continue de 75 % au moins avec exclusions, pleine propriété directe, plafond familial de 25 % pendant cinq ans, interdictions du h, non-cumul avec l'article 199 terdecies-0 A, intérêts de retard et échanges à compter du 1er janvier 2000. Les événements de sortie restent différents selon les 1 et 6 du I et le II : le remboursement n'est pas ajouté aux 1 et II. Points historiques à contrôler, conservés sans substitution : l'article 97 porte aujourd'hui sur la déclaration contrôlée des bénéfices non commerciaux ; l'article 39 quinquies H n'est pas présent dans le corpus courant fourni et sa rédaction historique doit être retrouvée pour le d. Le renvoi aux fonctions du 1° du 1 du III de l'article 975 a été vérifié ; la coquille « 1° de du 1 » du a est corrigée. La note source de la loi n° 2017-1837 du 30 décembre 2017 distingue l'IFI à compter du 1er janvier 2018 de l'ISF dû jusqu'en 2017 inclus, soumis à la rédaction au 31 décembre 2017 ; aucune de ces dates n'est utilisée comme entrée en vigueur d'une réforme future.",
    },
}

answer = []
for source in sources:
    draft = drafts[source["number"]]
    proposed = "".join(
        (ROOT / "fragments" / name).read_text() for name in draft["fragments"]
    ).strip()
    answer.append(
        {
            **{key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")},
            "proposed_xml": proposed,
            "reason": draft["reason"],
            "review_notes": draft["review_notes"],
            "status": "rewrite_draft",
        }
    )

(ROOT / "answer.json").write_text(
    json.dumps(answer, ensure_ascii=False, indent=2) + "\n"
)
