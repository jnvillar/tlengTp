"""Parser LR(1) del tp."""
import ply.yacc as yacc
from .lexer import tokens

precedence = []

def p_expression_zero(p):
    'expression : ZERO'
    p[0] = 0

def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

def p_expression_if_then_else(p):
    'expression : IF expression THEN expression ELSE expression'
    if p[2]:
        p[0] = p[4]
    else:
        p[0] = p[6]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_pred(p):
    'expression : PRED OPENPARENTHESIS expression CLOSEPARENTHESIS'
    res = p[3]-1
    if res < 0:
        p[0] = 0
    else:
        p[0] = res
   
def p_expression_succ(p):
    'expression : SUCC OPENPARENTHESIS expression CLOSEPARENTHESIS'
    p[0] = p[3]+1

def p_expression_is_zero(p): 
    'expression : ISZERO OPENPARENTHESIS expression CLOSEPARENTHESIS'
    if p[3] == 0:
        p[0] = True
    else:
        p[0] = False

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0].value = p[0].variableValue

def p_expression_lambda(p):
    'expression : BACKSLASH VARIABLE 2DOTS expression DOT expression'
    p[4].variableValue = p[0].variableValue

def p_expression_lambda_number(p):
    'expression : expression expresion'
    p[1].variableValue = p[2]

def p_error(p):
    print("Hubo un error en el parseo.")
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)