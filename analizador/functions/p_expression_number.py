def p_expression_number(p):
    'expression : NUMBER'
    p[0] = NatExpr(p[1])