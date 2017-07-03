"""Parser LR(1) del tp."""
import ply.yacc as yacc
from .lexer import tokens

precedence = []

s = lambda x: x+1

pred = lambda x: max(0,x-1)

iden = lambda x: x

ifs = lambda x,y,z: y if x else z


def p_expression_zero(p):
    'expression : ZERO'
    e = Element(0,'Nat')
    p[0] = e


def p_expression_true(p):
	'expression : TRUE'
	e = Element(True,'Bool')
	p[0] = e

def p_expression_false(p):
	'expression : FALSE'
	e = Element(False,'Bool')
	p[0] = e

def p_expression_if_then_else(p):
    'expression : IF expression THEN expression ELSE expression'
    e = Element()
    
    if (p[2].estaDefinido and p[4].estaDefinido and p[6].estaDefinido):
        if (p[2].error != None):
            e.error = p[2].error
        elif (p[4].error != None):
            e.error = p[2].error
        elif (p[6].error != None):
            e.error = p[2].error   
        else:        
            if(p[2].tipo != 'Bool'):
                e.error = 'ERROR: El if debe tener una condicion'
            if(p[4].tipo != p[6].tipo):
                e.error = 'ERROR: Las dos opciones del if deben tener el mismo tipo'
        if(e.error == None):    
            e.valor = ifs(p[2].valor, p[4].valor, p[6].valor)
            e.tipo = p[4].tipo
    else:
        e.valor = ifs
        e.hijo1 = p[2]
        e.hijo2 = p[4]
        e.hijo3 = p[6]

    p[0] = e

def p_expression_number(p):
    'expression : NUMBER'
    e = Element(p[1],'Nat')
    p[0] = e


def p_expression_type(p):
    'funcionType : TYPE'
    e = Element()
    e.tipo = p[1]
    p[0] = e

def p_expression_pred(p):
    'expression : PRED OPENPARENTHESIS expression CLOSEPARENTHESIS'
    
    e = Element()
    e.hijo1 = p[3]
    if (p[3].estaDefinido):
        if (p[3].tipo =='Nat'):
            e.valor = max(p[3].valor-1,0)
        else:
            e.error = "pred solo puede ser aplicada a naturales."
    else:
         e.valor = pred
         e.estaDefinido = False
    
    e.tipo = 'Nat'
    p[0] = e
   
def p_expression_succ(p):
    'expression : SUCC OPENPARENTHESIS expression CLOSEPARENTHESIS'
    e = Element()
    e.hijo1 = p[3]
    if (p[3].estaDefinido):
        if (p[3].tipo =='Nat'):
            e.valor = p[3].valor+1
        else:
            e.error = "succ solo puede ser aplicada a naturales."
    else:
         e.valor = s
         e.estaDefinido = False
    
    e.tipo = 'Nat'
    p[0] = e


def p_expression_is_zero(p): 
    'expression : ISZERO OPENPARENTHESIS expression CLOSEPARENTHESIS'
    e = Element()
    e.tipo = 'Bool'
    if p[3].estaDefinido:
        if (p[3].tipo =='Nat'):
            if(p[3].valor == 0):
                e.valor = True
            else:
                e.valor = False
        else:
            e.error = "iszero solo puede ser aplicada a naturales."    
    else:
        e.valor = False
        e.estaDefinido = False
    p[0] = e

def p_expression_variable(p):
    'expression : VARIABLE'
    e = Element()
    e.valor = p[1]
    e.tipo = 'Var'
    e.estaDefinido = False
    p[0] = e



def p_expression_lambda(p):
    'expression : BACKSLASH expression 2DOTS funcionType DOT expression'
    e = Element()
    e.tipo = 'Func'
    e.valor = iden
    e.tipo = p[4].tipo + '->' + p[6].tipo
    e.hijo1 = p[6]
    p[0] = e

    
def p_expression_application(p):
    'expression :  OPENPARENTHESIS expression CLOSEPARENTHESIS expression_values'
    e = Element()
    e.tipo = 'Func'
    if(p[4].valor == None):
        e.valor = iden
    else:
        e.valor = p[2].evaluate(p[4].valor)
    e.tipo = p[2].tipo.split('->')[1] 
    e.hijo1 = p[2]
    p[0] = e


def p_expression_values(p):
    'expression_values : expression'
    p[0] = p[1]

def p_expression_values_empty(p):
    'expression_values : '
    e = Element()
    p[0] = e
    pass

def p_error(p):
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)



class Element(object):
    def __init__(self, valor=None, tipo=None, hijo1=None):
        self.valor = valor
        self.tipo = tipo
        self.hijo1 = hijo1
        self.estaDefinido = True
        self.hijo2 = None
        self.hijo3 = None
        self.error = None

    def __str__(self):
        if(self.error != None):
            return str(self.error)
        if(self.valor == s):
            return 'succ('+str(self.hijo1)+'):'
        elif(self.valor == pred):
            return 'pred('+str(self.hijo1)+')'
        elif(self.valor == iden):
            tipo_aux = self.tipo.split('->')[0]
            return '\\x:'+ tipo_aux +'.'+str(self.hijo1)
        elif(self.valor == ifs):
            return 'if '+str(self.hijo1)+' then '+str(self.hijo2)+' else '+str(self.hijo3)
        return str(self.valor).lower()

    def evaluate(self, valor):
        if(self.hijo1 != None and esFuncion(self.hijo1)):
            return self.valor(self.hijo1.evaluate(valor))
        return self.valor(valor)
    


def esFuncion(e):
    return e.valor == s or e.valor == pred



		