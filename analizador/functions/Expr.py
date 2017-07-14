from model import *

def p_expression_true(p):
	'expression : TRUE'
	p[0] = BooleanExpr(True)


def p_expression_false(p):
	'expression : FALSE'
	p[0] = BooleanExpr(False)



def p_expression_if_then_else(p):
    'expression : IF expression THEN expression ELSE expression %prec IF'
    p[0] = IfExpr(p[2], p[4], p[6])