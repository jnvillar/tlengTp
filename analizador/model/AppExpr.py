from Tipo import *

g_count = 0

class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprIzq = expr1
        self.exprDer = expr2
        self.type = None
        self.initialExpression = False
        self.value = None
        self.defined = False
        self.name = None

    def evaluate(self, context, value=None):
        global g_count
        count = g_count
        g_count = g_count+1
        self.exprIzq.evaluate(context)
        self.exprDer.evaluate(context)
        valDer = self.exprDer.getValue()
        if valDer != None:
            context[self.exprIzq.getName()] = valDer
            self.defined = True
            self.name = self.exprIzq.getName()
        print str(count)+". AppExpr - RightVal: "+str(valDer)
        
        print str(count)+". AppExpr - ExprLeft type: "+str(self.exprIzq.getValue().__class__.__name__)
        if self.exprIzq.getValue() != None:
            print str(count)+". AppExpr - ExprLeft type: "+str(self.exprIzq.getValue().getName())
        print str(count)+". AppExpr - ExprLeft Value before evaluate: "+str(self.exprIzq.getValue())
        print str(count)+". AppExpr - Name: "+str(self.exprIzq.getName())
        self.exprIzq.evaluate(context)
        self.value = self.exprIzq.getValue()
        print str(count)+". AppExpr - ExprLeft Value: "+str(self.value)
        #if(self.exprDer.getValue() in context or self.exprDer.__class__.__name__ != 'VarExpr' or self.exprDer.isDefined()):
        

    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = str(self.exprIzq) + " " + str(self.exprDer)
        else:
            toPrint = toPrint + str(self.exprIzq)

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)

        return toPrint


    def setExprTypes(self, context):
        self.exprDer.setExprTypes(context)
        self.exprIzq.setExprTypes(context)
        if self.exprIzq.getType().getImg() == None:
            raise Exception("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + str(self.exprDer.getType()))
        
        self.type = Tipo(self.exprIzq.getType().getImg().getDom(), self.exprIzq.getType().getImg().getImg())


    def getType(self):
        return self.type

    def getValue(self):
        if not self.defined:
            return self
        return self.value


    def getName(self):
        return self.name