import PredExpr

def p_expression_pred(p):
    'expression : PRED OPENPARENTHESIS expression CLOSEPARENTHESIS'
    p[0] = PredExpr(p[3])