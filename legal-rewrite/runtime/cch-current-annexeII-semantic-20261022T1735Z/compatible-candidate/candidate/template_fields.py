"""Exact inherited model fields, source-bound; not a completion certificate."""
import hashlib, json, re
from pathlib import Path
from html.parser import HTMLParser
BAD=re.compile(r'\[\s*(?:\.\.\.|…|à compléter|texte inchangé)\s*\]|<placeholder>|TODO',re.I)
class Text(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.words=[]
    def handle_data(self,data):self.words.append(data)
    def result(self):return ' '.join(' '.join(self.words).split())
def normalized(body):
    p=Text();p.feed(body);return p.result()
def sha(body):return hashlib.sha256(body.encode()).hexdigest()
def validate_placeholders(source, proposed):
    if not proposed:
        return None  # Missing drafts/retained slots remain the callers’ responsibility.
    registry=CERTIFIED_FIELDS
    text=normalized(proposed)
    key=source['code_id']+'|'+source['source_id']
    certified=registry.get(key)
    if certified:
        if (source['source_sha256']!=certified['source_sha256'] or
            sha(source['source_xml'])!=certified['source_xml_sha256'] or
            sha(source.get('source_notes_xml',''))!=certified['notes_sha256']):
            raise ValueError('Certified source changed')
        # Exact, reviewed alternative representation of five statutory parameters.
        # This creates a validation-only view, never edits stored or returned XML.
        if key == PARAMETER_VARIANT_KEY and any(new in text for old, new in PARAMETER_VARIANTS):
            for old, new in PARAMETER_VARIANTS:
                if text.count(new) != 1 or old in text:
                    raise ValueError('Incomplete or duplicated approved parameter variant')
                text = text.replace(new, old, 1)
            for start, proof in VARIANT_PROTECTED_SECTIONS.items():
                end = proof['end']
                if text.count(start) != 1 or text.count(end) != 1:
                    raise ValueError('Variant protective clause boundary changed')
                lo, hi = text.index(start), text.index(end)
                if hi <= lo or sha(text[lo:hi].strip()) != proof['sha256']:
                    raise ValueError('Variant protective clause changed or parameter moved')
        original=normalized(source['source_xml'])
        headings=lambda xml: re.findall(r"^(?:<p>)?(\d+(?:\.\d+)?[AB]?\. [^<\n]+)",xml,re.M)
        if headings(source['source_xml']) != headings(proposed):
            raise ValueError('Template clause sequence changed')
        for anchor in certified['other_blank_anchors']:
            if original.count(anchor)!=1 or text.count(anchor)!=1:
                raise ValueError('Authentic template blank removed or filled')
        start,end=certified['start'],certified['end']
        if original.count(start)!=1 or original.count(end)!=1 or text.count(start)!=1 or text.count(end)!=1:
            raise ValueError('Missing or duplicated clause boundaries')
        lo,hi=text.index(start),text.index(end)
        block=text[lo:hi]
        if sha(block)!=certified['block_sha256'] or block!=original[original.index(start):original.index(end)]:
            raise ValueError('Capital clause changed, truncated, or filled')
        matches=list(BAD.finditer(block))
        if [(m.start(),m.group()) for m in matches]!=[tuple(x) for x in certified['slots']]:
            raise ValueError('Field inventory mismatch')
        # Only certified character intervals are ignored by this lexical test.
        # No alteration to the actual article, no mass substitution of ellipses.
        chars=list(text)
        for m in matches:chars[lo+m.start():lo+m.end()]=' '*len(m.group())
        text=''.join(chars)
    if BAD.search(text):raise ValueError('Incomplete placeholder outside certified source fields')
    return None

CERTIFIED_FIELDS = {'LEGITEXT000006074096|LEGIARTI000045646952': {'source_sha256': '93ea5cc8b7ffa2e3bb4d43074b68d9143cca81b9f2c9d95e8b4b620dc9f062c9', 'source_xml_sha256': 'f6a8639ea7a78ab3498e608c0d4277c28eb947ea58689dc8ff71b800fe737e39', 'notes_sha256': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'start': '5. Capital social', 'end': '6. Modification du capital social', 'block_sha256': '230dde45c432ad35c8a433cc24108849f9e3dcda2ec84a3de0f7976e900aac49', 'slots': [[52, '[…]'], [80, '[…]'], [129, '[…]']], 'other_blank_anchors': ['La dénomination de la société est :, société de coordination.', 'Le siège social est fixé à :.']}, 'LEGITEXT000006074096|LEGIARTI000045646995': {'source_sha256': 'df94d382652ef832dbfe2dbe13917de18fec2551b14ba9ef4367de6fcc5d9242', 'source_xml_sha256': '0c488525d03efd7c346696d670aeb9a8fad146281bb6d48a1f37ffb9b4f0a58b', 'notes_sha256': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'start': '5. Capital social', 'end': '6. Variabilité du capital', 'block_sha256': '97eeaa09e3b8642c304a5f82f5a43ba1aaad3caf4d7da5aca3124d8dd1291a8c', 'slots': [[161, '[…]'], [825, '[…]']], 'other_blank_anchors': ['La dénomination de la société est :, société coopérative de coordination à capital variable.', 'Le siège social est fixé à :.', "à l'issue de la période de préavis de mois"]}}

PARAMETER_VARIANT_KEY = 'LEGITEXT000006074096|LEGIARTI000045646995'
PARAMETER_VARIANTS = [('La dénomination de la société est :, société coopérative de coordination à capital variable.', 'La dénomination choisie par les associés et inscrite dans les statuts comprend les mots « société de coordination » et indique sa forme coopérative à capital variable.'), ('Le siège social est fixé à :.', "Le siège social est fixé à l'adresse inscrite dans les statuts."), ('Le capital statutaire est fixé à la somme de […] euros.', 'Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.'), ('La valeur nominale des parts sociales est de […] euros.', 'La valeur nominale des parts sociales, exprimée en euros, est fixée dans les statuts.'), ("à l'issue de la période de préavis de mois", "à l'issue de la période de préavis, dont la durée en mois est fixée dans les statuts,")]
VARIANT_PROTECTED_SECTIONS = {'1. Forme': {'end': '2. Dénomination', 'sha256': 'a51cdc872fc4724707bfdd4d6adf5236ed72c1f1612d340bf0edf142ceab40fc'}, '2. Dénomination': {'end': '3. Compétence territoriale-Siège social', 'sha256': '00ecb9969c34206c7b0afd67b56024ffee22b5b514b5da87f2b0ae7f61eb2787'}, '3. Compétence territoriale-Siège social': {'end': '4. Objet social', 'sha256': '9612acd7f90e7781f201de1f63968004f7ecdc7b72474a1ddfcdc103cb7431c9'}, '5. Capital social': {'end': '6. Variabilité du capital', 'sha256': 'ac5b230927ec212655fd8dd5c8d771347296fc4c885d1ab01df54e5bb111c0e7'}, '6. Variabilité du capital': {'end': "6.1. Retrait d'associés", 'sha256': '810d90e42531237e00fe3942456daceb3a4cac58ffb4533e86c80c421c315299'}, "6.1. Retrait d'associés": {'end': "6.2. Exclusion d'associés", 'sha256': '61b3e16dc9d461cf4db317fa01c8902336471577a0183872a0638c09cb15fead'}, "6.2. Exclusion d'associés": {'end': "6.3. Conséquences du retrait ou de l'exclusion", 'sha256': 'ad199ef8f7d4c40193ea50a16b6f2a04521c0d39226db2a70dbc1b0e3a476792'}, "6.3. Conséquences du retrait ou de l'exclusion": {'end': '7. Cessions de parts sociales', 'sha256': '7808a7e4781687300e26c53d4e668bc9e07a434bb28852140a929bcede71e983'}, '7. Cessions de parts sociales': {'end': "8A. Conseil d'administration (3)", 'sha256': 'a1ce2d362178a001bc48ef08570791e6551bf21eb8abc2ee50ee39e62bebf600'}, "8A. Conseil d'administration (3)": {'end': '8B. Conseil de surveillance et directoire (3)', 'sha256': 'dd396a8b2e0cd9a5e820eaeaf441be102179206e921989aac73e1d9a60598013'}, '8B. Conseil de surveillance et directoire (3)': {'end': '9. Assemblées générales', 'sha256': 'ced150175d121c8f0b76007b599914f81922b61c7fcf33efd67bcb2131a213df'}, '9. Assemblées générales': {'end': '10. Année sociale', 'sha256': 'b0faea2b3c2985ac59cd5b798161c2948579844fcd303a1f25c22b2fe5194020'}, '10. Année sociale': {'end': "11. Résultat de l'exercice (4)", 'sha256': '1ba9f4a1eb621978ecb52f01ffa557af97d0b8a9e170fcc034098cba32b2ef1a'}, "11. Résultat de l'exercice (4)": {'end': '12. Réserves', 'sha256': '6317a6a41fbc51b0b54a6b1a3c3f35def9e36956c8e48310d796b786e09fa4af'}, '12. Réserves': {'end': "13. Attribution de l'actif", 'sha256': '5a7621e81383e4254873464fca03287133e52e4f306ad4c12a00485fd8533fa8'}, "13. Attribution de l'actif": {'end': '14. Transmission des statuts', 'sha256': 'c8249412291dd65fccec5bf580a635a4af49b00549230839910588f754a0f243'}, '15. Révision coopérative': {'end': 'Dispositions transitoires.', 'sha256': '2d67d11e685f4be625aae4d18d7bb54f436d8a1e899c26e6f72b791d2b5434a4'}}
