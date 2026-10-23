from pathlib import Path
import json,shutil,hashlib,re
P=Path.cwd();O=P/'runtime/cch-current-annexeII-semantic-20261022T1735Z';D=O/'compatible-candidate';D.mkdir(exist_ok=True);old=P/'runtime/cch-template-diagnostic-20261022T100424Z/integration';C=D/'candidate';C.mkdir(exist_ok=True)
for x in (old/'candidate').iterdir():
 if x.is_file():shutil.copy2(x,C/x.name)
shutil.copytree(old.parent/'evidence',D/'evidence',dirs_exist_ok=True)
shutil.copytree(old/'candidate/runtime',C/'runtime',dirs_exist_ok=True)
t=(old/'test_real_gates.py').read_text().replace("EVIDENCE=ROOT.parent/'evidence'","EVIDENCE=ROOT/'evidence'");(D/'test_real_gates.py').write_text(t)
optimizer=P/'runtime/registration-convoy-20261022T1607Z/staging/register_batches_candidate.py';base=optimizer.read_text();candidate=(C/'register_batches.py').read_text();a="            if re.search(r'\\[\\s*(?:\\.\\.\\.|…|à compléter|texte inchangé)\\s*\\]|<placeholder>|TODO',proposed,re.I):raise ValueError('Placeholder in article '+str(key))";b="            validate_placeholders({'code_id':key[0], 'source_id':key[1], 'source_sha256':sha, 'source_xml':body, 'source_notes_xml':impact_source['source_notes_xml']}, row['proposed_xml'] or '')";assert base.count(a)==1;base=base.replace(a,b).replace('from pathlib import Path','from template_fields import validate_placeholders\nfrom pathlib import Path',1);(C/'register_batches.py').write_text(base)
s=(O/'source.txt').read_text().splitlines();p=(O/'proposed.txt').read_text().splitlines();pairs=[]
pairs=[('La dénomination de la société est :, société coopérative de coordination à capital variable.',next(x for x in p if x.startswith('La dénomination choisie'))),('Le siège social est fixé à :.',next(x for x in p if x.startswith('Le siège social est fixé à'))),('Le capital statutaire est fixé à la somme de […] euros.','Le montant du capital statutaire, exprimé en euros, est fixé dans les statuts.'),('La valeur nominale des parts sociales est de […] euros.','La valeur nominale des parts sociales, exprimée en euros, est fixée dans les statuts.'),("à l'issue de la période de préavis de mois","à l'issue de la période de préavis, dont la durée en mois est fixée dans les statuts,")]
import importlib.util
spec=importlib.util.spec_from_file_location('tf',C/'template_fields.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
source=(O/'source.xml').read_text();proposal=(O/'proposed.xml').read_text();virtual=mod.normalized(proposal)
for a,b in pairs:assert virtual.count(b)==1;virtual=virtual.replace(b,a)
heads=re.findall(r'^(?:<p>)?(\d+(?:\.\d+)?[AB]?\. [^<\n]+)',source,re.M)
protected={}
for i,h in enumerate(heads):
 if h.startswith(('4. ','14. ','15. ')):continue
 end=heads[i+1];block=virtual[virtual.index(h):virtual.index(end)].strip();protected[h]={'end':end,'sha256':mod.sha(block)}
# Clause 15 and all embedded notes are protected separately from appended transitions.
start='15. Révision coopérative';end='Dispositions transitoires.';protected[start]={'end':end,'sha256':mod.sha(virtual[virtual.index(start):virtual.index(end)].strip())}
helper=(C/'template_fields.py').read_text();needle="        original=normalized(source['source_xml'])";insert='''        # Exact, reviewed alternative representation of five statutory parameters.
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
''';assert helper.count(needle)==1;helper=helper.replace(needle,insert+needle);helper+='\nPARAMETER_VARIANT_KEY = '+repr('LEGITEXT000006074096|LEGIARTI000045646995')+'\nPARAMETER_VARIANTS = '+repr(pairs)+'\nVARIANT_PROTECTED_SECTIONS = '+repr(protected)+'\n';(C/'template_fields.py').write_text(helper)
(D/'manifest.json').write_text(json.dumps({'status':'offline_candidate_not_activation_ready','optimizer_base_sha256':hashlib.sha256(optimizer.read_bytes()).hexdigest(),'five_substitutions':pairs,'protected_sections':protected,'source_notes_hashes':'Unchanged original CERTIFIED_FIELDS constants','no_active_changes':True},ensure_ascii=False,indent=2))
print(D)
