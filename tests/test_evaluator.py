from code_bench.evaluator import *
def test_syntax(): assert not syntax_check('def x(')['ok']
def test_wrong_output(): assert not score_case('4','3')['passed']
def test_diff(): assert 'expected' in score_case('4','3')['diff']
def test_scorecard_edges():
 r=scorecard('print(1)',[{'expected':'1','actual':'1','edge':False},{'expected':'0','actual':'0','edge':True}]);assert r['pass_rate']==1 and r['edge_case_pass_rate']==1
def test_style(): assert style_score('x=1')['score']==100
