import sys


s = lambda x: x+1
pred = lambda x: max(0,x-1)
iden = lambda x: x
iden2 = lambda x: x
app = lambda x,y: x(y)
ifs = lambda x,y,z: y if x else z


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
        elif(self.valor == iden2):
            return '('+str(self.hijo1)+') '+str(self.hijo2)
        elif(str(self.tipo) == 'Nat'):
            return imprimirNat(self.valor)
        elif(str(self.tipo) == 'nada'):
            return ''
        return str(self.valor).lower()

    def evaluate(self, valor, var):
        # if(self.hijo1 != None and self.hijo1.valor == var):
        #     e = Element(valor)
        #     t = Tipo('Nat')
        #     e.tipo = t
        #     self.hijo1 = e
        # if(self.estaDefinido):
        #     return self.valor
        # if(self.hijo1 != None and esFuncion(self.hijo1)):
        #     return self.valor(self.hijo1.evaluate(valor, var))
        # if(self.hijo1 != None):
        #     valHijo = self.hijo1.evaluate(valor, var)
        #     if(type(valHijo) is str):
        #         return self.valor
        #     return self.valor(self.hijo1.evaluate(valor, var))
        # return self.valor(valor)

        if(self.hijo1 != None and self.hijo1.valor == var):
            e = Element(valor)
            t = Tipo('Nat')
            e.tipo = t
            self.hijo1 = e
        elif(self.hijo1 != None):
            self.hijo1.evaluate(valor,var)



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
		
