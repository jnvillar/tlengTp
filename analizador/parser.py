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

'''
precedence = [
    ('left', 'LAMBDA'),
    ('left', 'IF'),
    ('left', 'APP'),
]
'''

precedence = [
    ('left', 'LAMBDA'),
    ('left', 'IF'),
]

'''
def p_expr_zero(p):
    'expr : ZERO'
    e = Element(0)
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e

def p_expr_true(p):
	'expr : TRUE'
	e = Element(True)
	t = Tipo('Bool')
	e.tipo = t
	p[0] = e

def p_expr_false(p):
	'expr : FALSE'
	#p[0] = BoolExpr(False)

	e = Element(False)
	t = Tipo('Bool')
	e.tipo = t
	p[0] = e

def p_expr_if_then_else(p):
    'expr : IF expr THEN expr ELSE expr %prec IF'

    #p[0] = IfExpression(p[2], p[4], p[6])



    if(debug): print('p_expr_if_then_else')
    e = Element()
    if(p[4].tipo.dom != 'Var'):
    	e.tipo = p[4].tipo
    elif(p[6].tipo.dom != 'Var'):
    	e.tipo = p[6].tipo
    else:
    	t = Tipo('Var')
    	e.tipo = t
    if (p[2].estaDefinido and p[4].estaDefinido and p[6].estaDefinido):
        if (p[2].error != None):
            e.error = p[2].error
        elif (p[4].error != None):
            e.error = p[2].error
        elif (p[6].error != None):
            e.error = p[2].error   
        else:        
            if(str(p[2].tipo) != 'Bool'):
                e.error = 'ERROR: El if debe tener una condicion'
            if(str(p[4].tipo) != str(p[6].tipo)):
                e.error = 'ERROR: Las dos opciones del if deben tener el mismo tipo'
        if(e.error == None):    
            e.valor = ifs(p[2].valor, p[4].valor, p[6].valor)
    else:
    	e.estaDefinido = False
        e.valor = ifs
        e.hijo1 = p[2]
        e.hijo2 = p[4]
        e.hijo3 = p[6]


    p[0] = e

def p_expr_number(p):
    'expr : NUMBER'
    e = Element(p[1])
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e


def p_expr_type(p):
    'funcionType : TYPE funcImg'
    e = Element()
    t = Tipo(p[1])
    if (p[2].tipo != None):
        t.img = p[2].tipo
    e.tipo = t
    p[0] = e

def p_expr_type_img(p):
    'funcImg : ARROW funcionType'
    e = Element()
    t = Tipo(p[2].tipo)
    e.tipo = t
    p[0] = e

def p_expr_type_img_empty(p):
    'funcImg : '
    e = Element()
    p[0] = e

def p_expr_pred(p):
    'expr : PRED OPENPARENTHESIS expr CLOSEPARENTHESIS'
    if(debug): print('p_expr_pred')

    e = Element()
    e.hijo1 = p[3]
    if (p[3].estaDefinido):
        if (str(p[3].tipo) =='Nat'):
            e.valor = max(p[3].valor-1,0)
        else:
            e.error = "ERROR: pred espera un valor de tipo Nat"
    else:
         e.valor = pred
         e.estaDefinido = False
    
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e
   
def p_expr_succ(p):
    'expr : SUCC OPENPARENTHESIS expr CLOSEPARENTHESIS'
    if(debug): print('p_expr_succ')
    e = Element()
    e.hijo1 = p[3]
    if (p[3].estaDefinido):
    	e.estaDefinido = True
        if (str(p[3].tipo) =='Nat'):
            e.valor = p[3].valor+1

        else:
            e.error = "ERROR: succ espera un valor de tipo Nat"
    else:
         e.valor = s
         e.estaDefinido = False
    
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e


def p_expr_is_zero(p): 
    'expr : ISZERO OPENPARENTHESIS expr CLOSEPARENTHESIS'
    e = Element()
    t = Tipo('Bool')
    e.tipo = t
    if p[3].estaDefinido:
        if (str(p[3].tipo) =='Nat'):
            if(p[3].valor == 0):
                e.valor = True
            else:
                e.valor = False
        else:
            e.error = "ERROR: iszero espera un valor de tipo Nat"
    else:
        e.valor = False
        e.estaDefinido = False
    p[0] = e





    
    
def p_expr_application(p):
    'expr :  OPENPARENTHESIS expr CLOSEPARENTHESIS'
    if(debug): print('p_expr_application')
    p[0] = p[2]


def p_expr_values(p):
    'expr_values : expr'
    if(debug): print('p_expr_values')
    p[0] = p[1]

def p_expr_values_empty(p):
    'expr_values : '
    if(debug): print('p_expr_values_empty')
    e = Element()
    t = Tipo("nada")
    e.tipo = t
    e.estaDefinido = False
    p[0] = e
    pass

'''

'''
def p_expr_application_function(p):
    'expr :  expr expr %prec APP'
    if(debug): print('p_expr_application_function')
    p[0] = AppExpr.AppExpr(p[1],p[2])
'''


def p_expression_initial(p):
    'expression : expr'
    p[1].setExprTypes({})
    p[1].evaluate({})
    p[1].initialExpression = True
    p[0] = p[1]    

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
    p[0] = Tipo.Tipo(p[1], str(p[2]))

def p_expr_type_img(p):
    'funcImg : ARROW funcionType'
    p[0] = Tipo.Tipo(str(p[2]))

def p_expr_type_img_empty(p):
    'funcImg : '
    p[0] = Tipo.Tipo()


def p_error(p):
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)


def apply_parser(str):
    return parser.parse(str)
