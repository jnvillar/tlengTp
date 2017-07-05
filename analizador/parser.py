"""Parser LR(1) del tp."""
import ply.yacc as yacc
import sys
from .lexer import tokens

precedence = []

s = lambda x: x+1
pred = lambda x: max(0,x-1)
iden = lambda x: x
app = lambda x,y: x(y)
ifs = lambda x,y,z: y if x else z
debug = True

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
    if(debug): print('p_expression_if_then_else')
    e = Element()
    
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
    e = Element()
    e.valor = p[1]
    t = Tipo('Var')
    e.tipo = t
    e.estaDefinido = False
    e.error = "El termino no es cerrado (" + p[1] + " esta libre)"
    p[0] = e

def p_expression_lambda(p):
    'expression : BACKSLASH expression 2DOTS funcionType DOT expression'
    if(debug): print('p_expression_lambda')
    e = Element()
    img = p[4].tipo.dom
    if(p[4].tipo.img != None):
        img = p[4].tipo.img
    if(img != p[6].tipo.dom and p[6].estaDefinido):
        e.error = 'ERROR: func espera un valor de tipo '+p[6].tipo.dom
    
    e.valor = iden
    t = Tipo(p[4].tipo, p[6].tipo)
    e.tipo = t    
    e.hijo1 = p[6]
    e.hijo2 = p[2]
    p[0] = e
    
def p_expression_application(p):
    'expression :  OPENPARENTHESIS expression CLOSEPARENTHESIS expression_values'
    if(debug): print('p_expression_application')

    e = Element()
    if (p[2].estaDefinido and p[4].estaDefinido):
        if(debug): print('3')
        if (p[2].error != None):
            e.error = p[2].error
        elif (p[4].error != None):
            e.error = p[2].error  
        else:
            if(p[2].tipo.img == None or str(p[2].tipo.dom) != str(p[2].tipo)):
                e.error = 'ERROR: La parte izquierda de la aplicacion (' + str(p[2]) + ') no es una funcion con dominio en ' + str(p[4].tipo)
        if(e.error == None):
            if(debug): print('1')  
            e.valor = p[2].evaluate(p[4].valor)
            e.tipo.dom = p[2].tipo.img.dom
            e.tipo.img = p[2].tipo.img.img
    if(p[4].estaDefinido and p[4].valor == None):
        e.valor = iden
        e.tipo = p[2].tipo
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
            print >>sys.stderr, str(self.error)
            return ""
        if(self.valor == s):
            return 'succ('+str(self.hijo1)+')'
        elif(self.valor == pred):
            return 'pred('+str(self.hijo1)+')'
        elif(self.valor == iden):
            return '\\'+str(self.hijo2)+':'+ str(self.tipo.dom) +'.'+str(self.hijo1)
        elif(self.valor == ifs):
            return 'if '+str(self.hijo1)+' then '+str(self.hijo2)+' else '+str(self.hijo3)
        elif(str(self.tipo) == 'Nat'):
            return imprimirNat(self.valor)
        return str(self.valor).lower()

    def evaluate(self, valor):
        if(self.hijo1 != None and esFuncion(self.hijo1)):
            return self.valor(self.hijo1.evaluate(valor))
        return self.valor(valor)

class Tipo(object):
    def __init__(self, dom, img = None):
        self.dom = dom
        self.img = img

    def __str__(self):
        if (self.img == None):
            return str(self.dom)    
        else:
            return str(self.dom)+'->'+str(self.img)

def esFuncion(e):
    return e.valor == s or e.valor == pred

def imprimirNat(v):
    res = '0'
    for i in range(0,v):
        res = 'succ('+res+')'
    return res  
		