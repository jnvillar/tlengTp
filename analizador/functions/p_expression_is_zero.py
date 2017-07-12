import IsZeroExpr

def p_expression_is_zero(p): 
    'expression : ISZERO OPENPARENTHESIS expression CLOSEPARENTHESIS'
    p[0] = IsZeroExpr(p[3])