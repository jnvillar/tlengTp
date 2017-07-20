"""Parser LR(1) del tp."""
import ply.yacc as yacc
from .lexer import tokens
from analizador.model import AppExpr
from analizador.model import IfExpr
from analizador.model import IsZeroExpr
from analizador.model import LambdaExpr
from analizador.model import NatExpr
from analizador.model import PredExpr
from analizador.model import SuccExpr
from analizador.model import Tipo
from analizador.model import VarExpr
from analizador.model import ZeroExpr
from analizador.model import BooleanExpr
from analizador.model import ParanthesisExpr


precedence = [
    ('left', 'LAMBDA'),
    ('left', 'IF'),
    ('left', 'APP'),
]


def p_expression_initial(p):
    'expression : expr'
    p[1].setExprTypes({})
    p[1].evaluate({})
    p[1].initialExpression = True
    p[0] = p[1]    

def p_expr_application_function(p):
    'expr :  expr expr %prec APP'
    p[0] = AppExpr.AppExpr(p[1],p[2])

def p_expr_parenthesis(p):
    'expr : OPENPARENTHESIS expr CLOSEPARENTHESIS'
    p[0] = ParanthesisExpr.ParanthesisExpr(p[2])

def p_expr_zero(p):
    'expr : ZERO'
    p[0] = ZeroExpr.ZeroExpr()

def p_expr_pred(p):
    'expr : PRED OPENPARENTHESIS expr CLOSEPARENTHESIS'
    p[0] = PredExpr.PredExpr(p[3])

def p_expr_succ(p):
    'expr : SUCC OPENPARENTHESIS expr CLOSEPARENTHESIS'
    p[0] = SuccExpr.SuccExpr(p[3])

def p_expr_is_zero(p):
    'expr : ISZERO OPENPARENTHESIS expr CLOSEPARENTHESIS'
    p[0] = IsZeroExpr.IsZeroExpr(p[3])

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = NatExpr.NatExpr(p[1])

def p_expr_true(p):
    'expr : TRUE'
    p[0] = BooleanExpr.BooleanExpr(True)

def p_expr_false(p):
    'expr : FALSE'
    p[0] = BooleanExpr.BooleanExpr(False)

def p_expr_if_then_else(p):
    'expr : IF expr THEN expr ELSE expr %prec IF'
    p[0] = IfExpr.IfExpr(p[2], p[4], p[6])

def p_expr_variable(p):
    'expr : VARIABLE'
    p[0] = VarExpr.VarExpr(p[1])

def p_expr_lambda(p):
    'expr : BACKSLASH expr 2DOTS funcionType DOT expr %prec LAMBDA'
    p[0] = LambdaExpr.LambdaExpr(p[2], p[4], p[6])



def p_expr_type(p):
    'funcionType : TYPE funcImg'
    p[0] = Tipo.Tipo(p[1], p[2])

def p_expr_type_img(p):
    'funcImg : ARROW funcionType'
    p[0] = Tipo.Tipo(p[2])

def p_expr_type_img_empty(p):
    'funcImg : '
    p[0] = Tipo.Tipo(None)


def p_error(p):
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)


def apply_parser(str):
    return parser.parse(str)
