"""Build and check a coherent working edition; optionally publish existing sites.

An edition with unprocessed articles never claims exhaustive rewriting.
"""
from pathlib import Path
from contextlib import redirect_stdout
import argparse,errno,fcntl,json,os,re,subprocess,sys,time
from ingest import HERE,open_db
from register_batches import register

PROJECTS={
    'liberer-la-retraite':'prj_9PB01NleDnTt1V2QqsH8gwRrHIPb',
    'nouveaudroitdutravail':'prj_zahNFYxGRdJXSMA8mbNwl4POToxM',
    'liberer-le-revenu':'prj_FY6QVdGPCjjfSnDG6j7Z1UL3yC6g',
    'liberer-lentreprise':'prj_jWrUP6fckXn68VHV08S6NtVD0cPQ',
    'liberer-le-logement':'prj_t5M7thvfbgoLQpQkHp1GSnzPsqC3',
}


DEPLOYMENT_PENDING_EXIT=20
PUBLICATION_BUSY_EXIT=21
NETWORK_ERROR=re.compile(r'\b(?:ETIMEDOUT|ECONNRESET|EPIPE|EAI_AGAIN|ENETUNREACH|EHOSTUNREACH|ECONNREFUSED)\b|socket hang up|(?:HTTP|status(?: code)?)\s*[:=]?\s*(?:502|503|504)\b|FetchError: invalid json response body at https://api\.vercel\.com/[^\n]*"Internal S',re.I)

def deployment_environment():
    """Select a publication-only Node runtime; preserve transport security."""
    env=os.environ.copy()
    if env.get('NODE_TLS_REJECT_UNAUTHORIZED')=='0':
        raise ValueError('TLS certificate verification must remain enabled')
    config=HERE/'publication-runtime.json'
    if config.exists():
        value=json.loads(config.read_text())
        folder=Path(value['node_bin_directory'])
        if not folder.is_absolute() or not (folder/'node').is_file() or not os.access(folder/'node',os.X_OK):
            raise ValueError('Configured publication Node runtime is unavailable')
        env['PATH']=str(folder)+os.pathsep+env.get('PATH','')
    return env

def save_report(runtime,report):
    report['updated_at_unix']=int(time.time())
    temporary=runtime/'publication.json.tmp'
    temporary.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    temporary.replace(runtime/'publication.json')

def publish(deploy=False):
    runtime=HERE/'runtime';runtime.mkdir(exist_ok=True)
    with (runtime/'publication.lock').open('a') as lock:
        try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            # Coalesce overlapping requests; never queue another full validation
            # or overwrite the report owned by the active publisher.
            report={'status':'publication_in_progress','publication_pending':True,
                    'all_sites_published':False,'local_checks_passed':False}
            print(json.dumps(report));return report
        prior=json.loads((runtime/'publication.json').read_text()) if (runtime/'publication.json').exists() else {}
        report={'updated_at_unix':int(time.time()),'exhaustive_rewriting_complete':False,
                'local_checks_passed':False,'deployment_requested':deploy,
                'publication_pending':bool(prior.get('publication_pending')),
                'all_sites_published':False,'status':'validating_local',
                'deployments':{slug:{'published':False,'status':'not_attempted','attempts':[]} for slug in PROJECTS} if deploy else {}}
        save_report(runtime,report)
        stage='corpus_validation'
        try:
            db=open_db(HERE/'corpus.sqlite')
            try:
                with (runtime/'publication-validation.json').open('w') as log,redirect_stdout(log):register(db,HERE/'batches',False)
            finally:db.close()
            for name in ['build_reader.py','build_downloads.py','build_compact_sites.py','check_downloads.py']:
                stage=name
                with (runtime/(name+'.log')).open('w') as output:
                    subprocess.run([sys.executable,str(HERE/name)],cwd=HERE.parent,stdout=output,stderr=subprocess.STDOUT,check=True)
            stage='local_manifest'
            manifest=json.loads((HERE.parent/'sites/liberer-la-retraite/dist/downloads/manifest.json').read_text())
            report.update(drafted_articles=manifest['drafted_articles'],source_records=manifest['source_records'],local_checks_passed=True)
            if deploy:
                stage='destination_validation'
                deployment_env=deployment_environment()
                for slug,project in PROJECTS.items():
                    folder=HERE.parent/'sites'/slug/'dist'
                    linked=json.loads((folder/'.vercel/project.json').read_text())
                    if linked.get('projectId')!=project or linked.get('orgId')!='team_m7zLS15LnoyaB6RyJ0zKsHYj':raise ValueError('Vercel project mismatch: '+slug)
        except Exception as error:
            report.update(status='local_validation_failed',failure_stage=stage,failure_type=type(error).__name__)
            save_report(runtime,report)
            raise
        report['status']='publication_pending' if deploy else 'local_ready'
        if deploy:report['publication_pending']=True
        save_report(runtime,report)
        if deploy:
            for slug in PROJECTS:
                folder=HERE.parent/'sites'/slug/'dist';item=report['deployments'][slug]
                for attempt in range(1,4):
                    log_name=f'deploy-{slug}-attempt{attempt}.log'
                    item['status']='attempting';save_report(runtime,report)
                    transient=False;returncode=None;failure_type=None
                    try:
                        with (runtime/log_name).open('w') as output:
                            command=['vercel','deploy','--prod','--yes','--scope','personal-9062d8ea']
                            # Vercel's supported archive transport preserves the validated
                            # files while avoiding repeated large individual-file uploads.
                            if slug=='liberer-la-retraite':command.append('--archive=tgz')
                            result=subprocess.run(command,cwd=folder,stdout=output,stderr=subprocess.STDOUT,check=False,timeout=900,env=deployment_env)
                        returncode=result.returncode
                        if returncode:transient=bool(NETWORK_ERROR.search((runtime/log_name).read_text(errors='replace')))
                    except subprocess.TimeoutExpired:
                        transient=True;failure_type='TimeoutExpired'
                    except OSError as error:
                        transient=error.errno in {errno.ETIMEDOUT,errno.ECONNRESET,errno.ENETUNREACH,errno.EHOSTUNREACH,errno.ECONNREFUSED}
                        failure_type=type(error).__name__
                    item['attempts'].append({'attempt':attempt,'returncode':returncode,'transient_network_error':transient,'failure_type':failure_type,'log':'runtime/'+log_name})
                    item['published']=returncode==0
                    item['status']='published' if item['published'] else 'retrying' if transient and attempt<3 else 'failed'
                    save_report(runtime,report)
                    if item['published'] or not transient:break
                    if attempt<3:time.sleep(2*attempt)
            report['all_sites_published']=all(item['published'] for item in report['deployments'].values())
            report['publication_pending']=not report['all_sites_published']
            report['status']='published' if report['all_sites_published'] else 'publication_pending'
            save_report(runtime,report)
            if report['all_sites_published']:
                temporary=runtime/'last-published.json.tmp'
                temporary.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
                temporary.replace(runtime/'last-published.json')
        save_report(runtime,report)
        print(json.dumps(report,ensure_ascii=False,indent=2));return report

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--deploy',action='store_true');args=parser.parse_args()
    try:report=publish(args.deploy)
    except Exception:
        # The report names the failed stage; raw CLI/auth output stays in logs.
        print('Local publication checks failed; see runtime/publication.json.',file=sys.stderr)
        return 1
    if report['status']=='publication_in_progress':return PUBLICATION_BUSY_EXIT
    return DEPLOYMENT_PENDING_EXIT if args.deploy and report['publication_pending'] else 0

if __name__=='__main__':raise SystemExit(main())
