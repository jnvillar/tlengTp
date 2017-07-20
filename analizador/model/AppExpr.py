from Tipo import *


class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprIzq = expr1
        self.exprDer = expr2
        self.type = None
        self.initialExpression = False
        self.value = None
        self.defined = False

    def evaluate(self, context, value=None):
        self.exprDer.evaluate(context)
        valDer = self.exprDer.getValue()
        self.exprIzq.evaluate(context, valDer)
        self.value = self.exprIzq.getValue()
        if(self.exprDer.getValue() in context or self.exprDer.__class__.__name__ != 'VarExpr'):
            self.defined = True

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
        
        self.type = self.exprIzq.getType().getImg()


    def getType(self):
        return self.type

    def getValue(self):
        if not self.defined:
            return self
        return self.value