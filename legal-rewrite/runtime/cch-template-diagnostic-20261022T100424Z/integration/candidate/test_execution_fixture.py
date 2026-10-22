"""Synthetic CLI startup evidence for isolated tests; never a live receipt."""

def emit_cli_startup(kwargs):
    stream=kwargs['stderr'];folder=kwargs['cwd']
    stream.write('OpenAI Codex vTEST\n--------\nworkdir: '+str(folder)+
                 '\nmodel: gpt-6-astra\nprovider: openai\nreasoning effort: medium\n'
                 'session id: 00000000-0000-0000-0000-000000000001\n--------\nuser\nTest only\ncodex\nDone\n')
    stream.flush()
