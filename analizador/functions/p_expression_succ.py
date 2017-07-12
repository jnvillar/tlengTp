import SuccExpr

def p_expression_succ(p):
    'expression : SUCC OPENPARENTHESIS expression CLOSEPARENTHESIS'
    p[0] = SuccExpr(p[3])
    
    
