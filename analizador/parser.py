"""Parser LR(1) del tp."""
import ply.yacc as yacc
import sys
from .lexer import tokens
from model import *

precedence = [ 
('left', 'LAMBDA'), 
('left', 'IF'),
('left', 'APP'),
               ]


debug = True

def p_expression_zero(p):
    'expression : ZERO'
    e = Element(0)
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e

def p_expression_true(p):
	'expression : TRUE'
	e = Element(True)
	t = Tipo('Bool')
	e.tipo = t
	p[0] = e

def p_expression_false(p):
	'expression : FALSE'
	#p[0] = BoolExpr(False)

	e = Element(False)
	t = Tipo('Bool')
	e.tipo = t
	p[0] = e

def p_expression_if_then_else(p):
    'expression : IF expression THEN expression ELSE expression %prec IF'

    #p[0] = IfExpression(p[2], p[4], p[6])



    if(debug): print('p_expression_if_then_else')
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

def p_expression_number(p):
    'expression : NUMBER'
    e = Element(p[1])
    t = Tipo('Nat')
    e.tipo = t
    p[0] = e


def p_expression_type(p):
    'funcionType : TYPE funcImg'
    e = Element()
    t = Tipo(p[1])
    if (p[2].tipo != None):
        t.img = p[2].tipo
    e.tipo = t
    p[0] = e

def p_expression_type_img(p):
    'funcImg : ARROW funcionType'
    e = Element()
    t = Tipo(p[2].tipo)
    e.tipo = t
    p[0] = e

def p_expression_type_img_empty(p):
    'funcImg : '
    e = Element()
    p[0] = e

def p_expression_pred(p):
    'expression : PRED OPENPARENTHESIS expression CLOSEPARENTHESIS'
    if(debug): print('p_expression_pred')

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
   
def p_expression_succ(p):
    'expression : SUCC OPENPARENTHESIS expression CLOSEPARENTHESIS'
    if(debug): print('p_expression_succ')
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


def p_expression_is_zero(p): 
    'expression : ISZERO OPENPARENTHESIS expression CLOSEPARENTHESIS'
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

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = VarExpr(p[1])


def p_expression_lambda(p):
    'expression : BACKSLASH expression 2DOTS funcionType DOT expression %prec LAMBDA'
    if(debug): print('p_expression_lambda')
    p[0] = LambdaExpr(p[2], p[4], p[6])
    
    
def p_expression_application(p):
    'expression :  OPENPARENTHESIS expression CLOSEPARENTHESIS'
    if(debug): print('p_expression_application')
    p[0] = p[2]


def p_expression_values(p):
    'expression_values : expression'
    if(debug): print('p_expression_values')
    p[0] = p[1]

def p_expression_values_empty(p):
    'expression_values : '
    if(debug): print('p_expression_values_empty')
    e = Element()
    t = Tipo("nada")
    e.tipo = t
    e.estaDefinido = False
    p[0] = e
    pass

def p_expression_application_function(p):
    'expression :  expression expression %prec APP'
    if(debug): print('p_expression_application_function')
    p[0] = AppExpr(p[1],p[2])
    

def p_error(p):
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
