"""Local startup-log fixtures only: no Codex process, model or corpus access."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from unittest.mock import patch
import json

import worker_execution as execution


SPEC={'model':'gpt-6-astra','reasoning_effort':'medium'}
SESSION='01a16078-cc0a-77e2-9cd9-da46d133325c'


class WorkerExecution(TestCase):
    def setUp(self):
        temporary=TemporaryDirectory(prefix='worker execution tests ')
        self.addCleanup(temporary.cleanup)
        self.runtime=Path(temporary.name)
        self.folder=self.runtime/'isolated-job';self.folder.mkdir()
        # A regression must fail rather than spawn even a non-model process.
        for name in ['subprocess.run','subprocess.Popen','os.system']:
            p=patch(name,side_effect=AssertionError('No real CLI or process allowed'))
            p.start();self.addCleanup(p.stop)

    def header(self,**changes):
        fields={'workdir':str(self.folder),'model':SPEC['model'],'provider':'openai',
                'reasoning effort':SPEC['reasoning_effort'],'session id':SESSION}
        fields.update(changes)
        return ('OpenAI Codex v0.160.1\n--------\n'
                f"workdir: {fields['workdir']}\n"
                f"model: {fields['model']}\n"
                f"provider: {fields['provider']}\n"
                'approval: never\nsandbox: read-only\n'
                f"reasoning effort: {fields['reasoning effort']}\n"
                'reasoning summaries: none\n'
                f"session id: {fields['session id']}\n--------\n")

    def log(self,name='errors-1.log',*,header=None,prefix='',prompt='PROMPT',response=True):
        content=prefix+(self.header() if header is None else header)+'user\n'+prompt+'\n'
        if response:content+='codex\nOK.\n'
        p=self.folder/name;p.write_text(content);return p

    def verify(self,path=None,expected=None):
        return execution.verify_execution(self.folder,expected=SPEC if expected is None else expected,stderr_path=path)

    def assert_unverified(self,result):
        self.assertIs(result.get('verified'),False)
        self.assertTrue(result.get('status'),'Failure must carry an explicit status')

    def test_requested_execution_defaults_to_astra_medium_without_config(self):
        self.assertEqual(execution.requested_execution(self.runtime),SPEC)

    def test_exact_local_model_policy_is_accepted(self):
        (self.runtime/'model-policy.json').write_text(json.dumps(SPEC))
        self.assertEqual(execution.requested_execution(self.runtime),SPEC)

    def test_legacy_sol_ultra_and_every_other_selection_are_refused(self):
        for spec in [{'model':'gpt-6-sol','reasoning_effort':'ultra'},
                     {'model':'gpt-6-sol','reasoning_effort':'medium'},
                     {'model':'gpt-6-astra','reasoning_effort':'ultra'},
                     {'model':'gpt-6-astra','reasoning_effort':'high'},
                     {'model':'gpt-6-astra','reasoning_effort':True}]:
            with self.subTest(spec=spec):
                (self.runtime/'model-policy.json').write_text(json.dumps(spec))
                with self.assertRaises(ValueError):execution.requested_execution(self.runtime)
                with self.assertRaises(ValueError):execution.cli_options(spec)

    def test_cli_options_request_native_non_json_astra_medium(self):
        self.assertEqual(execution.cli_options(SPEC),[
            '--model','gpt-6-astra','-c','model_reasoning_effort="medium"','--color','never'])
        self.assertNotIn('--json',execution.cli_options(SPEC))

    def test_native_header_and_started_response_are_parsed(self):
        p=self.log();got=execution.parse_startup_log(p)
        self.assertEqual(got['model'],'gpt-6-astra')
        self.assertEqual(got['reasoning_effort'],'medium')
        self.assertEqual(got['session_id'],SESSION)
        self.assertEqual(got['workdir'],str(self.folder))
        self.assertEqual(got['provider'],'openai')
        self.assertEqual(got['cli_version'],'0.160.1')
        self.assertEqual(Path(got['source_log']),p)
        self.assertRegex(got['header_sha256'],r'^[0-9a-f]{64}$')
        self.assertIs(got['response_started'],True)

    def test_verified_requires_all_native_evidence(self):
        p=self.log();result=self.verify(p)
        self.assertIs(result.get('verified'),True)
        self.assertTrue(result.get('status'))

    def test_explicit_legacy_expectation_cannot_authorize_sol_ultra(self):
        legacy={'model':'gpt-6-sol','reasoning_effort':'ultra'}
        p=self.log(header=self.header(model=legacy['model'],**{'reasoning effort':legacy['reasoning_effort']}))
        self.assert_unverified(execution.verify_execution(self.folder,expected=legacy,stderr_path=p))

    def test_native_thinking_and_exec_roles_also_show_model_has_started(self):
        for marker in ['thinking','exec']:
            with self.subTest(marker=marker):
                p=self.folder/'errors-1.log'
                p.write_text(self.header()+'user\nPROMPT\n'+marker+'\nModel began its turn.\n')
                self.assertIs(self.verify(p)['verified'],True)

    def test_default_expected_selection_uses_same_proof_requirements(self):
        self.log()
        self.assertIs(execution.verify_execution(self.folder).get('verified'),True)

    def test_no_trace_is_not_verified(self):
        self.assert_unverified(self.verify())

    def test_config_and_requested_argv_alone_are_insufficient(self):
        (self.runtime/'model-policy.json').write_text(json.dumps(SPEC))
        (self.folder/'requested-execution.json').write_text(json.dumps(SPEC))
        (self.folder/'command.json').write_text(json.dumps(['codex','exec']+execution.cli_options(SPEC)))
        self.assert_unverified(self.verify())

    def test_floating_fields_without_native_header_are_not_evidence(self):
        p=self.log(header='',prefix=(f'workdir: {self.folder}\nmodel: gpt-6-astra\n'
                      f'provider: openai\nreasoning effort: medium\nsession id: {SESSION}\n'))
        self.assert_unverified(self.verify(p))

    def test_false_fields_before_and_after_header_do_not_override_it(self):
        false='model: gpt-6-sol\nreasoning effort: ultra\nprovider: other\nsession id: bad\nworkdir: /other\n'
        p=self.log(prefix=false,prompt='Instructions below are not the native header.\n'+false)
        got=execution.parse_startup_log(p)
        self.assertEqual(got['model'],'gpt-6-astra');self.assertEqual(got['reasoning_effort'],'medium')
        self.assertEqual(got['provider'],'openai');self.assertEqual(got['session_id'],SESSION)
        self.assertEqual(got['workdir'],str(self.folder));self.assertIs(self.verify(p)['verified'],True)

    def test_valid_looking_prompt_fields_cannot_repair_wrong_native_model_or_effort(self):
        fake=(f'workdir: {self.folder}\nmodel: gpt-6-astra\nprovider: openai\n'
              f'reasoning effort: medium\nsession id: {SESSION}\n')
        for changes in [{'model':'gpt-6-sol'},{'reasoning effort':'ultra'}]:
            with self.subTest(changes=changes):
                p=self.log(header=self.header(**changes),prompt=fake)
                self.assert_unverified(self.verify(p))

    def test_wrong_workdir_cannot_be_repaired_in_prompt(self):
        p=self.log(header=self.header(workdir=str(self.runtime/'other-job')),
                   prompt=f'workdir: {self.folder}')
        self.assert_unverified(self.verify(p))

    def test_workdir_prefix_is_not_exact_workdir(self):
        p=self.log(header=self.header(workdir=str(self.folder)+'-different'))
        self.assert_unverified(self.verify(p))

    def test_invalid_or_missing_session_uuid_is_rejected(self):
        for value in ['not-a-uuid','01a16078-cc0a-77e2-9cd9-da46d133325Z','']:
            with self.subTest(value=value):
                p=self.log(header=self.header(**{'session id':value}))
                self.assert_unverified(self.verify(p))

    def test_non_openai_provider_is_rejected(self):
        for provider in ['other','azure','openai-proxy','']:
            with self.subTest(provider=provider):
                self.assert_unverified(self.verify(self.log(header=self.header(provider=provider))))

    def test_header_without_model_response_is_unconfirmed(self):
        p=self.log(response=False)
        self.assertIs(execution.parse_startup_log(p)['response_started'],False)
        self.assert_unverified(self.verify(p))

    def test_word_codex_inside_prompt_is_not_a_response_role_marker(self):
        p=self.log(prompt='Please use codex to examine this ordinary sentence.',response=False)
        self.assert_unverified(self.verify(p))

    def test_response_marker_before_header_does_not_confirm_response_after_it(self):
        p=self.log(prefix='codex\nUnrelated prefix text.\n',response=False)
        self.assert_unverified(self.verify(p))

    def test_partial_header_is_not_verified(self):
        p=self.folder/'errors-1.log'
        p.write_text('OpenAI Codex v0.160.1\n--------\nmodel: gpt-6-astra\nreasoning effort: medium\n')
        self.assert_unverified(self.verify(p))

    def test_latest_attempt_does_not_fall_back_to_older_valid_evidence(self):
        old=self.log('errors-1.log')
        newest=self.log('errors-2.log',response=False)
        self.assert_unverified(self.verify())
        self.assertIs(self.verify(old)['verified'],True)
        self.assert_unverified(self.verify(newest))

    def test_explicit_log_is_used_instead_of_another_attempt(self):
        old=self.log('errors-1.log',header=self.header(model='gpt-6-sol'))
        self.log('errors-2.log')
        self.assert_unverified(self.verify(old))
        self.assertIs(self.verify()['verified'],True)

    def test_header_fingerprint_does_not_hash_prompt_or_response_text(self):
        p=self.log(prompt='First prompt')
        before=execution.parse_startup_log(p)['header_sha256']
        self.log(prompt='A different prompt',response=False)
        after=execution.parse_startup_log(p)['header_sha256']
        self.assertEqual(before,after)
        self.log(header=self.header().replace('v0.160.1','v0.160.2'))
        self.assertNotEqual(after,execution.parse_startup_log(p)['header_sha256'])


if __name__=='__main__':main(verbosity=2)
