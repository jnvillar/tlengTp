from Tipo import *

g_count = 0

class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprIzq = expr1
        self.exprDer = expr2
        self.type = None
        self.initialExpression = False
        self.value = self
        self.defined = False
        self.name = None

    def evaluate(self, context, value=None):
        if self.value != self:
            self.value.evaluate(context)
        else:
            self.evaluateExpr(context)

        

        
    def evaluateExpr(self, context, value=None):
        self.exprIzq.evaluate(context)
        self.exprDer.evaluate(context)
        valIzq = self.exprIzq.getValue()
        valDer = self.exprDer.getValue()
        if not (valDer.__class__.__name__ == 'VarExpr' and valDer.getValue() == valDer) and not (valIzq.__class__.__name__ == 'VarExpr' and valIzq.getValue() == valIzq):
            context[self.exprIzq.getValue().getName()] = valDer
            self.defined = True
            self.exprIzq.getValue().evaluate(context)
            self.value = self.exprIzq.getValue()


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
        return self.value


    def getName(self):
        return self.name
        #return self.value.getName()

    def isDefined(self):
        return self.defined

