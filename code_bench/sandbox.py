"""Container execution adapter.
Run candidate code in a dedicated locked-down Docker container in production.
The adapter returns normalized observations consumed by evaluator.py.
"""
import subprocess, tempfile, time

def docker_run(code, stdin='', timeout_s=2, image='python:3.11-slim'):
    with tempfile.TemporaryDirectory() as d:
        open(f'{d}/candidate.py','w').write(code)
        cmd=['docker','run','--rm','--network','none','--read-only','--memory','128m','--cpus','0.5','--pids-limit','32','-i','-v',f'{d}:/work:ro',image,'python','/work/candidate.py']
        st=time.perf_counter()
        try:
            p=subprocess.run(cmd,input=stdin,text=True,capture_output=True,timeout=timeout_s)
            return {'status':'ok' if p.returncode==0 else 'runtime_error','actual':p.stdout,'stderr':p.stderr,'elapsed_ms':(time.perf_counter()-st)*1000}
        except subprocess.TimeoutExpired:
            return {'status':'timeout','actual':'','stderr':'','elapsed_ms':(time.perf_counter()-st)*1000}
