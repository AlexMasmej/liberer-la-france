"""Classify terminal native CLI diagnostics, never the legal transcript.

Unknown failures still use the runner's existing three-attempt bound. This
function neither invokes the CLI nor retries, registers or authorizes a job.
"""
def native_access_failure(stderr):
    import re
    lines = stderr.splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    # Native text mode can finish with this informational two-line footer.
    if (len(lines) >= 2 and lines[-2].strip() == 'tokens used'
            and re.fullmatch(r'[\d,]+', lines[-1].strip())):
        del lines[-2:]
    while lines and not lines[-1].strip():
        lines.pop()
    diagnostics = []
    for line in reversed(lines):
        match = re.fullmatch(r'ERROR:\s*(.+)', line)
        if not match:
            match = re.fullmatch(
                r'\d{4}-\d\d-\d\dT\S+\s+ERROR\s+[\w:]+:\s*(.+)', line)
        if not match:
            break
        diagnostics.append(match[1])
    # Merely mentioning "quota", sign-in or authentication is insufficient.
    # Keep explicit access denials blocking even when transport also fails.
    denied = re.compile(
        r'\b(?:rate[ _-]limit(?:ed|s)?|usage[ _-]limit(?:s)?|'
        r'insufficient[ _-]quota|quota[ _-](?:exceeded|exhausted)|'
        r'authentication[ _-](?:failed|required)|unauthori[sz]ed|'
        r'invalid[ _-](?:api[ _-])?key|not (?:logged|signed) in|'
        r'please (?:log|sign) in|sign in (?:again|to continue)|'
        r'too many requests|insufficient (?:credits|funds)|'
        r'credit balance is too low)\b|'
        r'\b(?:HTTP(?:[/\d.]+)?(?: status| error)?|status(?: code)?|'
        r'unexpected status code)[ :=]+(?:401|403|429)\b', re.I)
    return any(denied.search(message) for message in diagnostics)
