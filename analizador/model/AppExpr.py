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
        valIzq = self.exprIzq.getValue()
        valDer = self.exprDer.getValue()
        if valDer != None and valIzq != None:
            context[self.exprIzq.getValue().getName()] = valDer
            self.defined = True
            self.name = self.exprIzq.getName()
            self.exprIzq.getValue().evaluate(context)
            self.value = self.exprIzq.getValue()
        #print str(count)+". AppExpr - RightVal: "+str(valDer)
        #print str(count)+". AppExpr - ExprLeft Value before evaluate: "+str(self.exprIzq.getValue())
        #print str(count)+". AppExpr - ExprLeft Value: "+str(self.value)
        

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

    def isDefined(self):
        return self.defined

