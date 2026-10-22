"""One read-only, on-demand MCP tool. No listener, ingestion or account tools.

Stdio follows MCP 2025-06-18. It does not read a key or contact past.dev until
past_recall is explicitly called. Pipeline activation is a separate step.
"""
import json
import sys
from past_memory import PastClient, PastError, NOTICE

TOOL = {
    'name': 'past_recall',
    'description': 'Recherche ciblée dans les décisions et audits datés de ce chantier. Consulter à la demande ; vérifier les textes locaux actuels et lire les sources légales intégrales. Aucun accès à d’autres identités ni aucun envoi de document.',
    'inputSchema': {
        'type': 'object',
        'properties': {'question': {'type': 'string', 'minLength': 3, 'maxLength': 1200},
                       'max_tokens': {'type': 'integer', 'minimum': 256, 'maximum': 8000, 'default': 4000}},
        'required': ['question'], 'additionalProperties': False},
    'annotations': {'readOnlyHint': True, 'destructiveHint': False, 'openWorldHint': True}
}


def handle(message):
    method = message.get('method')
    if method == 'initialize':
        return {'protocolVersion': '2025-06-18', 'capabilities': {'tools': {}},
                'serverInfo': {'name': 'legal-rewrite-memory', 'version': '0.1.0'}}
    if method == 'ping':
        return {}
    if method == 'tools/list':
        return {'tools': [TOOL]}
    if method == 'tools/call':
        params = message.get('params', {})
        args = params.get('arguments', {})
        if params.get('name') != 'past_recall' or not isinstance(args, dict) or not set(args) <= {'question', 'max_tokens'}:
            raise ValueError('Unknown tool or arguments')
        try:
            result = PastClient().recall(args.get('question'), args.get('max_tokens', 4000))
            return {'content': [{'type': 'text', 'text': json.dumps({'notice': NOTICE, 'recall': result}, ensure_ascii=False)}], 'isError': False}
        except PastError as error:
            return {'content': [{'type': 'text', 'text': json.dumps({'error': error.code, 'http_status': error.status, 'request_id': error.request_id})}], 'isError': True}
    raise LookupError('Unsupported method')


def main():
    for line in sys.stdin:
        request_id = None
        try:
            message = json.loads(line)
            if 'id' not in message:
                continue
            request_id = message['id']
            result = handle(message)
            response = {'jsonrpc': '2.0', 'id': request_id, 'result': result}
        except (ValueError, TypeError, KeyError, LookupError):
            response = {'jsonrpc': '2.0', 'id': request_id, 'error': {'code': -32602, 'message': 'Unsupported request or arguments'}}
        except Exception:
            # Never serialize exception details, environment values or headers.
            response = {'jsonrpc': '2.0', 'id': request_id, 'error': {'code': -32603, 'message': 'Local recall unavailable; consult the setup status'}}
        print(json.dumps(response, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
