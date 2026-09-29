import ast, difflib

def syntax_check(code):
    try: ast.parse(code); return {'ok': True, 'error': None}
    except SyntaxError as e: return {'ok': False, 'error': str(e)}

def score_case(expected, actual, status='ok'):
    e,a=expected.strip(),actual.strip()
    return {'passed': status=='ok' and e==a, 'status':status,
            'diff':'\n'.join(difflib.unified_diff(e.splitlines(),a.splitlines(),fromfile='expected',tofile='actual',lineterm=''))}

def style_score(code):
    issues=[]
    for n,line in enumerate(code.splitlines(),1):
        if len(line)>88: issues.append(f'line {n}: >88 chars')
        if '\t' in line: issues.append(f'line {n}: tab indentation')
    return {'score':max(0,100-10*len(issues)),'issues':issues}

def scorecard(code, observations):
    syntax=syntax_check(code); rows=[dict(o,**score_case(o['expected'],o.get('actual',''),o.get('status','ok'))) for o in observations]
    edges=[r for r in rows if r.get('edge')]
    return {'syntax':syntax,'pass_rate':sum(r['passed'] for r in rows)/max(1,len(rows)),
            'edge_case_pass_rate':sum(r['passed'] for r in edges)/max(1,len(edges)) if edges else 1.0,
            'style':style_score(code),'results':rows}
