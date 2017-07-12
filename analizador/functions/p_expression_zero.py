def p_expression_zero(p):
    'expression : ZERO'
    p[0] = ZeroExpr()