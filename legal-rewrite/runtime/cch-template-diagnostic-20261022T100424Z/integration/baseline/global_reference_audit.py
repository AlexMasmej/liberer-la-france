"""Read-only, whole-corpus reference inventory; never a legal approval.

The only writes are the requested audit files and an online SQLite backup.
Neither this module nor its CLI imports the mutable registration pipeline.
Text detection is deliberately conservative: unresolved code/number ambiguity is
retained, and exact historical identifiers are never silently redirected.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sqlite3
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET

VERSION = 1
HERE = Path(__file__).resolve().parent
WORK = 'LEGITEXT000006072050'
CGI = 'LEGITEXT000006069577'
ANNEXES = dict(zip(('I', 'II', 'III', 'IV'), (
    'LEGITEXT000006069568', 'LEGITEXT000006069569',
    'LEGITEXT000006069574', 'LEGITEXT000006069576')))
CODE_PATTERNS = (
    (WORK, r'code\s+du\s+travail'),
    (CGI, r'code\s+general\s+des\s+impots|\bCGI\b'),
    ('LEGITEXT000006073189', r'code\s+de\s+la\s+securite\s+sociale|\bCSS\b'),
    ('LEGITEXT000006074075', r"code\s+de\s+l['’]\s*urbanisme(?!\s+et\s+de\s+l['’]\s*habitation)"),
    ('LEGITEXT000006074096', r"code\s+de\s+la\s+construction\s+et\s+de\s+l['’]\s*habitation|\bCCH\b"),
)
LATIN = (r'bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|'
         r'undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|'
         r'septdecies|octodecies|novodecies|vicies|unvicies|duovicies|'
         r'tervicies|quatervicies|quinvicies|sexvicies|septvicies|octovicies|'
         r'nonvicies|tricies|untricies|duotricies|tertricies|quatertricies|'
         r'quintricies|sextricies|septtricies|octotricies|nontricies')
SUFFIX = r'(?:' + LATIN + r'|[A-Z]{1,5}(?![A-Za-z]))'
BARE = r'(?:1er|\d{1,5}(?:\s*-\s*\d{1,5})*(?:[ \t]+(?:' + SUFFIX + r')){0,6})'
PREFIXED = r'(?:LO|[LRDA])\s*[.*]?\s*\d{1,5}(?:\s*-\s*\d{1,5}[A-Za-z]*)*(?:[ \t]+(?:' + SUFFIX + r')){0,4}'
TOKEN = re.compile(r'(?:' + PREFIXED + r'|' + BARE + r')(?![\w-])')
PREFIX_TOKEN = re.compile(r'\b' + PREFIXED + r'(?![\w-])')
ARTICLE_WORD = re.compile(r'\b(?:articles?|art\.)[ \t\n]+', re.I)
SEPARATOR = re.compile(r'\s*(?P<sep>à|a|au|,|et|ou|ainsi\s+que)\s*', re.I)
SUBDIVISION = re.compile(r'\b(?:alin[ée]a\w*|[0-9]+\s*°|[IVX]+\s*(?:bis|ter)?\s*(?:du|de)|[a-z]\))', re.I)
HISTORICAL = re.compile(r'\b(?:ancien(?:ne|s|nes)?|r[ée]daction|version|abrog[ée]\w*|ant[ée]rieur\w*)\b|en vigueur avant', re.I)


def digest(value):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return hashlib.sha256(value or b'').hexdigest()


def file_digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def plain(value):
    return html.unescape(re.sub(r'<[^>]*>', ' ', value or ''))


def fold(value):
    return ''.join(c for c in unicodedata.normalize('NFD', value) if unicodedata.category(c) != 'Mn')


def normalize(value):
    result = re.sub(r'[\s.*]', '', value or '').upper()
    return '1' if result == '1ER' else result


def readonly(path):
    db = sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro', uri=True, timeout=2)
    db.execute('PRAGMA query_only=ON')
    return db


def snapshot_database(source, destination, pages=256):
    """Online backup: bounded read locks; no BEGIN/checkpoint or source writes.

    SQLite restarts a backup if writers modify pages between steps; the final
    destination is a coherent committed snapshot, not a copy of DB+WAL files.
    Source stats are observational only, never claimed to be a stable hash.
    """
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if source == destination or destination.exists():
        raise ValueError('Snapshot destination must be a new, different file')
    destination.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    before = {'size': source.stat().st_size, 'mtime_ns': source.stat().st_mtime_ns}
    progress = {'steps': 0, 'busy_steps': 0}
    latest = time.monotonic()

    def step(status, remaining, total):
        nonlocal latest
        progress['steps'] += 1
        progress['busy_steps'] += int(status in (5, 6))
        if time.monotonic() - latest >= 15:
            print(json.dumps({'stage': 'online_backup', 'remaining_pages': remaining,
                              'total_pages': total}), flush=True)
            latest = time.monotonic()

    src = readonly(source)
    dst = sqlite3.connect(destination)
    try:
        page_size = src.execute('PRAGMA page_size').fetchone()[0]
        src.backup(dst, pages=pages, progress=step, sleep=0.01)
        check = dst.execute('PRAGMA quick_check').fetchone()[0]
        if check != 'ok':
            raise ValueError('Snapshot failed quick_check: ' + str(check))
    finally:
        dst.close()
        src.close()
    return {'source_path': str(source), 'snapshot_path': str(destination),
            'started_at_utc': started, 'completed_at_utc': datetime.now(timezone.utc).isoformat(),
            'source_before': before,
            'source_after': {'size': source.stat().st_size, 'mtime_ns': source.stat().st_mtime_ns},
            'snapshot_sha256': file_digest(destination), 'quick_check': check,
            'pages_per_step': pages, 'max_read_bytes_per_step': pages * page_size,
            'source_connection': 'mode=ro; query_only=ON; no explicit transaction', **progress}


def qualify(text, start, end, own_code, code_aliases=()):
    """Nearest following explicit instrument wins, then short leading alias.

    Unqualified references stay unqualified: the current code is not guessed.
    """
    tail = fold(text[end:end + 190])
    tail = re.split(r';|\n|\.\s+|\b(?:articles?|art\.)\s', tail, maxsplit=1, flags=re.I)[0]
    head = fold(text[max(0, start - 65):start])
    for candidate, basis in ((tail, 'explicit_following'), (head, 'explicit_preceding')):
        matches = []
        combined_old_code = re.search(r"code\s+de\s+l['’]\s*urbanisme\s+et\s+de\s+l['’]\s*habitation", candidate, re.I)
        if combined_old_code:
            matches.append((combined_old_code.start(), 'external:historical_urbanisme_et_habitation',
                            'explicit_distinct_historical_code_title', len(combined_old_code.group())))
        same = re.search(r'\b(?:du|au|le)\s+present\s+code\b|\bdu\s+meme\s+code\b', candidate, re.I)
        if same:
            # "même code" needs a prior discourse antecedent not available here.
            if re.search('meme', same.group(), re.I):
                matches.append((same.start(), None, 'ambiguous_same_code_antecedent', len(same.group())))
            else:
                matches.append((same.start(), own_code, 'explicit_present_code', len(same.group())))
        annex = re.search(r"annexe\s+(IV|III|II|I|[1-4])\b", candidate, re.I)
        qualified_annex = annex and (re.search(r'impots|\bCGI\b', candidate, re.I) or own_code in {CGI, *ANNEXES.values()})
        if qualified_annex:
            roman = dict(zip('1234', ANNEXES)).get(annex.group(1), annex.group(1).upper())
            matches.append((annex.start(), ANNEXES[roman], 'explicit_annex', len(annex.group())))
        for code, pattern in CODE_PATTERNS:
            for match in re.finditer(pattern, candidate, re.I):
                if not qualified_annex:
                    matches.append((match.start(), code, basis, len(match.group())))
        for pattern, code, title in code_aliases:
            match = pattern.search(candidate)
            if match and not qualified_annex:
                matches.append((match.start(), code, 'explicit_canonical_code_title', len(match.group())))
        other = re.search(r"\bcode\s+(?!general\s+des\s+impots\b|du\s+travail\b|de\s+la\s+securite\s+sociale\b|de\s+la\s+construction\b|de\s+l['’]\s*urbanisme\b)[a-z][a-z'’ -]{2,65}", candidate, re.I)
        if other and not re.match(r'(?:present|meme)', other.group()[5:], re.I):
            if not any(x[0] == other.start() for x in matches):
                # Unknown title boundaries are not used as stable identifiers
                # for source/proposal comparison. Keep a short unresolved label.
                matches.append((other.start(), 'external:unidentified_code', 'explicit_external_code_title_unresolved', len(other.group())))
        instrument = re.search(r"\b(?:de\s+la|de\s+l['’]|du|de\s+ce|de\s+cette)\s*(?:loi|ordonnance|decret|arrete|reglement|directive|traite|constitution)\b[^.;\n]{0,100}", candidate, re.I)
        if instrument:
            # Dates/identifiers remain in context; stylistic wording is not an
            # instrument identity and must not generate spurious differences.
            kind = re.search(r'loi|ordonnance|decret|arrete|reglement|directive|traite|constitution', instrument.group(), re.I).group().lower()
            matches.append((instrument.start(), 'external:instrument:' + kind, 'explicit_external_instrument', len(instrument.group())))
        if matches:
            # Following qualifiers attach to an article list. Leading context is
            # accepted only when it ends in a short introduction such as CGI art.
            picked = min(matches, key=lambda x: (x[0], -x[3])) if basis == 'explicit_following' else max(matches, key=lambda x: (x[0], x[3]))
            leading_remainder = candidate[picked[0] + picked[3]:]
            leading_prior_article = ARTICLE_WORD.search(candidate[:picked[0]]) is not None
            if basis == 'explicit_following' or (not leading_prior_article and re.fullmatch(r"\s*[,;:\-]?\s*(?:l['’])?\s*", leading_remainder, re.I)):
                return {'code_id': picked[1], 'qualification': picked[2]}
    return {'code_id': None, 'qualification': 'unqualified'}


def expand_range(first, last, limit=100):
    """Only compatible numerical ranges; never invent suffix/order semantics."""
    a, b = normalize(first), normalize(last)
    if a.isdigit() and b.isdigit():
        begin, end, family = int(a), int(b), ''
    else:
        match = re.fullmatch(r'(.+-)(\d+)', a)
        if not match:
            return None
        family, begin = match.group(1), int(match.group(2))
        if b.isdigit():
            end = int(b)
        elif b.startswith(family) and b[len(family):].isdigit():
            end = int(b[len(family):])
        else:
            return None
    if not 0 <= end - begin <= limit:
        return None
    return [family + str(n) for n in range(begin, end + 1)]


def text_references(markup, own_code, code_aliases=()):
    text = plain(markup)
    groups, covered = [], []
    for trigger in ARTICLE_WORD.finditer(text):
        match = TOKEN.match(text, trigger.end())
        if not match:
            continue
        items = [(match.group(), match.start(), match.end(), None)]
        end = match.end()
        for _ in range(79):
            sep = SEPARATOR.match(text, end)
            nxt = TOKEN.match(text, sep.end()) if sep else None
            if not nxt:
                break
            items.append((nxt.group(), nxt.start(), nxt.end(), sep.group('sep').lower()))
            end = nxt.end()
        groups.append((trigger.start(), end, items))
        covered.append((trigger.start(), end))
    for match in PREFIX_TOKEN.finditer(text):
        if not any(a <= match.start() < b for a, b in covered):
            items = [(match.group(), match.start(), match.end(), None)]
            end = match.end()
            sep = SEPARATOR.match(text, end)
            nxt = TOKEN.match(text, sep.end()) if sep and sep.group('sep').lower() in {'à', 'a', 'au'} else None
            if nxt:
                items.append((nxt.group(), nxt.start(), nxt.end(), sep.group('sep').lower()))
                end = nxt.end()
                covered.append((match.start(), end))
            groups.append((match.start(), end, items))
    refs = []
    for start, end, items in groups:
        qualification = qualify(text, start, end, own_code, code_aliases)
        context = text[max(0, start - 100):min(len(text), end + 160)].strip()
        scope_text = text[max(0, start - 65):min(len(text), end + 65)]
        common = {**qualification, 'context': context, 'start': start, 'end': end,
                  'subdivision_context': scope_text.strip() if SUBDIVISION.search(scope_text) else None,
                  'historical_context': bool(HISTORICAL.search(context))}
        previous = None
        for token, pos, finish, sep in items:
            if sep in {'à', 'a', 'au'} and previous:
                expansion = expand_range(previous, token)
                if expansion:
                    for number in expansion[1:]:
                        refs.append({**common, 'number': number, 'raw': token,
                                     'expanded_range': [previous, token]})
                else:
                    refs.append({**common, 'number': normalize(token), 'raw': token,
                                 'range_unexpanded': [previous, token]})
            else:
                refs.append({**common, 'number': normalize(token), 'raw': token})
            previous = token
    return refs


def repeal_proposed(markup):
    value = plain(markup).strip()
    return bool(re.match(r'(?:(?:Le\s+)?pr[ée]sent\s+article\s+est\s+)?abrog[ée]\b', value, re.I))


def official_state_class(state):
    state = fold(state or '').upper()
    if state.endswith('_DIFF'):
        return 'scheduled_transition_not_current_repeal'
    if state in {'ABROGE', 'ANNULE', 'DISJOINT', 'PERIME', 'TRANSFERE'}:
        return 'official_inactive_state'
    return 'other'


def inventory(db, code, as_of):
    """Canonical tree, with every broken/missing branch retained as a limit."""
    current, missing_sections, missing_articles = set(), [], []
    seen = set()
    root = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='TEXTELR'", (code, code)).fetchone()
    if not root:
        return current, [code], []

    def walk(node):
        if node is None:
            return
        for link in node:
            if not link.get('debut', '0001-01-01') <= as_of < link.get('fin', '2999-01-01'):
                continue
            identifier = link.get('id')
            if link.tag == 'LIEN_ART':
                current.add(identifier)
            elif link.tag == 'LIEN_SECTION_TA' and identifier not in seen:
                seen.add(identifier)
                row = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='SECTION_TA'", (code, identifier)).fetchone()
                if row:
                    walk(ET.fromstring(row[0]).find('STRUCTURE_TA'))
                else:
                    missing_sections.append(identifier)
    walk(ET.fromstring(root[0]).find('STRUCT'))
    return current, missing_sections, missing_articles


class Catalog:
    def __init__(self, records, codes, as_of):
        self.records = {r['key']: r for r in records}
        self.codes, self.as_of = set(codes), as_of
        self.ids, self.current, self.historical, self.numbers = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
        self.historical_numbers = defaultdict(list)
        for key, row in self.records.items():
            self.ids[row['id']].append(key)
            slot = (row['code_id'], normalize(row['number']))
            self.historical[slot].append(key)
            self.historical_numbers[slot[1]].append(key)
            if row.get('in_inventory') and row['valid_from'] <= as_of < row['valid_until']:
                self.current[slot].append(key)
                self.numbers[slot[1]].append(key)

    def resolve(self, ref, own_code, hints=None):
        code, number, identifier = ref.get('code_id'), normalize(ref.get('number', '')), ref.get('target_id')
        basis = ref.get('qualification', 'canonical_identifier' if identifier else 'unqualified')
        if code and code not in self.codes:
            return {'status': 'outside_scope', 'target_code_id': code, 'target_id': identifier,
                    'number': number, 'basis': basis}
        if identifier:
            candidates = [k for k in self.ids.get(identifier, []) if not code or self.records[k]['code_id'] == code]
            if len(candidates) == 1:
                key = candidates[0]
                row = self.records[key]
                current = row.get('in_inventory') and row['valid_from'] <= self.as_of < row['valid_until']
                return {'status': 'resolved_current' if current else 'historical_identifier',
                        'target_key': key, 'target_code_id': row['code_id'], 'number': normalize(row['number']),
                        'basis': 'exact_canonical_identifier',
                        'current_number_candidates': self.current.get((row['code_id'], normalize(row['number'])), [])}
            if len(candidates) > 1:
                return {'status': 'ambiguous_identifier', 'candidate_keys': candidates, 'number': number, 'basis': basis}
            # A missing exact ID is not replaced by a same-number article.
            return {'status': 'unresolved_identifier', 'target_code_id': code, 'target_id': identifier,
                    'number': number, 'basis': basis,
                    'current_number_candidates': self.current.get((code, number), [])}
        if not code and hints and len(hints.get(number, set())) == 1:
            code = next(iter(hints[number]))
            basis = 'canonical_citation_code_hint'
        if code and code not in self.codes:
            return {'status': 'outside_scope', 'target_code_id': code, 'number': number, 'basis': basis}
        if not code:
            candidates = self.numbers.get(number, [])
            # "même code" cannot be resolved by catalogue uniqueness.
            if basis == 'ambiguous_same_code_antecedent':
                return {'status': 'ambiguous_code', 'number': number, 'candidate_keys': candidates, 'basis': basis}
            if len(candidates) == 1:
                row = self.records[candidates[0]]
                return {'status': 'resolved_unique_unqualified', 'target_key': candidates[0],
                        'target_code_id': row['code_id'], 'number': number, 'basis': 'unique_in_local_current_catalogue'}
            if candidates:
                return {'status': 'ambiguous_code_or_version', 'number': number,
                        'candidate_keys': candidates, 'basis': basis}
            histories = self.historical_numbers.get(number, [])
            return {'status': 'unqualified_historical_or_unresolved', 'number': number,
                    'historical_candidates_count': len(histories), 'candidate_keys': histories[:20], 'basis': basis}
        candidates = self.current.get((code, number), [])
        if len(candidates) == 1:
            return {'status': 'resolved_current', 'target_key': candidates[0],
                    'target_code_id': code, 'number': number, 'basis': basis}
        if len(candidates) > 1:
            return {'status': 'ambiguous_current_version', 'target_code_id': code,
                    'number': number, 'candidate_keys': candidates, 'basis': basis}
        historical = self.historical.get((code, number), [])
        return {'status': 'historical_number_only' if historical else 'unresolved_number',
                'target_code_id': code, 'number': number, 'candidate_keys': historical[:20],
                'historical_candidates_count': len(historical), 'basis': basis}


def strongly_connected(graph):
    """Iterative Kosaraju, so long reference chains cannot exhaust recursion."""
    vertices = set(graph)
    reverse = defaultdict(set)
    for source, targets in graph.items():
        vertices.update(targets)
        for target in targets:
            reverse[target].add(source)
    visited, order = set(), []
    for vertex in sorted(vertices):
        if vertex in visited:
            continue
        visited.add(vertex)
        stack = [(vertex, iter(graph.get(vertex, ())))]
        while stack:
            item, neighbours = stack[-1]
            nxt = next(neighbours, None)
            if nxt is None:
                stack.pop()
                order.append(item)
            elif nxt not in visited:
                visited.add(nxt)
                stack.append((nxt, iter(graph.get(nxt, ()))))
    visited, components = set(), []
    for vertex in reversed(order):
        if vertex in visited:
            continue
        component, stack = [], [vertex]
        visited.add(vertex)
        while stack:
            item = stack.pop()
            component.append(item)
            for nxt in reverse.get(item, ()):
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        if len(component) > 1 or vertex in graph.get(vertex, ()):
            components.append(sorted(component))
    return sorted(components, key=lambda x: (-len(x), x[0]))


LIMITS = [
    "Audit structurel local, sans revue juridique, sans approbation de fond et sans modification automatique.",
    "Le graphe couvre les citations ARTICLE structurées, les numéros préfixés et les listes numériques introduites par article/art.; les renvois implicites, livres/chapitres seuls et sémantiques ne sont pas exhaustifs.",
    "Les codes et instruments hors des neuf recueils sont inventoriés, pas vérifiés. Les titres de codes sont rapprochés des identifiants réellement présents dans les liens canoniques; les autres titres restent non identifiés. Leur absence locale n'est pas une anomalie juridique.",
    "Une unicité locale d'un numéro non qualifié ne prouve pas le code juridiquement visé; les ambiguïtés ne sont jamais tranchées arbitrairement.",
    "Les plages numériques compatibles jusqu'à 101 éléments sont développées; les autres plages et les suffixes non reconnus restent à examiner.",
    "Les liens canoniques sens=cible sont des citations entrantes de la source officielle, et ne prouvent pas leur maintien dans une proposition.",
    "Les suppressions et introductions de renvois sont comparées par code identifié et numéro, sans identité complète des instruments non codifiés ni validation des alinéas; une suppression normative autorisée peut les justifier.",
    "L'état ABROGE_DIFF signale une transition différée; il n'est jamais assimilé à une abrogation déjà applicable à la date du corpus.",
    "Les abrogations proposées ne sont reconnues automatiquement que par une formule initiale explicite; les suppressions partielles, dérogations, alinéas, versions et transitions demandent une lecture.",
    "Les cycles du graphe sont informatifs: un cycle n'établit aucune incohérence.",
    "Le snapshot fige une transaction SQLite cohérente pendant la rédaction active; les propositions ultérieures et les sources externes en cours de récupération en sont absentes. Les fichiers de politique sont figés individuellement juste après la sauvegarde, sans transaction atomique entre SQLite et JSON.",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=HERE / 'corpus.sqlite')
    parser.add_argument('--output', type=Path, default=HERE / 'runtime/global-reference-audit-20261022')
    parser.add_argument('--as-of', default='2026-10-18')
    parser.add_argument('--snapshot-only', action='store_true')
    parser.add_argument('--reuse-snapshot', action='store_true', help='Use only the existing, already frozen snapshot')
    args = parser.parse_args(argv)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    snapshot = output / 'corpus.snapshot.sqlite'
    if args.reuse_snapshot:
        capture = json.loads((output / 'capture.json').read_text())
        if file_digest(snapshot) != capture['snapshot_sha256']:
            raise ValueError('Frozen snapshot hash changed')
    else:
        capture = snapshot_database(args.db, snapshot)
        capture['policies'] = {}
        for name in ('corpus.json', 'policy-coordinations.json', 'site-summaries.json', 'reference-focus-extra.json'):
            source = args.db.resolve().parent / name
            if source.exists():
                value = source.read_bytes()
                (output / name).write_bytes(value)
                capture['policies'][name] = {'sha256': digest(value), 'source_path': str(source),
                                             'stable_during_capture': digest(source.read_bytes()) == digest(value)}
        capture['auditor_sha256'] = file_digest(__file__)
        capture['as_of'] = args.as_of
        write_json(output / 'capture.json', capture)
    if args.snapshot_only:
        print(json.dumps({'snapshot': str(snapshot), 'sha256': capture['snapshot_sha256']}), flush=True)
        return
    audit(snapshot, output, args.as_of, capture)


def audit(snapshot, output, as_of, capture):
    started = datetime.now(timezone.utc).isoformat()
    config = json.loads((output / 'corpus.json').read_text())
    codes = config['codes'] + config.get('annexes', [])
    code_map = {x['id']: x for x in codes}
    db = readonly(snapshot)
    db.row_factory = sqlite3.Row
    inventories, reports, selected = {}, {}, set()
    for code in codes:
        ids, missing_sections, missing_articles = inventory(db, code['id'], as_of)
        inventories[code['id']] = ids
        selected.update(code['id'] + '|' + identifier for identifier in ids)
        reports[code['id']] = {'code_id': code['id'], 'title': code['title'], 'slug': code['slug'],
                               'inventory_entries': len(ids), 'missing_sections': missing_sections,
                               'missing_articles': missing_articles, 'scanned_entries': 0,
                               'fields_scanned': Counter(), 'edges_by_field': Counter(),
                               'resolutions': Counter(), 'findings_by_kind': Counter(),
                               'findings_by_priority': Counter(), 'examples': []}
    records = []
    source_logical_hash = hashlib.sha256()
    for row in db.execute('SELECT code_id,id,number,valid_from,valid_until,state,source_sha256,archive FROM articles ORDER BY code_id,id'):
        data = dict(row)
        data['key'] = data['code_id'] + '|' + data['id']
        data['valid_from'] = data['valid_from'] or '0001-01-01'
        data['valid_until'] = data['valid_until'] or '2999-01-01'
        data['in_inventory'] = data['key'] in selected
        source_logical_hash.update(json.dumps(dict(row), sort_keys=True, ensure_ascii=False).encode() + b'\n')
        records.append(data)
    catalog = Catalog(records, code_map, as_of)
    missing = selected - catalog.records.keys()
    for key in sorted(missing):
        code, identifier = key.split('|', 1)
        reports[code]['missing_articles'].append(identifier)
    selected.difference_update(missing)
    out_of_date = [k for k in selected if not catalog.records[k]['valid_from'] <= as_of < catalog.records[k]['valid_until']]
    selected.difference_update(out_of_date)
    all_documents_hash, archives_hash, drafts_hash = hashlib.sha256(), hashlib.sha256(), hashlib.sha256()
    for row in db.execute('SELECT code_id,id,kind,sha256,archive FROM documents ORDER BY code_id,id,kind'):
        all_documents_hash.update(json.dumps(list(row), ensure_ascii=False).encode() + b'\n')
    for row in db.execute('SELECT * FROM archives ORDER BY name'):
        archives_hash.update(json.dumps(list(row), ensure_ascii=False).encode() + b'\n')
    # Exact strings are hashed, not normalized. draft_sources is separately
    # protected by the byte-for-byte frozen SQLite snapshot.
    for row in db.execute('SELECT * FROM drafts ORDER BY code_id,source_id'):
        drafts_hash.update(json.dumps(list(row), ensure_ascii=False).encode() + b'\n')
    fingerprint = {'snapshot_sha256': capture['snapshot_sha256'], 'as_of': as_of,
                   'all_article_metadata_sha256': source_logical_hash.hexdigest(),
                   'all_document_metadata_sha256': all_documents_hash.hexdigest(),
                   'archives_sha256': archives_hash.hexdigest(), 'all_drafts_sha256': drafts_hash.hexdigest(),
                   'policy_files': capture['policies'], 'auditor_sha256': file_digest(__file__)}
    run_id = digest(json.dumps(fingerprint, sort_keys=True, ensure_ascii=False))
    fingerprint['audit_id'] = run_id
    write_json(output / 'fingerprints.json', fingerprint)
    print(json.dumps({'stage': 'inventory_frozen', 'entries': len(selected),
                      'all_historical_article_versions': len(records), 'audit_id': run_id}), flush=True)

    query = '''SELECT a.code_id,a.id,a.content_xml,a.source_sha256,
               d.xml AS document_xml,d.sha256 AS document_sha256,
               p.source_sha256 AS draft_source_sha256,p.status AS draft_status,p.proposed_xml
               FROM articles a LEFT JOIN documents d
               ON d.code_id=a.code_id AND d.id=a.id AND d.kind='ARTICLE'
               LEFT JOIN drafts p ON p.code_id=a.code_id AND p.source_id=a.id
               WHERE a.valid_from<=? AND a.valid_until>? ORDER BY a.code_id,a.id'''
    guards, proposal_repeals, proposal_changed = {}, set(), set()
    canonical_code_titles, document_stats = defaultdict(set), Counter()
    manifest = (output / 'article-manifest.jsonl').open('w')
    anomalies = []
    for row in db.execute(query, (as_of, as_of)):
        key = row['code_id'] + '|' + row['id']
        if key not in selected:
            continue
        raw = row['document_xml']
        notes, xml_error = '', None
        if raw:
            try:
                root = ET.fromstring(raw)
                document_stats['article_documents_parsed'] += 1
                for link in root.findall('./LIENS/LIEN'):
                    cid = link.get('cidtexte')
                    if link.get('naturetexte') != 'CODE' or not cid or cid in code_map:
                        continue
                    title = re.split(r'\s+-\s+art(?:icle)?\.?\s', ''.join(link.itertext()), maxsplit=1, flags=re.I)[0]
                    title = title.split(',')[0].strip(' .')
                    if re.match(r'^(?:Code|Livre)\b', title, re.I):
                        canonical_code_titles[fold(title)].add(cid)
                node = root.find('NOTA/CONTENU')
                if node is not None:
                    notes = (node.text or '') + ''.join(ET.tostring(x, encoding='unicode') for x in node)
                    notes = notes.strip()
                if plain(notes).strip():
                    document_stats['nonempty_official_application_notes'] += 1
                body_node = root.find('BLOC_TEXTUEL/CONTENU')
                body_mirror = (body_node.text or '') + ''.join(ET.tostring(x, encoding='unicode') for x in body_node) if body_node is not None else ''
                if body_mirror == row['content_xml']:
                    document_stats['canonical_body_matches_stored_article_body'] += 1
                else:
                    anomalies.append((key, 'canonical_body_mirror_mismatch', 0, {'canonical_body_sha256': digest(body_mirror)}))
            except ET.ParseError as exc:
                xml_error = str(exc)
        guard = {'source_sha256': row['source_sha256'], 'source_body_sha256': digest(row['content_xml']),
                 'source_notes_sha256': digest(notes), 'article_document_sha256': digest(raw),
                 'article_document_stored_sha256': row['document_sha256'],
                 'proposal_sha256': digest(row['proposed_xml']) if row['proposed_xml'] is not None else None,
                 'draft_source_sha256': row['draft_source_sha256'], 'draft_status': row['draft_status']}
        guards[key] = guard
        manifest.write(json.dumps({'key': key, 'number': catalog.records[key]['number'],
                                   'valid_from': catalog.records[key]['valid_from'],
                                   'valid_until': catalog.records[key]['valid_until'],
                                   'source_state': catalog.records[key]['state'], **guard}, ensure_ascii=False) + '\n')
        if not raw:
            anomalies.append((key, 'missing_article_document', 1, {}))
        elif xml_error:
            anomalies.append((key, 'invalid_article_document_xml', 1, {'error': xml_error}))
        elif guard['article_document_sha256'] != guard['article_document_stored_sha256']:
            anomalies.append((key, 'canonical_document_hash_mismatch', 0, {}))
        if row['draft_source_sha256'] and row['draft_source_sha256'] != row['source_sha256']:
            anomalies.append((key, 'draft_source_fingerprint_mismatch', 0, {}))
        if row['proposed_xml'] is not None:
            if repeal_proposed(row['proposed_xml']):
                proposal_repeals.add(key)
            if row['proposed_xml'] != row['content_xml']:
                proposal_changed.add(key)
    manifest.close()
    code_aliases = []
    for title, ids in canonical_code_titles.items():
        if len(ids) == 1:
            pattern = re.compile(r'\b' + re.escape(title).replace(r'\ ', r'\s+').replace("'", "['’]") + r'\b', re.I)
            code_aliases.append((pattern, next(iter(ids)), title))
    code_aliases.sort(key=lambda x: -len(x[2]))
    write_json(output / 'external-code-title-catalogue.json', {'audit_id': run_id,
               'provenance': 'Titles and cidtexte observed in frozen canonical ARTICLE LIENS, naturetexte=CODE',
               'titles': {title: sorted(ids) for title, ids in sorted(canonical_code_titles.items())},
               'semantic_review_by_jurist': False})

    findings, edge_counts, resolution_counts, field_counts = [], Counter(), Counter(), Counter()
    source_graph, proposed_graph = defaultdict(set), defaultdict(set)
    unresolved_examples, diff_counts = [], Counter()
    edges = (output / 'edges.jsonl').open('w')
    finding_stream = (output / 'findings.jsonl').open('w')

    def finding(key, kind, priority, evidence, target_key=None):
        row = catalog.records[key]
        result = {'finding_id': digest(run_id + '|' + key + '|' + kind + '|' + json.dumps(evidence, sort_keys=True, ensure_ascii=False)),
                  'audit_id': run_id, 'priority': priority, 'kind': kind, 'source_key': key,
                  'code_id': row['code_id'], 'number': row['number'], 'source_guard': guards[key],
                  'evidence': evidence, 'semantic_review_by_jurist': False,
                  'automatic_change': False}
        if target_key:
            result['target_key'] = target_key
            target = catalog.records[target_key]
            result['target_guard'] = guards.get(target_key, {'source_sha256': target['source_sha256'],
                                                            'historical_source_only': True})
        finding_stream.write(json.dumps(result, ensure_ascii=False) + '\n')
        findings.append(result)
        report = reports[row['code_id']]
        report['findings_by_kind'][kind] += 1
        report['findings_by_priority'][str(priority)] += 1
        if priority < 3:
            report['examples'].append(result)
            report['examples'].sort(key=lambda x: (x['priority'], x['kind'], x['source_key']))
            del report['examples'][12:]

    for key, kind, priority, evidence in anomalies:
        finding(key, kind, priority, evidence)

    def emit_edge(key, field, ref, hints=None, is_effective=True):
        resolution = catalog.resolve(ref, catalog.records[key]['code_id'], hints)
        if field in {'source_body', 'source_notes', 'proposal'} and ref.get('historical_context') and resolution['status'].startswith('resolved'):
            resolution['status'] = 'historical_context_current_number_candidate'
            resolution['current_number_candidate_key'] = resolution.pop('target_key')
            resolution['version_scope'] = 'Historical text/date/transition requires a version-specific review; current number is not validated as the historical target'
        target_key = resolution.get('target_key')
        edge = {'audit_id': run_id, 'source_key': key, 'field': field, 'reference': ref,
                'resolution': resolution, 'source_guard': guards[key]}
        if target_key:
            target = catalog.records[target_key]
            edge['target_guard'] = guards.get(target_key, {'source_sha256': target['source_sha256'],
                                                          'historical_source_only': True})
        elif resolution.get('current_number_candidate_key'):
            edge['current_number_candidate_guard'] = guards.get(resolution['current_number_candidate_key'])
        edges.write(json.dumps(edge, ensure_ascii=False) + '\n')
        status = resolution['status']
        edge_counts[field] += 1
        resolution_counts[status] += 1
        report = reports[catalog.records[key]['code_id']]
        report['edges_by_field'][field] += 1
        report['resolutions'][status] += 1
        # The official incoming-link inventory is not inserted into the active
        # outgoing graph; both its direction and provenance remain explicit.
        if field == 'canonical_incoming_citation':
            return edge
        if target_key and status.startswith('resolved'):
            if field in {'source_body', 'source_notes', 'canonical_outgoing_citation'}:
                source_graph[key].add(target_key)
            if is_effective and field in {'proposal', 'source_body', 'source_notes'}:
                proposed_graph[key].add(target_key)
            target = catalog.records[target_key]
            if field == 'proposal' and target_key in proposal_repeals and not ref.get('historical_context'):
                finding(key, 'proposal_refers_to_proposed_repeal', 1,
                        {'field': field, 'reference': ref, 'resolution': resolution,
                         'review': 'Confirmer la coordination, les exceptions et les dispositions transitoires.'}, target_key)
            elif field == 'source_body' and is_effective and target_key in proposal_repeals and not ref.get('historical_context'):
                finding(key, 'unrewritten_referrer_to_proposed_repeal', 1,
                        {'field': field, 'reference': ref, 'resolution': resolution}, target_key)
            elif official_state_class(target.get('state')) == 'official_inactive_state':
                finding(key, 'reference_to_official_inactive_state', 2,
                        {'field': field, 'reference': ref, 'resolution': resolution,
                         'target_state': target['state']}, target_key)
            elif official_state_class(target.get('state')) == 'scheduled_transition_not_current_repeal' and is_effective:
                finding(key, 'target_deferred_transition_requires_review', 2,
                        {'field': field, 'reference': ref, 'resolution': resolution,
                         'target_state': target['state'], 'valid_from': target['valid_from'],
                         'valid_until': target['valid_until'],
                         'review': 'État différé; vérifier la date et la transition, sans conclure à une abrogation actuelle.'}, target_key)
            if ref.get('subdivision_context') and target_key in proposal_changed and is_effective:
                finding(key, 'subdivision_scope_requires_review', 2,
                        {'field': field, 'reference': ref, 'resolution': resolution,
                         'review': "La proposition cible change; la portée de l'alinéa/subdivision n'a pas été vérifiée."}, target_key)
        elif status != 'outside_scope':
            priority = 2 if field == 'proposal' and status in {'unresolved_identifier', 'unresolved_number'} else 3
            kind = 'historical_target_version_review' if status.startswith('historical') else 'reference_resolution_review'
            finding(key, kind, priority, {'field': field, 'reference': ref, 'resolution': resolution}, target_key)
        if ref.get('range_unexpanded'):
            finding(key, 'range_not_expanded', 2, {'field': field, 'reference': ref})
        return edge

    def identity(edge):
        r = edge['resolution']
        code = r.get('target_code_id') or edge['reference'].get('code_id') or '?'
        return code + '|' + r.get('number', edge['reference']['number'])

    last_log = time.monotonic()
    for row in db.execute(query, (as_of, as_of)):
        key, code = row['code_id'] + '|' + row['id'], row['code_id']
        if key not in selected:
            continue
        root, notes, links, hints = None, '', [], defaultdict(set)
        if row['document_xml']:
            try:
                root = ET.fromstring(row['document_xml'])
                note = root.find('NOTA/CONTENU')
                notes = ''.join(note.itertext()) if note is not None else ''
                links = root.findall('./LIENS/LIEN')
            except ET.ParseError:
                pass
        for link in links:
            if link.get('sens') == 'source' and link.get('typelien') == 'CITATION' and link.get('num') and link.get('cidtexte'):
                hints[normalize(link.get('num'))].add(link.get('cidtexte'))
        proposal = row['proposed_xml']
        source_refs, proposal_refs = {}, {}
        for field, value in (('source_body', row['content_xml']), ('source_notes', notes), ('proposal', proposal)):
            if field == 'proposal' and value is None:
                continue
            field_counts[field] += 1
            reports[code]['fields_scanned'][field] += 1
            refs = text_references(value, code, code_aliases)
            seen = set()
            for ref in refs:
                # Keep distinct positions and qualification; only exact parser
                # duplication is dropped, never repeated legal occurrences.
                signature = (ref['number'], ref['code_id'], ref['start'], ref['end'])
                if signature in seen:
                    continue
                seen.add(signature)
                edge = emit_edge(key, field, ref, hints, is_effective=(field == 'proposal' or proposal is None or field == 'source_notes'))
                if field == 'source_body':
                    source_refs.setdefault(identity(edge), edge)
                elif field == 'proposal':
                    proposal_refs.setdefault(identity(edge), edge)
        # Every canonical link is inventoried, including modification,
        # concordance and incoming metadata. Only CITATION forms graph edges.
        for link in links:
            ref = {'number': normalize(link.get('num', '')), 'raw_number': link.get('num'),
                   'code_id': link.get('cidtexte') or None, 'target_id': link.get('id') or None,
                   'qualification': 'canonical_metadata', 'link_type': link.get('typelien'),
                   'sens': link.get('sens'), 'context': ''.join(link.itertext()).strip(),
                   'historical_context': bool(HISTORICAL.search(''.join(link.itertext())))}
            if link.get('typelien') == 'CITATION':
                field = 'canonical_outgoing_citation' if link.get('sens') == 'source' else 'canonical_incoming_citation'
                emit_edge(key, field, ref, is_effective=False)
            else:
                edges.write(json.dumps({'audit_id': run_id, 'source_key': key, 'field': 'canonical_other_link',
                                        'reference': ref, 'source_guard': guards[key],
                                        'resolution': {'status': 'metadata_not_active_citation'}}, ensure_ascii=False) + '\n')
                edge_counts['canonical_other_link'] += 1
                reports[code]['edges_by_field']['canonical_other_link'] += 1
        if root is not None:
            field_counts['canonical_article_document'] += 1
            reports[code]['fields_scanned']['canonical_article_document'] += 1
            for version in root.findall('./VERSIONS/VERSION/LIEN_ART'):
                edges.write(json.dumps({'audit_id': run_id, 'source_key': key,
                                        'field': 'canonical_version_lineage',
                                        'reference': dict(version.attrib), 'source_guard': guards[key],
                                        'resolution': {'status': 'version_metadata_not_active_citation'}}, ensure_ascii=False) + '\n')
                edge_counts['canonical_version_lineage'] += 1
                reports[code]['edges_by_field']['canonical_version_lineage'] += 1
            for element in root.iter():
                for attribute, value in element.attrib.items():
                    if attribute.lower() not in {'href', 'src'}:
                        continue
                    for identifier in sorted(set(re.findall(r'(?:LEGI|JORF)ARTI\d{12}', value))):
                        emit_edge(key, 'canonical_embedded_article_identifier',
                                  {'number': '', 'target_id': identifier, 'code_id': None,
                                   'context': value, 'qualification': 'embedded_canonical_identifier'}, is_effective=False)
        if proposal is not None:
            for kind, changed in (('reference_disappeared_from_proposal', source_refs.keys() - proposal_refs.keys()),
                                  ('reference_introduced_in_proposal', proposal_refs.keys() - source_refs.keys())):
                for reference in sorted(changed):
                    edge = (source_refs if kind.startswith('reference_disappeared') else proposal_refs)[reference]
                    diff_counts[kind] += 1
                    status = edge['resolution']['status']
                    priority = 1 if kind == 'reference_introduced_in_proposal' and status in {'unresolved_number', 'unresolved_identifier'} else 2
                    finding(key, kind, priority, {'reference_identity': reference, 'field': edge['field'],
                            'reference': edge['reference'], 'resolution': edge['resolution'],
                            'source_proposal_explicit_repeal': key in proposal_repeals,
                            'review': 'Différence structurelle; contrôler la justification, le champ et la transition, sans présumer une erreur.'},
                            edge['resolution'].get('target_key'))
        reports[code]['scanned_entries'] += 1
        if time.monotonic() - last_log > 15:
            print(json.dumps({'stage': 'scan', 'scanned_entries': sum(r['scanned_entries'] for r in reports.values()),
                              'edges': sum(edge_counts.values()), 'findings': len(findings)}), flush=True)
            last_log = time.monotonic()
    edges.close()
    finding_stream.close()
    db.close()
    cycles = {}
    for name, graph in (('official_source_citations', source_graph), ('proposed_view_textual_citations', proposed_graph)):
        components = strongly_connected(graph)
        cycles[name] = {'status': 'informational_only_not_an_incoherence', 'components': len(components),
                        'vertices_in_cycles': sum(map(len, components)), 'largest_component': len(components[0]) if components else 0,
                        'members': components}
    write_json(output / 'cycles.json', {'audit_id': run_id, **cycles})
    queue_items = sorted(findings, key=lambda x: (x['priority'], x['code_id'], x['source_key'], x['kind'], x['finding_id']))
    queue = {'audit_id': run_id, 'semantic_review_by_jurist': False, 'automatic_change': False,
             'priority_legend': {'0': 'Intégrité source/proposition', '1': 'Coordination prioritaire à examiner',
                                 '2': 'Différence de renvoi ou portée à examiner', '3': 'Résolution/historique à qualifier'},
             'items_count': len(queue_items), 'items': queue_items}
    write_json(output / 'queue.json', queue)
    clusters = {}
    for item in queue_items:
        if item['kind'] not in {'proposal_refers_to_proposed_repeal', 'unrewritten_referrer_to_proposed_repeal'}:
            continue
        target = item['target_key']
        cluster = clusters.setdefault(target, {'target_key': target, 'target_number': catalog.records[target]['number'],
                'target_code_id': catalog.records[target]['code_id'], 'target_guard': guards[target],
                'source_keys': set(), 'finding_ids': [], 'occurrences': 0})
        cluster['source_keys'].add(item['source_key'])
        cluster['finding_ids'].append(item['finding_id'])
        cluster['occurrences'] += 1
    for cluster in clusters.values():
        cluster['source_keys'] = sorted(cluster['source_keys'])
        cluster['distinct_referrers'] = len(cluster['source_keys'])
    write_json(output / 'coordination-clusters.json', {'audit_id': run_id,
               'status': 'structural_coordination_review_not_legal_incoherence',
               'targets': sorted(clusters.values(), key=lambda x: (-x['distinct_referrers'], x['target_key']))})
    report_dir = output / 'codes'
    report_dir.mkdir(exist_ok=True)
    for code, report in reports.items():
        report['audit_id'] = run_id
        report['semantic_review_by_jurist'] = False
        report['limits'] = LIMITS
        report['queue_items'] = sum(report['findings_by_priority'].values())
        write_json(report_dir / (code_map[code]['slug'] + '.json'), report)
    summary = {'audit_id': run_id, 'version': VERSION, 'started_at_utc': started,
               'completed_at_utc': datetime.now(timezone.utc).isoformat(), 'as_of': as_of,
               'scope': 'five_complete_codes_and_four_CGI_annexes',
               'source_entries_in_canonical_inventory': len(selected) + len(missing) + len(out_of_date),
               'entries_scanned': sum(r['scanned_entries'] for r in reports.values()),
               'all_historical_article_versions_indexed': len(catalog.records),
               'missing_inventory_articles': sorted(missing), 'inventory_date_mismatches': out_of_date,
               'fields_scanned': field_counts, 'edge_counts': edge_counts,
               'canonical_document_checks': document_stats,
               'resolution_counts': resolution_counts, 'findings_count': len(findings),
               'distinct_articles_with_findings': len({x['source_key'] for x in findings}),
               'distinct_articles_with_priority_1_findings': len({x['source_key'] for x in findings if x['priority'] == 1}),
               'proposed_repeal_targets_with_detected_referrers': len(clusters),
               'findings_by_priority': Counter(str(x['priority']) for x in findings),
               'findings_by_kind': Counter(x['kind'] for x in findings),
               'reference_differences': diff_counts,
               'proposals_with_explicit_repeal_formula': len(proposal_repeals),
               'proposals_differing_from_source_body': len(proposal_changed),
               'cycles': {name: {k: v for k, v in value.items() if k != 'members'} for name, value in cycles.items()},
               'snapshot_and_policy_fingerprints': fingerprint,
               'semantic_review_by_jurist': False, 'automatic_change': False, 'limits': LIMITS,
               'code_reports': [{k: v for k, v in report.items() if k not in {'limits', 'examples'}} for report in reports.values()]}
    write_json(output / 'summary.json', summary)
    lines = ['# Audit structurel global des renvois', '',
             f"Date du corpus : {as_of}. Identifiant d'audit : `{run_id}`.", '',
             f"{summary['entries_scanned']:,} entrées analysées; {len(catalog.records):,} versions indexées; "
             f"{sum(edge_counts.values()):,} occurrences/liens inventoriés; {len(findings):,} points à examiner.", '',
             "Les points à examiner ne constituent pas des erreurs juridiques établies. Aucune proposition n'a été modifiée.", '',
             '| Recueil | Entrées analysées | Points à examiner |', '|---|---:|---:|']
    for report in reports.values():
        lines.append(f"| {report['title']} | {report['scanned_entries']} | {report['queue_items']} |")
    lines.extend(['', '## Couverture et limites', ''] + ['- ' + item for item in LIMITS])
    lines.extend(['', '## Exemples prioritaires', ''])
    for report in reports.values():
        lines.append('### ' + report['title'])
        lines.append('')
        for example in sorted(report['examples'], key=lambda x: x['priority'])[:3]:
            evidence = example['evidence']
            context = evidence.get('reference', {}).get('context', '')
            lines.append(f"- P{example['priority']} — {example['number']} (`{example['source_key']}`) : "
                         f"`{example['kind']}`. {context[:330]}")
        lines.append('')
    (output / 'REPORT.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'stage': 'complete', 'entries_scanned': summary['entries_scanned'],
                      'edges': sum(edge_counts.values()), 'findings': len(findings),
                      'summary': str(output / 'summary.json')}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
